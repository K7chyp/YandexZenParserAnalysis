from typing import final
from yandex_zen_page_parser import BaseClassPageParser
from bs4 import BeautifulSoup


@final
class HiFiPageParser(BaseClassPageParser):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.get_content_from_page()
        self.raiting = self.soup.find("span", {"class": "ratings__num"}).text
        self.browser.close()

    def get_content_from_page(self) -> None:
        self.text_from_page: str = "".join(
            [text_part.text for text_part in self.soup.find_all("p")]
        )
        self.text_from_page: str = self.text_from_page
        self.page_content: str = [
            content.text.replace("\n", "").replace("\t", "")
            for content in self.soup.find_all("div", {"class": "autor"})
        ]
        self.article_author = self.page_content[0]
        self.publish_date = self.page_content[1]
