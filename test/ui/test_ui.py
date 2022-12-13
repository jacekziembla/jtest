import pytest
from selenium.common import WebDriverException

from jtest.browser import browser


@pytest.mark.ui
class TestUI:
    """ UI Suite """

    def test_example_com(self):
        """ Verifies """

        page_url = "https://www.example.com"
        page_title = "Example Domain"

        browser().get(page_url)

        assert browser().title == page_title, "Title does not match!"

    def test_invalid_page(self):
        """ Verifies that page """

        page_url = "https://www.c17d21ec-52f2-4c10-b7ea-a4145589c78f.com"
        error_message = "net::ERR_NAME_NOT_RESOLVED"

        with pytest.raises(WebDriverException) as exec_info:
            browser().get(page_url)

        assert error_message in str(exec_info.value), "Error has not been thrown. Such page exists!"
