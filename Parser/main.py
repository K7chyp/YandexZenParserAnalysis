from hifi_parser import HiFiPageParser


def main():
    print(HiFiPageParser(
        "https://www.hi-fi.ru/magazine/kino/8-nastolko-strashnykh-uzh/?utm_referrer=https%3A%2F%2Fzen.yandex.com"
    ).raiting
)

if __name__ == "__main__":
    main()
