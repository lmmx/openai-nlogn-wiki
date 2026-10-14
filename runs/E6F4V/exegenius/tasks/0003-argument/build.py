import json, sys

SRC = "paper"
PAPER = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V/sources/paper.tex"
OUT = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V/exegenius/tasks/0003-argument.answer.json"


def ev(q):
    return {"source": SRC, "quote": q}


def mot(text, source, quote=None):
    d = {"text": text, "source": source}
    if quote is not None:
        d["quote"] = ev(quote)
    return d


def infer(id, claim, quote, page=None, frm=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote)}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    return n


def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children}
    if page:
        n["page"] = page
    if frm:
        n["from"] = frm
    if salient:
        n["salient"] = salient
    if adds:
        n["adds"] = [{"symbol": s, "name": a, "meaning": b, "relation": c} for (s, a, b, c) in adds]
    return n


# ---------------------------------------------------------------- R1 toolkit
R1_1 = infer(
    "R1.1",
    "Splitting on a digit, permuting two digits, moving a digit and dealing rows cyclically to $W$ streams are all $O(V)$-time scans on a fixed number of tapes.",
    r"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
    page="elementary-stream-ops",
    frm=["tape-address-model", "sorting-and-data-movement-on-tapes",
         "finite-alphabet-encodings-and-constant-factor-simulation"])

R1_2 = infer(
    "R1.2",
    "An update $y \\mapsto y + a(\\text{controls}) \\bmod Q$ of a target field that follows its controls costs $O(V)$, by splitting each fiber at the offset and merging the two pieces in the opposite order.",
    r"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
    page="controlled-shift",
    frm=["tape-address-model", "elementary-stream-ops", "modular-arithmetic", "primes-coprimality-and-gcd"])

R1 = show(
    "R1",
    "Arrays stored in lexicographic order on tapes support linear-time rearrangements: digit moves, row splitting and controlled cyclic shifts.",
    "state the storage convention and prove the two elementary linear-time scan lemmas",
    mot("Every later procedure is built from scans of the stored array, so the paper first fixes how an address is implicit in tape position and which rearrangements cost only $O(V)$, the baseline against which the later savings are measured.",
        "reconstructed"),
    [R1_1, R1_2],
    page="tape-address-model",
    frm=["multitape-tm", "binary-representation-and-bit-operations",
         "sorting-and-data-movement-on-tapes",
         "finite-alphabet-encodings-and-constant-factor-simulation"])

# ---------------------------------------------------------------- R2 interchange / key step
K1 = show(
    "K1",
    "A fixed linear network with $W$ wires exchanges two banks of values, with signs, and restores every scratch wire whatever its initial value.",
    "run the eight-row schedule: subtract the old scratch effect, add the source effect, restore the scratch values, then compose three stages",
    mot("Because the scratch wires may hold arbitrary values (they will be existing data rows when the network is run on arrays), the schedule must cancel their contribution before and after use; the paper reads this as a linear form of transparent computation.",
        "recoverable"),
    [infer("K1.1",
           "For arbitrary initial scratch values, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
           r"invocation changes $y_S$ to $y_S+x_S$ and leaves every other value"),
     infer("K1.2",
           "Three stages (forward, inverse forward, forward) send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every auxiliary value; over $\\mathbb F_2$ this is the exchange of $X_a$ and $Y_a$.",
           r"(X_a,Y_a)\longmapsto(-Y_a,X_a)")],
    page="linear-network",
    frm=["finite-field-f2-arithmetic", "vectors-matrices-and-invertibility", "permutations-and-cartesian-products"],
    salient="Scratch wires return to their arbitrary initial contents, so the network behaves as an exact permutation of the data banks even though its intermediate states are linear combinations.")

K2 = show(
    "K2",
    "Replacing each scalar by an array and giving every gate one common frame $D_v$ means the stored arrays carry frames that cancel between gates, so only the endpoint operator $D_{\\rm out}D_{\\rm in}^{-1}$ is applied to each role.",
    "commute the invertible frame operators through the pointwise linear gates and telescope them along each route",
    mot("A pointwise gate cannot be applied to arrays stored in different representations; giving all incidences of a gate the same frame makes the gate commute with it, so the cost of a route is only the change of frame on its edges.",
        "recoverable"),
    [infer("K2.1",
           "A pointwise linear gate commutes with a frame common to all its incident arrays, so the invariant 'stored array = frame applied to logical array' persists through every gate.",
           r"Thus the common frame commutes with the pointwise gate, and"),
     infer("K2.2",
           "The operator implemented by the whole array network is $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$.",
           r"D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}."),
     infer("K2.3",
           "A route from input role $w$ to output role $\\rho(w)$ applies its sign times $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$, so intermediate frames can be chosen freely to make each edge cheap.",
           r"D_{\mathrm{source}(w)}^{-1}$ to its input array.")],
    page="common-frame-principle",
    frm=["vectors-matrices-and-invertibility", "permutations-and-cartesian-products", "linear-network"])

K3 = show(
    "K3",
    "Nested nondegenerate subspaces of $F^{\\otimes 3}$ can be attached to the gates and terminals so that the total rank change over all edges is less than $W m$.",
    "label gates by tensor products of three-element-subset indicator lines, use their intersection-size inner products to make adjacent labels nested, and count dimension changes by telescoping",
    mot("The cost of an edge is the rank of its frame change, which equals the dimension gained or lost by its label; so the whole saving reduces to a counting problem on dimensions, which orthogonality of the subset indicators lets one solve with only the $I$ central-wire return edges decreasing.",
        "reconstructed"),
    [infer("K3.1",
           "For indicator vectors $t_S,t_T$ of three-element subsets the form gives $\\langle t_S,t_T\\rangle=|S\\cap T|-1$, so neighboring triples are orthogonal and unwanted gather/scatter coefficients can be cancelled by side wires.",
           r"\langle t_S,t_T\rangle=|S\cap T|-1,"),
     infer("K3.2",
           "Source labels have total dimension $N$ and sink labels $Wm-N$, so the signed dimension changes over all edges sum to $Wm-2N$.",
           r"Thus the signed dimension changes will sum to $Wm-2N$, because the"),
     infer("K3.3",
           "The only decreasing edges are the central-wire edges between times 3 and 4, each losing dimension $h$, so the loss is $L=Ich$.",
           r"edges are the central-wire edges from time 3 to time 4; their dimension"),
     infer("K3.4",
           "The loss ratios $L_{\\rm b}/N=100/539$ and $L_{\\rm c}/N=101/539$ are both below $1/2$.",
           r"In particular, both are smaller than $1/2$."),
     infer("K3.5",
           "With the extra $N$ source ranks, the bit network has total edge rank $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}<W_{\\rm b}m$, and its matrices differ by $I_m$ between sink and source of every role.",
           r"=177176569088785861287000000<W_{\rm b}m.")],
    page="subset-intersection-labels",
    frm=["linear-algebra-basics", "linear-network", "common-frame-principle", "finite-field-f2-arithmetic"],
    salient="The total rank change is strictly less than the trivial count $W m$ for both networks, because the loss on decreasing edges is below half the number of data wires ($L/N=100/539$ and $101/539$).")

K4 = infer(
    "K4",
    "The rank deficit is large enough that $s_{\\rm b}/W_{\\rm b}<m^{\\tau}$ for the fixed rational exponent $\\tau=1-2^{-50}$.",
    r"\frac{s_{\rm b}}{W_{\rm b}}<m^\tau,",
    frm=["subset-intersection-labels", "logarithms-and-iterated-logarithm-notation"])

K5 = show(
    "K5",
    "The address map $(H,D)\\mapsto(H+AD,D)$ for a rank-$a$ matrix $A$ costs exactly $a$ interchanges of single field pairs plus $O(V)$, and three shears interchange $H$ and $D$.",
    "factor $A=E_1\\Pi E_2$ with lower-triangular $E_1,E_2$, do the triangular parts as linear controlled shifts, and turn each pivot into one pairwise swap",
    mot("The recursion needs the number of smaller calls on an edge to equal the rank of the frame change, not its size $m$; a Bruhat-type factorization isolates the rank into the partial permutation $\\Pi$ while the triangular factors respect the tape order and cost only linear time.",
        "recoverable"),
    [infer("K5.1",
           "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
           r"A=E_1\Pi E_2,"),
     infer("K5.2",
           "The shear $(H,D)\\mapsto(H+AD,D)$ can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work.",
           r"can be performed with exactly $a$ interchanges of pairs of $b$-digit"),
     infer("K5.3",
           "The three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange $H$ and $D$, and only the middle shear needs the network.",
           r"D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D,")],
    page="address-shear",
    frm=["linear-algebra-basics", "controlled-shift", "elementary-stream-ops", "modular-arithmetic",
         "permutations-and-cartesian-products"])

K6 = show(
    "K6",
    "Running the network with each edge done by smaller interchanges on role streams of volume $V/W$ gives $F_k\\le(s/W)F_{k-1}+O(1)$, hence $F_k=O(e^{\\tau})$.",
    "split rows cyclically into $W$ role streams, charge $s$ smaller calls of volume $V/W$, divide by the volume, and sum the geometric series",
    mot("Dividing by volume turns $s$ calls on streams of size $V/W$ into the factor $s/W$ per level; whether this factor beats $m$ (the growth of the chunk width per level) decides whether the total is a power of the width smaller than the width itself.",
        "recoverable"),
    [infer("K6.1",
           "The number of smaller calls made by one node is the sum of the edge ranks, exactly $s$.",
           r"The number of recursive calls is the sum of the edge ranks, exactly $s$."),
     infer("K6.2",
           "The time per unit volume satisfies $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, since each of the $s$ children has volume $V/W$.",
           r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1)."),
     infer("K6.3",
           "Because $s/W<m^{\\tau}$ the geometric sum is $O(m^{k\\tau})$, so $F_k=O(e^{\\tau})$ for chunk width $e=m^k$.",
           r"Hence $F_k=O(e^\tau)$."),
     infer("K6.4",
           "The fixed-tape depth-first schedule (parking the other $W-1$ role streams on a stack) adds only $O(V)$ at each node, so temporary storage does not enter the factor $s/W$.",
           r"therefore not substituted for logical volume in the factor $s/W$.")],
    salient=None)

S_KEY = show(
    "S_key",
    "A fixed linear network whose total number $s$ of smaller calls is less than $W m$ gives a cost-per-volume recurrence with ratio $s/W<m$, hence a power-saving exponent $\\tau<1$.",
    "build a bank-exchanging network whose edge changes can be done by smaller instances of the same task, and bound the recursion by the total rank $s$ of the edge changes",
    mot("The recursive contribution per level is multiplied by $s/W$ while the width grows by the factor $m$; the strict inequality between the two is the source of the power saving.",
        "explicit",
        quote=r"increases the recursive contribution by $s/W<m$. This strict inequality"),
    [K1, K2, K3, K4, K5, K6],
    page="rank-saving-recurrence",
    frm=["tape-address-model", "elementary-stream-ops", "recurrences-and-induction", "big-o"],
    salient="The number $s$ of smaller calls is strictly less than $W m$, although the trivial network would need exactly $W m$; the margin is tiny (relative deficit about $10^{-11}$), yet it yields a fixed exponent $\\tau=1-2^{-50}<1$ and thus a power of the width instead of linear.",
    adds=[("W", "wire count", "The number of wires (roles) of the fixed linear network, including scratch wires.", "count"),
          ("m", "label dimension", "The dimension of the ambient label space, equal to the number of fields in each address chunk handled at one recursion level.", "count"),
          ("s", "call count", "The total rank of all edge frame changes, i.e. the number of smaller calls one network invocation makes.", "count"),
          ("\\tau", "saving exponent", "A fixed rational exponent below 1 with $s/W<m^{\\tau}$.", "direct")])

R2_2 = infer(
    "R2.2",
    "Arbitrary widths and row counts are handled by padding rows from the chunks' own high digits and splitting the remaining width in base $m$, giving $O(Vu^{\\tau})$ for an interchange of two $u$-bit fields.",
    r"in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$.")

R2 = show(
    "R2",
    "Two disjoint contiguous address fields of $u$ bits can be interchanged, $(p,h,g,d,z)\\mapsto(p,d,g,h,z)$, in $O(V u^{\\tau})$ time for a fixed $\\tau<1$.",
    "use the bit network, whose edges are address shears, to swap power-of-$m$ widths recursively, then remove the width and row-count restrictions",
    mot("Direct movement costs a scan per bit of the field; computing XOR combinations of intermediate data lets the swap be built from shears executed through a network whose total rank is below $W m$, which by the recursion saves a power of the width.",
        "reconstructed"),
    [S_KEY, R2_2],
    page="address-chunk-interchange",
    frm=["tape-address-model", "elementary-stream-ops", "controlled-shift", "permutations-and-cartesian-products"])

# ---------------------------------------------------------------- R3 butterfly layer
R3_1 = show(
    "R3.1",
    "A simultaneous layer $C^{\\otimes e}$ of the two-point kernel $C=aI+bX$ on $e=mf$ axes costs $s$ smaller layers on $f$ axes, and $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
    "give the complex network Hamming-weight phase frames, factor every edge change into directional two-point kernels, and convert the $C$ layer back to the normalized butterfly",
    mot("The binary network works on bits, but the butterfly acts on complex values; Hamming-weight phases make the frame changes of the complex network products of the two-point kernel $C$, and $C$ is related to $H_0$ by phase diagonals.",
        "recoverable"),
    [infer("R3.1a",
           "The frame change on an edge is a product of one translation kernel $aI+bX_{v_j}$ (or its inverse) per vector of an orthonormal basis of the edge residual.",
           r"=\prod_{j=1}^{\rho_{\rm edge}}(aI+bX_{v_j})^{\epsilon_j},"),
     infer("R3.1b",
           "Over a group of $e=mf$ axes the network makes exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and gives $C^{\\otimes e}$ on every role.",
           r"$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
     infer("R3.1c",
           "The normalized butterfly layer equals $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$ with $\\mathcal S_D$ a diagonal phase and $b^D$ a shift and fourth-root phase.",
           r"H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D.")],
    page="phase-frame-kernel",
    frm=["linear-network", "common-frame-principle", "subset-intersection-labels", "linear-algebra-basics",
         "finite-field-f2-arithmetic", "complex-numbers", "butterfly"])

R3_2 = show(
    "R3.2",
    "A binary row addition $y_{j_i}\\leftarrow y_{j_i}\\oplus x_{j_i}$ on the same bit position of $f$ address chunks costs $O(V(L^{\\tau}+1))$ and restores the third chunk's arbitrary contents.",
    "do eight chunk-wide cyclic shifts that act as the XOR away from a small bad set of addresses, then repair that set deterministically by sorting",
    mot("Doing the $f$ bit additions one at a time would cost $f$ passes; shifting whole chunks adds all of them at once, but carries between packed segments can occur at addresses where a guard value is near the boundary, so those few addresses are found and fixed separately.",
        "recoverable"),
    [infer("R3.2a",
           "One fixed procedure performs the $f$ XORs, preserves spectators and payloads, and restores the whole chunk $z$ for every initial value.",
           r"it restores the entire chunk $z$ for"),
     infer("R3.2b",
           "Eight conditional additions leave $w$ restored and flip the parity of $u$ exactly when the control is 1: $(u',w')=(u+c(1-2(u\\bmod 2)),w)$.",
           r"\bigl(u+c(1-2(u\bmod2)),\ w\bigr)."),
     infer("R3.2c",
           "Only addresses whose guard values lie within 10 of the ends are bad: twenty excluded values per guard, so at most a fraction $80(f-1)2^{-K}$ of addresses.",
           r"There are exactly twenty excluded values for each guard in"),
     infer("R3.2d",
           "The bad records are extracted with destination keys, sorted by stable binary radix sort and reinserted, which implements the ideal XOR map $T_0$ everywhere.",
           r"This implements $T_0$ everywhere.")],
    page="packed-selected-bit-addition",
    frm=["address-chunk-interchange", "controlled-shift", "elementary-stream-ops",
         "finite-field-f2-arithmetic", "modular-arithmetic"],
    salient="The exceptional set has density only $O(f2^{-K})$ with $K\\gg\\log p$, so the correction by sorting is negligible although the repair is deterministic and independent of the payload.")

R3_3 = show(
    "R3.3",
    "Splitting complete rows among the $W$ roles and recursing on slots gives $F(e)\\le(s/W)F(e/m)+O((eK)^{\\tau}+1)$, which solves to $O(d^{\\lambda'})$ per unit volume for a layer on $D\\le d$ axes.",
    "apply the same network recursion as for address interchange, with packed chunk moves as the per-node overhead",
    mot("The recursion has the same ratio $s/W<m$ as the interchange; the per-node overhead is now the packed basis change at cost $O(V(eK)^{\\tau})$, and stopping the recursion at $e<d^{1/2}$ keeps the leaf cost below the power saving.",
        "recoverable"),
    [infer("R3.3a",
           "Each internal node on $e=m^k$ chunks makes exactly $s$ calls on slots of $e/m$ chunks.",
           r"vector in an edge residual basis, hence exactly \(s\) calls in one"),
     infer("R3.3b",
           "Row splitting gives each edge call exactly $1/W$ of the parent's logical volume, with all unselected suffix fields kept.",
           r"one role stream with volume exactly \(1/W\) of its parent's logical"),
     infer("R3.3c",
           "Time per volume obeys $F(e)\\le (s/W)F(e/m)+O((eK)^{\\tau}+1)$ with $F(e)=O(e)$ for $e<d^{\\beta}$.",
           r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),"),
     infer("R3.3d",
           "Partitioning $D-q_0$ chunks into base-$m$ groups and summing gives total cost $O(d^{\\lambda'})$ per unit volume for any fixed $\\lambda'<1$ above the stated bounds.",
           r"=O(d^{\lambda'})")],
    frm=["rank-saving-recurrence", "packed-selected-bit-addition", "recurrences-and-induction"])

R3_4 = infer(
    "R3.4",
    "Reserving $p+\\Delta$ fractional bits with $\\Delta=O(d^{C_1})=o(p)$ represents every intermediate Gaussian dyadic exactly, so the whole layer is exact before one truncation.",
    r"Thus reserving \(p+\Delta\)",
    frm=["fixed-point-truncation", "norms-absolute-values-and-error-bounds"])

R3_5 = infer(
    "R3.5",
    "The simultaneous normalized butterfly layer returns $Q_p(\\mathcal H z)$ in the same format in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$.",
    r"coefficient order, and component format in $O(Vd^{\lambda'})$ time,",
    frm=["fixed-point-truncation"])

R3 = show(
    "R3",
    "The normalized two-point butterfly $H_0$ applied at the same bit offset in $d$ address chunks of a polynomial-record array costs $O(V d^{\\lambda'})$ for a fixed $\\lambda'<1$.",
    "evaluate the layer exactly through the phase-frame network with packed chunk moves and recurse on slots, truncating once at the end",
    mot("Applying the $d$ butterflies separately would need $d$ whole-array passes; the network reduces them to a recursion whose ratio $s/W<m$ gives a power saving in $d$.",
        "explicit",
        quote=r"$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly"),
    [R3_1, R3_2, R3_3, R3_4, R3_5],
    page="fast-butterfly-layer",
    frm=["fixed-point-truncation", "address-chunk-interchange", "rank-saving-recurrence", "butterfly",
         "polynomial-ring-mod", "recurrences-and-induction"],
    salient="The saving exponent is again controlled by the ratio $s/W<m$, now with the complex network of $s_{\\rm c}<W_{\\rm c}m$, and the exceptional-address repair keeps the bound worst-case.",
    adds=[("D", "selected axes", "The number of address chunks (axes) on which the layer applies $H_0$ simultaneously, at most $d$.", "count"),
          ("\\lambda'", "layer exponent", "A fixed exponent below 1 with layer cost $O(Vd^{\\lambda'})$.", "direct")])

# ---------------------------------------------------------------- R4 synthetic transforms
R4 = show(
    "R4",
    "A normalized Fourier-type transform over $\\mathbb C[y]/(y^r+1)$ with roots $\\omega_t=y^{2r/t}$ is computed by radix-two butterfly rounds in bit-reversed frequency order, in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
    "define the transform with signed-shift roots, compute it by decimation in frequency, store outputs in retained order, and lay the axes out so the simultaneous layers apply",
    mot("Powers of $y$ are exact roots of unity that act as signed shifts, so no multiplications by complex roots are needed; the rounds can then be grouped across axes into the simultaneous layers of the previous section, provided the participating bits are placed at a common offset of consecutive chunks.",
        "recoverable"),
    [infer("R4a",
           "The synthetic transforms satisfy $F_t^+F_t^-=t^{-1}I$ despite zero divisors in $\\mathbb C[y]/(y^r+1)$, by a direct character cancellation.",
           r"F_t^+F_t^-=t^{-1}I."),
     infer("R4b",
           "The decimation-in-frequency recursion writes the entry of frequency $j$ in slot $\\operatorname{rev}_a(j)$ without moving whole indices.",
           r"entry $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$."),
     infer("R4c",
           "The two procedures implement exactly $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the opposite transform consumes the stored order.",
           r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
     infer("R4d",
           "On $d-1$ axes of lengths $t_i\\in\\{2^{\\ell-1},2^{\\ell}\\}$ the layout-restoring transform costs $O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right)$ with error below $\\sqrt2\\ell 2^{-p}$.",
           r"O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)."),
     infer("R4e",
           "Moving the at most $D(b+1)$ slots to a prefix costs $O(TpdK)$, and the rounds on prefix slots are done as individual butterflies.",
           r"listed slots, so the moves cost $O(TpdK)$."),
     infer("R4f",
           "Exchanging the $Dq-1$ width-$K$ chunks to make the participating bits consecutive costs $O(Tp\\,pK^{\\tau-1})$ by the chunk-swap bound.",
           r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
     infer("R4g",
           "The simultaneous layer then handles all remaining rounds in $O(Tp\\ell d^{\\lambda'})$ total.",
           r"$O(Tp\ell d^{\lambda'})$ in total.")],
    page="synthetic-transform",
    frm=["polynomial-ring-mod", "dft", "multidimensional-dft", "butterfly", "roots-of-unity",
         "fast-fourier-transform-and-divide-and-conquer", "fixed-point-truncation",
         "address-chunk-interchange"])

# ---------------------------------------------------------------- R5 ring convolution
R5_1 = show(
    "R5.1",
    "Two disk-grid polynomials in $\\mathbb C[y]/(y^r+1)$ have their product's Gaussian-integer numerators computed, and $Q_p(fg/r)$ returned, in $O(rp\\log(rp))$ time using the established multiplier.",
    "pack coefficients as integers at base $2^{4p}$ (signed Kronecker substitution), multiply, and read the coefficients back by centered residues and carries",
    mot("The established $O(N\\log N)$ multiplier handles ordinary integers; a base large enough to separate coefficients turns a polynomial product into one integer product, and centered residues take care of negative coefficients.",
        "recoverable"),
    [infer("R5.1a",
           "One can compute the exact numerators of $fg$ and return $Q_p(fg/r)$ in the same format in time $O(rp\\log(rp))$.",
           r"numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time"),
     infer("R5.1b",
           "Every coefficient of an ordinary product obeys $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$ with $B_0=2^{4p}$, so a centered residue modulo $B_0$ identifies it once lower coefficients are removed.",
           r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
     infer("R5.1c",
           "Four exact integer products on $O(rp)$ bits dominate the linear packing, extraction, combination, wrapping and truncation costs.",
           r"Four exact integer products dominate the linear")],
    page="signed-packing",
    frm=["established-multiplier", "polynomial-ring-mod", "polynomials", "fixed-point-truncation",
         "norms-absolute-values-and-error-bounds"])

R5_2 = show(
    "R5.2",
    "Normalized convolution $\\mathcal M_r(f,g)=(f*g)/(rM)$ over the ring is obtained from two forward transforms in the same retained order, pointwise products divided by $r$, the opposite transform and an exact scaling by $M$.",
    "check the normalization identity, cancel the retained record permutation in the pointwise product, and add the errors of the three transforms and the product truncation",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied without undoing the bit-reversed layout.",
        "explicit",
        quote=r"Pointwise multiplication commutes with applying the same record"),
    [infer("R5.2a",
           "The forward transform turns convolution into pointwise product: $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, and $F^+F^-=I/M$ recovers $(f*g)/(rM)$.",
           r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
     infer("R5.2b",
           "The returned approximation has error below $\\sqrt2 M(3\\ell+1)2^{-p}$.",
           r"=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."),
     infer("R5.2c",
           "The $M=T/r$ pointwise products cost $O(Tp\\log(rp))$ in total, in addition to the three transform costs.",
           r"is $O(Tp\log(rp))$; the three transform costs are as stated, and")],
    frm=["synthetic-transform", "signed-packing", "cyclic-convolution", "dft"])

R5 = show(
    "R5",
    "Normalized convolution on $d-1$ axes of arrays with entries in $\\mathbb C[y]/(y^r+1)$ costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
    "transform both operands, multiply pointwise in the retained order using signed packing, and apply the opposite transform",
    mot("The fast synthetic transforms supply the cheap transforms and the established multiplier handles the short polynomial products; the paper does not call the improved algorithm recursively.",
        "recoverable"),
    [R5_1, R5_2],
    page="ring-convolution",
    frm=["polynomial-ring-mod", "cyclic-convolution", "dft", "multidimensional-dft",
         "synthetic-transform", "fixed-point-truncation"])

# ---------------------------------------------------------------- R6 resampling
R6 = show(
    "R6",
    "A Fourier transform of prime lengths $s_i$ on $d$ axes equals $2^{\\gamma}\\mathcal B_0 Q F_{\\boldsymbol t}\\mathcal A$ with power-of-two lengths $t_i>s_i$, and the linewise maps cost $O(dTp^{3/2+\\delta}\\alpha)$, with the permutations $R,Q$ left inside the identity.",
    "Gaussian-weighted contraction in one dimension, then a tensor product along the axes with zero padding to the box of $T$ entries",
    mot("Its usual implementation sorts twice on each coordinate; we retain both permutations in the transform formula and compute that formula directly.",
        "explicit",
        quote=r"Its usual implementation sorts twice on each"),
    [infer("R6a",
           "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
           r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
     infer("R6b",
           "Fixed multitape algorithms approximate $A$ and $B_0$ with error below $p^2$ and time $O(tp^{3/2+\\delta}\\alpha)$ per line of length $t$.",
           r"There are fixed multitape algorithms for approximations"),
     infer("R6c",
           "Tensoring gives $RF_{\\boldsymbol s}=2^{\\gamma}\\mathcal B_0 QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$.",
           r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
     infer("R6d",
           "The one-dimensional algorithms over all lines cost $O(dTp^{3/2+\\delta}\\alpha)$ with error below $dp^2$.",
           r"$O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$."),
     infer("R6e",
           "Exposing and restoring all lines in the padded box costs $O(Tp\\,d^2(1+\\ell^{\\tau}))$ by equal-width chunk swaps.",
           r"then exposing and restoring all the lines costs")],
    page="gaussian-resampling",
    frm=["dft", "multidimensional-dft", "fixed-point-truncation", "established-multiplier",
         "norms-absolute-values-and-error-bounds", "address-chunk-interchange", "roots-of-unity"])

# ---------------------------------------------------------------- R7 chirp and cancellation
R7 = show(
    "R7",
    "The middle factor $QF_{\\boldsymbol t}$ is a chirp-weighted normalized cyclic convolution, and the source permutation $R$ cancels across the two forward transforms, the pointwise product and the opposite transform: $RF^+_{\\boldsymbol s}[(RF_{\\boldsymbol s}u)(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
    "use Bluestein's chirp identity for the frequency change, and use that dilations by units commute with transforms and with pointwise products",
    mot("We retain both permutations in the transform formula, so $Q$ must be absorbed without a sort (the chirp does this) and $R$ must disappear on its own (it does, by $RF^+R=F^+$).",
        "explicit",
        quote=r"We retain both permutations in the transform formula and"),
    [infer("R7a",
           "$QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$ with the chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$.",
           r"\frac{a*(\overline a\mathbin{\cdot}u)}{T}.",
           page="bluestein-chirp",
           frm=["cyclic-convolution", "dft", "multidimensional-dft", "complex-numbers", "roots-of-unity"]),
     infer("R7b",
           "Since $RF^+R=F^+$, the retained permutation cancels: $(RF^+_{\\boldsymbol s})[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.",
           r"\bigl[(RF_{\boldsymbol s}u)\mathbin{\cdot}",
           salient="The permutation $R$ is never executed, yet it leaves no trace in the product: it cancels exactly between the forward and opposite transforms.")],
    page="permutation-cancellation",
    frm=["dft", "multidimensional-dft", "cyclic-convolution", "bluestein-chirp", "gaussian-resampling"])
# the bluestein step has its own page, so turn R7a into a show-less step with page set above
R7["salient"] = "The source permutation $R$ is never executed, yet it cancels exactly between the forward and opposite transforms."
R7["children"][1].pop("salient", None)

# ---------------------------------------------------------------- R8 multiplication algorithm
A0 = show(
    "A0",
    "Fixed rational exponents, $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$, a padded size $T\\in[4n/b,8n/b)$, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct primes $s_i$ just below $t_i$ with $T/2<S<T$ satisfy all hypotheses of the lemmas.",
    "choose the parameters so that every tape lemma and the resampling hypotheses apply, and verify the prime intervals by an explicit prime-count bound",
    mot("Each lemma has hypotheses on the sizes (power-of-two lengths, $\\theta=t/s-1>p/\\alpha^4$, comparison bands for $d$ and $r$); the choice is made in reverse so that all hold, and the primes must be close to the powers of two so that their product fills a fixed fraction of the box.",
        "recoverable"),
    [infer("A0a",
           "The fixed exponents include $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$.",
           r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
     infer("A0b",
           "The size parameters are $b=\\lceil\\log_2 n\\rceil$, $p=6b$, $d=\\lfloor b^{\\epsilon}\\rfloor$ and $K=\\lfloor d^{c}\\rfloor$.",
           r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
     infer("A0c",
           "The axis lengths satisfy $t_i\\in\\{r/2,r\\}$, $\\prod_i t_i=T$ and $t_d=r$.",
           r"t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r."),
     infer("A0d",
           "The resampling parameter is $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, so $2\\le\\alpha<\\sqrt p$ and $\\gamma=o(b)$.",
           r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
     infer("A0e",
           "Distinct odd primes exist with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$.",
           r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
     infer("A0f",
           "The product $S=\\prod_i s_i$ satisfies $T/2<S<T$.",
           r"Together with $s_i<t_i$, this gives $T/2<S<T$.")],
    page="parameter-choice",
    frm=["gaussian-resampling", "primes-coprimality-and-gcd", "logarithms-and-iterated-logarithm-notation",
         "floor-ceiling-and-summation-notation", "polynomial-ring-mod", "chinese-remainder-theorem"])

A1 = show(
    "A1",
    "The integer product is the polynomial product of the radix-$2^b$ digit lists, which has no wraparound modulo $x^S-1$ and coefficients below $2^{3b}$.",
    "write each input as a polynomial in $2^b$ and bound the degree and coefficient size of the product",
    mot("Cyclic convolution of digit lists computes the integer product once carries are propagated; the padding must be long enough that the cyclic wrap never touches a nonzero coefficient, and the coefficients must be small enough to be recovered by rounding.",
        "recoverable"),
    [infer("A1a",
           "The product of the two digit polynomials has degree at most $2q-2<2n/b\\le T/2<S$.",
           r"2q-2<2n/b\le T/2<S."),
     infer("A1b",
           "Convolution modulo $x^S-1$ therefore has no nonzero wraparound.",
           r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
     infer("A1c",
           "Every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
           r"0\le c_j\le q(2^b-1)^2<2^{3b},")],
    page="radix-digit-convolution",
    frm=["cyclic-convolution", "polynomials", "binary-representation-and-bit-operations"])

A2 = show(
    "A2",
    "The Chinese-remainder map $\\Phi:\\mathbb C[x]/(x^S-1)\\to\\mathbb C[x_1,\\dots,x_d]/(x_i^{s_i}-1)$ preserves convolution and is implemented by triangular controlled shifts in $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
    "show $\\Phi$ is an algebra isomorphism, give the coordinates by a triangular formula, and implement it by controlled shifts and axis reorderings",
    mot("A single long cyclic convolution of length $S$ becomes one on a product of distinct prime axes, which is the shape that Gaussian resampling needs; the triangular form of the coordinates lets each update be a controlled cyclic shift in tape order.",
        "recoverable"),
    [infer("A2a",
           "$\\Phi$ is an isomorphism and preserves cyclic convolution.",
           r"$\Phi$ is an isomorphism and preserves cyclic convolution."),
     infer("A2b",
           "The coordinate of $\\Phi(x^k)$ on axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}$, a shift of $a_i$ controlled by lower-index digits.",
           r"b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}."),
     infer("A2c",
           "The map, its inverse and their padding operations cost $O(Tp\\,d^2(1+\\ell^{\\tau}))$.",
           r"their padding operations cost")],
    page="crt-address-map",
    frm=["chinese-remainder-theorem", "cyclic-convolution", "controlled-shift", "address-chunk-interchange",
         "modular-arithmetic"])

A3 = show(
    "A3",
    "The coefficient twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ identifies $\\mathbb C[x_d]/(x_d^r-1)$ with $\\mathbb C[y]/(y^r+1)$, so complex cyclic convolution on $d$ axes is ring convolution on $d-1$ axes after twisting.",
    "multiply coefficient $k$ by $\\zeta^k$, check that the negative wrap equals the cyclic wrap after untwisting, and compose with the ring convolution",
    mot("The synthetic machinery lives over $\\mathbb C[y]/(y^r+1)$, whereas the Gaussian-resampling axes are cyclic; the twist turns one into the other without changing norms.",
        "recoverable"),
    [infer("A3a",
           "The twist multiplies coefficient $k$ by the nonzero number $\\zeta^k$, hence is an isometric isomorphism with inverse multiplying by $\\zeta^{-k}$.",
           r"multiplying coefficient $k$ by the nonzero number $\zeta^k$."),
     infer("A3b",
           "A product term with $k+l=j+hr$ gets factor $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
           r"\zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j.",
           salient="The sign $(-1)^h$ of the negative wrap is exactly cancelled by $\\zeta^{rh}=(-1)^h$, so after untwisting the wrap is the original cyclic one."),
     infer("A3c",
           "Normalized complex cyclic convolution is $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
           r"\mathcal M_r(\iota D_+f,\iota D_+g)")],
    page="phase-twist",
    frm=["polynomial-ring-mod", "cyclic-convolution", "roots-of-unity", "complex-numbers"])

A4 = show(
    "A4",
    "The computed chirp transform and the source transform $\\widetilde{\\mathscr F}=2^{\\gamma}\\mathcal B_0 QF_{\\boldsymbol t}\\mathcal A$ approximate $RF_{\\boldsymbol s}$ using one complex convolution.",
    "form the chirp-weighted convolution of the twisted data with disk-grid chirp values and wrap it in the two resampling maps",
    mot("This composes the Bluestein identity with the Gaussian resampling identity so that the prime-length transform is evaluated by power-of-two convolutions only.",
        "recoverable"),
    [infer("A4a",
           "The chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, convolves it with $\\widetilde a$ and multiplies by $\\overline{\\widetilde a}$ again.",
           r"x_0&=Q_p(\overline{\widetilde a}\mathbin{\cdot}x),"),
     infer("A4b",
           "The source transform $\\widetilde{\\mathscr F}$ has exact counterpart $\\mathscr F=2^{\\gamma}\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
           r"\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A")],
    frm=["bluestein-chirp", "gaussian-resampling", "phase-twist", "ring-convolution", "fixed-point-truncation"])

A5 = show(
    "A5",
    "The pipeline maps digits through $\\Phi$, applies two source transforms, multiplies pointwise, applies the opposite transform, rescales and rounds, and its two factors $S$ undo different normalizations.",
    "execute the pipeline in the order of the reduction and track the normalizing constants",
    mot("The reductions of the introduction (digit convolution, prime axes, power-of-two axes, ring convolution) are applied in order, and the exact counterpart after three transforms is $(u*v)/S^2$, whose scalings must be removed.",
        "recoverable"),
    [infer("A5a",
           "Step 1: the coefficient-address map $\\Phi$ with padded layout produces source arrays $u,v$ of norm below $1/4$.",
           r"Apply the coefficient-address map $\Phi$, with its padded layout, to obtain"),
     infer("A5b",
           "Step 2: compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.",
           r"\item Compute $\widetilde{\mathscr F}(u)$ and"),
     infer("A5c",
           "Step 4: compute $\\widetilde{\\mathscr F}^{+}(z)$ of the truncated pointwise product $z$ and multiply the grid numerators by $S$.",
           r"\item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid"),
     infer("A5d",
           "Step 5: multiply exactly by $2^{2b+4}S$, round to integers, and apply $\\Phi^{-1}$ to restore ordinary coefficient order.",
           r"\item Multiply the grid numerators of $\widetilde w$ exactly by"),
     infer("A5e",
           "The first $S$ turns $(u*v)/S^2$ into $w=(u*v)/S$ and the second $S$ with $2^{2b+4}$ gives the original integer coefficient convolution.",
           r"The two occurrences of $S$ in this algorithm undo different")],
    frm=["crt-address-map", "permutation-cancellation", "gaussian-resampling", "ring-convolution"])

A6 = show(
    "A6",
    "The accumulated coefficient error before rounding is below $1/2$, so rounding recovers the exact integer coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product.",
    "track error and disk margins through each approximate transform, scale by the known constants, then round and carry",
    mot("The transforms only approximate their exact counterparts; since the true coefficients are integers, an error strictly below $1/2$ identifies each uniquely, and the capacity bound $2^{3b}$ keeps the carries bounded.",
        "recoverable"),
    [infer("A6a",
           "The source transform has error below $E_sh_p$ with $E_s=9\\cdot2^{\\gamma}TL$ and stays in the disk.",
           r"E_s=9\,2^\gamma TL,"),
     infer("A6b",
           "After the first scaling by $S$ the error is below $E_wh_p$ with $E_w=S(3E_s+2)<28\\cdot2^{\\gamma}T^2L$.",
           r"E_w:=S(3E_s+2)<28\,2^\gamma T^2L."),
     infer("A6c",
           "After the second scaling the absolute error is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
           r"\le448b\,2^{-3b/4}<\frac12."),
     infer("A6d",
           "The nearest integer to each recovered coefficient is therefore the unique correct coefficient.",
           r"that value the unique correct coefficient."),
     infer("A6e",
           "Carries propagate by $k_0=0$, $d_j=(c_j+k_j)\\bmod Q_0$, $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$ and $k_j<Q_0^2$.",
           r"k_0=0,\qquad d_j=(c_j+k_j)\bmod Q_0,\qquad"),
     infer("A6f",
           "The product is below $2^{2n}$, so after removing padding bits exactly $2n$ output bits remain.",
           r"than $2^{2n}$; all bits above position $2n-1$ are therefore zero.")],
    page="exact-recovery",
    frm=["radix-digit-convolution", "cyclic-convolution", "fixed-point-truncation",
         "norms-absolute-values-and-error-bounds", "recurrences-and-induction", "phase-twist"],
    salient="The error bound $448b\\,2^{-3b/4}$ is tiny only because the precision $p=6b$ exceeds the $3b$ bits of coefficient capacity plus the $\\gamma+O(\\log)$ bits lost to the scalings; the slack is what lets truncated disk-grid arithmetic give exact integers.")

R8 = show(
    "R8",
    "Two $n$-bit integers are multiplied exactly by forming radix-$2^b$ digits, mapping them to prime axes, taking two source transforms, multiplying pointwise, applying the opposite transform, and rescaling, rounding and carrying.",
    "chain the reductions digit convolution, prime-axis cyclic convolution, power-of-two axes via resampling and chirps, and ring convolution after a coefficient twist",
    mot("Each reduction changes the problem into one the next tool handles: carries make multiplication a convolution, CRT makes the long axis a product of coprime axes, resampling and chirps make the transform lengths powers of two, and the twist makes the last axis a negacyclic ring.",
        "explicit",
        quote=r"The arrows describe changes of problem and representation. Fast address"),
    [A0, A1, A2, A3, A4, A5, A6],
    page="multiplication-algorithm",
    frm=["cyclic-convolution", "ring-convolution", "gaussian-resampling", "permutation-cancellation",
         "established-multiplier"],
    adds=[("b", "digit width", "The number of bits of one radix digit, $b=\\lceil\\log_2 n\\rceil$.", "count"),
          ("S", "prime product", "The product of the distinct prime source lengths $s_i$, with $T/2<S<T$.", "direct")])

# ---------------------------------------------------------------- R9 time accounting
rows = [
    ("R9.1", "layout moves", r"Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\",
     "Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, a power $p^{\\epsilon(1+c)}$ of $p$."),
    ("R9.2", "chunk exchanges", r"Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\",
     "Chunk exchanges for the transform layout cost $pK^{\\tau-1}$, a power $p^{1-\\epsilon c(1-\\tau)}$ of $p$."),
    ("R9.3", "butterfly rounds", r"Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\",
     "Simultaneous butterfly rounds cost $\\ell d^{\\lambda'}$, a power $p^{1-\\epsilon(1-\\lambda')}$."),
    ("R9.4", "CRT layout", r"CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\",
     "CRT and axis layouts cost $d^2(1+\\ell^{\\tau})$, a power $p^{\\tau+\\epsilon(2-\\tau)}$."),
    ("R9.5", "Gaussian line maps", r"Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\",
     "Gaussian line maps cost $dp^{1/2+\\delta}\\alpha$, a power $p^{3/4+\\delta+3\\epsilon/2}$."),
    ("R9.6", "chirps", r"Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\",
     "Chirps, twists and scalar products cost $dp^{\\delta}$, a power $p^{\\epsilon+\\delta}$."),
    ("R9.7", "packed products", r"Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\",
     "Packed polynomial products cost $\\log(rp)$, a power $p^{1-\\epsilon}$."),
]
R9_rows = [infer(i, c, q) for (i, _n, q, c) in rows]

R9_1 = show(
    "R9.A",
    "Dividing every cost by $V=Tp=\\Theta(n)$, seven rows of the cost table dominate and the other rows are absorbed.",
    "tabulate the cost of each operation per unit volume and its power of $p$",
    mot("The tape procedures were proved with volume-normalized bounds, and the repeated transforms are only a fixed number, so one table of costs per unit volume covers the whole algorithm.",
        "recoverable"),
    R9_rows)

R9 = show(
    "R9",
    "The total time is $O(Tp\\cdot p^{1-\\kappa})=O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$, since each of the seven dominant powers of $p$ is at most $1-2\\kappa$.",
    "tabulate normalized costs, compute the margin of each dominant power below 1, and absorb setup, exceptional streams and fixed powers of $\\log p$",
    mot("The saving is the smallest margin below 1 among the dominant rows; keeping an extra factor of two ($1-2\\kappa$ rather than $1-\\kappa$) lets any fixed power of $\\log p$ be absorbed by $p^{\\kappa}$.",
        "explicit",
        quote=r"This explicit slack will cover"),
    [R9_1,
     infer("R9.B",
           "The margins are $g_1>1/2$, $g_2=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$.",
           r"g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad"),
     infer("R9.C",
           "Hence $\\min_i g_i=2^{-181}=2\\kappa$.",
           r"Thus $\min_i g_i=2^{-181}=2\kappa$."),
     infer("R9.D",
           "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^{\\kappa}$ eventually.",
           r"Each of the seven displayed powers is at most $1-2\kappa$ by"),
     infer("R9.E",
           "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
           r"O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).")],
    page="time-accounting",
    frm=["parameter-choice", "fast-butterfly-layer", "address-chunk-interchange",
         "big-omega-theta-and-little-o-notation", "logarithms-and-iterated-logarithm-notation"],
    salient="The exponent $\\kappa=2^{-182}$ is astronomically small because the weakest of the seven margins, $g_2=\\epsilon c(1-\\tau)=2^{-181}$ from the chunk-exchange row, is a product of the tiny fixed exponents $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$.")

# ---------------------------------------------------------------- root
ROOT = show(
    "S0",
    "A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture.",
    "reduce integer multiplication to convolution over a polynomial ring, and speed up the data movement and the butterfly layers of its transforms with two new tape procedures that each save a power of the logarithm",
    mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both movement and arithmetic.",
        "explicit",
        quote=r"We therefore need savings in both movement and arithmetic. Two tape"),
    [R1, R2, R3, R4, R5, R6, R7, R8, R9],
    page="main-theorem",
    frm=["integer-multiplication-conjecture", "multitape-tm", "big-o", "established-multiplier"],
    salient="The saving is a strict power of the logarithm, $(\\lg n)^{-\\kappa}$, rather than a $\\log^*$ or $\\log\\log$ factor, although $\\kappa$ itself is astronomically small.",
    adds=[("\\kappa", "saving exponent", "The fixed exponent $2^{-182}$ by which the running time beats $n\\log n$ by a power of the logarithm.", "direct"),
          ("p", "working precision", "The number of fractional bits of every fixed-point coordinate, $p=6\\lceil\\log_2 n\\rceil$.", "count"),
          ("d", "axis count", "The number of tensor axes of the transform array.", "count"),
          ("r", "record length", "The number of complex coefficients of one polynomial record modulo $y^r+1$.", "count"),
          ("K", "chunk width", "The number of address bits in one axis chunk of the layer layout.", "count"),
          ("T", "box size", "The number of entries (power of two) of the padded array.", "direct")])

json.dump({"root": ROOT}, open(OUT, "w"), indent=1)

# ------------------------------------------------------------- verification
text = open(PAPER).read()
order = []


def walk(n):
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        c = text.count(q)
        pos = text.find(q)
        order.append((n["id"], pos, c))
    else:
        for ch in n["children"]:
            walk(ch)


walk(ROOT)
bad = False
prev = -1
for (i, pos, c) in order:
    flag = ""
    if c != 1:
        flag += " COUNT=%d" % c
        bad = True
    if pos < prev:
        flag += " OUT-OF-ORDER"
        bad = True
    prev = max(prev, pos)
    if flag:
        print(i, pos, flag)
# motivation quotes
def walkm(n):
    if n["intention"] == "show":
        m = n["motivation"]
        if m.get("quote"):
            q = m["quote"]["quote"]
            if text.count(q) < 1:
                print("MOTIVATION QUOTE MISSING", n["id"])
        for ch in n["children"]:
            walkm(ch)
walkm(ROOT)
print("ok" if not bad else "problems", len(order), "infer steps")
