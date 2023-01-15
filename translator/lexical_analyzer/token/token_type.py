class TokenType:
    __slots__ = [
        '_name',
        'unknown',
        'end_of_stream',
        'left_paren',
        'right_paren',
        'left_bracket',
        'right_bracket',
        'left_brace',
        'right_brace',
        'comma',
        'dot',
        'apostrophe',
        'quote',
        'semicolon',
        'colon',
        'backslash',
        'plus',
        'minus',
        'asterisk',
        'mul',
        'slash',
        'div',
        'mod',
        'increment ',
        'decrement ',
        'greater',
        'lesser',
        'eq',
        'geq',
        'leq',
        'neq',
        'logical_and',
        'logical_or',
        'logical_not',
        'assign',
        'plus_assign',
        'minus_assign',
        'mul_assign',
        'div_assign',
        'mod_assign',
        'shift_left',
        'shift_right',
        'bit_and',
        'bit_or',
        'bit_xor',
        'bit_not',
        'int',
        'float',
        'identifier'
    ]

    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return self._name

    @classmethod
    def is_assignable(cls) -> bool:
        return False

    @classmethod
    def is_comparable(cls) -> bool:
        return False

    @classmethod
    def is_operation(cls) -> bool:
        return False

    @classmethod
    def is_arithmetic(cls) -> bool:
        return False

    @classmethod
    def is_logical(cls) -> bool:
        return False

    @classmethod
    def is_bit(cls) -> bool:
        return False

    @classmethod
    def is_ordered(cls) -> bool:
        return False

    @classmethod
    def is_unary(cls) -> bool:
        return False

    @classmethod
    def is_binary(cls) -> bool:
        return False


# Utility
TokenType.unknown = TokenType('Unknown')
TokenType.end_of_stream = TokenType('End of Stream')

# Braces
TokenType.left_paren = TokenType('Left Paren')
TokenType.right_paren = TokenType('Right Paren')
TokenType.left_bracket = TokenType('Left Bracket')
TokenType.right_bracket = TokenType('Right Bracket')
TokenType.left_brace = TokenType('Left Brace')
TokenType.right_brace = TokenType('Right Brace')

# Syntax
TokenType.comma = TokenType(',')
TokenType.dot = TokenType('.')
TokenType.apostrophe = TokenType('\'')
TokenType.quote = TokenType('"')
TokenType.semicolon = TokenType(';')
TokenType.colon = TokenType(':')
TokenType.backslash = TokenType('\\')

# Type
TokenType.int = TokenType('Int')
TokenType.float = TokenType('Float')
TokenType.identifier = TokenType('Identifier')
