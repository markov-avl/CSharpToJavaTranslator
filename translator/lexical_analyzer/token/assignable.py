import re

from .token import Token


class Assignable(Token):
    pass


class Assign(Assignable):
    PATTERN = re.compile(r'^=')


class PlusAssign(Assignable):
    PATTERN = re.compile(r'^\+=')


class MinusAssign(Assignable):
    PATTERN = re.compile(r'^-=')


class MulAssign(Assignable):
    PATTERN = re.compile(r'^\*=')


class DivAssign(Assignable):
    PATTERN = re.compile(r'^/=')


class ModAssign(Assignable):
    PATTERN = re.compile(r'^%=')
