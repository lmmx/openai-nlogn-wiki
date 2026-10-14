import json, sys
sys.path.insert(0, '.')
from lib import *
Q = quote
for f in ['build1.py','build2.py','build3.py','build4.py','build5.py']:
    exec(open(f).read())
probs = validate(ROOT)
for p in probs: print("PROBLEM:", p)
json.dump({"root": ROOT}, open(BASE + "/exegenius/tasks/0003-argument.answer.json", "w"), ensure_ascii=False, indent=1)
print("written; problems:", len(probs))
