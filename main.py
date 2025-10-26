import os
import platform
import random
import time
import json
import paho.mqtt.client as mqtt
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import StringProperty

# OpenGL-Backend anpassen (Vermeidung schwarzer Fenster)
os.environ["KIVY_GL_BACKEND"] = "sdl2"

ON_ANDROID = platform.system() == "Android"
if ON_ANDROID:
    from plyer import gps


class GPSWidget(BoxLayout):
    coords_text = StringProperty("Noch keine GPS-Daten erhalten.")
    time_text = StringProperty("Keine Übertragung erfolgt.")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.lbl_coords = Label(text=self.coords_text, font_size="18sp")
        self.lbl_time = Label(text=self.time_text, font_size="16sp")
        self.add_widget(self.lbl_coords)
        self.add_widget(self.lbl_time)

    def update_info(self, lat, lon):
        self.coords_text = f"Letzte Koordinaten:\nLatitude: {lat:.6f}\nLongitude: {lon:.6f}"
        self.time_text = f"Letzter Sendezeitpunkt: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        self.lbl_coords.text = self.coords_text
        self.lbl_time.text = self.time_text


class GPSMQTTApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widget = GPSWidget()
        self.mqtt_client = mqtt.Client()
        self.mqtt_host = "broker.hivemq.com"
        self.topic = "radiocaching/ff/search_teams/1/coordinates"
        self.last_lat = 48.5  # Frankfurt Startwert
        self.last_lon = 14.4

    def build(self):
        self.connect_mqtt()

        if ON_ANDROID:
            gps.configure(on_location=self.on_gps_location, on_status=self.on_gps_status)
            gps.start(minTime=10000, minDistance=1)
        else:
            Clock.schedule_interval(self.simulate_gps, 10)

        return self.widget

    def connect_mqtt(self):
        try:
            self.mqtt_client.connect(self.mqtt_host, 1883, 60)
            self.mqtt_client.loop_start()
        except Exception as e:
            self.widget.lbl_coords.text = f"MQTT-Verbindung fehlgeschlagen: {str(e)}"

    def on_gps_location(self, **kwargs):
        lat = kwargs.get('lat')
        lon = kwargs.get('lon')
        self.publish_location(lat, lon)

    def simulate_gps(self, dt):
        # Simuliert laufende Bewegung in kleinen Schritten
        self.last_lat += random.uniform(-0.0005, 0.0005)
        self.last_lon += random.uniform(-0.0005, 0.0005)
        self.publish_location(self.last_lat, self.last_lon)

    def publish_location(self, lat, lon):
        try:
            data = {
                "latitude": lat,
                "longitude": lon,
                "timestamp": time.time()
            }
            msg = json.dumps(data)
            self.mqtt_client.publish(self.topic, msg)
            self.widget.update_info(lat, lon)
        except Exception as e:
            self.widget.lbl_coords.text = f"Fehler bei Publish: {str(e)}"

    def on_gps_status(self, stype, status):
        self.widget.lbl_time.text = f"GPS-Status: {stype} = {status}"


if __name__ == '__main__':
    GPSMQTTApp().run()
