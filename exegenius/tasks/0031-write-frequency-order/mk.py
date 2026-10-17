import json,re
md=open('../0031-write-frequency-order.answer.md').read()
def S(sym,name,meaning,rel,q): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=q)
q_ta="It orders the outputs of the [synthetic polynomial transform](synthetic-transform.md) $F_t^-$ over $\\mathcal R_r$, where $t$ is the transform length and $a=\\log_2t$ the number of rounds."
q_w="For $t$ a power of two dividing $2r$, define $\\omega_t=y^{2r/t}$; every power of $\\omega_t$ is an isometry, so each entry is an average of $t$ isometric images and both normalized transforms are contractions."
q_B="Let $B_t$ be the permutation moving the entry at $j$ to $\\operatorname{rev}_a(j)$"
q_H="With $H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ the two-point butterfly, apply $H_0$ to each pair, multiply the $b=1$ output by $\\omega_t^{-k}$, and recurse on the two length-$t/2$ branches."
q_J="With several axes, a round applies $H_0$ on every axis at once, one parallel butterfly $\\mathcal H$."
q_J2="Each axis's twiddle depends only on its own address bits, so twiddles commute with the other axes' butterflies and group into one recordwise monomial $J_E$ that multiplies the record by $y^E$, with"
q_u="Here $u_i$ is axis $i$'s current length, $b_i$ its new branch bit and $k_i$ the index encoded by its unprocessed slots, so $E$ depends on the address, not on coefficient values."
syms=[
S("t","transform length","The number of ring elements transformed along one axis, a power of two dividing 2r.","count",q_ta),
S("a","number of rounds","The number log_2 t of rounds of the fast algorithm.","count",q_ta),
S("\\omega_t","root of unity","The power y^{2r/t} of the ring variable used as the t-th root of unity.","direct",q_w),
S("H_0","two-point butterfly","The 2x2 matrix (1/2)[[1,1],[1,-1]] applied to each pair of entries.","direct",q_H),
S("B_t","bit-reversal permutation","The permutation of records moving the entry at j to rev_a(j).","direct","Let $B_t$ be the permutation moving the entry at $j$ to $\\operatorname{rev}_a(j)$ <cite"),
S("\\mathcal H","parallel butterfly","The butterfly layer applying H_0 on every participating axis at once.","direct",q_J),
S("J_E","recordwise monomial","The operation multiplying the record at each address by y^E.","direct",q_J2),
S("u_i","current length","The current recursive length of axis i.","direct",q_u),
S("b_i","branch bit","The newly written branch bit of axis i.","direct",q_u),
S("k_i","encoded index","The index encoded by the still unprocessed slots of axis i.","direct",q_u),
]
# B_t quote: use text before cite
syms[4]['quote']="Let $B_t$ be the permutation moving the entry at $j$ to $\\operatorname{rev}_a(j)$"
D=[
("S2.1.1",q_w),
("S2.1.2","The ring has zero divisors, so one cannot divide by $\\omega_t^j-1$; instead $\\sum_{k=0}^{t-1}\\omega_t^{jk}$ equals $t$ if $t\\mid j$ and $0$ otherwise."),
("S2.1.3","Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum $S$ by $y^{rj_0}=-1$."),
("S2.1.4","Hence the sum is zero, since the additive group of $\\mathcal R_r$ has no two-torsion"),
("S2.1.5",q_H),
("S2.1.6","After all $a$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ is stored at slot $\\operatorname{rev}_a(j)$, where $\\operatorname{rev}_a$ reverses the $a$ binary digits."),
("S2.1.7","The opposite procedure runs the levels backwards; since $H_0^2=I/2$, each reversed level is half the inverse of the forward level, over $a=\\log_2t$ levels."),
("S2.1.8","The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, and as $F_t^+B_t^{-1}B_tF_t^-=F_t^+F_t^-=I/t$ by character cancellation, the two reverse operators agree."),
("S2.1.9","So the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$."),
("S2.1.10",q_J+" "+q_J2),
("S2.1.11",q_u),
("S2.1.12","Each $\\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction."),
]
rel=[dict(prerequisite="synthetic-transform",predicate="orders the outputs of",quote=q_ta)]
for _,q in D+[(0,s['quote']) for s in syms]+[(0,rel[0]['quote'])]:
    assert q in md,q
json.dump(dict(symbols=syms,relations=rel,derivations=[dict(step=s,quote=q) for s,q in D]),open('../0031-write-frequency-order.answer.json','w'),indent=1)
# word count
t=re.sub(r'<cite.*?</cite>','',md,flags=re.S); t=re.sub(r'\$\$.*?\$\$','',t,flags=re.S); t=re.sub(r'\$.*?\$','',t)
print(len(t.split()))
