from utility.constants import *
from utility.quad import *
from utility.scope_tree import *

mem = {}

class VirtualMachine:

    def __init__(self, quad_list, constants_table, debug_mode=False):
        self.current_scope_stack = [0]
        self.quad_list = quad_list
        self.constants_table = constants_table
        self.debug_mode = debug_mode
        self.instruction_pointer = 0
        self.op_map = {
            Operations.START: self.op_start,
            Operations.PRINT: self.op_print,
            Operations.END: self.op_end,
            Operations.PLUS: self.op_plus,
            Operations.MINUS: self.op_minus,
            Operations.TIMES: self.op_times,
            Operations.DIVIDE: self.op_divide,
            Operations.MODULUS: self.op_modulus,
            Operations.EQUAL: self.op_equal,
        }
        self.type_map = {
            Types.INT_TYPE: int,
            Types.STRING_TYPE: str,
            Types.FLOAT_TYPE: float,
            Types.BOOL_TYPE: bool,
        }
        self.is_running = False
        self.current_quad = None
    
    def print_mem(self):
        print(mem)

    def set_constants(self):
        print("Setting Constants")
        for key in self.constants_table:
            constant_addr = self.constants_table[key]['addr']
            constant_type = self.constants_table[key]['type']
            mem[constant_addr] = self.type_map[constant_type](key)

    def execute_quads(self):
        self.set_constants()
        print("Executing quads")
        while True:
            self.set_current_quad()
            op_code = self.current_quad.op_code
            self.execute_op(op_code)
            if(not self.is_running):
                break
    
    def execute_op(self, op_code):
        self.op_map.get(op_code, self.op_error)()

    def set_current_quad(self):
        self.current_quad = self.quad_list[self.instruction_pointer]
    
    def op_error(self):
        raise Exception(f"OwO: Unkown op code {self.current_quad.op_code}")

    def output(self, s):
        print(f"OwO> {s}")

    def op_print(self):
        self.output(mem[self.current_quad.target])
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.instruction_pointer += 1

    def op_end(self):
        self.output("Terminating OwO...")
        self.is_running = False
    
    def op_plus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] + mem[self.current_quad.right]
        self.instruction_pointer += 1
    
    def op_minus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] - mem[self.current_quad.right]
        self.instruction_pointer += 1
    
    def op_times(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] * mem[self.current_quad.right]
        self.instruction_pointer += 1
    
    def op_divide(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] / mem[self.current_quad.right]
        self.instruction_pointer += 1
    
    def op_modulus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] % mem[self.current_quad.right]
        self.instruction_pointer += 1
    
    def op_equal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left]
        self.instruction_pointer += 1

