import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'<cite[^>]*>.*?</cite>','',t,flags=re.S)
t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S)
t=re.sub(r'\$.*?\$','',t,flags=re.S)
print(len(t.split()), len(re.findall(r"[A-Za-z0-9]+",t)))
t2=re.sub(r'\]\([^)]*\)',']',t)
print(len(t2.split()), len(re.findall(r"[A-Za-z0-9]+",t2)))
