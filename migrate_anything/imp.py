# this patches the imp dependency from migrate anything package to use the non deprecated importlib.util
import importlib


def new_module(name: str):
    module_spec = importlib.machinery.ModuleSpec(name, None)
    module = importlib.util.module_from_spec(module_spec)
    return module
