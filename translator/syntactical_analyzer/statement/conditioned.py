from abc import ABC

from .statement import Statement
from translator.syntactical_analyzer.body import Body
from translator.syntactical_analyzer.expression import Expression


class Conditioned(Statement, ABC):
    def __init__(self, condition: Expression, body: Body, pre: bool = True):
        self._condition = condition
        self._body = body
        self._pre = pre

    @property
    def condition(self) -> Expression | None:
        return self._condition

    @property
    def body(self) -> Body:
        return self._body

    def is_preconditioned(self) -> bool:
        return self._pre
