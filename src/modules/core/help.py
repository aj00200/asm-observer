import modules.core

class Module(modules.core.Module):
    commands = ['help']

    def cmd_help(self, main, params = None):
        '''SYNTAX: help [command/module]
          Shows help information for a command or module.
        '''
        print('Commands: %s' % ', '.join(main.commands))
