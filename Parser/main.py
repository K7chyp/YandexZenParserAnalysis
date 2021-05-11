from wroom_parser import WroomParser


def main():
    print(WroomParser(
    "https://wroom.ru/story/id/45139?utm_referrer=https%3A%2F%2Fzen.yandex.com"
    ).text_from_page)

if __name__ == "__main__":
    main()
