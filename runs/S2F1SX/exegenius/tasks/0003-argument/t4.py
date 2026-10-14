import json
from part4 import resampling, chirp, cancel
root={"id":"X","intention":"show","claim":"x","method":"m","motivation":{"text":"t","source":"recoverable"},"children":[resampling, chirp, cancel]}
s=json.dumps(root)
assert '\r' not in s and '\x0c' not in s and '\t' not in s and '\x08' not in s
json.dump({"root": root}, open('t4.json','w'))
