"""
Scans all of your music and uploads it to the cloud.
"""

from os import walk, path
import sys

PATH = r'c:/'

def main():
    """
    Entry point.
    """

    if len(sys.argv) > 1:
    	global PATH
        PATH = sys.argv[1]

    for filename in scan_path(PATH):
        print filename

def scan_path(path_name):
    """Scans path for music files.

    Args:
        path_name: directory path to scan.

    Returns:
        Yields music files as soon as found.
    """

    extensions = {'mp3', 'm4a'}

    for dirpath, dirnames, filenames in walk(path_name):
        music_files = [f for f in filenames if path.splitext(f)[1][1:] in extensions]
        for music_filename in music_files:
            yield path.join(dirpath, music_filename)

if __name__ == '__main__':
    main()
