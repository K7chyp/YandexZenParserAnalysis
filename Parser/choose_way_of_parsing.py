from base_class_parser import BaseClassParser


def choose_way_of_parsing(url: str):
    for value in (
        "https://zen.yandex.ru/",
        "https://www.hi-fi.ru/",
        "https://wroom.ru/",
        "https://www.autonews.ru/",
        "https://iz.ru/",
        "https://www.championat.com/",
    ):
        if value in url:
            return value
        else:
            if BaseClassParser(url).text_from_page is not None:
                return BaseClassParser(url).text_from_page
            else:
                raise "NotImplementedYet"
