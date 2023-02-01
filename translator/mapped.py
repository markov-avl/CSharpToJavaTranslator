from abc import ABC, abstractmethod


class Mapped(ABC):
    @abstractmethod
    def to_java(self, indent: int = 0) -> str:
        pass

    @staticmethod
    def _indented(indent: int, code: str = '') -> str:
        return '\t' * indent + code
