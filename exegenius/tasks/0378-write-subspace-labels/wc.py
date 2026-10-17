import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'<cite[^>]*>.*?</cite>','',t,flags=re.S)
t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S)
t=re.sub(r'\$.*?\$','',t,flags=re.S)
t=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',t)
w=re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*",t)
print(len(w))
