
from subprocess import run
from helper import PROJECT_PATH


def test_html_is_valid():
    assert run(f"npx html-validate {PROJECT_PATH}/*", shell=True).returncode == 0
