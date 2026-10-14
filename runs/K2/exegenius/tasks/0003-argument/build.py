import json, re, sys

SRC = '/home/user/openai-nlogn-wiki/runs/K2/sources/paper.tex'
OUT = '/home/user/openai-nlogn-wiki/runs/K2/exegenius/tasks/0003-argument.answer.json'
text = open(SRC, encoding='utf-8').read()

ORDER = ["polynomial-ring","polynomial-roots-of-unity","two-point-butterfly","gaussian-dyadic",
"linear-algebra","fixed-tape-machine","schonhage-strassen-conjecture","logical-volume","address-fields",
"elementary-stream-operations","row-splitting","controlled-shifts","scratch-restoration",
"triple-subset-exchange-network","frames","subspace-labels","rank-saving","volume-normalized-recursion",
"lower-triangular-factorization","matrix-shear-interchange","circuit-to-address-permutation",
"power-width-chunk-interchange","arbitrary-width-chunk-interchange","two-point-phase-kernel",
"binary-phase-frames","packed-selected-bit-xor","guard-bits","disk-grid-arrays","grid-truncation",
"simultaneous-butterfly-layer","transform-layout","cyclic-convolution","radix-digit-convolution",
"crt-coefficient-map","negacyclic-twist","discrete-fourier-transform","synthetic-transform",
"bluestein-chirp","synthetic-transform-on-tapes","frequency-order-retention","hvdh-multiplier",
"signed-coefficient-packing","ring-product","normalized-ring-convolution","approximate-roots-of-unity",
"contraction","gaussian-resampling","fixed-exponent-choices","size-parameters","prime-source-lengths",
"permutation-free-resampling","tensor-resampling","source-permutation-cancellation",
"complex-convolution-by-twist","chirp-transform-procedure","source-transform",
"digit-convolution-algorithm","carry-propagation","precision-and-exact-recovery",
"cost-exponent-accounting","main-theorem"]
RANK = {p: i for i, p in enumerate(ORDER)}
KNOWN = set("""big-o-notation polynomials complex-numbers turing-machines arithmetic-modulo-n
the-field-with-two-elements greatest-common-divisor-and-coprimality prime-numbers-and-trial-division
positional-radix-number-representation two-s-complement-integers bitwise-operations hamming-weight
floor-ceiling-logarithms-and-exponentials theta-omega-and-little-o-notation geometric-series
recurrence-relations mathematical-induction-and-proof-by-contradiction sets-cartesian-products-and-lexicographic-order
permutations-and-permutation-matrices binomial-coefficients-and-counting-subsets
polar-form-euler-s-formula-and-roots-of-unity matrix-rank-and-gaussian-elimination directed-graphs
worst-case-time-complexity-of-turing-machines sorting-stability-and-radix-sort
schoolbook-multiplication-and-long-division""".split())

def ev(q):
    return {"source": "paper", "quote": q}

def mot(t, src, q=None):
    return {"text": t, "source": src, "quote": ev(q) if q else None}

def bind(sym, name, meaning, rel):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def show(id, claim, method, motivation, children, page=None, frm=None, adds=None, salient=None):
    n = {"id": id, "intention": "show", "claim": claim, "method": method,
         "motivation": motivation, "page": page, "from": frm or [], "children": children}
    if adds: n["adds"] = adds
    if salient: n["salient"] = salient
    return n

def infer(id, claim, quote, page=None, frm=None, salient=None):
    n = {"id": id, "intention": "infer", "claim": claim, "quote": ev(quote),
         "page": page, "from": frm or []}
    if salient: n["salient"] = salient
    return n

# ---------------------------------------------------------------- tree
tools_children = [
 infer("S1.1", "Intermediate frames cancel along each route, so a route from input role $w$ to output role $\\rho(w)$ applies only $D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$ with its sign.",
       "intermediate frames cancel, and a route from input role $w$ to output", "frames",
       ["linear-algebra","logical-volume","address-fields"]),
 infer("S1.2", "The number $s$ of smaller calls satisfies $s<Wm$, so the per-level factor $s/W$ stays below $m$.",
       "number $s$ of smaller calls satisfies $s<Wm$.", "rank-saving",
       ["subspace-labels","frames","linear-algebra"],
       salient="The strict inequality $s<Wm$ holds on the total of all edges, so the factor $s/W$ is strictly below $m$ at every depth of the recursion."),
 infer("S1.3", "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes, and each step moves each head by at most one cell.",
       "A machine has one fixed finite alphabet and one fixed finite number of", "fixed-tape-machine",
       ["turing-machines"]),
 infer("S1.4", "Fixed-radix digit moves, pointwise maps on aligned streams and whole-row splits take $O(V)$ steps on a fixed number of one-dimensional tapes.",
       "takes $O(V)$ steps on a fixed number of one-dimensional tapes:", "elementary-stream-operations",
       ["fixed-tape-machine","logical-volume","address-fields"]),
 infer("S1.5", "Splitting whole rows cyclically into $W$ role streams gives streams of equal shape and volume $V/W$.",
       "whole rows cyclically into a fixed number $W$ of streams", "row-splitting",
       ["elementary-stream-operations","address-fields"]),
 infer("S1.6", "A cyclic shift of a target field by an offset computed from its control fields costs $O(V)$.",
       "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the", "controlled-shifts",
       ["elementary-stream-operations","address-fields","arithmetic-modulo-n"]),
 infer("S1.7", "For arbitrary initial values of the auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.",
       "For arbitrary initial values of its auxiliary wires, a forward", "scratch-restoration",
       ["linear-algebra","gaussian-dyadic"]),
 infer("S1.8", "The three-stage network sends $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restores every auxiliary value.",
       "(X_a,Y_a)\\longmapsto(-Y_a,X_a)", "triple-subset-exchange-network",
       ["scratch-restoration","linear-algebra"]),
 infer("S1.9", "Summed over all edges, the absolute changes in label dimension equal $Wm-2N+2L$.",
       "=Wm-2N+2L.", "subspace-labels",
       ["linear-algebra","frames","triple-subset-exchange-network"]),
 infer("S1.10", "Each edge change of the binary phase frames is $\\mathcal C_V\\mathcal C_U^{-1}$, a product of one kernel per residual basis vector.",
       "$\\mathcal C_V\\mathcal C_U^{-1}$ is a product of one translation", "binary-phase-frames",
       ["two-point-butterfly","gaussian-dyadic","frames","subspace-labels","two-point-phase-kernel","hamming-weight"]),
 infer("S1.11", "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$, with invertible lower-triangular $E_1,E_2$ and a partial permutation $\\Pi$ having $a$ ones.",
       "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", "lower-triangular-factorization",
       ["linear-algebra","matrix-rank-and-gaussian-elimination","permutations-and-permutation-matrices"]),
 infer("S1.12", "The shear $(H,D)\\mapsto(H+AD,D)$ for a rational matrix $A$ of rank $a$ is performed with exactly $a$ interchanges of field pairs and $O(V)$ further work.",
       "can be performed with exactly $a$ interchanges of pairs of $b$-digit", "matrix-shear-interchange",
       ["lower-triangular-factorization","address-fields","elementary-stream-operations","logical-volume"]),
 infer("S1.13", "Two disjoint equal chunks of $e=m^k$ digits are interchanged in $O(Ve^\\tau)$ time for a fixed $\\tau<1$.",
       "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every", "power-width-chunk-interchange",
       ["matrix-shear-interchange","circuit-to-address-permutation","volume-normalized-recursion","rank-saving","subspace-labels","frames","row-splitting","address-fields"],
       salient="One exponent $\\tau<1$ serves every chunk width $e=m^k$ and every data value, and the constant does not depend on the field lengths."),
 infer("S1.14", "The cost per unit volume obeys $F_k\\le(s/W)F_{k-1}+O(1)$, so $F_k=O(e^\\tau)$ when $s/W<m^\\tau$.",
       "F_k\\le(s/W)F_{k-1}+O(1).", "volume-normalized-recursion",
       ["rank-saving","logical-volume","subspace-labels"]),
 infer("S1.15", "Equal bit chunks of arbitrary width $u$ are interchanged in $O(Vu^\\tau)$ steps by an address permutation.",
       "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.", "arbitrary-width-chunk-interchange",
       ["power-width-chunk-interchange","address-fields","logical-volume"]),
 infer("S1.16", "The two-point phase kernel $C=H\\mathsf SH=aI+bX$, with $a=(1+i)/2$ and $b=(1-i)/2$, is the Hadamard conjugate of the phase $\\mathsf S$.",
       "C=H\\mathsf SH=aI+bX,\\qquad a=\\frac{1+i}{2},\\quad b=\\frac{1-i}{2}.", "two-point-phase-kernel",
       ["two-point-butterfly","gaussian-dyadic","linear-algebra","complex-numbers"]),
 infer("S1.17", "The packed operation XORs the selected bits of one chunk into the corresponding selected bits of another and restores the scratch chunk for every initial value.",
       "It preserves the spectator coordinates, all other chunk bits, and every", "packed-selected-bit-xor",
       ["binary-phase-frames","controlled-shifts","elementary-stream-operations","address-fields","logical-volume","bitwise-operations"]),
 infer("S1.18", "The truncation $Q_p$ rounds real and imaginary parts toward zero to $2^{-p}\\mathbb Z$, keeping coefficients in the disk.",
       "Let $Q_p$ truncate", "grid-truncation",
       ["disk-grid-arrays","gaussian-dyadic"]),
 infer("S1.19", "The normalized butterfly $H_0$ on the same selected bit of $D$ chunks is applied in $O(Vd^{\\lambda'})$ time with error below $\\sqrt2\\,2^{-p}$.",
       "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,", "simultaneous-butterfly-layer",
       ["binary-phase-frames","two-point-phase-kernel","packed-selected-bit-xor","guard-bits","grid-truncation","disk-grid-arrays","two-point-butterfly","arbitrary-width-chunk-interchange","power-width-chunk-interchange","gaussian-dyadic"]),
 infer("S1.20", "The layer uses at most $p+\\lceil C_0d^{C_1}\\rceil$ fractional bits per real component, which is $O(p)$.",
       "at most $p+\\lceil C_0d^{C_1}\\rceil$ fractional bits and", "guard-bits",
       ["gaussian-dyadic","two-point-phase-kernel","binary-phase-frames"]),
 infer("S1.21", "In $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$, multiplication by $y^a$ permutes the coefficients with signs, so it is an isometry.",
       "by $y^a$, for any integer $a$, permutes the coefficients and changes", "polynomial-ring",
       ["polynomials","complex-numbers"]),
 infer("S1.22", "For a power of two $t$ dividing $2r$, the element $\\omega_t=y^{2r/t}$ is a root of unity whose multiplication is a signed shift.",
       "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.", "polynomial-roots-of-unity",
       ["polynomial-ring","polar-form-euler-s-formula-and-roots-of-unity"]),
 infer("S1.23", "The normalized synthetic transforms over $\\mathcal R_r$ are contractions, since each output averages isometric images of the inputs.",
       "Thus both transforms are contractions.", "synthetic-transform",
       ["polynomial-ring","polynomial-roots-of-unity","two-point-butterfly","grid-truncation","disk-grid-arrays"]),
 show("S1.24",
      "The forward and opposite synthetic transforms run on fixed tapes as simultaneous butterfly rounds on a positional layout, with error below $\\sqrt2\\,\\ell\\,2^{-p}$ and cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
      "lay the record addresses out so that each round is a simultaneous butterfly layer, then charge the layout, the rounds and their restoration",
      mot("Positional layouts place the selected bits of every round in a common chunk, so the simultaneous layer applies to them.", "recoverable"),
      [
        infer("S1.24.1", "The procedure constructs an explicit positional layout permutation $L$ of record addresses that preserves the polynomial suffixes.",
              "The procedure constructs an explicit positional", "transform-layout",
              ["simultaneous-butterfly-layer","address-fields","arbitrary-width-chunk-interchange","power-width-chunk-interchange","polynomial-roots-of-unity"]),
        infer("S1.24.2", "Each procedure has error less than $\\sqrt2\\,\\ell\\,2^{-p}$ and returns disk-grid coefficients in the same component format.",
              "Each procedure has error less than", None, []),
        infer("S1.24.3", "Each procedure costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$, with the layout construction and restoration charged.",
              "O\\left(Tp\\left[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}\\right]\\right).", None, []),
      ],
      page="synthetic-transform-on-tapes",
      frm=["synthetic-transform","simultaneous-butterfly-layer","guard-bits","polynomial-roots-of-unity"]),
        infer("S1.25", "The forward procedure keeps its output layout through a pointwise product, and the opposite procedure consumes that order.",
              "The forward procedure may retain its output layout for a", "frequency-order-retention",
              ["synthetic-transform-on-tapes","transform-layout"]),
 infer("S1.25", "The exact Gaussian integer numerators of $fg$ can be computed, and $Q_p(fg/r)$ returned, in time $O(rp\\log(rp))$ on a fixed number of tapes.",
       "$O(rp\\log(rp))$ on a fixed number of tapes.", "signed-coefficient-packing",
       ["hvdh-multiplier","polynomial-ring","gaussian-dyadic","disk-grid-arrays"]),
 infer("S1.27", "The normalized product $Q_p(fg/r)$ is a disk-grid polynomial within $\\sqrt2\\,2^{-p}$ of $fg/r$.",
       "grid polynomial with error less than $\\sqrt2\\,2^{-p}$ from $fg/r$.", "ring-product",
       ["signed-coefficient-packing","grid-truncation","disk-grid-arrays","polynomial-ring"]),
 infer("S1.28", "The bilinear contraction $\\mathcal M_r(f,g)=(f*g)/(rM)=(f*g)/T$ is computed by two forward synthetic transforms, a pointwise ring product and an opposite transform.",
       "\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.", "normalized-ring-convolution",
       ["ring-product","synthetic-transform-on-tapes","frequency-order-retention","synthetic-transform","polynomial-ring"]),
 infer("S1.29", "The identity $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ expresses a length-$s$ transform through a length-$t$ transform, with contractions $A$ and $B_0$ built from Gaussian weights.",
       "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA", "gaussian-resampling",
       ["contraction","discrete-fourier-transform","gaussian-dyadic"]),
 infer("S1.30", "Fixed multitape algorithms approximate $A$ and $B_0$ with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, leaving both coordinate permutations in the transform identity.",
       "There are fixed multitape algorithms for approximations", "permutation-free-resampling",
       ["gaussian-resampling","contraction","approximate-roots-of-unity","disk-grid-arrays"]),
 infer("S1.31", "$RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ holds, with $\\mathcal A$ and $\\mathcal B_0$ tensor products of the one-dimensional contractions.",
       "=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A,", "tensor-resampling",
       ["permutation-free-resampling","gaussian-resampling","discrete-fourier-transform","contraction"]),
 infer("S1.32", "With the chirp $a$, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, a cyclic convolution with pointwise phases.",
       "\\frac{a*(\\overline a\\mathbin{\\cdot}u)}{T}.", "bluestein-chirp",
       ["discrete-fourier-transform","cyclic-convolution","arithmetic-modulo-n"]),
]

tools = show("S1",
  "The fixed-tape operations used by the product are exact where required, approximate their transforms within stated errors, and cost time linear in volume times a power of $p$ below one.",
  "build address changes from finite linear networks with a rank saving, then apply them to butterfly layers, polynomial-ring transforms and resampling",
  mot("Rescanning the transform at each of its levels already costs $\\Theta(n\\log n)$, so data movement and arithmetic must both be cheapened.", "explicit",
      "We therefore need savings in both movement and arithmetic."),
  tools_children, page=None, frm=[],
  adds=[bind("m","label dimension","The fixed dimension of the space that carries the subspace labels on each network vertex.","count"),
        bind("W","role count","The fixed number of role streams into which the rows of an array are split.","count"),
        bind("s","smaller calls","The number of smaller recursive calls made on one edge of a network.","count")])

exact_children = [
 show("S2.1", "Fixed rational exponents and size parameters are chosen so that the padded box, the digit count and the prime lengths meet the bounds used later.",
      "fix the rational exponents, then derive $b$, $p$, $d$, $K$ and the prime lengths from $n$",
      mot("Every later bound refers to these sizes, so they are fixed first.", "recoverable"),
      [
        infer("S2.1.1", "The fixed rational exponents are $\\tau=\\sigma=1-2^{-50}$, $\\beta=\\frac12$ and $\\delta=\\frac1{16}$.",
              "\\tau=\\sigma=1-2^{-50},\\qquad \\beta=\\frac12,\\qquad \\delta=\\frac1{16},", "fixed-exponent-choices",
              ["floor-ceiling-logarithms-and-exponentials"]),
        infer("S2.1.2", "The size parameters are $b=\\lceil\\log_2 n\\rceil$, $p=6b$ and $d=\\lfloor b^\\epsilon\\rfloor$, with $K=\\lfloor d^c\\rfloor$.",
              "b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,", "size-parameters",
              ["fixed-exponent-choices","floor-ceiling-logarithms-and-exponentials"]),
        infer("S2.1.3", "Distinct odd primes $s_i$ just below the powers of two $t_i$ give $T/2<S<T$, where $S=\\prod_i s_i$.",
              "Together with $s_i<t_i$, this gives $T/2<S<T$.", "prime-source-lengths",
              ["size-parameters","fixed-exponent-choices","prime-numbers-and-trial-division","greatest-common-divisor-and-coprimality"]),
      ], frm=[]),
 show("S2.2", "The product of $x$ and $y$ is the cyclic convolution of their $q$ radix-$2^b$ digits, whose coefficients $c_j$ are bounded as below.",
      "write both inputs as polynomials in $2^b$, check that the cyclic length exceeds the product degree, and bound each coefficient",
      mot("Splitting into radix digits turns the product into a convolution of small integers.", "recoverable"),
      [
        infer("S2.2.1", "Both inputs are written as polynomials in $2^b$, each with $q=\\lceil n/b\\rceil$ nonnegative digits.",
              "Write the two inputs as polynomials in $2^b$, each with", None, []),
        infer("S2.2.2", "Convolution modulo $x^S-1$ has no nonzero wraparound, since the product has degree below $2n/b\\le T/2<S$.",
              "Thus convolution modulo $x^S-1$ has no nonzero wraparound.", None, []),
        infer("S2.2.3", "Every product coefficient satisfies $0\\le c_j\\le q(2^b-1)^2<2^{3b}$.",
              "0\\le c_j\\le q(2^b-1)^2<2^{3b}", None, []),
      ], page="radix-digit-convolution", frm=["cyclic-convolution","positional-radix-number-representation"]),
 show("S2.3", "For pairwise coprime lengths $s_i$ with $S=\\prod_i s_i$, the map $\\Phi$ turns the ordinary coefficient order into a mixed-radix tensor order.",
      "apply the Chinese-remainder map $x\\mapsto\\prod_i x_i^{\\mu_i}$ to the coefficient list, realized by controlled cyclic shifts",
      mot("The source transform acts on a tensor of cyclic axes, so the coefficient stream must first be placed in tensor order.", "explicit",
          "To use the source tensor, we first place the ordinary coefficient stream"),
      [
        infer("S2.3.1", "The assignment $\\Phi$ is an algebra isomorphism that preserves cyclic convolution.",
              "$\\Phi$ is an isomorphism and preserves cyclic convolution.", None, []),
      ], page="crt-coefficient-map", frm=["cyclic-convolution","arithmetic-modulo-n","controlled-shifts","radix-digit-convolution"]),
 show("S2.4", "The normalized complex cyclic convolution $(f*g)/T$ is computed by twisting each operand by powers of $\\zeta$, applying the ring convolution, and untwisting.",
      "apply a diagonal phase twist on the last coordinate, which turns cyclic into negacyclic convolution over $\\mathcal R_r$",
      mot("The complex convolution is taken from the synthetic ring convolution by a coefficient twist.", "explicit",
          "obtained from the synthetic convolution by a coefficient twist."),
      [
        infer("S2.4.1", "The substitution $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ is well defined on $\\mathbb C[x_d]/(x_d^r-1)$ and multiplies coefficient $k$ by $\\zeta^k$.",
              "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$.", "negacyclic-twist",
              ["polynomial-ring","polynomial-roots-of-unity","cyclic-convolution"]),
        infer("S2.4.2", "The normalized complex cyclic convolution is $D_-\\iota^{-1}\\mathcal M_r(\\iota D_+f,\\iota D_+g)=(f*g)/T$.",
              "\\mathcal M_r(\\iota D_+f,\\iota D_+g)", None, ["normalized-ring-convolution","negacyclic-twist"]),
        infer("S2.4.3", "Disk-grid approximations to $\\zeta^{k}$ and $\\zeta^{-k}$ with error below $2\\,2^{-p}$ are obtained for every $0\\le k<r$.",
              "For $0\\le k<r$, obtain disk-grid approximations", "approximate-roots-of-unity",
              ["polynomial-roots-of-unity","disk-grid-arrays","grid-truncation","polynomial-ring"]),
      ], page="complex-convolution-by-twist", frm=["polynomial-ring","normalized-ring-convolution","approximate-roots-of-unity","disk-grid-arrays","cyclic-convolution","negacyclic-twist"]),
 show("S2.5", "The computed chirp transform, with approximate phases, a computed complex convolution and final truncations, maps disk-grid arrays of norm at most $.6$ to approximations of $QF_{\\boldsymbol t}x$.",
      "apply the chirp identity with approximate phases, the computed convolution and the final truncations",
      mot("The transform factor is computed from a cyclic convolution and two pointwise phase multiplications, so the chirp identity supplies it.", "explicit",
          "computed from a cyclic convolution and two pointwise phase"),
      [
        infer("S2.5.1", "Replacing the approximations by exact phases and exact convolution gives $\\overline a\\cdot\\mathcal M_{\\mathbb C}(a,\\overline a\\cdot x)=QF_{\\boldsymbol t}x$.",
              "by exact phases and exact convolution gives", None, ["bluestein-chirp","complex-convolution-by-twist"]),
      ], page="chirp-transform-procedure", frm=["bluestein-chirp","complex-convolution-by-twist","approximate-roots-of-unity","contraction","disk-grid-arrays"]),
 show("S2.6", "The computed source transform approximates $RF_{\\boldsymbol s}$ on disk-grid arrays of norm at most $.5$, and its exact counterpart is $2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
      "apply the linewise resampling map $\\mathcal A$, then the computed chirp transform, then the linewise map $\\mathcal B_0$, and multiply by $2^\\gamma$",
      mot("Each exact stage is a contraction, so the stage errors add and the disk bounds carry through the composition.", "recoverable"),
      [
        infer("S2.6.1", "The exact counterpart of the source transform is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$.",
              "\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A", None, []),
      ], page="source-transform", frm=["tensor-resampling","chirp-transform-procedure","contraction","disk-grid-arrays","size-parameters"]),
 infer("S2.7", "The source-transform procedures supply the three transforms needed for the radix-digit convolution.",
       "The source-transform procedures now supply the three transforms needed", None,
       ["source-transform","frequency-order-retention","normalized-ring-convolution"]),
 show("S2.8", "Every intermediate array stays in the disk, and the recovered integer coefficients have total error below one half, so rounding gives the exact product.",
      "bound each disk margin with one cutoff, identify the opposite transform of the product as $(u*v)/S^2$, and bound the final coefficient error",
      mot("Exact recovery needs the error of the whole chain of stages to stay below the rounding threshold.", "recoverable"),
      [
        infer("S2.8.1", "All disk margins are enforced by one fixed cutoff for all sufficiently large $n$.",
              "All these margins may be enforced by one fixed cutoff.", None, []),
        infer("S2.8.2", "The exact opposite transform of the product of the two forward source transforms is $(u*v)/S^2$, so the source permutation cancels.",
              "G(U\\cdot V_1)=(u*v)/S^2.", "source-permutation-cancellation",
              ["tensor-resampling","permutation-free-resampling","discrete-fourier-transform","bluestein-chirp"]),
        infer("S2.8.3", "The final absolute error of each recovered coefficient is at most $448b\\,2^{-3b/4}$, which is below $\\frac12$.",
              "\\le448b\\,2^{-3b/4}<\\frac12.", None, []),
        infer("S2.8.4", "The true coefficients are real integers, so the nearest integer to each recovered value is the correct coefficient.",
              "The true coefficients are real integers.", None, []),
      ], page="precision-and-exact-recovery", frm=["disk-grid-arrays","grid-truncation","contraction","source-transform","ring-product"]),
 show("S2.9", "The carries $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$ with $Q_0=2^b$ turn the coefficients into the binary digits of the product.",
      "process the coefficients from least to most significant, keeping a single carry",
      mot("Each carry is bounded, so one counter of $O(b)$ bits suffices.", "recoverable"),
      [
        infer("S2.9.1", "Set $Q_0=2^b$ and carry $k_0=0$ before processing the coefficients.",
              "To propagate carries, let $Q_0=2^b$.", None, []),
        infer("S2.9.2", "The digits satisfy $d_j=(c_j+k_j)\\bmod Q_0$ and the carries satisfy $k_{j+1}=\\lfloor(c_j+k_j)/Q_0\\rfloor$.",
              "k_{j+1}=\\left\\lfloor\\frac{c_j+k_j}{Q_0}\\right\\rfloor.", None, []),
        infer("S2.9.3", "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.",
              "The carries satisfy $0\\le k_j\\le q(Q_0-1)<Q_0^2$.", None, []),
        infer("S2.9.4", "The invariant $\\sum_{h<j}c_hQ_0^h=\\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ holds for every $j$, so the first $j$ digits of the product are fixed.",
              "It holds for $j=0$, and the defining relation proves its next instance.", None, []),
      ], page="carry-propagation", frm=["radix-digit-convolution","crt-coefficient-map","positional-radix-number-representation"]),
]
exact = show("S2",
  "On input $x\\#y$ the procedure outputs exactly the $2n$-bit binary product of $\\operatorname{val}(x)$ and $\\operatorname{val}(y)$.",
  "fix the sizes, reduce to a radix-digit convolution, evaluate it through the approximate transforms with chirp and twist, recover the integers by rounding, then propagate carries",
  mot("Splitting into radix digits turns the product into a convolution of small integers, which rounding recovers from an accurate evaluation.", "explicit",
      "Splitting the inputs into radix digits reduces multiplication to"),
  exact_children, page="digit-convolution-algorithm", frm=[],
  adds=[bind("b","digit width","The number of bits in each radix digit, $b=\\lceil\\log_2 n\\rceil$.","count"),
        bind("q","digit count","The number of radix digits in each input.","count"),
        bind("p","precision bits","The number of fractional bits of the working grid $2^{-p}\\mathbb Z$.","count"),
        bind("T","box size","The size of the padded power-of-two index box.","count"),
        bind("S","cyclic length","The product of the prime cyclic lengths $s_i$.","count")])

cost = show("S3",
  "Every cost term is $Tp$ times a power of $p$ with exponent at most $1-2\\kappa$, so the total time is $O(n(\\log n)^{1-\\kappa})$.",
  "write each cost term as $Tp$ times a power of $p$, bound the seven dominant exponents below $1-2\\kappa$, and convert $p$ to $\\log n$",
  mot("The bound is the largest of the dominant powers, so each must fall below one by a common margin.", "recoverable"),
  [
    infer("S3.1", "The seven dominant powers in the cost table have margins $g_1,\\dots,g_7$ below one, given in the margin equation.",
          "The seven dominant powers in Table~\\ref{tab:costs} have the following", None, []),
    infer("S3.2", "The smallest margin is $\\min_i g_i=2^{-181}=2\\kappa$, so every dominant exponent is at least $2\\kappa$ below one.",
          "Thus $\\min_i g_i=2^{-181}=2\\kappa$.", None, [],
          salient="All seven dominant exponents lie at least $2\\kappa=2^{-181}$ below one, a single common margin for every cost term."),
    infer("S3.3", "Each of the seven displayed powers is at most $1-2\\kappa$, and any fixed power of $\\log p$ is at most $p^\\kappa$ eventually.",
          "Each of the seven displayed powers is at most $1-2\\kappa$ by", None, []),
    infer("S3.4", "The complete large-input bound is $O(Tp\\cdot p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
          "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa}).", None, []),
  ], page="cost-exponent-accounting", frm=["precision-and-exact-recovery","carry-propagation","fixed-exponent-choices","size-parameters","synthetic-transform-on-tapes","simultaneous-butterfly-layer","tensor-resampling","signed-coefficient-packing"],
  adds=None)

conj = infer("S0.1", "The bound $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa>0$ disproves the $n\\log n$ optimality conjecture of Schönhage and Strassen for this fixed-tape model.",
             "disproves the $n\\log n$ optimality conjecture", "schonhage-strassen-conjecture", [])

root = show("S0",
  "On one deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, two $n$-bit integers multiply exactly in worst-case time $O(n(\\lg n)^{1-\\kappa})$, with $\\kappa=2^{-182}$.",
  "show that the fixed-tape tools are cheap and accurate, show that the transform pipeline returns the exact product, then bound its total cost",
  mot("The claim has three parts, all about one algorithm: its tape operations, its exactness and its total cost.", "recoverable"),
  [conj, tools, exact, cost], page="main-theorem", frm=[],
  adds=[bind("\\kappa","saving exponent","The fixed rational constant $\\kappa=2^{-182}$ by which the exponent of $\\lg n$ falls below one.","direct")])

# ---------------------------------------------------------------- collect
def walk(n, acc):
    acc.append(n)
    for c in n.get("children", []):
        walk(c, acc)
    return acc
ALL = walk(root, [])
ids = [n["id"] for n in ALL]
assert len(ids) == len(set(ids)), "duplicate ids"

# effective page (inherit from nearest ancestor)
def eff_pages(n, inherited, out):
    p = n["page"] if n.get("page") else inherited
    out[n["id"]] = p
    for c in n.get("children", []):
        eff_pages(c, p, out)
    return out
EFF = eff_pages(root, None, {})

# ---------------------------------------------------------------- checks
problems = []
# pages: each presented page appears once (as explicit page on a node)
presented = [n["page"] for n in ALL if n.get("page")]
for p in presented:
    if presented.count(p) > 1:
        problems.append("page presented twice: " + p)
# from constraints
for n in ALL:
    pg = EFF[n["id"]]
    for f in n.get("from", []):
        if f in KNOWN:
            continue
        if f not in RANK:
            problems.append(f"{n['id']}: unknown from id {f}")
        elif pg is not None and RANK[f] >= RANK[pg]:
            problems.append(f"{n['id']} (page {pg}): from {f} is not before its page")
# coverage: each page not presented must appear in some from
used = set()
for n in ALL:
    for f in n.get("from", []):
        used.add(f)
for p in ORDER:
    if p not in presented and p not in used:
        problems.append("page neither presented nor used in from: " + p)
# one step per page (explicit pages)
# quotes exist; deferred computation in DFS order
def occurrences(q):
    out = []
    start = 0
    while True:
        i = text.find(q, start)
        if i < 0: break
        out.append(text.count('\n', 0, i) + 1)
        start = i + 1
    return out
infers = [n for n in ALL if n["intention"] == "infer"]
last = 0
for n in infers:
    q = n["quote"]["quote"]
    occ = occurrences(q)
    if not occ:
        problems.append(f"{n['id']}: quote not found: {q}")
        continue
    later = [o for o in occ if o > last]
    if later:
        last = later[0]
        n.pop("deferred", None)
    else:
        n["deferred"] = True
# adds check: symbol occurs in descendant claims
def desc_claims(n):
    out = []
    for c in n.get("children", []):
        out.append(c["claim"])
        out.extend(desc_claims(c))
    return out
for n in ALL:
    for a in n.get("adds", []):
        sym = a["symbol"]
        dc = desc_claims(n)
        if not any(sym in c for c in dc):
            problems.append(f"{n['id']}: add {sym} not used in descendant claims")

# strip helper fields and empty children for infer nodes
def clean(n):
    out = {}
    for k, v in n.items():
        if k == "children":
            if v:
                out[k] = [clean(c) for c in v]
            continue
        if v is None and k in ("method", "motivation", "quote", "page"):
            out[k] = None
            continue
        out[k] = v
    if n["intention"] == "infer":
        out.pop("children", None)
        out.pop("method", None)
        out.pop("motivation", None)
    return out

answer = {"root": clean(root)}
if "--check" in sys.argv:
    print("problems:", problems)
    print("deferred:", [n["id"] for n in infers if n.get("deferred")])
    print("pages presented:", len(presented), "of", len(ORDER))
else:
    if problems:
        print("PROBLEMS:"); [print(" ", p) for p in problems]
        sys.exit(1)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(answer, f, ensure_ascii=False, indent=2)
    print("wrote", OUT)
    print("deferred:", [n["id"] for n in infers if n.get("deferred")])
