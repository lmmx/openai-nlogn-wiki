import json,re
md=open('0378-write-subspace-labels.answer.md').read()
def sent(start, end):
    i=md.index(start); j=md.index(end,i)+len(end)
    return md[i:j]
S_open=sent("The labels choose the frames of","the strict saving the recursion needs.")
S_nondeg=sent("A subspace $U$ is *nondegenerate*","joins orthogonal subspaces.")
S_form=sent("Bit labels use $F=","$1-h/9=-91/9$.")
S_trip1=sent("Triples $S,S'\\in\\mathcal T$ have","\\bmod2$.")
S_trip=sent("Triples $S,S'\\in\\mathcal T$ have","sharing zero or two (complex).")
S_tensor=sent("Label dimensions are computed from","\\perp(E'\\otimes G)$.")
S_calF=sent("Labels lie in $\\mathcal F","of dimension $h^3=m$.")
S_Ua=sent("With $U_a=","the terminal labels are")
S_src=sent("Source dimensions sum to $N$","=Wm-N$.")
S_tele=sent("A wire enters and leaves each gate","they sum to $Wm-2N$.")
S_L=sent("If decreasing edges lose $L$","$Wm-2N+2L$.")
S_j=sent("Stage $j\\in\\{1,2,3\\}$","varies $a_j$.")
S_APBQ=sent("In one of its invocations let","the line of the later ones.")
S_GE=sent("For subspaces $G,E\\subseteq F$ write","write")
S_GEp=sent("of dimension $(h^{j-1}-1)","P\\otimes F\\otimes Q$.")
S_fit=sent("They fit: the next stage has","as $P'=U_a$ there, $U_a^\\perp$.")
S_next=sent("They fit: the next stage has","P\\otimes\\langle t_{a_j}\\rangle$.")
S_Bp=sent("Splitting $A=B\\perp P$ and $F=","(P\\otimes t_{a_j}^\\perp)$.")
S_Qp=sent("With $Q=\\langle t_{a_{j+1}}\\rangle\\otimes Q'$","incoming labels.")
S_tXY=sent("With $t_X,t_Y$ the indicators","with gate times as subscripts, are")
S_sched=sent("Rows sharing a time meet at that gate","L_{\\rm c}=Ic_{\\rm c}h$.")
S_incl=sent("Comparing entries, every arrow","true as neighbours are orthogonal.")
S_Lc=sent("Each of the $I=3v^2$ invocations","L_{\\rm c}=Ic_{\\rm c}h$.")
S_ratio=sent("As $N=v^3$,","$L_{\\rm c}/N=101/539$.")
S_Pi=sent("In the bit network a vertex labelled $U$","else $0=\\Pi_0$.")
S_rank=sent("For nondegenerate $U\\subseteq U'$, a vector","rank one.")
S_Up=sent("For nondegenerate $U\\subseteq U'$, a vector","\\perp U'^\\perp$.")
S_sc=sent("[Binary phase frames](phase-frames.md) turn","<W_{\\rm c}m$.")
S_budget=sent("Bit-network edges cost their absolute change","to one small edge.")
for s in [S_open,S_nondeg,S_form,S_trip,S_tensor,S_calF,S_Ua,S_src,S_tele,S_L,S_j,S_APBQ,S_GE,S_GEp,S_fit,S_tXY,S_sched,S_incl,S_ratio,S_Pi,S_rank,S_sc,S_budget]:
    assert '<cite' not in s, s
def b(sym,name,meaning,rel,q): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=q)
symbols=[
b("W","wire count","The number of wires of the network under consideration, W_b for the bit network or W_c for the complex one.","count",S_open),
b("s","smaller-call count","The total number of smaller calls made by the edges of the network under consideration (s_b or s_c).","count",S_open),
b("s_{\\rm b}","bit smaller-call count","The number of smaller calls made by the edges of the bit network.","count",S_open),
b("s_{\\rm c}","complex smaller-call count","The number of smaller calls made by the edges of the complex network.","count",S_open),
b("U","subspace","A subspace of a space with a symmetric bilinear form, later a label.","direct",S_nondeg),
b("x","first vector","A vector of F, the first argument of the bit form (not the polynomial variable).","direct",S_form),
b("y","second vector","A vector of F, the second argument of the bit form (not the ring variable).","direct",S_form),
b("\\mathbf 1","all-ones vector","The vector of F whose entries are all 1.","direct",S_form),
b("S","triple","A three-element subset of [h] (not a convolution length).","direct",S_trip1),
b("S'","second triple","Another three-element subset of [h].","direct",S_trip1),
b("t_S","indicator vector","The indicator vector in F of the triple S.","direct",S_trip1),
b("E","first tensor factor","A subspace of a tensor power of F (in the bracket notation, a subspace of F).","direct",S_tensor),
b("E'","other subspace","Another subspace of a tensor power of F, orthogonal to E in the splitting fact, or a subspace of F containing E.","direct",S_tensor),
b("G","second tensor factor","A subspace of a tensor power of F (in the bracket notation, a subspace of F).","direct",S_tensor),
b("\\mathcal F","label space","The label space F tensor F tensor F, of dimension m.","direct",S_calF),
b("U_a","data line","The line spanned by the tensor product of the indicators of the three triples of the data index a.","direct",S_Ua),
b("L","total loss","The total dimension lost on decreasing edges of the network under consideration.","count",S_L),
b("L_{\\rm b}","bit loss","The total dimension lost on decreasing edges of the bit network.","count",S_L),
b("L_{\\rm c}","complex loss","The total dimension lost on decreasing edges of the complex network.","count",S_L),
b("j","stage index","The index 1, 2 or 3 of the stage, which varies the coordinate a_j.","direct",S_j),
b("A","earlier tensor space","The tensor power of F with j-1 factors, of dimension h^{j-1}.","direct",S_APBQ),
b("P","earlier line","The line in A spanned by the tensor product of the indicators of the earlier triples a_1,...,a_{j-1}.","direct",S_APBQ),
b("B","complement of P","The orthogonal complement of P in A.","direct",S_APBQ),
b("Q","later line","The line spanned by the tensor product of the indicators of the later triples a_{j+1},...,a_3.","direct",S_APBQ),
b("G'","larger first part","A subspace of F containing G.","direct",S_GEp),
b("A'","next earlier space","The space A of the next stage, A tensor F.","direct",S_next),
b("P'","next earlier line","The line P of the next stage, P tensor the line of t_{a_j}.","direct",S_next),
b("B'","next complement","The orthogonal complement of P' in A', the B of the next stage.","direct",S_Bp),
b("Q'","next later line","The line Q of the next stage, spanned by the indicators of the triples after a_{j+1}.","direct",S_Qp),
b("t_X","X-side indicator","The indicator of the j-th triple of the X-entry a wire serves.","direct",S_tXY),
b("t_Y","Y-side indicator","The indicator of the j-th triple of the Y-entry a wire serves.","direct",S_tXY),
b("\\Pi_U","projection","The projection onto U along its orthogonal complement, the matrix at a vertex labelled U.","direct",S_Pi),
b("U'","larger subspace","A nondegenerate subspace containing U.","direct",S_Up),
]
relations=[
 dict(prerequisite="array-frames",predicate="chooses the frames of",quote=S_open),
 dict(prerequisite="tensor-product-of-spaces",predicate="computes label dimensions from facts about",quote=S_tensor),
]
derivations=[
 dict(step="S1.3.1",quote=S_trip),
 dict(step="S1.3.2",quote=S_src),
 dict(step="S1.3.3",quote=S_tele),
 dict(step="S1.3.4",quote=S_fit),
 dict(step="S1.3.5",quote=S_incl),
 dict(step="S1.3.6",quote=S_sched),
 dict(step="S1.3.9",quote=S_ratio),
 dict(step="S1.3.7",quote=S_rank),
]
json.dump(dict(symbols=symbols,relations=relations,derivations=derivations),open('0378-write-subspace-labels.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
