import sys
import lex
import yacc
from utility.scope_tree import *
from utility.quad import *
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

# Values
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check if id is reserved keyword
    t.type = reserved.get(t.value, 'NAME')
    return t

t_FLOAT = r'((0|[1-9][0-9]*)\.[0-9][0-9]*)'
t_INT = r'(0|[1-9][0-9]*)'
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

# global_scope_counter_list = [0]
# # current_scope_counter = lambda global_scope_counter_list : global_scope_counter_list[0]
# scope_dict = {}
# global_scope = Scope(-1)
# scope_tree.dict[global_scope.ref] = global_scope
scope_tree = ScopeTree()
current_scope_ref = 0

start = 'program'

# Pending Operators
POper = []
# Pending Operands
PilaO = []
# Coresponding types
PTypes = []
# Pending Jumps
PJumps = []
# Counter for used temporary variables
temps_counter = 1
# List of quadruples
quad_list = [Quad(Operations.START)]

## Puntos Neuralgicos

def get_last_t(p):
    token = None
    n = 1
    while not token:
        token = p[-n]
        n += 1
    return token

# Cada ves que se lee un tipo de variable, no el literal (Ej. int, bool, float)
def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    # print(current_type)
    current_type = get_last_t(p)

# Cuando se abre un {} y se inicia un nuevo contexto.
def p_n_open_new_scope(p):
    'n_open_new_scope : '
    global current_scope_ref
    new_scope = Scope(scope_tree.dict[current_scope_ref].ref)
    scope_tree.add_scope(new_scope)
    current_scope_ref = new_scope.ref
    pass

# Cuando se cierra un {} y se cierra un contexto
def p_n_close_scope(p):
    'n_close_scope : '
    global current_scope_ref
    current_scope_ref = scope_tree.dict[current_scope_ref].parent_ref
    pass

# Cada vez que se lee un NAME y No se esta creando una variable nueva
def p_n_variable_reference(p):
    'n_variable_reference : '
    #look for var in variable tree
    var_name = get_last_t(p)
    aux_scope_ref = current_scope_ref
    while(aux_scope_ref > -1):
        if var_name in scope_tree.dict[aux_scope_ref].vars:
            global current_type
            current_type = scope_tree.dict[aux_scope_ref].vars[var_name]['type']
            return
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    e_error(f"Variable {var_name} referenced before instantiated", p)
    pass

# Cada vez que se lee un Name y se esta creando una variable, esto tambien
# aplica en los parametros de las funciones
def p_n_variable_instantiate(p):
    'n_variable_instantiate : '
    var_name = get_last_t(p)
    scope_tree.dict[current_scope_ref].set_variable(var_name, current_type)

# Puntos neuralgico s para procesar expresiones arithmeticas/matematicas
def p_n_math_expression_1_int(p):
    'n_math_expression_1_int : '
    n_math_expression(get_last_t(p), Types.INT_TYPE)
    pass

def p_n_math_expression_1_float(p):
    'n_math_expression_1_float : '
    n_math_expression(get_last_t(p), Types.FLOAT_TYPE)
    pass

def p_n_math_expression_1_string(p):
    'n_math_expression_1_string : '
    n_math_expression(get_last_t(p), Types.STRING_TYPE)
    pass

def p_n_math_expression_1_name(p):
    'n_math_expression_1_name : '
    var_name = get_last_t(p)
    n_math_expression(var_name, types_map[current_type])
    pass

def n_math_expression(token, type):
    PilaO.append(token)
    PTypes.append(type)
    pass

def p_n_math_expression_2(p):
    'n_math_expression_2 : '
    POper.append(operations_map[get_last_t(p)])
    pass

def p_n_math_expression_3(p):
    'n_math_expression_3 : '
    POper.append(operations_map[get_last_t(p)])
    pass

def p_n_math_expression_4(p):
    'n_math_expression_4 : '
    e = n_math_expression_gen_quad([Operations.PLUS, Operations.MINUS])
    if(e):
        e_error(e, p)
    pass

def p_n_math_expression_5(p):
    'n_math_expression_5 : '
    e = n_math_expression_gen_quad([Operations.TIMES, Operations.DIVIDE])
    if(e):
        e_error(e, p)
    pass

def p_n_math_expression_6(p):
    'n_math_expression_6 : '
    POper.append(get_last_t(p))
    pass

def p_n_math_expression_7(p):
    'n_math_expression_7 : '
    POper.pop()
    pass

def p_n_math_expression_8(p):
    'n_math_expression_8 : '
    POper.append(operations_map[get_last_t(p)])
    pass

def p_n_math_expression_9(p):
    'n_math_expression_9 : '
    # procesar operadores relacionales
    e = n_math_expression_gen_quad([
        Operations.LESSTHAN,
        Operations.GREATERTHAN,
        Operations.EQUALEQUAL,
        Operations.NOTEQUAL,
        Operations.LESSTHANOREQUAL,
        Operations.GREATERTHANOREQUAL,
    ])
    if(e):
        e_error(e, p)
    pass

def p_n_math_expression_10(p):
    'n_math_expression_10 : '
    # pushear operadores logicos
    POper.append(operations_map[get_last_t(p)])
    pass

def p_n_math_expression_11(p):
    'n_math_expression_11 : '
    # procesar operadores and
    e = n_math_expression_gen_quad([Operations.AND])
    if e:
        e_error(e, p)
    pass

def p_n_math_expression_12(p):
    'n_math_expression_12 : '
    # procesar operadores or
    e = n_math_expression_gen_quad([Operations.OR])
    if e:
        e_error(e, p)
    pass

def n_math_expression_gen_quad(operadores):
    if len(POper) == 0:
        pass
    elif POper[-1] in operadores:
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        operator = POper.pop()
        result_type = semantic_cube[left_type][right_type][operator]
        if result_type:
            global temps_counter
            result = f"t{temps_counter}"
            temps_counter += 1
            temp_quad = Quad(operator, left_operand, right_operand, result)
            quad_list.append(temp_quad)
            PilaO.append(result)
            PTypes.append(result_type)
            # TODO si algun operand es temparal(t#) entonces regresarla a "AVAILABLE", se puede volver a usar
        else:
            return f"Type Mismatch: left[type: {left_type}, op: {left_operand}]"\
                f" operator[{operator}]"\
                f" right[type: {right_type}, op: {right_operand}]"

def p_n_two_way_conditional_1(p):
    'n_two_way_conditional_1 : '
    exp_type = PTypes.pop()
    if(exp_type != Types.BOOL_TYPE):
        e_error("Type Mismatch in two way conditional", p)
    else:
        result = PilaO.pop()
        temp_quad = Quad(Operations.GOTOF, result)
        quad_list.append(temp_quad)
        cont = len(quad_list)
        PJumps.append(cont-1)
    pass

def p_n_two_way_conditional_2(p):
    'n_two_way_conditional_2 : '
    end = PJumps.pop()
    cont = len(quad_list)
    quad_list[end].target = cont
    pass

def p_n_two_way_conditional_3(p):
    'n_two_way_conditional_3 : '
    temp_quad = Quad(Operations.GOTO)
    quad_list.append(temp_quad)
    jump_false = PJumps.pop()
    cont = len(quad_list)
    PJumps.append(cont-1)
    quad_list[jump_false].target = cont
    pass

def p_n_pre_condition_loop_1(p):
    'p_n_pre_condition_loop_1 : '
    cont = len(quad_list)
    PJumps.append(cont)
    pass

def p_n_pre_condition_loop_2(p):
    'p_n_pre_condition_loop_2 : '
    exp_type = PTypes.pop()
    if(exp_type != Types.BOOL_TYPE):
        e_error("Type Mismatch in pre condition loop", p)
    else:
        result = PilaO.pop()
        temp_quad = Quad(Operations.GOTOF, result)
        quad_list.append(temp_quad)
        cont = len(quad_list)
        PJumps.append(cont-1)
    pass

def p_n_pre_condition_loop_3(p):
    'p_n_pre_condition_loop_3 : '
    end = PJumps.pop()
    return_jump = PJumps.pop()
    temp_quad = Quad(Operations.GOTO, target=return_jump)
    quad_list.append(temp_quad)
    cont = len(quad_list)
    quad_list[end].target = cont
    pass

def p_n_seen_equal_op(p):
    'n_seen_equal_op : '
    POper.append(operations_map[get_last_t(p)])
    pass

def do_assign():
    if len(POper) == 0:
        pass
    elif POper[-1] in [Operations.EQUAL]:
        left_operand = PilaO.pop()
        left_type = PTypes.pop()
        right_operand = PilaO.pop()
        right_type = PTypes.pop()
        operator = POper.pop()
        result_type = semantic_cube[left_type][right_type][operator]
        if result_type:
            temp_quad = Quad(operator, left_operand, target=right_operand)
            quad_list.append(temp_quad)
            # TODO si algun operand es temparal(t#) entonces regresarla a "AVAILABLE", se puede volver a usar
        else:
            return f"Type Mismatch: left[type: {left_type}, op: {left_operand}]"\
                f" operator[{operator}]"\
                f" right[type: {right_type}, op: {right_operand}]"
    pass

# Gramatica

## Track line numbers
def t_newline(t):
  r'[\n]+'
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
    parameter : type NAME n_variable_instantiate
    '''
    pass

def p_expression(p):
    '''
    expression : expression_or
    | expression_or AND n_math_expression_10 expression n_math_expression_11
    '''
    pass

def p_expression_or(p):
    '''
    expression_or : expression_rel
    | expression_rel OR n_math_expression_10 expression_or n_math_expression_12
    '''
    pass

def p_expression_rel(p):
    '''
    expression_rel : exp
    | exp relational_operator exp n_math_expression_9
    '''
    pass

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
    | NAME n_variable_reference n_math_expression_1_name
    '''
    pass

def p_assign(p):
    '''
    assign : type NAME n_variable_instantiate n_math_expression_1_name EQUAL n_seen_equal_op expression
    | NAME n_variable_reference n_math_expression_1_name EQUAL n_seen_equal_op expression
    '''
    e = do_assign()
    if e:
        e_error(e, p)
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
    whileloop : WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope
    '''
    pass

def p_forloop(p):
    '''
    forloop : FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope
    '''
    pass

def p_condition_if(p):
    '''
    condition_if : IF LPARENTHESIS expression RPARENTHESIS LCURLY n_two_way_conditional_1 n_open_new_scope codeblock RCURLY n_close_scope condition_else n_two_way_conditional_2
    '''
    pass

def p_condition_else(p):
    '''
    condition_else : ELSE n_two_way_conditional_3 LCURLY n_open_new_scope codeblock RCURLY n_close_scope
    | empty
    '''
    pass

## Utility

def print_scope_tree():
    print("--Scope Tree")
    print(scope_tree)

def print_variable_scopes():
    print("--Variable scopes")
    [print(scope_tree.dict[ref]) for ref in range(0, scope_tree.counter)]

def print_pilas():
    print(f"--PilaO: {PilaO}\n--PTypes: {PTypes}\n--POper: {POper}")

def print_quads():
    print("--Quads")
    [print(f"{ref} {quad_list[ref]}") for ref in range(0, len(quad_list))]

# Error handling for semantic exceptions
def e_error(e, p):
    raise Exception(f"{e} in line: {p.lineno(-1)}")

# Error handling lexer
def t_error(t):
    print(f"Illegal character {t}")
    t.lexer.skip(1)

# Error handling parser
def p_error(p):
    print("p_error called")
    if not p:
        print("End of File!")
        return
    print(f"Error {p}")
    sys.exit()

# Build the lexer
lexer = lex.lex()
# Build the parser
parser = yacc.yacc()

user_input = int(
    input("1.Programa valido\
    \n2.Programa no valido\
    \n3.Documento Mock\
    \n4.Complex variable\
    \n5.If Else\
    \n6.While\n"))

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
            int suma = A + B and C >= D or B;
            '''

elif user_input == 5:
    data = '''
            OwO
            if (A + B < C) {
                A = B + C;
            } else {
                A = B + C * D;
            }
            '''

elif user_input == 6:
    data = '''
    OwO
    int A = 4;

    while (A > B * C) {
        A = A - D;
    }
    B = C + A;
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


print_variable_scopes()
# print_pilas()
print_quads()
