from abc import ABC

from translator.lexical_analyzer.token import Token
from translator.syntactical_analyzer.mapped import Mapped


class Statement(Mapped, ABC):
    KEYWORD: str = None

    def __str__(self) -> str:
        return f'STATEMENT_{self.__class__.__name__}'

    @classmethod
    def is_appropriate_token(cls, token: Token) -> bool:
        return token.value == cls.KEYWORD
