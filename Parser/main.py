from YandexZenPageParser import YandexZenArticleNamesParser
from YandexZenPageParser import YandexZenPageContentParser
from tqdm import trange

ITERATIONS_COUNT = int(input("How many times do you want to parse it? "))


def main():
    YandexZenPageContentParser('https://zen.yandex.ru/media/nadzeiya/prostoi-sposob-ot-kitaianki-kak-za-chas-privesti-tiul-v-belosnejnoe-sostoianie-ne-verila-poka-sama-ne-proverila-pokazyvaiu-6027a81f241d462d4485d1c0').text
       
if __name__ == "__main__":
    main()
