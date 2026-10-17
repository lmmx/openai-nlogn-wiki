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
q5="Interchange and join the top $\\rho$ digits: the high parts form a row field of range $R=q^{2\\rho}\\ge W^k$ before both remaining chunks."
sym("\\rho","high digits","The number of top digits of each chunk interchanged first.","count",q5)
sym("R","row range","The range of the row field formed by the two high parts.","direct",q5)
sym("a_j","piece count","The number of pieces of width m^j in the base-m expansion of e minus rho.","count","Write $e-\\rho=\\sum_{j=0}^k a_jm^j$, $0\\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case.")
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
der("S1.5.2.1","Let chunks have $e=m^k$ digits ($m$ fields, $k$ levels), each field $b=e/m$ digits, so $H,D$ are vectors over $\\mathbb Z/q^b\\mathbb Z$.")
der("S1.5.2.2","Split whole rows cyclically into $W$ role streams within each prefix; row $r=Wg+(w-1)$ goes to stream $w$ as row $g$.")
der("S1.5.2.3","Each stream has volume $V/W$ and row count divisible by $W^{k-1}$")
der("S1.5.2.4","Each edge applies $\\Phi_{A_\\epsilon}$ to its role stream as above.")
der("S1.5.2.5a","A [frame](array-frames.md) at a vertex with matrix $M$ is the address permutation $\\Phi_M$, $(H,D)\\mapsto(H+MD,D)$; edges change it by $\\Phi_{M'-M}$, and a common address permutation commutes with every pointwise bit gate.")
der("S1.5.2.5b","By the endpoint contract the physical output is $f'_{\\sigma(w)}=\\Phi_{M_{\\mathrm{out}(\\sigma(w))}}\\Phi_{-M_{\\mathrm{in}(w)}}f_w=\\Phi_{I_m}f_w$")
der("S1.5.2.5c","Merging rows back undoes $\\sigma$; so $H\\gets H+D$ holds on every original row, scratch rows included.")
der("S1.5.2.5d","Then $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear needs the network.")
der("S1.5.2.5e","The calls number exactly $s$, the sum of the edge ranks")
der("S1.5.2.5g","With $F_k$ the bound on time per unit volume at width $m^k$, $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$")
der("S1.5.2.5f","each on volume $V/W$; other work costs $O(V)$.")
der("S1.5.2.6","Then $F_k=O(\\sum_{j=0}^k a^j)$, $a=s/W<m^\\tau$. If $a\\le1$, the sum is at most $k+1=O(m^{k\\tau})$. If $a>1$, it is $O(a^k)$ with $a^k<m^{k\\tau}$. So $F_k=O(e^\\tau)$.")
der("S1.5.2","Then $F_k=O(\\sum_{j=0}^k a^j)$, $a=s/W<m^\\tau$. If $a\\le1$, the sum is at most $k+1=O(m^{k\\tau})$. If $a>1$, it is $O(a^k)$ with $a^k<m^{k\\tau}$. So $F_k=O(e^\\tau)$.")
der("S1.5.3.2","Put $k=\\lceil\\log_m e\\rceil$ (a new meaning)")
der("S1.5.3.3","$\\rho=\\lceil k\\log W/(2\\log q)\\rceil$, so $q^{2\\rho}\\ge W^k$")
der("S1.5.3.4","Interchange and join the top $\\rho$ digits: the high parts form a row field of range $R=q^{2\\rho}\\ge W^k$ before both remaining chunks.")
der("S1.5.3.6","Pad with zero rows to $R'=W^k\\lceil R/W^k\\rceil<2R$ rows.")
der("S1.5.3.7","Write $e-\\rho=\\sum_{j=0}^k a_jm^j$, $0\\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case.")
der("S1.5.3.8","The cost $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$")
der("S1.5.3.9","is geometric since $a_j<m$ and $m^k<me$.")
der("S1.5.3.10","Padding $[2^u]$ to $[q^e]$ costs a fixed factor and gives $O(Vu^\\tau)$")
der("S1.5.3","Write $e-\\rho=\\sum_{j=0}^k a_jm^j$, $0\\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case. The cost $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$ is geometric since $a_j<m$ and $m^k<me$.")
json.dump(dict(symbols=S,relations=R,derivations=D),open('../0017-write-address-interchange.answer.json','w'),indent=1)
