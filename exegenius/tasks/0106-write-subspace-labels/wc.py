import re,sys
t=open(sys.argv[1]).read()
t=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S)
t=re.sub(r'\$.*?\$','',t,flags=re.S)
t=re.sub(r'\]\(.*?\)','',t)
print(len(t.split()))
for p in t.split('\n\n'):
    print(len(p.split()), p[:60].replace('\n',' '))
