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
        super().__init__(url)
        self.url_checker()
        self.get_text_from_yandex_zen_page()
        self.get_page_stats()
        self.browser.close()

    def url_checker(self):
        self.is_it_yandex_zen_page: bool = (
            True if "https://zen.yandex" in self.url else False
        )

    def get_text_from_yandex_zen_page(self):
        if self.is_it_yandex_zen_page:
            self.page_with_text = self.soup.find_all(
                "p", {"class": "article-render__block article-render__block_unstyled"}
            )
            self.text = "".join(
                [
                    part_of_this_article.text
                    for part_of_this_article in self.page_with_text
                ]
            )

    def get_page_stats(self):
        if self.is_it_yandex_zen_page:
            self.stats_for_page = self.soup.find(
                "span",
                {
                    "class": "ui-lib-likes-count__count _size_m _color_black _position_bottom"
                },
            ).text
            self.discuss = self.soup.find(
                "div", {"class": "ui-lib-comments-icon__bubble"}
            ).text
            self.page_stats = [
                stats_name.text
                for stats_name in self.soup.find_all(
                    "span", {"class": "article-stats-view-redesign__stats-item-count"}
                )
            ]
            self.publish_date = self.soup.find(
                "div", {"class": "article-stats-view-redesign__item"}
            ).text
            self.story_views = self.soup.find(
                "div", {"class": "article-stat-tip__item"}
            ).text
