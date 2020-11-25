from kivy.app import App
from kivy.extras.highlight import KivyLexer
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.behaviors import EmacsBehavior
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from pygments import lexers
from kivy.support import install_twisted_reactor

import codecs
import os

# Compiler imports
import sys
import lex
import yacc
# from compilador.examples import *
from compilador.vm import VirtualMachine
from compilador.utility.semantic_scope_tree import Scope, SemanticScopeTree
from compilador.utility.quad import Quad
# from compilador.utility.constants import *
from compilador.utility.constants import Types, Operations, operations_map, semantic_cube, types_map

### SUPER GLOBAL VARIABLES
current_code = '''
OwO
print(10*5);
string name = input_s();
print("String input: " + name);
int i = input_i();
print("Int input: ");
print(i);
float f = input_f();
print("Float input: ");
print(f);
'''

# input = 0
# output = 1
# err = 2
# status = 3
stdoutin= ['', '', '', '']

### COMPILER


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
    'return': 'RETURN',
    'OwO': 'OWO',
    'CHIEF/AARON': 'IDK',
    'print': 'PRINT',
    'input_s': 'INPUTSTRING',
    'input_i': 'INPUTINT',
    'input_f': 'INPUTFLOAT',
    # Flow
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    #logical
    'and': 'AND',
    'or': 'OR',
    # 'not': 'NOT',
    'True': 'TRUE',
    'False': 'FALSE',
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
    'COMMA', 'DOUBLEDOT', 'SEMICOLON',
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
t_STRING = r'("(\\"|[^"])*")'

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

current_type = None
# Scope tree for storing variables and functions
scope_tree = SemanticScopeTree()
current_scope_ref = 0

constants_table = {}
# Pending Operators
POper = []
# Pending Operands
PilaO = []
# Coresponding types
PTypes = []
# Pending Jumps
PJumps = []
# Counter for used temporary variables
# Used for creating names for temporary variables in debuging output
temps_counter = 1

# Size for each independent memory stack
DIR_SIZE = 1000

DIR_INT = 1000
dir_last_empty_int = DIR_INT

DIR_STRING = DIR_INT + DIR_SIZE
dir_last_empty_string = DIR_STRING

DIR_FLOAT = DIR_STRING + DIR_SIZE
dir_last_empty_float = DIR_FLOAT

DIR_BOOL =  DIR_FLOAT + DIR_SIZE
dir_last_empty_bool = DIR_BOOL
# List of quadruples with addresses
quad_addr_list = [Quad(Operations.START)]
# List of quadruples
quad_list = [Quad(Operations.START)]

# Verify that function exists and do the ERA quad
last_function_call = []
argument_counter = []
virtual_var_list = []
last_arr_name_stack = []
# stack to store the tokens for the the index's written for an array's size Ej: [i]
arr_size_stack = []

start = 'program'

# Resets every global variable
def init_compiler():
    global current_type 
    global scope_tree
    global current_scope_ref
    global constants_table
    global POper
    global PilaO
    global PTypes
    global PJumps
    global temps_counter
    global DIR_SIZE
    global DIR_INT
    global dir_last_empty_int
    global DIR_STRING
    global dir_last_empty_string
    global DIR_FLOAT
    global dir_last_empty_float
    global DIR_BOOL
    global dir_last_empty_bool
    global quad_addr_list
    global quad_list 
    global stdoutin
    global last_function_call 
    global argument_counter
    global virtual_var_list
    global last_arr_name_stack
    global arr_size_stack

    stdoutin = ['', '', '', '']
    current_type = None
    # Scope tree for storing variables and functions
    scope_tree = SemanticScopeTree()
    current_scope_ref = 0
    constants_table = {}
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
    DIR_SIZE = 1000
    DIR_INT = 1000
    dir_last_empty_int = DIR_INT
    DIR_STRING = DIR_INT + DIR_SIZE
    dir_last_empty_string = DIR_STRING
    DIR_FLOAT = DIR_STRING + DIR_SIZE
    dir_last_empty_float = DIR_FLOAT
    DIR_BOOL =  DIR_FLOAT + DIR_SIZE
    dir_last_empty_bool = DIR_BOOL
    # List of quadruples with addresses
    quad_addr_list = [Quad(Operations.START)]
    # List of quadruples
    quad_list = [Quad(Operations.START)]
    # Verify that function exists and do the ERA quad
    last_function_call = []
    argument_counter = []
    virtual_var_list = []
    last_arr_name_stack = []
    # stack to store the tokens for the the index's written for an array's size Ej: [i]
    arr_size_stack = []

# Runs compiler, receives code as arg 
def run_compiler(code):# Build the lexer
    init_compiler()
    lexer = lex.lex(optimize=1)
    # Build the parser
    parser = yacc.yacc(optimize=1)
    # Read input in lexer
    lexer.input(code)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
    # print(tok)

    result = parser.parse(code)
    return result


# Error check if there is no more memory for a memoery stack
def check_out_of_mem(last_used_addr, initial_addr):
    if(last_used_addr >= DIR_SIZE + initial_addr):
        raise Exception("OwO: Out of memory")

# Get the address of a variable, return -1 if not found
def get_var_addr(var, var_type):
    aux_scope_ref = current_scope_ref
    while aux_scope_ref > -1:
        vars_table = scope_tree.dict[aux_scope_ref].vars
        if var in vars_table:
            var_addr = vars_table[var]['addr']
            if var_addr != -1:
                return var_addr
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    return -1

def is_constant(token):
    token = str(token)
    return token[0] == '"' or token[0].isdigit() or token == "True" or token == "False"

# Get and/or generate the address for a variable or constant
def get_addr(value, value_type):
    # print(f"Getting address for{value}, is_constant={is_constant}")
    if is_constant(value):
        if value in constants_table:
            return constants_table[value]['addr']
    else:
        # Check if variable already exists
        addr = get_var_addr(value, value_type)
        if addr != -1:
            return addr

    # Variable/constant is NEW, create new addr
    global dir_last_empty_int
    if(value_type == Types.INT_TYPE):
        check_out_of_mem(dir_last_empty_int, DIR_INT)
        addr = dir_last_empty_int
        dir_last_empty_int += 1
    elif(value_type == Types.STRING_TYPE):
        global dir_last_empty_string
        check_out_of_mem(dir_last_empty_string, DIR_STRING)
        addr = dir_last_empty_string
        dir_last_empty_string += 1
    elif(value_type == Types.FLOAT_TYPE):
        global dir_last_empty_float
        check_out_of_mem(dir_last_empty_float, DIR_FLOAT)
        addr = dir_last_empty_float
        dir_last_empty_float += 1
    elif(value_type == Types.BOOL_TYPE):
        global dir_last_empty_bool
        check_out_of_mem(dir_last_empty_bool, DIR_BOOL)
        addr = dir_last_empty_bool
        dir_last_empty_bool += 1
    elif(value_type == Types.ADDR):
        check_out_of_mem(dir_last_empty_int, DIR_INT)
        addr = dir_last_empty_int
        dir_last_empty_int += 1
    elif(value_type == Types.VOID):
        addr = -1
    else:
        raise Exception(f"OwO: Attempting to generate address for unkown variable type ({value_type})")

    return addr


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
    current_type = types_map[get_last_t(p)]

# Cuando se abre un {} y se inicia un nuevo contexto.
def p_n_open_new_scope(p):
    'n_open_new_scope : '
    global current_scope_ref
    new_scope = Scope(scope_tree.dict[current_scope_ref].ref)
    scope_tree.add_scope(new_scope)
    current_scope_ref = new_scope.ref
    pass

# Cuando se abre un {} y se inicia un nuevo contexto.
def p_n_open_new_scope_function(p):
    'n_open_new_scope_function : '
    global current_scope_ref
    func_name = get_last_t(p)
    # Add function name to current scope
    scope_tree.dict[current_scope_ref].functions[func_name] = -1
    # Create new scope
    new_scope = Scope(scope_tree.dict[current_scope_ref].ref)
    new_scope.func_name = func_name
    scope_tree.add_scope(new_scope)
    # Set current scope to new scope
    current_scope_ref = new_scope.ref
    # Add reference for new/current scope to scope parent.functions
    parent_ref = scope_tree.dict[current_scope_ref].parent_ref
    scope_tree.dict[parent_ref].functions[func_name] = current_scope_ref
    # Add reference for new/current scope to itself.functions
    scope_tree.dict[current_scope_ref].functions[func_name] = current_scope_ref
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

# Cada vez que se lee un Name y se esta creando una variable, no aplica para
# los parametros de las funciones
def p_n_variable_instantiate(p):
    'n_variable_instantiate : '
    var_name = get_last_t(p)
    var_addr = get_addr(var_name, current_type)
    scope_tree.dict[current_scope_ref].add_variable(var_name, current_type, var_addr)

# Cada vez que se lee un Name y se esta creando una variable en los parametros
# de una funcion
def p_n_variable_instantiate_param(p):
    'n_variable_instantiate_param : '
    var_name = get_last_t(p)
    var_addr = get_addr(var_name, current_type)
    scope_tree.dict[current_scope_ref].add_variable(var_name, current_type, var_addr)
    scope_tree.dict[current_scope_ref].add_parameter(var_name)

def insert_constant(constant, constant_type, addr=None):
    if constant in constants_table:
        return
    constants_table[constant] = {
            'addr': addr if addr else get_addr(constant, constant_type),
            'type': constant_type,
        }

# Puntos neuralgico s para procesar expresiones arithmeticas/matematicas
def p_n_math_expression_1_int(p):
    'n_math_expression_1_int : '
    token = get_last_t(p)
    insert_constant(token, Types.INT_TYPE)
    n_math_expression(token, Types.INT_TYPE)
    pass

def p_n_math_expression_1_float(p):
    'n_math_expression_1_float : '
    token = get_last_t(p)
    insert_constant(token, Types.FLOAT_TYPE)
    n_math_expression(token, Types.FLOAT_TYPE)
    pass

def p_n_math_expression_1_string(p):
    'n_math_expression_1_string : '
    token = get_last_t(p)
    # token = token.strip('"')
    insert_constant(token, Types.STRING_TYPE)
    n_math_expression(token, Types.STRING_TYPE)
    pass

def p_n_math_expression_1_bool(p):
    'n_math_expression_1_bool : '
    token = get_last_t(p)
    insert_constant(token, Types.BOOL_TYPE)
    n_math_expression(token, Types.BOOL_TYPE)

def p_n_math_expression_1_name(p):
    'n_math_expression_1_name : '
    var_name = get_last_t(p)
    n_math_expression(var_name, current_type)
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

# pushear operadores logicos
def p_n_math_expression_10(p):
    'n_math_expression_10 : '
    POper.append(operations_map[get_last_t(p)])
    pass

# procesar operadores and
def p_n_math_expression_11(p):
    'n_math_expression_11 : '
    e = n_math_expression_gen_quad([Operations.AND])
    if e:
        e_error(e, p)
    pass

# procesar operadores or
def p_n_math_expression_12(p):
    'n_math_expression_12 : '
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
            result = gen_temp_var()
            # Add to debug quad
            temp_quad = Quad(operator, left_operand, right_operand, result)
            quad_list.append(temp_quad)
            # Add to addr quad
            result_addr = get_addr(result, result_type)
            addr_quad = Quad(operator, get_addr(left_operand, left_type), get_addr(right_operand, right_type), result_addr)
            quad_addr_list.append(addr_quad)

            PilaO.append(result)
            PTypes.append(result_type)
            # Append variable temp a los scopes
            scope_tree.dict[current_scope_ref].add_variable(result, result_type, result_addr)
            # TODO si algun operand es temparal(t#) entonces regresarla a "AVAILABLE", se puede volver a usar
        else:
            return f"Type Mismatch: left[type: {left_type}, op: {left_operand}]"\
                f" operator[{operator}]"\
                f" right[type: {right_type}, op: {right_operand}]"

def p_n_two_way_conditional_1(p):
    'n_two_way_conditional_1 : '
    result_type = PTypes.pop()
    if(result_type != Types.BOOL_TYPE):
        e_error("Type Mismatch in two way conditional", p)
    else:
        result = PilaO.pop()
        # Adding to debug quad list
        temp_quad = Quad(Operations.GOTOF, result)
        quad_list.append(temp_quad)
        # Adding to addr quad list
        addr_quad = Quad(Operations.GOTOF, get_addr(result, result_type))
        quad_addr_list.append(addr_quad)
        cont = len(quad_list)
        PJumps.append(cont-1)
    pass

def p_n_two_way_conditional_2(p):
    'n_two_way_conditional_2 : '
    end = PJumps.pop()
    cont = len(quad_list)
    # Debuag quad list
    quad_list[end].target = cont
    # Addr quad list
    quad_addr_list[end].target = cont
    pass

def p_n_two_way_conditional_3(p):
    'n_two_way_conditional_3 : '
    # Debug Quad list
    temp_quad = Quad(Operations.GOTO)
    quad_list.append(temp_quad)
    # Addr quad list
    addr_quad = Quad(Operations.GOTO)
    quad_addr_list.append(addr_quad)

    jump_false = PJumps.pop()
    cont = len(quad_list)
    PJumps.append(cont-1)
    # Debug Quad list
    quad_list[jump_false].target = cont
    # Addr quad list
    quad_addr_list[jump_false].target = cont
    pass

def p_n_pre_condition_loop_1(p):
    'p_n_pre_condition_loop_1 : '
    cont = len(quad_list)
    PJumps.append(cont)
    pass

def p_n_pre_condition_loop_2(p):
    'p_n_pre_condition_loop_2 : '
    result_type = PTypes.pop()
    if(result_type != Types.BOOL_TYPE):
        e_error("Type Mismatch in pre condition loop", p)
    else:
        result = PilaO.pop()
        # Debug quad list
        temp_quad = Quad(Operations.GOTOF, result)
        quad_list.append(temp_quad)
        # Addr quad list
        addr_quad = Quad(Operations.GOTOF, get_addr(result, result_type))
        quad_addr_list.append(addr_quad)

        cont = len(quad_list)
        PJumps.append(cont-1)
    pass

def p_n_pre_condition_loop_3(p):
    'p_n_pre_condition_loop_3 : '
    end = PJumps.pop()
    return_jump = PJumps.pop()
    # Debug quad list
    temp_quad = Quad(Operations.GOTO, target=return_jump)
    quad_list.append(temp_quad)
    # Addr quad list
    addr_quad = Quad(Operations.GOTO, target=return_jump)
    quad_addr_list.append(addr_quad)

    cont = len(quad_list)
    # Debug quad list
    quad_list[end].target = cont
    # Addr quad list
    quad_addr_list[end].target = cont
    pass

def p_n_seen_equal_op(p):
    'n_seen_equal_op : '
    POper.append(operations_map[get_last_t(p)])
    pass

def do_assign_var():
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
            # Debug quad list
            temp_quad = Quad(operator, left_operand, target=right_operand)
            quad_list.append(temp_quad)
            # Addr quad list
            addr_quad = Quad(operator, get_addr(left_operand, left_type), target=get_addr(right_operand, right_type))
            quad_addr_list.append(addr_quad)
            # TODO si algun operand es temparal(t#) entonces regresarla a "AVAILABLE", se puede volver a usar
        else:
            return f"Type Mismatch: left[type: {left_type}, op: {left_operand}]"\
                f" operator[{operator}]"\
                f" right[type: {right_type}, op: {right_operand}]"
    pass

def p_n_before_function_definition(p):
    'n_before_function_definition : '
    PJumps.append(len(quad_list))
    # Debug quad list
    quad_list.append(Quad(Operations.GOTO))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.GOTO))
    pass

def p_n_function_block_start(p):
    'n_function_block_start : '
    scope_tree.dict[current_scope_ref].quad_start = len(quad_list)
    pass

def p_n_function_block_end(p):
    'n_function_block_end : '
    # Debug quad list
    quad_list.append(Quad(Operations.ENDFUNC))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.ENDFUNC))

    function_start = PJumps.pop()
    # Debug quad list
    quad_list[function_start].target = len(quad_list)
    # Addr quad list
    quad_addr_list[function_start].target = len(quad_list)
    pass

def p_n_function_type(p):
    'n_function_type : '
    type = types_map[get_last_t(p)]
    scope_tree.dict[current_scope_ref].return_type = type
    pass


def p_n_function_call_1(p):
    'n_function_call_1 : '
    # Insert false bottom to Operator stack
    POper.append('(')
    func_name = get_last_t(p)
    global last_function_call
    last_function_call.append(func_name)
    aux_scope_ref = current_scope_ref
    while(aux_scope_ref > -1):
        # check if function is child context
        if func_name in scope_tree.dict[aux_scope_ref].functions:
            func_ref = scope_tree.dict[aux_scope_ref].functions[func_name]
            # Se pasa una referencia a Que es scope es func_name con func_ref, esto en relacion al scope_tree
            func_quad = scope_tree.dict[func_ref].quad_start
            # Debug quad list
            quad_list.append(Quad(Operations.ERA, left=func_name, right=func_ref, target=func_quad))
            # Addr quad list
            quad_addr_list.append(Quad(Operations.ERA, left=func_name, right=func_ref, target=func_quad))
            return
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    e_error(f"Function {func_name} called before instantiated", p)
    pass


def p_n_function_call_2(p):
    'n_function_call_2 : '
    global argument_counter
    argument_counter.append(0)
    pass

# Verify Argument vs Parameter
def p_n_function_call_3(p):
    'n_function_call_3 : '
    global argument_counter
    argument_value = PilaO.pop()
    argument_type = PTypes.pop()
    function_name = last_function_call[-1]
    # Get function ref by traversing up scope tree
    aux_scope_ref = current_scope_ref
    while aux_scope_ref > -1:
        if function_name in scope_tree.dict[aux_scope_ref].functions:
            function_ref = scope_tree.dict[aux_scope_ref].functions[function_name]
            break
        else:
            aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    if aux_scope_ref == -1:
        e_error("Function called before instantiated", p)
    # Manage parms and args
    params_list = scope_tree.dict[function_ref].params
    if (argument_counter[-1] >= len(params_list)):
        e_error(f"Argument mismatch for function ({function_name}) call, args({argument_counter[-1]+1}), params({len(params_list)})", p)

    param_type = scope_tree.dict[function_ref].vars[params_list[argument_counter[-1]]]['type']
    if (argument_type != param_type):
        e_error(f"Type Mismatch for argument({params_list[argument_counter[-1]]}) in function ({function_name}) call", p)

    argument_temp = f"$param{argument_counter[-1]+1}"
    # Debug quad list
    quad_list.append(Quad(Operations.PARAM, left=argument_value, target=argument_temp))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.PARAM, left=get_addr(argument_value, argument_type), target=argument_temp))
    pass

def p_n_function_call_4(p):
    'n_function_call_4 : '
    global argument_counter
    argument_counter[-1] += 1
    pass

def p_n_function_call_5(p):
    'n_function_call_5 : '
    # Pop false bottom to Operator stack
    POper.pop()
    function_name = last_function_call[-1]
    # Get function ref by traversing up scope tree
    aux_scope_ref = current_scope_ref
    while aux_scope_ref > -1:
        if function_name in scope_tree.dict[aux_scope_ref].functions:
            function_ref = scope_tree.dict[aux_scope_ref].functions[function_name]
            break
        else:
            aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    if aux_scope_ref == -1:
        e_error("Function called before instantiated", p)
    params_list = scope_tree.dict[function_ref].params
    if (argument_counter[-1] != len(params_list)-1):
        e_error(f"Argument mismatch for function ({function_name}) call, args({argument_counter[-1]+1}), params({len(params_list)})", p)
    argument_counter.pop()
    pass

def p_n_function_call_6(p):
    'n_function_call_6 : '
    function_name = last_function_call[-1]
    # Get function ref by traversing up scope tree
    aux_scope_ref = current_scope_ref
    while aux_scope_ref > -1:
        if function_name in scope_tree.dict[aux_scope_ref].functions:
            function_ref = scope_tree.dict[aux_scope_ref].functions[function_name]
            break
        else:
            aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    if aux_scope_ref == -1:
        e_error("Function called before instantiated", p)
    function_type = scope_tree.dict[function_ref].return_type
    function_start_quad = scope_tree.dict[function_ref].quad_start
    params_list = scope_tree.dict[function_ref].params
    return_variable_name = f"${function_name}_return_value"
    return_variable_addr = get_addr(return_variable_name, function_type)
    # Se pasa una referencia a Que es scope es func_name con func_ref, esto en relacion al scope_tree
    # Debug Quad list
    quad_list.append(Quad(Operations.GOSUB, function_name, function_ref, function_start_quad))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.GOSUB, function_name, function_ref, function_start_quad))

    # Handle return_value
    temp_var = gen_temp_var()
    temp_var_type = scope_tree.dict[function_ref].return_type
    temp_var_addr = get_addr(temp_var, temp_var_type)
    PilaO.append(temp_var)
    PTypes.append(temp_var_type)
    scope_tree.dict[current_scope_ref].add_variable(return_variable_name, temp_var_type, return_variable_name)

    scope_tree.dict[current_scope_ref].add_variable(temp_var, temp_var_type, temp_var_addr)
    # Debug quad list
    quad_list.append(Quad(Operations.EQUAL, left=return_variable_name, target=temp_var))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.EQUAL, left=return_variable_name, target=temp_var_addr))

    last_function_call.pop()
    pass

def p_n_return(p):
    'n_return : '
    # thorw error if in global scope
    if(current_scope_ref == 0):
        e_error("Unable to use 'return' statement in global scope", p)

    # Get function ref by traversing up scope tree
    aux_scope_ref = current_scope_ref
    while aux_scope_ref > -1:
        if scope_tree.dict[aux_scope_ref].func_name:
            function_ref = aux_scope_ref
            break
        else:
            aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    if aux_scope_ref == -1:
        e_error("Function called before instantiated", p)

    # Get Function attributes
    func_name = scope_tree.dict[function_ref].func_name
    func_return_type = scope_tree.dict[function_ref].return_type

    # Break if void function
    if(func_return_type == Types.VOID):
        e_error(f"Void function ({func_name}) cannot have a return value", p)

    # Get return value
    return_value = PilaO.pop()
    return_type = PTypes.pop()
    if return_type != func_return_type:
        e_error(f"Wrong return type for ({func_name}), return type is ({return_type.value}), must be ({func_return_type.value})", p)
    return_var_name = f"${func_name}_return_value"

    # Debug Quad List
    quad_list.append(Quad(Operations.RETURN, left=return_var_name, target=return_value))
    # Addr Quad List
    quad_addr_list.append(Quad(Operations.RETURN, left=return_var_name, target=get_addr(return_value, return_type)))
    # Debug quad list
    quad_list.append(Quad(Operations.ENDFUNC))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.ENDFUNC))
    pass

def p_n_return_void(p):
    'n_return_void : '
    func_ref = current_scope_ref
    func_name = scope_tree.dict[func_ref].func_name
    e_error(f"Void function({func_name}) should not have a return", p)
    pass

def p_n_print(p):
    'n_print : '
    s = PilaO.pop()
    str_type = PTypes.pop()
    # if str_type != Types.STRING_TYPE:
    #     e_error("Cannot print non STRING value" ,p)
    # Debug Quad list
    quad_list.append(Quad(Operations.PRINT, target=s))
    # Addr Quad list
    quad_addr_list.append(Quad(Operations.PRINT, target=get_addr(s, str_type)))
    pass

def p_n_input_string(p):
    'n_input_string : '
    n_input(Types.STRING_TYPE, Operations.INPUTSTRING)
    pass

def p_n_input_int(p):
    'n_input_int : '
    n_input(Types.INT_TYPE, Operations.INPUTINT)
    pass

def p_n_input_float(p):
    'n_input_float : '
    n_input(Types.FLOAT_TYPE, Operations.INPUTFLOAT)
    pass

def n_input(temp_var_type, op_code):
    temp_var = gen_temp_var()
    # Add to debug quad
    temp_quad = Quad(op_code, target=temp_var)
    quad_list.append(temp_quad)
    # Add to addr quad
    temp_var_addr = get_addr(temp_var, temp_var_type)
    addr_quad = Quad(op_code,  target=temp_var_addr)
    quad_addr_list.append(addr_quad)
    # Append variable temp a los scopes
    scope_tree.dict[current_scope_ref].add_variable(temp_var, temp_var_type, temp_var_addr)
    # Agregar a las pilas de operadores
    PilaO.append(temp_var)
    PTypes.append(temp_var_type)
    pass


def p_n_arr_reference(p):
    'n_arr_reference : '
    # verify that named variable already exists
    arr_name = last_arr_name_stack.pop()
    aux_scope_ref = current_scope_ref
    d1 = -1
    arr_start_addr = -1
    array_type = None
    while(aux_scope_ref > -1):
        scope_vars = scope_tree.dict[aux_scope_ref].vars
        if arr_name in scope_vars:
            # get d1
            d1 = scope_vars[arr_name]['d1']
            # get initial addr
            arr_start_addr = scope_vars[arr_name]['addr']
            # get array type
            array_type = scope_tree.dict[aux_scope_ref].vars[arr_name]['type']
            break
        if aux_scope_ref == 0:
            e_error(f"Dimensioned variable ({arr_name}) referenced before instantiated", p)
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref

    # VER Quad
    s1 = PilaO.pop()
    s1_type = PTypes.pop()
    if s1_type != Types.INT_TYPE:
        e_error(f"Cannot access dimensioned variable({arr_name}) address with non int value", p)

    insert_constant(d1, Types.INT_TYPE)
    d1_addr = constants_table[d1]['addr']
    # Add to debug quad
    quad_list.append(Quad(Operations.VER, 0, d1, s1))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.VER, 0, d1_addr, get_addr(s1, array_type)))

    # Get address with QUAD
    virtual_var_name = gen_temp_var(True)
    virtual_var_addr = get_addr(virtual_var_name, array_type)
    virtual_var_list.append(virtual_var_addr)
    scope_tree.dict[current_scope_ref].add_variable(virtual_var_name, array_type, virtual_var_addr, True)

    # arr_start_addr_name = gen_temp_var()
    # arr_start_addr_addr = get_addr(arr_start_addr_name, Types.INT_TYPE)
    insert_constant(arr_start_addr, Types.INT_TYPE)
    arr_start_addr_addr = constants_table[arr_start_addr]['addr']
    # Add to debug quad
    quad_list.append(Quad(Operations.PLUS, arr_start_addr, s1, virtual_var_name))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.PLUS, arr_start_addr_addr, get_addr(s1, Types.INT_TYPE), virtual_var_addr))

    PilaO.append(virtual_var_name)
    PTypes.append(array_type)
    pass

def p_n_matrix_reference(p):
    'n_matrix_reference : '
    # verify that named variable already exists
    arr_name = last_arr_name_stack.pop()
    aux_scope_ref = current_scope_ref
    d1 = -1
    d2 = -1
    arr_start_addr = -1
    array_type = None
    while(aux_scope_ref > -1):
        scope_vars = scope_tree.dict[aux_scope_ref].vars
        if arr_name in scope_vars:
            # get ds
            d1 = scope_vars[arr_name]['d1']
            d2 = scope_vars[arr_name]['d2']
            # get initial addr
            arr_start_addr = scope_vars[arr_name]['addr']
            # get matrix type
            array_type = scope_tree.dict[aux_scope_ref].vars[arr_name]['type']
            break
        if aux_scope_ref == 0:
            e_error(f"Dimensioned variable ({arr_name}) referenced before instantiated", p)
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    # TODO Potencialmente valga la pena generar los VER quads con mas puntos neuragicos a medio referenci, no al final?
    # VER Quad
    s2 = PilaO.pop()
    s2_type = PTypes.pop()
    s1 = PilaO.pop()
    s1_type = PTypes.pop()
    if s1_type != Types.INT_TYPE or s2_type != Types.INT_TYPE:
        e_error(f"Cannot access dimensioned variable({arr_name}) address with non int value", p)

    insert_constant(d1, Types.INT_TYPE)
    d1_addr = constants_table[d1]['addr']
    insert_constant(d2, Types.INT_TYPE)
    d2_addr = constants_table[d2]['addr']

    # Add to debug quad
    quad_list.append(Quad(Operations.VER, 0, d1, s1))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.VER, 0, d1_addr, get_addr(s1, array_type)))
    # Add to debug quad
    quad_list.append(Quad(Operations.VER, 0, d2, s2))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.VER, 0, d2_addr, get_addr(s2, array_type)))

    # Get address with QUAD
    s1_times_d2_name = gen_temp_var()
    s1_times_d2_addr = get_addr(s1_times_d2_name, Types.INT_TYPE)
    scope_tree.dict[current_scope_ref].add_variable(s1_times_d2_name, Types.INT_TYPE, s1_times_d2_addr)
    # Add to debug quad
    quad_list.append(Quad(Operations.TIMES, s1, d2, s1_times_d2_name))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.TIMES, get_addr(s1, Types.INT_TYPE), d2_addr, s1_times_d2_addr))

    plus_s2_name = gen_temp_var()
    plus_s2_addr = get_addr(plus_s2_name, Types.INT_TYPE)
    scope_tree.dict[current_scope_ref].add_variable(plus_s2_name, Types.INT_TYPE, plus_s2_addr)
    # Add to debug quad
    quad_list.append(Quad(Operations.PLUS, s1_times_d2_name, s2, plus_s2_name))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.PLUS, s1_times_d2_addr, get_addr(s2, Types.INT_TYPE), plus_s2_addr))


    virtual_var_name = gen_temp_var(True)
    virtual_var_addr = get_addr(virtual_var_name, array_type)
    virtual_var_list.append(virtual_var_addr)
    scope_tree.dict[current_scope_ref].add_variable(virtual_var_name, array_type, virtual_var_addr)

    insert_constant(arr_start_addr, Types.INT_TYPE)
    arr_start_addr_addr = constants_table[arr_start_addr]['addr']
    # Add to debug quad
    quad_list.append(Quad(Operations.PLUS, arr_start_addr, plus_s2_name, virtual_var_name))
    # Add to addr quad
    quad_addr_list.append(Quad(Operations.PLUS, arr_start_addr_addr, plus_s2_addr, virtual_var_addr))

    PilaO.append(virtual_var_name)
    PTypes.append(array_type)
    scope_tree.dict[current_scope_ref].add_variable(virtual_var_name, array_type, virtual_var_addr, True)
    pass


def p_n_arr_instantiate_name(p):
    'n_arr_instantiate_name : '
    # get array initial position from type stack/mem
    arr_name = get_last_t(p)
    arr_type = current_type
    arr_addr = get_addr(arr_name, arr_type)
    # add to scope tree
    scope_tree.dict[current_scope_ref].add_variable(arr_name, arr_type, arr_addr)
    # add to last stack referenced
    global last_arr_name_stack
    last_arr_name_stack.append(arr_name)
    pass

def p_n_arr_reference_name(p):
    'n_arr_reference_name : '
    arr_name = get_last_t(p)
    last_arr_name_stack.append(arr_name)
    pass

def p_n_arr_instantiate_size(p):
    'n_arr_instantiate_size : '
    # add size to size stack
    arr_size = get_last_t(p)
    arr_size_stack.append(arr_size)
    pass

def reserve_array_mem(arr_size, arr_type):
    if(arr_type == Types.INT_TYPE):
        global dir_last_empty_int
        check_out_of_mem(dir_last_empty_int + arr_size - 1, DIR_INT)
        dir_last_empty_int += arr_size - 1
    elif(arr_type == Types.STRING_TYPE):
        global dir_last_empty_string
        check_out_of_mem(dir_last_empty_string + arr_size - 1, DIR_STRING)
        dir_last_empty_string += arr_size - 1
    elif(arr_type == Types.FLOAT_TYPE):
        global dir_last_empty_float
        check_out_of_mem(dir_last_empty_float + arr_size - 1, DIR_FLOAT)
        dir_last_empty_float += arr_size - 1
    elif(arr_type == Types.BOOL_TYPE):
        global dir_last_empty_bool
        check_out_of_mem(dir_last_empty_bool + arr_size - 1, DIR_BOOL)
        dir_last_empty_bool += arr_size - 1
    else:
        raise Exception(f"OwO: Attempting to generate array size for unkown type ({arr_type})")

def p_n_arr_instantiate(p):
    'n_arr_instantiate : '
    # pop the size of the array, 'apartar' la memoria
    arr_size = int(arr_size_stack.pop())
    arr_type = current_type
    reserve_array_mem(arr_size, arr_type)
    # Set size in scope tree
    last_arr_name = last_arr_name_stack.pop()
    scope_tree.dict[current_scope_ref].vars[last_arr_name]['d1'] = arr_size
    pass

def p_n_matrix_instantiate(p):
    'n_matrix_instantiate : '
    # reserve memory for matrix
    arr_size_d2 = int(arr_size_stack.pop())
    arr_size_d1 = int(arr_size_stack.pop())
    arr_size = arr_size_d1 * arr_size_d2
    arr_type = current_type
    reserve_array_mem(arr_size, arr_type)
    # Set size in scope tree
    last_arr_name = last_arr_name_stack.pop()
    scope_tree.dict[current_scope_ref].vars[last_arr_name]['d1'] = arr_size_d1
    scope_tree.dict[current_scope_ref].vars[last_arr_name]['d2'] = arr_size_d2
    pass

def p_n_left_bracket(p):
    'n_left_bracket : '
    POper.append("[")
    pass

def p_n_right_bracket(p):
    'n_right_bracket : '
    POper.pop()
    pass

def p_n_end(p):
    'n_end : '
    # Debug Quad list
    quad_list.append(Quad(Operations.END))
    # Addr Quad list
    quad_addr_list.append(Quad(Operations.END))
    pass

# Generate a name for temporary variables, used for debugging
def gen_temp_var(addr=False):
    global temps_counter
    result = "$" + ("V" if addr else "") + f"t{temps_counter}"
    temps_counter += 1
    return result

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
    program : program_aux codeblock n_end
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
    | TRUE n_math_expression_1_bool
    | FALSE n_math_expression_1_bool
    '''
    pass

def p_function_type(p):
    '''
    function_type : VOID n_function_type
    | INT_TYPE n_function_type
    | STRING_TYPE n_function_type
    | DOUBLE_TYPE n_function_type
    | FLOAT_TYPE n_function_type
    | BOOL_TYPE n_function_type
    '''
    pass

def p_function_definition(p):
    '''
    function_definition : n_before_function_definition FUNCTION NAME n_open_new_scope_function parameter_list DOUBLEDOT function_type LCURLY n_function_block_start codeblock RCURLY n_close_scope n_function_block_end
    '''
    pass

def p_return(p):
    '''
    return : RETURN expression n_return SEMICOLON
    | RETURN n_return_void SEMICOLON
    '''
    pass

def p_function_call(p):
    '''
    function_call : NAME n_function_call_1 \
                  LPARENTHESIS n_function_call_2 arg_list RPARENTHESIS \
                  n_function_call_5 n_function_call_6
                  | NAME n_function_call_1 \
                  LPARENTHESIS RPARENTHESIS \
                  n_function_call_6
    '''
    pass

def p_arg_list(p):
    '''
    arg_list : arg
    | arg COMMA n_function_call_4 arg_list
    '''
    pass

def p_parameter_list(p):
    '''
    parameter_list : empty
    | parameter
    | parameter COMMA parameter_list
    '''
    pass

def p_arg(p):
    '''
    arg : expression n_function_call_3
    '''
    pass

def p_parameter(p):
    '''
    parameter : type NAME n_variable_instantiate_param
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

def p_input(p):
    '''
    input : INPUTSTRING LPARENTHESIS RPARENTHESIS n_input_string
    | INPUTINT LPARENTHESIS RPARENTHESIS n_input_int
    | INPUTFLOAT LPARENTHESIS RPARENTHESIS n_input_float
    '''
    pass

def p_value(p):
    '''
    value : function_call
    | literal
    | reference
    | input
    '''
    pass

# When you reference a value from a variable or an array's postion/index
def p_reference(p):
    '''
        reference : NAME n_variable_reference n_math_expression_1_name
        | arr_reference
    '''
    pass

# Reference for an arrays's position/index
def p_arr_reference(p):
    '''
        arr_reference : NAME n_arr_reference_name LBRACKET n_left_bracket expression RBRACKET n_right_bracket n_arr_reference
        | NAME n_arr_reference_name LBRACKET n_left_bracket expression RBRACKET n_right_bracket LBRACKET n_left_bracket expression RBRACKET n_right_bracket n_matrix_reference
    '''
    pass

# When you declare a variable without an assign(=)after it
def p_declare(p):
    '''
    declare : type NAME n_variable_instantiate
    | type NAME n_arr_instantiate_name LBRACKET INT n_arr_instantiate_size RBRACKET n_arr_instantiate
    | type NAME n_arr_instantiate_name LBRACKET INT n_arr_instantiate_size RBRACKET LBRACKET INT n_arr_instantiate_size RBRACKET n_matrix_instantiate
    '''
    pass

# When you assign a value to a variable, this could be its instantiation
def p_assign(p):
    '''
    assign : type NAME n_variable_instantiate n_math_expression_1_name EQUAL n_seen_equal_op expression
    | reference EQUAL n_seen_equal_op expression
    '''
    e = do_assign_var()
    if e:
        e_error(e, p)
    pass

def p_print(p):
    '''
    print : PRINT LPARENTHESIS expression n_print RPARENTHESIS
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
    | declare
    | function_call
    | print
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
    | return
    '''
    pass

def p_loop(p):
    '''
    loop : whileloop
    '''
    pass

def p_whileloop(p):
    '''
    whileloop : WHILE p_n_pre_condition_loop_1 LPARENTHESIS expression RPARENTHESIS p_n_pre_condition_loop_2 LCURLY n_open_new_scope codeblock RCURLY p_n_pre_condition_loop_3 n_close_scope
    '''
    pass

# DEPRECATED
# def p_forloop(p):
#     '''
#     forloop : FOR LPARENTHESIS n_open_new_scope assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY n_close_scope
#     '''
#     pass

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

def print_addr_used():
    print(f"DIR_INT: {DIR_INT}")
    print(f"dir_last_empty_int: {dir_last_empty_int}")

    print(f"DIR_STRING: {DIR_STRING}")
    print(f"dir_last_empty_string: {dir_last_empty_string}")

    print(f"DIR_FLOAT: {DIR_FLOAT}")
    print(f"dir_last_empty_float: {dir_last_empty_float}")

    print(f"DIR_BOOL: {DIR_BOOL}")
    print(f"dir_last_empty_bool: {dir_last_empty_bool}")

def print_variable_scopes():
    print("--Variable scopes")
    [print(scope_tree.dict[ref]) for ref in range(0, scope_tree.counter)]

def print_pilas():
    print(f"--PilaO: {PilaO}\n--PTypes: {PTypes}\n--POper: {POper}")

def print_quads():
    print("--Quads")
    [print(f"{ref} {quad_list[ref]}") for ref in range(0, len(quad_list))]

def print_addr_quads():
    print("--Addr Quads")
    [print(f"{ref} {quad_addr_list[ref]}") for ref in range(0, len(quad_addr_list))]

def get_adrr_quads_str():
    return [(f"{ref} {quad_addr_list[ref]}") for ref in range(0, len(quad_addr_list))]

def output_quads_to_file(file_name='output_quads.txt'):
    with open(file_name, 'w+') as f:
        quads_str_list = get_adrr_quads_str()
        for quad in quads_str_list:
            f.write(f'{quad}\n')
    

# Error handling for semantic exceptions
def e_error(e, p):
    print_scope_tree()
    raise Exception(f"OwO: {e} in line: {p.lineno(-1)}")

# Error handling lexer
def t_error(t):
    print(f"Illegal character {t}")
    t.lexer.skip(1)

# Error handling parser
def p_error(p):
    if not p:
        raise Exception(f"End of File! Probably missing a semicolon ;")
    raise Exception(f"Error {p}")


### MOBILE/GRAPHICAL APPLICATION 
class Fnt_SpinnerOption(SpinnerOption):
    pass


class LoadDialog(Popup):

    def load(self, path, selection):
        self.choosen_file = [None, ]
        self.choosen_file = selection
        Window.title = selection[0][selection[0].rfind(os.sep) + 1:]
        self.dismiss()

    def cancel(self):
        self.dismiss()


class SaveDialog(Popup):

    def save(self, path, selection):
        _file = codecs.open(selection, 'w', encoding='utf8')
        _file.write(self.text)
        Window.title = selection[selection.rfind(os.sep) + 1:]
        _file.close()
        self.dismiss()

    def cancel(self):
        self.dismiss()


class CodeInputWithBindings(EmacsBehavior, CodeInput):
    '''CodeInput with keybindings.
    To add more bindings, add the behavior before CodeInput in the class
    definition.
    '''
    pass


class CodeInputTest(App):

    files = ListProperty([None, ])

    def build(self):
        b = BoxLayout(orientation='vertical')
        languages = Spinner(
            text='language',
            values=sorted(['KvLexer', ] + list(lexers.LEXERS.keys())))

        languages.bind(text=self.change_lang)

        menu = BoxLayout(
            size_hint_y=None,
            height='30pt')
        fnt_size = Spinner(
            text='FontSize: 12',
            values=list(map(str, list(range(10, 120, 5)))))
        fnt_size.bind(text=self._update_size)

        fonts = [
            file for file in LabelBase._font_dirs_files
            if file.endswith('.ttf')]

        fnt_name = Spinner(
            text='RobotoMono',
            option_cls=Fnt_SpinnerOption,
            values=fonts)
        fnt_name.bind(text=self._update_font)
        mnu_file = Spinner(
            text='File',
            values=('Open', 'SaveAs', 'Save', 'Close'))
        mnu_file.bind(text=self._file_menu_selected)
        key_bindings = Spinner(
            text='Key bindings',
            values=('Default key bindings', 'Emacs key bindings'))
        key_bindings.bind(text=self._bindings_selected)

        run_button = Button(text='Run')
        run_button.bind(on_press=self.compile)

        menu.add_widget(mnu_file)
        menu.add_widget(fnt_size)
        menu.add_widget(run_button)
        # menu.add_widget(fnt_name)
        # menu.add_widget(languages)
        # menu.add_widget(key_bindings)
        b.add_widget(menu)

        self.codeinput = CodeInputWithBindings(
            lexer=KivyLexer(),
            font_size=12,
            text=current_code,
            key_bindings='default',
            # onChange save to code
        )
        
        self.output_box = CodeInputWithBindings(
            font_size=12,
            text="SECTION: OUTPUT\n",
            key_bindings='default',
        )

        self.command_input = TextInput(text='Hello world', multiline=False, cursor_blink=True, cursor_width=8)
        self.command_input.bind(on_text_validate=self.on_enter)

        b.add_widget(self.codeinput)
        b.add_widget(self.output_box)
        b.add_widget(self.command_input)

        return b

    def ask_user_input(self):
        print("No he pasadoasdaosjkd poasjdlasdj")
        print("YA PASE")
        # return 'Azul'

    def compile(self, instance):
        print("Running compiler...")
        print(f'{10*"#"} current_code {10*"#"} {self.get_code()}\n{10*"#"} end_current_code {10*"#"}')
        try:
            run_compiler(self.get_code())
        except KeyboardInterrupt:
            return
        except BaseException as err:
            print(f"Error caught: {err}")
            stdoutin[2] += f"{str(err)}\n"
            self.display_and_flush_everything()            
        # TODO: Remove this from output mobile build, dont use it
        output_quads_to_file()
        self.vm = VirtualMachine(quad_addr_list, constants_table, scope_tree, virtual_var_list, stdoutin=stdoutin)
        # Starts execution for the first time
        self.resume_vm_execution()
            
    def resume_vm_execution(self):
        print("Resuming execution after...")
        try:
            # Simulate do while
            while (True):
                yield_op_code = self.vm.execute_quads()
                if yield_op_code in [Operations.INPUTSTRING, Operations.INPUTINT, Operations.INPUTFLOAT]:
                    if stdoutin[0] == '':
                        print('Waiting for user input on the graphical side.')
                        return # this gets resumed if thers an input with the callback of the user_input
                elif yield_op_code in [Operations.PRINT]:
                    # We only go out of vm to print ouput and then go back inside
                    self.display_and_flush_everything()
                else:
                    # Breaks out of do while if it doesnt return an input op_code
                    # If it gets here it means that vm ended execution
                    print("Breaking out of the loop yaaaaaay")
                    break
            pass
        except KeyboardInterrupt:
            return
        except BaseException as err:
            print(f"Error caught: {err}")
            stdoutin[2] += f"{str(err)}\n"

        print(f"stdoutin: {stdoutin}")
        self.display_and_flush_everything()


    def on_enter(self, instance):
      self.stdin = instance.text
      self.display_output(f'{self.stdin}\n')
      stdoutin[0] = self.stdin 
      self.resume_vm_execution()

    def get_stdout(self):
        return stdoutin[1]
    
    def get_stderr(self):
        return stdoutin[2]

    def get_code(self):
      return self.codeinput.text

    # everything means stdout and stderr
    def display_and_flush_everything(self):
        self.display_output(self.get_stdout()) # stdout
        self.display_output(self.get_stderr()) # stderr 
        stdoutin[1] = stdoutin[2] = '' 

    def display_output(self, message):
      output = f'{message}'
      print(f'STDOUT: {output}') 
      self.output_box.text += output

    def _update_size(self, instance, size):
        self.codeinput.font_size = float(size)
        self.output_box.font_size = float(size)
        self.command_input.font_size = float(size)

    def _update_font(self, instance, fnt_name):
        instance.font_name = self.codeinput.font_name = self.output_box.font_name = fnt_name

    def _file_menu_selected(self, instance, value):
        if value == 'File':
            return
        instance.text = 'File'
        if value == 'Open':
            if not hasattr(self, 'load_dialog'):
                self.load_dialog = LoadDialog()
            self.load_dialog.open()
            self.load_dialog.bind(choosen_file=self.setter('files'))
        elif value == 'SaveAs':
            if not hasattr(self, 'saveas_dialog'):
                self.saveas_dialog = SaveDialog()
            self.saveas_dialog.text = self.codeinput.text
            self.saveas_dialog.open()
        elif value == 'Save':
            if self.files[0]:
                _file = codecs.open(self.files[0], 'w', encoding='utf8')
                _file.write(self.codeinput.text)
                _file.close()
        elif value == 'Close':
            if self.files[0]:
                self.codeinput.text = ''
                Window.title = 'untitled'

    def _bindings_selected(self, instance, value):
        value = value.split(' ')[0]
        self.codeinput.key_bindings = value.lower()

    def on_files(self, instance, values):
        if not values[0]:
            return
        _file = codecs.open(values[0], 'r', encoding='utf8')
        self.codeinput.text = _file.read()
        _file.close()

    def change_lang(self, instance, z):
        if z == 'KvLexer':
            lx = KivyLexer()
        else:
            lx = lexers.get_lexer_by_name(lexers.LEXERS[z][2][0])
        self.codeinput.lexer = lx


### MAIN
if __name__ == '__main__':
    CodeInputTest().run()
