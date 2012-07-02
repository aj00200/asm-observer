import modules.core

class Module(modules.core.Module):
    commands = ['quit']

    def cmd_quit(self, main, params = None):
        '''SYNTAX: quit
          Shutdown ASM Observer
        '''
        main.running = False
        print(' [*] Shutting down...')
        print('     Goodbye :)')
