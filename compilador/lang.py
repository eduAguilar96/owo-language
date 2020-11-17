import sys
import lex
import yacc
from scope_tree import ScopeTree
from utility.constants import *

reserved = {
    # Types
    'int': 'INT_TYPE',
    'double': 'DOUBLE_TYPE',
    'float': 'FLOAT_TYPE',
    'string': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'void': 'VOID',
    # Program
    'function': 'FUNCTION',
    'OwO': 'OWO',
    'CHIEF/AARON': 'IDK',
    # Flow
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    #logical
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

# Tokens
tokens = [
    # Values
    'NAME', 'INT', 'FLOAT', 'STRING',
    # Arithmetic operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULUS',
    # Encapsulators
    'LPARENTHESIS','RPARENTHESIS', 'LCURLY', 'RCURLY', 'LBRACKET', 'RBRACKET',
    # Punctuations
    'DOT', 'COMMA', 'DOUBLEDOT', 'SEMICOLON',
    # Comparators
    'EQUAL', 'LESSTHAN', 'GREATERTHAN',
    # Compound Comparators
    'EQUALEQUAL', 'NOTEQUAL', 'LESSTHANOREQUAL', 'GREATERTHANOREQUAL',
] + list(reserved.values())

#Tokens to Enum
operations_map = {
  '+': Operations.PLUS,
  '-': Operations.MINUS,
  '*': Operations.TIMES,
  '/': Operations.DIVIDE,
  '%': Operations.MODULUS,
  '=': Operations.EQUAL,
  '<': Operations.LESSTHAN,
  '>': Operations.GREATERTHAN,
  '==': Operations.EQUALEQUAL,
  '!=': Operations.NOTEQUAL,
  '<=': Operations.LESSTHANOREQUAL,
  '>=': Operations.GREATERTHANOREQUAL,
  'and': Operations.AND,
  'or': Operations.OR,
}

# Values
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check if id is reserved keyword
    t.type = reserved.get(t.value, 'NAME')
    return t

t_FLOAT = r'([0-9]*\.[0-9]*)'
t_INT = r'([1-9][0-9]*)'
t_STRING = r'\".*\"'

# Arithmetic operators
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MODULUS = r'%'

# Encapsulators
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Punctuations
t_DOT = r'\.'
t_COMMA = r'\,'
t_DOUBLEDOT = r':'
t_SEMICOLON = r';'

# Comparators
t_EQUAL = r'='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'

# Compound Comparators
t_EQUALEQUAL = r'=='
t_NOTEQUAL = r'!='
t_LESSTHANOREQUAL = r'<='
t_GREATERTHANOREQUAL = r'>='

# A string containing ignored characters
t_ignore = ' \t'

# Comments
t_ignore_COMMENT = r'\#.*'

# dictionary of names (for storing variables)
current_type = None

global_scope_counter_list = [0]
# current_scope_counter = lambda global_scope_counter_list : global_scope_counter_list[0]
scope_dict = {}
global_scope = ScopeTree(global_scope_counter_list, -1)
scope_dict[global_scope.ref] = global_scope
current_scope_ref = global_scope.ref
print(f" verificar {global_scope_counter_list[0]} == 1")


start = 'program'

## Puntos Neuralgicos

# Cada ves que se lee un tipo de variable, no el literal (Ej. int, bool, float)
def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    # print(current_type)
    current_type = p[-1]

# Cuando se abre un {} y se inicia un nuevo contexto.
def p_n_open_new_scope(p):
    'n_open_new_scope : '
    global current_scope_ref
    new_scope = ScopeTree(global_scope_counter_list, scope_dict[current_scope_ref].ref)
    scope_dict[new_scope.ref] = new_scope
    current_scope_ref = new_scope.ref
    pass

# Cuando se cierra un {} y se cierra un contexto
def p_n_close_scope(p):
    'n_close_scope : '
    global current_scope_ref
    current_scope_ref = scope_dict[current_scope_ref].parent_ref
    pass

# Cada vez que se lee un NAME
def p_n_name(p):
    'n_name : '
    scope_dict[current_scope_ref].set_variable(p[-1], current_type)
    pass

POper = []
PilaO = []
PTypes = []
quad_counter = 1
temps_counter = 1

# Puntos neuralgico s para procesar expresiones arithmeticas/matematicas
def p_n_math_expression_1_int(p):
    'n_math_expression_1_int : '
    n_math_expression(p[-1], Types.INT_TYPE)
    pass

def p_n_math_expression_1_float(p):
    'n_math_expression_1_float : '
    n_math_expression(p[-1], Types.FLOAT_TYPE)
    pass

def p_n_math_expression_1_string(p):
    'n_math_expression_1_string : '
    n_math_expression(p[-1], Types.STRING_TYPE)
    pass

def p_n_math_expression_1_name(p):
    'n_math_expression_1_name : '
    # TODO mientras no tenemos la logica para que tipo es una variable, usar int
    n_math_expression(p[-1], Types.INT_TYPE)
    pass

def n_math_expression(token, type):
    PilaO.append(token)
    PTypes.append(type)
    pass

def p_n_math_expression_2(p):
    'n_math_expression_2 : '
    POper.append(operations_map[p[-1]])
    pass

def p_n_math_expression_3(p):
    'n_math_expression_3 : '
    POper.append(operations_map[p[-1]])
    pass

def p_n_math_expression_4(p):
    'n_math_expression_4 : '
    n_math_expression_4_punto_5([Operations.PLUS, Operations.MINUS])
    pass

def p_n_math_expression_5(p):
    'n_math_expression_5 : '
    n_math_expression_4_punto_5([Operations.TIMES, Operations.DIVIDE])
    pass

def n_math_expression_4_punto_5(operadores):
    if len(POper) == 0:
        pass
    elif POper[-1] in operadores:
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()
        result_type = semantic_cube[left_type][right_type][operator]
        # print("result_type: " + str(result_type))
        # print(f"{left_type} {right_type} {operator}")
        if result_type:
            global temps_counter
            result = f"t{temps_counter}"
            temps_counter += 1
            global quad_counter
            print(f"{quad_counter} {operator}, {left_operand}, {right_operand}, {result}")
            quad_counter += 1
            PilaO.append(result)
            PTypes.append(result_type)
            # TODO si algun operand es temparal(t#) entonces regresarla a "AVAILABLE", se puede volver a usar
        else:
            raise Exception("Type Mismatch")

def p_n_math_expression_6(p):
    'n_math_expression_6 : '
    POper.append(p[-1])
    pass

def p_n_math_expression_7(p):
    'n_math_expression_7 : '
    POper.pop()
    pass

def p_n_math_expression_8(p):
    'n_math_expression_8 : '
    POper.append(operations_map[p[-1]])
    pass

def p_n_math_expression_9(p):
    'n_math_expression_9 : '
    # procesar operadores relacionales
    n_math_expression_4_punto_5([
        Operations.LESSTHAN,
        Operations.GREATERTHAN,
        Operations.EQUALEQUAL,
        Operations.NOTEQUAL,
        Operations.LESSTHANOREQUAL,
        Operations.GREATERTHANOREQUAL,
    ])
    pass

def p_n_math_expression_10(p):
    'n_math_expression_10 : '
    # pushear operadores logicos
    POper.append(operations_map[p[-1]])
    pass

def p_n_math_expression_11(p):
    'n_math_expression_11 : '
    # procesar operadores and
    n_math_expression_4_punto_5([Operations.AND])
    pass

def p_n_math_expression_12(p):
    'n_math_expression_12 : '
    # procesar operadores or
    n_math_expression_4_punto_5([Operations.OR])
    pass

# Gramatica

## Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_program(p):
    '''
    program : program_aux codeblock
    '''
    pass

def p_program_aux(p):
    '''
    program_aux : IDK
    | OWO
    '''
    pass

def p_type(p):
    '''
    type : INT_TYPE n_seen_type
    | STRING_TYPE n_seen_type
    | DOUBLE_TYPE n_seen_type
    | FLOAT_TYPE n_seen_type
    | BOOL_TYPE n_seen_type
    '''
    pass

def p_relational_operator(p):
    '''
    relational_operator : GREATERTHAN n_math_expression_8
    | LESSTHAN n_math_expression_8
    | EQUALEQUAL n_math_expression_8
    | LESSTHANOREQUAL n_math_expression_8
    | GREATERTHANOREQUAL n_math_expression_8
    | NOTEQUAL n_math_expression_8
    '''
    pass

# TODO todavia no implementamos el not
# def p_logical_operator(p):
#     '''
#     logical_operator : AND n_math_expression_10
#     | OR n_math_expression_10
#     | NOT n_math_expression_10
#     '''
#     pass

# def p_arithmetic_operator(p):
#     '''
#     arithmetic_operator : PLUS
#     | MINUS
#     | TIMES
#     | DIVIDE
#     | MODULUS
#     '''
#     pass

def p_literal(p):
    '''
    literal : FLOAT n_math_expression_1_float
    | INT n_math_expression_1_int
    | STRING n_math_expression_1_string
    '''
    pass

def p_function_type(p):
    '''
    function_type : type
    | VOID
    '''
    pass

def p_function_definition(p):
    '''
    function_definition : FUNCTION NAME n_open_new_scope parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY n_close_scope
    '''
    pass

def p_function_call(p):
    '''
    function_call : NAME LPARENTHESIS parameter_list RPARENTHESIS
    '''
    pass

def p_parameter_list(p):
    '''
    parameter_list : empty
    | parameter
    | parameter COMMA parameter_list
    '''
    pass

def p_parameter(p):
    '''
    parameter : type NAME n_name
    | assign
    '''
    pass

# TODO borrar comentario
# p_expression
def p_expression(p):
    '''
    expression : expression_or
    | expression_or AND n_math_expression_10 expression n_math_expression_11
    '''
    pass

# TODO borrar comentario
# p_exp
def p_expression_or(p):
    '''
    expression_or : expression_rel
    | expression_rel OR n_math_expression_10 expression_or n_math_expression_12
    '''
    pass

# TODO borrar comentario
# p_xp
def p_expression_rel(p):
    '''
    expression_rel : exp
    | exp relational_operator exp n_math_expression_9
    '''
    pass

# TODO borrar comentario
# p_x
def p_exp(p):
    '''
    exp : termino n_math_expression_4
    | termino n_math_expression_4 PLUS n_math_expression_2 exp
    | termino n_math_expression_4 MINUS n_math_expression_2 exp
    '''
    pass

def p_termino(p):
    '''
    termino : factor n_math_expression_5
    | factor n_math_expression_5 TIMES n_math_expression_3 termino
    | factor n_math_expression_5 DIVIDE n_math_expression_3 termino
    | factor n_math_expression_5 MODULUS n_math_expression_3 termino
    '''
    pass

def p_factor(p):
    '''
    factor : LPARENTHESIS n_math_expression_6 expression RPARENTHESIS n_math_expression_7
    | PLUS value
    | MINUS value
    | value
    '''
    pass

# TODO falta agregar n_math_expression_1 para function_call
def p_value(p):
    '''
    value : function_call
    | literal
    | NAME n_math_expression_1_name
    '''
    pass

def p_assign(p):
    '''
    assign : type NAME n_name EQUAL expression
    | NAME n_name EQUAL expression
    '''
    pass

def p_statement(p):
    '''
    statement : statement_aux SEMICOLON
    '''
    pass

def p_statement_aux(p):
    '''
    statement_aux : assign
    | function_call
    '''
    # | PRINT
    pass

def p_codeblock(p):
    '''
    codeblock : empty
    | codeblock_aux codeblock
    '''
    pass

def p_codeblock_aux(p):
    '''
    codeblock_aux : statement
    | function_definition
    | condition_if
    | loop
    '''
    pass

def p_loop(p):
    '''
    loop : forloop
    | whileloop
    '''
    pass

def p_whileloop(p):
    '''
    whileloop : WHILE LPARENTHESIS expression RPARENTHESIS LCURLY n_open_new_scope codeblock RCURLY n_close_scope
    '''
    pass

def p_forloop(p):
    '''
    forloop : FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope
    '''
    pass

def p_condition_if(p):
    '''
    condition_if : IF LPARENTHESIS expression RPARENTHESIS LCURLY n_open_new_scope codeblock RCURLY n_close_scope condition_else
    '''
    pass

def p_condition_else(p):
    '''
    condition_else : ELSE LCURLY n_open_new_scope codeblock RCURLY n_close_scope
    | empty
    '''
    pass

# Error handling lexer
def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Error handling parser
def p_error(p):
    print("p_error called")
    if not p:
        print("End of File!")
        return
    print("error")
    print(f"Error {p}")
    sys.exit()

# Build the lexer
lexer = lex.lex()
# Build the parser
parser = yacc.yacc()

user_input = int(
    input("1.Programa valido\n2.Programa no valido\n3.Documento Mock\n"))

data = ""

if user_input == 1:
    data = '''
            OwO
            int nombre = 12345;
            '''

elif user_input == 2:
    data = '''
        OwO
        int nombre = 12345;
        estoEstaMal *()+`'''

elif user_input == 3:
    f = open("test.txt", "r")
    if f.mode == 'r':
        data = f.read()
    else:
        print("404: File not found")

elif user_input == 4:
    data = '''
            OwO
            int suma = A + B and C < D or B;
            '''

# Read input in lexer
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    # print(tok)

result = parser.parse(data)
# print(result)
def print_variable_scopes():
    print("--Variable scopes")
    [print(scope_dict[ref]) for ref in range(0, global_scope_counter_list[0])]
def print_pilas():
    print(f"--PilaO: {PilaO}\n--PTypes: {PTypes}\n--POper: {POper}")
# print_variable_scopes()
print_pilas()
