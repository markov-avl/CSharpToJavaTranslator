import re

from .token import Token


class Dynamic(Token):
    pass


class Int(Dynamic):
    PATTERN = re.compile(r'^\d+')


class Float(Dynamic):
    PATTERN = re.compile(r'^(\d+\.\d+|\d+\.|\.\d+)')


class Identifier(Dynamic):
    PATTERN = re.compile(r'^[a-zA-Z_]\w*')
