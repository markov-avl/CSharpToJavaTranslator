from translator.mapped import Mapped
from translator.syntactical_analyzer.statement.statement import Statement


class Body(Mapped):
    def __init__(self, statements: list[Statement] = None):
        self._statements = statements if statements else []

    def __len__(self) -> int:
        return len(self._statements)

    def __iter__(self):
        for statement in self._statements:
            yield statement

    def __eq__(self, other):
        if not isinstance(other, Body):
            return False
        return self._statements == other.statements

    @property
    def statements(self) -> list[Statement]:
        return self._statements

    def is_empty(self) -> bool:
        return not self._statements

    def add(self, statement: Statement) -> None:
        self._statements.append(statement)

    def to_java(self, indent: int = 0) -> str:
        return '\n'.join(statement.to_java(indent) for statement in self._statements)
