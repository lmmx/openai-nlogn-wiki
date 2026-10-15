import json
body = open('../0015-write-subset-intersection-labels.answer.md', encoding='utf-8').read()

def q(s):
    n = body.count(s)
    assert n == 1, (n, s[:80])
    return s

Q = {}
Q['W'] = q(r"Subspace labels from three-element subsets are nested nondegenerate subspaces that keep a network's total edge rank below $Wm$, where $W$ counts wires and $m$ is the label dimension.")
Q['link'] = q(r"The labels are attached to the gates and terminals of a [Linear exchange network with restored scratch wires](linear-network.md).")
Q['nest'] = q(r"Each label $U$ has projection $P_U,$ and for nested labels $U\subset V,$ $P_V-P_U$ is the identity on the residual $V\cap U^\perp$ and zero on its complement, so an edge costs rank $\dim V-\dim U.$")
Q['alg'] = q(r"The labels are based on [Rank, subspaces and orthogonal complements](linear-algebra-basics.md).")
Q['frame'] = q(r"They are used as frames in [Frames on wire arrays](common-frame-principle.md): vertex $v$ carries $M_v=P_{U_v}.$")
Q['bitF'] = q(r"For the bit network $F=\mathbb Q^h$ with $\langle p,g\rangle=p^{\mathsf T}(I-J/9)g,$ $J$ the all-ones matrix; for the complex network $F=\mathbb F_2^h$ with the dot product.")
Q['ground'] = q(r"Triples $S,T$ in a ground set of $h=100$ points have indicators $t_S,t_T.$")
Q['triple'] = q(r"Since $t_S,t_T$ have three ones, $\langle t_S,t_T\rangle=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2,$ so each triple line is nondegenerate.")
Q['label'] = q(r"The label space $\mathcal F=F^{\otimes3}$ has dimension $m=h^3.$")
Q['input'] = q(r"An input $a=(a_1,a_2,a_3)$ of three triples has label $U_a=\langle u_a\rangle,$ where $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}.$")
Q['roles'] = q(r"$X_a$ has source $U_a$ and sink $\mathcal F,$ $Y_a$ has source $0$ and sink $U_a^\perp,$ and scratch roles have source $0$ and sink $\mathcal F.$")
Q['sums'] = q(r"Each $U_a$ is a line, so sources total $N,$ one per input, and sinks $Wm-N.$")
Q['stage'] = q(r"At stage $j$ let $A=F^{\otimes(j-1)},$ $R=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$ and $B=R^\perp$ in $A.$")
Q['next'] = q(r"The next stage has $A'=A\otimes F,$ $R'=R\otimes\langle t_{a_j}\rangle$ and $B'=(R')^\perp,$ so outgoing labels equal the next incoming ones.")
Q['dim'] = q(r"Dimension drops only on central edges from time $3$ to $4,$ each by $h.$")
Q['inv'] = q(r"With $\nu$ invocations of $c$ central wires each, total loss $L=\nu ch.$")
Q['gate'] = q(r"Gate labels at times $0$ to $7$ are $B\otimes\langle t_T\rangle,$ $B\otimes F,$ $(B\otimes F)\oplus(R\otimes\langle t_T\rangle),$ $A\otimes F,$ $B\otimes F,$ $(B\otimes F)\oplus(R\otimes\langle t_T\rangle^\perp),$ $A\otimes F,$ $A\otimes F,$ with $\oplus$ the orthogonal sum.")
Q['side'] = q(r"The side edge has residual $R\otimes\langle t_S,t_T\rangle^\perp$ of dimension $h-2,$ since neighbouring triples satisfy $t_S\perp t_T.$")
Q['loss'] = q(r'The loss ratios are $L_{\rm b}/N=100/539$ <cite data-source="paper">\frac{L_{\rm b}}{N}=\frac{100}{539}</cite> and $L_{\rm c}/N=101/539,$ both below one half, so $N$ extra source ranks leave a strict saving.')
Q['bit'] = q(r"Bit network: $-P_{U_a}$ replaces $M_v$ at the source of $X_a;$ then $P_{U_a^\perp}+P_{U_a}=I_m$ makes every endpoint difference $I_m.$ Edge ranks equal dimension changes, except at the $N$ source edges, where $2P_{U_a}$ has rank one. Write $s$ for the total edge rank, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m.$")
Q['cpx'] = q(r"Complex network: $C=H\operatorname{diag}(1,i)H=\alpha I+\beta\sigma,$ with $H$ the Hadamard matrix, $\alpha=\frac{1+i}{2},$ $\beta=\frac{1-i}{2}$ and $\sigma$ the coordinate swap.")
Q['frames'] = q(r"Frames over binary $x$ are $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m},$ with $q_U(x)=|P_Ux|\bmod4$ and $|\cdot|$ the Hamming weight.")
Q['basis'] = q(r"For an orthonormal basis $\mathcal K$ of a residual $E,$ $q_V(x)-q_U(x)=\sum_{w\in\mathcal K}|w|\,(w\cdot x\bmod2)\pmod4,$ with $|w|$ odd.")
Q['kernel'] = q(r"Each factor $i^{\pm(w\cdot x\bmod2)}$ is a kernel $\alpha I+\beta\tau_w$ or its inverse, since $H\operatorname{diag}(1,-1)H=\sigma$ turns $(-1)^{w\cdot x}$ into a translation $\tau_w.$")
Q['resid'] = q(r"Over $\mathbb F_2$ residuals have orthonormal bases, so $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m.$")
Q['pair'] = q(r"The pair $X_a\to Y_a$ has inverse kernels, which $C=iZC^{-1}Z$ with $Z=\operatorname{diag}(1,-1)$ turns into $C,$ so every role carries $C^{\otimes m}.$")

def sym(symbol, name, meaning, relation, quote):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation, "quote": quote}

symbols = [
 sym("W","wire count","The number of wires of the network, $W_{\\rm b}$ or $W_{\\rm c}$ for the two constructions.","count",Q['W']),
 sym("m","label dimension","The dimension of the label space, which is $h^3$.","count",Q['W']),
 sym("U","label","A label, the smaller member of a nested pair $U\\subset V$.","direct",Q['nest']),
 sym("V","larger label","A label, the larger member of a nested pair $U\\subset V$.","direct",Q['nest']),
 sym("P_U","label projection","The projection onto a label $U$ along $U^\\perp$.","direct",Q['nest']),
 sym("v","vertex","A vertex of the network.","direct",Q['frame']),
 sym("M_v","vertex frame matrix","The frame matrix at vertex $v$, the projection of its label.","direct",Q['frame']),
 sym("U_v","vertex label","The label of vertex $v$.","direct",Q['frame']),
 sym("F","bilinear space","The bilinear space $\\mathbb Q^h$ of the bit network or $\\mathbb F_2^h$ of the complex network.","direct",Q['bitF']),
 sym("J","all-ones matrix","The matrix with every entry equal to one.","direct",Q['bitF']),
 sym("p","bilinear form argument","A vector of $F$ in the bilinear form of the bit network.","direct",Q['bitF']),
 sym("g","bilinear form argument","A vector of $F$ in the bilinear form of the bit network.","direct",Q['bitF']),
 sym("h","ground-set size","The number of points in the ground set, here 100.","count",Q['ground']),
 sym("S","triple","A triple, a 3-element subset of the ground set.","direct",Q['ground']),
 sym("T","triple","A triple, a 3-element subset of the ground set.","direct",Q['ground']),
 sym("t_S","triple indicator","The indicator vector of the triple $S$.","direct",Q['ground']),
 sym("t_T","triple indicator","The indicator vector of the triple $T$.","direct",Q['ground']),
 sym("\\mathcal F","label space","The label space $F^{\\otimes3}$.","direct",Q['label']),
 sym("a","input","An input, named by a triple of triple indices $(a_1,a_2,a_3)$.","direct",Q['input']),
 sym("u_a","input tensor","The pure tensor $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$ of input $a$.","direct",Q['input']),
 sym("U_a","input label","The label of input $a$, the line spanned by $u_a$.","direct",Q['input']),
 sym("X_a","input role","The input role of $a$, whose source is the label $U_a$.","direct",Q['roles']),
 sym("Y_a","paired role","The role paired with $X_a$, whose sink is $U_a^\\perp$.","direct",Q['roles']),
 sym("N","input count","The number of inputs $a$, each contributing one source dimension.","count",Q['sums']),
 sym("j","stage index","The index of the current stage, which exposes the $j$th tensor factor.","direct",Q['stage']),
 sym("A","stage space","The tensor space $F^{\\otimes(j-1)}$ at stage $j$.","direct",Q['stage']),
 sym("R","stage line","The line spanned by the first $j-1$ triple tensors.","direct",Q['stage']),
 sym("B","stage complement","The complement $R^\\perp$ of $R$ inside $A$.","direct",Q['stage']),
 sym("\\nu","invocation count","The number of invocations of the repeated block.","count",Q['inv']),
 sym("c","central wires","The number of central wires in one invocation.","count",Q['inv']),
 sym("L","total loss","The total dimension lost on decreasing edges.","count",Q['inv']),
 sym("\\oplus","orthogonal sum","The orthogonal direct sum of two subspaces.","direct",Q['gate']),
 sym("s","total edge rank","The total rank of all edge changes.","count",Q['bit']),
 sym("C","two-point kernel","The matrix $H\\operatorname{diag}(1,i)H$.","direct",Q['cpx']),
 sym("H","Hadamard matrix","The normalized Hadamard matrix.","direct",Q['cpx']),
 sym("\\alpha","kernel coefficient","The coefficient $\\frac{1+i}{2}$ of the identity in $C$.","direct",Q['cpx']),
 sym("\\beta","kernel coefficient","The coefficient $\\frac{1-i}{2}$ of $\\sigma$ in $C$.","direct",Q['cpx']),
 sym("\\sigma","coordinate swap","The matrix that interchanges the two coordinates.","direct",Q['cpx']),
 sym("\\mathcal C_U","phase frame","The phase frame of label $U$ on functions of binary vectors.","direct",Q['frames']),
 sym("q_U","phase exponent","The phase exponent $|P_Ux|\\bmod 4$ of label $U$.","direct",Q['frames']),
 sym("x","binary vector","A binary vector in $\\mathbb F_2^m$.","direct",Q['frames']),
 sym("|\\cdot|","Hamming weight","The number of ones in a binary vector.","direct",Q['frames']),
 sym("\\mathcal K","orthonormal basis","An orthonormal basis of the residual $E$.","direct",Q['basis']),
 sym("E","residual","The orthogonal residual of an edge.","direct",Q['basis']),
 sym("w","basis vector","A vector of the orthonormal basis $\\mathcal K$.","direct",Q['basis']),
 sym("\\tau_w","translation","The translation by a binary vector $w$.","direct",Q['kernel']),
 sym("Z","sign matrix","The diagonal sign matrix $\\operatorname{diag}(1,-1)$.","direct",Q['pair']),
]

relations = [
 {"prerequisite":"linear-network","predicate":"are attached to","quote":Q['link']},
 {"prerequisite":"common-frame-principle","predicate":"are used as frames in","quote":Q['frame']},
 {"prerequisite":"linear-algebra-basics","predicate":"are based on","quote":Q['alg']},
]

derivations = [
 {"step":"S4.3.1","quote":Q['triple']},
 {"step":"S4.3.2","quote":Q['roles']+" "+Q['sums']},
 {"step":"S4.3.3","quote":Q['next']},
 {"step":"S4.3.4","quote":Q['dim']+" "+Q['inv']},
 {"step":"S4.3.5","quote":"and $L_{\\rm c}/N=101/539,$ both below one half, so $N$ extra source ranks leave a strict saving."},
 {"step":"S4.3.6","quote":Q['bit']},
 {"step":"S4.3.7","quote":Q['kernel']+" "+Q['resid']},
]

# every derivation quote must be on the page (as one contiguous passage)
for d in derivations:
    assert body.count(d['quote'])==1, d['step']
assert body.count(derivations[4]['quote'])==1
out={"symbols":symbols,"relations":relations,"derivations":derivations}
open('../0015-write-subset-intersection-labels.answer.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=1))
print('ok', len(symbols))
