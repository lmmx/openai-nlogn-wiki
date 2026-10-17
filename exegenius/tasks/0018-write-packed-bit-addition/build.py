import json,re
T=r"\tau"
s_intro=r"Packed selected-bit addition XORs selected bits of an address chunk $x$ into chunk $y$, with a third chunk $z$ as restored scratch, for the [simultaneous butterfly layer](simultaneous-layer.md)'s binary changes of basis."
S1=r"A chunk has $L=fK$ bits: $f$ selected bits spaced $K$ apart, at positions $j_i=\rho+iK$."
S2=r"Let $M$ be the number of addresses, $R$ the bits per record, $V=MR$ the volume, and $A_{\rm rect}=\log_2(2V)$ rounded up, the bit length of counters."
SC=r"The packed map performs its rotations as [controlled shifts](controlled-shifts.md) costing $O(V)$."
SI=r"It swaps chunks using the [chunk interchange](address-interchange.md), costing $O(VL^\tau)$ for fixed $\tau<1$."
S3=r"For a control $c$ and integers $u,w$, do these eight additions in order:"
DISP=r"$$\begin{array}{llll} u\mathrel{-}=c[w\equiv0\pmod2] & w\mathrel{-}=c[u\equiv0\pmod2] & u\mathrel{+}=c[w\equiv0\pmod2] & w\mathrel{+}=c[u\equiv0\pmod2]\\ w\mathrel{+}=c[u\equiv1\pmod2] & u\mathrel{+}=c[w\equiv1\pmod2] & w\mathrel{-}=c[u\equiv1\pmod2] & u\mathrel{-}=c[w\equiv1\pmod2]\end{array}$$"
D2=r"For $c=1$ the first four induce the cycle $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11)$, so their composition is $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$."
D3=r"Predicates depend only on parities, so tracing $(0,0),(0,1),(1,0),(1,1)$ gives $(1,0),(1,1),(0,0),(0,1)$, hence the complete output is $(u',w')=(u+c(1-2(u\bmod2)),w)$, which keeps the quotient of $u$ by two and restores $w$."
D4=r"For $0\le i<f-1$, the $K$ bits of $y$ from position $j_i$ form a segment $u_i=2g_i+a_i$, and those of $z$ give $w_i=2h_i+b_i$, with bits $a_i,b_i$. The guard values satisfy $0\le g_i,h_i<2^{K-1}$, and the control is $c_i=x_{j_i}$."
D5=r"One line applied to all segments is one cyclic shift of a whole chunk, whose offset never depends on the target chunk, hence a bijection of the rectangle."
D11=r"Let $S_0$ be the eight lines' composition. It uses at most sixteen swaps and eight rotations"
CITE=r' <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>'
SB=r"Let $\mathcal B$ be the addresses where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11$."
D6=r"Elsewhere, each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$ and no segment carries into or borrows from its neighbour. Then $S_0$ equals the ideal XOR map $T_0$."
D7=r"There are exactly twenty excluded values for each guard among $2^{K-1}$."
D8=r"A union bound over the $2(f-1)$ guards, with the same guard distribution at every choice of other coordinates, bounds the bad addresses."
D9=r"Hence $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, whatever the records."
D10=r"Both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, and $T_0$ preserves $\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$."
D12=r"The repair extracts the records at $\mathcal B$ with destination-rank keys, stably radix-sorts them, and reinserts them in one scan. The keys are distinct because $T_0S_0^{-1}$ permutes $\mathcal B$."
D1=r"With $\delta_{\rm bad}$ as above, the time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$:"
D13=r"movement costs $O(V(L^\tau+1))$, record scans $O(MA_{\rm rect}^3+V)$, radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$."
D14=r"Dividing the extra terms by $V$, with $p$ the coefficient precision and $d$ the chunk bound, gives $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=o(1)$ when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$. So the cost is $O(V(L^\tau+1))$."
P=[s_intro, " ".join([S1,S2,SC,SI]), S3, DISP, " ".join([D2,D3]),
 " ".join([r"Omit the top selected position.",D4]),
 " ".join([D5,D11])+CITE,
 " ".join([SB,D6]), " ".join([D7,D8,D9]), D10, D12, " ".join([D1,D13,D14])]
body="\n\n".join(P)+"\n"
open("exegenius/tasks/0018-write-packed-bit-addition.answer.md","w").write(body)
def w(s):
    t=re.sub(r"<cite.*?</cite>","",s)
    t=re.sub(r"\$\$.*?\$\$","",t,flags=re.S); t=re.sub(r"\$.*?\$","",t)
    t=re.sub(r"\(\S*\.md\)","",t)
    return len(re.findall(r"[A-Za-z]+",t))
print("words",w(body))
def q(x):
    assert x in body,x; return x
D=[("S1.6.3.1",D1),("S1.6.3.2",D2),("S1.6.3.3",D3),("S1.6.3.4",D4),("S1.6.3.5",D5),("S1.6.3.6",D6),("S1.6.3.7",D7),("S1.6.3.8",D8),("S1.6.3.9",D9),("S1.6.3.10",D10),("S1.6.3.11",D11),("S1.6.3.12",D12),("S1.6.3.13",D13),("S1.6.3.14",D14)]
sym=[
("L","bits per chunk","Number of bits in each address chunk.","count",S1),
("f","selected bits","Number of selected bits in each chunk.","count",S1),
("K","spacing","Spacing between consecutive selected positions, which is also the bit length of a segment.","direct",S1),
("\\rho","offset","Offset of the lowest selected position.","direct",S1),
("M","address count","Number of addresses.","count",S2),
("R","record length","Number of bits in a record.","count",S2),
("V","volume","Total number of bits, M times R.","count",S2),
("A_{\\rm rect}","counter length","Bit length of counters.","direct",S2),
("c","control","Boolean control of the eight additions.","direct",S3),
("u","target integer","Integer whose parity is flipped by the eight additions.","direct",S3),
("w","auxiliary integer","Arbitrary auxiliary integer restored by the eight additions.","direct",S3),
("\\tau","interchange exponent","Fixed exponent below one in the cost of the chunk interchange.","direct",SI),
("\\mathcal B","exceptional set","Set of addresses where some guard fails the interval test.","direct",SB),
("S_0","packed map","Composition of the eight packed cyclic-shift lines.","direct",r"Let $S_0$ be the eight lines' composition."),
("p","coefficient precision","Bit precision of the record coefficients.","direct",D14),
("d","chunk bound","Maximum number of address chunks.","direct",D14),
]
syms=[dict(symbol=a,name=n,meaning=m,relation=r,quote=q(qq)) for a,n,m,r,qq in sym]
rel=[dict(prerequisite="controlled-shifts",predicate="performs its rotations as",quote=q(SC)),
     dict(prerequisite="address-interchange",predicate="swaps chunks using",quote=q(SI))]
json.dump(dict(derivations=[dict(step=a,quote=q(b)) for a,b in D],relations=rel,symbols=syms),open("exegenius/tasks/0018-write-packed-bit-addition.answer.json","w"),indent=1)
