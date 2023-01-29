from abc import ABC

from translator.syntactical_analyzer.mapped import Mapped


class Statement(Mapped, ABC):
    def __str__(self) -> str:
        return f'STATEMENT_{self.__class__.__name__}'
