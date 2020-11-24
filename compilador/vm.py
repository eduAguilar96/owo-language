from compilador.utility.constants import *
from compilador.utility.quad import *
from compilador.utility.semantic_scope_tree import *
from compilador.utility.execution_scope_tree import *

class VirtualMachine:

    def __init__(self, quad_list, constants_table, semantic_tree, virtual_var_list, debug_mode=False, stdoutin=None):
        self.bash_signature = "OwO"
        self.current_scope_stack = [0]
        self.quad_list = quad_list
        self.constants_table = constants_table
        self.virtual_var_list = virtual_var_list
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
            Operations.VER: self.op_ver,
        }
        self.type_map = {
            Types.INT_TYPE: int,
            Types.STRING_TYPE: str,
            Types.FLOAT_TYPE: float,
            Types.BOOL_TYPE: self.to_bool,
        }
        self.std = {
            'in': 0,
            'out': 1,
            'err': 2,
            'status': 3,
        }
        self.is_running = False
        self.current_quad = None
        self.stdoutin = stdoutin
        self.mem_tree = ExecutionTree()
        self.args_list_stack = []
        self.semantic_tree_ref_stack = []
        self.return_instruction_pointer_stack = []
        self.return_values = {}

    def print_mem_tree(self):
        print(self.mem_tree)

    def to_bool(self, s):
        return s == "True"

    def set_constants(self):
        self.mem_tree.add_node(0,-1)
        for value in self.constants_table:
            constant_addr = self.constants_table[value]['addr']
            constant_type = self.constants_table[value]['type']
            if constant_type == Types.STRING_TYPE:
                value = value.strip('"')
            self.set_value(constant_addr, self.type_map[constant_type](value))

    def execute_quads(self, run_in_terminal=False):
        if run_in_terminal:
            self.execute_quads_in_terminal()
            return
        while True:
            self.set_current_quad()
            op_code = self.current_quad.op_code
            print(f'Last opcode ran ({op_code})')
            stdin = self.stdoutin[self.std['in']]
            # TODO Handle case when user executes vm accidentally with an enter,
            # either by disabling the enter  on the graphical side till there's
            # a print or by checking for stdin and op_code mismatch here in vm.
            if not stdin and op_code in [Operations.INPUTSTRING, Operations.INPUTINT, Operations.INPUTFLOAT]:
                print(f"Enterng yield because of opcode ({op_code})")
                return op_code
            self.execute_op(op_code)
            if op_code in [Operations.PRINT]:
                print(f"Pausing execution for output... {op_code}")
                return op_code
            if(not self.is_running):
                return None

    def execute_quads_in_terminal(self):
        while True:
            self.set_current_quad()
            op_code = self.current_quad.op_code
            self.execute_op(op_code)
            if(not self.is_running):
                break

    def get_value(self, addr, check_for_virtual=True):
        if check_for_virtual and addr in self.virtual_var_list:
            return self.mem_tree.get_value(self.mem_tree.get_value(addr))
        return self.mem_tree.get_value(addr)

    def set_value(self, addr, result, check_for_virtual=False):
        if check_for_virtual and addr in self.virtual_var_list:
            addr = self.mem_tree.get_value(addr)
            self.mem_tree.set_value(addr, result)
        self.mem_tree.set_value(addr, result)
        pass


    def execute_op(self, op_code):
        # print(f"Executing {op_code}")
        self.op_map.get(op_code, self.op_error)()
        # self.print_mem_tree()

    def set_current_quad(self):
        self.current_quad = self.quad_list[self.instruction_pointer]

    def op_error(self):
        raise Exception(f"OwO: Unkown op code {self.current_quad.op_code}")

    def output(self, s):
        output_msg = f"{self.bash_signature}> {s}"
        print(output_msg)
        if self.stdoutin is not None:
            self.stdoutin[self.std['out']] += f"{output_msg}\n"


    def op_print(self):
        s_t = self.get_value(self.current_quad.target)
        self.output(f"{s_t}")
        self.instruction_pointer += 1

    def op_start(self):
        self.is_running = True
        self.current_semantic_scope_ref = 0
        self.semantic_tree_ref_stack.append(0)
        self.set_constants()
        self.instruction_pointer += 1

    def op_end(self):
        if self.debug_mode:
            self.output("Terminating OwO...")
        self.is_running = False

    def op_plus(self):
        tree_result = self.get_value(self.current_quad.left) + self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_minus(self):
        tree_result = self.get_value(self.current_quad.left) - self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_times(self):
        tree_result = self.get_value(self.current_quad.left) * self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_divide(self):
        tree_result = self.get_value(self.current_quad.left) / self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_modulus(self):
        tree_result = self.get_value(self.current_quad.left) % self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_equal(self):
        # if saving from global return value variable
        if(str(self.current_quad.left)[0] == '$'):
            self.set_value(self.current_quad.target, self.return_values[self.current_quad.left])
        else:
            self.set_value(self.current_quad.target, self.get_value(self.current_quad.left), True)
        self.instruction_pointer += 1

    def op_or(self):
        tree_result = self.get_value(self.current_quad.left) or self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_and(self):
        tree_result = self.get_value(self.current_quad.left) and self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_equalequal(self):
        tree_result = self.get_value(self.current_quad.left) == self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_lessthan(self):
        tree_result = self.get_value(self.current_quad.left) < self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_greaterthan(self):
        tree_result = self.get_value(self.current_quad.left) > self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_notequal(self):
        tree_result = self.get_value(self.current_quad.left) != self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_lessthanorequal(self):
        tree_result = self.get_value(self.current_quad.left) <= self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_greaterthanorequal(self):
        tree_result = self.get_value(self.current_quad.left) >= self.get_value(self.current_quad.right)
        self.set_value(self.current_quad.target, tree_result)
        self.instruction_pointer += 1

    def op_goto(self):
        self.instruction_pointer = self.current_quad.target

    def op_gotot(self):
        condition_t = self.get_value(self.current_quad.left)
        if condition_t == True:
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1

    def op_gotof(self):
        condition_f = self.get_value(self.current_quad.left)
        if condition_f == False:
            self.instruction_pointer = self.current_quad.target
            return
        self.instruction_pointer = self.instruction_pointer + 1

    def op_era(self):
        # Add empty list to store param values, add to to stack
        self.args_list_stack.append([])
        # Add return value key to self.return_values map
        self.return_values[f"${self.current_quad.left}_return_value"] = None
        self.instruction_pointer = self.instruction_pointer + 1

    def op_param(self):
        # Add param to last/top params list
        self.args_list_stack[-1].append(self.get_value(self.current_quad.left))
        self.instruction_pointer = self.instruction_pointer + 1

    def op_gosub(self):
        # Add current position + 1 to IP stack
        self.return_instruction_pointer_stack.append(self.instruction_pointer + 1)
        # self.Get gosub function info
        function_start_quad = self.current_quad.target
        function_semantic_scope_ref = self.current_quad.right
        function_name = self.semantic_tree.dict[function_semantic_scope_ref].func_name
        # Set new instruction pointer
        self.instruction_pointer = function_start_quad
        # USING SEMANTIC TREE
        # if function is self, add layer
        if(function_name == self.semantic_tree.dict[self.semantic_tree_ref_stack[-1]].func_name):
            self.mem_tree.add_layer()
        # if function is child function, add step from current position
        elif(function_name in self.semantic_tree.dict[self.semantic_tree_ref_stack[-1]].functions):
            self.mem_tree.add_node(function_semantic_scope_ref, self.mem_tree.current_node_ref)
        # if function is NOT child function, go up and find semantic parent, add step from parent
        else:
            aux_semantic_scope_ref = self.semantic_tree_ref_stack[-1]
            while (aux_semantic_scope_ref > -1):
                # print(self.semantic_tree.dict[aux_semantic_scope_ref])
                # if function in semantic scope parent
                if (function_name in self.semantic_tree.dict[aux_semantic_scope_ref].functions):
                    # get equivalent execution node -> semantic scope
                    execution_parent_ref = self.mem_tree.get_node_ref(aux_semantic_scope_ref)
                    # add new node
                    self.mem_tree.add_node(function_semantic_scope_ref, execution_parent_ref)
                aux_semantic_scope_ref = self.semantic_tree.dict[aux_semantic_scope_ref].parent_ref
        self.semantic_tree_ref_stack.append(function_semantic_scope_ref)

        # loop through list of parameters and list of arguments
        params_list = self.semantic_tree.dict[self.semantic_tree_ref_stack[-1]].params
        for i in range(0, len(self.args_list_stack[-1])):
            param_name = params_list[i]
            arg_addr = self.semantic_tree.dict[self.semantic_tree_ref_stack[-1]].vars[param_name]['addr']
            self.set_value(arg_addr, self.args_list_stack[-1][i])
        self.args_list_stack.pop()

    def op_return(self):
        return_value = self.get_value(self.current_quad.target)
        self.return_values[self.current_quad.left] = return_value
        self.instruction_pointer = self.instruction_pointer + 1

    def op_endfunc(self):
        self.mem_tree.step_back()
        self.instruction_pointer = self.return_instruction_pointer_stack[-1]
        self.return_instruction_pointer_stack.pop()
        self.semantic_tree_ref_stack.pop()

    def flush_stdin(self):
        self.stdoutin[self.std['in']] = ''

    def op_inputstring(self):
        # i = input(f"{self.bash_signature}<s ")
        i = self.stdoutin[self.std['in']]
        # flush stdin
        self.flush_stdin()
        self.set_value(self.current_quad.target, str(i))
        self.instruction_pointer = self.instruction_pointer + 1


    def op_inputint(self):
        i = input(f"{self.bash_signature}<i ")
        self.set_value(self.current_quad.target, int(i))
        self.instruction_pointer = self.instruction_pointer + 1

    def op_inputfloat(self):
        i = input(f"{self.bash_signature}<f ")
        self.set_value(self.current_quad.target, float(i))
        self.instruction_pointer = self.instruction_pointer + 1

    def op_ver(self):
        high_range = self.get_value(self.current_quad.right)
        index = self.get_value(self.current_quad.target)
        if index < 0 or index >= high_range:
            raise Exception(f"OwO: Trying to access value outside of dimensioned variable range")
        self.instruction_pointer = self.instruction_pointer + 1
        pass
