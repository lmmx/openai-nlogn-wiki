import re,sys
body=open('../0213-write-subset-intersection-construction.answer.md',encoding='utf-8').read()
src=open('/home/user/lmmx/openai-nlogn-wiki/runs/R2/sources/paper.tex',encoding='utf-8').read()
norm=lambda s: re.sub(r'\s+',' ',s)
S=norm(src)
for m in re.finditer(r'<cite data-source="(\w+)">(.*?)</cite>',body,re.S):
    t=norm(m.group(2)).strip()
    print('FOUND' if t in S else 'MISSING', '|', t)
prose=re.sub(r'\$\$.*?\$\$|\$[^$]*\$','',body,flags=re.S)
prose=re.sub(r'<cite[^>]*>.*?</cite>','',prose,flags=re.S)
prose=re.sub(r'\[([^\]]*)\]\([^)]*\)',r'\1',prose)
print('words:',len(prose.split()))
