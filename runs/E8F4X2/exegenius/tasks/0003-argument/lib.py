import json, re
BASE="/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E8F4X2"
TEXT=open(BASE+"/sources/paper.tex",encoding="utf-8").read()

def ev(q):
    return {"source":"paper","quote":q}

def inf(id, claim, quote, frm=(), salient=None, deferred=False, page=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(quote)}
    if frm: n["from"]=list(frm)
    if salient: n["salient"]=salient
    if deferred: n["deferred"]=True
    if page: n["page"]=page
    return n

def mot(text, source, quote=None):
    m={"text":text,"source":source}
    if quote: m["quote"]=ev(quote)
    return m

def show(id, claim, method, motivation, children, page=None, frm=(), adds=(), salient=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":motivation,"children":children}
    if page: n["page"]=page
    if frm: n["from"]=list(frm)
    if adds: n["adds"]=[{"symbol":a[0],"name":a[1],"meaning":a[2],"relation":a[3]} for a in adds]
    if salient: n["salient"]=salient
    return n

def walk(n):
    yield n
    for c in n.get("children",[]):
        yield from walk(c)

def check(root):
    ok=True
    pos=-1
    for n in walk(root):
        qs=[]
        if n["intention"]=="infer":
            qs.append(("quote",n["quote"]["quote"]))
        m=n.get("motivation")
        if m and m.get("quote"):
            qs.append(("mot",m["quote"]["quote"]))
        for kind,q in qs:
            c=TEXT.count(q)
            if c==0:
                print("MISSING",n["id"],kind,repr(q)); ok=False; continue
            if c>1:
                print("DUP",c,n["id"],kind,repr(q[:70]))
        if n["intention"]=="infer" and not n.get("deferred"):
            q=n["quote"]["quote"]
            i=TEXT.find(q,pos+1)
            if i<0:
                j=TEXT.find(q)
                print("ORDER",n["id"],"first at",j,"prev",pos, repr(q[:60])); ok=False
            else:
                pos=i
    return ok
