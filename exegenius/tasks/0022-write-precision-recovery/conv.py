import re
s=open('0022-write-precision-recovery/page.src').read()
# protect cites
parts=re.split(r'(<cite.*?</cite>)',s)
out=[]
for x in parts:
    if x.startswith('<cite'): out.append(x); continue
    x=re.sub(r'\$[^$]+\$[,.;:]+',lambda m: m.group(0)[:m.group(0).index('$',1)] + m.group(0)[m.group(0).index('$',1)+1:].strip() and '' or '',x) if False else x
    # proper sequential: tokenise
    res='';i=0
    for m in re.finditer(r'\$[^$]+\$([,.;:]*)',x):
        res+=x[i:m.start()]
        full=m.group(0); punc=m.group(1)
        body=full[:len(full)-len(punc)-1]
        res+=body+punc+'$'
        i=m.end()
    res+=x[i:]
    out.append(res)
t=''.join(out)
open('0022-write-precision-recovery.answer.md','w').write(t)
u=re.sub(r'<cite.*?</cite>','',t)
u=re.sub(r'\$[^$]*\$','',u)
u=re.sub(r'\]\([^)]*\)',']',u)
print(len(u.split()))
