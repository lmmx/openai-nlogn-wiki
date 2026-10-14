import json, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1V"
TEXT = open(BASE + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def mot(text, source, quote=None):
    return {"text": text, "source": source, "quote": ev(quote) if quote else None}

def inf(id, claim, quote, page=None, frm=None, deferred=False, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm or []}
    if page: n["page"] = page
    if deferred: n["deferred"] = True
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, motivation, children, page=None, frm=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "children": children, "from": frm or []}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def b(symbol, name, meaning, rel):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": rel}

# ---------------- key step: power-width interchange ----------------
bit_network = show(
    "KEY.1",
    "A fixed network of $W_{\\rm b}$ pointwise XOR gates exchanges two banks of values and restores every scratch wire, and nested rational labels give edge matrices whose ranks sum to $s_{\\rm b}<W_{\\rm b}m$ while the endpoint difference is $I_m$ on every role.",
    "Attach nested rational subspaces (labels) to the gates and terminals of the scalar network, take their projections as address-shear frames, and count the rank of each edge difference.",
    mot("A frame change along an edge is cheap exactly when the labels at its ends are nested and differ in few dimensions, so the labels are chosen to make the dimension changes small.",
        "explicit", "choose its intermediate labels to make the changes of frame inexpensive."),
    [
        inf("KEY.1.1",
            "For arbitrary initial scratch values, one forward invocation of the eight-row copy/gather/scatter/side-injection schedule changes $y_S$ to $y_S+x_S$ and nothing else; three stages then swap the two banks with signs and restore every scratch wire.",
            "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
            page="network",
            frm=["boolean-gates-and-circuits", "binary-field-f2-and-xor", "sets-subsets-and-basic-combinatorics"],
            salient="The net effect on the target does not depend on the arbitrary initial values of the scratch wires, because the first two rows subtract exactly what the last rows put back."),
        inf("KEY.1.2",
            "If every array on a wire is given an invertible frame at each vertex, with one common frame at all incidences of a gate, then the pointwise gate commutes with the frame and the network's overall effect is the endpoint frames applied to each role.",
            "Thus the common frame commutes with the pointwise gate, and",
            page="frames",
            frm=["network", "vectors-matrices-and-linear-maps", "functions-bijections-and-permutations"],
            salient="All intermediate frames cancel along a route; only the source and sink frames of each role remain, so intermediate frames can be chosen freely to make edges cheap."),
        show("KEY.1.3",
             "Labels built from indicator vectors of three-element subsets, tensored three times, are nested along every edge of the network and the labels of neighboring gates are orthogonal.",
             "Give each gate a tensor product of triple lines and orthogonal complements, using the intersection-size pairings of the Frankl-Wilson/Alon construction.",
             mot("Side wires join neighboring triples, and passing through nested subspaces is only possible when neighboring triple lines are orthogonal.",
                 "explicit", "The first inclusion is possible because $t_X\\perp t_Y$."),
             [
                 inf("KEY.1.3.1",
                     "Every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field of either construction.",
                     "Thus every triple line is nondegenerate, and neighboring triple lines"),
                 inf("KEY.1.3.2",
                     "Every edge of the network joins comparable nondegenerate labels, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
                     "Every edge joins comparable nondegenerate labels."),
             ],
             page="subset-labels",
             frm=["network", "matrix-basics", "sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor"]),
        show("KEY.1.4",
             "The labels' dimension changes along all edges sum to $Wm-2N+2L$ with total loss $L<N/2$, so the rational ranks of the edge differences sum to a total $s<Wm$.",
             "Telescope the signed dimension changes at each gate, then add twice the total loss on the decreasing edges.",
             mot("The saving can only come from keeping the dimension lost on decreasing edges small relative to the number $N$ of exchanged values.",
                 "explicit", "The saving will come from keeping the total dimension lost on decreasing"),
             [
                 inf("KEY.1.4.1",
                     "The signed sum of dimension changes telescopes at every gate, since each touched wire has the same gate label coming in and going out.",
                     "The signed sum of dimension changes telescopes at every gate: each"),
                 inf("KEY.1.4.2",
                     "Source dimensions sum to $N$ and sink dimensions to $Wm-N$, so the signed increase is $Wm-2N$.",
                     "The signed increase is therefore $Wm-2N$."),
                 inf("KEY.1.4.3",
                     "There are $Ic$ decreasing edges each losing $h$, so passing to absolute changes adds $2L$.",
                     "There are $Ic$ decreasing edges, each of loss $h$; replacing signed"),
                 inf("KEY.1.4.4",
                     "The loss ratio is $L_{\\rm b}/N=100/539$, below $1/2$.",
                     "\\frac{L_{\\rm b}}{N}=\\frac{100}{539},\\qquad"),
             ],
             page="rank-saving",
             frm=["subset-labels", "matrix-basics", "frames"],
             salient="The rank total is only barely below $Wm$ (relative deficit about $1.5\\cdot10^{-11}$) yet strictly below it, because only one edge per central wire loses dimension and $L<N/2$ leaves $N-2L>0$ spare."),
        inf("KEY.1.5",
            "The bit network's matrices obey $M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m$ for every input role $w$.",
            "M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m"),
        inf("KEY.1.6",
            "The rank sum $s_{\\rm b}=W_{\\rm b}m-N+2L_{\\rm b}$ falls short of $W_{\\rm b}m$ by $N-2L_{\\rm b}>0$ (the $N$ negative source projections cost one extra rank each).",
            "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$."),
    ],
    page="bit-network",
    frm=["network", "frames", "subset-labels", "rank-saving", "matrix-basics"],
    salient="The endpoint operator is the same address shear $(H,D)\\mapsto(H+D,D)$ on every one of the $W_{\\rm b}$ roles, scratch roles included, although every edge applies a different frame change.")

recurrence = show(
    "KEY.8",
    "With $s$ calls on streams of volume $V/W$ the normalized cost obeys $F_k\\le(s/W)F_{k-1}+O(1)$; since $s/W<m^\\tau$ this solves to $F_k=O(e^\\tau)$ for $e=m^k$.",
    "Unroll the recurrence into a geometric sum with ratio $s/W$ and compare it with $m^{k\\tau}$.",
    mot("Dividing the cost by the volume turns the $s$ calls on $1/W$-volume streams into a factor $s/W$ per level of recursion, and $m^k=e$ levels' growth is read off the geometric sum.",
        "recoverable"),
    [
        inf("KEY.8.1",
            "The number of recursive calls at a node is the sum of the edge ranks, exactly $s$.",
            "The number of recursive calls is the sum of the edge ranks, exactly $s$."),
        inf("KEY.8.2",
            "Each call acts on one role stream of volume $V/W$, so $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
            "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1)."),
        inf("KEY.8.3",
            "For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$, whether $a\\le1$ or $a>1$.",
            "For $a=s/W<m^\\tau$ the geometric sum"),
        inf("KEY.8.4",
            "Hence $F_k=O(e^\\tau)$.",
            "Hence $F_k=O(e^\\tau)$."),
    ],
    page="power-saving-recurrence",
    frm=["rank-saving", "proof-by-induction-and-recursion", "logarithms-and-exponentials", "asymptotic-notation-beyond-big-o"],
    salient="The normalized cost grows like $(s/W)^k$, below $m^{k\\tau}=e^{\\tau}$ with $\\tau=1-2^{-50}$ barely less than $1$: only the strict inequality $s<Wm$ matters, not how large the deficit is.")

key = show(
    "KEY",
    "Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time by running a fixed exchange network of $W$ wires whose edges are smaller interchanges, with $s<Wm$ smaller calls in all.",
    "Exchange the chunks with a shear $H\\leftarrow H+D$ run through the bit network on $W$ role streams of volume $V/W$, implement each edge by smaller interchanges, and solve the recursion.",
    mot("The cost per unit volume is multiplied by $s/W$ at each level; because the sum of ranks $s$ is less than the number of wires times $m$, this multiplier is below $m$ and the recursion saves a power of the chunk width.",
        "explicit", "is the source of the power saving."),
    [
        bit_network,
        inf("KEY.2",
            "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with exactly $a$ ones.",
            "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
            page="lower-triangular",
            frm=["matrix-basics", "vectors-matrices-and-linear-maps"]),
        show("KEY.3",
             "The shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ for a rank-$a$ rational $m\\times m$ matrix $A$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
             "Conjugate the partial permutation $\\Pi$ by lower-triangular controlled shifts and turn each of its $a$ ones into one field interchange.",
             mot("Lower-triangular updates target later fields from earlier ones and so are linear time; only the ones of $\\Pi$ need real interchanges, which is why the number of recursive calls is the rank.",
                 "recoverable"),
             [
                 inf("KEY.3.1",
                     "A lower triangular transformation of the $H$ or $D$ fields costs $O(V)$, updating coordinates in descending physical order.",
                     "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
                 inf("KEY.3.2",
                     "For $A=E_1\\Pi E_2$: transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
                     "For $A=E_1\\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
                 inf("KEY.3.3",
                     "Each one of $\\Pi$ calls for $H_i\\leftarrow H_i+D_j$, done with two linear updates and one interchange, so there are $a$ interchanges in all.",
                     "It uses just one interchange."),
             ],
             page="matrix-shear",
             frm=["lower-triangular", "controlled-shifts", "array-order", "modular-arithmetic"]),
        inf("KEY.4",
            "Split whole rows cyclically into $W$ role streams, each of volume $V/W$ with the same address set.",
            "Split whole rows cyclically into $W$ role streams within each prefix"),
        inf("KEY.5",
            "On every circuit edge apply the shear $\\Phi_{A_e}$ to that role stream, recursively interchanging each pivot pair of $b$-digit fields, and run the gates pointwise.",
            "$\\Phi_{A_e}$ to that role stream; implement it by"),
        inf("KEY.6",
            "Merging the rows back undoes the role permutation, and the common-frame identity leaves $H\\leftarrow H+D$ on every original row, scratch rows included.",
            "Merge by returning row $g$ of"),
        inf("KEY.7",
            "The three updates $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange the chunks; only the middle shear uses the circuit.",
            "To interchange the two full chunks, perform"),
        recurrence,
    ],
    page="power-interchange",
    frm=["bit-network", "matrix-shear", "stream-ops", "frames"],
    salient="The saving is a power $e^{\\tau}$, $\\tau=1-2^{-50}$, rather than a log factor, and it comes from the single strict inequality $s<Wm$ although the chunks are moved only by XOR combinations that finally form an exact permutation.",
    adds=[
        b("W", "wire count", "The number of wires (roles) in the fixed exchange network.", "count"),
        b("m", "label dimension", "The number of digit fields in each address chunk, i.e. the dimension of the label space.", "count"),
        b("s", "total edge rank", "The sum of the ranks of all edge matrices, equal to the number of smaller interchange calls.", "count"),
        b("\\tau", "interchange exponent", "A fixed exponent below $1$ with $s/W<m^\\tau$.", "direct"),
    ])

chunk_int = show(
    "R1",
    "Two disjoint address chunks of $u$ bits, with any prefix, gap and suffix, can be interchanged in $O(Vu^\\tau)$ tape steps for a fixed $\\tau<1$.",
    "Move the top digits of both chunks into a row field, pad rows to a multiple of $W^k$, write the remaining width in base $m$ and apply the power-width interchange to each base-$m$ piece.",
    mot("The recursion handles only widths $m^k$ with enough rows, and the rows can be supplied by a few of the array's own high digits.",
        "explicit", "We have proved the fast operation for power widths with enough rows."),
    [
        key,
        inf("R1.1",
            "Write each chunk as its top $\\rho$ digits followed by the rest, interchange the high digits one pair at a time and join them as a row field of range at least $W^k$.",
            "Write each chunk as its top $\\rho$ digits followed by its remaining"),
        inf("R1.2",
            "Append zero rows within each prefix so the row count is a multiple of $W^k$, at most doubling the volume.",
            "Append zero rows, separately within"),
        inf("R1.3",
            "Write the remaining width in base $m$ and split each chunk into $a_j$ pieces of width $m^j$.",
            "Write the remaining width in base $m$:"),
        inf("R1.4",
            "Applying the power-width interchange to each piece costs $O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)$.",
            "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau)."),
        inf("R1.5",
            "Padding binary chunks to radix-$q$ ranges costs a fixed factor, and $e=O(u)$ gives the bound $O(Vu^\\tau)$.",
            "Since $e=O(u)$ for fixed $q$, the bound is"),
    ],
    page="chunk-interchange",
    frm=["power-interchange", "stream-ops", "array-order", "floor-ceiling-and-rounding"])

# ---------------- simultaneous butterfly layer ----------------
packed = show(
    "R2.4",
    "The XOR $y\\leftarrow y\\oplus x$ on the same bit position of $f$ chunks at once, restoring a third scratch chunk, takes $O(V(L^\\tau+1))$ time using eight cyclic shifts of whole chunk ranges plus a deterministic repair.",
    "Perform eight carry-free cyclic shifts that act correctly away from a small set of addresses whose guard values fail, then fix that set by sorting.",
    mot("A whole-chunk shift adds the same offset to $f$ packed segments at once, but carries between segments are only avoided when guard values stay in range; the few addresses where they fail are exactly identified by their addresses and corrected by sorting.",
        "recoverable"),
    [
        inf("R2.4.1",
            "The eight conditional additions to $u$ and $w$ flip the parity of $u$ exactly when $c=1$ and restore $w$.",
            "Consequently the complete output is"),
        inf("R2.4.2",
            "The excluded guard values number twenty per guard, so the bad addresses are at most a fraction $\\delta_{\\rm bad}=\\min\\{1,80(f-1)2^{-K}\\}$.",
            "There are exactly twenty excluded values for each guard in"),
        inf("R2.4.3",
            "The exceptional records are extracted, stably radix-sorted by destination rank and reinserted, which costs little because the bad fraction is tiny.",
            "while stable binary radix sorting scans only the extracted records and"),
    ],
    page="packed-bit-addition",
    frm=["chunk-interchange", "controlled-shifts", "stream-ops"])

layer = show(
    "R2",
    "Applying $H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ at one bit position in each of $D\\le d$ equal-width address chunks costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$, with one final truncation.",
    "Rewrite $H_0^{\\otimes D}$ through the phase kernel $C$, evaluate $C^{\\otimes D}$ by the complex phase network whose edge calls are smaller layers on $1/W$-volume row streams, and implement the binary basis changes by packed address-bit additions.",
    mot("Separate butterfly factors would require $D$ whole-array passes, one per axis, whereas one network call handles many axes together.",
        "explicit", "factors would require $D$ whole-array passes."),
    [
        inf("R2.1",
            "The complex network with binary labels factors each edge's phase-frame change into $s_{\\rm c}$ translation kernels $aI+bX_v$ in total, with $s_{\\rm c}<W_{\\rm c}m$, and yields $C^{\\otimes m}$ on every role.",
            "After source and sink diagonal corrections, and undoing the signed",
            page="phase-network",
            frm=["network", "frames", "subset-labels", "rank-saving", "complex-numbers", "dyadic-rationals-and-binary-fractions", "binary-field-f2-and-xor"],
            deferred=True,
            salient="Whatever the edge-by-edge phase frames, the endpoint operator is the same $C^{\\otimes m}$ on every role, scratch roles included, just as the shear was for the bit network."),
        inf("R2.2",
            "Applying the network to a group of $e=mf$ selected axes gives exactly $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",
            "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot."),
        inf("R2.3",
            "The normalized layer is recovered from the $C$ layer by diagonal phases: $H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D$.",
            "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."),
        packed,
        inf("R2.5",
            "A row index $u=Wg+w$ sends each whole row to role $w$, so every child call acts on a stream of exactly $1/W$ of the parent's volume.",
            "At a node, write a row index as \\(u=Wg+w\\), with \\(0\\le w<W\\),"),
        inf("R2.6",
            "The normalized cost satisfies $F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1)$, with leaves of fewer than $d^{\\beta}$ chunks handled by individual kernels.",
            "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),"),
        inf("R2.7",
            "Summing the internal costs, the leaves and the base-$m$ groups gives total time $O(Vd^{\\lambda'})$ on fixed tapes.",
            "above give total time $O(Vd^{\\lambda'})$ on fixed tapes, including"),
        inf("R2.8",
            "The guard-width calculation bounds denominator and magnitude growth by $\\lceil C_0d^{C_1}\\rceil=o(p)$ bits, so all intermediate dyadics are exact in $O(p)$ bits before one final truncation.",
            "The guard-width calculation above bounds both denominator and magnitude"),
    ],
    page="simultaneous-layer",
    frm=["phase-network", "packed-bit-addition", "chunk-interchange", "power-saving-recurrence", "butterfly-fft", "fixed-point-disk-grid"])

tools = show(
    "T",
    "There are two fixed-tape procedures whose cost beats a full scan per level by a power: an address-chunk interchange in $O(Vu^\\tau)$ and a simultaneous butterfly layer in $O(Vd^{\\lambda'})$.",
    "Build each procedure from a fixed linear network that exchanges two banks of values and restores its scratch values, and apply it recursively with a strict rank deficit.",
    mot("Scanning the whole array at each of the logarithmically many transform levels already costs $n\\log n$, so both the data movement and the butterfly arithmetic must be cheaper than a scan.",
        "explicit", "We therefore need savings in both movement and arithmetic."),
    [
        inf("T.1",
            "Fixed-radix digit permutations, digit moves, splits by a digit, pointwise maps, merges and cyclic row splitting into a fixed number of streams each take $O(V)$ steps.",
            "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
            page="stream-ops",
            frm=["fixed-tape-model", "array-order", "tape-machines"]),
        inf("T.2",
            "Updating a target field by an offset computed from earlier control fields modulo $q^b$, or multiplying it by a fixed rational unit, costs $O(V)$.",
            "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
            page="controlled-shifts",
            frm=["array-order", "stream-ops", "modular-arithmetic", "primes-coprimality-and-gcd"]),
        chunk_int,
        layer,
    ])

# ---------------- transforms ----------------
layout = show(
    "R3.5",
    "On a layout placing the selected bits of all axes at a common offset in consecutive chunks, a forward and an opposite synthetic transform cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$, keeping the bit-reversed frequency order.",
    "Move a few bit slots to a prefix, exchange width-$K$ chunks into round-major order, and run one simultaneous layer per round.",
    mot("The simultaneous layer needs the selected bits of the participating axes at the same offset in consecutive chunks.",
        "explicit", "we must place the selected bits of the participating axes at a common"),
    [
        inf("R3.5.1",
            "At most $D(b+1)=O(dK)$ listed bit slots are moved to a prefix, and the rounds on them are done bit by bit.",
            "There are at most $D(b+1)=O(dK)$"),
        inf("R3.5.2",
            "At most $Dq-1$ chunk exchanges of width $K$ reorder the remaining chunks, costing $O(Tp\\cdot pK^{\\tau-1})$.",
            "O\\bigl(Tp\\,DqK^\\tau\\bigr)"),
        inf("R3.5.3",
            "Each remaining round is one simultaneous layer, costing $O(Tp\\,d^{\\lambda'})$ per round and $O(Tp\\,\\ell\\,d^{\\lambda'})$ in all.",
            "The simultaneous-layer procedure therefore applies at cost"),
        inf("R3.5.4",
            "Each of at most $\\ell$ rounds adds one truncation error below $\\sqrt2\\,2^{-p}$ and contractions do not amplify it, while layout permutations are isometries.",
            "give the claimed error and disk bounds."),
        inf("R3.5.5",
            "The exact operators are $LBF_{\\boldsymbol t}^-$ forward and $F_{\\boldsymbol t}^+B^{-1}L^{-1}$ for the opposite procedure, which consumes the stored order.",
            "(L\\mathcal D_-L^{-1})L=LB F_{\\boldsymbol t}^-,"),
    ],
    page="transform-layout",
    frm=["synthetic-transform", "simultaneous-layer", "chunk-interchange", "stream-ops"])

synth = show(
    "R3",
    "Normalized Fourier-type transforms of arrays of polynomials modulo $y^r+1$, with roots of unity $\\omega_t=y^{2r/t}$, need arithmetic only in butterflies, leave outputs in bit-reversed slot order, and have an opposite transform that consumes that order.",
    "Run radix-2 decimation in frequency with the roots $y^{2r/t}$, group the rounds over all axes as a parallel butterfly followed by a monomial shift, and track the stored frequency order.",
    mot("Multiplication by a power of $y$ is a signed shift of the coefficient list, so the twiddle factors cost no arithmetic.",
        "explicit", "where the required roots of unity act by exact signed permutations"),
    [
        inf("R3.1",
            "For a power of two $t$ dividing $2r$, set $\\omega_t=y^{2r/t}$; every power of $\\omega_t$ is an isometry, so both transforms are contractions.",
            "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$."),
        inf("R3.2",
            "The synthetic characters cancel: $\\sum_k\\omega_t^{jk}$ is $t$ if $t\\mid j$ and $0$ otherwise, so $F_t^+F_t^-=t^{-1}I$.",
            "\\qquad F_t^+F_t^-=t^{-1}I."),
        inf("R3.3",
            "The recursion implements $B_tF_t^-$ and $F_t^+B_t^{-1}$, where $B_t$ is the bit-reversal record permutation.",
            "B_tF_t^-,\\qquad F_t^+B_t^{-1},"),
        inf("R3.4",
            "The axis steps of a round group as one parallel butterfly followed by one recordwise monomial $y^E$ with an address-dependent exponent $E$.",
            "Consequently the individual axis steps may be grouped as a parallel"),
        layout,
    ],
    page="synthetic-transform",
    frm=["polynomial-ring-mod", "butterfly-fft", "dft", "multidim-transform", "simultaneous-layer"])

kron = show(
    "R4.1",
    "Two ring polynomials with $O(p)$-bit Gaussian-integer coefficients are multiplied exactly by evaluating at $B_0=2^{4p}$ as signed integers, using the $O(N\\log N)$ integer multiplier, extracting centered coefficients and wrapping negacyclically, in $O(rp\\log(rp))$ time.",
    "Use Kronecker substitution with signed packing: evaluate at a large power of two, multiply the evaluation integers, and read the coefficients back.",
    mot("Evaluating at $B_0$ turns polynomial multiplication into integer multiplication, and the coefficients can be read back because every product coefficient is smaller than $B_0/2$ in absolute value.",
        "recoverable"),
    [
        inf("R4.1.1",
            "Writing $f,g$ with integer numerators of degree below $r$, set $B_0=2^{4p}$ and form the signed evaluation integers $A_u=u(B_0)$.",
            "coefficients of absolute value at most $2^p$.  Set $B_0=2^{4p}$"),
        inf("R4.1.2",
            "The four products of evaluation integers are computed with the established multiplier on their absolute values, restoring signs.",
            "pairs of absolute values using the established multiplier and restore"),
        inf("R4.1.3",
            "Every product coefficient satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so a centered residue identifies each coefficient in turn.",
            "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2."),
        inf("R4.1.4",
            "The real and imaginary parts are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
            "The real and imaginary numerator streams are respectively"),
        inf("R4.1.5",
            "Four exact integer products dominate the linear packing, extraction and truncation costs.",
            "Four exact integer products dominate the linear"),
    ],
    page="kronecker-packing",
    frm=["nlogn-multiplier", "polynomial-ring-mod", "positional-number-representation-and-carries"])

ringconv = show(
    "R4",
    "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\\mathbb C[y]/(y^r+1)$ is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ time.",
    "Transform both operands forward, multiply pointwise in the stored order using signed packing, and apply the opposite transform to that order.",
    mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs need not be reordered before the product.",
        "explicit", "forward outputs in their retained order and pass that order directly"),
    [
        kron,
        inf("R4.2",
            "Perform both forward transforms, retain their common $LB$ order, multiply the corresponding polynomial records with the packing lemma, apply the opposite procedure and scale by $M=T/r$.",
            "Perform both forward transforms and retain their common $LB$ order."),
        inf("R4.3",
            "Expanding the finite sums gives $F^-_{\\boldsymbol t}(f*g)=M(F^-_{\\boldsymbol t}f)(F^-_{\\boldsymbol t}g)$, so the scaled opposite transform of the product is $(f*g)/(rM)$.",
            "To check normalization, expansion of the finite sums gives"),
        inf("R4.4",
            "Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite procedure applied to stored outputs gives the convolution.",
            "Since $LB$ permutes records and leaves their polynomial suffixes"),
        inf("R4.5",
            "The three transform errors and the product truncation total error less than $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$ after scaling.",
            "$M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$, as claimed."),
    ],
    page="ring-convolution",
    frm=["transform-layout", "kronecker-packing", "convolution-theorem", "cyclic-convolution", "synthetic-transform"])

xform = show(
    "X",
    "The normalized convolution over power-of-two axes needed by the multiplication is available, with every cost and error bound, from the synthetic transforms.",
    "Build the polynomial-ring convolution from the retained-order synthetic transforms and the signed packing multiplication.",
    mot("The final convolutions are over rings in which the roots of unity are exact signed shifts, so the faster layers can be applied to every round.",
        "reconstructed"),
    [synth, ringconv])

# ---------------- resampling group ----------------
gres = show(
    "G.1",
    "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, and tensoring over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with the permutations $R,Q$ retained.",
    "Use the Gaussian identity of Harvey and van der Hoeven, rescale so both maps are contractions, and keep the coordinate permutations inside the formula.",
    mot("The product needs transforms of pairwise coprime lengths while the synthetic transforms use powers of two, and Gaussian resampling connects these two shapes.",
        "explicit", "The transform lengths needed for the integer product are pairwise coprime,"),
    [
        inf("G.1.1",
            "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.",
            "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA."),
        inf("G.1.2",
            "Setting $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$ with the stated normalizations makes both contractions and gives $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
            "Now set $A=\\mathsf S'$ and $B_0=\\mathsf D'\\mathsf J'C$."),
        inf("G.1.3",
            "Tensoring the one-dimensional identity over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, and the linewise maps cost $O(dTp^{3/2+\\delta}\\alpha)$.",
            "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
    ],
    page="gaussian-resampling",
    frm=["dft", "fixed-point-disk-grid", "exponential-function-and-gaussian-function", "multidim-transform", "chunk-interchange", "nlogn-multiplier"])

chirp = show(
    "G.2",
    "For the chirp array $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, the permuted transform is $QF_{\\boldsymbol t}u=\\overline a\\cdot\\bigl(a*(\\overline a\\cdot u)\\bigr)/T$.",
    "Expand the right side coefficient by coefficient and compare with the matrix entries of $QF_{\\boldsymbol t}$.",
    mot("The middle transform has length not suited to the synthetic transforms, but writing $jk$ as a difference of squares turns it into a cyclic convolution with a chirp between two pointwise phase multiplications.",
        "recoverable"),
    [
        inf("G.2.1",
            "The chirp $a$ has period $t_i$ in coordinate $i$, since replacing $j_i$ by $j_i+t_i$ changes the exponent by an integral multiple of $2\\pi i$.",
            "Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
        inf("G.2.2",
            "The coefficient of $u_{\\boldsymbol k}$ on the right equals $\\frac1T\\exp(2\\pi i\\sum_i s_ij_ik_i/t_i)$, which is the coefficient in $QF_{\\boldsymbol t}$.",
            "This is precisely the coefficient in $QF_{\\boldsymbol t}$, because"),
    ],
    page="chirp-identity",
    frm=["dft", "cyclic-convolution", "multidim-transform", "gaussian-resampling"])

permc = show(
    "G.3",
    "The retained source permutation cancels: $(RF_{\\boldsymbol s}^+)\\bigl[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)\\bigr]=(u*v)/S^2$ with $S=\\prod_is_i$, so no sort is executed.",
    "Show that $R$ commutes appropriately with the opposite transform, so that $RF^+R=F^+$, and then apply the normalized convolution rule.",
    mot("A coordinate dilation by a unit moves the opposite transform to the inverse dilation, so the dilation retained after one forward transform and the one retained before the opposite transform undo each other.",
        "recoverable"),
    [
        inf("G.3.1",
            "For a unit $c$ modulo $q$, $F_q^+R_c=R_c^{-1}F_q^+$, hence $RF_{\\boldsymbol s}^+R=F_{\\boldsymbol s}^+$.",
            "$F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence"),
        inf("G.3.2",
            "Therefore $RF^+_{\\boldsymbol s}[R(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)]=F^+_{\\boldsymbol s}(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products.",
            "because a coordinate permutation commutes with pointwise products."),
        inf("G.3.3",
            "The two normalizations give $F_{\\boldsymbol s}^+(F_{\\boldsymbol s}u\\cdot F_{\\boldsymbol s}v)=(u*v)/S^2$.",
            "proving \\eqref{eq:source-permutation-cancel}."),
    ],
    page="permutation-cancellation",
    frm=["dft", "convolution-theorem", "gaussian-resampling"],
    salient="The output $(u*v)/S^2$ does not involve the permutation $R$ at all, although each forward transform carries it, because $R$ is its own conjugator of $F^+$.")

resamp = show(
    "G",
    "The transform of pairwise coprime lengths $s_i$ is expressible through power-of-two tensor transforms, a chirp convolution, and a cancellation of the retained permutation.",
    "Retain the source and target coordinate permutations in the identity instead of executing sorts, and use Bluestein's chirp for the middle transform.",
    mot("The usual implementation of Gaussian resampling sorts twice on each coordinate, which is too expensive, so both permutations are retained in the transform formula.",
        "explicit", "We retain both permutations in the transform formula and"),
    [gres, chirp, permc])

# ---------------- assembly ----------------
primes = show(
    "PB.2",
    "Distinct odd primes $s_i\\in((1-2\\eta)t_i,(1-\\eta)t_i]$ exist and are found deterministically in time $n^{o(1)}$, with $T/2<S<T$ and every resampling hypothesis satisfied.",
    "Quote the explicit prime-interval bound, check the two intervals are disjoint and rich in primes, and multiply the lower bounds.",
    mot("The primes must be close to the powers of two so their product fills a fixed fraction of the padded box, while the ratios $t_i/s_i$ must stay separated from $1$ for resampling.",
        "explicit", "The distinct prime lengths $s_i$ must be close to the powers of two"),
    [
        inf("PB.2.1",
            "For $0<\\eta<1/4$ and $x>e^{2/\\eta}$ the interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains at least $\\eta x/(2\\log x)$ primes.",
            "contains at least $\\eta x/(2\\log x)$ primes."),
        inf("PB.2.2",
            "Choose distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ near the powers of two $t_i$.",
            "We may therefore choose distinct odd primes satisfying"),
        inf("PB.2.3",
            "Multiplying the bounds with Bernoulli's inequality gives $T/2<S<T$.",
            "Together with $s_i<t_i$, this gives $T/2<S<T$."),
        inf("PB.2.4",
            "Every hypothesis of the one-dimensional resampling lemma holds for large $n$, with $\\alpha^4\\theta_i>p$.",
            "Thus every hypothesis of Lemma~\\ref{lem:no-sort-resampling} holds for"),
        inf("PB.2.5",
            "The machine finds the primes by scanning the two intervals and trial division, in time $n^{o(1)}=o(n)$.",
            "The machine finds these primes by scanning the two intervals"),
    ],
    page="prime-lengths",
    frm=["primes-coprimality-and-gcd", "logarithms-and-exponentials"])

crt = show(
    "PB.3.2",
    "The map $\\Phi:x\\mapsto\\prod_ix_i^{\\mu_i}$ is a ring isomorphism from cyclic convolution of length $S=s_1\\cdots s_d$ to $d$-dimensional cyclic convolution on the prime axes, performed on tape by triangular prefix-controlled cyclic shifts in $O(Tp\\,d^2(1+\\ell^\\tau))$.",
    "Use the Chinese remainder theorem with coordinate powers $\\mu_i=P_i^{-1}$ chosen so that axis $i$ depends only on lower-index digits, which makes the change of order a sequence of controlled shifts.",
    mot("With these powers the new coordinate $b_i$ is $a_i$ plus a multiple of the lower digits modulo $s_i$, a shift of a later field controlled by earlier fields.",
        "recoverable"),
    [
        inf("PB.3.2.1",
            "The assignment $\\Phi$ sends $x$ to an element of order $S$, so it is an isomorphism and preserves cyclic convolution.",
            "$\\Phi$ is an isomorphism and preserves cyclic convolution."),
        inf("PB.3.2.2",
            "Each triangular update $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j$ is a prefix-controlled cyclic shift of the valid interval, preserving zero padding.",
            "Each triangular update is a prefix-controlled cyclic shift."),
        inf("PB.3.2.3",
            "Exchanging axes of widths $\\ell$ or $\\ell-1$ costs $O(d^2)$ chunk swaps, so $\\Phi$ and its inverse cost $O(Tp\\,d^2(1+\\ell^\\tau))$.",
            "their padding operations cost"),
    ],
    page="crt-axis-map",
    frm=["cyclic-convolution", "controlled-shifts", "chunk-interchange", "primes-coprimality-and-gcd", "modular-arithmetic"])

twist = show(
    "PB.3.3.1",
    "Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ is a ring isomorphism from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathbb C[y]/(y^r+1)$ whose negative wrap cancels the twist.",
    "Check that $x_d\\mapsto\\zeta y$ is well defined and diagonal in the coefficient bases, then verify the wrap sign.",
    mot("Cyclic convolution wraps with sign $+1$ while the ring wraps with $-1$; the factor $\\zeta^r=-1$ compensates exactly.",
        "recoverable"),
    [
        inf("PB.3.3.1.1",
            "The map $x_d\\mapsto\\zeta y$ is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.",
            "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."),
        inf("PB.3.3.1.2",
            "A product term after twisting and negacyclic reduction has factor $\\zeta^{k+l}(-1)^h=\\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
            "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j."),
    ],
    page="negacyclic-twist",
    frm=["polynomial-ring-mod", "cyclic-convolution", "complex-numbers"])

cconv = show(
    "PB.3.3",
    "Normalized cyclic convolution $f*g/T$ of complex arrays on power-of-two axes is computed with error below $6TL\\cdot2^{-p}$ by twisting the last axis into the polynomial ring and using the ring convolution.",
    "Twist both operands with exact phases, convolve over the polynomial ring, and untwist the result.",
    mot("The ring convolution handles only the first $d-1$ axes over the ring, so the last scalar axis is made into the polynomial coefficient axis by a twist.",
        "recoverable"),
    [
        twist,
        inf("PB.3.3.2",
            "With $\\iota$ identifying the last axis with polynomial coefficients and $D_\\pm$ the diagonal twists, $\\mathcal M_{\\mathbb C}(f,g)=D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=f*g/T$.",
            "Consequently, with $\\mathcal M_r$ from"),
        inf("PB.3.3.3",
            "The computed version twists with truncated phases $f'=Q_p(\\widetilde\\theta^+\\cdot f)$, applies the ring convolution to $\\iota f',\\iota g'$ and untwists.",
            "f'&=Q_p(\\widetilde\\theta^+\\mathbin{\\cdot}f),"),
    ],
    page="complex-convolution",
    frm=["negacyclic-twist", "ring-convolution", "complex-numbers"])

srct = show(
    "PB.3.4",
    "The computed source transform $\\widetilde{\\mathscr F}$ approximates $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$ on disk-grid tensors of norm at most $.5$.",
    "Apply the Gaussian map $A$ line by line, the chirp transform through the complex convolution, the map $B_0$, and an exact power-of-two scale.",
    mot("This is the Gaussian-resampling identity executed with the chirp identity supplying the middle transform.",
        "reconstructed"),
    [
        inf("PB.3.4.1",
            "The chirp transform forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, then $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$, then $Q_p(\\overline{\\widetilde a}\\cdot y_0)$.",
            "x_0&=Q_p(\\overline{\\widetilde a}\\mathbin{\\cdot}x),"),
        inf("PB.3.4.2",
            "The source transform applies $\\mathcal A$, the chirp transform and $\\mathcal B_0$ and multiplies the numerators exactly by $2^\\gamma$; its exact counterpart is $RF_{\\boldsymbol s}$.",
            "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A"),
        inf("PB.3.4.3",
            "The opposite-sign procedure $\\overline{\\widetilde{\\mathscr F}(\\overline z)}$ has exact counterpart $RF_{\\boldsymbol s}^+$.",
            "its exact counterpart is $RF_{\\boldsymbol s}^{+}$ by"),
    ],
    page="source-transform",
    frm=["gaussian-resampling", "chirp-identity", "complex-convolution", "fixed-point-disk-grid"])

multalg = show(
    "PB.3",
    "The algorithm splits both inputs into radix-$2^b$ digits, applies $\\Phi$, computes the source transform of each, multiplies pointwise, applies the opposite transform with scalings, rounds and propagates carries to output exactly $2n$ bits.",
    "Reduce the product to a cyclic convolution of digit lists on coprime axes and evaluate it by the transform, pointwise product and inverse transform with the retained permutation cancelling.",
    mot("Splitting into digits turns the product into a convolution, and the convolution theorem turns the convolution into one pointwise product between a transform and its opposite.",
        "recoverable"),
    [
        inf("PB.3.1",
            "With $q=\\lceil n/b\\rceil$ digits per input, the product has degree below $S$, so convolution modulo $x^S-1$ has no wraparound.",
            "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
        crt,
        cconv,
        srct,
        inf("PB.3.5",
            "Multiply corresponding complex coefficients of $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$ exactly and truncate to $p$ fractional bits.",
            "Multiply corresponding complex coefficients exactly and truncate"),
        inf("PB.3.6",
            "Apply $\\widetilde{\\mathscr F}^{+}$ to the product, scale exactly by $S$ and then by $2^{2b+4}S$, round to integers, and apply $\\Phi^{-1}$ with padding removal.",
            "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid"),
        inf("PB.3.7",
            "The two occurrences of $S$ undo different normalizations: the exact counterpart after three transforms is $(u*v)/S^2$.",
            "The two occurrences of $S$ in this algorithm undo different"),
    ],
    page="mult-algorithm",
    frm=["int-as-convolution", "crt-axis-map", "source-transform", "permutation-cancellation", "exact-recovery"])

exact = show(
    "PB.4",
    "The computed coefficients have absolute error below $1/2$, so rounding gives the integer convolution coefficients and radix-$2^b$ carries produce the exact $2n$-bit product.",
    "Track disk bounds and errors through every scaled call, then bound the final error by $448b\\,2^{-3b/4}<1/2$.",
    mot("Rounding recovers the exact integer coefficients only if the accumulated error is strictly below one half, which requires each scale factor to be paid for by the $6b$ fractional bits.",
        "recoverable"),
    [
        inf("PB.4.1",
            "The product $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ differs from $U\\cdot V_1$ by less than $(2E_s+2)2^{-p}$.",
            "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$."),
        inf("PB.4.2",
            "The unscaled integer coefficient array is $2^{2b+4}Sw$, where the second occurrence of $S$ reverses the remaining normalization.",
            "In tensor order, the unscaled integer coefficient array is"),
        inf("PB.4.3",
            "The final absolute error is less than $448b\\,2^{-3b/4}<1/2$, so the nearest integer is the unique correct coefficient.",
            "\\le448b\\,2^{-3b/4}<\\frac12."),
        inf("PB.4.4",
            "The carry recurrence $d_j=(c_j+k_j)\\bmod 2^b$, $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ keeps $0\\le k_j<2^{2b}$ and fixes the first $j$ radix digits.",
            "To propagate carries, let $Q_0=2^b$."),
        inf("PB.4.5",
            "Dropping the zero bits above position $2n-1$ yields exactly $2n$ output bits, also for zero inputs.",
            "Remove only those zero padding bits and retain leading zeros as needed"),
    ],
    page="exact-recovery",
    frm=["fixed-point-disk-grid", "positional-number-representation-and-carries", "vector-norms-and-error-bounds", "floor-ceiling-and-rounding"])

cost = show(
    "PB.5",
    "Each of the seven dominant rows of the cost table, divided by $Tp$, is at most $p^{1-2\\kappa}$, so the total time is $O(n(\\log n)^{1-\\kappa})$.",
    "Compare each cost row with its margin $g_i$ below one and absorb any fixed power of $\\log p$ into the slack $\\kappa$.",
    mot("Every row must fall below $p^{1}$ by a margin, because only then does the total drop below $n\\log n$ by a power.",
        "reconstructed"),
    [
        inf("PB.5.1",
            "The seven dominant powers of $p$ have margins $g_1,\\ldots,g_7$ below one.",
            "The seven dominant powers in Table~\\ref{tab:costs} have the following"),
        inf("PB.5.2",
            "Direct substitution gives $\\min_i g_i=2^{-181}=2\\kappa$.",
            "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
        inf("PB.5.3",
            "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
            "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
        inf("PB.5.4",
            "The complete large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
            "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."),
        inf("PB.5.5",
            "Below a fixed cutoff use schoolbook multiplication, giving one fixed-alphabet, fixed-tape deterministic machine with worst-case time $O(n(\\lg n)^{1-\\kappa})$.",
            "fixed-alphabet, fixed-tape deterministic machine has worst-case time"),
    ],
    salient="The exponent $\\kappa=2^{-182}$ is exactly half of the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$, the margin of the chunk-exchange row: the interchange exponent $\\tau$ barely below $1$ is the bottleneck.")

assembly = show(
    "PB",
    "With $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K$, $r$, $T$ and the tiny exponents fixed, the multiplication algorithm is correct and runs in $O(n(\\lg n)^{1-\\kappa})$ time.",
    "Fix compatible parameters, present the algorithm built from the transform machinery, prove the recovered coefficients round correctly, and add up the cost rows.",
    mot("Each cost row trades one saving against the growth of $d$, $K$ or $r$, so the parameters must be chosen together for every row to stay below one.",
        "explicit", "We choose compatible parameters for these procedures, recover"),
    [
        inf("PB.1",
            "Fixed rational exponents are $\\tau=\\sigma=1-2^{-50}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$, $C_1=20$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$.",
            "C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."),
        inf("PB.1.1",
            "Take $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, and $r=2^{\\lceil(\\log_2T)/d\\rceil}$, with $d$ axes of length $r/2$ or $r$.",
            "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"),
        primes,
        multalg,
        exact,
        cost,
    ],
    page="parameter-balance",
    frm=["prime-lengths", "chunk-interchange", "simultaneous-layer", "transform-layout"],
    adds=[
        b("p", "working precision", "The number of fractional bits of every stored complex coefficient, equal to $6b$.", "direct"),
        b("d", "axis count", "The number of axes of the padded box.", "count"),
        b("K", "chunk size", "The number of address bits in one chunk used by the butterfly layers.", "direct"),
        b("r", "ring dimension", "The number of coefficients of a ring polynomial, a power of two.", "count"),
        b("T", "box size", "The number of entries of the padded power-of-two box.", "count"),
    ])

root = show(
    "ROOT",
    "There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
    "Reduce the product to a digit convolution computed with Fourier-type transforms on power-of-two axes, and accelerate the transforms' address rearrangements and butterfly layers by a power of the logarithm.",
    mot("Scanning the array at each of the logarithmically many transform levels already costs $n\\log n$, so a power saving needs the movement and the arithmetic per level to be cheaper than a scan.",
        "explicit", "$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$."),
    [tools, xform, resamp, assembly],
    page="main-theorem",
    frm=["fixed-tape-model", "nlogn-conjecture", "big-o", "asymptotic-notation-beyond-big-o",
         "determinism-and-exact-versus-approximate-computation"])

answer = {"root": root}

# ---------------- validation ----------------
def walk(n, out):
    out.append(n)
    for c in n.get("children", []) or []:
        walk(c, out)

nodes = []
walk(root, nodes)
ids = [n["id"] for n in nodes]
assert len(ids) == len(set(ids)), "dup ids"
pos = -1
bad = 0
for n in nodes:
    qs = []
    if n["intention"] == "infer":
        qs.append(("quote", n["quote"]["quote"]))
    m = n.get("motivation")
    if m and m.get("quote"):
        qs.append(("mot", m["quote"]["quote"]))
    for kind, q in qs:
        c = TEXT.count(q)
        if c != 1:
            print("QUOTE COUNT", c, n["id"], kind, repr(q)); bad += 1
            continue
        if kind == "quote" and not n.get("deferred"):
            i = TEXT.index(q)
            if i < pos:
                print("ORDER", n["id"], repr(q)); bad += 1
            pos = max(pos, i)
pages = [n.get("page") for n in nodes if n.get("page")]
assert len(pages) == len(set(pages)), "dup pages"
print("pages used:", len(pages))
allpages = """fixed-tape-model nlogn-conjecture nlogn-multiplier array-order stream-ops controlled-shifts matrix-basics network frames subset-labels rank-saving bit-network lower-triangular matrix-shear power-saving-recurrence power-interchange chunk-interchange packed-bit-addition polynomial-ring-mod kronecker-packing cyclic-convolution int-as-convolution dft butterfly-fft phase-network fixed-point-disk-grid negacyclic-twist simultaneous-layer convolution-theorem multidim-transform synthetic-transform gaussian-resampling chirp-identity permutation-cancellation transform-layout ring-convolution crt-axis-map prime-lengths complex-convolution source-transform exact-recovery mult-algorithm parameter-balance main-theorem""".split()
froms = set()
for n in nodes:
    froms.update(n.get("from", []))
for p in allpages:
    if p not in pages and p not in froms:
        print("page unused", p); bad += 1
for p in pages:
    if p not in allpages: print("unknown page", p); bad += 1
# from order check
order = {p: i for i, p in enumerate(allpages)}
def check(n, cur):
    cur = n.get("page") or cur
    for f in n.get("from", []):
        if f in order and order[f] >= order[cur]:
            print("FROM ORDER", n["id"], f, cur); 
            global bad
            bad += 1
    for c in n.get("children", []) or []:
        check(c, cur)
check(root, "main-theorem")
print("bad", bad)
json.dump(answer, open(BASE + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1)
