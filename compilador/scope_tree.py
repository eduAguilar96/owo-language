class ScopeTree:

    def __init__(self, global_context_counter_list, parent_ref):
        self.ref = global_context_counter_list[0]
        global_context_counter_list[0] += 1
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
