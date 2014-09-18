#!/usr/bin/env python3

import argparse
import os.path
from pathlib import Path

def main():
    args = get_args()
    if(args.path):
        ok, path = check_path(args.path)
        if(ok):
            p = Path(path)
            known_extensions = ['.jpg', '.jpeg', '.png']
            filepaths = []
            for f in [f for f in p.iterdir() if f.is_file()]:
                _, ext = os.path.splitext(f._str)
                if(ext.lower() in known_extensions):
                    filepaths.append(f)
            if(filepaths):
                print_xml(filepaths)

def print_xml(filepaths):
    prefix='''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">
<wallpapers>'''
    template='''
    <wallpaper deleted="false">
        <name>{0}</name>
        <name xml:lang="en_GB">{0}</name>
        <filename>{1}</filename>
        <options>zoom</options>
        <pcolor>#ffffff</pcolor>
        <scolor>#000000</scolor>
    </wallpaper>'''
    postfix='</wallpapers>'
    print(prefix)
    for filepath in filepaths:
        name, _ = os.path.splitext(filepath.name)
        print(template.format(name, filepath._str))
    print(postfix)

def get_args():
    parser = argparse.ArgumentParser(description='Create a gnome3 background xml file')
    parser.add_argument('path', help='the path where your wallpapers are stored')
    return parser.parse_args()

def check_path(path):
    sanitized = os.path.expanduser(path)
    return os.path.isdir(sanitized), sanitized

if __name__ == '__main__':
    main()