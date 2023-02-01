from translator.syntactical_analyzer import declaration, Program

from .keyword import Keyword


class SemanticAnalyzer:
    def analyze(self, program: Program) -> None:
        self._check_main(program)
        [self._analyze_class(delc) for delc in program.declarations if isinstance(delc, declaration.Class)]

    def _analyze_class(self, class_: declaration.Class) -> None:
        self._check_name(class_.name)

    @staticmethod
    def _check_main(program: Program) -> None:
        classes = [delc for delc in program.declarations if isinstance(delc, declaration.Class)]
        mains = [method for method in sum([class_.methods for class_ in classes], []) if method.name == 'Main']
        if len(mains) == 0:
            raise SyntaxError('No entry points found (no Main)')
        elif len(mains) > 1:
            raise SyntaxError('Found multiple entry points (multiple Main)')

    @staticmethod
    def _check_name(name: str) -> None:
        if Keyword.is_keyword(name):
            raise SyntaxError(f'Name identifier cannot be a keyword ({name})')
