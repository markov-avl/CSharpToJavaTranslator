# CSharpToJavaTranslator

Транслятор исходного кода из C# в Java.

## Полезные ссылки

- [Описание необходимого транслятора](https://github.com/KostikShutov/compilers)
- [Пример лексического анализатора для JavaScript](https://github.com/KostikShutov/lexical-analyzer-for-js)

## Инструкция по запуску

### Зависимости

Для запуска на машине необходим установленный python версии 3.10+

Проверить установлен ли python можно следующей командой:

```
python3 --version
```

Установка python@3.11 на Ubuntu:

```
sudo apt update
sudo apt install python3.11
```

MacOS:

```
brew install python@3.11
```

[Windows](https://www.python.org/downloads/)

Также для запуска тестов необходимо установить `pytest`:

```
pip install -U pytest
pip install -U pytest-cov
```

### Запуск приложения

#### Запуск main.py

Для запуск необходимо передать полный путь к файлу.

Пример:

```
python3 main.py /Users/alexoff/CSharpToJavaTranslator/test.txt
```

Результат работы программы будет напечатан в консоль.

#### Запуск тестов

Запуск unit-тестов c покрытием:

```
pytest --cov=translator/ translator/tests/
```
