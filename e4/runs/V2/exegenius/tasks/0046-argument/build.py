import json, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V2"
SRC = open(BASE + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def inf(id, claim, q, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(q), "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def show(id, claim, method, mot_text, mot_src, mot_q, children, page=None, frm=None, salient=None, adds=None):
    m = {"text": mot_text, "source": mot_src}
    if mot_q: m["quote"] = ev(mot_q)
    n = {"id": id, "intention": "show", "claim": claim, "method": method, "motivation": m,
         "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def add(sym, name, meaning, rel="direct"):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

# ---------------- R1 toolkit
S1 = show("S1", "Linear-time stream scans and controlled cyclic shifts are available on a fixed number of tapes.",
  "collect the elementary array scans and the ordered affine updates that every later procedure calls",
  "Interchanging fields whose lengths grow is not a bounded number of scans, so the paper first fixes which operations are linear in the volume, with counters and rewinds charged.",
  "explicit", "the elementary scans it uses.",
  [
   inf("S1.1", "Fixed digit permutations, digit moves, splitting into aligned streams, pointwise maps, merging and cyclic row splitting each take $O(V)$ steps on an array of volume $V$.",
       "The bounds include shape preparation, counter initialization and resets,",
       page="elementary-streams",
       frm=["turing-machine", "binary-counters-and-finite-state-bookkeeping", "sets-functions-bijections-and-permutations"]),
   inf("S1.2", "Updating a later address field $y \\mapsto y + a(\\text{controls}) \\bmod q^b$ and multiplying by a fixed rational unit mod $q^b$ cost $O(V)$.",
       " y\\longmapsto y+a(\\text{controls})\\pmod Q",
       page="controlled-cyclic-shifts",
       frm=["elementary-streams", "modular-arithmetic-and-congruences", "greatest-common-divisor-and-the-euclidean-algorithm", "stacks-and-queues"]),
  ],
  frm=["turing-machine", "binary-counters-and-finite-state-bookkeeping"])

# ---------------- R2 networks
S2 = show("S2", "There are fixed linear exchange networks (a bit network and a complex network) with $W$ wires, a label space of dimension $m$ and a total edge rank $s<Wm$.",
  "build a three-stage exchange of two banks with restored scratch wires, then attach nested subspace labels to gates and count the dimension changes on edges",
  "The recursion only saves a power if the number of smaller calls per wire is below the dimension growth factor, so the construction is organized around making the total edge rank $s$ fall short of $Wm$.",
  "explicit", "number $s$ of smaller calls satisfies $s<Wm$.",
  [
   inf("S2.1", "A fixed network of copy, gather, scatter and side-injection gates sends $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ in three stages and restores every scratch wire for arbitrary initial values.",
       "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$.",
       page="scalar-exchange-network",
       frm=["bitwise-xor", "vectors-and-matrices-over-the-two-element-field", "binomial-coefficients", "sets-functions-bijections-and-permutations"],
       salient="The cancellation of the scratch wires does not depend on their initial contents: the two net contributions from the central and side wires add up to exactly the identity update $y\\gets y+x$."),
   inf("S2.2", "If every vertex carries an invertible operator $D_v$ (a frame) on its wire's array and gates act pointwise, the frames commute with the gates, so a route applies only the endpoint operator $D_{\\mathrm{sink}}D_{\\mathrm{source}}^{-1}$.",
       "Thus the common frame commutes with the pointwise gate, and",
       page="frames",
       frm=["scalar-exchange-network", "linear-algebra-basics", "matrices-matrix-products-and-inverses", "sets-functions-bijections-and-permutations"]),
   show("S2.3", "Nested nondegenerate subspaces of an $m$-dimensional space can be attached to gates and terminals so that the total dimension change over all edges is $Wm-2N+2L$ with $L<N/2$, hence $<Wm$ after the source ranks are added.",
        "give every vertex a subspace built from triple indicator vectors, check adjacent labels are nested, and count the dimension of each orthogonal residual",
        "An edge between nested labels costs exactly the dimension of the residual between them, so choosing the labels cleverly controls the total cost.",
        "explicit", "The saving will come from keeping the total dimension lost on decreasing",
        [
         inf("S2.3.1", "Every edge joins comparable nondegenerate labels, so each edge cost is the dimension of an orthogonal residual.",
             "Every edge joins comparable nondegenerate labels.",
             frm=["linear-algebra-basics", "tensor-product"]),
         inf("S2.3.2", "Label dimension never decreases along an edge except on the central wires between times 3 and 4, where the loss is exactly $h$.",
             "Label dimension is nondecreasing along every edge except center $3\\to4$, which removes",
             frm=["linear-algebra-basics", "tensor-product"]),
         inf("S2.3.3", "The signed dimension changes sum to $Wm-2N$, so the sum of absolute changes is $Wm-2N+2L$ where $L$ is the total loss on decreasing edges.",
             "changes by absolute changes adds $2L$.",
             frm=["linear-algebra-basics"]),
         inf("S2.3.4", "The loss ratio satisfies $L/N<1/2$ in both constructions, so after charging $N$ extra ranks for the sources there is still a strict deficit.",
             "In particular, both are smaller than $1/2$.",
             frm=["binomial-coefficients"]),
        ],
        page="subspace-labels-rank-saving",
        frm=["linear-algebra-basics", "tensor-product", "frames", "scalar-exchange-network", "binomial-coefficients", "vectors-and-matrices-over-the-two-element-field"],
        salient="The total rank $s$ is strictly smaller than $Wm$ although every one of the $W$ wires is moved from the zero space to the full space: only about $N$ source ranks and $2L$ lost dimensions are charged, and $L/N=100/539<1/2$.",
        adds=[]),
   inf("S2.4", "Assigning the projections $P_U$ to gates gives rational matrices $M_v$ whose endpoint differences are the identity $I_m$, and whose edge ranks sum to $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$.",
       "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
       page="rational-matrix-interface",
       frm=["subspace-labels-rank-saving", "frames", "linear-algebra-basics", "modular-arithmetic-and-congruences"]),
   inf("S2.5", "With binary labels and phase frames $\\mathcal C_U$, every edge change is a product of $C$-type translation kernels, one per residual basis vector, and the whole complex network realizes $C^{\\otimes m}$ on every role with $s_{\\rm c}<W_{\\rm c}m$ kernels.",
       "Thus each residual vector contributes one factor acting on all $k$",
       page="phase-frame-interface",
       frm=["phase-kernel", "tensor-product", "subspace-labels-rank-saving", "frames", "complex-numbers", "vectors-and-matrices-over-the-two-element-field"]),
   inf("S2.6", "The fixed rational exponent $\\tau=\\sigma=1-2^{-50}$ satisfies $s/W<m^{\\tau}$ for both networks.",
       " \\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,",
       frm=["rational-matrix-interface", "logarithms-floors-and-ceilings"]),
  ],
  frm=["linear-algebra-basics", "tensor-product", "matrices-matrix-products-and-inverses"],
  adds=[add("W", "wire count", "the number of wires of the fixed network, scratch wires included", "count"),
        add("m", "label dimension", "the dimension of the space of subspace labels, equal to the number of address fields per chunk", "count"),
        add("s", "smaller calls", "the sum over all edges of the rank of the edge change, i.e. the number of smaller calls the network needs", "count"),
        add("N", "bank size", "the number of data wires in each of the two banks being exchanged", "count"),
        add("L", "lost dimension", "the total dimension lost on the decreasing edges of the labelled network", "count")])

# ---------------- R3 interchange
S3_3 = show("S3.3", "Two disjoint chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^{\\tau})$ time when the row field has length divisible by $W^k$.",
  "split rows among the $W$ roles, run the exchange network with address-shear frames so each edge becomes recursive interchanges of chunks of width $e/m$ on volume $V/W$, and solve the resulting recurrence",
  "Each of the $s$ smaller calls runs on a stream carrying only $1/W$ of the volume, so one level multiplies the normalized cost by $s/W$, which is below the width factor $m$; this is where the saving enters.",
  "explicit", "$m$, the resulting recurrence saves a power of the chunk width.",
  [
   inf("S3.3.1", "Splitting whole rows cyclically into $W$ role streams gives streams of identical shape, each of volume $V/W$.",
       "Split whole rows cyclically into $W$ role streams within each prefix",
       frm=["elementary-streams"]),
   inf("S3.3.2", "On every circuit edge $e$ the shear $\\Phi_{A_e}$ is applied to that role stream by recursively interchanging each pivot pair of $b$-digit fields, while gates act pointwise.",
       "$\\Phi_{A_e}$ to that role stream; implement it by",
       frm=["address-shear-cost", "frames"]),
   inf("S3.3.3", "By the frame identity, the frames cancel along each route and every role receives the single shear $H\\leftarrow H+D$, scratch roles included.",
       "is $H\\leftarrow H+D$ on every original row, including rows assigned",
       frm=["frames", "rational-matrix-interface", "scalar-exchange-network"]),
   inf("S3.3.4", "Three shears $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange the chunks, and only the middle one needs the circuit.",
       " D\\leftarrow D-H,\\qquad H\\leftarrow H+D,\\qquad D\\leftarrow H-D,",
       frm=["controlled-cyclic-shifts"]),
   inf("S3.3.5", "The number of recursive calls at a node is exactly $s$, each on volume $V/W$, so the normalized cost satisfies $F_0=O(1)$, $F_k\\le (s/W)F_{k-1}+O(1)$.",
       " F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
       frm=["recurrences-induction-and-geometric-sums"],
       salient="The recursion factor $s/W$ is a constant below $m^{\\tau}$ with $\\tau<1$, so after $k=\\log_m e$ levels the cost is $e^{\\tau}$ rather than the $e$ of naive digit-by-digit exchange."),
   inf("S3.3.6", "Since $s/W<m^\\tau$, the geometric sum $\\sum_{j\\le k}(s/W)^j$ is $O(m^{k\\tau})$, hence $F_k=O(e^{\\tau})$.",
       "Hence $F_k=O(e^\\tau)$.",
       frm=["recurrences-induction-and-geometric-sums", "big-o"]),
   inf("S3.3.7", "Recursive calls on the $W$ role streams run on a fixed set of tapes by parking the inactive streams on a stack, with only $O(V)$ extra cost per node.",
       "Before a recursive call, append the $W-1$ inactive role streams to the",
       page="fixed-tape-recursion-schedule",
       frm=["stacks-and-queues", "turing-machine", "elementary-streams"]),
  ],
  page="power-width-interchange",
  frm=["rational-matrix-interface", "address-shear-cost", "frames", "fixed-tape-recursion-schedule", "elementary-streams", "recurrences-induction-and-geometric-sums", "scalar-exchange-network"],
  salient="The exponent $\\tau=1-2^{-50}$ is strictly below 1 even though the network has an enormous number of wires: the saving is only the tiny relative deficit $(Wm-s)/(Wm)$, and it is the same factor at every level of the recursion.",
  adds=[add("e", "chunk width", "the number of radix digits in each of the two chunks, a power $m^k$ of the label dimension", "count")])

S3 = show("S3", "Exchanging two disjoint equal-width address chunks of $u$ bits, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, takes $O(Vu^{\\tau})$ time for any shape and any $u$, with $\\tau<1$.",
  "factor the needed address shears through lower-triangular controlled shifts and a few pivot interchanges, run the power-width recursion, and then lift to arbitrary widths by supplying rows from high digits and splitting the width in base $m$",
  "The recursive network needs many rows and a width that is a power of $m$, so the general interchange must be reduced to that special case.",
  "explicit", "Rows for a general array can be supplied by a few of its own high digits.",
  [
   inf("S3.1", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
       "permutation matrix has exactly $a$ ones.",
       page="lower-triangular-factorization",
       frm=["matrices-matrix-products-and-inverses", "gaussian-elimination-and-row-operations", "linear-algebra-basics"]),
   inf("S3.2", "The address shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b$ with $\\operatorname{rank}A=a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
       "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,",
       page="address-shear-cost",
       frm=["lower-triangular-factorization", "controlled-cyclic-shifts", "elementary-streams", "modular-arithmetic-and-congruences"]),
   S3_3,
   inf("S3.4", "Peeling the top $\\rho$ digits of each chunk as a row field and padding to a multiple of $W^k$ supplies enough rows at cost $O(V\\rho)$.",
       "Write each chunk as its top $\\rho$ digits followed by its remaining",
       frm=["elementary-streams", "logarithms-floors-and-ceilings"]),
   inf("S3.5", "The remaining width is written in base $m$ as $e-\\rho=\\sum_j a_jm^j$ and split into $a_j$ pieces of width $m^j$ that are interchanged by power-width calls.",
       " e-\\rho=\\sum_{j=0}^{k} a_jm^j,\\qquad 0\\le a_j<m.",
       frm=["binary-representation-of-integers", "sets-functions-bijections-and-permutations"]),
   inf("S3.6", "The calls sum to $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^{\\tau})$, so the full interchange costs $O(Vu^{\\tau})$.",
       " O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau).",
       frm=["recurrences-induction-and-geometric-sums"]),
  ],
  page="chunk-interchange",
  frm=["elementary-streams", "sets-functions-bijections-and-permutations", "recurrences-induction-and-geometric-sums"],
  adds=[add("u", "chunk bits", "the number of bits in each of the two address chunks being exchanged", "count"),
        add("V", "bit volume", "the number of stored data bits of the array being rearranged", "count"),
        add("\\tau", "interchange exponent", "a fixed constant below 1 (here $1-2^{-50}$) such that interchanging chunks of $u$ bits costs $O(Vu^{\\tau})$")])

# ---------------- R4 butterfly
S4_3 = show("S4.3", "Adding selected bits of $f$ chunks of one address field into another, $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$, while restoring a third chunk, costs $O(V(L^{\\tau}+1))$ in the paper's parameter range.",
  "do the XORs as packed cyclic shifts of whole chunks, which are correct away from carry-prone guard values, and repair the few explicitly identified bad addresses by sorting",
  "A shift of a whole chunk adds to every selected bit position at once, but carries between packed segments break it exactly when a segment is near its extremes, which only a tiny fraction of addresses are.",
  "recoverable", None,
  [
   inf("S4.3.1", "Eight conditional parity-controlled shifts flip the parity of $u$ exactly when the control is 1 and restore the auxiliary $w$.",
       "u+c(1-2(u\\bmod2)),\\ w\\bigr)",
       frm=["modular-arithmetic-and-congruences", "bitwise-xor"]),
   inf("S4.3.2", "The packed shifts agree with the ideal XOR map except on a set $\\mathcal B$ of addresses whose guard values fail, with $|\\mathcal B|\\le\\delta_{\\rm bad}M$ and $\\delta_{\\rm bad}$ exponentially small in the chunk width.",
       " |\\mathcal B|\\le\\delta_{\\rm bad}M.",
       frm=["binary-representation-of-integers"]),
   inf("S4.3.3", "The records at bad addresses are extracted, sorted by destination rank with stable radix sort and reinserted, which implements the ideal map everywhere.",
       "This implements $T_0$ everywhere.",
       frm=["sorting-and-radix-sort", "binary-counters-and-finite-state-bookkeeping"]),
  ],
  page="packed-selected-bit-addition",
  frm=["chunk-interchange", "controlled-cyclic-shifts", "elementary-streams", "bitwise-xor", "sorting-and-radix-sort"])

S4 = show("S4", "One normalized butterfly layer $H_0=\\tfrac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ applied simultaneously to the same bit of $D\\le d$ address chunks of a polynomial-record array costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$.",
  "turn $H_0^{\\otimes D}$ into a phase-conjugated $C^{\\otimes D}$, evaluate that by the complex network recursively with packed binary basis changes, and bound the exact dyadic arithmetic before one final truncation",
  "Doing the butterflies one chunk at a time would need $D$ whole-array passes; the network recursion handles all selected bits together at the price of $s/W$ per level.",
  "explicit", "factors would require $D$ whole-array passes.",
  [
   inf("S4.1", "The complex network with column frames gives $C^{\\otimes e}$ on a group of $e=mf$ selected bits using exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ bits of one slot.",
       "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
       frm=["phase-frame-interface", "phase-kernel", "tensor-product"]),
   inf("S4.2", "The normalized layer equals a diagonal phase, the $C$ layer, and another phase: $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$.",
       "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",
       frm=["phase-kernel", "complex-numbers"]),
   S4_3,
   inf("S4.4", "The normalized cost $F(e)$ of $C^{\\otimes e}$ satisfies $F(e)\\le (s/W)F(e/m)+O((eK)^{\\tau}+1)$, with leaves handled one kernel at a time.",
       "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),",
       frm=["recurrences-induction-and-geometric-sums"],
       salient="The same factor $s/W<m^{\\sigma}$ appears as in the bit network: the layer costs a power $d^{\\lambda'}$ with $\\lambda'<1$ per unit volume instead of $d$."),
   inf("S4.5", "Since $s/W<m^\\lambda$, internal costs sum geometrically to $O(e^\\lambda)$, and with the base-$m$ partition of the $D$ chunks the whole layer costs $O(d^{\\lambda'})$ per unit volume.",
       "=O(d^{\\lambda'})",
       frm=["recurrences-induction-and-geometric-sums", "big-o"]),
   inf("S4.6", "All intermediate values are exact Gaussian dyadics whose size is bounded by guard widths $\\Delta=\\lceil C_0d^{C_1}\\rceil=o(p)$, so the whole layer is evaluated exactly before one truncation.",
       "A(e)\\le 8dB^{k+1}\\le8B^2d^{\\nu+1}.",
       page="guard-width-exactness",
       frm=["fixed-point-disk-arithmetic", "complex-numbers", "phase-frame-interface"]),
   inf("S4.7", "Truncating toward zero once keeps the result in the disk with error below $\\sqrt2\\,2^{-p}$, because $H_0$ has row sums of modulus one.",
       "error less than $\\sqrt2\\,2^{-p}$: truncation cannot increase the",
       frm=["fixed-point-disk-arithmetic", "vector-norms-and-the-triangle-inequality"]),
  ],
  page="simultaneous-butterfly-layer",
  frm=["phase-frame-interface", "packed-selected-bit-addition", "chunk-interchange", "guard-width-exactness", "fixed-point-disk-arithmetic", "fft-butterfly", "phase-kernel"],
  salient="The layer of $D$ simultaneous butterflies costs only $d^{\\lambda'}$ per unit volume with $\\lambda'<1$ (here $1-2^{-54}$) rather than the $D\\le d$ passes of separate butterflies, for the same reason as the interchange: $s/W<m^{\\sigma}$.",
  adds=[add("D", "selected chunks", "the number of consecutive address chunks on which one common bit position is butterflied, at most $d$", "count"),
        add("K", "chunk width", "the number of bits in each address chunk, $\\lfloor d^{c}\\rfloor$", "count"),
        add("\\lambda'", "layer exponent", "a fixed constant below 1 such that a simultaneous layer costs $O(Vd^{\\lambda'})$")])

# ---------------- R5 synthetic convolution
S5_2 = show("S5.2", "Placing the selected bits of all axes at a common offset of consecutive $K$-bit chunks lets each transform round be one simultaneous layer, for total cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
  "move the leading address slots of the axes to a prefix, reorder the remaining chunks round by round with chunk exchanges, and charge each round to the simultaneous layer",
  "The layer procedure only applies when the participating bits sit at the same offset in consecutive chunks, so the stored layout must be rearranged first.",
  "explicit", "we must place the selected bits of the participating axes at a common",
  [
   inf("S5.2.1", "Moving the at most $D(b+1)=O(dK)$ listed slots to a prefix costs $O(TpdK)$, and those prefix rounds are done by individual butterflies.",
       "listed slots, so the moves cost $O(TpdK)$.",
       frm=["elementary-streams"]),
   inf("S5.2.2", "The remaining $q$ chunks of each axis are regrouped by at most $Dq-1$ exchanges of width-$K$ chunks, costing $O(Tp\\,pK^{\\tau-1})$.",
       "=O\\bigl(Tp\\,pK^{\\tau-1}\\bigr).",
       frm=["chunk-interchange"]),
   inf("S5.2.3", "The $\\ell$ rounds of simultaneous layers cost $O(Tpd^{\\lambda'})$ each, $O(Tp\\ell d^{\\lambda'})$ in total.",
       "$O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
       frm=["simultaneous-butterfly-layer"]),
  ],
  page="synthetic-transform-layout",
  frm=["synthetic-transform", "simultaneous-butterfly-layer", "chunk-interchange", "multidimensional-transform", "elementary-streams"])

S5 = show("S5", "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ can be computed from two forward synthetic transforms, a pointwise ring product and the opposite transform, with error $<\\sqrt2\\,M(3\\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
  "transform both operands with the synthetic transform, multiply pointwise by signed packing in the stored order, and apply the opposite transform, which consumes that order",
  "A pointwise product commutes with the same record permutation on both operands, so the bit-reversed storage never has to be undone between the transforms.",
  "explicit", "forward outputs in their retained order and pass that order directly",
  [
   inf("S5.1", "The synthetic transform with roots $\\omega_t=y^{2r/t}$, computed by butterflies and signed shifts, leaves entry $j$ in slot $\\operatorname{rev}_a(j)$, and the opposite transform consumes that bit-reversed order.",
       "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
       page="synthetic-transform",
       frm=["polynomial-ring-mod", "dft", "fft-butterfly", "roots-of-unity", "cyclic-convolution", "multidimensional-transform"]),
   S5_2,
   inf("S5.3", "Evaluating at $B_0=2^{4p}$, multiplying the resulting integers with the established multiplier and extracting signed coefficients by centered residues multiplies two ring elements in $O(rp\\log(rp))$.",
       "pairs of absolute values using the established multiplier and restore",
       page="signed-packing",
       frm=["harvey-hoeven-multiplier", "polynomial-ring-mod", "two-s-complement-and-fixed-width-signed-integers", "polynomials"]),
   inf("S5.4", "Both forward transforms are retained in their common $LB$ order, multiplied pointwise, and fed to the opposite procedure, then scaled exactly by $M$.",
       "Perform both forward transforms and retain their common $LB$ order.",
       frm=["cyclic-convolution", "synthetic-transform-layout", "signed-packing", "synthetic-transform"]),
   inf("S5.5", "The three transform errors and the truncated product give a total error of $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
       "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$",
       frm=["vector-norms-and-the-triangle-inequality", "fixed-point-disk-arithmetic"]),
  ],
  page="synthetic-convolution",
  frm=["synthetic-transform", "synthetic-transform-layout", "signed-packing", "cyclic-convolution", "multidimensional-transform", "polynomial-ring-mod", "harvey-hoeven-multiplier"],
  adds=[add("\\ell", "log record length", "the base-2 logarithm of the record length $r$, which is the number of transform rounds")])

# ---------------- R6 resampling
S6_1 = show("S6.1", "A transform of coprime length $s_i<t_i$ per axis equals $2^{\\gamma}$ times a power-of-two transform sandwiched between Gaussian contractions: $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with the permutations $R,Q$ left in the identity.",
  "prove the one-dimensional identity $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ from Gaussian resampling, then tensor it over the axes",
  "The usual implementation sorts twice on every coordinate, which is too expensive; keeping the permutations inside the formula avoids executing them.",
  "explicit", "coordinate. We retain both permutations in the transform formula and",
  [
   inf("S6.1.1", "In one dimension, $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ with contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ computable to error $<p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$.",
       "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
       frm=["dft", "complex-numbers", "fixed-point-disk-arithmetic", "vector-norms-and-the-triangle-inequality"]),
   inf("S6.1.2", "Tensoring the one-dimensional identity over the $d$ axes gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, applied one line at a time.",
       "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,",
       frm=["tensor-product", "multidimensional-transform"]),
  ],
  page="gaussian-resampling",
  frm=["dft", "multidimensional-transform", "tensor-product", "fixed-point-disk-arithmetic", "vector-norms-and-the-triangle-inequality", "complex-numbers", "chunk-interchange"])

S6 = show("S6", "The source transform $RF_{\\boldsymbol s}$ on coprime axes, and the product of two such transforms, can be reduced to power-of-two transforms and cyclic convolution without executing the coordinate permutations.",
  "resample to power-of-two lengths, express the middle transform as a chirp convolution, and cancel the leftover source permutation across the two forward and one opposite transforms",
  "The synthetic transforms only handle power-of-two lengths whereas the digit convolution lives on pairwise coprime lengths, so the two shapes have to be connected.",
  "explicit", "whereas the synthetic transforms use powers of two. Gaussian resampling",
  [
   S6_1,
   inf("S6.2", "Bluestein's identity writes $QF_{\\boldsymbol t}u=\\overline a\\cdot (a*(\\overline a\\cdot u))/T$, so the permuted transform is a normalized cyclic convolution with the chirp $a$.",
       "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because",
       page="bluestein-chirp",
       frm=["dft", "cyclic-convolution", "multidimensional-transform", "complex-numbers", "gaussian-resampling"]),
   inf("S6.3", "Because $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$ and permutations commute with pointwise products, $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
       "$RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$",
       page="permutation-cancellation",
       frm=["cyclic-convolution", "dft", "modular-arithmetic-and-congruences", "gaussian-resampling"],
       salient="The source permutation $R$ never has to be executed: it cancels exactly across two forward transforms, a pointwise product and the opposite transform."),
  ],
  frm=["gaussian-resampling", "dft"],
  adds=[add("S", "prime axis product", "the product $\\prod_i s_i$ of the pairwise coprime source lengths, with $T/2<S<T$", "count")])

# ---------------- R7 algorithm
S7 = show("S7", "Multiplying $n$-bit integers is done by writing the operands as radix-$2^b$ digit lists on a padded prime-axis box, transforming, multiplying pointwise, transforming back, rescaling by $S$ and $2^{2b+4}$, undoing the address map, rounding and carrying.",
  "choose compatible parameters, place the digit convolution on distinct prime cyclic axes by a Chinese-remainder map, evaluate the transforms with resampling, chirps and a coefficient twist, and recover integer coefficients",
  "Each stage was proved for its own interface; the algorithm composes them in the order of the reduction pictured in the paper.",
  "explicit", "We now use the preceding algorithms to multiply two $n$-bit integers.",
  [
   inf("S7.1", "For input length $n$ take $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, power-of-two axis lengths $t_i\\in\\{r/2,r\\}$ and distinct odd primes $s_i$ just below $t_i$, so that $T/2<S<T$ and every resampling hypothesis holds.",
       "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
       page="parameter-choice",
       frm=["prime-numbers", "logarithms-floors-and-ceilings", "gaussian-resampling", "binary-representation-of-integers"]),
   inf("S7.2", "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an isomorphism turning one cyclic convolution of length $S$ into a $d$-dimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts.",
       "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
       page="crt-address-map",
       frm=["chinese-remainder-theorem", "controlled-cyclic-shifts", "chunk-interchange", "multiplication-by-convolution", "cyclic-convolution"]),
   inf("S7.3", "The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ turns the cyclic wrap of the last axis into the negative wrap of $\\mathbb C[y]/(y^r+1)$, so complex cyclic convolution is the synthetic convolution after twisting and untwisting.",
       "Untwisting therefore recovers the cyclic coefficient with the correct",
       page="coefficient-twist",
       frm=["polynomial-ring-mod", "roots-of-unity", "complex-numbers", "cyclic-convolution"]),
   inf("S7.4", "The computed source transform is the Gaussian expansion, the chirp convolution, the Gaussian compression and a scale by $2^{\\gamma}$, with exact counterpart $RF_{\\boldsymbol s}$.",
       "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A",
       frm=["gaussian-resampling", "bluestein-chirp", "coefficient-twist", "synthetic-convolution"]),
   inf("S7.5", "After the two scalings the exact counterpart is $2^{2b+4}(u*v)$, whose image under $\\Phi^{-1}$ is the integer coefficient convolution.",
       "$2^{2b+4}(u*v)$, whose inverse image under $\\Phi$ is the original",
       frm=["permutation-cancellation", "crt-address-map", "multiplication-by-convolution"]),
  ],
  page="multiplication-algorithm",
  frm=["multiplication-by-convolution", "parameter-choice", "crt-address-map", "coefficient-twist", "synthetic-convolution", "gaussian-resampling", "bluestein-chirp", "permutation-cancellation"],
  adds=[add("b", "digit bits", "the number $\\lceil\\log_2 n\\rceil$ of bits in each radix digit", "count")])

# ---------------- R8 precision
S8 = show("S8", "The recovered convolution coefficients have error below $1/2$, so rounding gives the exact integers and radix-$2^b$ carry propagation outputs the exact $2n$-bit product.",
  "track the scale factors and the disk margins through every approximate stage, add the errors, and compare the final error with $1/2$",
  "The true coefficients are integers, so any approximation with error below $1/2$ determines them uniquely.",
  "explicit", "The strict error below $1/2$ makes the nearest integer to",
  [
   inf("S8.1", "Each source transform has error below $E_sh_p$ with $E_s=9\\,2^{\\gamma}TL$ and all computed arrays stay inside the disk with margin.",
       " E_s=9\\,2^\\gamma TL,",
       frm=["fixed-point-disk-arithmetic", "vector-norms-and-the-triangle-inequality"]),
   inf("S8.2", "After the product, opposite transform and scaling by $S$ the error on $w=(u*v)/S$ is below $E_wh_p$ with $E_w=S(3E_s+2)<28\\,2^{\\gamma}T^2L$.",
       "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.",
       frm=["fixed-point-disk-arithmetic"]),
   inf("S8.3", "Scaling by $2^{2b+4}S$ and using $p=6b$ gives final coefficient error below $448b\\,2^{-b+\\gamma}\\le 448b\\,2^{-3b/4}<1/2$.",
       "<448b\\,2^{-b+\\gamma}",
       frm=["logarithms-floors-and-ceilings"],
       salient="The error bound $2^{-3b/4}$ decays with $b$ although the transforms lose $2^{\\gamma}TL$ in scale, because the working precision $p=6b$ is three times the $2b$-bit scale of the digits and $\\gamma=o(b)$."),
   inf("S8.4", "Rounded coefficients lie in $[0,2^{3b})$ and the carry recurrence $d_j=(c_j+k_j)\\bmod 2^b$, $k_{j+1}=\\lfloor (c_j+k_j)/2^b\\rfloor$ produces the exact product bits.",
       "After $\\Phi^{-1}$ the coefficients occur in increasing ordinary index,",
       frm=["schoolbook-binary-addition-with-carries", "binary-representation-of-integers"]),
  ],
  page="precision-exact-recovery",
  frm=["fixed-point-disk-arithmetic", "multiplication-by-convolution", "schoolbook-binary-addition-with-carries", "vector-norms-and-the-triangle-inequality"])

# ---------------- R9 time bound
S9 = show("S9", "Dividing all stage costs by $Tp=\\Theta(n)$ gives normalized costs that are each at most $p^{1-2\\kappa}$, so the whole machine runs in $O(n(\\lg n)^{1-\\kappa})$ time.",
  "tabulate the normalized cost of every stage as a power of $p$, compute the margin of each below 1 from the fixed parameter choices, and take the minimum",
  "The exponents $\\tau,\\sigma,\\lambda'$ are only slightly below 1, so one has to verify that every other row of the cost table is also a fixed margin below 1 and that this margin swallows any logarithmic factor.",
  "explicit", "any remaining fixed power of $\\log p$.",
  [
   inf("S9.1", "The normalized cost of each stage (layout moves, chunk exchanges, simultaneous rounds, CRT and axis layouts, Gaussian line maps, chirps, packed polynomial products) is a power of $p$ listed in a table.",
       "\\caption{Costs divided by $Tp$; each coefficient",
       frm=["big-o", "chunk-interchange", "simultaneous-butterfly-layer", "synthetic-transform-layout"]),
   inf("S9.2", "The seven dominant margins below 1 are at least $2^{-181}=2\\kappa$, the smallest being $\\epsilon c(1-\\tau)=2^{-181}$ from the chunk exchanges.",
       "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
       frm=["parameter-choice", "logarithms-floors-and-ceilings"],
       salient="The overall margin $2\\kappa=2^{-181}$ is the product of the three tiny exponents $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$: the saving over $\\log n$ is real but astronomically small."),
   inf("S9.3", "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^{\\kappa}$ eventually.",
       "Each of the seven displayed powers is at most $1-2\\kappa$ by",
       frm=["asymptotic-notation-omega-theta-and-little-o"]),
   inf("S9.4", "The total is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
       "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).",
       frm=["big-o"]),
  ],
  page="time-bound-accounting",
  frm=["parameter-choice", "simultaneous-butterfly-layer", "chunk-interchange", "synthetic-transform-layout", "big-o"])

ROOT = show("S0", "One deterministic fixed-tape Turing machine multiplies $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, which refutes the $n\\log n$ optimality conjecture in this model.",
  "build two faster tape primitives (address interchange and simultaneous butterfly layers) from recursive linear networks with a rank saving, then run them inside the Gaussian resampling, chirp and synthetic convolution reduction of integer multiplication to convolution, and add up the costs",
  "Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $n\\log n$, so both data movement and arithmetic must be sped up.",
  "explicit", "We therefore need savings in both movement and arithmetic.",
  [S1, S2, S3, S4, S5, S6, S7, S8, S9],
  page="main-theorem",
  frm=["integer-multiplication-problem", "optimality-conjecture", "harvey-hoeven-multiplier"],
  salient="The exponent $1-\\kappa$ is a genuine power saving in $\\lg n$, but $\\kappa=2^{-182}$ is astronomically small.",
  adds=[add("p", "precision", "the number of fractional bits of every stored complex coordinate, equal to $6\\lceil\\log_2 n\\rceil$", "count"),
        add("d", "dimension", "the number of axes of the transform array, a tiny power $\\lfloor b^{\\epsilon}\\rfloor$ of the digit bits", "count"),
        add("r", "record length", "the number of complex coefficients in a polynomial record, a power of two", "count"),
        add("T", "array size", "the number of entries of the padded transform array, the product of the power-of-two axis lengths, about $n/b$", "count")])

ans = {"root": ROOT}
out = BASE + "/exegenius/tasks/0046-argument.answer.json"
json.dump(ans, open(out, "w"), indent=1)

# verify quotes and order
def walk(n, acc):
    if n["intention"] == "infer":
        acc.append(n)
    for c in n.get("children", []) or []:
        walk(c, acc)
acc = []
walk(ROOT, acc)
last = -1
ok = True
for n in acc:
    q = n["quote"]["quote"]
    c = SRC.count(q)
    pos = SRC.find(q)
    line = SRC.count("\n", 0, pos) + 1
    flag = ""
    if c == 0: flag = "MISSING"; ok = False
    elif c > 1: flag = "MULTI(%d)" % c
    if pos < last and not n.get("deferred"): flag += " OUTOFORDER"; ok = False
    last = max(last, pos + len(q))
    print(n["id"], line, flag)
# motivation quotes
def walk2(n):
    m = n.get("motivation")
    if m and m.get("quote"):
        q = m["quote"]["quote"]
        if SRC.count(q) == 0:
            print("MOTIV MISSING", n["id"], q); 
    for c in n.get("children", []) or []:
        walk2(c)
walk2(ROOT)
print("ok" if ok else "PROBLEMS")
