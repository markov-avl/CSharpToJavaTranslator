import unittest

from translator.code_generator import CodeGenerator
from translator.lexical_analyzer import token
from translator.syntactical_analyzer import statement, declaration, expression, SyntacticalAnalyzer, Program, \
    AccessModifier, Body


class CodeGeneratorTestCase(unittest.TestCase):
    code_generator = CodeGenerator()

    def test_class(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))


if __name__ == '__main__':
    unittest.main()
