import json,re
p='/home/user/e2e-run/exegenius/tasks/0310-write-simultaneous-layer.answer.md'
t=open('/home/user/e2e-run/exegenius/tasks/0310-write-simultaneous-layer/prev.md').read()
def rep(a,b):
    global t
    assert t.count(a)==1,a
    t=t.replace(a,b)
rep("selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\\lambda'}),$ $\\lambda'<1,$ instead of $D$ passes ($D$ counts chunks, not the source group of the shear page).",
"selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\\lambda'}),$ $\\lambda'<1,$ instead of $D$ passes; here $D$ is the number of selected address chunks, not the second chunk value of [Fast address-chunk interchange](address-interchange.md), and $D$ is not the source group of [Matrix shear by triangular factorization](matrix-shear.md).")
rep("z(x).$ Phases","z(x).$ Here $z$ is an array, not an address suffix as on [Fast address-chunk interchange](address-interchange.md), and $z$ is not a binary vector as on [Binary phase frames](phase-frames.md). Phases")
rep(" acts on an array $z$ (not a suffix) by"," acts on an array $z$ by")
rep("selected axes ($e$ counts axes, not digits of a chunk) has","selected axes ($e$ is the number of selected axes, not the number of digits in a chunk as on [Fast address-chunk interchange](address-interchange.md)) has")
rep("has absolute row sum one <cite data-source=\"paper\">absolute row sum one.</cite> Hence $\\mathcal H$ maps disk arrays to disk arrays.","has absolute row sum one. Hence $\\mathcal H$ maps disk arrays to disk arrays <cite data-source=\"paper\">absolute row sum one. Thus $\\mathcal H$ maps disk arrays to disk</cite>.")
rep("($E$ below is an operation bound, not a tensor factor)","($E$ below is an operation bound, not the first tensor factor of [Tensor products of subspaces](tensor-product-of-spaces.md); $E$ is likewise not the edge residual of the phase frames page)")
open(p,'w').write(t)
c=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
c=re.sub(r'\$\$.*?\$\$','',c,flags=re.S)
c=re.sub(r'\$.*?\$','',c)
print(len(c.split()))
def span(a,b):
    i=t.index(a); j=t.index(b,i)+len(b); return t[i:j]
der=[
("S1.6.1",span("With $\\mathsf S=\\operatorname{diag}(1,i),$","$C^4=I$")),
("S1.6.2",span("Apply $\\mathcal P_\\Gamma^{-1},$ then","with $Z=\\operatorname{diag}(1,-1).$")),
("S1.6.2b",span("With $x_1,\\dots,x_D$ the selected bits","leaving $C^{\\otimes D}.$")),
("S1.6.3b",span("Elimination writes $\\Gamma$","$O(V((eK)^\\tau+1))$")),
("S1.6.4",span("Rows go to the $W$ wire roles","$O(d^{\\lambda'}).$")),
("S1.6.5",span("Let $\\chi(e)$ bound","every intermediate coefficient exactly")),
("S1.6.6",span("Absolute row sums multiply","disk arrays to disk arrays")),
("S1.6.7",span("Truncation toward zero cannot","\\sqrt2\\,2^{-p}$")),
]
for s_,q in der:
    assert '<cite' not in q,s_
    assert q in t,s_
sym=[]
def add(sy,name,meaning,rel,q):
    assert q in t,q
    sym.append(dict(symbol=sy,name=name,meaning=meaning,relation=rel,quote=q))
first=t.split('\n')[0]
add("D","selected chunk count","The number of selected address chunks.","count",first)
q=span("A group of $e=mf$ selected axes","in $\\mathbb F_2^m.$")
add("e","selected axis count","The number of selected axes in a group.","count",q)
q=span("where the diagonal operator $\\mathcal S_D$ acts","by $(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x).$")
add("z","array","An array acted on by the diagonal operator.","direct",q)
add("\\mathcal S_D","diagonal phase operator","The diagonal operator multiplying the value at address x by i to the sum of the selected bits.","direct",q)
q=span("Let $\\Gamma$ be an invertible","an address permutation.")
add("\\Gamma","basis-change matrix","An invertible F_2 matrix whose first columns are the residual basis vectors.","direct",q)
add("\\mathcal P_\\Gamma","address permutation","The address permutation moving the value at x to Gamma x.","direct",q)
q=span("with residual basis vectors $v_\\xi$ indexed by $\\xi,$","shifting a column by $v.$")
add("\\xi","residual basis index","The index of the residual basis vectors.","direct",q)
add("\\eta_\\xi","edge sign","The sign plus or minus one of the xi-th residual basis vector's exponent.","direct",q)
q=span("$\\mathbf 1_\\xi$ the","standard basis vector")
add("\\mathbf 1_\\xi","standard basis vector","The xi-th standard basis vector.","direct",q)
q=span("So the first $q_0=","row index of range at least $W^{\\lceil\\log_md\\rceil}.$")
add("q_0","individual chunk count","The number of leading chunks given individual C kernels.","count",q)
q=span("Let $\\chi(e)$ bound","(","") if False else span("Let $\\chi(e)$ bound the operations on a chain from an input to an intermediate coefficient","coefficient")
add("\\chi","operation-chain bound","A bound on the arithmetic operations on a chain from an input to an intermediate coefficient.","count",q)
q=span("($E$ below is an operation bound,","edge residual of the phase frames page)")
add("E","invocation operation bound","The bound on arithmetic operations in one invocation of the network.","count",q)
q=span("With $\\Psi=s+E,$","for any bound $\\varphi\\ge1,$")
add("\\Psi","level growth factor","The sum s plus E, the factor by which each internal level multiplies the chain bound.","direct",q)
add("\\varphi","chain bound","Any bound on a chain's operation count that is at least one.","direct",q)
q=span("With $\\vartheta=\\min","not a digit count)")
add("\\vartheta","exponent","The least positive exponent j with m to the j at least Psi.","direct",q)
q=span("with $C_0=128m\\Psi^2,$","\\vartheta+3\\}.$")
add("C_0","guard constant","The constant 128 m Psi squared in the reserved extra bits Delta.","direct",q)
rel=[
("phase-frames","is computed by",span("$C^{\\otimes e}$ is computed by","smaller calls.")),
("rank-recurrence","obeys the recursion of","The layer obeys the recursion of [Recursive power saving](rank-recurrence.md)."),
("packed-bit-addition","XORs selected bits by",span("[Packed selected-bit addition](packed-bit-addition.md) XORs","exceptional addresses.")),
("fixed-point","is evaluated in","The layer is evaluated in [Fixed-point Gaussian dyadic records](fixed-point.md)."),
]
for pr,pd,q in rel: assert q in t,q
J=dict(symbols=sym,relations=[dict(prerequisite=a,predicate=b,quote=c) for a,b,c in rel],derivations=[dict(step=a,quote=b) for a,b in der])
json.dump(J,open('/home/user/e2e-run/exegenius/tasks/0310-write-simultaneous-layer.answer.json','w'),indent=1)
