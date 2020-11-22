from utility.constants import *
from utility.quad import *
from utility.semantic_scope_tree import *
from utility.execution_scope_tree import *

mem_tree = ExecutionTree()
args_list_stack = []
semantic_tree_ref_stack = []
return_instruction_pointer_stack = []
return_values = {}

class VirtualMachine:

    def __init__(self, quad_list, constants_table, semantic_tree, debug_mode=False):
        self.bash_signature = "OwO"
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
            Operations.INPUTSTRING: self.op_inputstring,
            Operations.INPUTINT: self.op_inputint,
            Operations.INPUTFLOAT: self.op_inputfloat,
        }
        self.type_map = {
            Types.INT_TYPE: int,
            Types.STRING_TYPE: str,
            Types.FLOAT_TYPE: float,
            Types.BOOL_TYPE: self.to_bool,
        }
        self.is_running = False
        self.current_quad = None
    
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
            mem_tree.set_value(constant_addr, self.type_map[constant_type](value))
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
        print(f"{self.bash_signature}> {s}")

    def op_print(self):
        s_t = mem_tree.get_value(self.current_quad.target)
        self.output(f"{s_t}")
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.current_semantic_scope_ref = 0
        global semantic_tree_ref_stack
        semantic_tree_ref_stack.append(0)
        self.set_constants()
        self.instruction_pointer += 1

    def op_end(self):
        self.output("Terminating OwO...")
        self.is_running = False
    
    def op_plus(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) + mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_minus(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) - mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_times(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) * mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_divide(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) / mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_modulus(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) % mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equal(self):
        global mem_tree
        # check if variable is global funciton return variable, which is not in memory
        if(str(self.current_quad.left)[0] == '$'):
            mem_tree.set_value(self.current_quad.target, return_values[self.current_quad.left])
        else:
            mem_tree.set_value(self.current_quad.target, mem_tree.get_value(self.current_quad.left))
        self.instruction_pointer += 1
    
    def op_or(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) or mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_and(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) and mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_equalequal(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) == mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthan(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) < mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthan(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) > mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_notequal(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) != mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_lessthanorequal(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) <= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_greaterthanorequal(self):
        global mem_tree
        tree_result = mem_tree.get_value(self.current_quad.left) >= mem_tree.get_value(self.current_quad.right)
        mem_tree.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1
    
    def op_goto(self):
        self.instruction_pointer = self.current_quad.target
    

    def op_gotot(self):
        condition_t = mem_tree.get_value(self.current_quad.left)
        if condition_t == True:    
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_gotof(self):
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
        # USING SEMANTIC TREE
        # if function is self, add layer
        if(function_name == self.semantic_tree.dict[semantic_tree_ref_stack[-1]].func_name):
            mem_tree.add_layer()
        # if function is child function, add step from current position
        elif(function_name in self.semantic_tree.dict[semantic_tree_ref_stack[-1]].functions):
            mem_tree.add_node(function_semantic_scope_ref, mem_tree.current_node_ref)
        # if function is NOT child function, go up and find semantic parent, add step from parent
        else:
            aux_semantic_scope_ref = semantic_tree_ref_stack[-1]
            while (aux_semantic_scope_ref > -1):
                # print(self.semantic_tree.dict[aux_semantic_scope_ref])
                # if function in semantic scope parent
                if (function_name in self.semantic_tree.dict[aux_semantic_scope_ref].functions):
                    # get equivalent execution node -> semantic scope
                    execution_parent_ref = mem_tree.get_node_ref(aux_semantic_scope_ref)
                    # add new node
                    mem_tree.add_node(function_semantic_scope_ref, execution_parent_ref)
                aux_semantic_scope_ref = self.semantic_tree.dict[aux_semantic_scope_ref].parent_ref
        semantic_tree_ref_stack.append(function_semantic_scope_ref)

        # loop through list of parameters and list of arguments
        params_list = self.semantic_tree.dict[semantic_tree_ref_stack[-1]].params
        for i in range(0, len(args_list_stack[-1])):
            param_name = params_list[i]
            arg_addr = self.semantic_tree.dict[semantic_tree_ref_stack[-1]].vars[param_name]['addr']
            mem_tree.set_value(arg_addr, args_list_stack[-1][i])
        args_list_stack.pop()
            
    
    def op_return(self):
        return_value = mem_tree.get_value(self.current_quad.target)
        return_values[self.current_quad.left] = return_value
        self.instruction_pointer = self.instruction_pointer + 1
    
    def op_endfunc(self):
        mem_tree.step_back()
        self.instruction_pointer = return_instruction_pointer_stack[-1]
        return_instruction_pointer_stack.pop()
        semantic_tree_ref_stack.pop()

    def op_inputstring(self):
        i = input(f"{self.bash_signature}<s ")
        mem_tree.set_value(self.current_quad.target, str(i))
        self.instruction_pointer = self.instruction_pointer + 1


    def op_inputint(self):
        i = input(f"{self.bash_signature}<i ")
        mem_tree.set_value(self.current_quad.target, int(i))
        self.instruction_pointer = self.instruction_pointer + 1

    def op_inputfloat(self):
        i = input(f"{self.bash_signature}<f ")
        mem_tree.set_value(self.current_quad.target, float(i))
        self.instruction_pointer = self.instruction_pointer + 1
    

