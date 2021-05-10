from selenium import webdriver
from requests import get
from bs4 import BeautifulSoup


class YandexZenPageParser:
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome(
            "/home/nikita/Desktop/YandexZenParserAnalysis/Parser/SileniumFiles/chromedriver"
        )
        self.get_html()
        self.soup = BeautifulSoup(self.html, "lxml")
        self.get_page_info()
        self.browser.close()

    def get_html(self) -> str:
        self.browser.get(self.url)
        self.html = self.browser.page_source

    def get_page_info(self):
        self.page = self.soup.find("div", {"class": "card-image-2-view__content"})
        self.articles = {
            article.text: article.get("href") for article in self.page.find_all("h2")
        }
