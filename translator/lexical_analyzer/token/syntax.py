import re

from .token import Token


class Syntax(Token):
    pass


class Comma(Syntax):
    PATTERN = re.compile(r'^,')


class Dot(Syntax):
    PATTERN = re.compile(r'^\.')


class Apostrophe(Syntax):
    PATTERN = re.compile(r'^\'')


class Quote(Syntax):
    PATTERN = re.compile(r'^"')


class Semicolon(Syntax):
    PATTERN = re.compile(r'^;')


class Colon(Syntax):
    PATTERN = re.compile(r'^:')


class Backslash(Syntax):
    PATTERN = re.compile(r'^\\')
