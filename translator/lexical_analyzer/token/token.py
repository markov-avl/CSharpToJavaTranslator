from __future__ import annotations
from abc import ABC
import re

from translator.positioned import Positioned


class Token(Positioned, ABC):
    PATTERN: str

    def __init__(self, value: str, line: int = None, column: int = None):
        super().__init__(line, column)
        self._value = value

    def __str__(self) -> str:
        return f'TOKEN_{self.__class__.__name__}'

    def __len__(self) -> int:
        return len(self._value)

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return self._value == other.value and \
            self._line == other.line and \
            self._column == other.column

    @property
    def value(self) -> str:
        return self._value

    @classmethod
    def parse(cls, program_code: str, symbol: int) -> Token | None:
        if match := re.search(rf'^{cls.PATTERN}', program_code[symbol:]):
            return cls(match.group(0))
