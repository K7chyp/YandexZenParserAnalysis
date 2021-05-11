from typing import final
from base_class_parser import BaseClassParser


@final
class HiFiPageParser(BaseClassParser):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.get_content_from_page()
        self.raiting = self.soup.find("span", {"class": "ratings__num"}).text
        self.browser.close()

    def get_content_from_page(self) -> None:
        self.page_content: str = [
            content.text.replace("\n", "").replace("\t", "")
            for content in self.soup.find_all("div", {"class": "autor"})
        ]
        self.article_author = self.page_content[0]
        self.publish_date = self.page_content[1]
