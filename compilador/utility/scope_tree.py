class Scope:

    def __init__(self, parent_ref):
        self.ref = -1
        self.parent_ref = parent_ref
        self.vars = {}

    def set_variable(self, name, type):
        self.vars[name] = {
            'type': type
        }

    def __str__(self):
        return \
        f"ref: {self.ref}\n" \
        f"parent_ref: {self.parent_ref}\n" \
        f"vars: {self.vars}"

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
        [print(self.dict[ref]) for ref in range(0, self.counter)]
