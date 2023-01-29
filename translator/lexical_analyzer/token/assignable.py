import re

from .token import Token


class Assignable(Token):
    pass


class Assign(Assignable):
    PATTERN = r'='


class PlusAssign(Assignable):
    PATTERN = r'\+='


class MinusAssign(Assignable):
    PATTERN = r'-='


class MulAssign(Assignable):
    PATTERN = r'\*='


class DivAssign(Assignable):
    PATTERN = r'/='


class ModAssign(Assignable):
    PATTERN = r'%='
