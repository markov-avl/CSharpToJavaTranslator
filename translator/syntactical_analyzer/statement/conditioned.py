from .statement import Statement
from translator.syntactical_analyzer.body import Body
from translator.syntactical_analyzer.expression import Expression


class Conditioned(Statement):
    KEYWORD = None

    def __init__(self, condition: Expression, body: Body | Statement):
        self._condition = condition
        self._body = body

    def __eq__(self, other):
        if not isinstance(other, Conditioned):
            return False
        return self._condition == other.condition and \
            self._body == other.body

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def body(self) -> Body | Statement:
        return self._body

    def to_java(self, indent: int = 0) -> str:
        raise NotImplementedError('This method could not be implemented')
