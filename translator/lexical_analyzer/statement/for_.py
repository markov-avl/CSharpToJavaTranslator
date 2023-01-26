from .body import Body
from .statement import Statement
from translator.lexical_analyzer.expression import Expression


class For(Statement):
    def __init__(self, initialization: Statement, condition: Expression, next_: Statement, body: Body):
        self._initialization = initialization
        self._condition = condition
        self._next = next_
        self._body = body

    @property
    def initialization(self) -> Statement:
        return self._initialization

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def next(self) -> Statement:
        return self._next

    @property
    def body(self) -> Body:
        return self._body
