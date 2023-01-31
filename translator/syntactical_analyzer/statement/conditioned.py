from .statement import Statement
from translator.syntactical_analyzer.body import Body
from translator.syntactical_analyzer.expression import Expression


class Conditioned(Statement):
    KEYWORD = None

    def __init__(self, condition: Expression, body: Body | Statement):
        self._condition = condition
        self._body = body

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def body(self) -> Body | Statement:
        return self._body

    def to_java(self, indent: int = 0) -> str:
        raise NotImplementedError('This method could not be implemented')
