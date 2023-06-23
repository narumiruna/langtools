from langtools import WebBrowser


def test_web_browser():
    tool = WebBrowser()

    res = tool.run('https://www.google.com')
    assert isinstance(res, str)
    assert len(res) > 0
