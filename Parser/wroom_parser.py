from typing import final
from base_class_parser import BaseClassParser


class WroomParser(BaseClassParser):
    def __init__(self, url):
        super().__init__(url)
        self.text_from_page
        self.browser.close()