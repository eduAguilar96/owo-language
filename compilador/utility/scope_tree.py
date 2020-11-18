class Scope:

    def __init__(self, parent_ref):
        self.ref = -1
        self.parent_ref = parent_ref
        self.vars = {}
        self.functions = {}
        self.func_name = None

    def set_variable(self, name, type):
        self.vars[name] = {
            'type': type
        }

    def __str__(self):
        str_vars = f"vars: {self.vars}\n" if self.vars else ""
        str_functions = f"functions: {self.functions}\n" if self.functions else ""
        return f"ref: {self.ref} {self.func_name if self.func_name else ''} \n" \
            f"parent_ref: {self.parent_ref}\n" + str_vars + str_functions

class ScopeTree:
    def __init__(self):
        self.counter = 0
        global_scope = Scope(-1)
        self.dict = {}
        self.add_scope(global_scope)

    def add_scope(self, scope):
        scope.ref = self.counter
        self.dict[scope.ref] = scope
        self.counter = self.counter + 1

    def __str__(self):
        lista = [str(self.dict[ref]) for ref in range(0, self.counter)]
        return "\n".join(lista)
