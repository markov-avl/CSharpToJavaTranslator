from translator.syntactical_analyzer.statement.statement import Statement


class Body:
    def __init__(self, statements: list[Statement] = None):
        self._statements = statements if statements else []

    def __iter__(self):
        for statement in self._statements:
            yield statement

    def is_empty(self) -> bool:
        return not self._statements

    def add(self, statement: Statement) -> None:
        self._statements.append(statement)

    def to_java(self) -> str:
        return '\n'.join(statement.to_java() for statement in self._statements)
