import os
from glob import glob

PROJECT_PATH = os.environ.get('PROJECT_PATH', '../moje1')


def get_by_ext(ext: str) -> list[str]:
    pattern = os.path.join(PROJECT_PATH, f'*.{ext}')
    print(pattern)
    return glob(pattern)


def get_html_paths():
    return get_by_ext('html') + get_by_ext('htm')


def get_css_paths():
    return get_by_ext('css')


if __name__ == '__main__':
    print("html files:")
    for path in get_html_paths():
        print(path)
    print("css files:")
    for path in get_css_paths():
        print(path)
