from yandex_zen_page_parser import YandexZenArticleNamesParser
from choose_way_of_parsing import get_parsed_info
from sub_functions import dict_preprocessing
from time import sleep
from tqdm import tqdm

TIMES_YOU_WANT_TO_PARSE: int = int(input("How many iterations do you want to parse? "))


def main():
    output: dict = {}
    parsed_pages: dict = {}
    for _ in range(TIMES_YOU_WANT_TO_PARSE):
        output = dict_preprocessing(output, YandexZenArticleNamesParser().articles)
        sleep(1)
    for short_article_name, url in output.items():
        parsed_pages: dict = dict_preprocessing(
            {short_article_name: get_parsed_info(url)}, parsed_pages
        )
    return parsed_pages


if __name__ == "__main__":
    main()
