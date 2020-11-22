from utility.constants import *
from utility.quad import *
from utility.scope_tree import *

class VirtualMachine:

    def __init__(self, quad_list, debug_mode=False):
        self.current_scope_stack = [0]
        self.quad_list = quad_list
        self.quad_list_adr = []
        self.debug_mode = debug_mode
        self.instruction_pointer = 0
        self.op_map = {
            Operations.START: self.op_start,
            Operations.PRINT: self.op_print,
            Operations.END: self.op_end,
        }
        self.is_running = False
        self.current_quad = None
    
    def transform_quads(self):
        print("Transforming quaqds to addresses")
        # TODO tranform quads to contain addresses
        self.quad_list_adr = self.quad_list

    def execute_quads(self):
        self.transform_quads()
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
        self.current_quad = self.quad_list_adr[self.instruction_pointer]
    
    def op_error(self):
        raise Exception("OwO: Unkown op code")

    def output(self, s):
        print(f"OwO> {s}")

    def op_print(self):
        self.output(self.current_quad.target)
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.instruction_pointer += 1

    def op_end(self):
        self.output("Terminating OwO...")
        self.is_running = False
