import os
import importlib.util

def load_plugins(bot):
    for filename in os.listdir("plugins"):
        if filename.endswith(".py"):
            path = f"plugins/{filename}"
            name = filename[:-3]
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "register"):
                module.register(bot)
