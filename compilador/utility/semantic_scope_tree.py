class Scope:

    def __init__(self, parent_ref):
        self.ref = -1
        self.parent_ref = parent_ref
        self.vars = {}
        self.functions = {}
        self.func_name = None
        self.quad_start = None
        self.return_type = None
        self.params = []
        self.return_value = None

    def add_variable(self, name, type, addr=-1, virtual=False):
        self.vars[name] = {
            'type': type,
            'addr': addr,
            'd1': 1,
            'd2': 1,
            'v': virtual
        }

    def add_parameter(self, name):
        self.params.append(name)

    def __str__(self):
        str_vars = ""
        if self.vars:
            vars_list = [f"\t{var_key}: {self.vars[var_key]}" for var_key in self.vars]
            str_vars = "vars: " + "\n".join(vars_list)

        str_params = f"params: {self.params}\n" if self.func_name else ""
        str_functions = f"functions: {self.functions}\n" if self.functions else ""
        return f"ref: {self.ref} {self.func_name + ' : ' + str(self.return_type) + ' - ' + str(self.quad_start) if self.func_name else ''} \n" \
            f"parent_ref: {self.parent_ref}\n" + str_vars + str_params + str_functions

class SemanticScopeTree:
    def __init__(self):
        self.counter = 0
        global_scope = Scope(-1)
        self.dict = {}
        self.add_scope(global_scope)

    def add_scope(self, scope):
        scope.ref = self.counter
        self.dict[scope.ref] = scope
        self.counter = self.counter + 1

    # TODO check duplicate variable names

    def __str__(self):
        lista = [str(self.dict[ref]) for ref in range(0, self.counter)]
        return "\n".join(lista)
