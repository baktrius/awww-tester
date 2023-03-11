"""
Tests detecting if tester at least found expected files in project
"""
from helper import get_css_paths, get_html_paths, report


def test_html_and_css_is_detected():
    html_paths = get_html_paths()
    css_paths = get_css_paths()
    assert len(html_paths) == 1, "Expected exactly one .html file"
    assert len(css_paths) >= 1, "Expected at least one .css file"
    report(html_paths + css_paths)
