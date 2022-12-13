# pylint: disable=too-few-public-methods,
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore

from jtest._internal import singleton


def browser() -> WebDriver:
    """ Obtains browser instance

    Returns:
        Web Driver

    """
    return BrowserSingleton().driver


@singleton
class BrowserSingleton:
    """ Class representing browser singleton instance """

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
