from abc import ABC, abstractmethod


class Mapped(ABC):
    @abstractmethod
    def to_java(self) -> str:
        pass
