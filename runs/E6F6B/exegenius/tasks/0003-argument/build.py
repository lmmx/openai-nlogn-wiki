import json, sys
BASE = "/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6B"
SRC = open(BASE + "/sources/paper.tex").read()

def ev(q):
    return {"source": "paper", "quote": q}

def infer(id, claim, quote, frm, page=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote), "from": frm}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    return n

def show(id, claim, method, mot_text, mot_src, children, frm, page=None, mot_quote=None, salient=None, adds=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": {"text": mot_text, "source": mot_src, "quote": ev(mot_quote) if mot_quote else None},
         "children": children, "from": frm}
    if page: n["page"] = page
    if salient: n["salient"] = salient
    if adds: n["adds"] = adds
    return n

def B(symbol, name, meaning, relation):
    return {"symbol": symbol, "name": name, "meaning": meaning, "relation": relation}

# ---------- S3: fast address interchange ----------
S3 = show(
 "S1.3", 
 "Two disjoint address fields of $u$ bits in an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$, although the intermediate steps XOR data together.",
 "Realize the exchange by a fixed network of XOR gates on $W$ wire roles whose edges are cheap changes of address frame, each costing smaller interchanges, so that the sum of edge ranks $s<Wm$ makes the recursion save a power of the chunk width; then handle arbitrary widths by padding and a base-$m$ decomposition.",
 "A strict rank deficit s<Wm makes the normalized cost recurrence grow like a power of the width below one, which no direct scan of the fields can do.",
 "explicit",
 [
  infer("S1.3.1",
   "A fixed network of linear gates on $W$ wires, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange $X$ and $Y$ up to sign and restores every scratch wire whatever its initial value.",
   "For arbitrary initial values of its auxiliary wires, a forward",
   ["binary-representation-bit-strings-and-xor", "matrices-invertibility-and-rank", "rational-numbers-and-dyadic-fractions"],
   page="bank-exchange-network"),
  infer("S1.3.2",
   "Replacing scalars by arrays and giving each vertex an invertible frame $D_v$, pointwise linear gates commute with a common frame, so the network implements $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$ and each edge only changes frame by $D_vD_u^{-1}$.",
   "$c_j\\in R$.  Thus the common frame commutes with the pointwise gate, and",
   ["bank-exchange-network", "linear-algebra-spaces", "permutations-and-bijections", "matrices-invertibility-and-rank", "cartesian-products-and-lexicographic-order"],
   page="frames-on-arrays"),
  infer("S1.3.3",
   "Nondegenerate subspaces of an $m$-dimensional space, built from three-element subsets, can be attached to gates and terminals so that adjacent labels are nested and the orthogonal residual dimensions over all edges total $s<Wm$.",
   "edges are the central-wire edges from time 3 to time 4; their dimension",
   ["linear-algebra-spaces", "bank-exchange-network", "frames-on-arrays", "vector-spaces-bases-and-dimension"],
   page="subspace-labels",
   salient="Although the network exchanges two full banks, the total edge rank $s$ is strictly below the trivial budget $Wm$ in which every edge changes a full $m$-dimensional frame: the only decreasing edges are the central-wire edges from time 3 to time 4, each losing dimension $h$, which keeps the loss below $N/2$ and leaves a strict deficit."),
  infer("S1.3.4",
   "With frames $\\Phi_M$ moving the entry at $(H,D)$ to $(H+MD,D)$, the bit network turns the exchange into the shear $H\\leftarrow H+D$ on every role, with total edge rank $s<Wm$.",
   "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
   ["frames-on-arrays", "subspace-labels", "recursive-power-saving", "linear-algebra-spaces", "controlled-shifts", "modular-arithmetic-and-congruences", "matrices-invertibility-and-rank"],
   page="bit-shear-interface"),
  infer("S1.3.5",
   "A call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the normalized cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, and because $s/W<m^\\tau$ the cost is $O(Ve^\\tau)$ with $\\tau<1$.",
   "\\frac{s_{\\rm b}}{W_{\\rm b}}<m^\\tau,",
   ["subspace-labels", "multitape-streams", "recurrences-and-induction", "big-o", "logarithms-floor-and-ceiling"],
   page="recursive-power-saving",
   salient="The exponent is strictly below one only because $s/W$ is strictly below $m$: the strict rank deficit $s<Wm$ becomes the factor $s/W<m^\\tau$ per level of a recursion of depth $\\log_m e$, giving $e^\\tau$ rather than $e$."),
  infer("S1.3.6",
   "Every $m\\times m$ rational matrix $A$ of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation matrix with exactly $a$ ones.",
   "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
   ["matrices-invertibility-and-rank", "gaussian-elimination"],
   page="lower-triangular-factorization"),
  infer("S1.3.7",
   "The address map $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^b\\mathbb Z$ with $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work, using one swap per pivot of the factorization.",
   "can be performed with exactly $a$ interchanges of pairs of $b$-digit",
   ["lower-triangular-factorization", "controlled-shifts", "bit-shear-interface", "modular-arithmetic-and-congruences", "multitape-streams"],
   page="matrix-shear-cost"),
  infer("S1.3.8",
   "Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\\tau)$ time by splitting rows into $W$ role streams, running the bit network with shear edges implemented by $s$ smaller interchanges, and then applying $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$.",
   "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",
   ["matrix-shear-cost", "bit-shear-interface", "recursive-power-saving", "frames-on-arrays", "bank-exchange-network", "multitape-streams"],
   page="power-width-interchange"),
  infer("S1.3.9",
   "For an arbitrary width $u$, padding the row count and the chunk ranges and writing the remaining width in base $m$ reduces to power-width interchanges, so the whole interchange costs $O(Vu^\\tau)$.",
   "Write the remaining width in base $m$:",
   ["power-width-interchange", "multitape-streams", "logarithms-floor-and-ceiling"]),
 ],
 ["power-width-interchange", "recursive-power-saving", "multitape-streams", "binary-representation-bit-strings-and-xor"],
 page="chunk-interchange",
 mot_quote="is the source of the power saving.",
 salient="The cost exponent $\\tau$ is strictly less than one, so moving an arbitrary pair of address fields is cheaper than a linear number of passes in their width, even though the final effect is just a permutation.",
 adds=[B("W", "wire count", "the number of wires, one role each, in the fixed linear network", "count"),
       B("m", "label dimension", "the dimension of the space whose subspaces label the gates and terminals, also the number of digit fields in a chunk", "count"),
       B("s", "total edge rank", "the total rank of the frame changes over all edges, which equals the number of smaller calls", "count")])

# ---------- S4: simultaneous butterfly layer ----------
S4 = show(
 "S1.4",
 "Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in $D\\le d$ address chunks of $K$ bits at once, on polynomial records with fixed-point complex coefficients, costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$ and ends with one truncation of error below $\\sqrt2\\,2^{-p}$.",
 "Reuse the rank-saving network on Gaussian dyadic values: phase frames turn every edge into two-point kernels on selected bits, packed row additions implement the binary changes of basis, the recurrence over groups of chunks gives the power saving, and a guard-width bound lets the whole layer be evaluated exactly before one truncation.",
 "The network is built so that every edge can be implemented by smaller calls to the same procedure, which gives the power saving over $d$ separate whole-array butterfly passes.",
 "explicit",
 [
  infer("S1.4.1",
   "With $C=H\\mathsf SH$ (a Gaussian dyadic combination of $I$ and the bit flip $X$) one has $H_0^{\\otimes D}$ equal to a constant times $\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, and phase frames of binary labels make each network edge a product of translation kernels, one per residual basis vector.",
   "\\eqref{eq:phase-basic-identities} on all selected coordinates gives",
   ["bank-exchange-network", "frames-on-arrays", "subspace-labels", "linear-algebra-spaces", "recursive-power-saving", "chunk-interchange", "complex-numbers", "binary-representation-bit-strings-and-xor", "matrices-invertibility-and-rank"],
   page="phase-frames"),
  infer("S1.4.2",
   "Adding (XOR) selected bits of one address chunk into another costs $O(V(L^\\tau+1))$ using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.",
   "significant bit, one fixed multitape procedure performs",
   ["chunk-interchange", "controlled-shifts", "multitape-streams", "binary-representation-bit-strings-and-xor", "phase-frames"],
   page="packed-selected-bit-addition"),
  infer("S1.4.3",
   "Splitting a group of $e=mf$ chunks into $m$ slots with one child call per residual basis vector and rows distributed over $W$ roles gives $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$, which unrolls to $O(d^{\\lambda'})$ per unit volume.",
   "Indeed, the \\(s\\) child calls are executed on streams of volume",
   ["recursive-power-saving", "phase-frames", "packed-selected-bit-addition", "multitape-streams", "recurrences-and-induction"]),
  infer("S1.4.4",
   "Intermediate values in a butterfly layer are exact Gaussian dyadics whose denominators and magnitudes grow by at most $O(d^{20})$ guard bits, so one truncation can follow the completed layer.",
   "The accelerated network is evaluated exactly until an entire",
   ["fixed-point-precision", "phase-frames", "rational-numbers-and-dyadic-fractions", "recursive-power-saving", "norms-absolute-value-and-triangle-inequality"],
   page="guard-bits"),
  infer("S1.4.5",
   "Converting the exact $C$-layer to $H_0^{\\otimes D}$ and truncating once, the result stays in the unit disk because every row of $H_0^{\\otimes D}$ has absolute row sum one, with error below $\\sqrt2\\,2^{-p}$.",
   "converts the resulting exact $C$-layer to $\\mathcal H$.",
   ["fixed-point-precision", "guard-bits", "norms-absolute-value-and-triangle-inequality"]),
 ],
 ["phase-frames", "packed-selected-bit-addition", "guard-bits", "fixed-point-precision", "chunk-interchange", "recursive-power-saving", "subspace-labels", "bank-exchange-network", "frames-on-arrays", "synthetic-transforms", "radix-two-fft", "negacyclic-ring"],
 page="simultaneous-butterfly-layer",
 mot_quote="so that every edge can be implemented by smaller calls to the same",
 salient="The cost exponent $\\lambda'$ is strictly below one, so a layer acting on $d$ chunks at once costs far less than the $d$ whole-array passes that separate butterfly factors would need.")

# ---------- S2: synthetic convolution ----------
S2 = show(
 "S2",
 "Convolution of arrays over the polynomial ring $\\mathbb C[y]/(y^r+1)$ on $d-1$ axes is computed from two forward synthetic transforms, pointwise ring products in the retained frequency order and the opposite transform, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$, where $M=T/r$ and $\\ell=\\log_2 r$.",
 "Transform both operands with synthetic transforms laid out on tape so each FFT round is one simultaneous layer, multiply the records pointwise exactly by signed packing and the established multiplier, and apply the opposite transform to the same retained order.",
 "Powers of y are roots of unity that act as signed shifts, so the transform costs only butterflies and layouts, while the opposite transform consumes the retained stored frequency order, so no permutation need be undone.",
 "explicit",
 [
  infer("S2.1",
   "Fourier-type transforms over $\\mathbb C[y]/(y^r+1)$ use $\\omega_t=y^{2r/t}$ as root of unity, so twiddle multiplications are signed coefficient shifts, radix-two butterflies leave outputs in bit-reversed order, and the forward and opposite versions invert each other up to $1/t$.",
   "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
   ["negacyclic-ring", "discrete-fourier-transform", "radix-two-fft", "fixed-point-precision", "euler-s-formula-and-roots-of-unity", "polynomials"],
   page="synthetic-transforms"),
  infer("S2.2",
   "A positional address permutation places the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks, so each FFT round is one simultaneous layer, at total cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ for $M=T/r$ records.",
   "we must place the selected bits of the participating axes at a common",
   ["synthetic-transforms", "simultaneous-butterfly-layer", "chunk-interchange", "multitape-streams", "radix-two-fft", "logarithms-floor-and-ceiling"],
   page="synthetic-transform-layout"),
  infer("S2.3",
   "Products of ring polynomials are computed exactly by evaluating each at a large power of two (signed Kronecker substitution), multiplying the resulting integers with the established multiplier and unpacking the coefficients, in time $O(rp\\log(rp))$.",
   "Let $r=2^\\ell<2^p$ with integers $\\ell\\geq1$ and $p\\geq2$, and fix $C_w>1$.",
   ["hvdh-multiplier", "negacyclic-ring", "fixed-point-precision", "convolution-multiplication", "polynomials", "radix-representation-and-carry-propagation"],
   page="signed-kronecker-packing"),
  infer("S2.4",
   "Because pointwise multiplication commutes with the record permutation, multiplying the forward outputs in their retained order and applying the opposite transform gives $(f*g)/(rM)$, with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ and the stated cost.",
   "Perform both forward transforms and retain their common $LB$ order.",
   ["discrete-fourier-transform", "synthetic-transforms", "synthetic-transform-layout", "signed-kronecker-packing", "norms-absolute-value-and-triangle-inequality"]),
 ],
 ["synthetic-transforms", "synthetic-transform-layout", "signed-kronecker-packing", "negacyclic-ring", "simultaneous-butterfly-layer", "fixed-point-precision"],
 page="synthetic-convolution",
 mot_quote="is stored, because the opposite transform consumes that same order",
 adds=[B("M", "record count", "the number of polynomial records, equal to the product of the first $d-1$ axis lengths, $T/r$", "count"),
       B("\\ell", "ring exponent", "the base-two logarithm of $r$, the number of butterfly rounds on the last axis", "count")])

# ---------- T3: resampling ----------
T3 = show(
 "S3",
 "The prime-length transforms $RF_{\\boldsymbol s}$ needed for the digit convolution can be computed through power-of-two tensor transforms $QF_{\\boldsymbol t}$ without executing the source and target coordinate permutations.",
 "Rewrite each prime-length transform line by line as contractions around a power-of-two transform, keep both coordinate permutations inside the transform identity, turn the middle transform into a cyclic convolution by a chirp, and cancel the source permutation across the pointwise product.",
 "Sorting twice on each coordinate is what the usual implementation of Gaussian resampling pays for; keeping both permutations in the transform formula avoids it.",
 "explicit",
 [
  infer("S3.1",
   "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, each computable in time $O(tp^{3/2+\\delta}\\alpha)$, with no sorting.",
   "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",
   ["discrete-fourier-transform", "fixed-point-precision", "hvdh-multiplier", "rounding-and-square-roots", "norms-absolute-value-and-triangle-inequality", "primes-coprimality-and-gcd", "euler-s-formula-and-roots-of-unity"],
   page="gaussian-resampling"),
  infer("S3.2",
   "Applying the one-dimensional resampling maps line by line along each of $d$ axes of the zero-padded power-of-two box, exposing each axis with chunk interchanges, gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with error below $dp^2$ and total line cost $O(dTp^{3/2+\\delta}\\alpha)$.",
   "Both $\\mathcal A$ and $\\mathcal B_0$ are contractions. The linewise",
   ["gaussian-resampling", "chunk-interchange", "permutation-cancellation", "multitape-streams"],
   page="tensor-resampling"),
  infer("S3.3",
   "The permuted transform $QF_{\\boldsymbol t}$ equals chirp multiplication, a cyclic convolution with the chirp array $a$ divided by $T$, and chirp multiplication again, so the frequency permutation is never executed.",
   "Then $a$ has period $t_i$ in coordinate $i$, and",
   ["discrete-fourier-transform", "coefficient-twist", "synthetic-convolution", "euler-s-formula-and-roots-of-unity", "modular-arithmetic-and-congruences"],
   page="bluestein-chirp"),
  infer("S3.4",
   "Because a coordinate permutation $R$ commutes with pointwise products, applying $RF_{\\boldsymbol s}$ to both operands and $RF_{\\boldsymbol s}^+$ to their pointwise product yields $(u*v)/S^2$, so the source permutation never has to be undone.",
   "If $S=\\prod_i s_i$, then",
   ["discrete-fourier-transform", "gaussian-resampling", "bluestein-chirp", "permutations-and-bijections", "modular-arithmetic-and-congruences"],
   page="permutation-cancellation",
   salient="The permutation $R$ appears on both operands and again on the product, yet the result is the plain scaled convolution $(u*v)/S^2$ with no trace of $R$: pointwise products commute with coordinate permutations and the two copies of $R$ cancel through the opposite transform."),
 ],
 ["discrete-fourier-transform", "synthetic-convolution", "chunk-interchange", "coefficient-twist"],
 mot_quote="We retain both permutations in the transform formula and")

# ---------- T4: multiplication algorithm ----------
T4 = show(
 "S4",
 "Split into radix digits, map by the Chinese-remainder address map, apply the source transform (resampling and chirp convolution via ring convolution) to both operands, multiply pointwise, apply the opposite transform, undo the scales, round and propagate carries.",
 "Instantiate the reductions of the flow chart (digit convolution, cyclic convolution on distinct prime axes, normalized convolution on power-of-two axes, convolution over the polynomial ring) with explicit size parameters, then run the resulting six-stage procedure.",
 "The tape procedures and transforms are only useful once the sizes are compatible, so the sizes are fixed first and every change of representation is charged.",
 "explicit",
 [
  infer("S4.1",
   "For input length $n$ choose $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T$ near $4n/b$ split into $d$ axis lengths $r/2$ or $r$, and distinct odd primes $s_i$ just below the $t_i$ with $T/2<S<T$.",
   "Take the power of two $T$ in $[4n/b,8n/b)$, and let",
   ["primes-coprimality-and-gcd", "trial-division-and-primality-search", "logarithms-floor-and-ceiling", "gaussian-resampling", "fixed-point-precision"],
   page="parameter-choice"),
  infer("S4.2",
   "Writing each integer as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ small digit coefficients, the product is a convolution of digit lists with no wraparound modulo $x^S-1$ because $2q-2<S$, with carries propagated afterwards.",
   "Write the two inputs as polynomials in $2^b$, each with",
   ["polynomials", "radix-representation-and-carry-propagation", "divide-and-conquer-multiplication"],
   page="convolution-multiplication"),
  infer("S4.3",
   "The map $x\\mapsto\\prod_i x_i^{\\mu_i}$ is an algebra isomorphism turning one cyclic convolution of length $S=s_1\\cdots s_d$ into a $d$-dimensional cyclic convolution over pairwise coprime axes, implemented by triangular controlled shifts.",
   "Let $s_1,\\ldots,s_d$ be the pairwise coprime",
   ["controlled-shifts", "chunk-interchange", "modular-arithmetic-and-congruences", "euclidean-algorithm-and-modular-inverses", "primes-coprimality-and-gcd", "polynomials"],
   page="crt-cyclic-convolution"),
  infer("S4.4",
   "Multiplying coefficient $k$ of the last cyclic coordinate by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps cyclic convolution of length $r$ to the ring modulo $y^r+1$, so the ring convolution computes complex cyclic convolution.",
   "The power-of-two complex convolution used in the chirp identity is",
   ["synthetic-convolution", "negacyclic-ring", "euler-s-formula-and-roots-of-unity", "discrete-fourier-transform"],
   page="coefficient-twist"),
  infer("S4.5",
   "The source transform applies the linewise approximation of $\\mathcal A$, the chirp transform built from the twisted ring convolution, and the linewise approximation of $\\mathcal B_0$, then scales by $2^\\gamma$, so that it computes $RF_{\\boldsymbol s}$ on a disk-grid tensor.",
   "For a source disk-grid tensor of norm at most $.5$, write",
   ["gaussian-resampling", "tensor-resampling", "bluestein-chirp", "coefficient-twist", "synthetic-convolution", "fixed-point-precision"]),
  infer("S4.6",
   "The source transforms of both operands are multiplied pointwise, the opposite transform is applied, the two occurrences of $S$ and the scale $2^{2b+4}$ undo the normalizations, and rounding and radix-$2^b$ carry propagation give the $2n$-bit product.",
   "The source-transform procedures now supply the three transforms needed",
   ["permutation-cancellation", "crt-cyclic-convolution", "convolution-multiplication", "radix-representation-and-carry-propagation", "rounding-and-square-roots"]),
 ],
 ["convolution-multiplication", "crt-cyclic-convolution", "tensor-resampling", "bluestein-chirp", "permutation-cancellation", "coefficient-twist", "synthetic-convolution", "parameter-choice"],
 page="multiplication-algorithm",
 mot_quote="reduction and accounts for every change of representation.",
 adds=[B("b", "digit width", "the number of bits in one radix digit, $b=\\lceil\\log_2 n\\rceil$, so digits are in base $2^b$", "count")])

# ---------- T5: exact recovery ----------
T5 = show(
 "S5",
 "Disk margins keep every intermediate array in the unit disk, the accumulated approximation errors stay below $1/2$ per coefficient, so rounding returns the exact integer product coefficients and carry propagation gives the $2n$-bit product.",
 "Track the norm and the error of each computed array through the pipeline using contraction bounds, show that the final error is below $1/2$, and then round and propagate carries.",
 "The true coefficients are integers, so an error strictly below one half identifies each of them as the nearest integer.",
 "explicit",
 [
  infer("S5.1",
   "Every computed array stays in the unit disk, because the smaller operand norms $.7$, $.6$, $.5$ and $1/4$ are preserved and the errors, scaled by $2^{-p}$, stay below $10^{-3}$ for large $n$.",
   "Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this",
   ["fixed-point-precision", "norms-absolute-value-and-triangle-inequality", "synthetic-convolution", "multiplication-algorithm"]),
  infer("S5.2",
   "The final absolute error on every integer coefficient is below $448b\\,2^{-3b/4}<1/2$, so the nearest integer to the computed value is the exact product coefficient.",
   "Since $S\\le T<2^b$ and $L<b$ eventually, the final absolute error is less than",
   ["rounding-and-square-roots", "norms-absolute-value-and-triangle-inequality", "fixed-point-precision"]),
  infer("S5.3",
   "Propagating radix-$2^b$ carries in increasing coefficient order, with carries bounded by $q(2^b-1)$, yields the exact $2n$-bit product.",
   "To propagate carries, let $Q_0=2^b$.  The recovered ordinary",
   ["radix-representation-and-carry-propagation", "recurrences-and-induction"]),
 ],
 ["fixed-point-precision", "rounding-and-square-roots", "radix-representation-and-carry-propagation", "multiplication-algorithm"],
 page="exact-recovery",
 mot_quote="that value the unique correct coefficient.")

# ---------- T6: time bound ----------
T6 = show(
 "S6",
 "Dividing each phase's cost by $Tp=\\Theta(n)$ gives seven dominant powers of $p$, each at most $1-2\\kappa$ for the fixed rational exponents, so the total is $O(n(\\log n)^{1-\\kappa})$.",
 "Tabulate the normalized cost of each phase, read off the exponent of $p$ of each dominant row, compare each with one using the fixed rational parameters, and absorb remaining powers of $\\log p$.",
 "Every phase handles $Tp=\\Theta(n)$ stored bits, so cost per bit is a power of $p=\\Theta(\\log n)$, and the total is $n$ times that power of the logarithm.",
 "recoverable",
 [
  infer("S6.1",
   "After division by $V=Tp$, the phases cost $dK$, $pK^{\\tau-1}$, $\\ell d^{\\lambda'}$, $d^2(1+\\ell^\\tau)$, $dp^{1/2+\\delta}\\alpha$, $dp^{\\delta}$ and $\\log(rp)$, with all remaining phases absorbed.",
   "For the cost calculation put $V=Tp=\\Theta(n)$. The fixed-width coefficient",
   ["time-bound-accounting", "big-o", "logarithms-floor-and-ceiling", "synthetic-convolution", "tensor-resampling", "crt-cyclic-convolution", "parameter-choice"] ),
  infer("S6.2",
   "The seven margins $g_i$ below one satisfy $\\min_i g_i=2^{-181}=2\\kappa$ for the fixed rational parameters.",
   "Thus $\\min_i g_i=2^{-181}=2\\kappa$.  This explicit slack will cover",
   ["parameter-choice", "logarithms-floor-and-ceiling"],
   salient="The binding margin is exactly $2\\kappa=2^{-181}$, coming from the chunk-exchange row, whose margin $\\epsilon c(1-\\tau)$ is the product of three tiny exponents; all other rows have far more slack."),
  infer("S6.3",
   "Each of the seven powers is at most $1-2\\kappa$ and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually, so the total cost is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
   "Each of the seven displayed powers is at most $1-2\\kappa$ by",
   ["parameter-choice", "big-o", "polynomial-time-and-computational-cost-on-tapes"]),
 ],
 ["parameter-choice", "synthetic-convolution", "tensor-resampling", "crt-cyclic-convolution", "big-o", "exact-recovery"],
 page="time-bound-accounting")

# fix S6.1 from: remove self reference
for c in T6["children"]:
    c["from"] = [x for x in c["from"] if x != "time-bound-accounting"]

# ---------- S1 group: tape procedures ----------
S1 = show(
 "S1",
 "There are two fast tape procedures: an interchange of two address fields of $u$ bits in $O(Vu^\\tau)$ time and a simultaneous butterfly layer over $d$ address chunks in $O(Vd^{\\lambda'})$ time, with $\\tau,\\lambda'<1$ and $V$ the stored bit volume.",
 "Set up the elementary stream and controlled-shift tools, then build each of the two procedures from its own rank-saving linear network that recurses on smaller calls of itself.",
 "Scanning the array at each of the transform levels costs n log n, so both the movement of addresses and the arithmetic of a butterfly layer must be sped up by a power.",
 "recoverable",
 [
  infer("S1.1",
   "Splitting, merging, digit moves and row splits on an array of volume $V$ in lexicographic order cost $O(V)$ steps on a fixed number of tapes.",
   "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
   ["turing-machines", "cartesian-products-and-lexicographic-order", "polynomial-time-and-computational-cost-on-tapes", "big-o"],
   page="multitape-streams"),
  infer("S1.2",
   "Updating a target field by an offset computed from earlier control fields (a cyclic rotation of blocks), or multiplying it by a unit modulo $q^b$, costs $O(V)$.",
   "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
   ["multitape-streams", "modular-arithmetic-and-congruences", "euclidean-algorithm-and-modular-inverses", "primes-coprimality-and-gcd"],
   page="controlled-shifts"),
  S3,
  S4,
 ],
 ["turing-machines", "big-o"],
 mot_quote=None)

ROOT = show(
 "S0",
 "A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "Provide two fast tape procedures, place them inside the Gaussian-resampling and synthetic-transform reduction of the integer product to a convolution, then check precision and exact recovery and add up the costs of all phases.",
 "Scanning $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both address movement and arithmetic.",
 "explicit",
 [S1, S2, T3, T4, T5, T6],
 ["big-o", "turing-machines", "polynomial-time-and-computational-cost-on-tapes"],
 page="multiplication-below-nlogn",
 mot_quote="We therefore need savings in both movement and arithmetic.",
 salient="The saving is a fixed power of the logarithm, $(\\lg n)^{-\\kappa}$, rather than a $\\log\\log$ factor, even though $\\kappa=2^{-182}$ is astronomically small.",
 adds=[B("p", "working precision", "the number of fractional bits of the fixed-point complex coefficients", "count"),
       B("d", "axis count", "the number of axes, equivalently address chunks, acted on together", "count"),
       B("K", "chunk width", "the number of address bits in one chunk, $K=\\lfloor d^c\\rfloor$", "count"),
       B("r", "ring length", "the number of complex coefficients in a polynomial record modulo $y^r+1$", "count"),
       B("T", "array size", "the number of complex coefficients in the whole padded array, the product of the axis lengths", "count"),
       B("\\tau", "interchange exponent", "the fixed exponent below one in the interchange cost $O(Vu^\\tau)$", "direct"),
       B("\\lambda'", "layer exponent", "the fixed exponent below one in the butterfly-layer cost $O(Vd^{\\lambda'})$", "direct")])
ROOT["children"][0]["motivation"]["quote"] = None

# ---------- check quotes order ----------
pos = 0
bad = False
def walk(n):
    global pos, bad
    if n["intention"] == "infer":
        q = n["quote"]["quote"]
        i = SRC.find(q, pos)
        if i < 0:
            j = SRC.find(q)
            print("QUOTE", "OUT OF ORDER" if j >= 0 else "MISSING", n["id"], repr(q), "line", SRC[:j].count("\n")+1 if j>=0 else None)
            bad = True
        else:
            print(n["id"], "line", SRC[:i].count("\n")+1)
            pos = i + len(q)
    else:
        mq = n["motivation"].get("quote")
        if mq and SRC.find(mq["quote"]) < 0:
            print("MOT QUOTE MISSING", n["id"], mq["quote"]); bad = True
        for c in n["children"]:
            walk(c)
walk(ROOT)
json.dump({"root": ROOT}, open(BASE + "/exegenius/tasks/0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)
print("BAD" if bad else "OK")
