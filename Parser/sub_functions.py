from yandex_zen_page_parser import YandexZenArticleNamesParser
from choose_way_of_parsing import get_parsed_info
from time import sleep
from tqdm import trange
from csv import writer


def dict_preprocessing(dict_last_iteration: dict, dict_new_itrearion: dict) -> dict:
    utility_dict: dict = dict_new_itrearion.copy()
    dict_new_itrearion: dict = {**utility_dict, **dict_last_iteration}
    return dict_new_itrearion


def writerow_preprocessing(
    short_article_name: str, dict_with_information: dict
) -> list:
    return [short_article_name] + [item for _, item in dict_with_information.items()]


def getting_information(times_you_want_to_parse):
    output: dict = {}
    parsed_pages: dict = {}
    for _ in range(times_you_want_to_parse):
        output = dict_preprocessing(output, YandexZenArticleNamesParser().articles)
        sleep(1)
    for short_article_name, url in output.items():
        parsed_pages: dict = dict_preprocessing(
            {short_article_name: get_parsed_info(url)}, parsed_pages
        )
    return parsed_pages


def csv_file_preparation(times_you_want_to_parse: int, file_name: str):
    parsed_pages = getting_information(times_you_want_to_parse)
    with open(f"{file_name}.csv", "w") as csv_file:
        write = writer(csv_file)
        write.writerow([['short_name', 'text', 'author_name', 'date', 'href']])
        for short_name, elemnts in parsed_pages.items():
            write.writerow(writerow_preprocessing(short_name, elemnts))
