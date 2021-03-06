from importlib import reload
from types import ModuleType


def rreload(module):
    """Recursively reload modules."""
    reload(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            rreload(attribute)


def reload_all():
    import demo
    rreload(demo)
