import json
t=open('/home/user/e2e-run/exegenius/tasks/0034-write-simultaneous-layer.answer.md').read()
def find(start,end=None):
    i=t.index(start)
    j=t.index(end,i)+len(end) if end else i+len(start)
    return t[i:j]
D=[
("S1.6.1",find("Direct multiplication, using","C^4=I$")),
("S1.6.2",find("So apply $\\mathcal P_M^{-1}$","each on $f=e/m$ axes.")),
("S1.6.2b",find("For selected address bits","exact Gaussian dyadic operations.")),
("S1.6.3b",find("Gaussian elimination writes","$O(V((eK)^\\tau+1))$")),
("S1.6.4",find("Let $W$ be the network","=O(d^{\\lambda'})$")),
("S1.6.5",find("Chains satisfy","the width is $O(p).$")),
("S1.6.6",find("Rows of $H_0$","to disk arrays")),
("S1.6.7",find("$Q_p$ truncates","\\sqrt2\\,2^{-p}$")),
]
ders=[{"step":s,"quote":q} for s,q in D]
rels=[
{"prerequisite":"phase-frames","predicate":"is applied by the network of","quote":find("On $e=mf$ axes","\\pm1.$")},
{"prerequisite":"packed-bit-addition","predicate":"has its row additions done by","quote":find("Gaussian elimination writes","(packed-bit-addition.md).")},
{"prerequisite":"rank-recurrence","predicate":"has its recurrence solved as in","quote":find("The recurrence, solved as in","\\beta=\\frac12.$")},
{"prerequisite":"fixed-point","predicate":"represents coefficients exactly as in","quote":find("So with $\\Delta","represents every intermediate coefficient exactly.")},
]
S1=find("On a stream of $V$ bits","instead of $D$ whole-array passes.")
S2=find("On $e=mf$ axes","\\pm1.$")
S3=find("Let $W$ be the network","divided by volume.")
syms=[]
def S(sym,name,meaning,rel,quote): syms.append({"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":quote})
S("V","stream volume","The number of bits of the stream.","count",S1)
S("K","chunk width","The number of bits in an address chunk.","count",S1)
S("p","fractional bits","The number of fractional bits of each coefficient.","count",S1)
S("D","selected chunks","The number of address chunks whose selected bit is butterflied.","count",S1)
S("d","chunk bound","The maximum number of chunks, D at most d.","direct",S1)
S("e","axis count","The number of axes in a group handled by the network.","count",S2)
S("m","slot count","The number of slots into which the e axes are arranged.","count",S2)
S("f","slot width","The number of bits in each slot.","count",S2)
S("s","child count","The number of children, the total of residual dimensions over the network.","count","Summing residual dimensions gives exactly $s$ children, each on $f=e/m$ axes.")
S("W","wire count","The number of wires of the network.","count",S3)
S("F(e)","normalized time","The time divided by the stream volume.","direct",S3)
json.dump({"derivations":ders,"relations":rels,"symbols":syms},open('/home/user/e2e-run/exegenius/tasks/0034-write-simultaneous-layer.answer.json','w'),indent=1)
