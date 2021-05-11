from typing import final
from yandex_zen_page_parser import BaseClassPageParser
from bs4 import BeautifulSoup


@final
class HiFiPageParser(BaseClassPageParser):
    def __init__(self, url) -> None:
        super().__init__(url)
        self.get_content_from_page()
        self.browser.close()

    def get_content_from_page(self) -> None:
        self.text_from_page: str = "".join(
            [text_part.text for text_part in self.soup.find_all("p")]
        )
        self.text_from_page: str = self.text_from_page
