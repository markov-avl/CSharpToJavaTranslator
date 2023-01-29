import re

from .token import Token


class Closable(Token):
    pass


class LeftParen(Closable):
    PATTERN = r'\('


class RightParen(Closable):
    PATTERN = r'\)'


class LeftBracket(Closable):
    PATTERN = r'\['


class RightBracket(Closable):
    PATTERN = r']'


class LeftBrace(Closable):
    PATTERN = r'\{'


class RightBrace(Closable):
    PATTERN = r'}'
