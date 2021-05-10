from YandexZenPageParser import YandexZenArticleNamesParser
from YandexZenPageParser import YandexZenPageContentParser
from tqdm import trange

ITERATIONS_COUNT = int(input("How many times do you want to parse it? "))


def main():
    output: dict = {}
    for _ in trange(ITERATIONS_COUNT):
        utility_parsed_page: dict = YandexZenArticleNamesParser(
            "https://zen.yandex.ru/"
        ).articles
        utility_output: dict = output.copy()
        output: dict = {**utility_output, **utility_parsed_page}
    return output


if __name__ == "__main__":
    print(main())
