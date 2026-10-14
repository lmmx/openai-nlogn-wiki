import json
from part2 import S2
json.dump({"root": S2}, open('t2.json','w'))
s=json.dumps(S2)
assert '\r' not in s and '\x0c' not in s and '\t' not in s
