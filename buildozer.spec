[app]

# (str) Title of your application
title = GPS MQTT Sender

# (str) Package name
package.name = gpsmqtt

# (str) Package domain (must be unique)
package.domain = org.example

# (str) Source code where main.py is located
source.dir = .

# (str) The main .py file to execute
source.main = main.py

# (list) Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, ACCESS_BACKGROUND_LOCATION

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Application requirements
requirements = python3,kivy,plyer,paho-mqtt

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon (optional)
# icon.filename = %(source.dir)s/data/icon.png

# (int) Target API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 27

# (int) Android SDK version to use
android.sdk = 33

# (int) Android NDK version
android.ndk = 25b

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Application versioning
version = 1.0

# (str) Package format (aab = Play Store upload, apk = direct install)
android.release_artifact = apk

# (str) Logcat filters to show
logcat_filters = *:S python:D ActivityManager:I

# (bool) Ask for permissions on runtime (required for Android 6+)
android.accept_sdk_license = True

# (bool) Enable Android logcat
log_level = 2

# (bool) Include source in apk
copy_libs = 1

# (list) Permissions you want to request manually
android.init_permissions = True

# (str) Gradle build mode
android.gradle_dependencies =

# (str) Custom command before build
# (useful to check MQTT broker or GPS availability)
# before_build = python3 check_environment.py

# (bool) Indicate whether the app should request the GPS at start
android.presplash_color = #000000

# (list) Patterns to exclude from the APK
exclude_patterns = tests, bin, __pycache__

# (str) Entry point of the app
entrypoint = main.py


[buildozer]

# (str) Directory to store the build artifacts
build_dir = build

# (str) Log level (0 = minimal, 2 = verbose)
log_level = 2

# (bool) Run logcat automatically after installation
logcat_preserve_log = True

# (bool) Automatically accept SDK licenses
accept_android_license = True

# (str) Configuration of packaging tool
warn_on_root = 1

