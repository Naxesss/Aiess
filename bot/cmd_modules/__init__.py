from os.path import dirname, basename, isfile, join
import glob

# This specifies to find all modules when using the * wildcard operator in imports.
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]