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
        int suma = A + B and C >= D or B;
    '''
))

data_examples.append(Example(
    'If else',
    '''
        OwO
        if (A + B < C) {
            A = B + C;
        } else {
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
        int b = 5;
        int c = process(1,masUno(5), 3);
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

        int zero = cero();
        int x = masUno(x);
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
        string hola = "Hola mundo";
        print(hola);
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
