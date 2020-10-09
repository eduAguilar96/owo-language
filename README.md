# OWO

## Example code
```
(OwO)

string mi_nombre = "Jaimito";
int a = 1, b = 0;
float fu = -0.1, ack = 0.314;

for (int i = -1: i < 10: i = i + 1) {
  a = a + 1;
  b = b - 1;
}
```

## Grammar

[Grammar link](https://docs.google.com/document/d/1Sl-Xqvqma83L_Q2IM0E7kuVlZnZoebezW3tmraRpfOE/edit#)

[Diagram link](https://drive.google.com/file/d/1kDECc6qLETylzCYxO4f23YomMLlRZtPX/view?usp=sharing)

```
E -> empty

TYPE -> “int” | “string” | “double” | “float” | “bool”

LOGIC_OPERATOR -> ">" | "<" | "==" | ">=" | "<=" | "!="

ARITHMETHIC_OPERATOR -> ‘+’ | ‘-’ | ‘*’ | ‘/’ | ‘%’

LITERAL -> float | double | string | int

FUNCTION_TYPE -> TYPE | "void"

FUNCTION_DEFINITION -> “function” NAME PARAMETER_LIST “:” FUNCTION_TYPE “{“ CODE_BLOCK ‘}”

FUNCTION_CALL -> NAME "(" PARAMETER_LIST ")"

PARAMETER_LIST -> E  | PARAMETER | PARAMETER “,” PARAMETER_LIST

PARAMETER -> TYPE NAME | ASSIGN

EXPRESSION -> WRAP_EXP | WRAP_EXP LOGIC_OPERATOR WRAP_EXP

WRAP_EXP -> EXP | "(" EXP ")"

EXP -> VALUE | EXP'' ARITHMETIC_OPERATOR WRAP_EXP
VALUE -> FUNCTION_CALL | LITERAL | NAME

PROGRAM  -> PROGRAM’’ CODEBLOCK
PROGRAM’’ -> “CHIEF/AARON :)” | “(OwO)”

ASSIGN     -> TYPE ASSIGN’’ AS_AGAIN | ASSIGN’’ AS_AGAIN
ASSIGN’’    -> NAME “=” EXPRESSION
AS_AGAIN -> “,” ASSIGN | E

STATEMENT -> STATEMENT'' ";"
STATEMENT'' -> ASSIGN | FUNCTION_CALL | PRINT

CODEBLOCK -> E | CODEBLOCK'' CODEBLOCK
CODEBLOCK'' -> STATEMENT | FUNCTION_DEFINITION | CONDITION_IF | LOOP

LOOP -> FORLOOP | WHILELOOP

WHILELOOP -> “while” “(“ EXPRESSION “)” “{“ CODE_BLOCK “}”

FORLOOP -> "for" ASSIGN ":" EXPRESSION ":" ASSIGN ")" "{" CODE_BLOCK "}"

CONDITION_IF -> “if” “(“ EXPRESSION “)” “{“ CODE_BLOCK “}” CONDITION_ELSE

CONDITION_ELSE -> else | CONDITION_ELSE''
CONDITION_ELSE''  -> E | "{" CODE_BLOCK "}" | "else" CONDITION_IF
```

# Log

## 08/10/2020 - Entrega 1

Definimos la Gramatica y la implementamos en Python con la libreria de ply.

Found issues: nos falta definir comentarios, Print y 'true'/'false'.
