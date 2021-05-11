import os
from bs4 import BeautifulSoup
from selenium import webdriver


class BaseClassPageSettings:
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome(
            str(os.path.dirname(os.path.realpath(__file__)))
            + "/SileniumFiles/chromedriver"
        )
        self.get_html()
        self.soup = BeautifulSoup(self.html, "lxml")

    def get_html(self) -> None:
        self.browser.get(self.url)
        self.html: list = self.browser.page_source
