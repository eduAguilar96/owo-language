class ExecutionTree:

    def __init__(self):
        self.current_node_ref = -1
        self.node_dict = {}
    
    def __error(self, e):
        raise Exception(f"OwO: ExecutionTree: {e}")
    
    def __get_node_ref_for_addr(self, addr):
        aux_node_ref = self.current_node_ref
        while(aux_node_ref > -1):
            aux_node = self.node_dict[aux_node_ref]
            if(addr in aux_node.layer_stack[-1]):
                return aux_node_ref
            aux_node_ref = aux_node.parent_node_ref
        return -1
    
    def __str__(self):
        lista = [str(self.node_dict[ref]) for ref in range(0, len(self.node_dict))]
        return "\n".join(lista)
    
    def get_value(self, addr):
        aux_node_ref = self.__get_node_ref_for_addr(addr)
        if aux_node_ref != -1:
            return self.node_dict[aux_node_ref].layer_stack[-1][addr]
        self.__error(f"could not find address {addr}, current execution node: {self.current_node_ref}")
    
    def set_value(self, addr, value):
        aux_node_ref = self.__get_node_ref_for_addr(addr)
        # If address found, override in tree
        if aux_node_ref != -1:
            self.node_dict[aux_node_ref].layer_stack[-1][addr] = value
        # If address not found, add to current layer/mem
        else:
            node = self.node_dict[self.current_node_ref]
            layer_stack_top = node.layer_stack[-1]
            layer_stack_top[addr] = value
        
    def add_node(self):
        last_empty_ref = len(self.node_dict)
        new_node = Node(last_empty_ref, self.current_node_ref)
        self.node_dict[new_node.node_ref] = new_node
        self.current_node_ref = new_node.node_ref
    
    def add_layer(self):
        node = self.node_dict[self.current_node_ref]
        node.add_layer()
    
    def step_back(self):
        if len(self.node_dict[self.current_node_ref].layer_stack) > 0:
            self.node_dict[self.current_node_ref].layer_stack.pop()
            return
        self.current_node_ref = self.node_dict[self.current_node_ref].parent_node_ref

class Node:

    def __init__(self, node_ref, parent_node_ref):
        self.node_ref = node_ref
        self.parent_node_ref = parent_node_ref
        self.layer_stack = [{}]
    
    def __str__(self):
        return f"ref:{self.node_ref}, parent_ref:{self.parent_node_ref}, layer_stack:{self.layer_stack}"
    
    def add_layer(self):
        self.layer_stack.append({})      

# class Layer:
#     def __init__(self):
#         self.mem = {}