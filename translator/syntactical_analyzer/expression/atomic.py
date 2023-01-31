from .expression import Expression


class Atomic(Expression):
    def to_java(self, indent: int = 0) -> str:
        return self._value

    @classmethod
    def is_atomic(cls) -> bool:
        return True
