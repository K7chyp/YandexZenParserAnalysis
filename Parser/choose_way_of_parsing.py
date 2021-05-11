
from base_class_parser import BaseClassParser


def choose_way_of_parsing(url: str):
    if 'https://zen.yandex.ru/' in url: 
        return 'zen'
    elif 'https://www.hi-fi.ru/' in url:
        return 'hi-fi'
    elif 'https://wroom.ru/' in url: 
        return 'wroom'
    elif 'https://www.autonews.ru/' in url: 
        return 'autonews'
    elif 'https://iz.ru/' in url: 
        return 'izvestia'
    elif 'https://www.championat.com/' in url:
        return 'championat'
    else: 
        if BaseClassParser(url).text_from_page is not None: 
          return  BaseClassParser(url).text_from_page 
        else: 
            raise 'NotImplementedYet'
     
         