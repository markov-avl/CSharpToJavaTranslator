from .operation import Operation
from .unary import Unary
from .binary import Binary
from .token_type import TokenType
from .ordered import Order


class Bit(Operation):
    def is_bit(cls) -> bool:
        return True


class BitUnary(Bit, Unary):
    pass


class BitBinary(Bit, Binary):
    pass


TokenType.bit_not = BitUnary('~')
TokenType.bit_and = BitBinary('&', Order.HIGH)
TokenType.bit_or = BitBinary('|', Order.HIGH)
TokenType.bit_xor = BitBinary('^', Order.HIGH)
TokenType.shift_left = BitBinary('<<', Order.HIGH)
TokenType.shift_right = BitBinary('>>', Order.HIGH)
