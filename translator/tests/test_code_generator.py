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

    def test_class_method(self):
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
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_class_methods(self):
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
                            access_modifier=AccessModifier.private,
                            return_type='int',
                            name='foo',
                            params=[],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '',
            '	}',
            '',
            '	private int foo() {',
            '',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_method_param(self):
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
                                declaration.Param(type_='String[]', name='args')
                            ],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main(String[] args) {',
            '',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_method_params(self):
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
                                declaration.Param(type_='String[]', name='args'),
                                declaration.Param(type_='int', name='code'),
                            ],
                            body=Body()
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main(String[] args, int code) {',
            '',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_variable_declaration(self):
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
                                    declaration.Variable(type_='int', name='a'),
                                    declaration.Variable(type_='float', name='b', expression=expression.Atomic('.1'))
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		int a;',
            '		float b = .1;',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_assignment(self):
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
                                    statement.Assignment(
                                        name='a',
                                        token_type=token.PlusAssign('+='),
                                        right=expression.Atomic('1')
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		a += 1;',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_assignment(self):
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
                                    statement.Assignment(
                                        name='a',
                                        token_type=token.PlusAssign('+='),
                                        right=expression.Atomic('1')
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		a += 1;',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_if(self):
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
                                            body=Body()
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Atomic('false'),
                                            body=Body(
                                                statements=[
                                                    statement.Assignment(
                                                        name='a',
                                                        token_type=token.Assign('='),
                                                        right=expression.Atomic('1')
                                                    )
                                                ]
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Lesser('<'),
                                                right=expression.Atomic('2')
                                            ),
                                            body=statement.Assignment(
                                                name='a',
                                                token_type=token.Assign('='),
                                                right=expression.Binary(
                                                    left=expression.Atomic('1'),
                                                    operation=token.Plus('+'),
                                                    right=expression.Atomic('1')
                                                )
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Eq('=='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=Body()
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Greater('>'),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Binary(
                                                        left=expression.Atomic('5'),
                                                        operation=token.Mod('%'),
                                                        right=expression.Atomic('2')
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Neq('!='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Atomic('5'),
                                                operation=token.ShiftRight('>>'),
                                                right=expression.Atomic('2')
                                            )
                                        )
                                    ),
                                    statement.If(
                                        if_=statement.Conditioned(
                                            condition=expression.Binary(
                                                left=expression.Atomic('1'),
                                                operation=token.Geq('>='),
                                                right=expression.Atomic('2')
                                            ),
                                            body=Body()
                                        ),
                                        else_=statement.If(
                                            if_=statement.Conditioned(
                                                condition=expression.Binary(
                                                    left=expression.Atomic('1'),
                                                    operation=token.Leq('<='),
                                                    right=expression.Atomic('2')
                                                ),
                                                body=Body()
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		if (true) {',
            '',
            '		} ',
            '		if (false) {',
            '			a = 1;',
            '		} ',
            '		if (1 < 2) {',
            '			a = 1 + 1;',
            '		} ',
            '		if (1 == 2) {',
            '',
            '		} ',
            '		if (1 > 2) {',
            '',
            '		} else {',
            '			a = 5 % 2;',
            '		}',
            '		if (1 != 2) {',
            '',
            '		} else {',
            '			a = 5 >> 2;',
            '		}',
            '		if (1 >= 2) {',
            '',
            '		} else if (1 <= 2) {',
            '',
            '		} ',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_while(self):
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
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('true')
                                        ),
                                        body=Body()
                                    ),
                                    statement.While(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Call(
                                                        name='a',
                                                        arguments=[
                                                            expression.Atomic('true')
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ),
                                    statement.While(
                                        condition=expression.Binary(
                                            left=expression.Atomic('false'),
                                            operation=token.LogicalAnd('||'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Paren(
                                                    expression=expression.Binary(
                                                        left=expression.Atomic('1'),
                                                        operation=token.Plus('+'),
                                                        right=expression.Atomic('1')
                                                    )
                                                ),
                                                operation=token.Mul('*'),
                                                right=expression.Atomic('5')
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		while (true && true) {',
            '',
            '		}',
            '		while (true && false) {',
            '			a = a(true);',
            '		}',
            '		while (false || false) {',
            '			a = (1 + 1) * 5;',
            '		}',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_do_while(self):
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
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('true')
                                        ),
                                        body=Body()
                                    ),
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('true'),
                                            operation=token.LogicalAnd('&&'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=Body(
                                            statements=[
                                                statement.Assignment(
                                                    name='a',
                                                    token_type=token.Assign('='),
                                                    right=expression.Atomic('a')
                                                )
                                            ]
                                        )
                                    ),
                                    statement.DoWhile(
                                        condition=expression.Binary(
                                            left=expression.Atomic('false'),
                                            operation=token.LogicalAnd('||'),
                                            right=expression.Atomic('false')
                                        ),
                                        body=statement.Assignment(
                                            name='a',
                                            token_type=token.Assign('='),
                                            right=expression.Binary(
                                                left=expression.Paren(
                                                    expression=expression.Binary(
                                                        left=expression.Atomic('1'),
                                                        operation=token.Plus('+'),
                                                        right=expression.Atomic('1')
                                                    )
                                                ),
                                                operation=token.Mul('*'),
                                                right=expression.Atomic('5')
                                            )
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		do {',
            '',
            '		} while (true && true);',
            '		do {',
            '			a = a;',
            '		} while (true && false);',
            '		do {',
            '			a = (1 + 1) * 5;',
            '		} while (false || false);',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_return(self):
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
                                    statement.Return(),
                                    statement.Return(
                                        expression=expression.Atomic('5')
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public int Main() {',
            '		return;',
            '		return 5;',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))

    def test_statement_expression(self):
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
                                        expression_=expression.Atomic('true')
                                    ),
                                    statement.Expression(
                                        expression_=expression.Binary(
                                            left=expression.Atomic('5'),
                                            operation=token.Div('/'),
                                            right=expression.Atomic('1.0')
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            ]
        )
        generated_code = '\n'.join([
            'class Program {',
            '	public void Main() {',
            '		true;',
            '		5 / 1.0;',
            '	}',
            '}'
        ])
        self.assertEqual(generated_code, self.code_generator.generate(program))


if __name__ == '__main__':
    unittest.main()
