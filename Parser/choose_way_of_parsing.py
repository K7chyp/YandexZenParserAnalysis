from base_class_parser import BaseClassParser
from yandex_zen_page_parser import YandexZenPageContentParser
from hifi_parser import HiFiPageParser
from wroom_parser import WroomParser
from autonews_parser import AutoNewsPageParser
from izvestia_parser import IzvestiaParser
from championat_parser import ChampionatParser

BASEDICT: dict = {
    "https://zen.yandex.ru/": YandexZenPageContentParser,
    "https://www.hi-fi.ru/": HiFiPageParser,
    "https://wroom.ru/": WroomParser,
    "https://www.autonews.ru/": AutoNewsPageParser,
    "https://iz.ru/": IzvestiaParser,
    "https://www.championat.com/": ChampionatParser,
}


def get_parsed_info(url: str):

    for value in BASEDICT.keys():
        if value in url:
            parser = BASEDICT[value](url)
            return {
                "text": parser.text_from_page,
                "author": parser.author,
                "publish_date": parser.publish_date,
                "href": url,
            }

        else:
            text: str = BaseClassParser(url).text_from_page
            if text is not None:
                return {
                    "text": text,
                    "author": None,
                    "publish_date": None,
                    "href": url
                }
            else:
                continue
