from typing import final
from base_class_parser import BaseClassParser
from text_templates import string_spaces_delete


@final
class IzvestiaParser(BaseClassParser):
    def __init__(self, url):
        super().__init__(url)
        self.author_name = string_spaces_delete(
            self.soup.find(
                "div", {"class": "top_big_img_article__info__inside__author"}
            ).text
        )
        self.browser.close()