import sys

from translator import Translator


def main(path: str) -> None:
    translator_ = Translator()
    try:
        with open(path, 'r') as source_code:
            translated_code = translator_.translate(source_code.read())
        print(translated_code)
    except FileNotFoundError:
        print('Файл не найден. Нужно передать полный путь к файлу.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        raise UserWarning('Передайте полный путь к файлу.')
