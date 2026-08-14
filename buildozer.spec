[app]

# (str) Title of your application
title = Vivarium Flora Fauna

# (str) Package name
package.name = vivariumflorafauna

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Fixado em python3==3.10.12 para evitar que o p4a tente usar Python 3.14 instavel
requirements = python3==3.10.12,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) Enables Android auto backup feature
android.allow_backup = True

# (bool) allow p4a to download/use prebuilt wheels
p4a.bootstrap = sdl2

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

[buildozer]

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output (APK, AAB, etc)
# bin_dir = ./bin
# (int) Target Android API
android.api = 33

# (int) Minimum API support
android.minapi = 24

# (str) Versao estavel do Build Tools (evita tentar baixar a v37 instavel)
android.build_tools_version = 33.0.2
