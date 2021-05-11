from yandex_zen_page_parser import YandexZenPageContentParser


def main():
    print(YandexZenPageContentParser(
        'https://zen.yandex.ru/media/100mln/kak-ne-stat-bogatym-imeia-vse-vozmojnosti-razbogatet-606a011ee0a09f1423579998' ).author_stats
)

if __name__ == "__main__":
    main()
