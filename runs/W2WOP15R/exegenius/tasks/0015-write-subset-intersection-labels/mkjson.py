import json,sys,re
raw=open(sys.argv[1]).read()
md=re.sub(r'<cite[^>]*>.*?</cite>','',raw,flags=re.S)
def span(start,end):
    i=md.index(start)
    j=md.index(end,i)
    q=md[i:j+len(end)]
    assert '\n' not in q, q
    return q
S_open=span("Subspace labels attach","as recursive saving requires.")
S_par2=span("Triples are three-element","$m=h^3.$")
S_frames=span("The labels choose the frames","in its larger.")
S_L=span("The saving needs","relative to $N.$")
S_F=span("The bit network uses","$-91/9.$")
S_tT=span("Triple indicators $t_S,t_T$","\\bmod 2.$")
S_s431=span("Triple indicators $t_S,t_T$","forms multiplying factorwise.")
S_calF=span("Labels lie in","forms multiplying factorwise.")
S_u=span("Put $u_a=","U_a=\\langle u_a\\rangle.$")
S_terminal=span("so sources total dimension","=Wm-N.$")
S_stage=span("At stage $j$ put","labels move")
S_next=span("Writing $K=","to $\\mathcal F,U_a^\\perp.$")
S_loss=span("Labels nest along every edge","Wm-2N+2L.$")
S_ratio=span("Thus $L/N=","below one half.")
S_bit=span("Bit-network label $U$","because $2L_{\\rm b}<N$ holds.")
S_Pi=span("Bit-network label $U$ gets","elsewhere.")
S_C=span("A complex-network label $U$ gets","swapping two entries.")
S_E=span("On an edge $U\\to V$","an even support:")
S_sh=span("As $\\operatorname{wt}(e)$ is odd","as $L_{\\rm c}<N$ holds.")
S_Z=span("On $X_a\\to Y_a,$","C=iZC^{-1}Z.$")
S_c7=span("As $\\operatorname{wt}(e)$ is odd","leaves $C^{\\otimes m}$ everywhere.")
def sym(symbol,name,meaning,rel,quote):
    return dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote)
symbols=[
 sym("m","label-space dimension","The dimension of the bilinear space in which all labels live, equal to h^3.","count",S_open),
 sym("W","wire count","The total number of wires in the network.","count",S_open),
 sym("s","total edge cost","The total cost of all edge changes of the network: the sum of the edge ranks, which is the number of smaller calls.","count",S_open),
 sym("h","ground-set size","The number of points (100) from which the three-element subsets are drawn.","count",S_par2),
 sym("N","bank size","The number of wires in each data bank, one for each triple of triples a.","count",S_par2),
 sym("a","bank index","A triple of triples (a_1,a_2,a_3) indexing the data wires X_a and Y_a.","direct",S_par2),
 sym("I","invocation count","The number of invocations over the three stages, 3 binom(h,3)^2.","count",S_par2),
 sym("c","central wires per invocation","The number of central wires in each invocation: 100 in the bit network, 101 in the complex one.","count",S_par2),
 sym("L","lost dimension","The total label dimension lost on the decreasing edges of the network.","count",S_L),
 sym("F","coordinate space","The h-dimensional space carrying a nondegenerate symmetric bilinear form: Q^h with the modified form in the bit network, F_2^h with the dot product in the complex one.","direct",S_F),
 sym("t_T","triple indicator","The indicator vector in F of the triple T.","direct",S_tT),
 sym("\\mathcal F","label space","The space F tensor F tensor F of h x h x h arrays, with the factorwise bilinear form, in which every label is a subspace.","direct",S_calF),
 sym("u_a","index tensor","The tensor product of the indicators of the three triples of a.","direct",S_u),
 sym("U_a","index line","The line spanned by u_a, the source label of X_a.","direct",S_u),
 sym("j","stage number","The stage (1, 2 or 3), which operates on the j-th coordinate of the index a.","direct",S_stage),
 sym("A","exposed factors","The tensor power of F over the j-1 coordinates already exposed at stage j.","direct",S_stage),
 sym("P","exposed index line","The line in A spanned by the tensor of the indicators of the first j-1 triples of a.","direct",S_stage),
 sym("B","complement of P","The orthogonal complement of P inside A.","direct",S_stage),
 sym("K","later index line","The line spanned by the tensor of the indicators of the triples of a after the j-th.","direct",S_stage),
 sym("\\Pi_U","projection onto a label","The projection onto the label U along its orthogonal complement.","direct",S_Pi),
 sym("\\mathcal C_U","phase frame","The frame given to a vertex with label U in the complex network.","direct",S_C),
 sym("q_U","phase exponent","The Hamming weight of the binary projection of the address onto U, modulo 4.","direct",S_C),
 sym("x","binary address","An address of a wire's array, a vector in F_2^m.","direct",S_C),
 sym("\\operatorname{wt}","Hamming weight","The number of nonzero coordinates of a binary vector.","direct",S_C),
 sym("H","Hadamard matrix","The 2 x 2 Hadamard matrix.","direct",S_C),
 sym("C","two-point kernel","The 2 x 2 kernel H diag(1,i) H = alpha I + beta sh.","direct",S_C),
 sym("\\alpha","kernel identity coefficient","The coefficient (1+i)/2 of the identity in C.","direct",S_C),
 sym("\\beta","kernel swap coefficient","The coefficient (1-i)/2 of the swap in C.","direct",S_C),
 sym("\\mathrm{sh}","swap","The 2 x 2 matrix swapping the two entries of a vector.","direct",S_C),
 sym("\\mathcal E","residual basis","An orthonormal basis of the orthogonal residual of an edge.","direct",S_E),
 sym("\\mathrm{sh}_e","translation by e","The operator translating an array on F_2^m by the vector e.","direct",S_sh),
 sym("Z","sign matrix","The diagonal matrix diag(1,-1).","direct",S_Z),
]
derivs=[
 dict(step="S4.3.1",quote=S_s431),
 dict(step="S4.3.2",quote=S_terminal),
 dict(step="S4.3.3",quote=S_next),
 dict(step="S4.3.4",quote=S_loss),
 dict(step="S4.3.5",quote=S_ratio),
 dict(step="S4.3.6",quote=S_bit),
 dict(step="S4.3.7",quote=S_c7),
]
rels=[
 dict(prerequisite="linear-network",predicate="attach subspaces to the vertices of",quote=S_open),
 dict(prerequisite="common-frame-principle",predicate="choose the frames of",quote=S_frames),
 dict(prerequisite="linear-algebra-basics",predicate="measure each edge's frame change by",quote=S_frames),
]
json.dump(dict(symbols=symbols,relations=rels,derivations=derivs),open(sys.argv[2],'w'),indent=1,ensure_ascii=False)
print("ok")
