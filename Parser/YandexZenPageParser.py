from selenium import webdriver
from requests import get
from bs4 import BeautifulSoup
import os


class BaseClassYandexParser:
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


class YandexZenArticleNamesParser(BaseClassYandexParser):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.get_info_about_articles()
        self.browser.close()

    def get_info_about_articles(self) -> None:
        self.page = self.soup.find_all("div", {"class": "card-image-2-view__content"})
        self.articles: dict = {
            article.text: article.find("a").get("href")
            for article in self.page
            if article.text != " "
        }


class YandexZenPageContentParser(BaseClassYandexParser):
    def __init__(self, url):
        super.__init__(url)
        self.url_checker()
        self.browser.close()

    def url_checker(self):
        self.is_it_yandex_zen_page: bool = (
            True if "https://zen.yandex" in self.url else False
        )

    def get_text_from_yandex_zen_page(self): 
        pass