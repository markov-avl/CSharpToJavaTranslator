from abc import ABC

from translator.mapped import Mapped


class Expression(Mapped, ABC):
    def __init__(self, value: str = None):
        self._value = value

    def __str__(self) -> str:
        return f'EXPRESSION_{self.__class__.__name__}'

    def __eq__(self, other):
        if not isinstance(other, Expression):
            return False
        return self._value == other.value

    @property
    def value(self) -> str | None:
        return self._value

    @classmethod
    def is_atomic(cls) -> bool:
        return False
