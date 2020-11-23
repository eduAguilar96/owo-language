from scanner import *

# Runs compiler, receives code as arg
def run_compiler(code):
    # Read input in lexer
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break
    # print(tok)

    result = parser.parse(data)

examples_output = [print(f"{i}. {str(data_examples[i])}") for i in range(0, len(data_examples))]
user_input = int(input())
if user_input in range(0, len(examples_output)):
    data = data_examples[user_input].data
else:
    raise Exception("Invalid Code/Index for example")

# Build the lexer
lexer = lex.lex()
# Build the parser
parser = yacc.yacc()

run_compiler(data)

vm = VirtualMachine(quad_addr_list, constants_table, scope_tree)
vm.execute_quads(True)
