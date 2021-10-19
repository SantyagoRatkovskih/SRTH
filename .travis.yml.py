os: linux
dist: focal
language: python

python:
  - 3.8

install:
  - sudo apt -y install python3-distutils
  - sudo apt -y install python3-pip
  - sudo apt install -y git
  - git clone https://github.com/kivy/buildozer.git
  - python3 -m site
  - ls -l
  - cd buildozer
  - ls -l
  - python3 setup.py install
  - ls -l
  - cd ..
  - ls -l

  - sudo apt update
  - sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
  - pip3 install --upgrade Cython==0.29.19 virtualenv
  - export PATH=$PATH:~/.local/bin/
  - ls -l
  - echo "TODO COMPILE 32bit"
  - yes | buildozer android debug
  - ls -la
  - ls bin/ -l
  - gem install dpl --pre
  - dpl releases --token $GITHUB_TOKEN --file "bin/SRTH-0.1-armeabi-v7a-debug.apk" --tag_name "v.0.1"
  - echo "TODO COMPILE 64bit"
  - ls -l /home/travis/
  - ls -l /home/travis/build/SRTH/test/
  - ls -la
  - rm -r -f .buildozer
  - ls -la
  - rm -r -f /home/travis/build/SRTH/TEST/.buildozer
  - ls -l /home/travis/
  - ls -l /home/travis/build/SRTH/TEST/
  - ls -l
  - yes | cp -f buildozer-64bit.spec buildozer.spec
  - yes | buildozer android debug
  - ls -la
  - ls bin/ -l
  - echo "TODO"
  - gem install dpl --pre
  - dpl releases --token $GITHUB_TOKEN --file "bin/SRTH-1.0-arm64-v8a-debug.apk" --tag_name "v.0.1"
  - echo "OK"
