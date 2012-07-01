import modules

submodules = {
    'workspace': None
}

class Module(modules.Module):
    module_name = 'workspace'

def setup(main):
    from modules.workspace import workspace
    submodules['workspace'] = workspace.Module()
    submodules['workspace'].register(main)
        
