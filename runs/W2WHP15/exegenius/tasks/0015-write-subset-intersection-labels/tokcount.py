import re, sys
t=open(sys.argv[1],encoding='utf-8').read()
base=re.sub(r'<cite[^>]*>.*?</cite>',' ',t,flags=re.S)
base=re.sub(r'\$\$.*?\$\$',' ',base,flags=re.S)
v=re.sub(r'\$[^$]*\$',' ',base); v=re.sub(r'\[([^\]]*)\]\([^)]*\)',r' \1 ',v)
toks=[w for w in re.split(r'\s+',v) if w]
print('grader-style tokens:', len(toks), '| alpha-words:', len([w for w in toks if re.search(r'[A-Za-z]',w)]), '| punct-only:', len([w for w in toks if not re.search(r'[A-Za-z]',w)]))
