
from subprocess import run
from helper import get_html_paths


def test_html_is_valid():
    cmd = f"npx html-validate {' '.join(get_html_paths())}"
    assert run(cmd, shell=True).returncode == 0
