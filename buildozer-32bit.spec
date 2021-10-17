[app]

title = Mechanics Netbook

package.name = mechanicsnetbook

package.domain = org.santyagoratkovskih

source.dir =.

version = 1.0

requirements = python3,kivy==2.0.0,kivymd,https://github.com/kivymd/KivyMD/archive/3274d62.zip,sdl2_ttf==2.0.15

#presplash.filename = %(source.dir)s/data/logo/presplash512okmin.png

#icon.filename = %(source.dir)s/data/logo/logo512min.png

orientation = all

osx.python_version = 3

osx.kivy_version = 2.0.0

fullscreen = 0

android.arch = armeabi-v7a

android.allow_backup = True

ios.kivy_ios_url = https://github.com/kivy/kivy-ios

ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy

ios.ios_deploy_branch = 1.10.0

ios.codesign.allowed = false

[buildozer]

log_level = 2

warn_on_root = 1
