class ExecutionTree:
    '''Stores the memory of the program dynamically during execution in a tree-like structure'''

    def __init__(self):
        self.current_node_ref = -1
        self.node_path_stack = []
        self.node_dict = {}
    
    def __error(self, e):
        raise Exception(f"OwO: ExecutionTree: {e}")
    
    def __get_node_ref_for_addr(self, addr):
        '''Get the node_ref for the node that contains the specified address.
        Moves upward in the tree to find such node'''
        aux_node_ref = self.current_node_ref
        while(aux_node_ref > -1):
            aux_node = self.node_dict[aux_node_ref]
            if(len(aux_node.layer_stack) > 0 and addr in aux_node.layer_stack[-1]):
                return aux_node_ref
            aux_node_ref = aux_node.parent_node_ref
        return -1
    
    def __str__(self):
        lista = [str(self.node_dict[ref]) for ref in range(0, len(self.node_dict))]
        return "\n".join(lista)

    def get_node_ref(self, semantic_scope_ref):
        '''Get the node_ref for the node that matches the specifed semantic_scope_ref.
        Moves upward in the tree to find such node'''
        aux_ref = self.current_node_ref
        while (aux_ref > -1):
            if semantic_scope_ref == self.node_dict[aux_ref].semantic_tree_ref:
                return self.node_dict[aux_ref].semantic_tree_ref
            aux_ref = self.node_dict[aux_ref].parent_node_ref
        self.__error(f"Could not find execution node for semantic ref({semantic_scope_ref})")

    
    def get_value(self, addr):
        '''Get the value for the specfied address. Move upward in the tree to find the node
        that contains the value. For each node checked, only check for the top-most layer of the
        LayerStack'''
        aux_node_ref = self.__get_node_ref_for_addr(addr)
        if aux_node_ref != -1:
            return self.node_dict[aux_node_ref].layer_stack[-1][addr]
        self.__error(f"Could not find address {addr}, current execution node: {self.current_node_ref}")
    
    def set_value(self, addr, value):
        '''Set the value for the specified address. Move upward in the tree to find if the
        specifed address is stored in another node. For each node checked, only check for the top-most
        layer of the LayerStack. If not found, add address and value to the current_node 's top-most
        layer of the LayerStack.'''
        aux_node_ref = self.__get_node_ref_for_addr(addr)
        # If address found, override in tree
        if aux_node_ref != -1:
            self.node_dict[aux_node_ref].layer_stack[-1][addr] = value
        # If address not found, add to current layer/mem
        else:
            node = self.node_dict[self.current_node_ref]
            layer_stack_top = node.layer_stack[-1]
            layer_stack_top[addr] = value
        
    def add_node(self, semantic_tree_ref, parent_ref):
        '''Add an ExecutionNode to the ExecutionTree.'''
        last_empty_ref = len(self.node_dict)
        new_node = Node(last_empty_ref, parent_ref, semantic_tree_ref)
        self.node_dict[new_node.node_ref] = new_node
        self.current_node_ref = new_node.node_ref
        self.node_path_stack.append(new_node.node_ref)
    
    def add_layer(self):
        '''Add an new layer to the current_node's LayerStack.'''
        node = self.node_dict[self.current_node_ref]
        node.add_layer()
    
    def step_back(self):
        '''Move the current_node pointer backwards in the tree.
        This is achieved by doing either: with the corresponding priority:
        a. popping the top-most layer of the layer-stack if there are more than 1 layers,
            in the current_node or
        b. popping the top value of the node_path_stack and setting the current_node to 
        the new top value of the node_path_stack.'''
        if len(self.node_dict[self.current_node_ref].layer_stack) > 1:
            self.node_dict[self.current_node_ref].layer_stack.pop()
            return
        self.node_path_stack.pop()
        self.current_node_ref = self.node_dict[self.node_path_stack[-1]].node_ref

class Node:

    def __init__(self, node_ref, parent_node_ref, semantic_tree_ref):
        self.node_ref = node_ref
        self.parent_node_ref = parent_node_ref
        self.layer_stack = [{}]
        self.semantic_tree_ref = semantic_tree_ref
    
    def __str__(self):
        return f"ref:{self.node_ref}, parent_ref:{self.parent_node_ref}, layer_stack:{self.layer_stack}"
    
    def add_layer(self):
        '''Add a new layer to the layer_stack'''
        self.layer_stack.append({})