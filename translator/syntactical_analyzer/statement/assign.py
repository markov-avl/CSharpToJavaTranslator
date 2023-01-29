from .statement import Statement
from translator.lexical_analyzer import token
from translator.syntactical_analyzer.expression import Expression


class Assign(Statement):
    def __init__(self, name: str, token_type: token.Assignable, right: Expression):
        self._name = name
        self._token_type = token_type
        self._right = right

    @property
    def name(self) -> str:
        return self._name

    @property
    def token_type(self) -> token.Assignable:
        return self._token_type

    @property
    def right(self) -> Expression:
        return self._right

    def to_java(self) -> str:
        return f'{self._name} {self._token_type.value} {self._right.to_java()}'
