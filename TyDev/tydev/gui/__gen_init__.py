import importlib
import os

with open("__init__.py", "w") as f:
    for n in os.listdir():
        if n.endswith(".py") and not n.startswith("__"):
            m = importlib.import_module(n[:-3])
            if hasattr(m, n[:-3].capitalize()):
                f.write(f"from .{n[:-3]} import {n[:-3].capitalize()}\n")
            else:
                f.write(f"# from .{n[:-3]} import {n[:-3].capitalize()}  # Class not found\n")
