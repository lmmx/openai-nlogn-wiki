import json,re,sys
base='/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WOP15/exegenius/tasks/'
page=open(base+'0015-write-subset-intersection-labels.answer.md').read()
lines=page.split('\n')
def find(start, end=None):
    """Return exact substring of page starting with `start` and ending with `end` (inclusive)."""
    i=page.find(start); assert i>=0, start
    if end is None: return start
    j=page.find(end,i); assert j>=0, end
    return page[i:j+len(end)]
open_s=find("Subspace labels are nested", "smaller calls.")
frame_s=find("Each label is turned into", "in the larger.")
saving_s=find("The saving comes from", "per bank.")
triple_s=find("A *triple* $T$", "\\{0,1\\}^h.$")
bitF_s=find("The bit network uses", "\\sum_ky_k.$")
labels_s=find("Labels lie in", "multiply factorwise.")
bank_s=find("Bank index $a$", "t_{a_3}.$")
delta_s=find("and all wires at a gate share its label", "telescope:")
stage_s=find("Stage $j$ varies", "data labels move as")
gate_s=find("An invocation's gate labels", "gate's triple):")
split_s=find("Splitting $A=B", "\\langle t_X\\rangle\\subset t_Y^\\perp.$")
inv_s=find("With $I=3", "central wires each,")
proj_s=find("Bit network: label $U$", "else $0$).")
sb_s=find("So total rank", "endpoint shears are")
frameC_s=find("Complex network: with Hamming", "H^{\\otimes m}.$")
basis_s=find("Orthogonal binary vectors", "residual $E,$")
kernel_s=find("Each $\\operatorname{wt}(z)$ is odd", "in all.")
route_s=find("Routes $0\\to\\mathcal F$", "differs:")
z_s=find("so $C^{-1}$ on 27 coordinates", "C=iZC^{-1}Z.$")

def sym(symbol,name,meaning,rel,quote): return dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote)
symbols=[
 sym("\\mathcal F","label space","The fixed space F⊗F⊗F (the h×h×h arrays) whose nondegenerate subspaces serve as labels.","direct",labels_s),
 sym("m","label-space dimension","The dimension of the label space, m = h^3.","count",open_s),
 sym("W","wire count","The number of wires in the network under consideration.","count",open_s),
 sym("L","lost dimension","The total dimension lost over all edges whose label shrinks.","count",saving_s),
 sym("N","bank size","The number of values in each of the two data banks, N = C(h,3)^3.","count",saving_s),
 sym("T","triple","A 3-element subset of {1,…,h}.","direct",triple_s),
 sym("h","ground-set size","The size of the ground set {1,…,h} whose 3-element subsets are the triples; h = 100.","count",triple_s),
 sym("t_T","triple indicator","The 0/1 indicator vector of triple T in F.","direct",triple_s),
 sym("F","factor space","The space of h-entry vectors with its form: Q^h with the shifted dot product (bit network) or F_2^h with the dot product (complex network).","direct",bitF_s),
 sym("a","bank index","The index of a value in the data banks, a triple (a_1,a_2,a_3) of triples.","direct",bank_s),
 sym("u_a","index tensor","The array t_{a_1}⊗t_{a_2}⊗t_{a_3} attached to bank index a.","direct",bank_s),
 sym("U_a","index line","The line spanned by u_a, the source label of X_a.","direct",bank_s),
 sym("\\Delta","edge dimension change","The change in label dimension along one edge, head minus tail.","direct",delta_s),
 sym("j","stage number","The stage of the network, 1, 2 or 3, which varies the coordinate a_j.","direct",stage_s),
 sym("t_X","control-side indicator","The indicator of the X-bank triple at one end of a side wire.","direct",split_s),
 sym("t_Y","target-side indicator","The indicator of the Y-bank triple at the other end of a side wire, a neighbor of the X triple.","direct",split_s),
 sym("I","invocation count","The number of invocations, 3·C(h,3)^2.","count",inv_s),
 sym("\\gamma","central wires per invocation","The number of central wires in each invocation: 100 in the bit network, 101 in the complex one (written c in the source).","count",inv_s),
 sym("\\Pi_U","label projection","The projection onto label U along its orthogonal complement, used as the shear matrix of the bit-network frame.","direct",proj_s),
 sym("s_{\\rm b}","bit-network rank sum","The total rank of all edge matrix differences in the bit network, i.e. its number of smaller calls.","count",sb_s),
 sym("\\mathcal C_U","phase frame","The frame H^{⊗m} diag(i^{q_U(x)}) H^{⊗m} given to a vertex with binary label U.","direct",frameC_s),
 sym("q_U","weight phase","The Hamming weight of the projection of x onto U, taken modulo 4.","direct",frameC_s),
 sym("\\operatorname{wt}","Hamming weight","The number of nonzero coordinates of a binary vector.","direct",frameC_s),
 sym("H","Hadamard matrix","The 2×2 Hadamard matrix (1/√2)[[1,1],[1,−1]].","direct",frameC_s),
 sym("E","edge residual","The orthogonal residual of an edge, with V = U ⊥ E.","direct",basis_s),
 sym("\\mathcal B","residual basis","An orthonormal basis of the residual E over F_2.","direct",basis_s),
 sym("\\operatorname{sh}_z","translation","Translation of a function on F_2^m by z: (sh_z f)(x) = f(x+z).","direct",kernel_s),
 sym("s_{\\rm c}","complex-network kernel count","The total number of two-point kernels over all edges of the complex network.","count",kernel_s),
 sym("C","two-point kernel","The 2×2 matrix H diag(1,i) H = ((1+i)/2) I + ((1−i)/2) X.","direct",frameC_s),
 sym("Z","sign matrix","The diagonal matrix diag(1,−1).","direct",z_s),
]
relations=[
 dict(prerequisite="linear-network",predicate="are attached to the gates of",quote=open_s),
 dict(prerequisite="common-frame-principle",predicate="are turned into",quote=frame_s),
 dict(prerequisite="linear-algebra-basics",predicate="measures edge cost by",quote=frame_s),
]
ders=[
 ("S4.3.1", find("As indicators sum to $3,$","are orthogonal.")),
 ("S4.3.2", find("Terminal labels:","Wm-2N+2L.$$")),
 ("S4.3.3", find("Stage $j$ varies","\\mathcal F,U_a^\\perp.$")),
 ("S4.3.4", find("Splitting $A=B","at $3\\to4.$")),
 ("S4.3.5", find("With $I=3","per invocation shrink.")),
 ("S4.3.6", find("Bit network: label $U$","=I_m.$$")),
 ("S4.3.7", find("Complex network: with Hamming","in all.")),
]
derivations=[dict(step=s,quote=q) for s,q in ders]
json.dump(dict(symbols=symbols,relations=relations,derivations=derivations),open(base+'0015-write-subset-intersection-labels.answer.json','w'),ensure_ascii=False,indent=1)
print("ok")
