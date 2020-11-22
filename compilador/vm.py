from utility.constants import *
from utility.quad import *
from utility.semantic_scope_tree import *
from utility.execution_scope_tree import *

mem = {}
mem_tree = ExecutionTree()

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
            Operations.AND: self.op_and,
            Operations.OR: self.op_or,
            Operations.LESSTHAN: self.op_lessthan,
            Operations.GREATERTHAN: self.op_greaterthan,
            Operations.EQUALEQUAL: self.op_equalequal,
            Operations.NOTEQUAL: self.op_notequal,
            Operations.LESSTHANOREQUAL: self.op_lessthanorequal,
            Operations.GREATERTHANOREQUAL: self.op_greaterthanorequal,
            Operations.GOTO: self.op_goto,
            Operations.GOTOT: self.op_gotot,
            Operations.GOTOF: self.op_gotof,
        }
        self.type_map = {
            Types.INT_TYPE: int,
            Types.STRING_TYPE: str,
            Types.FLOAT_TYPE: float,
            Types.BOOL_TYPE: self.to_bool,
        }
        self.is_running = False
        self.current_quad = None
    
    def print_mem(self):
        print(mem)
    
    def print_mem_tree(self):
        print(mem_tree)

    def to_bool(self, s):
        return s == "True"

    def set_constants(self):
        mem_tree.add_node()
        for value in self.constants_table:
            constant_addr = self.constants_table[value]['addr']
            constant_type = self.constants_table[value]['type']
            if constant_type == Types.STRING_TYPE:
                value = value.strip('"')
            mem[constant_addr] = self.type_map[constant_type](value)
            mem_tree.set_value(constant_addr, self.type_map[constant_type](value))
        # print(self.constants_table)
        # print(mem)

    def execute_quads(self):
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
        s = mem[self.current_quad.target]
        s_t = mem_tree.get_value(self.current_quad.target)
        self.output(f"Old: {s}")
        self.output(f"New: {s_t}")
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.set_constants()
        self.instruction_pointer += 1

    def op_end(self):
        self.output("Terminating OwO...")
        self.is_running = False
    
    def op_plus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] + mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) + mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_minus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] - mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) - mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_times(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] * mem[self.current_quad.right]

        global mem_tree
        left = mem_tree.get_value(self.current_quad.left)
        right = mem_tree.get_value(self.current_quad.right)
        tree_result = mem_tree.get_value(self.current_quad.left) * mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_divide(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] / mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) / mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_modulus(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] % mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) % mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left]

        global mem_tree
        mem_tree.set_value(self.current_quad.target, mem_tree.get_value(self.current_quad.left))
        self.instruction_pointer += 1
    
    def op_or(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] or mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) or mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_and(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] and mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) and mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equalequal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] == mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) == mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthan(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] < mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) < mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthan(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] > mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) > mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_notequal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] != mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) != mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthanorequal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] <= mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) <= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthanorequal(self):
        global mem
        mem[self.current_quad.target] = mem[self.current_quad.left] >= mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) >= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_goto(self):
        self.instruction_pointer = self.current_quad.target
    

    def op_gotot(self):
        condition = mem[self.current_quad.left]
        condition_t = mem_tree.get_value(self.current_quad.left)
        if condition_t == True:    
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_gotof(self):
        condition = mem[self.current_quad.left]
        condition_t = mem_tree.get_value(self.current_quad.left)
        if condition_t == False:    
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1