import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S)
t=re.sub(r'\$[^$]*\$','',t)
t=re.sub(r'<cite[^>]*>.*?</cite>','',t,flags=re.S)
t=re.sub(r'\]\([^)]*\)',']',t)
t=re.sub(r'[#*\[\]]',' ',t)
w=[x for x in t.split() if re.search(r'\w',x)]
print(len(w))
