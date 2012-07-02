#! /usr/bin/env python3
import sys

class Main():
    '''Contains the setup code and the input loop. This class stores all
    the session data, workspaces, etc. and is passed around to modules.
    This class also parses the command line arguments.
    '''

    params = {
        'verbose': False
    }
    modules = {}
    commands = {}
    environment = {}
    autoload_modules = ['core', 'workspace']

    workspace = ''
    workspaces = {}

    running = True

    def __init__(self):
        # Check CLI parameters
        if '-v' in sys.argv:
            self.params['verbose'] = 1
        if '-v5' in sys.argv:
            self.params['verbose'] = 5

        # Preform additional setup
        self.load_modules(self.autoload_modules)
        self.check_optional_modules()

    def check_optional_modules(self):
        '''Check the Python install to see which non-default modules are
        installed and store the information so modules can just check it
        here instead of running their own tests.
        '''
        try:
            import Crypto
            self.environment['pycrypto'] = Crypto.version_info
        except ImportError as err:
            self.environment['pycrypto'] = False
        
    def load_modules(self, module):
        '''Load a module from the modules directory, call the setup
        method on it. If a list is given, load all modules in the list.
        '''
        if isinstance(module, list):
            for mod in module:
                self.load_modules(mod)
        else:
            print(' [*] Loading module: %s' % module)
            self.modules[module] = getattr(__import__('modules.%s' % module),
                                           module)
            self.modules[module].setup(self)
                
    def register_command(self, name, pointer):
        '''Register a command. `name` should be two parts, the module
        name followed by a period and then the command name. `pointer`
        should be a refrerence to the method for that command.
        '''
        self.commands[name] = pointer

    def call_module(self, name, params):
        if name in self.commands:
                self.commands[name](self, params)

    def input_loop(self):
        '''Get input from the user and run commands with it.'''
        while self.running:
            params = None
            inp = input('asmo\x1B[;31m$\x1B[m ').split(' ', 1)

            if len(inp) > 1:
                params = inp[1]

            self.call_module(inp[0],params)

if __name__ == '__main__':
    print('''
                           <<<   \x1B[;32ASM Observer\x1B[m   >>>
    ''')

    main = Main()
    print('    ')
    main.input_loop()
