from utility.constants import *
from utility.quad import *
from utility.semantic_scope_tree import *
from utility.execution_scope_tree import *

mem = {}
mem_tree = ExecutionTree()
args_list_stack = []
return_instruction_pointer_stack = []
return_values = {}

class VirtualMachine:

    def __init__(self, quad_list, constants_table, semantic_tree, debug_mode=False):
        self.current_scope_stack = [0]
        self.quad_list = quad_list
        self.constants_table = constants_table
        self.semantic_tree = semantic_tree
        self.debug_mode = debug_mode
        self.instruction_pointer = 0
        self.current_semantic_scope_ref = -1
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
            Operations.ERA: self.op_era,
            Operations.PARAM: self.op_param,
            Operations.GOSUB: self.op_gosub,
            Operations.RETURN: self.op_return,
            Operations.ENDFUNC: self.op_endfunc,
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
        mem_tree.add_node(0,-1)
        for value in self.constants_table:
            constant_addr = self.constants_table[value]['addr']
            constant_type = self.constants_table[value]['type']
            if constant_type == Types.STRING_TYPE:
                value = value.strip('"')
            # mem[constant_addr] = self.type_map[constant_type](value)
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
        # s = mem[self.current_quad.target]
        s_t = mem_tree.get_value(self.current_quad.target)
        # self.output(f"Old: {s}")
        self.output(f"{s_t}")
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.current_semantic_scope_ref = 0
        self.set_constants()
        self.instruction_pointer += 1

    def op_end(self):
        self.output("Terminating OwO...")
        self.is_running = False
    
    def op_plus(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] + mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) + mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_minus(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] - mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) - mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_times(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] * mem[self.current_quad.right]

        global mem_tree
        left = mem_tree.get_value(self.current_quad.left)
        right = mem_tree.get_value(self.current_quad.right)
        tree_result = mem_tree.get_value(self.current_quad.left) * mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_divide(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] / mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) / mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_modulus(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] % mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) % mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equal(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left]

        global mem_tree
        # check if variable is global funciton return variable, which is not in memory
        if(str(self.current_quad.left)[0] == '$'):
            # print(f"{self.current_quad.target} = {self.current_quad.left}")
            # print(return_values)
            mem_tree.set_value(self.current_quad.target, return_values[self.current_quad.left])
        else:
            mem_tree.set_value(self.current_quad.target, mem_tree.get_value(self.current_quad.left))
        self.instruction_pointer += 1
    
    def op_or(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] or mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) or mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_and(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] and mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) and mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equalequal(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] == mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) == mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthan(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] < mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) < mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthan(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] > mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) > mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_notequal(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] != mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) != mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthanorequal(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] <= mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) <= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthanorequal(self):
        # global mem
        # mem[self.current_quad.target] = mem[self.current_quad.left] >= mem[self.current_quad.right]

        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) >= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_goto(self):
        self.instruction_pointer = self.current_quad.target
    

    def op_gotot(self):
        # condition = mem[self.current_quad.left]
        condition_t = mem_tree.get_value(self.current_quad.left)
        if condition_t == True:    
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_gotof(self):
        # condition = mem[self.current_quad.left]
        condition_t = mem_tree.get_value(self.current_quad.left)
        if condition_t == False:    
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_era(self):
        # Add empty list to store param values, add to to stack
        args_list_stack.append([])
        # Add return value key to return_values map
        return_values[f"${self.current_quad.left}_return_value"] = None
        self.instruction_pointer = self.instruction_pointer + 1

    def op_param(self):
        # Add param to last/top params list
        args_list_stack[-1].append(mem_tree.get_value(self.current_quad.left))
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_gosub(self):
        # Add current position + 1 to IP stack
        return_instruction_pointer_stack.append(self.instruction_pointer + 1)
        # Get gosub function info
        function_start_quad = self.current_quad.target
        function_semantic_scope_ref = self.current_quad.right
        function_name = self.semantic_tree.dict[function_semantic_scope_ref].func_name
        # Set new instruction pointer
        self.instruction_pointer = function_start_quad
        # TODO change execution node
        # USING SEMANTIC TREE
        # if function is child function, add step from current position
        # print(f"current_semantic_scope_ref: {self.current_semantic_scope_ref}")
        # print(self.semantic_tree)
        if(function_name in self.semantic_tree.dict[self.current_semantic_scope_ref].functions):
            mem_tree.add_node(function_semantic_scope_ref, mem_tree.current_node_ref)
        # if function is NOT child function, go up and find semantic parent, add step from parent
        else:
            aux_semantic_scope_ref = self.current_semantic_scope_ref
            while (aux_semantic_scope_ref > -1):
                # if function in semantic scope parent
                if (function_name in self.semantic_tree.dict[aux_semantic_scope_ref].functions):
                    # get equivalent execution node -> semantic scope
                    execution_parent_ref = mem_tree.get_node_ref(aux_semantic_scope_ref)
                    # add new node
                    mem_tree.add_node(function_semantic_scope_ref, execution_parent_ref)
                aux_semantic_scope_ref = self.semantic_tree.dict[aux_semantic_scope_ref].parent_ref
        self.current_semantic_scope_ref = function_semantic_scope_ref
        # TODO set up parameters
        # loop through list of parameters, form era stack
        params_list = self.semantic_tree.dict[self.current_semantic_scope_ref].params
        # print(f"args_list_stack: {args_list_stack}")
        # print(f"params_list[i]: {params_list}")
        # print(f"args_list_stack[-1]: {args_list_stack[-1]}")
        for i in range(0, len(args_list_stack[-1])):
            param_name = params_list[i]
            # print(f"param_name: {param_name}")
            arg_addr = self.semantic_tree.dict[self.current_semantic_scope_ref].vars[param_name]['addr']
            mem_tree.set_value(arg_addr, args_list_stack[-1][i])
            # print(f"arg_name: {args_list_stack[-1][i]}")
        args_list_stack.pop()
            
    
    def op_return(self):
        return_value = mem_tree.get_value(self.current_quad.target)
        return_values[self.current_quad.left] = return_value
        # print(return_values)
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_endfunc(self):
        self.instruction_pointer = return_instruction_pointer_stack[-1]
        return_instruction_pointer_stack.pop()
    

