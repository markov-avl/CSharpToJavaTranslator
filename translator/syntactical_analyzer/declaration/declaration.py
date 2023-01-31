from abc import ABC

from translator.lexical_analyzer.token import Token
from translator.syntactical_analyzer.statement import Statement


class Declaration(Statement, ABC):
    KEYWORD: str = None

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f'DECLARATION_{self.__class__.__name__}'

    def __eq__(self, other):
        if not isinstance(other, Declaration):
            return False
        return self._name == other.name

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def is_appropriate_token(cls, token: Token) -> bool:
        return token.value == cls.KEYWORD
