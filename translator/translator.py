from translator.code_generator import CodeGenerator
from translator.lexical_analyzer import LexicalAnalyzer
from translator.syntactical_analyzer import SyntacticalAnalyzer


class Translator:
    @staticmethod
    def translate(source_code: str) -> str:
        lexical_analyzer = LexicalAnalyzer()
        syntactical_analyzer = SyntacticalAnalyzer()
        code_generator = CodeGenerator()

        tokens = lexical_analyzer.tokenize(source_code)

        for token in tokens:
            print(f'token.{token.__class__.__name__}(\'{token.value}\', {token.line}, {token.column}),')

        program = syntactical_analyzer.parse(tokens)

        return code_generator.generate(program)
