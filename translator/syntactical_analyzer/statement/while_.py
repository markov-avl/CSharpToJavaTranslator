from .statement import Statement
from .conditioned import Conditioned
from translator.syntactical_analyzer.body import Body
from translator.syntactical_analyzer.expression import Expression


class While(Conditioned):
    KEYWORD = 'while'

    def __init__(self, condition: Expression, body: Body | Statement):
        super().__init__(condition, body)

    def __eq__(self, other):
        if not isinstance(other, While):
            return False
        return self._condition == other.condition and \
            self._body == other.body

    def to_java(self, indent: int = 0) -> str:
        return self._indented(
            indent,
            f'{self.KEYWORD} ({self._condition.to_java()}) '
            f'{{\n{self._body.to_java(indent + 1)}\n{self._indented(indent)}}}'
        )
