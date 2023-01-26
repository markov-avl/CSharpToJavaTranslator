from .statement import Statement
from .body import Body
from translator.lexical_analyzer.expression import Expression


class Conditioned(Statement):
    def __init__(self, name: str, condition: Expression, body: Body, pre: bool = True):
        self._name = name
        self._condition = condition
        self._body = body
        self._pre = pre

    @property
    def name(self) -> str:
        return self._name

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def body(self) -> Body:
        return self._body

    def is_preconditioned(self) -> bool:
        return self._pre
