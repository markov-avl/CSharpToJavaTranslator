import re

from .token import Token


class Closable(Token):
    pass


class LeftParen(Closable):
    PATTERN = re.compile(r'^\(')


class RightParen(Closable):
    PATTERN = re.compile(r'^\)')


class LeftBracket(Closable):
    PATTERN = re.compile(r'^\[')


class RightBracket(Closable):
    PATTERN = re.compile(r'^]')


class LeftBrace(Closable):
    PATTERN = re.compile(r'^\{')


class RightBrace(Closable):
    PATTERN = re.compile(r'^}')
