import modules

submodules = {
    'help': None
}

class Module(modules.Module):
    module_name = 'core'

def setup(uv):
    from modules.core import help
    submodules['help'] = help.Module()
    submodules['help'].register(uv)
        
    from modules.core import sys
    submodules['sys'] = sys.Module()
    submodules['sys'].register(uv)
