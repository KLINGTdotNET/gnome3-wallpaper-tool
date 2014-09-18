#!/bin/bash

OUTFILE="/usr/share/gnome-background-properties/${USER}_wallpapers.xml"

if [ -d "$1" ]; then
    echo "output will be redirected to $OUTFILE"
    src/main.py $1 > $OUTFILE
else
    echo "usage: ./run.sh wallpaper_path"
fi
