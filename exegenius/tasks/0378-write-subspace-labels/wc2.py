import re,sys
t=open(sys.argv[1]).read()
tot=0
for para in t.split('\n\n'):
    t1=re.sub(r'<cite[^>]*>.*?</cite>','',para,flags=re.S)
    t2=re.sub(r'\$\$.*?\$\$',' ',t1,flags=re.S)
    t3=re.sub(r'\$.*?\$','',t2,flags=re.S)
    n=len(t3.split()); tot+=n
    print(n, para[:60].replace('\n',' '))
print('total',tot)
