import sys, json
sys.path.insert(0, 'exegenius/tasks/0003-argument')
from lib import *

# ---------------------------------------------------------------- T1, T2
t1 = infer(r"Fixed-radix digit permutations, digit moves, splitting on a digit with a pointwise map, and cyclic splitting of whole rows into a fixed number $W$ of equal streams each take $O(V)$ steps on a fixed number of tapes, for an array of stored volume $V$.",
           Q(493, "Each of the following operations on an array of", "tapes:"),
           frm=["array-order", "fixed-tape-model", "tape-machines"], page="stream-ops")

t2 = infer(r"Adding to a target address field an offset computed from earlier control fields modulo $q^b$ (a cyclic shift of blocks), or multiplying it by a fixed rational unit, takes $O(V)$ steps.",
           Q(566, "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the"),
           frm=["stream-ops", "array-order", "modular-arithmetic", "primes-coprimality-and-gcd"], page="controlled-shifts")

# ---------------------------------------------------------------- T3 networks
scalar = infer(r"For arbitrary initial values of its scratch wires, a forward invocation of the copy/gather/scatter/side-injection schedule changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged; three stages then exchange the banks, $(X_a,Y_a)\mapsto(-Y_a,X_a)$, and restore every scratch value.",
               Q(729, "For arbitrary initial values of its auxiliary wires, a forward", "unchanged."),
               frm=["sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor", "boolean-gates-and-circuits", "graphs"])

frames = infer(r"If every array on a wire is given an invertible frame $D_v$ at each vertex, a common frame commutes with a pointwise linear gate, so the network's overall effect is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: only the endpoint frames matter and each edge merely changes the frame.",
               Q(812, "Thus the common frame commutes with the pointwise gate, and", "the invariant continues to the sinks."),
               frm=["network", "vectors-matrices-and-linear-maps", "functions-bijections-and-permutations"], page="frames",
               salient="The intermediate frames cancel completely: the endpoint operator depends only on the source and sink frames of each role, however many gates the route crosses.")

labels = infer(r"Subspaces of the tensor-cube space $\mathcal F=F^{\otimes 3}$, built from indicator vectors of three-element subsets, label the gates so that labels are nested along every edge, neighboring subsets give orthogonal lines, and the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$.",
               Q(998, "Every edge joins comparable nondegenerate labels.", "loss is $h$."),
               frm=["matrix-basics", "network", "frames", "sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor", "vectors-matrices-and-linear-maps"], page="subset-labels",
               salient="All the dimension lost anywhere in the network is concentrated on one edge per central wire (time 3 to time 4), each losing exactly $h$; every other edge only grows its label, which is what makes the later deficit small.")

rank = show(r"The total number $s$ of smaller calls, the sum of the edge ranks of all labels, is strictly less than $Wm$, where $W$ is the number of wires and $m$ the dimension of the label space.",
            "Count dimension changes along edges: the signed changes telescope at gates to a fixed total, only one kind of edge decreases, so the sum of absolute changes exceeds the signed total by twice the small decreasing loss; the rational interface then adds one rank per source.",
            M("The count is organised to show that the dimension lost on decreasing edges is below half of the source dimension, and that the extra ranks needed by the interface still leave a strict deficit.", "explicit",
              Q(894, "We will obtain $L<N/2$. The rational interface below will require", "saving in both constructions.")),
            [
              infer(r"The signed dimension changes along all edges telescope at every gate, so since the sources have total dimension $N$ and the sinks $Wm-N$, they sum to $Wm-2N$.",
                    Q(1066, "The signed sum of dimension changes telescopes at every gate", "is therefore $Wm-2N$.")),
              infer(r"There are $Ic$ decreasing edges, each losing $h$, so the total loss is $L=Ich$ and the sum of absolute dimension changes is $Wm-2N+2L$.",
                    Q(1070, "There are $Ic$ decreasing edges, each of loss $h$;", "adds $2L$.")),
              infer(r"The loss is a small fraction of the source dimension: $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$, both smaller than $1/2$.",
                    Q(1110, "In particular, both are smaller than $1/2$.")),
              infer(r"The rational interface adds one rank for each of the $N$ negative source projections, so the edge ranks sum to $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, which is strictly below $W_{\rm b}m$ because $N-2L_{\rm b}>0$.",
                    Q(1163, "At stage 1, $B=0$,", "$N-2L_{\rm b}>0$.")),
            ],
            frm=["subset-labels", "matrix-basics", "frames"], page="rank-saving",
            salient="The deficit $Wm-s$ is only a relative sliver (about $10^{-11}$ of $Wm$), yet it is strictly positive; it exists because dimension is lost on a single edge per central wire, so $2L$ stays below the $N$ ranks that the interface adds. That strict inequality is the entire source of the power saving.",
            adds=[B("N", "bank size", "the number of data indices $a$, equal to the sum of the source label dimensions", "count"),
                  B("L", "dimension loss", "the total dimension lost on decreasing edges"),
                  ])

bitnet = infer(r"The bit network uses only XOR gates and rational labels whose frames are address shears, sends its input to the bank-exchanged permutation, and its endpoint matrices differ by $I_m$ on every input role, so the endpoint operator is $(H,D)\mapsto(H+D,D)$ with rank sum $s_{\rm b}<W_{\rm b}m$.",
               Q(1169, "For an input $X_a$ the endpoint difference is", "$P_{U_a^\\perp}-(-P_{U_a})=I_m$."),
               frm=["rank-saving", "frames", "subset-labels", "network", "matrix-basics", "vectors-matrices-and-linear-maps", "binary-field-f2-and-xor"], page="bit-network",
               salient="The same shear $H\\gets H+D$ appears on every role: data banks, swapped banks and scratch wires alike. For $X_a$ the difference $P_{U_a^\\perp}-(-P_{U_a})$ is the identity because the two projections are complementary, and for every other role it is the identity because the source matrix is zero.")

phase = show(r"The complex network with binary labels has edge frame changes equal to products of $s_{\rm c}<W_{\rm c}m$ two-point kernels $aI+bX_v$ (one per vector of an orthonormal residual basis), and after sign and phase corrections its endpoint operator is $C^{\otimes m}$ on every role.",
             "Compute the phase-weight difference across an edge from an orthonormal basis of the residual, turn each phase character into a translation kernel, count the kernels with the same rank budget, and telescope the endpoint frames.",
             M("Phases $i^{\\mathrm{wt}}$ are additive modulo four across orthogonal pieces, so an edge splits into one factor per residual basis vector, mirroring the rational construction with kernels in place of shears.", "recoverable"),
             [
               infer(r"For orthogonal $V=U\perp E$ with orthonormal basis $\mathcal B$ of $E$, the phase weight difference is $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\mathrm{wt}(v)[v\cdot x]\pmod 4$.",
                     Q(1241, "q_V(x)-q_U(x)=\\sum_{v\\in\\mathcal B}", "\\pmod4.")),
               infer(r"Each term $i^{\varepsilon[v\cdot x]}$ becomes the translation kernel $aI+bX_v$ or its inverse after conjugating by Hadamard matrices.",
                     Q(1256, "The displayed phase therefore", "$aI+bX_v$ or its inverse.")),
               infer(r"The same residual dimension count gives $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}$ kernels in all, with deficit $2N-2L_{\rm c}>0$.",
                     Q(1259, "The same lemma gives the count $s_{\\rm c}$.", "$2N-2L_{\\rm c}>0$.")),
               infer(r"After the $Z$ corrections on the 27 coordinates of the $X_a\to Y_a$ route, negating the physical $X$ outputs and undoing the bank exchange, every role, including every scratch role, carries the forward tensor product $C^{\otimes m}$.",
                     Q(1312, "Negate those outputs and send output role", "the required forward tensor product.")),
             ],
             frm=["bit-network", "rank-saving", "subset-labels", "frames", "butterfly-fft", "dft", "complex-numbers", "binary-field-f2-and-xor"], page="phase-network",
             salient="The endpoint operator is the same $C^{\\otimes m}$ on every role, scratch roles included, even though one route ($X_a\\to Y_a$) carries a different intermediate phase; the identity $C=iZC^{-1}Z$ repairs exactly the 27 inverse factors on that route.")

netcont = show(r"Two fixed linear networks exchange two banks of values with prescribed signs, return every scratch wire to its arbitrary initial value, and carry nested subspace labels whose edge ranks sum to $s<Wm$ for $W$ wires and label dimension $m$.",
               "Build a scalar schedule of copy, gather, scatter and side-injection gates that cancels arbitrary scratch values, lift it to arrays through frames, then attach nested subspace labels to its gates and count the dimension changes, once with rational labels (bits) and once with binary labels (phases).",
               M("Array operations on a tape are expensive to rearrange arbitrarily, so the exchange is designed as a fixed finite network in which each edge only changes a representation by an operator whose cost is measured by a rank.", "recoverable"),
               [scalar, frames, labels, rank, bitnet, phase],
               frm=["sets-subsets-and-basic-combinatorics", "binary-field-f2-and-xor", "boolean-gates-and-circuits", "graphs"], page="network",
               adds=[B("W", "wire count", "the number of wires, including scratch wires, of the network", "count"),
                     B("m", "label dimension", "the dimension of the fixed label space $\\mathcal F$, also the base in which chunk widths are split"),
                     B("s", "smaller calls", "the sum of the ranks (or dimension changes) over all edges, which is the number of smaller operations per network invocation", "count")])

# ---------------------------------------------------------------- T4 chunk interchange
lowtri = infer(r"Every rational matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation with exactly $a$ ones.",
               Q(1366, "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"),
               frm=["matrix-basics", "vectors-matrices-and-linear-maps"], page="lower-triangular")

mshear = infer(r"The shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ by a rational matrix $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.",
               Q(1405, "can be performed with exactly $a$ interchanges of pairs of $b$-digit", "further work."),
               frm=["lower-triangular", "controlled-shifts", "stream-ops", "matrix-basics", "modular-arithmetic", "primes-coprimality-and-gcd"], page="matrix-shear")

recur = show(r"Calling $s$ smaller interchanges, each on a stream of volume $V/W$, gives normalized cost $F_k\le (s/W)F_{k-1}+O(1)$, and since $s/W<m^\tau$ this solves to $F_k=O(e^\tau)$, a strict power saving.",
             "Write the cost per unit volume as a recurrence in which the number of children is the rank sum $s$ and each child has $1/W$ of the volume, then sum the geometric series using $s/W<m^\\tau$.",
             M("After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by only $s/W<m$; this strict inequality is the source of the power saving.", "explicit",
               Q(173, "After dividing cost by volume, multiplying the parameter by $m$", "is the source of the power saving.")),
             [
               infer(r"The number of recursive calls at a node is the sum of the edge ranks, exactly $s$, each on one role stream.",
                     Q(1543, "The number of recursive calls is the sum of the edge ranks, exactly $s$.")),
               infer(r"If $F_k$ is a uniform bound on time divided by logical volume at width $m^k$, then $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$.",
                     Q(1552, "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).")),
               infer(r"For $a=s/W<m^\tau$ the geometric sum $\sum_{j=0}^k a^j$ is $O(m^{k\tau})$, hence $F_k=O(e^\tau)$.",
                     Q(1554, "For $a=s/W<m^\\tau$ the geometric sum", "$F_k=O(e^\\tau)$.")),
             ],
             frm=["rank-saving", "bit-network", "matrix-shear", "proof-by-induction-and-recursion", "asymptotic-notation-beyond-big-o", "logarithms-and-exponentials"], page="power-saving-recurrence",
             salient="Only the ratio $s/W$ enters the recurrence, not $s$ itself: although each node makes $s$ child calls, each child touches only $1/W$ of the data, so the branching factor per unit volume is just below $m$ and the total grows like $e^\\tau$ with $\\tau<1$ instead of linearly in the width $e$.")

powint = show(r"Two disjoint chunks of $e=m^k$ radix-$q$ digits, in an array with enough rows, can be interchanged in $O(Ve^\tau)$ time by running the bit network on row streams with every edge shear done by smaller interchanges.",
              "Split the rows among the $W$ roles, apply the matrix shear on each network edge through recursive smaller interchanges, merge to obtain the shear $H\\leftarrow H+D$ on every row, compose three shears into a swap, and solve the resulting recurrence.",
              M("The bit network only exchanges banks of scalars; the row split supplies one stream per role so the frame identity turns its endpoint shear into the address shear, and three shears make an exact swap.", "recoverable"),
              [
                lowtri, mshear,
                infer(r"Whole rows are split cyclically into $W$ role streams within each prefix, each of volume $V/W$ and with the same remaining shape.",
                      Q(1497, "Split whole rows cyclically into $W$ role streams within each prefix", "preceding the row field.")),
                infer(r"On every circuit edge the shear $\Phi_{A_e}$ is applied to that role stream by the matrix-shear lemma, recursively interchanging each pivot pair of $b$-digit fields, while each gate runs pointwise at matching addresses.",
                      Q(1509, "On every circuit edge apply", "of $b$-digit fields.")),
                infer(r"By the common-frame identity the merged result is the shear $H\leftarrow H+D$ on every original row, including rows of scratch roles whose initial values were arbitrary.",
                      Q(1531, "is $H\\leftarrow H+D$ on every original row,", "initial values were arbitrary.")),
                infer(r"The three componentwise updates $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$ send $(H,D)$ to $(D,H)$; only the middle shear uses the network.",
                      Q(1535, "To interchange the two full chunks, perform", "sends $(H,D)$ to $(D,H)$.")),
                recur,
                infer(r"Scheduling the recursive calls depth-first on a fixed number of tapes, parking inactive role streams on a stack, adds only $O(V)$ at each node.",
                      Q(1584, "Each push, pop, copy, positioning operation, or erasure moves $O(V)$", "at a parent node.")),
              ],
              frm=["bit-network", "frames", "matrix-shear", "stream-ops", "array-order", "controlled-shifts"], page="power-interchange",
              adds=[B("e", "chunk width", "the number of radix-$q$ digits in each of the two chunks, a power $m^k$ of $m$", "count")])

chunk = show(r"Two disjoint address chunks of $u$ bits in an array of stored volume $V$ (with any prefix, gap and suffix) can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$, although intermediate steps form XOR combinations of data.",
             "Interchange chunks with a fixed bit-exchange network whose edge changes are address shears, each performed by a smaller interchange, run row-parallel on tape; then handle arbitrary widths and row counts by padding rows and splitting the width in base $m$.",
             M("Because the sum of the edge ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.", "explicit",
               Q(1352, "Because the sum of these ranks is less than the number of wires times", "saves a power of the chunk width.")),
             [
               powint,
               infer(r"Padding rows to a multiple of $W^k$ and cutting the width $e-\rho$ in base $m$ into pieces of widths $m^j$ gives total cost $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$, so any width $u$ costs $O(Vu^\tau)$.",
                     Q(1705, "O(V)\\sum_j a_jm^{j\\tau}=O(Ve^\\tau).")),
             ],
             frm=["bit-network", "rank-saving", "stream-ops", "controlled-shifts", "array-order", "frames"], page="chunk-interchange",
             adds=[B("\\tau", "interchange exponent", "a fixed rational exponent below $1$ with $s/W<m^\\tau$"),
                   B("u", "chunk width", "the number of bits in each of the two chunks", "count")])

# ---------------------------------------------------------------- T5 simultaneous layer
packed = show(r"Adding the selected bit of $x$ into $y$ at $f$ positions of two chunks at once, $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$, costs $O(V(L^\tau+1))$ plus a small correction term, using eight cyclic shifts of whole chunk ranges that restore a third scratch chunk.",
              "Use eight cyclic shifts that equal the desired XOR away from a small, explicitly identified set of addresses where guard values fail, then repair that set by extracting it, sorting by destination key and reinserting.",
              M("A rotation by whole chunk ranges is a linear-cost controlled shift, so the XORs at all $f$ positions are done together; the guard segments make the packing exact except on an address set whose size is bounded by the number of guards.", "explicit",
                Q(1947, "The construction first uses a constant number", "explicitly bounded set of\naddresses.")),
              [
                infer(r"The eight operations on a pair of integers flip the parity of $u$ exactly when the control is set, preserving both quotients and restoring the arbitrary auxiliary integer $w$.",
                      Q(2047, "Here $u\\bmod2\\in\\{0,1\\}$", "auxiliary integer $w$ is restored.")),
                infer(r"Away from the set $\mathcal B$ of addresses where a guard fails, the composition $S_0$ of the packed shifts agrees with the ideal XOR permutation $T_0$.",
                      Q(2092, "then agrees with the ideal permutation $T_0$", "fixes all other address coordinates.")),
                infer(r"Each guard excludes only twenty values out of $2^{K-1}$, so the bad set has size at most $\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.",
                      Q(2097, "There are exactly twenty excluded values for each guard in", "\\delta_{\\rm bad}M.")),
                infer(r"The records at bad addresses are extracted with destination keys, stably radix sorted, and reinserted, which implements $T_0$ everywhere.",
                      Q(2181, "Hold the full stream untouched", "This implements $T_0$ everywhere.")),
                infer(r"The total time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ on a fixed number of tapes.",
                      Q(2201, "Equation~\\eqref{eq:packed-bad-fraction} proves", "on a fixed number of tapes.")),
              ],
              frm=["chunk-interchange", "controlled-shifts", "stream-ops", "binary-field-f2-and-xor", "modular-arithmetic", "array-order"], page="packed-bit-addition")

simul = show(r"The two-point butterfly $H_0$ applied at one bit position in each of $D\le d$ equal-width address chunks of an array of complex fixed-point polynomial records costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, followed by one truncation, instead of $D$ whole-array passes.",
             "Express the layer through the complex phase network: $C^{\\otimes e}$ on $e=mf$ axes needs $s_{\\rm c}$ children on $f$ axes with binary basis changes done by packed selected-bit addition; split rows among the $W_{\\rm c}$ roles so children shrink, solve the recurrence, evaluate exactly in Gaussian dyadics, and convert to $H_0$ with a single truncation.",
             M("The phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis.", "explicit",
               Q(1799, "Its phase\nframes express a $C$ tensor product using smaller groups of\nselected bits, separated by binary changes of basis.")),
             [
               infer(r"An edge's phase-frame change is a product of directional kernels $(aI+bX_{v_j})^{\epsilon_j}$, one for each vector $v_j$ of an orthonormal basis of its residual.",
                     Q(1837, "gives the frame change", "\\epsilon_j\\in\\{1,-1\\}.")),
               infer(r"After an invertible binary change of coordinates on each column, each kernel is one child operation on the $f$ bits of one slot, an inverse kernel needing only a forward child with sign wrappers.",
                     Q(1880, "apply $(C^{\\epsilon_h})^{\\otimes f}$ to the", "on the $f$ axes in slot $h$.")),
               infer(r"One invocation of the complex network on $e=mf$ axes uses exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and produces $C^{\otimes e}$ on every role.",
                     Q(1905, "Summing its residual dimensions gives exactly", "one slot.")),
               infer(r"The normalized layer is recovered from the $C$ layer by diagonal phases: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.",
                     Q(1930, "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.")),
               packed,
               infer(r"Splitting rows among the roles gives each recursive edge call exactly $1/W$ of its parent's volume.",
                     Q(2331, "Each recursive edge call acts on", "logical\nvolume.")),
               infer(r"The normalized cost obeys $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, with $F(e)=O(e)$ below the cutoff $d^\beta$.",
                     Q(2407, "F(e)\\le (s/W)F(e/m)+O((eK)^\\tau+1),")),
               infer(r"Summing over a base-$m$ partition of the chunks gives total cost $O(d^{\lambda'})$ per unit volume for any fixed $\lambda'$ above $\max\{\lambda,\sigma+\beta(1-\sigma)\}$.",
                     Q(2436, "Adding their costs and the row preprocessing gives")),
               infer(r"Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer bits per real component, with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, represents every intermediate coefficient exactly.",
                     Q(2569, "Thus reserving \\(p+\\Delta\\)", "prevents overflow.")),
               infer(r"The row construction and recurrence analysis give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams.",
                     Q(2736, "The row construction and the recurrence analysis", "including all padded and auxiliary streams.")),
               infer(r"Each row of $\mathcal H$ has absolute row sum one, so disk arrays stay in the disk and truncation toward zero adds error below $\sqrt2\,2^{-p}$.",
                     Q(2751, "Finally, every row of $\\mathcal H$ has", "error less than $\\sqrt2\\,2^{-p}$:")),
             ],
             frm=["phase-network", "chunk-interchange", "rank-saving", "frames", "power-saving-recurrence", "butterfly-fft", "fixed-point-disk-grid", "polynomial-ring-mod", "stream-ops", "controlled-shifts"], page="simultaneous-layer",
             salient="The cost per unit volume grows like $d^{\\lambda'}$ with $\\lambda'<1$, so applying the butterfly to $d$ axes together is cheaper than $d$ separate linear passes; this follows from the branching ratio $s_{\\rm c}/W_{\\rm c}<m^{\\sigma}$ with $\\sigma<1$, exactly as for the address interchange.",
             adds=[B("d", "axis bound", "the largest number of axes whose butterfly is applied simultaneously", "count"),
                   B("K", "chunk bits", "the number of bits in each address chunk", "count"),
                   B("\\lambda'", "layer exponent", "a fixed rational exponent below $1$ for the cost $O(Vd^{\\lambda'})$ of a simultaneous layer")])

# ---------------------------------------------------------------- T6 ring convolution
synth = show(r"With roots $\omega_t=y^{2r/t}$ in $\mathbb C[y]/(y^r+1)$, the length-$t$ transforms $F_t^\pm$ are contractions computed by radix-2 decimation in frequency whose twiddles are signed shifts of coefficient lists; the outputs come out in bit-reversed order, which the reverse procedure consumes to give the opposite transform.",
             "Run the usual decimation-in-frequency FFT recursion in the ring where the roots of unity are powers of $y$, track where each frequency entry is stored, and run the recursion backward from that order.",
             M("Powers of $y$ are exact roots of unity whose multiplication is only a signed shift, so only butterflies cost arithmetic; the stored order must be tracked because the opposite transform will consume it after a pointwise product.", "recoverable"),
             [
               infer(r"For a power of two $t$ dividing $2r$, character sums cancel and $F_t^+F_t^-=t^{-1}I$, checked directly because the ring has zero divisors.",
                     Q(2816, "F_t^+F_t^-=t^{-1}I.")),
               infer(r"A decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the second output by $\omega_t^{-k}$, and recurses on both branches, computing $F_t^-$.",
                     Q(2835, "Multiply", "within the two branches.")),
               infer(r"After all rounds the entry $(F_t^-z)_j$ is stored at slot $\operatorname{rev}_a(j)$: frequency order is bit-reversed.",
                     Q(2866, "$\\operatorname{rev}_a(j)$ reverses the $a$ binary digits of $j$, the", "slot $\\operatorname{rev}_a(j)$.")),
               infer(r"Running the recursion backward from the stored order gives the two procedures $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the opposite transform consumes the bit-reversed order directly.",
                     Q(2881, "Thus the two", "exact procedures implement")),
               infer(r"On several axes the individual axis steps group into one parallel butterfly followed by one recordwise monomial operation $J_E$, a signed shift of the coefficient list.",
                     Q(2899, "Consequently the individual axis steps may be grouped as a parallel", "$J_E$.")),
             ],
             frm=["polynomial-ring-mod", "dft", "butterfly-fft", "multidim-transform", "convolution-theorem", "cyclic-convolution", "complex-numbers"], page="synthetic-transform",
             salient="The frequency entries come out in bit-reversed order at no extra cost and are never sorted; the reverse recursion is the exact inverse in that order, which is what lets the pointwise product sit between the two transforms.")

layout = show(r"Placing the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks makes each radix-two round one simultaneous layer, so a transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$, and the forward output keeps its layout $LB$ for the pointwise product.",
              "Move the top slots of each axis to a prefix, interchange chunks to line up the remaining bits, run each round as a simultaneous layer, and keep the layout and bit-reversed order through the pointwise product to the opposite transform.",
              M("The layer procedure needs the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks.", "explicit",
                Q(2918, "we must place the selected bits of the participating axes at a common", "offset in consecutive $K$-bit chunks.")),
              [
                infer(r"At most $D(b+1)=O(dK)$ slots are moved to a prefix by single-bit moves, costing $O(TpdK)$.",
                      Q(3007, "There are at most $D(b+1)=O(dK)$", "cost $O(TpdK)$.")),
                infer(r"At most $Dq-1$ exchanges of width-$K$ chunks, each costing $O(TpK^\tau)$, cost $O(Tp\,pK^{\tau-1})$ in all.",
                      Q(3023, "exchanges of width-$K$ address chunks", "all these exchanges cost")),
                infer(r"The simultaneous-layer procedure applies at cost $O(Tp\,d^{\lambda'})$ per round and $O(Tp\,\ell d^{\lambda'})$ in total.",
                      Q(3103, "The simultaneous-layer procedure therefore applies at cost", "in total.")),
                infer(r"One truncation after the exact round makes the computed result the same as truncating once, so at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$ and stay in the disk.",
                      Q(3166, "Thus the actual forward call sequence returns exactly the result of", "exact contraction round.")),
                infer(r"The forward entry with frequency address $j$ is stored at $L(Bj)$, so the exact operators are $LBF^-_{\boldsymbol t}$ and $F^+_{\boldsymbol t}B^{-1}L^{-1}$.",
                      Q(3194, "In particular, the forward entry with frequency address $j$ is", "stored at $L(Bj)$.")),
              ],
              frm=["synthetic-transform", "simultaneous-layer", "chunk-interchange", "stream-ops", "multidim-transform", "fixed-point-disk-grid", "polynomial-ring-mod"], page="transform-layout")

kron = show(r"Two disk-grid polynomials modulo $y^r+1$ can be multiplied exactly and returned as $Q_p(fg/r)$ in time $O(rp\log(rp))$ by evaluating at $B_0=2^{4p}$ as signed integers, four calls to the $O(N\log N)$ multiplier, centered extraction of coefficients, and negacyclic wrapping.",
            "Signed Kronecker substitution: pack each coefficient list into one integer with fields wide enough that coefficients of the ordinary product never overlap, multiply the integers, read the fields back by centered residues, and reduce modulo $y^r+1$.",
            M("A single integer product of $O(rp)$-bit numbers carries out a whole polynomial product, and the established $O(N\\log N)$ multiplier makes this affordable on short records.", "recoverable"),
            [
              infer(r"Each coefficient list becomes the signed integer $A_u=u(B_0)$ with $B_0=2^{4p}$, stored as a two's-complement string of $4p$-bit blocks.",
                    Q(3240, "Set $B_0=2^{4p}$", "define the signed evaluation integer")),
              infer(r"Every coefficient of the ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so fields never overlap.",
                    Q(3260, "|h_j|\\leq r2^{2p}<2^{3p}<B_0/2.")),
              infer(r"Reading blocks with a carry in $\{0,1\}$ and centering modulo $B_0$ recovers each coefficient $h_j$ exactly from the product integer.",
                    Q(3321, "Thus $\\widehat h_j=h_j$.")),
              infer(r"The real and imaginary numerator streams $ac-be$ and $ae+bc$ are reduced modulo $y^r+1$ by subtracting the coefficient at $j+r$ from the one at $j$.",
                    Q(3331, "The real and imaginary numerator streams are respectively", "for $0\\leq j<r$")),
            ],
            frm=["polynomial-ring-mod", "nlogn-multiplier", "positional-number-representation-and-carries", "complex-numbers", "fixed-tape-model"], page="kronecker-packing")

ringconv = show(r"The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on power-of-two axes is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ by two forward synthetic transforms, pointwise ring products by signed packing, and one opposite transform.",
                "Transform both operands in the same stored order, multiply pointwise in the ring with signed packing, apply the opposite transform consuming that order, and scale by the number of cyclic points; verify normalization and error by the convolution theorem.",
                M("Pointwise multiplication commutes with the same record permutation applied to both operands, so the product can be formed in the retained order and passed straight to the opposite procedure.", "explicit",
                  Q(3202, "Pointwise multiplication commutes with applying the same record", "permutation $LB$ to both operands.")),
                [
                  synth, layout, kron,
                  infer(r"Both forward transforms are performed and left in their common $LB$ order, the polynomial products are formed by the signed packing lemma, and the opposite procedure is applied to that order.",
                        Q(3415, "Perform both forward transforms and retain their common $LB$ order.")),
                  infer(r"Expanding the finite sums gives $F^-_{\boldsymbol t}(f*g)=M(F^-_{\boldsymbol t}f)(F^-_{\boldsymbol t}g)$, so with $F^+F^-=I/M$ the scaled result equals $(f*g)/(rM)$.",
                        Q(3425, "=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g).")),
                  infer(r"Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite procedure applied to the pointwise product of stored outputs equals the unpermuted computation.",
                        Q(3436, "Since $LB$ permutes records and leaves their polynomial suffixes", "$P(LBu,LBv)=LBP(u,v)$.")),
                  infer(r"The three transform errors and the product truncation total less than $3\delta+\eta$, and the final exact multiplication by $M$ gives error less than $\sqrt2\,M(3\ell+1)2^{-p}$.",
                        Q(3472, "The final exact multiplication by $M$ therefore gives error less than", "as claimed.")),
                  infer(r"The $M=T/r$ pointwise polynomial products cost $O(Tp\log(rp))$ in total; the three transforms cost as stated and the final scaling is linear.",
                        Q(3491, "There are $M=T/r$ pointwise polynomial products.", "$O(Tp\\log(rp))$;")),
                ],
                frm=["synthetic-transform", "transform-layout", "kronecker-packing", "convolution-theorem", "cyclic-convolution", "polynomial-ring-mod", "multidim-transform", "fixed-point-disk-grid"], page="ring-convolution",
                adds=[B("T", "padded box size", "the total number of complex coefficients, the product of the axis lengths and the ring dimension", "count"),
                      B("r", "ring dimension", "the number of complex coefficients in a polynomial record modulo $y^r+1$", "count"),
                      B("p", "precision bits", "the number of fractional bits of each fixed-point coefficient", "count"),
                      B("\\ell", "log ring dimension", "the base-2 logarithm of $r$")])

# ---------------------------------------------------------------- T7 multiplication algorithm
gauss = show(r"For coprime $s<t$ with $\theta=t/s-1>p/\alpha^4$, there are contractions $A$ and $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ keeping both coordinate permutations in the identity, computable on tape with error below $p^2$ per line and tensored over $d$ axes with error below $dp^2$.",
             "Use Harvey and van der Hoeven's Gaussian resampling identity and contraction estimates, but leave the two coordinate permutations inside the formula instead of sorting, and tensor the one-dimensional maps line by line over the padded array.",
             M("The usual implementation sorts twice on each coordinate; retaining both permutations in the transform formula lets the formula be computed directly.", "explicit",
               Q(3501, "Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and", "compute that formula directly.")),
             [
               infer(r"There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.",
                     Q(3562, "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.")),
               infer(r"The Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ holds and $\|N-I\|<2^{-\alpha^2\theta}$, so $N$ is invertible by a Neumann series.",
                     Q(3606, "\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}.")),
               infer(r"The ordered numerical maps for $A$ and $B_0$ have errors below $p^2$ and cost $O(tp^{3/2+\delta}\alpha)$ on a line of length $t$.",
                     Q(3688, "Contraction of the exact maps yields errors less than", "The costs add to the claimed bound.")),
               infer(r"Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
                     Q(3812, "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,")),
               infer(r"The total time in the one-dimensional algorithms is $O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$.",
                     Q(3820, "one-dimensional algorithms for both maps is", "with a constant independent of $d$.")),
               infer(r"Exposing and restoring all lines of the padded box by chunk exchanges costs $O(Tp\,d^2(1+\ell^\tau))$.",
                     Q(3827, "then exposing and restoring all the lines costs", "\\ell^\\tau)\\bigr)")),
             ],
             frm=["dft", "multidim-transform", "fixed-point-disk-grid", "nlogn-multiplier", "exponential-function-and-gaussian-function", "chunk-interchange", "vector-norms-and-error-bounds", "functions-bijections-and-permutations"], page="gaussian-resampling")

chirp = infer(r"For even lengths, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$ with the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, so the frequency permutation $Q$ is absorbed into two pointwise phases and a cyclic convolution.",
              Q(3923, "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}."),
              frm=["dft", "cyclic-convolution", "multidim-transform", "complex-numbers", "gaussian-resampling"], page="chirp-identity")

primes = show(r"Distinct odd primes $s_i$ just below the powers of two $t_i$, with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, can be found deterministically so that $T/2<S<T$ and every $t_i/s_i$ is separated from $1$ enough for resampling.",
              "Use the prime-interval lower bound of Harvey and van der Hoeven to show each interval holds more than $d$ primes, bound the product of the chosen primes with Bernoulli's inequality, check the separation hypothesis of the resampling lemma, and find the primes by trial division in time $n^{o(1)}$.",
              M("The distinct prime lengths must be close to the powers of two: their product must occupy a fixed fraction of the padded box, while each ratio must leave enough separation for resampling.", "explicit",
                Q(4105, "The distinct prime lengths $s_i$ must be close to the powers of two", "leave enough separation for resampling.")),
              [
                infer(r"For $0<\eta<1/4$ and $x>e^{2/\eta}$ the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, which exceeds $d$ for $x=r/2$ and $x=r$.",
                      Q(4118, "contains at least $\\eta x/(2\\log x)$ primes.")),
                infer(r"Multiplying the lower bounds and using Bernoulli's inequality gives $S/T>(1-1/(2d))^d>1/2$, so $T/2<S<T$.",
                      Q(4144, "Together with $s_i<t_i$, this gives $T/2<S<T$.")),
                infer(r"The upper bound on $s_i$ gives $\alpha^4\theta_i>3db\ge6b=p$, which is the separation hypothesis of the resampling lemma.",
                      Q(4149, "\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\geq6b=p.")),
                infer(r"Scanning the two intervals and testing candidates by trial division takes $n^{o(1)}=o(n)$ time.",
                      Q(4170, "Since $p=6\\lceil\\log_2 n\\rceil=\\Theta(\\log n)$, the search takes", "$n^{o(1)}=o(n)$ time.")),
              ],
              frm=["gaussian-resampling", "chirp-identity", "primes-coprimality-and-gcd", "logarithms-and-exponentials", "floor-ceiling-and-rounding", "crt-axis-map"], page="prime-lengths")

digits = infer(r"Writing each input in radix $2^b$ with $q=\lceil n/b\rceil$ digits gives a product of degree below $T/2<S$, so convolution modulo $x^S-1$ has no wraparound and every coefficient is below $2^{3b}$.",
               Q(4187, "Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
               frm=["int-as-convolution", "positional-number-representation-and-carries", "polynomials", "cyclic-convolution"])

crt = show(r"The map $\Phi$ sending $x\mapsto\prod_i x_i^{\mu_i}$ is an isomorphism from cyclic convolution of length $S=s_1\cdots s_d$ to $d$-dimensional cyclic convolution on the prime axes, implemented on tape by triangular prefix-controlled cyclic shifts in $O(Tp\,d^2(1+\ell^\tau))$.",
          "Use the Chinese remainder theorem to identify the monomial group, write the new coordinate on each axis as the old one plus a multiple of lower-index coordinates, and perform those updates from the last axis to the first as controlled shifts, with axis reordering by chunk interchanges.",
          M("The change of order is made a sequence of controlled cyclic shifts by choosing coordinate powers so each new coordinate depends only on earlier ones.", "explicit",
            Q(4200, "with coordinate powers that make the change of order a", "sequence of controlled cyclic shifts.")),
          [
            infer(r"The assignment $x\mapsto\prod_i x_i^{\mu_i}$ is an algebra isomorphism, so $\Phi$ preserves cyclic convolution.",
                  Q(4220, "$\\Phi$ is an isomorphism and preserves cyclic convolution.")),
            infer(r"With the mixed-radix expression $k=\sum_j a_jP_j$, the new coordinate on axis $i$ is $b_i=a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$.",
                  Q(4228, "b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j\\pmod{s_i}.")),
            infer(r"After reordering the padded axes so lower indices come first, the targets are updated in the order $i=d,d-1,\ldots,1$, so each offset uses unchanged controls.",
                  Q(4252, "Update the targets in the", "using \\eqref{eq:triangular-crt}.")),
            infer(r"Each triangular update is a prefix-controlled cyclic shift of the valid target interval, with padding left unchanged.",
                  Q(4273, "Each triangular update is a prefix-controlled cyclic shift.")),
          ],
          frm=["cyclic-convolution", "polynomial-ring-mod", "controlled-shifts", "chunk-interchange", "primes-coprimality-and-gcd", "modular-arithmetic", "functions-bijections-and-permutations"], page="crt-axis-map")

cplx = show(r"Normalized cyclic convolution $f*g/T$ of complex arrays on the power-of-two axes is obtained by twisting the last axis into $\mathbb C[y]/(y^r+1)$, convolving the other axes over the ring, and untwisting.",
            "Multiply coefficient $k$ of the last axis by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$, so the negative wrap of the ring cancels the twist, and use the ring convolution on the remaining axes.",
            M("The negacyclic wrap of the ring supplies exactly the sign that the twist removes, so a cyclic convolution on the last axis becomes a ring convolution.", "recoverable"),
            [
              infer(r"After twisting and negacyclic reduction a product term carries the factor $\zeta^{k+l}(-1)^h=\zeta^j$, so untwisting recovers the cyclic coefficient with the correct sign.",
                    Q(4317, "\\zeta^{k+l}(-1)^h=\\zeta^j(\\zeta^r)^h(-1)^h=\\zeta^j.")),
              infer(r"Hence $\mathcal M_{\mathbb C}(f,g):=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=f*g/T$.",
                    Q(4338, ":=D_-\\iota^{-1}", "=\\frac{f*g}{T}.")),
              infer(r"The computed version twists each operand with grid approximations of $\zeta^{k}$, truncating once after each phase product, then calls the ring convolution procedure.",
                    Q(4385, "f'&=Q_p(\\widetilde\\theta^+\\mathbin{\\cdot}f),")),
            ],
            frm=["ring-convolution", "negacyclic-twist", "cyclic-convolution", "fixed-point-disk-grid", "polynomial-ring-mod", "complex-numbers"], page="complex-convolution")

srct = show(r"The transform $RF_{\boldsymbol s}$ of coprime lengths is computed as $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$: the Gaussian map $\mathcal A$ line by line, the chirp transform through complex convolution, the map $\mathcal B_0$, and an exact power-of-two scale, retaining the permutation $R$.",
            "Chain the resampling maps around the chirp transform: use the chirp identity to turn the middle power-of-two transform with its permutation into a convolution, evaluated by the complex convolution procedure.",
            M("The middle factor of the resampling identity includes a frequency permutation, which the chirp identity converts into pointwise phases and a cyclic convolution without a separate sort.", "recoverable"),
            [
              infer(r"With exact phases and exact convolution, $\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)=QF_{\boldsymbol t}x$, so the computed chirp transform approximates the middle factor.",
                    Q(4447, "Replacing the approximations", "\\eqref{eq:permuted-chirp}.")),
              infer(r"The source transform applies the linewise approximation to $\mathcal A$, the computed chirp transform, the linewise approximation to $\mathcal B_0$, and an exact scale by $2^\gamma$.",
                    Q(4456, "For a source disk-grid tensor of norm at most $.5$, write", "exactly by $2^\\gamma$.")),
              infer(r"Its exact counterpart is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$.",
                    Q(4462, "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A", "=RF_{\\boldsymbol s}.")),
            ],
            frm=["gaussian-resampling", "chirp-identity", "complex-convolution", "prime-lengths", "fixed-point-disk-grid"], page="source-transform")

alg = infer(r"The algorithm applies the coefficient-address map $\Phi$, computes the source transforms of both digit arrays, multiplies pointwise and truncates, applies the opposite-sign transform with scalings, rounds, undoes $\Phi$, and propagates carries.",
            Q(4508, "\\item Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain", "$u,v$."),
            frm=["crt-axis-map", "source-transform", "int-as-convolution", "positional-number-representation-and-carries"])

perm = infer(r"The retained source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving $(u*v)/S^2$ with no sort executed.",
             Q(4537, "By \\eqref{eq:source-permutation-cancel}, the exact", "$w=(u*v)/S$."),
             frm=["gaussian-resampling", "chirp-identity", "dft", "convolution-theorem", "multidim-transform", "functions-bijections-and-permutations", "modular-arithmetic"], page="permutation-cancellation",
             salient="The permutation $R$ disappears entirely from the product of transforms: it enters once in each forward transform and once in the opposite transform, and since $RF^+R=F^+$ the three occurrences combine to the identity, so no sort is ever executed.")

exact = show(r"The recovered coefficient error is below $1/2$, so rounding gives the integer convolution coefficients exactly, and radix-$2^b$ carry propagation outputs precisely the $2n$ product bits.",
             "Track norms and errors through every approximate routine with contraction and bilinear-contraction bounds, check each computed array stays in the disk, scale back by the known factors, then round and carry.",
             M("The strict error below $1/2$ makes the nearest integer to the computed value the unique correct coefficient.", "explicit",
               Q(4730, "The strict error below $1/2$ makes the nearest integer to", "unique correct coefficient.")),
             [
               infer(r"The computed ring convolution output has norm below $.701$ for large $n$, so every call returns a legal disk-grid array without clipping.",
                     Q(4594, "Its computed grid output consequently", "for large $n$.")),
               infer(r"The source transform has error below $E_sh_p$ with $E_s=9\,2^\gamma TL$.",
                     Q(4652, "E_s=9\\,2^\\gamma TL,")),
               infer(r"The truncated pointwise product $z$ satisfies $\|z-U\cdot V_1\|<(2E_s+2)h_p$.",
                     Q(4687, "Thus $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.")),
               infer(r"After the first scale by $S$, the computed array approximates $w=(u*v)/S$ with error below $E_wh_p$, $E_w:=S(3E_s+2)<28\,2^\gamma T^2L$.",
                     Q(4709, "E_w:=S(3E_s+2)<28\\,2^\\gamma T^2L.")),
               infer(r"After the second scale, the final absolute error is below $448b\,2^{-3b/4}<1/2$.",
                     Q(4724, "2^{2b+4}S\\cdot28\\,2^\\gamma T^2L\\cdot2^{-6b}", "<\\frac12."),),
               infer(r"Since the true coefficients are integers and the error is strictly below $1/2$, the nearest integer to each recovered value is the unique correct coefficient, in $[0,2^{3b})$.",
                     Q(4728, "The true coefficients are real integers.", "unique correct coefficient.")),
               infer(r"The carries of the recurrence $d_j=(c_j+k_j)\bmod Q_0$ satisfy $0\le k_j\le q(Q_0-1)<Q_0^2$ and fix the radix digits of the full product.",
                     Q(4779, "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.")),
               infer(r"The product is less than $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.",
                     Q(4802, "The exact product is less than", "therefore zero.")),
             ],
             frm=["fixed-point-disk-grid", "int-as-convolution", "permutation-cancellation", "source-transform", "positional-number-representation-and-carries", "floor-ceiling-and-rounding", "vector-norms-and-error-bounds", "determinism-and-exact-versus-approximate-computation"], page="exact-recovery",
             salient="The final error is not merely below $1/2$ but exponentially small, about $2^{-3b/4}$, because the working precision $p=6b$ outweighs the scalings $2^{2b+4}S$, the transform sizes $T^2$ and the resampling factor $2^\\gamma$ with $\\gamma=o(b)$.")

mult = show(r"The algorithm that splits both inputs into digits, applies the coefficient-address map, takes source transforms, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries outputs the exact $2n$-bit product.",
            "Assemble the procedures: reduce the product to a convolution of digit coefficients, move it onto coprime prime axes, evaluate transforms of coprime length through resampling and chirp convolutions that call the power-of-two ring convolution, then undo scalings, round and carry.",
            M("The remaining proof places the procedures inside the multiplication reduction and accounts for every change of representation.", "explicit",
              Q(183, "The remaining proof places these procedures inside the multiplication", "reduction and accounts for every change of representation.")),
            [gauss, chirp, primes, digits, crt, cplx, srct, alg, perm, exact],
            frm=["int-as-convolution", "ring-convolution", "cyclic-convolution", "polynomials", "positional-number-representation-and-carries"], page="mult-algorithm",
            adds=[B("b", "digit width", "the number of bits in each radix digit, $\\lceil\\log_2 n\\rceil$", "count"),
                  B("S", "source length", "the product $s_1\\cdots s_d$ of the pairwise coprime prime source lengths", "count")])

# ---------------------------------------------------------------- T8 parameter balance
table = show(r"Each dominant row of the cost table has normalized power of $p$ at most $1-2\kappa$, the margins being $g_1,\ldots,g_7$ with minimum $2^{-181}$.",
             "Divide each operation's cost by $V=Tp$, read off its power of $p$, and subtract from one.",
             M("Every cost bound in the earlier sections is normalized by the volume $Tp$, so the total is a sum of terms $p^{\\text{power}}$ whose largest exponent governs.", "recoverable"),
             [
               infer(r"Prefix-slot moves and individual butterfly rounds cost $dK$ per unit volume, power $\epsilon(1+c)$.",
                     Q(4822, "Prefix-slot moves and individual butterfly rounds & $dK$ & $\\epsilon(1+c)$")),
               infer(r"Chunk exchanges for the transform layout cost $pK^{\tau-1}$, power $1-\epsilon c(1-\tau)$.",
                     Q(4823, "Chunk exchanges for transform layout & $pK^{\\tau-1}$ & $1-\\epsilon c(1-\\tau)$")),
               infer(r"Simultaneous butterfly rounds cost $\ell d^{\lambda'}$, power $1-\epsilon(1-\lambda')$.",
                     Q(4824, "Simultaneous butterfly rounds & $\\ell d^{\\lambda'}$ & $1-\\epsilon(1-\\lambda')$")),
               infer(r"CRT and axis layouts cost $d^2(1+\ell^\tau)$, power $\tau+\epsilon(2-\tau)$.",
                     Q(4825, "CRT and axis layouts & $d^2(1+\\ell^\\tau)$ & $\\tau+\\epsilon(2-\\tau)$")),
               infer(r"Gaussian line maps cost $dp^{1/2+\delta}\alpha$, power $3/4+\delta+3\epsilon/2$.",
                     Q(4826, "Gaussian line maps & $dp^{1/2+\\delta}\\alpha$ & $3/4+\\delta+3\\epsilon/2$")),
               infer(r"Chirps, twists and scalar products cost $dp^\delta$, power $\epsilon+\delta$.",
                     Q(4827, "Chirps, twists and scalar products & $dp^\\delta$ & $\\epsilon+\\delta$")),
               infer(r"Packed polynomial products cost $\log(rp)$, power $1-\epsilon$.",
                     Q(4828, "Packed polynomial products & $\\log(rp)$ & $1-\\epsilon$")),
             ])

params = show(r"With $p=\Theta(\log n)$, $d=\lfloor b^\epsilon\rfloor$ axes, chunk size $K$, ring dimension $r=2^{\Theta(p/d)}$ and tiny fixed exponents, every row of the cost table has normalized power of $p$ at most $1-2\kappa$, so the total is $O(n(\log n)^{1-\kappa})$ with $\kappa=2^{-182}$.",
              "Fix all exponents as explicit rational numbers, derive the sizes $T$, $d$, $r$, $K$ from $n$, list every operation's normalized cost as a power of $p$, verify each margin below one by direct substitution, and absorb remaining logarithmic factors in the slack.",
              M("The smallest margin gives explicit slack that covers any remaining fixed power of $\\log p$.", "explicit",
                Q(4854, "This explicit slack will cover", "any remaining fixed power of $\\log p$.")),
              [
                infer(r"The sizes are fixed from the input length: $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, with $Tp=\Theta(n)$.",
                      Q(4055, "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,"), deferred=True),
                infer(r"The exponents are fixed rational numbers with $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$.",
                      Q(4013, "C_1=20,\\qquad \\epsilon=2^{-75},\\qquad \\kappa=2^{-182}."), deferred=True),
                table,
                infer(r"The seven margins satisfy $\min_i g_i=2^{-181}=2\kappa$.",
                      Q(4854, "Thus $\\min_i g_i=2^{-181}=2\\kappa$.")),
                infer(r"Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the cost is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.",
                      Q(4983, "Each of the seven displayed powers is at most $1-2\\kappa$ by", "O(n(\\log n)^{1-\\kappa}).")),
                infer(r"Below one fixed cutoff the machine uses schoolbook multiplication, so the single machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length.",
                      Q(4989, "Fix one cutoff beyond all the size, precision, margin and layout", "included by enlarging the implicit constant.")),
              ],
              frm=["transform-layout", "simultaneous-layer", "chunk-interchange", "crt-axis-map", "gaussian-resampling", "ring-convolution", "prime-lengths", "mult-algorithm", "exact-recovery", "logarithms-and-exponentials", "asymptotic-notation-beyond-big-o"], page="parameter-balance",
              salient="The exponent $\\kappa=2^{-182}$ is half of the smallest margin $g_2=\\epsilon c(1-\\tau)=2^{-181}$, which is itself a product of three tiny exponents $\\epsilon=2^{-75}$, $c=2^{-56}$ and $1-\\tau=2^{-50}$: the saving over $\\log n$ is minuscule because each ingredient saves only a sliver.")

concl = infer(r"The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model, disproving the Schönhage--Strassen conjecture there.",
              Q(70, "The theorem refutes an", "in this model."), deferred=True,
              frm=["nlogn-conjecture"])

root = show(r"There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in this model.",
            "Reduce the product to a convolution of short digit coefficients computed by Fourier-type transforms, and cut the two costs that make every transform level a full pass (address movement and butterfly arithmetic) by two power-saving tape procedures derived from linear networks with a rank deficit; then assemble the exact algorithm and balance the parameters so every cost term is at most $p^{1-2\\kappa}$ per unit volume.",
            M("Scanning an array of $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both movement and arithmetic.", "explicit",
              Q(90, "Scanning an array of $\\Theta(n)$ stored bits at each of", "savings in both movement and arithmetic.")),
            [t1, t2, netcont, chunk, simul, ringconv, mult, params, concl],
            frm=["fixed-tape-model", "nlogn-conjecture", "asymptotic-notation-beyond-big-o", "logarithms-and-exponentials"], page="main-theorem",
            adds=[B("n", "input length", "the number of bits in each of the two integers to be multiplied", "count"),
                  B("\\kappa", "saving exponent", "the fixed exponent $2^{-182}$ by which the logarithmic factor is reduced"),
                  B("V", "stored volume", "the number of stored data bits in an array, to which costs are normalized", "count")])

number(root)
json.dump({"root": root}, open('exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)

# order check
seq = []
def walk(n):
    if n["intention"] == "infer":
        if not n.get("deferred"):
            seq.append((POS[id(n["quote"])], n["id"]))
    for c in n.get("children", []):
        walk(c)
walk(root)
bad = [(a, b) for a, b in zip(seq, seq[1:]) if a[0] >= b[0]]
print("n infer", len(seq), "bad", bad)
