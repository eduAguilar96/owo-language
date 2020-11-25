# Module containing enum and constant Data
from collections import defaultdict
from enum import Enum, IntEnum, auto

# DATA TYPES
class Types(Enum):
  INT_TYPE = 'int'
  FLOAT_TYPE = 'float'
  BOOL_TYPE = 'bool'
  STRING_TYPE = 'string'
  VOID = 'void'
  ADDR = 'addr'

types_map = {
  'int': Types.INT_TYPE,
  'float': Types.FLOAT_TYPE,
  'bool': Types.BOOL_TYPE,
  'string': Types.STRING_TYPE,
  'void': Types.VOID,
  'addr': Types.ADDR,
}

class Operations(Enum):
  # OPERATORS
  PLUS    = '+'
  MINUS   = '-'
  TIMES   = '*'
  DIVIDE  = '/'
  MODULUS = '%'
  # Logical Operators
  AND = 'and'
  OR = 'or'
  NOT = 'not'
  # Relational Operators
  EQUAL = '='
  LESSTHAN = '<'
  GREATERTHAN = '>'
  EQUALEQUAL = '=='
  NOTEQUAL = '!='
  LESSTHANOREQUAL = '<='
  GREATERTHANOREQUAL = '>='
  # MISC
  PLUSUNARY = '+'
  MINUSUNARY = '-'
  # Machine
  GOTO = 'goto'
  GOTOT = 'gotoT'
  GOTOF = 'gotoF'
  GOSUB = 'gosub'
  ERA = 'era'
  ENDFUNC = 'endFunc'
  START = 'start'
  END = 'end'
  PARAM = 'param'
  RETURN = 'return'
  VER = 'ver'
  PRINT = 'print'
  INPUTSTRING = 'inputString'
  INPUTINT = 'inputInt'
  INPUTFLOAT = 'inputFloat'

#Tokens to Enum
operations_map = {
  '+': Operations.PLUS,
  '-': Operations.MINUS,
  '*': Operations.TIMES,
  '/': Operations.DIVIDE,
  '%': Operations.MODULUS,
  # NOT TODO
  'and': Operations.AND,
  'or': Operations.OR,
  '=': Operations.EQUAL,
  '<': Operations.LESSTHAN,
  '>': Operations.GREATERTHAN,
  '==': Operations.EQUALEQUAL,
  '!=': Operations.NOTEQUAL,
  '<=': Operations.LESSTHANOREQUAL,
  '>=': Operations.GREATERTHANOREQUAL,
  'goto': Operations.GOTO,
  'gotoT': Operations.GOTOT,
  'gotoF': Operations.GOTOF,
  'gosub': Operations.GOSUB,
  'era': Operations.ERA,
  'endFunc': Operations.ENDFUNC,
  'start': Operations.START,
  'end': Operations.END,
  'param': Operations.PARAM,
  'return': Operations.RETURN,
  'ver': Operations.VER,
}

semantic_cube = defaultdict(
  lambda: defaultdict(lambda: defaultdict(lambda: None)))

semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.GREATERTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.PLUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.MINUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.TIMES] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.DIVIDE] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.MODULUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.PLUSUNARY] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.MINUSUNARY] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.PLUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.MINUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.TIMES] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.DIVIDE] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.MODULUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.PLUSUNARY] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.MINUSUNARY] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.GREATERTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.PLUS] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.MINUS] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.TIMES] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.DIVIDE] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.EQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.AND] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.PLUSUNARY] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.MINUSUNARY] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHAN] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHAN] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.NOTEQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.EQUALEQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHANOREQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHANOREQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.GREATERTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.PLUS] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.PLUS] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.MINUS] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.MINUS] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.TIMES] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.TIMES] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.DIVIDE] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.DIVIDE] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.MODULUS] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.MODULUS] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE

semantic_cube[Types.STRING_TYPE][Types.STRING_TYPE][Operations.EQUAL] = Types.STRING_TYPE
semantic_cube[Types.STRING_TYPE][Types.STRING_TYPE][Operations.PLUS] = Types.STRING_TYPE
semantic_cube[Types.STRING_TYPE][Types.STRING_TYPE][Operations.EQUAL] = Types.BOOL_TYPE

semantic_cube[Types.INT_TYPE][Types.ADDR][Operations.PLUS] = semantic_cube[Types.ADDR][Types.INT_TYPE][Operations.PLUS] = Types.ADDR
semantic_cube[Types.INT_TYPE][Types.ADDR][Operations.MINUS] = semantic_cube[Types.ADDR][Types.INT_TYPE][Operations.MINUS] = Types.ADDR
semantic_cube[Types.INT_TYPE][Types.ADDR][Operations.EQUAL] = semantic_cube[Types.ADDR][Types.INT_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.STRING_TYPE][Types.ADDR][Operations.EQUAL] = semantic_cube[Types.ADDR][Types.STRING_TYPE][Operations.EQUAL] = Types.STRING_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.ADDR][Operations.EQUAL] = semantic_cube[Types.ADDR][Types.FLOAT_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.ADDR][Operations.EQUAL] = semantic_cube[Types.ADDR][Types.BOOL_TYPE][Operations.EQUAL] = Types.BOOL_TYPE
