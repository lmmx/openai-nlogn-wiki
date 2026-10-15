import re, sys
text = open(sys.argv[1], encoding='utf-8').read()
t = re.sub(r'<cite[^>]*>.*?</cite>', ' ', text, flags=re.S)
t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.S)
t = re.sub(r'\$[^$]*\$', ' ', t)
t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r' \1 ', t)
t = re.sub(r'^##.*$', ' ', t, flags=re.M)
words = [w for w in re.split(r'\s+', t) if re.search(r'[A-Za-z]', w)]
print(len(words))
