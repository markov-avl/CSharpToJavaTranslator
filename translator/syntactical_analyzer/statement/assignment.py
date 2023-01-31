from .statement import Statement
from translator.lexical_analyzer import token
from translator.syntactical_analyzer.expression import Expression


class Assignment(Statement):
    KEYWORD = None

    def __init__(self, name: str, token_type: token.Assignable, right: Expression):
        self._name = name
        self._token_type = token_type
        self._right = right

    def __eq__(self, other):
        if not isinstance(other, Assignment):
            return False
        return self._name == other.name and \
            self._token_type == other.token_type and \
            self._right == other.right

    @property
    def name(self) -> str:
        return self._name

    @property
    def token_type(self) -> token.Assignable:
        return self._token_type

    @property
    def right(self) -> Expression:
        return self._right

    def to_java(self, indent: int = 0) -> str:
        return self._indented(indent, f'{self._name} {self._token_type.value} {self._right.to_java()};')
