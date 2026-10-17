import os
import importlib.util as importlib
from os import path

__examples = {}

__example_path = path.join(path.dirname(__file__), "examples")
print("Loading examples from:", __example_path)

for example in os.listdir(__example_path):
    name = example[:-3]
    path_ = path.join(__example_path, example)
    if not path.isfile(path_) or not path_.endswith(".py"):
        continue

    try:
        assert (spec := importlib.spec_from_file_location(name, path_))
        module = importlib.module_from_spec(spec)
        assert (loader := spec.loader)
        loader.exec_module(module)

        __examples[name] = module.mcp
        print("Loaded example:", name)
    except ImportError as exc:
        print(f"Failed to load example {name}: {exc}")
        continue

def __getattr__(name: str, /):
    if name == "__all__":
        return __examples.keys()
    if name in __examples:
        return __examples[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
