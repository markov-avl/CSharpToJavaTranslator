from .declaration_body import DeclarationBody
from translator.lexical_analyzer.expression import Expression


class Variable(DeclarationBody):
    def __init__(self, type_: str, expression: Expression):
        self._type = type_
        self._expression = expression

    @property
    def type(self) -> str:
        return self._type

    @property
    def expression(self) -> Expression:
        return self._expression
