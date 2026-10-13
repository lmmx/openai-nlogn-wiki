import json
P="/home/user/openai-nlogn-wiki/runs/C4/"
src=open(P+"sources/paper.tex").read()
def Q(q): return {"source":"paper","quote":q}
def inf(id,claim,quote,page=None,frm=None,**kw):
    d={"id":id,"intention":"infer","claim":claim,"quote":Q(quote),"page":page,"from":frm or []}
    d.update(kw); return d
def show(id,claim,method,mot,msrc,children,page=None,frm=None,mq=None,**kw):
    d={"id":id,"intention":"show","claim":claim,"method":method,
       "motivation":{"text":mot,"source":msrc,"quote":Q(mq) if mq else None},
       "children":children,"page":page,"from":frm or []}
    d.update(kw); return d
def B(s,n,m,r="direct"): return {"symbol":s,"name":n,"meaning":m,"relation":r}

S1=inf("S1","A machine with one fixed alphabet and a fixed number of tapes pays for moving data by scans, so a pass over $n$ bits costs $\\Theta(n)$.",
 "A machine has one fixed finite alphabet and one fixed finite number of","multitape-model",["turing-tapes","big-o"])

S2=show("S2","Fixed linear exchange networks with $s<Wm$ give a recursion whose per-volume cost grows by a factor $s/W<m$ when the parameter is multiplied by $m$, hence cost $V\\cdot(\\text{parameter})^\\theta$ with $\\theta<1$.",
 "Build a fixed network on $W$ roles with frames, label its gates by nested subspaces of an $m$-dimensional space so that the number $s$ of smaller calls is below $Wm$, then solve the recursion.",
 "The power saving comes only from a strict rank deficit across the edges of the network, so the argument must construct the network and its labels before the recursion can be analysed.",
 "explicit",
 [inf("S2.1","With an invertible frame $D_v$ at each vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array.",
   "At each source, gate and sink $v$, assign an invertible $R$-linear operator","linear-network-frames",["matrices-and-linear-maps","diagonal-matrices"]),
  inf("S2.2","Labelling gates by subspaces built from three-element subsets makes adjacent edge operators nested, so the total number $s$ of smaller calls is less than $Wm$.",
   "The saving will come from keeping the total dimension lost on decreasing","subset-intersection-network",["linear-network-frames","vector-spaces-over-finite-fields","matrices-and-linear-maps"],
   salient="The total rank is strictly below the trivial bound $Wm$ (a small but strict deficit), and this strictness is what the whole power saving rests on."),
  inf("S2.3","A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$, so $s/W<m^\\tau$ with $\\tau<1$ and the cost is $V$ times a power of the parameter below $1$.",
   "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,")],
 page="recursive-power-saving",frm=["recurrences-and-divide-and-conquer","big-o","multitape-model"],
 mq="is the source of the power saving. The later tape and arithmetic",
 adds=[B("W","number of roles","the number of wires (roles) of the network, among which rows are distributed.","count"),
       B("m","label dimension","the dimension of the fixed space whose subspaces label the gates."),
       B("s","number of smaller calls","the total number of smaller calls over all edges of the network.","count")],
 salient="The saving is a power of the parameter, obtained from a strict inequality $s<Wm$ between two nearly equal quantities.")
# fix: adds must occur in claims below; S2 children use W? ensure below
S2["children"][2]["claim"]="A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ with $W$ roles and label dimension $m$, so $s/W<m^\\tau$ with $\\tau<1$ and the cost is $V$ times a power of the parameter below $1$."
S2["children"][1]["claim"]="Labelling gates by subspaces of an $m$-dimensional space built from three-element subsets makes adjacent edge operators nested, so the total number $s$ of smaller calls is less than $Wm$."

S3=show("S3","Two disjoint contiguous address fields of $u$ bits of an array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ with a fixed $\\tau<1$, exactly for arbitrary auxiliary values.",
 "Realise the bit network on tape: factor each edge operator into lower triangular shears performed in linear time, and apply the recursion with the rank saving; then remove width and row restrictions.",
 "Plain sorting of fields costs a full pass per level; computing XOR combinations through the saving network replaces most passes by smaller interchanges, which is where $\\tau<1$ comes from.",
 "recoverable",
 [inf("S3.1","A rational shear $(H,D)\\mapsto(H+AD,D)$ of rank $a$ is performed with $a$ interchanges of $b$-digit fields plus linear work, via lower triangular factors with reversed coordinate order, on $u$-digit fields.",
   "is the Bruhat factorization for arbitrary matrices, with coordinate order","lower-triangular-shear",["matrices-and-linear-maps","permutations","multitape-model"]),
  inf("S3.2","The interchange of two $u$-bit chunks $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$ is done for arbitrary widths $u$ in $O(Vu^\\tau)$ steps.",
   "There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape")],
 page="chunk-interchange",frm=["recursive-power-saving","subset-intersection-network","linear-network-frames","multitape-model"],
 adds=[B("u","chunk width","the number of bits (digits) in each of the two interchanged address chunks.","count")],
 salient="The final effect is an exact permutation, although intermediate steps form XOR combinations of data, and it is exact for arbitrary auxiliary initial values.")

S4=show("S4","A butterfly layer $H_0$ on the same bit of $d$ address chunks of a polynomial array of volume $V$ costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$, instead of $d$ full passes.",
 "Apply the complex network to a tensor product of an auxiliary kernel using phase frames, bound the exact dyadic intermediate values, then convert to $H_0$ with a single truncation.",
 "Separate butterfly factors would need $D$ whole-array passes; the same rank-saving recursion over selected bits gives a power saving in the number of chunks.",
 "explicit",
 [inf("S4.1","The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied coefficientwise to selected bits of many address chunks, as a tensor product over $d$ chunks.",
   "of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits, acting","butterfly-h0",["fast-fourier-transform","polynomials","complex-numbers"]),
  inf("S4.2","Diagonal phase frames express a tensor product of the auxiliary kernel $C$ on many selected bits via smaller groups of bits separated by binary changes of basis done by moving whole chunks.",
   "We first construct tensor products of the auxiliary two-point kernel","phase-frames",["linear-network-frames","diagonal-matrices","butterfly-h0","chunk-interchange"]),
  inf("S4.3","All intermediate values are exact Gaussian dyadics, and the layer is evaluated exactly before one truncation.",
   "call. Finally, we bound the intermediate dyadic values and convert the","gaussian-dyadics",["fixed-point-precision"]),
  inf("S4.4","The layer over $d$ chunks costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
   "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,")],
 page="fast-butterfly-layer",frm=["recursive-power-saving","chunk-interchange","ring-y-r","fixed-point-precision"],
 mq="whereas separate butterfly factors",
 adds=[B("d","number of chunks","the number of equal-width address chunks (selected axes) on which the layer acts at once.","count")],
 salient="The cost exponent $\\lambda'$ is below $1$ uniformly in the number of chunks, versus linear cost for separate factors.")

S6=show("S6","Two polynomials in the ring modulo $y^r+1$ with disk coefficients are multiplied exactly in $O(rp\\log(rp))$ time.",
 "Pack signed coefficients into one integer (Kronecker substitution) and call the established integer multiplier as an ordinary subroutine.",
 "A polynomial product is an integer product after packing, so the known $O(N\\log N)$ multiplier handles it; being short records of $O(rp)$ bits, its cost is acceptable.",
 "recoverable",
 [inf("S6.1","Signed coefficients including negative ones are packed into one integer so that the polynomial product becomes an integer product.",
   "reduction is a signed form of Kronecker substitution; compare","kronecker-packing",["polynomials","binary-representation-and-bit-operations"])],
 page="hvdh-multiplier",frm=["polynomials"])
# S6 should have a hvdh-first quote; put as first child? order: hvdh text 3211 before 3217
S6["children"].insert(0,None)
S6["children"]=[inf("S6.1","Signed coefficients including negative ones are packed into one integer so that the polynomial product becomes an integer product.",
   "reduction is a signed form of Kronecker substitution; compare","kronecker-packing",["polynomials","binary-representation-and-bit-operations"])]
S6["children"].insert(0,None); S6["children"].pop(0)
# Use hvdh intro as the node's own motivation; add final infer
S6["children"].append(inf("S6.2","Both inputs are packed, multiplied by the Harvey--van der Hoeven multiplier, and unpacked to give the exact product and the rounded $fg/r$.",
   "One can compute the exact Gaussian integer"))
S6["motivation"]["quote"]=Q("To multiply the polynomial records, we use the fixed-tape integer")
S6["motivation"]["source"]="explicit"

S5=show("S5","Convolution over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ with $r$ coefficients per record is computed with synthetic transforms laid out on tape, a pointwise product and the opposite transform, with the stored frequency order retained.",
 "Use polynomial roots of unity $y^{2r/t}$ so the transforms are signed shifts and butterflies, arrange tape layout so the parallel layers apply, then multiply pointwise by exact ring products.",
 "Roots of unity inside the ring act as signed shifts, which makes each transform level a butterfly layer that the fast simultaneous layer accelerates.",
 "explicit",
 [inf("S5.1","The ring of polynomials modulo $y^r+1$ with $r$ coefficients has powers of $y$ as roots of unity, and multiplication by $y^a$ is a signed cyclic shift of the coefficients.",
   "\\mathcal R_r=\\mathbb C[y]/(y^r+1),\\qquad","ring-y-r",["polynomials","complex-numbers","modular-arithmetic","norms-and-triangle-inequality"]),
  inf("S5.2","With $\\omega_t=y^{2r/t}$ the synthetic transforms are computed by radix-two butterflies and the frequency order is retained through the pointwise product.",
   "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.","synthetic-transform",["ring-y-r","dft-convolution","fast-fourier-transform"]),
  inf("S5.3","The selected bits of the participating axes are placed at a common offset in consecutive chunks so that the parallel layers apply, and the layout cost is included.",
   "we must place the selected bits of the participating axes at a common"),
  S6,
  inf("S5.4","Convolution on the retained transform layout is approximated with the stated error by the two forward transforms, the pointwise ring product and the opposite transform.",
   "$\\mathcal M_r$ on disk grid operands has an approximation with error")],
 page="transform-layout",frm=["ring-y-r","dft-convolution","fast-butterfly-layer","chunk-interchange","synthetic-transform"],
 mq="The work here is to apply the simultaneous layers on a suitable tape",
 adds=[B("r","record length","the number of complex coefficients in a polynomial record, a power of two.","count")])
S5["motivation"]["quote"]=None
S5["motivation"]["source"]="recoverable"

S7=show("S7","A Fourier transform of coprime length is expressed through a power-of-two tensor transform by Gaussian resampling, with the permutations retained and the middle transform turned into cyclic convolution.",
 "Use Harvey--van der Hoeven resampling, keeping source and target permutations inside the transform formula, apply it line by line over many coordinates, and rewrite the middle transform by a chirp identity.",
 "The needed lengths are pairwise coprime, but the synthetic transforms need powers of two, and sorting twice per coordinate would cost too much.",
 "explicit",
 [inf("S7.1","The source and target coordinate permutations are kept inside the transform formula instead of being sorted, so they cancel across the forward transforms, product and inverse.",
   "We retain both permutations in the transform formula and","retained-permutations",["permutations","fixed-point-precision"]),
  inf("S7.2","One-dimensional resampling maps are applied line by line over many coordinates, with axis movement by chunk interchange.",
   "For the tensor product, apply the one-dimensional maps to one coordinate","tensor-resampling",["chunk-interchange","tuples-products-of-sets-and-mixed-radix-indexing"]),
  inf("S7.3","Bluestein's chirp identity writes the middle transform as a cyclic convolution between pointwise phase multiplications, without applying the target permutation separately.",
   "computed from a cyclic convolution and two pointwise phase","bluestein-chirp",["dft-convolution","euler-s-formula-and-exponentials-of-complex-numbers"])],
 page="gaussian-resampling",frm=["dft-convolution","fixed-point-precision","gaussian-function-and-gaussian-sums","hvdh-multiplier"],
 mq="The transform lengths needed for the integer product are pairwise coprime,")
S7["motivation"]["quote"]=Q("The transform lengths needed for the integer product are pairwise coprime,")

S8=show("S8","The integer product is recovered exactly from the ring convolution with a compatible parameter choice, and the total cost fits $O(n(\\lg n)^{1-\\kappa})$.",
 "Fix the parameters, map the radix-digit coefficients to prime axes, twist to the polynomial ring, run the algorithm, bound precision, and sum the cost table.",
 "Every earlier procedure comes with its own cost and error; only a single compatible choice of parameters and an explicit total accounting yields the final exponent.",
 "recoverable",
 [inf("S8.1","A fixed rational choice of $\\tau,\\lambda',\\epsilon,\\kappa=2^{-182}$ and the other constants makes all layer conditions hold.",
   "The two motif exponents were fixed in \\eqref{eq:explicit-motif-exponents}.","parameter-choice",["floor-ceiling-rounding-and-logarithms"]),
  inf("S8.2","A Chinese-remainder address map places the coefficient list on a product of pairwise coprime prime cyclic axes and preserves convolution.",
   "The power-of-two complex convolution used in the chirp identity is".replace("The power-of-two complex convolution used in the chirp identity is","Let $s_1,\\ldots,s_d$ be the pairwise coprime"),"crt-prime-axes",["modular-arithmetic","greatest-common-divisor-and-coprimality","cyclic-groups-and-direct-products"]),
  inf("S8.3","A phase twist $x_d\\mapsto\\zeta y$ converts the last cyclic coordinate into a polynomial modulo $y^r+1$ whose negative wrap gives the original cyclic wrap.",
   "The power-of-two complex convolution used in the chirp identity is","phase-twist",["ring-y-r","dft-convolution","euler-s-formula-and-exponentials-of-complex-numbers"]),
  inf("S8.4","Writing both integers in a radix turns their product into a convolution of short integer coefficient lists, followed by carry propagation.",
   "The source-transform procedures now supply the three transforms needed","radix-digit-convolution",["schoolbook-multiplication-and-carries","binary-representation-and-bit-operations"]),
  inf("S8.5","Values are stored on a $2^{-p}$ grid with truncation errors that add under composition, and a final coefficient error below $1/2$ lets rounding and carries recover the exact product.",
   "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this","fixed-point-precision",["real-and-complex-number-approximation","norms-and-triangle-inequality","floor-ceiling-rounding-and-logarithms"]),
  inf("S8.6","All terms of the cost table, divided by the volume $V=\\Theta(n)$, fit $O((\\lg n)^{1-\\kappa})$.",
   "For the cost calculation put $V=Tp=\\Theta(n)$. The fixed-width coefficient")],
 page=None,
 mq="A compatible choice of rational")
S8["motivation"]["quote"]=None

root=show("R","Two $n$-bit integers are multiplied exactly by a deterministic fixed-tape machine in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
 "Reduce the product to convolution through a chain of exact changes of representation, supply the movement and butterfly cost savings by two fast tape procedures, and assemble parameters, precision and cost.",
 "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels costs $\\Theta(n\\log n)$, so both address movement and arithmetic must be sped up before the transform chain is used.",
 "explicit",
 [S1,S2,S3,S4,S5,S7,S8],page="main-theorem",frm=["conjecture"],
 salient="The saving is a power of the logarithm, $(\\lg n)^{-\\kappa}$ with a tiny $\\kappa=2^{-182}$, below the long-conjectured $n\\log n$.")
root["motivation"]["quote"]=Q("We therefore need savings in both movement and arithmetic. Two tape")
json.dump({"root":root},open(P+"exegenius/tasks/0003-argument.answer.json","w"),indent=1)

# check order
pos=0
def walk(n):
    global pos
    if n["intention"]=="infer":
        q=n["quote"]["quote"]; i=src.find(q,pos)
        j=src.find(q)
        print(n["id"],"OK" if i>=0 else "MISSING/ORDER", j)
        if i>=0: pos=i+len(q)
    for c in n.get("children",[]): walk(c)
walk(root)
for n in [root]: pass
