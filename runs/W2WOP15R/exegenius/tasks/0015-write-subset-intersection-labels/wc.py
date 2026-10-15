import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S)
t=re.sub(r'\$.*?\$','',t,flags=re.S)
t=re.sub(r'<cite[^>]*>.*?</cite>','',t,flags=re.S)
t=re.sub(r'\]\([^)]*\)',']',t)
w=[x for x in re.split(r'\s+',t) if re.search(r'[A-Za-z0-9]',x)]
print(len(w))
