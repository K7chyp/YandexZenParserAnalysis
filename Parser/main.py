from yandex_zen_page_parser import YandexZenPageContentParser
from tqdm import trange


def main():
    YandexZenPageContentParser(
        "https://pythonru.com/uroki/35-instrukcija-assert-dlja-nachinajushhih"
    ).publish_date


if __name__ == "__main__":
    main()
