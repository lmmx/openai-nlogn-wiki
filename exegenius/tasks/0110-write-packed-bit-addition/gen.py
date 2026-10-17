import json
md=open('0110-write-packed-bit-addition.answer.md').read()
S1="Packed selected-bit addition XORs chosen bits of a chunk $x$ into chunk $y$ (chunks here), restoring a scratch chunk $z$; the [simultaneous butterfly layer](simultaneous-layer.md) on $d$ address chunks needs it."
Q_R="Records have $R$ bits."
Q_L="A chunk has $L=fK$ bits (segment length $K\\ge6$); the $f$ selected bits lie at $j_i=\\rho+iK$, $0\\le i<f$, with offset $\\rho<K$; the goal is $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$."
Q_M="Let $M$ count addresses, $V=MR$, and $A_{\\rm rect}=\\lceil\\log_2(2V)\\rceil$ bound counter lengths."
Q_c="For a Boolean control $c$ and integers $u,w$, $c[P]$ is $c$ if $P$ holds, else $0$."
Q_seg="For $0\\le i<f-1$, the $K$ bits of $y$ from $j_i$ give a segment $u_i=2g_i+a_i$ and those of $z$ give $w_i=2h_i+b_i$, with bits $a_i,b_i$, guard values $g_i,h_i\\in\\{0,\\dots,2^{K-1}-1\\}$, and control $c_i=x_{j_i}$."
Q_S0="Each is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the addresses; $S_0$ composes the eight."
Q_B="Let $\\mathcal B$ (exceptional addresses) be those where a guard of $y$ or $z$ fails $10\\le g\\le2^{K-1}-11$."
Q_T0="Off $\\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no segment carries into or borrows from a neighbour, and $S_0$ equals the ideal map $T_0$ XORing at $j_0,\\dots,j_{f-2}$."
Q_U="Guards are equidistributed at every spectator choice, so a union bound over $2(f-1)$ guards gives $|\\mathcal B|\\le\\delta_{\\rm bad}M$ with $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$."
Q_cost="It performs rotations as [controlled shifts](controlled-shifts.md) costing $O(V)$ and swaps as [chunk interchanges](address-interchange.md) costing $O(VL^\\tau)$ for fixed exponent $\\tau<1$."
Q_p="With $p$ the precision bits, both vanish when $A_{\\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\\le d\\le p$ and $K/\\log p\\to\\infty$, so the cost is $O(V(L^\\tau+1))$."
Q_14="Per $V$ the extra terms are $A_{\\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\\rm rect}(1+A_{\\rm rect}/R)$. "+Q_p
Q_10="$T_0$ flips only the bits $a_i$, preserving guards and so $\\mathcal B$. Two bijections agreeing off $\\mathcal B$ give $S_0(\\mathcal B^c)=T_0(\\mathcal B^c)=\\mathcal B^c$ and $S_0(\\mathcal B)=\\mathcal B$, so $T_0S_0^{-1}$ fixes $\\mathcal B^c$ and permutes $\\mathcal B$."
Q_12="A scan extracts records at $\\mathcal B$, computing each destination $T_0S_0^{-1}$ by reversing the eight additions; its rank (current rank plus signed chunk differences times strides) is the key, and its hole is marked. As $T_0S_0^{-1}$ permutes $\\mathcal B$, the keys are exactly the holes' ranks, so a stable radix sort and one scan refilling holes in order apply $T_0$."
Q_13="Schoolbook arithmetic on counters costs $O(A_{\\rm rect}^3)$ per record; at most $A_{\\rm rect}$ radix passes sort $|\\mathcal B|$ records of $R+A_{\\rm rect}$ bits."
Q_1="The time is $O(V(L^\\tau+1)+MA_{\\rm rect}^3+\\delta_{\\rm bad}MA_{\\rm rect}(R+A_{\\rm rect}))$"
Q_2="For $c=1$, substituting the four parity pairs shows the first four lines induce $(00\\ 01\\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\\ 10\\ 11)$, composing to $(00\\ 10)(01\\ 11)$: it flips the parity of $u$ and restores $w$'s."
Q_3="So $(u',w')=(u+c(1-2(u\\bmod2)),w)$, keeping quotients by two."
Q_6="$S_0$ has at most eight rotations and sixteen swaps"
Q_7="Ten values fall on each side of the interval ($2^{K-1}\\ge32$): twenty per guard"
for q in [S1,Q_R,Q_L,Q_M,Q_c,Q_seg,Q_S0,Q_B,Q_T0,Q_U,Q_cost,Q_p,Q_14,Q_10,Q_12,Q_13,Q_1,Q_2,Q_3,Q_6,Q_7]:
    assert q in md, q
sym=[]
def s(symbol,name,meaning,rel,quote): sym.append(dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote))
s("x","source chunk","The address chunk whose selected bits are XORed into y.","direct",S1)
s("y","target chunk","The address chunk that receives the XORs (not the ring variable).","direct",S1)
s("z","scratch chunk","The third address chunk, used as scratch and restored.","direct",S1)
s("d","chunk count","The number of address chunks the butterfly layer acts on.","count",S1)
s("R","record bits","The number of bits in a record (not the scalar ring).","count",Q_R)
s("L","chunk bits","The number of bits in an address chunk, L=fK.","count",Q_L)
s("K","segment length","The number of bits in a segment, and the spacing of selected positions.","count",Q_L)
s("f","selected bits","The number of selected bit positions in a chunk.","count",Q_L)
s("\\rho","offset","The position of the lowest selected bit, 0 <= rho < K.","direct",Q_L)
s("j_i","selected position","The position j_i = rho + iK of the i-th selected bit.","direct",Q_L)
s("M","address count","The number of addresses.","count",Q_M)
s("V","volume","The number of bits stored, MR.","count",Q_M)
s("A_{\\rm rect}","counter length","The bit length of counters, ceil(log2(2V)).","direct",Q_M)
s("c","control","A Boolean control.","direct",Q_c)
s("u","first integer","The integer on which the parity-conditioned additions act first (a segment of y).","direct",Q_c)
s("w","second integer","The auxiliary integer to be restored (a segment of z).","direct",Q_c)
s("g_i","guard of y","The segment value of y divided by two, rounded down.","direct",Q_seg)
s("h_i","guard of z","The segment value of z divided by two, rounded down.","direct",Q_seg)
s("a_i","low bit of y","The lowest bit of the i-th segment of y.","direct",Q_seg)
s("b_i","low bit of z","The lowest bit of the i-th segment of z.","direct",Q_seg)
s("c_i","segment control","The selected bit of x at j_i, controlling the i-th segment pair.","direct",Q_seg)
s("S_0","packed map","The composition of the eight packed cyclic shifts.","direct",Q_S0)
s("\\mathcal B","exceptional set","The addresses where some guard of y or z lies outside [10, 2^{K-1}-11].","direct",Q_B)
s("T_0","ideal map","The permutation that performs the required XORs at j_0..j_{f-2}.","direct",Q_T0)
s("\\delta_{\\rm bad}","bad fraction","The bound min{1, 80(f-1)2^{-K}} on the fraction of exceptional addresses.","direct",Q_U)
s("\\tau","swap exponent","The fixed exponent below 1 in the chunk interchange cost.","direct",Q_cost)
s("p","precision","The number of precision bits of the records.","count",Q_p)
der=[("S1.6.3.1",Q_1),("S1.6.3.2",Q_2),("S1.6.3.3",Q_3),("S1.6.3.4",Q_seg),("S1.6.3.5",Q_S0),("S1.6.3.6",Q_T0),("S1.6.3.7",Q_7),("S1.6.3.8",Q_U),("S1.6.3.9",Q_U),("S1.6.3.10",Q_10),("S1.6.3.11",Q_6),("S1.6.3.12",Q_12),("S1.6.3.13",Q_13),("S1.6.3.14",Q_14)]
out=dict(symbols=sym,
 relations=[dict(prerequisite="controlled-shifts",predicate="performs rotations as",quote=Q_cost),
            dict(prerequisite="address-interchange",predicate="performs swaps as",quote=Q_cost)],
 derivations=[dict(step=a,quote=b) for a,b in der])
json.dump(out,open('0110-write-packed-bit-addition.answer.json','w'),indent=1)
