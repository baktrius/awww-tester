import os
from glob import glob
import subprocess

PROJECT_PATH = os.environ.get('PROJECT_PATH', '../moje1')
# Make tilde in path work:
PROJECT_PATH = os.path.expanduser(PROJECT_PATH)

REPORT = os.environ.get('REPORT', '1')


def report(paths: list[str]):
    # just to be on a safe side convert every path to absolute
    paths = [os.path.abspath(path) for path in paths]
    if REPORT == '1':
        subprocess.run("code -r -w " + " ".join(paths), shell=True)


def get_by_ext(ext: str) -> list[str]:
    # Double star with a recursive flag is interpreted
    # as 0,1,2,... directories.
    pattern = os.path.join(PROJECT_PATH, f'**/*.{ext}')
    print(f'Globbing by pattern: {pattern}')
    return [os.path.abspath(path) for path in glob(pattern, recursive=True)]


def get_html_paths():
    return get_by_ext('html') + get_by_ext('htm')


def get_url():
    paths = get_html_paths()
    assert len(paths) >= 1
    return 'file://' + paths[0]


def get_css_paths():
    return get_by_ext('css')


def get_css_absolute_paths():
    return get_css_paths()


if __name__ == '__main__':
    print("html files:")
    for path in get_html_paths():
        print(path)
    print("css files:")
    for path in get_css_paths():
        print(path)
