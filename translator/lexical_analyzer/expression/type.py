from .expression_body import ExpressionBody


class Type(ExpressionBody):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return self._name
