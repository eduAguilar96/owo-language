import sys
from ply import lex
from ply import yacc

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
current_func = '#global'
names = {
    '#global': {
        'vars': {}
    }
}

start = 'program'

# Track line numbers
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

def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    # print(current_type)
    current_type = p[-1]

def p_type(p):
    '''
    type : INT_TYPE n_seen_type
    | STRING_TYPE n_seen_type
    | DOUBLE_TYPE n_seen_type
    | FLOAT_TYPE n_seen_type
    | BOOL_TYPE n_seen_type
    '''
    pass

def p_logic_operator(p):
    '''
    logic_operator : GREATERTHAN
    | LESSTHAN
    | EQUALEQUAL
    | LESSTHANOREQUAL
    | GREATERTHANOREQUAL
    | NOTEQUAL
    '''
    pass

# def p_relational_operator(p):
#     '''
#     logic_operator : GREATERTHAN
#     | LESSTHAN
#     | EQUALEQUAL
#     | LESSTHANOREQUAL
#     | GREATERTHANOREQUAL
#     | NOTEQUAL
#     '''
#     pass

def p_arithmetic_operator(p):
    '''
    arithmetic_operator : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MODULUS
    '''
    pass

def p_literal(p):
    '''
    literal : FLOAT
    | INT
    | STRING
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
    function_definition : FUNCTION NAME parameter_list DOUBLEDOT function_type LCURLY codeblock RCURLY
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
    parameter : type NAME
    | assign
    '''
    pass

def p_expression(p):
    '''
    expression : exp
    | exp logic_operator exp
    '''
    pass

def p_exp(p):
    '''
    exp : termino
    | termino PLUS exp
    | termino MINUS exp
    '''
    pass

def p_termino(p):
    '''
    termino : factor
    | factor TIMES termino
    | factor DIVIDE termino
    '''
    pass

def p_factor(p):
    '''
    factor : LPARENTHESIS expression RPARENTHESIS
    | PLUS value
    | MINUS value
    | value
    '''
    pass

def p_value(p):
    '''
    value : function_call
    | literal
    | NAME
    '''
    pass

def p_assign(p):
    '''
    assign : type NAME n_name_assign EQUAL expression
    | NAME n_name_assign EQUAL expression
    '''
    pass

def p_n_name_assign(p):
    'n_name_assign : '
    global current_func
    names[current_func]['vars'][p[-1]] = {
        'type': current_type
    }
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
    whileloop : WHILE LPARENTHESIS expression RPARENTHESIS LCURLY codeblock RCURLY
    '''
    pass

def p_forloop(p):
    '''
    forloop : FOR LPARENTHESIS assign DOUBLEDOT expression DOUBLEDOT assign RPARENTHESIS LCURLY codeblock RCURLY
    '''
    pass

def p_condition_if(p):
    '''
    condition_if : IF LPARENTHESIS expression RPARENTHESIS LCURLY codeblock RCURLY condition_else
    '''
    pass

def p_condition_else(p):
    '''
    condition_else : ELSE LCURLY codeblock RCURLY
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
print(names)

# Notas para el futuro
# nos falto definir 'true' y 'false' como constantes para variables de tipo bool
# nos falto definir syntaxis para comentarios
