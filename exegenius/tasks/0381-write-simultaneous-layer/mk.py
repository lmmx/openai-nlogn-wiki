import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0381-write-simultaneous-layer.answer.md').read()
def span(a,b):
    i=t.index(a); j=t.index(b,i)+len(b)
    return t[i:j]
der=[
("S1.6.1",span("the [Two-point kernel C]","$C^4=I$")),
("S1.6.2",span("Apply $\\mathcal P_\\Gamma^{-1}$ to every column","$Z=\\operatorname{diag}(1,-1)$.")),
("S1.6.2b",span("Applying the identity on every selected bit gives","z(x)$.")),
("S1.6.3b",span("As their number is fixed","axis chunks cost")),
("S1.6.4",span("Writing $D-q_0$ in base $m$","\\sigma+\\beta(1-\\sigma)$.")),
("S1.6.5",span("A value after $\\ell$ operations","represents every intermediate coefficient exactly")),
("S1.6.6",span("A row of $\\mathcal H$ consists","to disk arrays")),
("S1.6.7",span("Truncation $Q_p$ toward zero","less than $2^{-p}$")),
]
def sent(a,b):
    return span(a,b)
rel=[
("phase-frames","is handled by the network of",span("The group is handled by the network of","smaller calls.")),
("rank-recurrence","follows the recursion of",span("The cost of the layer follows the recursion of","not $m$.")),
("packed-bit-addition","performs each row addition by",span("The layer performs each row addition by","exceptional addresses.")),
("fixed-point","is evaluated in",span("The layer is evaluated in","(fixed-point.md).")),
]
sy=[
("D","selected chunk count","The number of selected address chunks (axes), at most d.","count",span("one bit of each of $D\\le d$ selected address chunks","K$ bits")),
("e","group axis count","The number of selected axes in a group, e=mf.","count",span("Take $e=mf$ selected axes","chunk digits as on")),
("f","slot width","The number of axes in each of the m slots of a group.","count",span("split into $m$ slots of $f$ axes","axes.")),
("\\Gamma","basis-change matrix","An invertible matrix over F_2 whose first columns are the residual basis vectors.","direct",span("Take an invertible $\\mathbb F_2$-matrix $\\Gamma$","$v_\\xi$,")),
("\\xi","residual index","The index of a residual basis vector of an edge.","direct",span("over residual basis vectors $v_\\xi$","modulo 2.")),
("\\mathcal P_\\Gamma","address permutation","The address permutation sending x to Gamma x.","direct",span("and the address permutation $\\mathcal P_\\Gamma:x\\mapsto\\Gamma x$.","")) if False else ("\\mathcal P_\\Gamma","address permutation","The address permutation sending x to Gamma x.","direct","Take an invertible $\\mathbb F_2$-matrix $\\Gamma$ whose first columns are the $v_\\xi$, and the address permutation $\\mathcal P_\\Gamma:x\\mapsto\\Gamma x$."),
("\\mathcal S_D","phase diagonal","The diagonal operator multiplying the value at x by i to the power x_1+...+x_D.","direct",span("where the diagonal operator $\\mathcal S_D$","z(x)$.")),
("q_0","individual chunk count","The number of leading chunks to which C is applied individually and whose bits form the row index.","count",span("the first $q_0=","chunks get individual $C$ kernels")),
("\\Xi","time per unit volume","The time for e axes divided by their stream volume, as a function of e.","direct","Let $\\Xi(e)$ be the time for the $e$ axes divided by their stream volume."),
("\\chi","chain operation bound","A bound on the number of arithmetic operations on a chain from an input coefficient to an intermediate one.","count","Let $\\chi(e)$ bound the operations on a chain from an input coefficient to an intermediate one."),
("E","operation bound","A bound on the operations of one network invocation, 64(W+m+1)^3.","count",span("below $E=64(W+m+1)^3$","operation bound here)")),
("\\Psi","chain growth factor","The sum s+E, the factor by which each recursion level multiplies the chain bound.","direct","With $\\Psi=s+E$, $s\\varphi+E\\le\\Psi\\varphi$ for $\\varphi\\ge1$, so each of at most $\\lceil\\log_md\\rceil$ levels multiplies the bound by at most $\\Psi$"),
("\\vartheta","exponent of m","The least j at least 1 with m^j at least Psi.","direct",span("where $\\vartheta=\\min","\\ge\\Psi\\}$")),
("C_0","guard constant","The constant 128 m Psi^2 in the guard width.","direct",span("where $C_0=128m\\Psi^2$","\\vartheta+3\\}$")),
]
out={"derivations":[{"step":a,"quote":b} for a,b in der],
"relations":[{"prerequisite":a,"predicate":b,"quote":c} for a,b,c in rel],
"symbols":[{"symbol":a,"name":b,"meaning":c,"relation":d,"quote":e} for a,b,c,d,e in sy]}
for d in out["derivations"]: assert d["quote"] in t
for d in out["relations"]: assert d["quote"] in t
for d in out["symbols"]: assert d["quote"] in t,d
json.dump(out,open('/home/user/e2e-run/exegenius/tasks/0381-write-simultaneous-layer.answer.json','w'),indent=1)
