from selenium import webdriver
from requests import get
from bs4 import BeautifulSoup
import os


class YandexZenArticleNamesParser:
    def __init__(self, url) -> None:
        self.url = url
        self.browser = webdriver.Chrome(
            str(os.path.dirname(os.path.realpath(__file__)))
            + "/SileniumFiles/chromedriver"
        )
        self.get_html()
        self.soup = BeautifulSoup(self.html, "lxml")
        self.get_page_info()
        self.browser.close()

    def get_html(self) -> None:
        self.browser.get(self.url)
        self.html: list = self.browser.page_source

    def get_page_info(self) -> None:
        self.page = self.soup.find_all("div", {"class": "card-image-2-view__content"})
        self.articles: dict = {
            article.text: article.find('a').get("href")
            for article in self.page
            if article.text != " "
        }
        
