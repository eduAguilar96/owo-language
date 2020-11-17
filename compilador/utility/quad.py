from utility.constants import *

class Quad:

    def __init__(self, opcode, left=None, right=None, target=None):
        self.opcode = opcode
        self.left = left
        self.right = right
        self.target = target

    def __str__(self):
        return f" Quad {self.opcode}"\
            f"{(len('Operations.GREATERTHANOREQUAL')-len(str(self.opcode))+1)*' '}"\
            f"{self.left} {self.right} {self.target}"
