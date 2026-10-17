import json
p='/home/user/e2e-run/exegenius/tasks/0108-write-address-interchange.answer.md'
t=open(p).read()
def Q(s):
    assert s in t, s
    return s
S=lambda sym,name,mean,rel,q:{"symbol":sym,"name":name,"meaning":mean,"relation":rel,"quote":Q(q)}
l1="An address is $(p,h,g,d,z)$: prefix $p$, chunks $h,d$, gap $g$, suffix $z$; the goal is $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$."
hd="Write each chunk as top $\\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$."
ek="Let each chunk have $e=m^k$ digits ($k$ recursion levels)."
op="Fast address-chunk interchange, a tape primitive behind the main result, swaps two disjoint $u$-bit address fields of a bit array of volume $V$ (stored bits)"
aj="Write $e-\\nu=\\sum_{j=0}^{k'}a_jm^j$, $0\\le a_j<m$."
symbols=[
S("u","chunk width","The number of bits in each of the two address chunks.","count",op),
S("V","volume","The number of stored bits of the array.","count",op),
S("\\tau","time exponent","The fixed exponent below 1 in the time bound, 1-2^{-50}.","direct","with $\\tau=1-2^{-50}$."),
S("p","prefix","The address field before the first chunk.","direct",l1),
S("h","first chunk","The address field of the first chunk.","direct",l1),
S("d","second chunk","The address field of the second chunk.","direct",l1),
S("g","gap","The address field between the chunks.","direct",l1),
S("z","suffix","The address field after the second chunk.","direct",l1),
S("q","radix","The fixed prime used as digit radix.","direct","Digits are radix $q$, a fixed prime."),
S("H","first chunk value","The value of the first chunk, a vector of m fields.","direct","For chunk values $H,D$,"),
S("D","second chunk value","The value of the second chunk, a vector of m fields.","direct","For chunk values $H,D$,"),
S("e","chunk digits","The number of radix-q digits in each chunk.","count",ek),
S("k","level count","The number of recursion levels, with e=m^k.","count",ek),
S("b","field digits","The number of digits in each of the m fields of a chunk.","count","Cut it into $m$ fields of $b=e/m$ digits"),
S("M","vertex matrix","The rational m by m matrix assigned to a terminal or gate.","direct","each terminal and gate carries a rational $m\\times m$ matrix $M$"),
S("i","edge index","Index of an edge of the network.","direct","and edge $i$ carries $A_i=M_{\\mathrm{head}(i)}-M_{\\mathrm{tail}(i)}$"),
S("A_i","edge matrix","The difference of the matrices at the head and tail of edge i.","direct","and edge $i$ carries $A_i=M_{\\mathrm{head}(i)}-M_{\\mathrm{tail}(i)}$"),
S("I_m","identity matrix","The m by m identity matrix.","direct","with $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$ (the identity)"),
S("w","wire index","The index of a wire of the network, 1 to W.","direct","The shear contract says input wire $w$ ends at output role $\\rho(w)$"),
S("\\Phi_M","shear permutation","The array permutation moving the entry at address (H,D) to (H+MD,D).","direct","Let $\\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$."),
S("M'","other matrix","Another rational m by m matrix.","direct","For another matrix $M'$,"),
S("x","stream row","The row number within a role stream.","direct","row $Wx+w-1$ is sent to role stream $w$ as row $x$"),
S("f_w","input array","The physical input array on wire w.","direct","Wire $w$'s input $f_w$ is read as the logical array"),
S("f'_{\\rho(w)}","output array","The physical output array at role rho(w).","direct","the output is $f'_{\\rho(w)}=\\Phi_{M_{\\mathrm{out}(\\rho(w))}}\\Phi_{-M_{\\mathrm{in}(w)}}f_w=\\Phi_{I_m}f_w$"),
S("j","level","Index of a level of the unrolled recurrence.","direct","Unrolled over levels $j$,"),
S("F_k","normalized cost","The time per unit volume of the interchange at width m^k.","direct","The time per unit volume $F_k$ at width $m^k$ obeys"),
S("k'","level count","The least integer with m^{k'} at least e.","direct","put $k'=\\lceil\\log_m e\\rceil$"),
S("\\nu","top digits","The number of top digits of each chunk interchanged first.","count","and $\\nu=\\lceil k'\\log W/(2\\log q)\\rceil$"),
S("h^+","high part of h","The top nu digits of the first chunk.","direct",hd),
S("h^-","rest of h","The remaining digits of the first chunk.","direct",hd),
S("d^+","high part of d","The top nu digits of the second chunk.","direct",hd),
S("d^-","rest of d","The remaining digits of the second chunk.","direct",hd),
S("\\Lambda","row range","The range of the row field formed by the two high parts.","direct","Now $d^+,h^+$ form a row field of range $\\Lambda=q^{2\\nu}\\ge W^{k'}$ before both remaining chunks."),
S("\\Lambda'","padded row range","The row count after padding with zero rows.","direct","Pad with zero rows to $\\Lambda'=W^{k'}\\lceil \\Lambda/W^{k'}\\rceil<2\\Lambda$ rows"),
S("a_j","piece count","The number of pieces of width m^j, the j-th base-m digit of e minus nu.","count",aj),
]
rel=[
("rank-recurrence","obeys the recurrence of","The time per unit volume $F_k$ at width $m^k$ obeys $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md)."),
("matrix-shear","performs its shears by","[Matrix shear by triangular factorization](matrix-shear.md) performs each $\\Phi_{A_i}$: rank $a$ costs $a$ interchanges of $b$-digit fields"),
("stream-ops","sends rows to role streams by","Within each prefix, row $Wx+w-1$ is sent to role stream $w$ as row $x$ by [stream scans](stream-ops.md)."),
]
relations=[{"prerequisite":a,"predicate":b,"quote":Q(c)} for a,b,c in rel]
d=[
("S1.5.2","For chunk values $H,D$, $D\\gets D-H$, $H\\gets H+D$, $D\\gets H-D$ send $(H,D)$ to $(H,D-H)$, $(D,D-H)$, $(D,H)$. Only the middle shear needs the circuit."),
("S1.5.2","Let each chunk have $e=m^k$ digits ($k$ recursion levels). Cut it into $m$ fields of $b=e/m$ digits, so $H,D$ are vectors over $\\mathbb Z/q^b\\mathbb Z$."),
("S1.5.2","Within each prefix, row $Wx+w-1$ is sent to role stream $w$ as row $x$ by [stream scans](stream-ops.md). Each stream has volume $V/W$ and row count divisible by $W^{k-1}$, the hypothesis one level down."),
("S1.5.2","The [frame](array-frames.md) at a vertex with matrix $M$ is $\\Phi_M$; an edge to a vertex with matrix $M'$ changes it by $\\Phi_{M'-M}=\\Phi_{A_i}$. A common address permutation commutes with every pointwise bit gate."),
("S1.5.2","By the composition rule and the contract, the output is $f'_{\\rho(w)}=\\Phi_{M_{\\mathrm{out}(\\rho(w))}}\\Phi_{-M_{\\mathrm{in}(w)}}f_w=\\Phi_{I_m}f_w$. Merging rows back undoes $\\rho$, so $H\\gets H+D$ holds on every original row, scratch rows included."),
("S1.5.2","The time per unit volume $F_k$ at width $m^k$ obeys $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md). Unrolled over levels $j$, $F_k=O(\\sum_{j=0}^k (s/W)^j)$. If $s/W\\le1$ the sum is at most $k+1=O(m^{k\\tau})$; otherwise it is $O((s/W)^k)$, below $m^{k\\tau}$. Hence $F_k=O(e^\\tau)$."),
("S1.5.3","For general large $e$, put $k'=\\lceil\\log_m e\\rceil$ and $\\nu=\\lceil k'\\log W/(2\\log q)\\rceil$, so $q^{2\\nu}\\ge W^{k'}$, $1\\le\\nu<e$ and $\\nu=O(\\log 2e)$; small $e$ use single-digit interchanges."),
("S1.5.3","Interchange the high digits and move $h^+$ next to $d^+$: $(h^+,h^-,g,d^+,d^-)$ becomes $(d^+,h^+,h^-,g,d^-)$. Now $d^+,h^+$ form a row field of range $\\Lambda=q^{2\\nu}\\ge W^{k'}$ before both remaining chunks. Pad with zero rows to $\\Lambda'=W^{k'}\\lceil \\Lambda/W^{k'}\\rceil<2\\Lambda$ rows (volume below $2V$)."),
("S1.5.3","Write $e-\\nu=\\sum_{j=0}^{k'}a_jm^j$, $0\\le a_j<m$. Split each remaining chunk into $a_j$ pieces of width $m^j$ and interchange corresponding pieces as above, all with this row field. The total $O(V)\\sum_ja_jm^{j\\tau}\\le O(V)\\,m\\sum_jm^{j\\tau}=O(Ve^\\tau)$, since $m^{k'}<me$."),
("S1.5.3","For $u$-bit chunks, pad $[2^u]$ to $[q^e]$ with least $e$ such that $q^e\\ge2^u$ and scan the padding away."),
]
der=[{"step":a,"quote":Q(b)} for a,b in d]
json.dump({"symbols":symbols,"relations":relations,"derivations":der},open('/home/user/e2e-run/exegenius/tasks/0108-write-address-interchange.answer.json','w'),indent=1)
