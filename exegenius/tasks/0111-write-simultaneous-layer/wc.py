import re
t=open('/home/user/e2e-run/exegenius/tasks/0111-write-simultaneous-layer.answer.md').read()
tot=0;tot2=0
for para in t.split('\n\n'):
    u=re.sub(r'<cite.*?</cite>','',para,flags=re.S)
    u=re.sub(r'\$\$.*?\$\$','',u,flags=re.S)
    u=re.sub(r'\$.*?\$','',u)
    w=u.split(); w2=[x for x in w if re.search(r'[A-Za-z]',x)]
    print(len(w),len(w2), para[:40]);tot+=len(w);tot2+=len(w2)
print(tot,tot2)
