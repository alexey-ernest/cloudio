"""
Scans all of your music and uploads it to the cloud.
"""

from os import walk, path
import sys
import platform

PATH = r'c:/' if platform.system().lower().startswith('Windows') else r'/'
EXTENSIONS = {'mp3', 'm4a'}
EXCLUDE_DIRS = {
    # windows
    r'c:/windows',
    r'c:/program files',

    # mac os
    r'/applications',
    r'/library',
    r'/system/library',
    r'/private'
}

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

    for dirpath, dirnames, filenames in walk(path_name):
        # skip system dirs
        if dirpath.lower() in EXCLUDE_DIRS:
            dirnames[:] = []
            continue

        # filter music files
        music_files = [f for f in filenames if path.splitext(f)[1][1:] in EXTENSIONS]
        for music_filename in music_files:
            yield path.join(dirpath, music_filename)

if __name__ == '__main__':
    main()
