from translator.code_generator import CodeGenerator
from translator.lexical_analyzer import LexicalAnalyzer
from translator.syntactical_analyzer import SyntacticalAnalyzer
from translator.semantic_analyzer import SemanticAnalyzer


class Translator:
    def __init__(self):
        self._lexical_analyzer = LexicalAnalyzer()
        self._syntactical_analyzer = SyntacticalAnalyzer()
        self._semantic_analyzer = SemanticAnalyzer()
        self._code_generator = CodeGenerator()

    def translate(self, source_code: str) -> str:
        tokens = self._lexical_analyzer.tokenize(source_code)
        program = self._syntactical_analyzer.parse(tokens)
        self._semantic_analyzer.analyze(program)
        return self._code_generator.generate(program)
