# A python script that creates a gnome3 wallpaper xml

## What's the problem?

In gnome3 you can't simply set a path that stores your wallpapers. A workaround is to save them in your *Pictures* folder root. But this is unsatisfactory because you have to clutter this folder with wallpapers, not a good way of organizing files.

## Solution

- gnome3 looks for special `xml` files that describe available wallpapers
- it's a stupid *no-brain job* to write them manually
- this python script iterates over the *jpeg* and *png* files in the folder you specified and outputs a corresponding wallpaper xml

## how to run

- `sudo -E ./run.sh wallpaper_path`
- `-E` preserves the user environment, so you can use the `~` in your wallpaper_path, f.e. `~/Dropbox/Wallpaper`