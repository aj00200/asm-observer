
class Module():
    module_name = 'default_module'
    commands = []

    def register(self, uv):
        '''Register all commands with the main program.'''
        for command in self.commands:
            uv.register_command('%s.%s' % (self.module_name, command),
                                getattr(self, 'cmd_%s' % command))
