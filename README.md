# OwO - Lenguaje de Programación
by Eduardo Aguilar and Aaron Garcia

**OwO** es un lenguaje de programación procedimental, se compila utilizando python y se ejecuta por una máquina virtual de Python. **Corre en cualquier sistema operativo** incluyendo dispositivos móviles.

[Documentación y Consideraciones de OwO Language](https://docs.google.com/document/d/1wYxsjxeZLEEC3CDC_lQ8JxAXf0MV6j60eAPvt9NA0B4/edit?usp=sharing)

- [OwO - Lenguaje de Programación](#owo---lenguaje-de-programación)
  - [Estructura del Programa](#estructura-del-programa)
  - [Tipos de Datos](#tipos-de-datos)
  - [Literales](#literales)
  - [Scopes (Contextos)](#scopes-contextos)
    - [Variables Globales](#variables-globales)
    - [Funciones](#funciones)
  - [Declaraciones](#declaraciones)
    - [Llamadas a funciones](#llamadas-a-funciones)
  - [Estatutos de Control](#estatutos-de-control)
    - [Condición If-Else](#condición-if-else)
    - [Ciclo While](#ciclo-while)
  - [Variables Dimensionadas](#variables-dimensionadas)
    - [Variables de 1-dimension](#variables-de-1-dimension)
    - [Variables de 2-dimensiones](#variables-de-2-dimensiones)
  - [Expresiones](#expresiones)
    - [Operadores Aritméticos](#operadores-aritméticos)
  - [|Módulo|%|](#módulo)
  - [|Negativo|-|](#negativo-)
    - [Operadores Lógicos](#operadores-lógicos)
  - [|Or|or|](#oror)
    - [Operadores Relacionales](#operadores-relacionales)
  - [|Diferente a|!=|](#diferente-a)
    - [Operadores de Asignación](#operadores-de-asignación)
    - [Asociatividad](#asociatividad)
    - [Ordén de Precedencia](#ordén-de-precedencia)
      - [Modificar Precedencia de Operadores](#modificar-precedencia-de-operadores)
  - [Lógica Aritmética](#lógica-aritmética)
  - [Funciones Especiales](#funciones-especiales)
    - [print](#print)
    - [input](#input)
    - [concatenación de strings](#concatenación-de-strings)
  - [Comentarios](#comentarios)


## Estructura del Programa
**Lo ÚNICO que requiere** el programa de **OwO** es que el **archivo empieze con la palabra** `OwO`. 

No tiene que seguir una estructura en específico no requiere de una función de entrada main ni nada. Cada archivo requiere empezar con la palabra `OwO` y apartir de esa línea todo es el contexto global.

Puedes declarar y definir funciones en cualquier lugar, se ejecuta el contexto global línea por línea apartir del OwO.

Un programa básico se vería así:

```
OwO

function hola_mundo : void {
  print("Hola mundo! OwO");
}

hola_mundo();
```

## Tipos de Datos
El lenguaje **OwO** soporta los siguientes tipos primitivos:

1. **int**: numero entero positivo o negativo, sin punto decimal, de tamaño ilimitado.
   1. ej. 0, 1, 2, 3, -1, -2, -3
2. **float**: numero con punto decimal ya sea positivo o negativo, de tamaño ilimitado.
   1. ej. 1.0, 1.5, 2.0, 0.0, -0.5, -1.0
3. **string**: almacena palabras formadas por valores de la tabla ascii
   1. ej. "hola", "como", "estas?", "OwO"
4. **bool**: almacena verdadero o falso, en inglés (solo tiene 2 valores)>
   1. ej. True, False


## Literales
Esta tabla es la representación de los literales, divido por tipo primitivo.
|Name |Quantity|Ejemplo|
|-----|--------|-------|
|int  |Valor númerico sin puntos decimales     |0,1,2,3,...
|float|Valor númerio con puntos decimales      |0,1,0.5,1.0...
|string|Cualquier palabra o letra rodeada por comillas dobles| "palabra", "a", ...
|bool |verdadero o falso| True,False

## Scopes (Contextos)
### Variables Globales
Las variables globales en **OwO** se escriben en el archivo principal, afuera de las funciones, simplemente tienes que estar declaradas despu es de `OwO`.

Syntax varaibles:  
&nbsp;&nbsp;&nbsp;&nbsp;*tipo nombre = literal;*

### Funciones 
Las funciones se pueden definir con el siguiente syntax:

&nbsp;&nbsp;&nbsp;&nbsp;*function nombre tipo param1, tipo param2 : tipo {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;}*

Funciones pueden regresar cualquier tipo primitivo (pero es necesario tener un `return` al final que regrese el mismo tipo establecido en la función):
```
function dame_esos_cinco : int {
  return 5;
}
```

Funciones pueden no regresar nada (`void`, no es necesario `return` al final):

```
function imprime int x : void {
  print(x);
}
```

Funciones pueden recibir parametros ilimitados:
```
# creas función
function suma int x, int y : int {
  return x + y;
}
```

## Declaraciones
### Llamadas a funciones
Puedes llamar a funciones:
1. Sin parametros:  
&nbsp;&nbsp;&nbsp;&nbsp;*nombre_funcion();*
2. Con parametros:  
&nbsp;&nbsp;&nbsp;&nbsp;*nombre_funcion(expr);*

```
# llamada a función
suma(1,2);
```

## Estatutos de Control
### Condición If-Else

Los estatutos de condición pueden definirse con el siguiente syntax:
1. **if**:  
&nbsp;&nbsp;&nbsp;&nbsp;*if (condición) {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;}*
2. **if-else**:  
&nbsp;&nbsp;&nbsp;&nbsp;*if (condición) {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;} else {  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...  
&nbsp;&nbsp;&nbsp;&nbsp;}*

### Ciclo While
Los ciclos son definidos con el siguiente syntax:  
*while (condición) {  
&nbsp;&nbsp;&nbsp;&nbsp;...  
}*

```
int i = 0;
while (i < 10) {
  print(i);
  i = i + 1;
}
```

## Variables Dimensionadas
### Variables de 1-dimension
Las variables de 1-dimension o mejor conocidos como **arreglos** se definen con el siguiente syntax:  
&nbsp;&nbsp;&nbsp;&nbsp;*tipo nombre[int_literal];*
```
# Declaración de arreglo de 3 posiciones
int arr[3];
```

Para accesarlos se utiliza el siguiente syntax:  
&nbsp;&nbsp;&nbsp;&nbsp;*nombre[int_literal];*  
```
# Inicializando arreglo anterior
arr[0] = 0;
arr[1] = 1;
arr[2] = 2;
```


### Variables de 2-dimensiones
Las variables de 2-dimensiones o mejor conocidos como **matrices** se definen con el siguiente syntax:  
&nbsp;&nbsp;&nbsp;&nbsp;*tipo nombre[int_literal][int_literal];*
```
# Declaración de matriz de 2x2
int matriz[2][2];
```

Para accesarlos se utiliza el siguiente syntax:  
&nbsp;&nbsp;&nbsp;&nbsp;*nombre[int_literal][int_literal];*  
```
# Inicializando matriz anterior
matriz[0][0] = 0;
matriz[0][1] = 1;
matriz[1][0] = 2;
matriz[1][1] = 3;
```

## Expresiones
### Operadores Aritméticos
**Operadores Binarios**  

|Operación |Token|
|-----|--------|
|Suma|+|
|Resta|-|
|Multiplicación|*|
|División|/|
|Módulo|%|   
-----
**Operadores Unarios**
|Operación |Token|
|-----|--------|
|Positivo|+|
|Negativo|-|
-----
### Operadores Lógicos
**Operadores Binarios**
|Operación |Token|
|-----|--------|
|And|and|
|Or|or|
----
### Operadores Relacionales 
**Operadores Binarios**
|Operación |Token|
|-----|--------|
|Menor que|<|
|Mayor que|>|
|Menor igual que|<=|
|Mayor igual que|>=|
|Iguak|==|
|Diferente a|!=|
----
### Operadores de Asignación
**Operadores Binarios**
|Operación|Token|
|---------|-----|
|Igual|=|

### Asociatividad
Todos los operadores son asociativos a la izquierda, excepto el operador de asignación, es asociativo a la derecha.

### Ordén de Precedencia
- +, -
- *, /, %
- <, >, <=, >=, ==, !=
- or
- and
- =

#### Modificar Precedencia de Operadores
Se pueden utilizar parentesis para modificar la precedencia de los operadores en las expresiones:
```
x = 2 + 4 / 2;    # x = 4
x = (2 + 4) / 2;  # x = 3
```

## Lógica Aritmética

**OwO** tiene lógica aritmética, solo se pueden hacer operaciones entre enteros y enteros, flotantes y flotantes, o, enteros y flotantes.

## Funciones Especiales
**OwO** tiene varias funciones integradas para input y output:

### print
Te permite imprimir cualquier elemento primitivo en la consola.  
El syntax es el siguiente:
*print(expr);*
```
print("Hola mundo!");
```

### input
Te permite leer input del usuario. Existen 3 tipos de syntaxis distintas dependiendo de que tipo de variable estés intentando leer:
- Leer un string:

- Leer un int:  
  &nbsp;&nbsp;&nbsp;&nbsp;*nombre = input_i();*
- Leer un float:  
  &nbsp;&nbsp;&nbsp;&nbsp;*nombre = input_f();*
- Leer un string:  
  &nbsp;&nbsp;&nbsp;&nbsp;*nombre = input_s();*

```
# Leer numero entero (int)
# Leer numero flotante (float)
# Leer una palabra (string)
int i = input_i();
float f = input_f();
string s = input_s();
```

### concatenación de strings
En **OwO** es posible hacer concatenación de strings. La syntax es la siguiente:  
&nbsp;&nbsp;&nbsp;&nbsp;*string_literal + string_literal*

```
# s contiene "Hola Mundo! OwO" al final de la 3er línea
string s = "Hola " + "Mundo!";
s = s + "OwO";
```

## Comentarios
Utiliza el signo de gato `#` al principio de una línea de código para que el compilador la "ignore".
```
# Esto es un comentario
print("Este no es un comentario.");
```
