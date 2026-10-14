import json,sys
SRC=open('../../../sources/paper.tex').read()
def Q(q):
    assert q in SRC, q
    return {"source":"paper","quote":q}
def infer(id,claim,quote,page=None,frm=(),salient=None):
    return {"id":id,"intention":"infer","claim":claim,"quote":Q(quote),"page":page,"from":list(frm),"salient":salient}
def show(id,claim,method,mot,src,children,page=None,frm=(),salient=None,adds=None,quote=None):
    m={"text":mot,"source":src,"quote":Q(quote) if quote else None}
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":m,"children":children,"page":page,"from":list(frm),"salient":salient}
    if adds: n["adds"]=adds
    return n

# --- C1 tape toolkit
c11=infer("S1.1","An array with a product address set, stored in lexicographic order, supports digit permutation, digit move, splitting on a digit with a pointwise map and merging, and cyclic row splitting into streams, each in $O(V)$ time on a fixed number of tapes.",
 "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",page="stream-ops",
 frm=["lexicographic-order-and-mixed-radix-indexing","multitape-tm","tape-based-subroutines-and-stacks","sorting-merging-and-radix-sort"])
c12=infer("S1.2","Updating a later address field $y$ by $y+a(\\text{controls})$ modulo $q^b$, or multiplying it by a fixed rational unit, costs $O(V)$.",
 "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",page="controlled-shift",
 frm=["stream-ops","modular-arithmetic","dyadic-and-rational-numbers","primes-divisibility-coprimality-and-gcd"])

n1=infer("S1.3.1","Three stages of forward invocations over triples of a ground set realize the exchange $(X,Y)\\mapsto(-Y,X)$ on two banks and restore every scratch wire to its arbitrary initial value.",
 "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",page="subset-gadget",
 frm=["linear-network","sets-subsets-and-binomial-coefficients","xor-and-mod-2-arithmetic"],
 salient="The scratch wires, which start with arbitrary values, come out unchanged: the side and central contributions cancel for every initial value because the net map $\\mathcal J\\mathcal V+\\mathcal R\\mathcal G$ does not depend on them.")
n2=infer("S1.3.2","If every wire at a gate is stored in the same invertible frame $D_v$ and gates are pointwise linear, the whole network implements $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$ and each edge costs $D_vD_u^{-1}$.",
 "Thus the common frame commutes with the pointwise gate, and",page="frames",
 frm=["linear-network","matrices-and-matrix-vector-products"])
n3=infer("S1.3.3","Nested nondegenerate subspaces of an $m$-dimensional space can be attached to the gates and terminals so that the sum $s$ of edge-difference ranks stays strictly below $Wm$.",
 "Every edge joins comparable nondegenerate labels.  The only decreasing",page="rank-saving",
 frm=["linear-algebra","subset-gadget","frames","sets-subsets-and-binomial-coefficients"],
 salient="The total rank is strictly less than $Wm$, the amount a naive treatment of every wire would need; the deficit $N-2L>0$ comes from the loss $L<N/2$ on the few decreasing central edges.")
n4=infer("S1.3.4","The bit network with rational matrices $M_v$ whose endpoint difference is $I_m$ makes every role undergo the shear $(H,D)\\mapsto(H+D,D)$, with rank sum $s_{\\rm b}<W_{\\rm b}m$.",
 "The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",page="bit-network-shear",
 frm=["rank-saving","frames","controlled-shift","xor-and-mod-2-arithmetic"])
n5=infer("S1.3.5","With binary labels and the phase frames $\\mathcal C_U$, each edge difference is a product of two-point kernels $aI+bX_v$, and telescoping gives $C^{\\otimes m}$ on every role, with rank sum $s_{\\rm c}<W_{\\rm c}m$.",
 "bank exchange, telescoping these phase frames gives $C^{\\otimes m}$",page="complex-phase-network",
 frm=["rank-saving","frames","hamming-weight","euler-s-formula-and-complex-conjugation"],
 salient="The same kernel $C^{\\otimes m}$ appears on every role, including the roles that carried only scratch values, because the endpoint frames are the same full-label and zero-label frames on all of them.")
c13=show("S1.3","A fixed linear network on $W$ wires exchanges two banks with signs and restores every scratch wire, and its gates can be labelled so that the total rank $s$ of the edge changes of representation satisfies $s<Wm$.",
 "build the scalar exchange gadget, let arrays ride on it in gate-wise frames, then choose nested subspace labels and read off the bit and phase interfaces",
 "The tape procedures need a network whose representation changes along edges are cheap; the scalar gadget fixes what is computed, the frames separate what is computed from how it is stored, and the labels make the edge changes few.",
 "explicit",[n1,n2,n3,n4,n5],page="linear-network",
 frm=["linear-algebra","sets-subsets-and-binomial-coefficients","xor-and-mod-2-arithmetic","matrices-and-matrix-vector-products"],
 quote="so that every edge can be implemented by smaller calls to the same")
c1=show("S1","The tape toolkit: elementary stream scans, controlled shifts, and the finite exchange networks with rank saving are available on a fixed number of tapes.",
 "collect the stream operations and the finite networks that both tape procedures use",
 "Both procedures run on the same elementary scans and the same kind of finite network, so these are set up once before either is built.",
 "reconstructed",[c11,c12,c13])

# --- C2 chunk interchange
d1=infer("S2.1","Every rational $m\\times m$ matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with $a$ ones.",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",page="triangular-factorization",
 frm=["matrices-and-matrix-vector-products","linear-algebra"])
d2=infer("S2.2","The shear $(H,D)\\mapsto(H+AD,D)$ for a rank-$a$ rational matrix $A$ is done with exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit",page="matrix-shear",
 frm=["triangular-factorization","controlled-shift"])
d3=infer("S2.3","For chunks of $e=m^k$ digits, running the bit network on $W$ row-split role streams with edges done by smaller interchanges gives $F_k\\le(s/W)F_{k-1}+O(1)$, hence cost $O(Ve^\\tau)$ since $s/W<m^\\tau$.",
 "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",page="power-width-interchange",
 frm=["bit-network-shear","frames","matrix-shear","stream-ops","divide-and-conquer-and-recurrences","rank-saving"],
 salient="The cost per unit volume grows only like $e^\\tau$ with $\\tau<1$, because each level of the recursion multiplies it by $s/W$, which is strictly below the factor $m$ by which the width grows.")
d4=infer("S2.4","Interchanging two disjoint $u$-bit address fields of an arbitrary bit array costs $O(Vu^\\tau)$, after padding and moving a few high digits to supply rows.",
 "in $O(Vu^\\tau)$ steps, where",page=None,
 frm=["power-width-interchange"])
c2=show("S2","Interchanging two disjoint $u$-bit address fields of an array in which all address combinations occur costs $O(Vu^\\tau)$ for a fixed $\\tau<1$.",
 "turn the bit network into a recursion on chunk width whose branching factor is below the width growth, then remove the width and row restrictions",
 "The sum of the edge ranks is less than the number of wires times $m$, so the recursion saves a power of the chunk width.",
 "explicit",[d1,d2,d3,d4],page="chunk-interchange",
 frm=["power-width-interchange","stream-ops"],
 salient="Although the procedure computes XOR combinations of the data, its final effect is an exact permutation for arbitrary auxiliary values, and it beats the naive cost $O(Vu)$ by a power of $u$.",
 adds=[{"symbol":"u","name":"chunk width","meaning":"the number of bits in each of the two address fields being interchanged","relation":"count"},
       {"symbol":"\\tau","name":"interchange exponent","meaning":"a fixed rational exponent strictly between 0 and 1 in the cost $O(Vu^\\tau)$ of an interchange","relation":"direct"}],
 quote="$m$, the resulting recurrence saves a power of the chunk width.")

# --- C3 simultaneous layer
e1a=infer("S3.1.1","Applying the network with column frames to $e=mf$ selected axes needs $s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot, plus binary changes of basis and phase corrections.",
 "$s_{\\rm c}$ child calls, each on the $f=e/m$ axes of one slot.",page=None,
 frm=["complex-phase-network"])
e1b=infer("S3.1.2","The simultaneous butterfly layer equals $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$, so it reduces to $C$ kernels between diagonal phases.",
 "H_0^{\\otimes D}=b^D\\mathcal S_D C^{\\otimes D}\\mathcal S_D.",page=None,
 frm=["butterfly-fft","dft"])
e1=show("S3.1","Since $H_0=b\\mathsf SC\\mathsf S$, a simultaneous layer of $H_0$ on $D$ selected bits reduces to $C^{\\otimes D}$, which the network turns into $s_{\\rm c}$ calls on $D/m$ axes plus binary basis changes.",
 "rewrite $H_0$ as a diagonal phase times $C$ times a diagonal phase, then apply the complex network to $C^{\\otimes e}$",
 "The complex network produces $C^{\\otimes m}$ on every role, not $H_0$; a diagonal phase conjugation connects the two with only exact Gaussian dyadic operations.",
 "recoverable",[e1a,e1b],page="phase-frame-reduction",
 frm=["complex-phase-network","butterfly-fft","dft","ring-mod-yr","euler-s-formula-and-complex-conjugation"])
e2=infer("S3.2","A binary row addition on corresponding selected bits of two address chunks, with a third chunk restored, costs $O(V(L^\\tau+1))$ by eight packed cyclic shifts and deterministic repair of an exponentially small set of exceptional addresses.",
 "$O(V(L^\\tau+1))$, uniformly over the permitted lengths and payloads",page="packed-bit-addition",
 frm=["chunk-interchange","controlled-shift","stream-ops","sorting-merging-and-radix-sort","xor-and-mod-2-arithmetic"],
 salient="Eight cyclic shifts of whole chunks act as the single XOR on every selected bit simultaneously, with the third chunk returning to its arbitrary value.")
e3=infer("S3.3","Batching the complex network over the whole layer on a fixed number of tapes gives a recursion in which $s/W$ calls on role streams of volume $V/W$ cost less than the width growth $m$.",
 "We now turn the finite complex network into an algorithm for a whole",page=None,
 frm=["phase-frame-reduction","packed-bit-addition","divide-and-conquer-and-recurrences"])
e4=infer("S3.4","Intermediate values of a layer stay exact Gaussian dyadics of width $O(p)$ with explicit guard bits, so only one final truncation is needed.",
 "The accelerated network is evaluated exactly until an entire",page=None,
 frm=["fixed-point","two-s-complement-and-signed-integers","dyadic-and-rational-numbers"])
e5=infer("S3.5","The procedure returns $Q_p(\\mathcal Hz)$ with error below $\\sqrt2\\,2^{-p}$ in $O(Vd^{\\lambda'})$ time.",
 "The procedure returns $Q_p(\\mathcal H z)$ in the same array,",page=None,
 frm=["contraction-error"] if False else ["fixed-point"])
c3=show("S3","Applying $H_0$ to the same bit position in $d$ address chunks of polynomial records at once, exactly in Gaussian dyadics with a single final truncation, costs $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
 "reduce the layer to $C$ kernels, implement the basis changes by packed chunk operations, run the network recursively on role streams, and bound the dyadic growth",
 "Separate butterfly factors would need $D$ whole-array passes, so the network's rank saving is used again.",
 "explicit",[e1,e2,e3,e4,e5],page="simultaneous-layer",
 frm=["phase-frame-reduction","packed-bit-addition","chunk-interchange","fixed-point","ring-mod-yr","dyadic-and-rational-numbers"],
 salient="The cost is $O(Vd^{\\lambda'})$ with $\\lambda'<1$, a power saving over the $d$ passes of separate layers, for the same reason as for address interchange: $s_{\\rm c}/W_{\\rm c}<m^{\\sigma}$.",
 adds=[{"symbol":"d","name":"number of axes","meaning":"the number of address chunks whose selected bits take part in one simultaneous layer","relation":"count"},
       {"symbol":"\\lambda'","name":"layer exponent","meaning":"a fixed rational exponent strictly between 0 and 1 in the layer cost $O(Vd^{\\lambda'})$","relation":"direct"}],
 quote="factors would require $D$ whole-array passes.")

# --- C4 ring convolution
f1=infer("S4.1","The forward synthetic transform leaves frequencies in a retained layout, and the opposite transform consumes that layout, at cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.",
 "bound.  The forward procedure may retain its output layout for a",page="transform-layout",
 frm=["simultaneous-layer","chunk-interchange","synthetic-transform","butterfly-fft","multidim-transform","contraction-error","ring-mod-yr"])
f2=infer("S4.2","Polynomials with small signed coefficients are evaluated at a large power of two, multiplied with the established $O(N\\log N)$ integer multiplier, and recovered by centered residues, giving normalized ring products in $O(rp\\log(rp))$.",
 "$O(rp\\log(rp))$ on a fixed number of tapes.",page="signed-packing",
 frm=["ring-mod-yr","fixed-point","history","schoolbook-multiplication-and-carries","binary-representation-of-integers"])
f3=infer("S4.3","Two forward transforms, pointwise ring products and the opposite transform in the same stored order compute $f*g/(rM)$ over $\\mathcal R_r$ with error below $\\sqrt2M(3\\ell+1)2^{-p}$.",
 "Perform both forward transforms and retain their common $LB$ order.",page=None,
 frm=["transform-layout","signed-packing","convolution","contraction-error"])
c4=show("S4","Normalized cyclic convolution over $\\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with the fast layers, using synthetic transforms in a retained frequency order and signed packing for pointwise ring products.",
 "evaluate convolution by the convolution theorem with synthetic transforms, forgetting the order of frequencies between the forward and opposite passes",
 "The pointwise product does not depend on the order of the frequencies, so no sorting is required between transforms.",
 "reconstructed",[f1,f2,f3],page="ring-convolution",
 frm=["transform-layout","signed-packing","convolution","multidim-transform","contraction-error","synthetic-transform"])

# --- C5 retained permutations
g1=infer("S5.1","Gaussian resampling gives $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for coprime $s<t$, with $A,B_0$ contractions computable in time $O(tp^{3/2+\\delta}\\alpha)$.",
 "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",page=None,
 frm=["gaussian-resampling","dft","permutations"])
g2=infer("S5.2","Applied one coordinate line at a time on $d$ axes, the identity becomes $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with movement costs from chunk interchanges.",
 "Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies",page=None,
 frm=["gaussian-resampling","multidim-transform","chunk-interchange"])
g3=infer("S5.3","The chirp absorbs the target permutation, $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$, and the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.",
 "retained source permutation $R$ cancels when computing a convolution.",page=None,
 frm=["bluestein","convolution","dft"],
 salient="The source permutation $R$ appears in each of the three source transforms yet never has to be executed: the three copies cancel exactly, leaving the plain convolution divided by $S^2$.")
c5=show("S5","The two coordinate permutations of Gaussian resampling are kept in the transform formula rather than executed, with the chirp absorbing the target permutation and the source permutation cancelling.",
 "write resampling per axis, then express the middle transform through a chirp convolution, and track both permutations algebraically",
 "Sorting twice per coordinate is exactly the movement cost that the paper wants to avoid.",
 "explicit",[g1,g2,g3],page="retained-permutations",
 frm=["gaussian-resampling","bluestein","dft","multidim-transform","convolution","contraction-error","permutations"],
 quote="We retain both permutations in the transform formula and")

# --- C6 assembly
h1=infer("S6.1","From $n$ choose $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$ and a power of two $T\\in[4n/b,8n/b)$ split into $d$ axes of length $r/2$ or $r$, and distinct primes $s_i$ just below each $t_i$.",
 "Take the power of two $T$ in $[4n/b,8n/b)$, and let",page="parameters",
 frm=["logarithms-floors-and-ceilings","primes-divisibility-coprimality-and-gcd","chunk-interchange","simultaneous-layer","retained-permutations"])
h2=infer("S6.2","Writing both inputs as polynomials in $2^b$ with $b$-bit digits, the product is a convolution of digit lists; padding so the degree is below $S$ avoids wraparound, and coefficients stay below $2^{3b}$.",
 "Thus convolution modulo $x^S-1$ has no nonzero wraparound.",page="integer-as-convolution",
 frm=["polynomials","convolution","schoolbook-multiplication-and-carries","crt-map"])
h3=infer("S6.3","Normalized cyclic convolution on all $d$ power-of-two axes is obtained by twisting the last coordinate into the ring, applying the ring convolution on the other axes, and untwisting.",
 "obtained from the synthetic convolution by a coefficient twist.",page="complex-convolution-twist",
 frm=["phase-twist","ring-convolution","convolution"])
h4=infer("S6.4","The source transform $RF_{\\boldsymbol s}$ is computed by the Gaussian map $\\mathcal A$ on each line, the chirp transform by complex convolution, the Gaussian map $\\mathcal B_0$, and scaling by $2^\\gamma$; the opposite sign comes by complex conjugation.",
 "For a source disk-grid tensor of norm at most $.5$, write",page="source-transform",
 frm=["gaussian-resampling","bluestein","retained-permutations","complex-convolution-twist","fixed-point","euler-s-formula-and-complex-conjugation"])
h5=infer("S6.5","The algorithm forms the radix-$2^b$ digits, applies $\\Phi$, computes two forward source transforms, multiplies pointwise, applies the opposite transform, rescales by $S$ and $2^{2b+4}S$, rounds, inverts $\\Phi$ and propagates carries.",
 "With these streams prepared, perform the following operations.",page=None,
 frm=["source-transform","crt-map","parameters","integer-as-convolution"])
h6=infer("S6.6","After removing the known scales each recovered digit-convolution coefficient has error below $1/2$, so rounding gives the exact integer coefficients and radix-$2^b$ carries give the $2n$-bit product.",
 "The strict error below $1/2$ makes the nearest integer to",page="exact-recovery",
 frm=["integer-as-convolution","contraction-error","schoolbook-multiplication-and-carries","fixed-point"])
c6=show("S6","The multiplication algorithm, with its parameters and exact recovery, multiplies two $n$-bit integers exactly.",
 "reduce to a convolution of digit lists on distinct prime axes, compute it by two forward and one opposite source transform, and recover exact coefficients by rounding",
 "The product is a convolution, and a convolution of long lists is a pointwise product of transforms; rounding is exact because the total error stays under one half.",
 "reconstructed",[h1,h2,h3,h4,h5,h6],page="multiplication-algorithm",
 frm=["source-transform","crt-map","parameters","integer-as-convolution","exact-recovery"])

c7=infer("S7","Dividing costs by $Tp=\\Theta(n)$, the seven dominant terms have powers of $p$ at most $1-2\\kappa$, so every polylogarithmic loss is absorbed and the total is $O(n(\\log n)^{1-\\kappa})$.",
 "Each of the seven displayed powers is at most $1-2\\kappa$ by",page="cost-accounting",
 frm=["parameters","multiplication-algorithm","simultaneous-layer","chunk-interchange","transform-layout","retained-permutations","constant-factors-versus-asymptotic-dominance","big-o"],
 salient="The smallest margin is only $2^{-181}=2\\kappa$, yet every margin is positive, so all seven terms are $O(p^{1-2\\kappa})$ and the exponent $1-\\kappa$ survives.")

root=show("S0","A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "reduce multiplication to a convolution computed by Gaussian-resampling, Bluestein and synthetic transforms, accelerate the address movement and butterfly layers by two network-based tape procedures, and add up the costs",
 "Scanning the array at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so both the movement and the arithmetic of the transforms must be made cheaper.",
 "explicit",[c1,c2,c3,c4,c5,c6,c7],page="main-theorem",
 frm=["history","big-o","multitape-tm"],
 salient="The saving is a power $(\\lg n)^{-\\kappa}$ of the logarithmic factor, not just a smaller constant, with the tiny exponent $\\kappa=2^{-182}$ set by the smallest margin in the cost table.",
 adds=[{"symbol":"V","name":"stored volume","meaning":"the number of data bits stored in an array on tape","relation":"count"}],
 quote="We therefore need savings in both movement and arithmetic.")
json.dump({"root":root},open('../0045-argument.answer.json','w'),indent=1)
print("ok")
