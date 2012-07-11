
class ASM():
    '''Store ASM code in an easy-to-access object.'''

    def __init__(self):
        self.labels = {}
        self.code = {}

    def add_line(self, address, line):
        self.code[address] = line

class Line():
    def __init__(self, address, bytestring, opcode, parameters, comment=None):
        '''Create an object to represent a line of ASM code.
           `address`: an integer representing the address of this line
           `bytestring`: a bytes object with the disassembled data
           `opcode`: a string with the ASM op code
           `parameters`: a tuple containing the parameters to the opcode
           `comment`: extra data from the disassembler
          '''

        self.address = address
        self.bytes = bytestring
        self.opcode = opcode
        self.parameters = parameters
        self.comment = comment

        # Create an empty list where users can add their own comments
        self.usercomments = []
