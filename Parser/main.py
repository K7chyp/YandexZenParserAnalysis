from izvestia_parser import IzvestiaParser


def main():
    print(IzvestiaParser(
    "https://iz.ru/1151401/veronika-kulakova/odni-v-pole-rossiiskie-agrarii-tak-i-ne-dozhdalis-migrantov?utm_referrer=https%3A%2F%2Fzen.yandex.com"
    ).author_name)

if __name__ == "__main__":
    main()
