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
android.api = 30
android.minapi = 21
android.ndk = 25b
android.sdk = 30
android.build_tools = 30.0.3
android.private_storage = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
