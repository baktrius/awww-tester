import os
from glob import glob

PROJECT_PATH = os.environ.get('PROJECT_PATH', '../moje1')
# Make tilde in path work:
PROJECT_PATH = os.path.expanduser(PROJECT_PATH)

def get_by_ext(ext: str) -> list[str]:
    # Double star with a recursive flag is interpreted
    # as 0,1,2,... directories.
    pattern = os.path.join(PROJECT_PATH, f'**/*.{ext}')
    print(f'Globbing by pattern: {pattern}')
    return glob(pattern, recursive=True)

def get_html_paths():
    return get_by_ext('html') + get_by_ext('htm')

# TODO: possible index out of bound
def get_url():
    return 'file://' + os.path.abspath(get_html_paths()[0])


def get_css_paths():
    return get_by_ext('css')

def get_css_absolute_paths():
    retval = get_css_paths()
    for i in range(len(retval)):
        retval[i] = os.path.abspath(retval[i])
    return retval


if __name__ == '__main__':
    print("html files:")
    for path in get_html_paths():
        print(path)
    print("css files:")
    for path in get_css_paths():
        print(path)
