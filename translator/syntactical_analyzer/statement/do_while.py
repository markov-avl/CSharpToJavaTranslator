from translator.syntactical_analyzer.body import Body
from .conditioned import Conditioned
from translator.syntactical_analyzer.expression import Expression


class DoWhile(Conditioned):
    def __init__(self, condition: Expression, body: Body):
        super().__init__(condition, body, False)

    def to_java(self) -> str:
        return f'do {{\n{self._body.to_java()}\n}} while ({self._condition.to_java()});'
