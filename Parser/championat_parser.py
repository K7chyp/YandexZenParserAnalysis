from typing import final
from base_class_parser import BaseClassParser
from text_templates import string_spaces_delete


@final
class ChampionatParser(BaseClassParser):
    def __init__(self, url):
        super().__init__(url)
        self.publish_date = self.soup.find("time", {"class": "article-head__date"}).text
        self.author_name = string_spaces_delete(
            self.soup.find("div", {"class": "article-head__author-name"}).text
        )
        self.browser.close()