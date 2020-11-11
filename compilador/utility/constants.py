from collections import defaultdict
from enum import Enum, IntEnum, auto

# MEMORY RANGES
# TODO: Add this before moving on?

# DATA TYPES 
class Types(Enum):
  INT_TYPE = 'int'
  FLOAT_TYPE = 'float'
  BOOL_TYPE = 'bool'
  STRING_TYPE = 'string'
  VOID = 'void'

class Operations(IntEnum):
  # OPERATORS
  PLUS    = 1
  MINUS   = 2
  TIMES   = 3 
  DIVIDE  = 4
  MODULUS = 5 # deprecated
  # Logical Operators
  AND = 6
  OR = 7
  NOT = 8
  # Relational Operators
  EQUAL = 9
  LESSTHAN = 10
  GREATERTHAN = 11
  EQUALEQUAL = 12
  NOTEQUAL = 13
  LESSTHANOREQUAL = 14
  GREATERTHANOREQUAL = 15
  # MISC
  PLUSUNARY = 16
  MINUSUNARY = 17

semantic_cube = defaultdict(
  lambda: defaultdict(lambda: defaultdict(lambda: None)))

semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.PLUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.MINUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.TIMES] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.DIVIDE] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.INT_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.PLUSUNARY] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.MINUSUNARY] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.PLUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.MINUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.TIMES] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.DIVIDE] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.FLOAT_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.PLUSUNARY] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.MINUSUNARY] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.PLUS] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.MINUS] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.TIMES] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.DIVIDE] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.BOOL_TYPE][Operations.EQUAL] = Types.BOOL_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.PLUSUNARY] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.MINUSUNARY] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Operations.NOT] = Types.BOOL_TYPE

semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.AND] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.OR] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHAN] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHAN] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.NOTEQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.EQUALEQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.LESSTHANOREQUAL] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.PLUS] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.PLUS] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.MINUS] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.MINUS] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.TIMES] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.TIMES] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.DIVIDE] = semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.DIVIDE] = Types.FLOAT_TYPE
semantic_cube[Types.INT_TYPE][Types.FLOAT_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.INT_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE

semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.AND] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.OR] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.LESSTHAN] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.GREATERTHAN] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.NOTEQUAL] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.EQUALEQUAL] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.LESSTHANOREQUAL] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.PLUS] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.PLUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.MINUS] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.MINUS] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.TIMES] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.TIMES] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.DIVIDE] = semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.DIVIDE] = Types.INT_TYPE
semantic_cube[Types.INT_TYPE][Types.BOOL_TYPE][Operations.EQUAL] = Types.INT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.INT_TYPE][Operations.EQUAL] = Types.BOOL_TYPE

semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.AND] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.AND] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.OR] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.OR] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.LESSTHAN] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.LESSTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.GREATERTHAN] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.GREATERTHAN] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.NOTEQUAL] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.NOTEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.EQUALEQUAL] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.EQUALEQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.LESSTHANOREQUAL] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.LESSTHANOREQUAL] = Types.BOOL_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.PLUS] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.PLUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.MINUS] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.MINUS] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.TIMES] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.TIMES] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.DIVIDE] = semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.DIVIDE] = Types.FLOAT_TYPE
semantic_cube[Types.FLOAT_TYPE][Types.BOOL_TYPE][Operations.EQUAL] = Types.FLOAT_TYPE
semantic_cube[Types.BOOL_TYPE][Types.FLOAT_TYPE][Operations.EQUAL] = Types.BOOL_TYPE
