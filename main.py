from translator import Translator


def main() -> None:
    with open('programs/test1.cs', 'r') as source_code:
        translated_code = Translator.translate(source_code.read())
    print(translated_code)


if __name__ == '__main__':
    main()
