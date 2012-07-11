import modules

submodules = {
    'objdump': None
}

class Module(modules.Module):
    module_name = 'import_asm'

def setup(uv):
    from modules.import_asm import objdump
    submodules['objdump'] = objdump.Module()
    submodules['objdump'].register(uv)
