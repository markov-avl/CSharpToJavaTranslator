from translator.syntactical_analyzer.declaration import Declaration


class Program:
    def __init__(self):
        self._declarations: list[Declaration] = []
        self._functions: list[Declaration] = []
