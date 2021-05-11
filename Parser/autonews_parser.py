from typing import final
from base_class_parser import BaseClassParser


@final
class AutoNewsPageParser(BaseClassParser):
    def __init__(self, url):
        super().__init__(url)
        self.page_author = self.soup.find(
            "span", {"class": "article__header__author"}
        ).text
        self.publish_date = self.soup.find(
            "span", {"class": "article__header__date"}
        ).text
        self.browser.close()
