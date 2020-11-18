from utility.constants import *

class Quad:

    def __init__(self, opcode, left=None, right=None, target=None):
        self.opcode = opcode
        self.left = left
        self.right = right
        self.target = target

    def __str__(self):
        spacing = 25
        return f" Quad {self.opcode} {(spacing-len(str(self.opcode)))*' '}"\
            f" {self.left}{(spacing-len(str(self.left)))*' '}"\
            f" {self.right}{(spacing-len(str(self.right)))*' '}"\
            f" {self.target}{(spacing-len(str(self.target)))*' '}"
