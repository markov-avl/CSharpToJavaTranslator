from .token import Token


class Dynamic(Token):
    pass


class Int(Dynamic):
    PATTERN = r'\d+'


class Float(Dynamic):
    PATTERN = r'(\d+\.\d+|\d+\.|\.\d+)'


class Identifier(Dynamic):
    PATTERN = r'[a-zA-Z_]\w*'
