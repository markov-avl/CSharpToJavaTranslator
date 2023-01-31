from translator.syntactical_analyzer.body import Body
from .statement import Statement
from translator.syntactical_analyzer.expression import Expression


class For(Statement):
    KEYWORD = 'for'

    def __init__(self, body: Body, init: Statement = None, condition: Expression = None, step: Statement = None):
        self._body = body
        self._init = init
        self._condition = condition
        self._step = step

    def __eq__(self, other):
        if not isinstance(other, For):
            return False
        return self._body == other.body and \
            self._init == other.init and \
            self._condition == other.condition and \
            self._step == other.step

    @property
    def body(self) -> Body:
        return self._body

    @property
    def init(self) -> Statement:
        return self._init

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def step(self) -> Statement:
        return self._step

    def to_java(self, indent: int = 0) -> str:
        init = self._init.to_java() if self._init else ''
        condition = self._condition.to_java() if self._condition else ''
        step = self._step.to_java() if self._step else ''
        return f'{self.KEYWORD} ({init}; {condition}; {step}) {{\n{self._body.to_java()}\n}}'
