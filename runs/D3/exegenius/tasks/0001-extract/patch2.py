import json
f="0001-extract.answer.json"
d=json.load(open(f))
ids={c["id"]:c for c in d["concepts"]}
def add(id,name,gloss,req,ev):
    d["concepts"].append(dict(id=id,name=name,aliases=[],gloss=gloss,requires=req,known=False,evidence=[{"source":"paper","quote":q} for q in ev]))
add("elementary-streams","Elementary stream operations and controlled shifts","Linear-time scans on tapes: digit permutations, moves, and controlled shifts/fixed rational scalings of a field using earlier control fields; arrays stored in lexicographic order with a self-delimiting integer header code.",["multitape-model"],
 ["\\begin{lemma}[Elementary stream operations]","\\begin{lemma}[Controlled shifts and fixed rational scalings]","\\Gamma(v)=0^{b_v-1}\\operatorname{bin}_{b_v}(v)"])
add("scalar-motifs","Scalar gates with restored scratch wires","In the network, a forward invocation adds x_S to y_S for arbitrary scratch contents; three stages exchange the banks (X,Y) to (−Y,X) and restore all auxiliary values.",["finite-network-subspaces"],
 ["a forward\ninvocation changes $y_S$ to $y_S+x_S$ and leaves every other value\nunchanged."])
add("motif-residuals","Rank budget of the network labels","Edges join comparable subspace labels; total dimension change over edges equals Wm−2N+2L, giving the strict rank deficit s<Wm.",["scalar-motifs"],
 ["Every edge joins comparable nondegenerate labels.","\\sum_{e}\\bigl|\\dim U_{\\mathrm{head}(e)}-"])
add("motif-interfaces","Bit and complex network interfaces","The bit network (XOR gates, rational matrices) realises an address permutation with rank sum small; the complex network realises phase frames made of translation kernels and yields the H0 layer.",["motif-residuals","linear-network-frames"],
 ["\\begin{proposition}\\label{prop:bit-motif-interface}","\\begin{proposition}\\label{prop:complex-motif-interface}","The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,"])
add("matrix-shear","Lower triangular factorization and matrix shear","Any rational matrix of rank a factors as E1·Π·E2 with lower triangular E1,E2, so the shear (H,D)↦(H+AD,D) needs exactly a field interchanges plus linear work.",["elementary-streams","address-interchange-prelim"] if False else ["elementary-streams"],
 ["\\begin{lemma}[Lower triangular factorization]","\\begin{lemma}[The cost of a rational matrix shear]","can be performed with exactly $a$ interchanges of pairs of $b$-digit"])
add("chunk-swap","Power-width and arbitrary-width chunk interchange","Recurrence on parameter e=m^k gives chunk interchange in O(V e^τ); then arbitrary width u by decomposition.",["matrix-shear","motif-interfaces","recursive-power-saving"],
 ["\\begin{proposition}[Power-width interchange with rows]","\\begin{lemma}[Arbitrary-width interchange]","There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape"])
add("packed-selected-bit-addition","Packed selected-bit addition on grouped rectangles","XORs selected bits at positions ρ+iK of several chunks simultaneously by packing, repairing a small exceptional set of addresses.",["elementary-streams"],
 ["\\begin{lemma}[Packed selected-bit addition on one rectangle]","\\begin{definition}[Grouped packed stream]","\\begin{lemma}[Packed selected-bit addition for grouped rectangles]"])
add("transform-layout-cost","Synthetic transform layout and cost","Layout of the synthetic transform over R_r with truncation Q_p, contractions, and stored frequency order retained through pointwise product; cost via simultaneous layers.",["fast-butterfly-layer","synthetic-transforms","address-interchange"],
 ["\\begin{lemma}[Transform layout and cost]","\\begin{proposition}[Convolution from the retained transform layout]"])
add("tensor-resampling","Tensor resampling with retained permutations","Gaussian resampling lines combined over d axes, keeping source and target permutations inside the transform identity.",["gaussian-resampling"],
 ["\\begin{lemma}[Tensor interface]"])
add("parameter-choice","Fixed rational parameter choice and cost table","Choice τ=σ=1−2^{−50}, c, λ′ etc. and a cost table whose rows each fit O(p^{1−ε′}) after dividing by volume.",["transform-layout-cost","chunk-swap"],
 ["\\subsection{A fixed rational choice}","\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},"])
# rewire
ids={c["id"]:c for c in d["concepts"]}
ids["address-interchange"]["requires"]+= ["chunk-swap"]
ids["fast-butterfly-layer"]["requires"]+= ["packed-selected-bit-addition","motif-interfaces"]
ids["gaussian-resampling"]["requires"]+= ["tensor-resampling"] if False else []
ids["main-theorem"]["requires"]+= ["tensor-resampling","parameter-choice","transform-layout-cost","elementary-streams"]
ids["precision-exact-recovery"]["evidence"].append({"source":"paper","quote":"\\subsubsection{Scales and disk margins}"})
json.dump(d,open(f,"w"),indent=1)
