"""
Scans all of your music and uploads it to the cloud.
"""

from os import walk, path
import sys
import platform

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

def sync(dir_path):
    """
    Entry point.

    Args:
        dir_path: directory to scan.
    """

    for filename in _scan(dir_path):
        print filename

def _scan(dir_path):
    """Scans path for music files.

    Args:
        dir_path: directory path to scan.

    Returns:
        Yields music files as soon as found.
    """

    for dirpath, dirnames, filenames in walk(dir_path):
        # skip system dirs
        if dirpath.lower() in EXCLUDE_DIRS:
            dirnames[:] = []
            continue

        # filter music files
        music_files = [f for f in filenames if path.splitext(f)[1][1:] in EXTENSIONS]
        for music_filename in music_files:
            yield path.join(dirpath, music_filename)

if __name__ == '__main__':
    DIR_PATH = r'c:/' if platform.system().lower().startswith('Windows') else r'/'
    if len(sys.argv) > 1:
        DIR_PATH = sys.argv[1]
    sync(DIR_PATH)
