from .token import Token


class Syntax(Token):
    pass


class Comma(Syntax):
    PATTERN = r','


class Dot(Syntax):
    PATTERN = r'\.'


class Apostrophe(Syntax):
    PATTERN = r'\''


class Quote(Syntax):
    PATTERN = r'"'


class Semicolon(Syntax):
    PATTERN = r';'


class Colon(Syntax):
    PATTERN = r':'


class Backslash(Syntax):
    PATTERN = r'\\'
