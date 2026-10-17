import re
t=open('/home/user/e2e-run/exegenius/tasks/0108-write-address-interchange.answer.md').read()
t=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
t=re.sub(r'\$.*?\$','',t)
t=re.sub(r'\(([^)]*)\.md\)','',t)
print(len(t.split()))
