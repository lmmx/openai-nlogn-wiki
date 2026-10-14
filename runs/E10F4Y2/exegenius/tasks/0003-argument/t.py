import sys, importlib
from lib import *
mod, fn = sys.argv[1], sys.argv[2]
n = getattr(importlib.import_module(mod), fn)()
assign_ids(n)
d = n.to_dict()
print("ok", len(list(walk(n))))
