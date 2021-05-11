import os
from selenium import webdriver
from bs4 import BeautifulSoup


DIV = "div"
CLASS = "class"
SPAN = "span"


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
        self.page = self.soup.find_all(DIV, {CLASS: "card-image-2-view__content"})
        self.articles: dict = {
            article.text: article.find("a").get("href")
            for article in self.page
            if article.text != " "
        }


class YandexZenPageContentParser(BaseClassYandexParser):
    def __init__(self, url):
        super().__init__(url)
        self.url_checker()
        self.set_text_from_yandex_zen_page()
        self.set_page_stats()
        self.browser.close()

    def url_checker(self):
        self.is_it_yandex_zen_page: bool = "https://zen.yandex" in self.url
        assert self.is_it_yandex_zen_page is True, "It's not Yandex Zen Page"

    def set_text_from_yandex_zen_page(self):
        self.page_with_text = self.soup.find_all(
            "p", {CLASS: "article-render__block article-render__block_unstyled"}
        )
        self.text = "".join(
            [part_of_this_article.text for part_of_this_article in self.page_with_text]
        )

    def set_page_stats(self):
        self.stats_for_page = self.soup.find(
            SPAN,
            {CLASS: "ui-lib-likes-count__count _size_m _color_black _position_bottom"},
        ).text
        self.discuss = self.soup.find(DIV, {CLASS: "ui-lib-comments-icon__bubble"}).text
        self.page_stats = [
            stats_name.text
            for stats_name in self.soup.find_all(
                SPAN, {CLASS: "article-stats-view-redesign__stats-item-count"}
            )
        ]
        self.publish_date = self.soup.find(
            DIV, {CLASS: "article-stats-view-redesign__item"}
        ).text
        self.story_views = self.soup.find(DIV, {CLASS: "article-stat-tip__item"}).text
