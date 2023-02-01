import unittest

from translator.semantic_analyzer import SemanticAnalyzer
from translator.syntactical_analyzer import declaration, Program, AccessModifier, Body


class SemanticAnalyzerTestCase(unittest.TestCase):
    semantic_analyzer = SemanticAnalyzer()

    def test_no_main(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'No entry points found (no Main)')

    def test_multiple_mains(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body()
                        ),
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Found multiple entry points (multiple Main)')

    def test_name_identifier_as_keyword(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='while',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body()
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Name identifier cannot be a keyword (while)')


if __name__ == '__main__':
    unittest.main()
