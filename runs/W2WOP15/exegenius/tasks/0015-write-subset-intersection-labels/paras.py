import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'\$\$.*?\$\$',' ',t,flags=re.S)
t=re.sub(r'<cite.*?</cite>',' ',t,flags=re.S)
t=re.sub(r'\$.*?\$',' ',t,flags=re.S)
t=re.sub(r'\]\([^)]*\)',']',t)
for p in t.split('\n'):
    if p.strip(): print(len(p.split()), '|', ' '.join(p.split())); print()
