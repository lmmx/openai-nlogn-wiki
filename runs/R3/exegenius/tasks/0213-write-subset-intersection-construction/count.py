import re
t = open('/home/user/lmmx/openai-nlogn-wiki/runs/R3/exegenius/tasks/0213-write-subset-intersection-construction.answer.md', encoding='utf-8').read()
t = re.sub(r'<cite[^>]*>.*?</cite>', '', t, flags=re.S)
t = re.sub(r'\$\$.*?\$\$', '', t, flags=re.S)
t = re.sub(r'\$[^$]*\$', '', t)
t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
print(len(re.findall(r'\S+', t)))
