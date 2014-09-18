#!/bin/bash

if [ -d "$1" ]; then
    echo "output will be redirected to /usr/share/gnome-background-properties/user_wallpapers.xml"
    src/main.py $1 > /usr/share/gnome-background-properties/user_wallpapers.xml
else
    echo "usage: ./run.sh wallpaper_path"
fi
