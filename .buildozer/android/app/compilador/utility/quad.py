from compilador.utility.constants import *

class Quad:

    def __init__(self, op_code, left=None, right=None, target=None):
        self.op_code = op_code
        self.left = left
        self.right = right
        self.target = target

    def __str__(self):
        spacing = 25
        return f" Quad {self.op_code.value} {(spacing-len(str(self.op_code.value)))*' '}"\
            f" {self.left}{(spacing-len(str(self.left)))*' '}"\
            f" {self.right}{(spacing-len(str(self.right)))*' '}"\
            f" {self.target}"
