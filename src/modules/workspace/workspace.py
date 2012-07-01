import modules.workspace

class Module(modules.workspace.Module):
    commands = ['new', 'list', 'switch']

    def cmd_new(self, main, params = None):
        '''SYNTAX: workspace.new [name]
          Create a new workspace. You may choose to set a name.
        '''
        if params:
            name = params
        else:
            name = 'Workspace %s' % len(main.workspaces)

        main.workspaces[name] = Workspace()
        main.workspace = name

    def cmd_list(self, main, params = None):
        '''SYNTAX: workspace.list
          Display a list of all workspaces.
        '''
        for workspace in main.workspaces:
            if main.workspace == workspace: # Current workspace
                print('> %s' % workspace)
            else:                         # Other workspace
                print('  %s' % workspace)

    def cmd_switch(self, mail, params = None):
        '''SYNTAX: workspace.switch [workspace name]
          Switch to an already running workspace.
        '''
        if params in main.workspaces:
            main.workspace = params
        else:
            print('That workspace does not exist.')

class Workspace():
    '''A class for holding variables for a single session. Workspaces
    can be switched on the fly by the user.
    '''
    def __init__(self):
        self.vars = {}
