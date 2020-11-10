from ply import lex
from ply import yacc

print("Hello World")

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
    '(OwO)': 'OWO',
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
    t.type = reserved.get(t.value, 'ID')
    return t

t_FLOAT = r'(0.0|-?[0-9]*\.[0-9])'
t_INT = r'(0|-?[1-9][0-9]*)'
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


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# A string containing ignored characters
t_ignore = ' \t'

# Error handling lexer
def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

# Precedence rules for the arithmetic operators
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    )

# dictionary of names (for storing variables)
current_type = None
current_func = '#global'
names = {
    '#global': {
        'vars': {}
    }
}

start = 'PROGRAM'

def p_empty(p):
    '''
    empty :
    '''
    pass

def p_PROGRAM(p):
    '''
    PROGRAM : PROGRAM_AUX CODEBLOCK
    '''
    pass

def p_PROGRAM_AUX(p):
    '''
    PROGRAM_AUX : IDK
    | OWO
    '''
    pass

def p_n_seen_type(p):
    'n_seen_type : '
    global current_type
    current_type = p[-1]

def p_TYPE(p):
    '''
    TYPE : INT_TYPE n_seen_type
    | STRING_TYPE n_seen_type
    | DOUBLE_TYPE n_seen_type
    | FLOAT_TYPE n_seen_type
    | BOOL_TYPE n_seen_type
    '''
    pass

def p_LOGIC_OPERATOR(p):
    '''
    LOGIC_OPERATOR : GREATERTHAN
    | LESSTHAN
    | EQUALEQUAL
    | LESSTHANOREQUAL
    | GREATERTHANOREQUAL
    | NOTEQUAL
    '''
    pass

def p_ARITHMETIC_OPERATOR(p):
    '''
    ARITHMETIC_OPERATOR : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | MODULUS
    '''
    pass

def p_LITERAL(p):
    '''
    LITERAL : FLOAT
    | NAME
    | INT
    | STRING
    '''
    pass

def p_FUNCTION_TYPE(p):
    '''
    FUNCTION_TYPE : TYPE
    | VOID
    '''
    pass

def p_FUNCTION_DEFINITION(p):
    '''
    FUNCTION_DEFINITION : FUNCTION NAME PARAMETER_LIST DOUBLEDOT FUNCTION_TYPE LCURLY CODEBLOCK RCURLY
    '''
    pass

def p_FUNCTION_CALL(p):
    '''
    FUNCTION_CALL : NAME LPARENTHESIS PARAMETER_LIST RPARENTHESIS
    '''
    pass

def p_PARAMETER_LIST(p):
    '''
    PARAMETER_LIST : empty
    | PARAMETER
    | PARAMETER COMMA PARAMETER_LIST
    '''
    pass

def p_PARAMETER(p):
    '''
    PARAMETER : TYPE NAME
    | ASSIGN
    '''
    pass

def p_EXPRESSION(p):
    '''
    EXPRESSION : WRAP_EXP
    | WRAP_EXP LOGIC_OPERATOR WRAP_EXP
    '''
    pass

def p_WRAP_EXP(p):
    '''
    WRAP_EXP : EXP
    | LPARENTHESIS EXP RPARENTHESIS
    '''
    pass

def p_EXP(p):
    '''
    EXP : VALUE
    | VALUE ARITHMETIC_OPERATOR WRAP_EXP
    '''
    pass

def p_VALUE(p):
    '''
    VALUE : FUNCTION_CALL
    | LITERAL
    | NAME
    '''
    pass

def p_ASSIGN(p):
    '''
    ASSIGN : TYPE ASSIGN_AUX AS_AGAIN
    | ASSIGN_AUX AS_AGAIN
    '''
    pass

def p_n_name_assign_aux(p):
    'n_name_assign_aux : '
    names[current_func]['vars'][p[-1]] = {
        'type': current_type
    }

def p_ASSIGN_AUX(p):
    '''
    ASSIGN_AUX : NAME n_name_assign_aux EQUAL EXPRESSION
    '''
    pass

def p_AS_AGAIN(p):
    '''
    AS_AGAIN : COMMA ASSIGN
    | empty
    '''
    pass

def p_STATEMENT(p):
    '''
    STATEMENT : STATEMENT_AUX SEMICOLON
    '''
    pass

def p_STATEMENT_AUX(p):
    '''
    STATEMENT_AUX : ASSIGN
    | FUNCTION_CALL
    '''
    # | PRINT
    pass

def p_CODEBLOCK(p):
    '''
    CODEBLOCK : empty
    | CODEBLOCK_AUX CODEBLOCK
    '''
    pass

def p_CODEBLOCK_AUX(p):
    '''
    CODEBLOCK_AUX : STATEMENT
    | FUNCTION_DEFINITION
    | CONDITION_IF
    | LOOP
    '''
    pass

def p_LOOP(p):
    '''
    LOOP : FORLOOP
    | WHILELOOP
    '''
    pass

def p_WHILELOOP(p):
    '''
    WHILELOOP : WHILE LPARENTHESIS EXPRESSION RPARENTHESIS LCURLY CODEBLOCK RCURLY
    '''
    pass

def p_FORLOOP(p):
    '''
    FORLOOP : FOR ASSIGN DOUBLEDOT EXPRESSION DOUBLEDOT ASSIGN RPARENTHESIS LCURLY CODEBLOCK RCURLY
    '''
    pass

def p_CONDITION_IF(p):
    '''
    CONDITION_IF : IF LPARENTHESIS EXPRESSION RPARENTHESIS LCURLY CODEBLOCK RCURLY CONDITION_ELSE
    '''
    pass

def p_CONDITION_ELSE(p):
    '''
    CONDITION_ELSE : ELSE
    | CONDITION_ELSE_AUX
    '''
    pass

def p_CONDITION_ELSE_AUX(p):
    '''
    CONDITION_ELSE_AUX : empty
    | LCURLY CODEBLOCK RCURLY
    | ELSE CONDITION_IF
    '''
    pass

# Error handling parser
def p_error(p):
    print("Done")
    if not p:
        print("End of File!")
        return

    while True:
        tok = parser.token()  # Get next token
        if not tok or tok.type == 'closebrac':
            break
    parser.restart()

# Build the lexer
lexer = lex.lex()
# Build the parser
parser = yacc.yacc()
user_input = int(
    input("1.Programa valido\n2.Programa no valido\n3.Documento Mock\n"))

data = ""

if user_input == 1:
    data = '''
            (OwO)
            int nombre = 12345;
            '''

elif user_input == 2:
    data = '''estoEstaMal *()+`'''

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
    print(tok)

result = parser.parse(data)
print(result)
print(names)

# Notas para el futuro
# nos falto definir 'true' y 'false' como constantes para variables de tipo bool
# nos falto definir syntaxis para comentarios
