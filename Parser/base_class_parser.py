from base_class_page_settings import BaseClassPageSettings
from bs4 import BeautifulSoup


class BaseClassParser(BaseClassPageSettings):
    def __init__(self, url):
        super().__init__(url)
        self.find_common_patterns()

    def find_common_patterns(self):
        self.text_from_page: str = "".join(
            [text_part.text for text_part in self.soup.find_all("p")]
        )