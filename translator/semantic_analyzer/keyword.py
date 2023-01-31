from __future__ import annotations


class Keyword:
    __slots__ = [
        '_name',
        'abstract',
        'as_',
        'base',
        'bool',
        'break_',
        'byte',
        'case',
        'catch',
        'char',
        'checked',
        'class_',
        'const',
        'continue_',
        'decimal',
        'default',
        'delegate',
        'do',
        'double',
        'else_',
        'enum',
        'event',
        'explicit',
        'extern',
        'false',
        'finally_',
        'fixed',
        'float',
        'for_',
        'foreach',
        'goto',
        'if_',
        'implicit',
        'in_',
        'int',
        'interface',
        'internal',
        'is_',
        'lock',
        'long',
        'namespace',
        'new',
        'null',
        'object',
        'operator',
        'out',
        'override',
        'params',
        'private',
        'protected',
        'public',
        'readonly',
        'ref',
        'return_',
        'sbyte',
        'sealed',
        'short',
        'sizeof',
        'stackalloc',
        'static',
        'string',
        'struct',
        'switch',
        'this',
        'throw',
        'true',
        'try_',
        'typeof',
        'uint',
        'ulong',
        'unchecked',
        'unsafe',
        'ushort',
        'using',
        'virtual',
        'void',
        'volatile',
        'while_'
    ]

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @staticmethod
    def all() -> list[Keyword]:
        return [v for v in Keyword.__dict__.values() if isinstance(v, Keyword)]

    @staticmethod
    def is_keyword(word: str) -> bool:
        return word in [keyword.name for keyword in Keyword.all()]


Keyword.abstract = Keyword('abstract')
Keyword.as_ = Keyword('as')
Keyword.base = Keyword('base')
Keyword.bool = Keyword('bool')
Keyword.break_ = Keyword('break')
Keyword.byte = Keyword('byte')
Keyword.case = Keyword('case')
Keyword.catch = Keyword('catch')
Keyword.char = Keyword('char')
Keyword.checked = Keyword('checked')
Keyword.class_ = Keyword('class')
Keyword.const = Keyword('const')
Keyword.continue_ = Keyword('continue')
Keyword.decimal = Keyword('decimal')
Keyword.default = Keyword('default')
Keyword.delegate = Keyword('delegate')
Keyword.do = Keyword('do')
Keyword.double = Keyword('double')
Keyword.else_ = Keyword('else')
Keyword.enum = Keyword('enum')
Keyword.event = Keyword('event')
Keyword.explicit = Keyword('explicit')
Keyword.extern = Keyword('extern')
Keyword.false = Keyword('false')
Keyword.finally_ = Keyword('finally')
Keyword.fixed = Keyword('fixed')
Keyword.float = Keyword('float')
Keyword.for_ = Keyword('for')
Keyword.foreach = Keyword('foreach')
Keyword.goto = Keyword('goto')
Keyword.if_ = Keyword('if')
Keyword.implicit = Keyword('implicit')
Keyword.in_ = Keyword('in')
Keyword.int = Keyword('int')
Keyword.interface = Keyword('interface')
Keyword.internal = Keyword('internal')
Keyword.is_ = Keyword('is')
Keyword.lock = Keyword('lock')
Keyword.long = Keyword('long')
Keyword.namespace = Keyword('namespace')
Keyword.new = Keyword('new')
Keyword.null = Keyword('null')
Keyword.object = Keyword('object')
Keyword.operator = Keyword('operator')
Keyword.out = Keyword('out')
Keyword.override = Keyword('override')
Keyword.params = Keyword('params')
Keyword.private = Keyword('private')
Keyword.protected = Keyword('protected')
Keyword.public = Keyword('public')
Keyword.readonly = Keyword('readonly')
Keyword.ref = Keyword('ref')
Keyword.return_ = Keyword('return')
Keyword.sbyte = Keyword('sbyte')
Keyword.sealed = Keyword('sealed')
Keyword.short = Keyword('short')
Keyword.sizeof = Keyword('sizeof')
Keyword.stackalloc = Keyword('stackalloc')
Keyword.static = Keyword('static')
Keyword.string = Keyword('string')
Keyword.struct = Keyword('struct')
Keyword.switch = Keyword('switch')
Keyword.this = Keyword('this')
Keyword.throw = Keyword('throw')
Keyword.true = Keyword('true')
Keyword.try_ = Keyword('try')
Keyword.typeof = Keyword('typeof')
Keyword.uint = Keyword('uint')
Keyword.ulong = Keyword('ulong')
Keyword.unchecked = Keyword('unchecked')
Keyword.unsafe = Keyword('unsafe')
Keyword.ushort = Keyword('ushort')
Keyword.using = Keyword('using')
Keyword.virtual = Keyword('virtual')
Keyword.void = Keyword('void')
Keyword.volatile = Keyword('volatile')
Keyword.while_ = Keyword('while')
