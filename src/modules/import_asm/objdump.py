import re
import libs.asm
import modules.import_asm

class Module(modules.import_asm.Module):
    commands = ['objdump']

    def cmd_objdump(self, main, params = None):
        '''SYNTAX: objdump file
          Import objdump output which is stored in `file`
        '''
        if not params:
            print('Need a filename')
            return

        asm = libs.asm.ASM()

        # Open the objdump file
        f = open(params)
        for each in range(0, 4):
            f.readline() # Waste 4 lines

        c = f.read()     # Read remaining file contents
        f.close()

        sections = {}
        section = ''

        # Parse contents
        for line in c.split('\n'):
            if line == '': # Blank line
                pass

            elif line.startswith('Disassembly of section .'):
                section = '.' + line

            elif re.match('\d+ <.*>:', line):
                pass # TODO: Deal with labels

            elif line.startswith('  '):
                # Default values
                parameters = ()
                comment = None
                opcode = None

                # Parse the line
                stripped = re.sub('[ ]+', ' ', line[2:])
                parts = stripped.split('\t')
                
                # Get data from line
                address = int(parts[0][0:-1], 16)
                bytestring = bytes()

                for byte in parts[1].split():
                    bytestring += bytes(chr(int(byte, 16)), 'charmap')

                if len(parts) > 2:
                    subparts = parts[2].split()
                    opcode = subparts[0]

                    if len(subparts) > 1:
                        parameters = tuple(subparts[1].split(','))

                    if len(subparts) > 2:
                        comment = subparts[2]

                # Add Line object to ASM object
                l = libs.asm.Line(address, bytes, opcode, parameters, comment)
                asm.add_line(address, l)
