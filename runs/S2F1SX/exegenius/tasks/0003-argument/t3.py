import json
from part3 import layout, ring_conv
root={"id":"X","intention":"show","claim":"x","method":"m","motivation":{"text":"t","source":"recoverable"},"children":[layout, ring_conv]}
s=json.dumps(root)
assert '\r' not in s and '\x0c' not in s and '\t' not in s and '\x08' not in s
json.dump({"root": root}, open('t3.json','w'))
