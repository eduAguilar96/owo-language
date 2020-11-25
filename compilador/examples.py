data_examples = []

class Example:

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return self.name

data_examples.append(Example(
    'Declare Variables',
    '''
        OwO
        int num = 12345;
        string nombre = "Juanito";
        float pi = 3.1416;
        bool nose = num > pi;
    '''
))

data_examples.append(Example(
    'Invalid variable',
    '''
        OwO
        int numero = "numero";
    '''
))

data_examples.append(Example(
    'Complex Variable',
    '''
        OwO
        int A = 1;
        int B = 2;
        int C = 3;
        int D = 4;
        int suma = A + B + C + D;
        print(suma);
    '''
))

data_examples.append(Example(
    'If else',
    '''
        OwO
        int A = 1;
        int B = 1;
        int C = 3;
        int D = 5;
        if (A + B > C) {
            print("Inside if");
            A = B + C;
        } else {
            print("Inside else");
            A = B + C * D;
        }
    '''
))

data_examples.append(Example(
    'While loop',
    '''
        OwO
        int A = 4;
        int B = 3;
        int C = 5;
        int D = 7;

        while (A > B * C) {
            A = A + D;
        }
        B = C + A;
    '''
))

data_examples.append(Example(
    'Nested Function calls',
    '''
        OwO

        int global = 9000;

        function masUno int x : int {
            return x + 1;
        }

        function masDos int x : int {
            return x + 2;
        }

        function process int x, int y, int z : int {
            int a = 0;
            return a;
        }

        #string hola = "hola";
        #int a = masUno(5);
        #int b = 5;
        #int c = process(1,masUno(5), 3);
        print(masUno(masUno(1)));
    '''
))

data_examples.append(Example(
    'Paramterless Functions',
    '''
        OwO

        function masUno int x : int {
            return x + 1;
        }

        function cero : int {
            return 0;
        }


        # int x = masUno(1); Esto causa un error
        int zero = cero();
        int x = masUno(1);

    '''
))

data_examples.append(Example(
    'Void Functions',
    '''
        OwO

        function nada : void {
            int x = 6;
        }

        nada();
    '''
))

data_examples.append(Example(
    'Print Function',
    '''
        OwO

        print("Hello World");
        #string hola = "Hola mundo";
        #print(hola);
    '''
))

data_examples.append(Example(
    'Declare empty variables',
    '''
        OwO
        int a;
        a = 1;
    '''
))

data_examples.append(Example(
    'Dos whiles de Guadiana',
    '''
        OwO
        int i = 0;
        while (i < 10) {
            int x = 3000;
            i = i + 1;
            print(x + i);
        }
        i = 0;
        while (i < 10) {
            int x = 3000;
            i = i + 1;
            print(i);
        }
    '''
))

data_examples.append(Example(
    'Recursion de Aaron',
    '''
        OwO
        int global = 999;

        function addOne int x : int {
            int y = 4 + global;
            print(y);

            function addTwo int x : int {
                print(x);
                if (x < 10) {
                    x = x + 2 + addTwo(x);
                }
                return x;
            }

            return addTwo(x + 1);
        }

        function minusOne int x : int {
            return addOne(x) - 2;
        }

        print(minusOne(1));
    '''
))

data_examples.append(Example(
    'Modulus',
    '''
        OwO
        print(10 % 2);
    '''
))

data_examples.append(Example(
    'Boolean',
    '''
        OwO
        bool a = True;
        bool b = False;
        string hello = "hello";
        string world = "world";
        print(hello + world);
        print("4 > 5");
        print(4 > 5);
        print("4 < 5");
        print(4 < 5);
        print("4 <= 5");
        print(4 <= 5);
        print("5 <= 5");
        print(5 <= 5);

        print("h" + "e" + "l" + "l" + "o" + " " + "w" + "o" + "r" + "l" + "d");
    '''
))

data_examples.append(Example(
    'Recursion',
    '''
        OwO
        function nose int x : void {
            print(x);
            if(x < 10) {
                nose(x + 1);
            }
        }
        nose(1);
    '''
))

# TODO add error check for when a function has no return
data_examples.append(Example(
    'Fibbonacci',
    '''
OwO
function fibo int x : int {
    if (x <= 1) {
        return x;
    }
    return fibo(x-1) + fibo(x-2);
}
print(fibo(0));
print(fibo(1));
print(fibo(2));
print(fibo(3));
print(fibo(4));
print(fibo(5));
print(fibo(6));
    '''
))

data_examples.append(Example(
    'Basic Recursive',
     '''
        OwO
        function masUno int x : int {
            print("Inside masUno");
            print(x);
            if (x <= 1) {
                x = masUno(x+1);
            }
            return x;
        }
        print(masUno(0));
     '''
))

data_examples.append(Example(
    'Input',
    '''
        OwO
        print("How old are you?");
        int a = input_i();
        print("How tall are you?");
        float height = input_f();
        print("whats your name?");
        string name = input_s();

        print("Hello " + name + " its great to meet you!");
        print(name + " is...");
        print(height);
        print("...meters tall");
        print(name + " is...");
        print(a);
        print("...years old");


    '''
))

data_examples.append(Example(
    'Concatenated function calls',
    '''
        OwO
        function masUno int n : int {
            return n + 1;
        }
        print(masUno(1));
        print(masUno(masUno(1)));
        print(masUno(1) + masUno(1));
    '''
))

data_examples.append(Example(
    'Concatenated function calls in return',
    '''
        OwO

        function masUno int n : int {
            return n + 1;
        }

        function two int n : int {
            return masUno(0) + masUno(0);
        }

        function timesTwo int n : int {
            return n * 2;
        }

        print(two(1));
    '''
))

data_examples.append(Example(
    'Verify Math',
    '''
        OwO
        print(4 * (1 + 1));
    '''
))

data_examples.append(Example(
    'Test Arrays',
    '''
        OwO
        int A[10];
        A[4] = 5;
        print(A[4]);
        print(A[4]);

        int B[2][3];
        B[0][2] = A[4];
        int x = B[0][1+1];
        print(x);
    '''
))

# TODO add error check for when a function has no return
data_examples.append(Example(
    'Fibbonacci with cache',
    '''
OwO
# print("Begin");
int f[500];
int i = 0;
# print("Declared");
while (i < 500) {
    # print(i);
    f[i] = 0;
    i = i + 1;
}
print("After while");
function fibo int x : int {
    if (x <= 1) {
        return x;
    }
    if (f[x] == 0) {
        int fibo = fibo(x-1) + fibo(x-2);
        f[x] = fibo;
    }
    return f[x];
}
print(fibo(0));
print(fibo(1));
print(fibo(2));
print(fibo(3));
print(fibo(4));
print(fibo(5));
print(fibo(6));
print(fibo(100));
    '''
))

data_examples.append(Example(
    'Verify input',
    '''
        OwO
        int x = input_i();
        print(x);
    '''
))



'''
BUBBLE SORT: (FAILING):
OwO

int arr2[4];
arr2[0] = 64;
arr2[1] = 34;
arr2[2] = 25;
arr2[3] = 12;
#arr2[4] = 22;
#arr2[5] = 11;
#arr2[6] = 90;

function print_arr int n : void {
  int i = 0;
  while (i < n) {
    print(arr2[i]);
    i = i + 1;
  }
}

function swap int x, int y, int i, int j: void {
  print("Being swap: ");
  print("i: ");
  print(i);
  print("j: ");
  print(j);
  print("Before swap: ");
  print(arr2[i]);
  print(arr2[j]);
  int tmp = x;
  arr2[i] = y;
  arr2[j] = tmp;
  print("After swap: ");
  print(arr2[j]);
  print(arr2[i]);
}

#swap(arr2[0], arr2[1], 0, 1);

function bubble_sort int n : void {
print("Entering Bubble Sort: ");
  int i = 0;
  int j = 0;
  while (i < n-1) {
    while (j < n-i-1){
      if (arr2[j] > arr2[j+1]) {
        swap(arr2[j], arr2[j+1], j, j+1);
      }
      print("###### j ######");
	  print(j);
      j = j + 1;
    }
    print("###### i ######");
	print(i);
    i = i + 1;
  }
}

print("Unsorted stuff: ");
print_arr(4);
print("Sorted array: ");
bubble_sort(4);
print_arr(4);
'''

'''
BUBBLE SORT (arr of size 2):
OwO

int size = 100;
int arr[100];

int i = 0;
while (i < size) {
    arr[i] = 0;
    i = i + 1;
}

# First number is 0
# Second number is 1
arr[0] = 0;
arr[1] = 1;

# Calculates fib till size
function fib_n int n : void {
  i = 2;
  while (i < size) {
    arr[i] = arr[i-2] + arr[i-1];
    i = i + 1;
  }
  print("Fib answer: ");
  if (n < size) {
    print(arr[n]);
  }
}

fib_n(3);
fib_n(4);
fib_n(5);
fib_n(6);
fib_n(7);
'''


'''
# FIND CODE:
OwO

int arr[7];
arr[0] = 64;
arr[1] = 34;
arr[2] = 25;
arr[3] = 12;
arr[4] = 22;
arr[5] = 11;
arr[6] = 90;


function print_arr int n : void {
  int i = 0;
  while (i < n) {
    print(arr[i]);
    i = i + 1;
  }
}

function find int size, int n : void {
  int i = 0;
  bool found_something = False;
  while (i < size) {
    int curr = arr[i];
    if (curr == n) {
      found_something = True;
      print("Found number: ");
      print(n);
      print("In position: ");
      print(i);
    }
    i = i + 1;
  }
  if (found_something == False) {
    print("Didn't find number: ");
    print(n);
  }
}

find(7, 11);
find(7, 90);
find(7, 999);
find(7, 64);
'''


'''
# Fibonacci iterativo

OwO

int size = 100;
int arr[100];

int i = 0;
while (i < size) {
    arr[i] = 0;
    i = i + 1;
}

# First number is 0
# Second number is 1
arr[0] = 0;
arr[1] = 1;

# Calculates fib till size
function fib_n int n : void {
  i = 2;
  while (i < size) {
    arr[i] = arr[i-2] + arr[i-1];
    i = i + 1;
  }
  print("Fib answer: ");
  if (n < size) {
    print(arr[n]);
  }
}

fib_n(3);
fib_n(4);
fib_n(5);
fib_n(6);
fib_n(7);

'''

'''
MULTIPLICACION DE MATRICES (FAILED)

OwO
int res[2][2];
int mat1[2][2];
int mat2[2][2];
int n = 2;
int i = 0;
int j = 0;
int k = 0;

res[0][0] = 0;
res[0][1] = 0;
res[1][0] = 0;
res[1][1] = 0;

mat1[0][0] = 1;
mat1[0][1] = 1;
mat1[1][0] = 2;
mat1[1][1] = 2;

mat2[0][0] = 1;
mat2[0][1] = 1;
mat2[1][0] = 2;
mat2[1][1] = 2;

i = 0;
j = 0;
k = 0;

while(i < n) {
  while(j < n) {
    while(k < n) {
      res[i][j] = res[i][j] + mat1[i][k] * mat2[k][j];
      k = k + 1;
    }
    j = j + 1;
  }
  i = i + 1;
}

print("Result: ");

i = 0;
j = 0;
while(i < n) {
  while(j < n) {
    print("### i ###");
    print(i);
    print("### j ###");
    print(j);
    print("### res[i][j] ###");
    print(res[i][j]);
    j = j + 1;
  }
  i = i + 1;
}
'''