import unittest

from translator.lexical_analyzer import token
from translator.semantic_analyzer import SemanticAnalyzer
from translator.syntactical_analyzer import statement, declaration, expression, Program, AccessModifier, Body


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

    def test_identical_param_names(self):
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
                            params=[
                                declaration.Param(type_='int', name='a'),
                                declaration.Param(type_='string', name='b'),
                                declaration.Param(type_='float', name='b'),
                            ],
                            body=Body()
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'The method has several identical parameter names')

    def test_invalid_return(self):
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
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('0')
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Void function must not have any return statements')

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
                            body=Body(
                                statements=[
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('true'),
                                            body=statement.Return(
                                                expression=expression.Atomic('0')
                                            )
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Void function must not have any return statements')

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
                            body=Body(
                                statements=[
                                    statement.While(
                                        condition=expression.Atomic('true'),
                                        body=statement.Return(
                                            expression=expression.Atomic('0')
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Void function must not have any return statements')

        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='abstract',
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
        self.assertEqual(e.exception.msg, 'Invalid return type')

    def test_invalid_type(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='int',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Paren(
                                            expression=expression.Atomic('true')
                                        ),
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Expected type int')

        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='float',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('true'),
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Expected type float')

        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='bool',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('1'),
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Expected type bool')

    def test_variable_is_not_declared(self):
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
                            body=Body(
                                statements=[
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('true'),
                                            body=statement.Assignment(
                                                name='a',
                                                token_type=token.Assign('='),
                                                right=expression.Atomic('5')
                                            )
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Variable a is not declared')

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
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='int',
                                        name='a'
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('true'),
                                            body=statement.Assignment(
                                                name='a',
                                                token_type=token.Assign('='),
                                                right=expression.Atomic('5')
                                            )
                                        ),
                                        else_=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Atomic('5')
                                                ),
                                                statement.Assignment(
                                                    name='b',
                                                    token_type=token.Assign('='),
                                                    right=expression.Atomic('5')
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Variable b is not declared')

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
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='int',
                                        name='a'
                                    ),
                                    statement.While(
                                        condition=expression.Atomic('true'),
                                        body=statement.Assignment(
                                            name='b',
                                            token_type=token.Assign('='),
                                            right=expression.Atomic('5')
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Variable b is not declared')

    def test_function_is_not_declared(self):
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
                            body=Body(
                                statements=[
                                    statement.Expression(
                                        expression_=expression.Call(
                                            name='Foo',
                                            arguments=[]
                                        )
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Function Foo is not declared')

    def test_invalid_variable_type(self):
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
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='abstract',
                                        name='a'
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Unknown variable type abstract')

    def test_variable_already_declared(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[
                        declaration.Attribute(
                            access_modifier=AccessModifier.private,
                            type_='int',
                            name='bar'
                        )
                    ],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='float',
                                        name='bar'
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Variable bar already declared')

    def test_invalid_argument_type(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[
                        declaration.Attribute(
                            access_modifier=AccessModifier.private,
                            type_='int',
                            name='bar'
                        )
                    ],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='float',
                                        name='a',
                                        expression=expression.Atomic('1.0')
                                    ),
                                    statement.Expression(
                                        expression_=expression.Call(
                                            name='Foo',
                                            arguments=[
                                                expression.Atomic('a')
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='int',
                            name='Foo',
                            params=[
                                declaration.Param(
                                    type_='int',
                                    name='a'
                                )
                            ],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('0')
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, '1 param type of the Foo() do not match with 1 argument')

    def test_invalid_argument_number(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[
                        declaration.Attribute(
                            access_modifier=AccessModifier.private,
                            type_='int',
                            name='bar'
                        )
                    ],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    declaration.Variable(
                                        type_='float',
                                        name='a',
                                        expression=expression.Atomic('1.0')
                                    ),
                                    statement.Expression(
                                        expression_=expression.Call(
                                            name='Foo',
                                            arguments=[
                                                expression.Atomic('a'),
                                                expression.Atomic('b')
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='int',
                            name='Foo',
                            params=[
                                declaration.Param(
                                    type_='int',
                                    name='a'
                                )
                            ],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('0')
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Number of parameters and function arguments do not match')

    def test_argument_is_not_declared(self):
        program = Program(
            declarations=[
                declaration.Class(
                    name='Program',
                    attributes=[
                        declaration.Attribute(
                            access_modifier=AccessModifier.private,
                            type_='int',
                            name='bar'
                        )
                    ],
                    methods=[
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='void',
                            name='Main',
                            params=[],
                            body=Body(
                                statements=[
                                    statement.Expression(
                                        expression_=expression.Call(
                                            name='Foo',
                                            arguments=[
                                                expression.Atomic('a')
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
                        declaration.Method(
                            access_modifier=AccessModifier.public,
                            return_type='int',
                            name='Foo',
                            params=[
                                declaration.Param(
                                    type_='int',
                                    name='a'
                                )
                            ],
                            body=Body(
                                statements=[
                                    statement.Return(
                                        expression=expression.Atomic('0')
                                    )
                                ]
                            )
                        ),
                    ]
                )
            ]
        )
        with self.assertRaises(SyntaxError) as e:
            self.semantic_analyzer.analyze(program)
        self.assertEqual(e.exception.msg, 'Argument a is not declared')


if __name__ == '__main__':
    unittest.main()
