[app]
title = Gurujodi
package.name = gurujodi
package.domain = org.test
source.dir = .
# This includes your .ttf font files in the APK
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 0.1
# Added requirements for your Firebase and Kivy code
requirements = python3,kivy,requests,certifi,urllib3
orientation = portrait
fullscreen = 0
# Permission needed for Firebase database
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.accept_sdk_license = True
android.skip_update = True
android.archs = arm64-v8a
[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
