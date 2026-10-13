import json
P="paper"
def ev(*qs): return [{"source":P,"quote":q} for q in qs]
C=[]
def add(id,name,gloss,requires,evidence=(),known=False,aliases=(),title=None,symbols=None):
    d={"id":id,"name":name,"aliases":list(aliases),"gloss":gloss,"requires":list(requires),"known":known,"evidence":ev(*evidence)}
    if title: d["title"]=title; d["symbols"]=symbols
    C.append(d)

add("big-o","Big-O notation","Asymptotic upper bounds on running time such as O(n log n).",[],known=True)
add("polynomial","Polynomials","Expressions Σ a_k x^k with addition and multiplication, including coefficient lists.",[],known=True)
add("complex-numbers","Complex numbers","Numbers a + bi, with modulus, conjugate and roots of unity e^{2πi/q}.",[],known=True)
add("turing-machine","Turing machines and tapes","Machines with a finite control, tapes of cells and read/write heads that move one cell per step.",[],known=True)

add("fixed-tape-model","Fixed-tape Turing machine model","The model where one machine has a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step touching one cell per tape, so time counts head movement as well as arithmetic.",["turing-machine"],
 ["A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes.",
  "Fixed tracks and finitely\nmany work tapes change time by a fixed factor."])
add("elementary-stream-ops","Elementary stream operations on tape arrays","Linear-time scans on an array stored in lexicographic order: swapping or moving one digit, splitting into streams by a digit or cyclically by rows, applying a pointwise map, and merging back.",["fixed-tape-model","big-o"],
 ["takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
  "An address permutation $f$ moves the entry at $x$ to $f(x)$."])
add("controlled-shift","Controlled shifts and rational scalings","An O(V) tape operation that adds an offset computed from earlier fields to a later field modulo q^b (a cyclic shift), or multiplies it by a fixed rational unit.",["elementary-stream-ops"],
 ["y\\longmapsto y+a(\\text{controls})\\pmod Q",
  "Controlled shifts and fixed rational scalings"])
add("convolution","Convolution","The product of two coefficient lists, cyclic when indices wrap around modulo the length, equal to polynomial multiplication modulo x^S − 1.",["polynomial"],
 ["Splitting the inputs into radix digits reduces multiplication to\nconvolution of short integer coefficients.",
  "let $*$ denote cyclic convolution in the displayed\naxes"])
add("radix-digit-convolution","Integer multiplication as digit convolution","Writing each n-bit integer as a polynomial in 2^b with digits of b bits, so the integer product is a convolution of digit lists followed by carry propagation.",["convolution","big-o"],
 ["Write the two inputs as polynomials in $2^b$, each with",
  "Thus convolution modulo $x^S-1$ has no nonzero wraparound."])
add("dft","Discrete Fourier transform","The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q}, which turns convolution into pointwise multiplication.",["complex-numbers","convolution"],
 ["(F_q u)_k=\\frac1q\\sum_{j=0}^{q-1}u_j e^{-2\\pi i jk/q},",
  "The normalized convolution rule is"])
add("fft-butterfly","Radix-2 butterflies and FFT","Computing a power-of-two transform by repeated two-point butterflies (u,v) ↦ ((u+v)/2,(u−v)/2) followed by twiddle multiplications and smaller transforms (decimation in frequency).",["dft"],
 ["H_0(u,v)=\\bigl((u+v)/2,(u-v)/2\\bigr)",
  "the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for"])
add("linear-subspaces","Subspaces, rank and orthogonal complements","Linear algebra over Q or F_2: subspaces, matrix rank, bilinear forms, orthogonal complements and projections.",[],
 ["A label is a nondegenerate subspace of a fixed bilinear space.",
  "the \\emph{orthogonal residual} is the orthogonal complement of the smaller label inside"])
add("fixed-point-precision","Fixed-point disk arithmetic and truncation error","Storing complex numbers of modulus at most 1 as signed binary numerators over 2^p, truncating toward zero, and tracking how contractions and bilinear maps propagate the errors.",["complex-numbers"],
 ["A disk array has norm at most one.",
  "\\|Q_p z-z\\|_\\infty<\\sqrt2\\,2^{-p},\\qquad"])
add("nlogn-multiplier","Established O(n log n) integer multiplier","The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records.",["fixed-tape-model","big-o"],
 ["the established $O(n\\log n)$ multiplier as an\nordinary subroutine.",
  "they do not invoke the improved theorem recursively."])
add("synthetic-ring","Polynomial ring modulo y^r + 1","The ring of complex polynomials of degree below r with y^r = −1, where multiplying by a power of y is a signed shift of the coefficient list.",["polynomial","complex-numbers"],
 ["\\mathcal R_r=\\mathbb C[y]/(y^r+1),",
  "by $y^a$, for any integer $a$, permutes the coefficients and changes\nsome signs"],
 title="Polynomial ring modulo $y^r + 1$",
 symbols=[{"symbol":"y","name":"ring variable","meaning":"The polynomial variable, which satisfies y^r = −1 in the ring.","relation":"direct"},
          {"symbol":"r","name":"record length","meaning":"The number of complex coefficients in a polynomial record, a power of two.","relation":"count"}])
add("synthetic-transform","Synthetic polynomial transform","A Fourier transform whose roots of unity are ω_t = y^{2r/t} in the ring modulo y^r + 1, so twiddles are signed shifts, computed by butterfly rounds with outputs left in bit-reversed order.",["synthetic-ring","fft-butterfly"],
 ["For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",
  "multiplication by\nsuch a root is a signed shift of the coefficient list."])
add("signed-packing","Signed packing of polynomial products","Kronecker substitution: evaluating ring polynomials at 2^{4p} to multiply them with the integer multiplier, then reading coefficients back by centered residues.",["synthetic-ring","nlogn-multiplier","fixed-point-precision"],
 ["The reduction is a signed form of Kronecker substitution; compare",
  "Signed packing and normalized ring multiplication"])
add("phase-kernel-c","Two-point kernel C and phase frames","The matrix C = H S H = aI + bX with C^2 = X and H_0 = b S C S, so a butterfly layer is a phase-conjugated tensor power of C.",["fft-butterfly"],
 ["H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad",
  "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D."])
add("frames-on-arrays","Frames on pointwise linear networks","Replacing scalars on wires by arrays and assigning each gate an invertible frame operator that commutes with the gate, so edges only change representation and the endpoint operators telescope.",["linear-subspaces"],
 ["At a pointwise linear gate $G$, the common frame commutes with the gate:",
  "We call $D_v$ its frame: the stored"])
add("exchange-network","Subset-intersection exchange network","A fixed linear network of copy, gather, scatter and side wires indexed by three-element subsets that swaps two banks X and Y with a sign and restores arbitrary scratch values.",["linear-subspaces"],
 ["invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
  "(X_a,Y_a)\\longmapsto(-Y_a,X_a)"])
add("subspace-labels","Subspace labels and the rank budget","Nested nondegenerate subspaces attached to gates so each edge's dimension change counts the smaller operations needed, with total dimension lost small enough to give a strict deficit.",["exchange-network","frames-on-arrays","linear-subspaces"],
 ["A label is a nondegenerate subspace of a fixed bilinear space.",
  "The only decreasing\nedges are the central-wire edges from time 3 to time 4; their dimension\nloss is $h$."])
add("recursive-power-saving","Recursive power saving from a rank deficit","If a call at parameter mf is made from s calls at parameter f on streams of volume V/W with s < Wm, the normalized cost grows like m^τ per level with τ < 1.",["big-o"],
 ["This strict inequality\nis the source of the power saving.",
  "The decisive property is that the total\nnumber $s$ of smaller calls satisfies $s<Wm$."])
add("bit-network-interface","Bit network shear interface","The bit version of the network with rational matrices M_v at gates such that the endpoint difference is the identity, i.e. the shear H ← H + D, with rank sum s_b < W_b m.",["subspace-labels"],
 ["The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",
  "M_{\\mathrm{sink}(\\rho(w))}-M_{\\mathrm{source}(w)}=I_m"])
add("triangular-factorization","Lower triangular (Bruhat-type) factorization","Every rational matrix A of rank a factors as E_1 Π E_2 with lower triangular invertible E_1, E_2 and a partial permutation Π with a ones.",["linear-subspaces"],
 ["Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization"])
add("matrix-shear","Cost of a rational matrix shear","The map (H,D) ↦ (H + AD, D) over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus O(V) other work.",["triangular-factorization","controlled-shift"],
 ["can be performed with exactly $a$ interchanges of pairs of $b$-digit",
  "D_j\\leftarrow D_j+H_i,\\qquad"])
add("power-width-interchange","Power-width address interchange","Swapping two chunks of m^k digits by running the bit network with matrix shears as edges, each edge recursing into smaller interchanges, in time O(V e^τ).",["bit-network-interface","matrix-shear","recursive-power-saving","frames-on-arrays","elementary-stream-ops"],
 ["The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",
  "Power-width interchange with rows"])
add("chunk-interchange","Fast chunk interchange","Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.",["power-width-interchange"],
 ["(p,h,g,d,z)\\longmapsto(p,d,g,h,z)",
  "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$."])
add("complex-phase-network","Complex phase network","The complex-scalar version of the exchange network with binary labels whose phase frames i^{wt(Px)} reduce to translation kernels aI + bX_v, giving C^{⊗m} on every role with s_c < W_c m.",["subspace-labels","phase-kernel-c","exchange-network"],
 ["is a product of one translation\nkernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis",
  "q_U(x)=\\operatorname{wt}(P_Ux)\\pmod4."])
add("packed-selected-bit-addition","Packed selected-bit addition","Adding corresponding selected bits of two address chunks (a binary row addition) by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.",["controlled-shift","chunk-interchange"],
 ["y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}",
  "Packed selected-bit addition on one rectangle"])
add("simultaneous-butterfly-layer","Simultaneous butterfly layer","Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.",["complex-phase-network","packed-selected-bit-addition","recursive-power-saving","fixed-point-precision","chunk-interchange","fft-butterfly"],
 ["The procedure returns $Q_p(\\mathcal H z)$ in the same array,",
  "whereas separate butterfly\nfactors would require $D$ whole-array passes."])
add("synthetic-transform-layout","Synthetic transform layout and cost","Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.",["synthetic-transform","simultaneous-butterfly-layer","chunk-interchange"],
 ["The procedure constructs an explicit positional\nlayout permutation $L$ of record addresses",
  "Transform layout and cost"])
add("synthetic-convolution","Convolution from the retained transform layout","Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.",["synthetic-transform-layout","signed-packing"],
 ["\\mathcal M_r(f,g)=\\frac{f*g}{rM}=\\frac{f*g}{T}.",
  "Perform both forward transforms and retain their common $LB$ order."])
add("convolution-twist","Coefficient twist to the negacyclic ring","The map x_d ↦ ζy with ζ = e^{πi/r} that turns cyclic convolution in the last coordinate into convolution modulo y^r + 1, so complex cyclic convolution reduces to the synthetic one.",["synthetic-convolution","synthetic-ring"],
 ["x_d\\longmapsto\\zeta y",
  "is well defined, since $(\\zeta y)^r=(-1)(-1)=1$."])
add("gaussian-resampling","Gaussian resampling","Relating a Fourier transform of coprime length s to one of larger power-of-two length t via Gaussian-weighted contractions A and B_0, as P_sF_s = 2^{2α²} B_0 P_t F_t A.",["dft","fixed-point-precision","nlogn-multiplier"],
 ["P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
  "Gaussian resampling\nconnects these two shapes."])
add("tensor-resampling","Multidimensional resampling on a padded box","Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.",["gaussian-resampling","chunk-interchange"],
 ["If each $t_i\\in\\{r/2,r\\}$ with $r=2^\\ell$, the array is kept in the",
  "Tensor interface"])
add("chirp-identity","Bluestein chirp identity","Writing a Fourier transform (with its target permutation) as a pointwise chirp phase, a cyclic convolution with the chirp, and another chirp phase.",["dft","convolution"],
 ["Bluestein's chirp identity converts the middle transform,",
  "Chirp and permutation cancellation"])
add("permutation-cancellation","Source permutation cancellation","The coordinate permutation retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².",["dft","convolution","gaussian-resampling"],
 ["The second identity shows how the\nretained source permutation $R$ cancels when computing a convolution.",
  "the source permutation retained during resampling cancels"])
add("crt-axis-map","Chinese-remainder axis map","Mapping a cyclic convolution of length S = ∏ s_i with pairwise coprime s_i to a multidimensional cyclic convolution via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.",["convolution","controlled-shift","chunk-interchange"],
 ["x\\longmapsto\\prod_i x_i^{\\mu_i}",
  "Agarwal and Cooley used the Chinese remainder"])
add("parameter-choices","Parameter choices","Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.",["crt-axis-map","gaussian-resampling","radix-digit-convolution"],
 ["b=\\lceil\\log_2n\\rceil,\\quad p=6b,\\quad d=\\lfloor b^\\epsilon\\rfloor,",
  "\\lambda=1-2^{-52},\\qquad c=2^{-56},\\qquad"])
add("exact-recovery","Exact recovery of the integer product","Showing the accumulated numerical error on the recovered coefficients is below 1/2, rounding to integers, and propagating radix carries to the exact 2n-bit product.",["fixed-point-precision","radix-digit-convolution"],
 ["proves that the recovered\ncoefficient error is strictly below $1/2$, and propagates carries to",
  "Propagate radix-$2^b$ carries in increasing coefficient order."])
add("multiplication-algorithm","The multiplication algorithm","Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.",["crt-axis-map","tensor-resampling","chirp-identity","permutation-cancellation","convolution-twist","radix-digit-convolution","parameter-choices","exact-recovery"],
 ["Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain",
  "The two occurrences of $S$ in this algorithm undo different\nnormalizations."])
add("cost-accounting","Complete time bound","Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).",["multiplication-algorithm","chunk-interchange","simultaneous-butterfly-layer","synthetic-convolution","tensor-resampling"],
 ["Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
  "O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})."])
add("sub-nlogn-multiplication","Sub-n log n integer multiplication","A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.",["multiplication-algorithm","cost-accounting","fixed-tape-model"],
 ["T_A(n)=O\\!\\left(n(\\lg n)^{1-\\kappa}\\right),",
  "We give a deterministic algorithm that multiplies two $n$-bit integers"])
json.dump({"target":"sub-nlogn-multiplication","concepts":C},open("../0001-extract.answer.json","w"),indent=1)
# verify
import re
src=open("/home/user/openai-nlogn-wiki/runs/G4/sources/paper.tex").read()
n=lambda s:re.sub(r"\s+","",s)
ns=n(src)
for c in C:
    for e in c["evidence"]:
        if n(e["quote"]) not in ns: print("MISSING",c["id"],e["quote"])
ids={c["id"] for c in C}
for c in C:
    for r in c["requires"]: assert r in ids,(c["id"],r)
print(len(C))
