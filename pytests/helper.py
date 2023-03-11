import os
from glob import glob
import subprocess
from sys import stderr
import tempfile

PROJECT_PATH = os.environ.get('PROJECT_PATH', '../grader/project')
# Make tilde in path work:
PROJECT_PATH = os.path.expanduser(PROJECT_PATH)

REPORT = os.environ.get('REPORT', '0')


def report(paths: list[str]):
    print(REPORT, file=stderr)
    if REPORT == '1':
        # just to be on a safe side convert every path to absolute
        paths = [os.path.abspath(path) for path in paths]
        subprocess.run("code -n -w " + " ".join(paths), shell=True)


def report_file(recipe, *args, **kwargs):
    if REPORT == '1':
        with tempfile.NamedTemporaryFile(*args, **kwargs) as f:
            recipe(f.name)
            report([f.name])


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


def fd_input(prompt):
    # Based on https://github.com/pytest-dev/pytest/issues/5053#issuecomment-484921801
    with os.fdopen(os.dup(1), "w") as stdout:
        stdout.write("\n{}".format(prompt))

    with os.fdopen(os.dup(2), "r") as stdin:
        return stdin.readline()


if __name__ == '__main__':
    print("html files:")
    for path in get_html_paths():
        print(path)
    print("css files:")
    for path in get_css_paths():
        print(path)
