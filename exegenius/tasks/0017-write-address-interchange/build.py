import json
t=open('../0017-write-address-interchange.answer.md').read()
S=[]
def sym(symbol,name,meaning,rel,quote):
    assert quote in t,quote
    S.append(dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote))
q0="Fast address-chunk interchange swaps two disjoint $u$-bit address fields of an array with $V$ entries (volume) in time $O(Vu^\\tau)$"
sym("u","chunk width","The number of bits in each of the two address chunks.","count",q0)
sym("V","volume","The number of entries of the array.","count",q0)
sym("\\tau","time exponent","The fixed exponent below 1 in the time bound, 1-2^{-50}.","direct","with $\\tau=1-2^{-50}$ fixed.")
q1="With radix-$q$ digits, $q$ a fixed prime, let $H,D$ be the chunk values."
sym("q","radix","The fixed prime used as digit radix.","direct",q1)
sym("H","first chunk","The value of the first chunk.","direct",q1)
sym("D","second chunk","The value of the second chunk.","direct",q1)
q2="Let chunks have $e=m^k$ digits ($m$ fields, $k$ levels), each field $b=e/m$ digits, so $H,D$ are vectors over $\\mathbb Z/q^b\\mathbb Z$."
sym("e","chunk digits","The number of radix-q digits in each chunk.","count",q2)
sym("m","fields per chunk","The number of fields each chunk is split into.","count",q2)
sym("k","levels","The number of recursion levels, with e = m^k.","count",q2)
sym("b","field width","The number of digits in each field.","count",q2)
q3="The [exchange network](exchange-network.md) has $W$ wires and edge matrices $A_\\epsilon$ of total rank $s<Wm$"
sym("W","wires","The number of wires of the exchange network.","count",q3)
sym("A_\\epsilon","edge matrix","The matrix attached to a network edge.","direct",q3)
sym("s","total edge rank","The sum of the ranks of the edge matrices.","count",q3)
sym("\\Phi_M","frame permutation","The address permutation moving the entry at (H,D) to (H+MD,D).","direct","A [frame](array-frames.md) at a vertex with matrix $M$ is the address permutation $\\Phi_M$, $(H,D)\\mapsto(H+MD,D)$")
sym("M","vertex matrix","The matrix attached to a network vertex, determining its frame.","direct","A [frame](array-frames.md) at a vertex with matrix $M$ is the address permutation $\\Phi_M$")
q4="$f_w$ is wire $w$'s input, $\\sigma(w)$ its role"
sym("f_w","wire input","The physical input array of wire w.","direct",q4)
sym("\\sigma","role assignment","The map sending wire w to its role sigma(w).","direct",q4)
sym("F_k","cost per volume","A uniform upper bound on time divided by logical volume at width m^k.","direct","With $F_k$ the bound on time per unit volume at width $m^k$")
q5="Put $k'=\\lceil\\log_m e\\rceil$ and let $\\rho=\\lceil k'\\log W/(2\\log q)\\rceil$ be the number of top digits interchanged first"
sym("k'","chunk level","The least integer with m^{k'} at least e, the recursion depth for width e.","direct",q5)
sym("\\rho","high digits","The number of top digits of each chunk interchanged first.","count",q5)
sym("R","row range","The range of the row field formed by the two high parts.","direct","Joining them, the high parts form a row field of range $R=q^{2\\rho}\\ge W^{k'}$ before both remaining chunks.")
sym("a_j","piece count","The number of pieces of width m^j in the base-m expansion of e minus rho.","count","Write $e-\\rho=\\sum_{j=0}^{k'} a_jm^j$, $0\\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case.")
R=[]
def rel(pre,pred,quote):
    assert quote in t,quote
    R.append(dict(prerequisite=pre,predicate=pred,quote=quote))
rel("matrix-shear","performs each shear by","Each shear is performed by [Matrix shear by triangular factorization](matrix-shear.md): rank $\\alpha$ costs $\\alpha$ interchanges of $b$-digit fields")
rel("stream-ops","splits and merges streams by","Each stream has volume $V/W$ and row count divisible by $W^{k-1}$; streams are split and merged by [stream scans](stream-ops.md).")
rel("rank-recurrence","satisfies the recurrence of","With $F_k$ the bound on time per unit volume at width $m^k$, $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, so it satisfies the recurrence of [Recursive power saving](rank-recurrence.md).")
D=[]
def der(step,quote):
    assert quote in t,(step,quote)
    D.append(dict(step=step,quote=quote))
a=t.index("each on volume $V/W$; other work")
b=t.index("So $F_k=O(e^\\tau)$.")+len("So $F_k=O(e^\\tau)$.")
der("S1.5.2",t[a:b])
a=t.index("Put $k'=")
b=t.index("gives $O(Vu^\\tau)$")+len("gives $O(Vu^\\tau)$")
der("S1.5.3",t[a:b])
json.dump(dict(symbols=S,relations=R,derivations=D),open('../0017-write-address-interchange.answer.json','w'),indent=1)
