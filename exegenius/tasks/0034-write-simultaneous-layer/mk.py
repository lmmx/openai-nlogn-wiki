import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0034-write-simultaneous-layer.answer.md').read()
def find(start,end=None):
    i=t.index(start)
    j=t.index(end,i)+len(end) if end else i+len(start)
    return t[i:j]
def sent(start,end): return find(start,end)
D=[]
D.append(("S1.6.1",find("Direct multiplication, using","$C^4=I$")))
D.append(("S1.6.2",find("Gaussian elimination writes","each on $f=e/m$ axes.")))
D.append(("S1.6.2b",find("For selected bits","exact Gaussian dyadic operations.")))
D.append(("S1.6.3b",find("Each row addition XORs","$O(V((eK)^\\tau+1))$")))
D.append(("S1.6.4",find("Let $W$ be the network","=O(d^{\\lambda'})$")))
D.append(("S1.6.5",find("Arithmetic operations along","the width is $O(p)$.")))
D.append(("S1.6.6",find("In $\\mathcal H=H_0","to disk arrays")))
D.append(("S1.6.7",find("$Q_p$ truncates","\\sqrt2\\,2^{-p}$")))
ders=[{"step":s,"quote":q} for s,q in D]
rel=[
("phase-frames","is applied by the network of",find("On $e=mf$ axes","(phase-frames.md)")+"; its edges are products of kernels $C^{\\epsilon_h}$ along residual vectors $v_h\\in\\mathbb F_2^m$."),
("packed-bit-addition","has its row additions done by",find("Each row addition XORs","(packed-bit-addition.md).")),
("rank-recurrence","has its recurrence solved as in",find("The recurrence, solved as in","(rank-recurrence.md), is")),
("fixed-point","represents coefficients exactly as in",find("So with $\\Delta","represents every intermediate coefficient exactly.")),
]
rels=[{"prerequisite":a,"predicate":b,"quote":c} for a,b,c in rel]
syms=[]
def S(sym,name,meaning,rel,quote): syms.append({"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":quote})
S("V","stream volume","The volume of the stream in bits.","direct",find("On a stream of $V$ bits","instead of $D$ whole-array passes."))
S("K","chunk width","The number of bits in an address chunk.","count",find("On a stream of $V$ bits","instead of $D$ whole-array passes."))
S("p","fractional bits","The number of fractional bits of each coefficient.","count",find("On a stream of $V$ bits","instead of $D$ whole-array passes."))
S("W","wire count","The number of wires of the network.","count",find("Let $W$ be the network","divided by volume."))
S("F(e)","normalized time","The time divided by the stream volume.","direct",find("Let $W$ be the network","divided by volume."))
S("s","child count","The number of children, the total of residual dimensions over the network.","count","Summing residual dimensions gives exactly $s$ children, each on $f=e/m$ axes.")
json.dump({"derivations":ders,"relations":rels,"symbols":syms},open('/home/user/e2e-run/exegenius/tasks/0034-write-simultaneous-layer.answer.json','w'),indent=1)
