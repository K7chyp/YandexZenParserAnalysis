from YandexZenPageParser import YandexZenArticleNamesParser
from YandexZenPageParser import YandexZenPageContentParser
from tqdm import trange

# ITERATIONS_COUNT = int(input("How many times do you want to parse it? "))


def main():
    # output: dict = {}
    # for _ in trange(ITERATIONS_COUNT):
    #     utility_parsed_page: dict = YandexZenArticleNamesParser(
    #         "https://zen.yandex.ru/"
    #     ).articles
    #     utility_output: dict = output.copy()
    #     output: dict = {**utility_output, **utility_parsed_page}
    print(YandexZenPageContentParser('https://zen.yandex.ru/media/nadzeiya/prostoi-sposob-ot-kitaianki-kak-za-chas-privesti-tiul-v-belosnejnoe-sostoianie-ne-verila-poka-sama-ne-proverila-pokazyvaiu-6027a81f241d462d4485d1c0').publish_date)
       
if __name__ == "__main__":
    main()
