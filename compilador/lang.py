import sys
import lex
import yacc
from examples import *
from vm import *
from utility.semantic_scope_tree import *
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
    'return': 'RETURN',
    'OwO': 'OWO',
    'CHIEF/AARON': 'IDK',
    'print': 'PRINT',
    # Flow
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    #logical
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
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

start = 'program'

def check_out_of_mem(last_addr, initial_addr):
    if(last_addr >= DIR_SIZE + initial_addr):
        raise Exception("OwO: Out of memory")

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
    return token[0] == '"' or token[0].isdigit() or token == "True" or token == "False"

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
    if(value_type == Types.INT_TYPE):
        global dir_last_empty_int
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
    elif(value_type == Types.VOID):
        addr = -1
    else:
        raise Exception("OwO: Attempting to generate address for unkown variable type")

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

def insert_constant(constant, constant_type):
    if constant in constants_table:
        return
    constants_table[constant] = {
            'addr': get_addr(constant, constant_type),
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

# Verify that function exists and do the ERA quad
last_function_call = []
def p_n_function_call_1(p):
    'n_function_call_1 : '
    func_name = get_last_t(p)
    global last_function_call
    last_function_call.append(func_name)
    aux_scope_ref = current_scope_ref
    while(aux_scope_ref > -1):
        # check if function is child context
        if func_name in scope_tree.dict[aux_scope_ref].functions:
            func_ref = scope_tree.dict[current_scope_ref].functions[func_name]
            # Se pasa una referencia a Que es scope es func_name con func_ref, esto en relacion al scope_tree
            # Debug quad list
            quad_list.append(Quad(Operations.ERA, left=func_name, right=func_ref))
            # Addr quad list
            quad_addr_list.append(Quad(Operations.ERA, left=func_name, right=func_ref))
            return
        aux_scope_ref = scope_tree.dict[aux_scope_ref].parent_ref
    e_error(f"Function {func_name} called before instantiated", p)
    pass

argument_counter = []
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
    function_ref = scope_tree.dict[current_scope_ref].functions[function_name]
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
    function_name = last_function_call[-1]
    function_ref = scope_tree.dict[current_scope_ref].functions[function_name]
    params_list = scope_tree.dict[function_ref].params
    if (argument_counter[-1] != len(params_list)-1):
        e_error(f"Argument mismatch for function ({function_name}) call, args({argument_counter[-1]+1}), params({len(params_list)})", p)
    argument_counter.pop()
    pass

def p_n_function_call_6(p):
    'n_function_call_6 : '
    function_name = last_function_call[-1]
    function_ref = scope_tree.dict[current_scope_ref].functions[function_name]
    params_list = scope_tree.dict[function_ref].params
    # Se pasa una referencia a Que es scope es func_name con func_ref, esto en relacion al scope_tree
    # Debug Quad list
    quad_list.append(Quad(Operations.GOSUB, left=f"${function_name}_return_value", right=function_ref))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.GOSUB, left=f"${function_name}_return_value", right=function_ref))

    # Handle return_value
    temp_var = gen_temp_var()
    temp_var_type = scope_tree.dict[function_ref].return_type
    temp_var_addr = get_addr(temp_var, temp_var_type)
    PilaO.append(temp_var)
    PTypes.append(temp_var_type)

    scope_tree.dict[current_scope_ref].add_variable(temp_var, temp_var_type, temp_var_addr)
    # Debug quad list
    quad_list.append(Quad(Operations.EQUAL, left=f"${function_name}_return_value", target=temp_var))
    # Addr quad list
    quad_addr_list.append(Quad(Operations.EQUAL, left=f"${function_name}_return_value", target=temp_var_addr))


    last_function_call.pop()
    pass

def p_n_return(p):
    'n_return : '
    func_ref = current_scope_ref
    func_name = scope_tree.dict[func_ref].func_name
    func_return_type = scope_tree.dict[func_ref].return_type
    if(func_return_type == Types.VOID):
        e_error(f"Void function ({func_name}) cannot have a return value", p)
    return_value = PilaO.pop()
    return_type = PTypes.pop()
    if return_type != func_return_type:
        e_error(f"Wrong return type for ({func_name}), return type is ({return_type.value}), must be ({func_return_type.value})", p)
    # Debug Quad List
    quad_list.append(Quad(Operations.RETURN, target=return_value))
    # Addr Quad List
    quad_addr_list.append(Quad(Operations.RETURN, target=get_addr(return_value, return_type)))
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

def p_n_end(p):
    'n_end : '
    # Debug Quad list
    quad_list.append(Quad(Operations.END))
    # Addr Quad list
    quad_addr_list.append(Quad(Operations.END))
    pass

def gen_temp_var():
    global temps_counter
    result = f"$t{temps_counter}"
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
    function_definition : n_before_function_definition FUNCTION NAME n_open_new_scope_function parameter_list DOUBLEDOT function_type LCURLY n_function_block_start codeblock return RCURLY n_close_scope n_function_block_end
    '''
    pass

def p_return(p):
    '''
    return : RETURN expression n_return SEMICOLON
    | RETURN n_return_void SEMICOLON
    | empty
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

# TODO falta agregar n_math_expression_1 para function_call
def p_value(p):
    '''
    value : function_call
    | literal
    | NAME n_variable_reference n_math_expression_1_name
    '''
    pass

# TODO agregar soporte para instantiate varibale sin un assign

def p_declare(p):
    '''
    declare : type NAME n_variable_instantiate
    '''

def p_assign(p):
    '''
    assign : type NAME n_variable_instantiate n_math_expression_1_name EQUAL n_seen_equal_op expression
    | NAME n_variable_reference n_math_expression_1_name EQUAL n_seen_equal_op expression
    '''
    e = do_assign()
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

def print_addr_quads():
    print("--Addr Quads")
    [print(f"{ref} {quad_addr_list[ref]}") for ref in range(0, len(quad_addr_list))]

# Error handling for semantic exceptions
def e_error(e, p):
    raise Exception(f"OwO: {e} in line: {p.lineno(-1)}")

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

examples_output = [print(f"{i}. {str(data_examples[i])}") for i in range(0, len(data_examples))]
user_input = int(input())
if user_input in range(0, len(examples_output)):
    data = data_examples[user_input].data
else:
    raise Exception("Invalid Code/Index for example")

# Read input in lexer
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    # print(tok)

result = parser.parse(data)

# print_variable_scopes()
# print_pilas()
# print(constants_table)
# print_scope_tree()
# print_addr_quads()
# print_quads()

vm = VirtualMachine(quad_addr_list, constants_table)
vm.execute_quads()
# vm.print_mem()
# vm.print_mem_tree()
