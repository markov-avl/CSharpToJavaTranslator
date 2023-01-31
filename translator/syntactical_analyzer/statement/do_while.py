from .statement import Statement
from .conditioned import Conditioned
from translator.syntactical_analyzer.body import Body
from translator.syntactical_analyzer.expression import Expression


class DoWhile(Conditioned):
    KEYWORD = 'do'
    KEYWORD_WHILE = 'while'

    def __init__(self, condition: Expression, body: Body | Statement):
        super().__init__(condition, body)

    def to_java(self, indent: int = 0) -> str:
        return self._indented(
            indent,
            f'{self.KEYWORD} {{\n{self._body.to_java(indent + 1)}\n{self._indented(indent)}}} '
            f'{self.KEYWORD_WHILE} ({self._condition.to_java()});'
        )
