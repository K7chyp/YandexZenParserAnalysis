from sub_functions import csv_file_preparation

TIMES_YOU_WANT_TO_PARSE: int = int(input("How many iterations do you want to parse? "))
OUTPUT_FILE_NAME: str = str(input("How do you want to call this file? "))


def main():
    csv_file_preparation(TIMES_YOU_WANT_TO_PARSE, OUTPUT_FILE_NAME)


if __name__ == "__main__":
    main()