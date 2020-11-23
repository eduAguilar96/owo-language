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