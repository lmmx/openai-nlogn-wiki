import json
P='paper'
def Q(q): return {"source":P,"quote":q}
def inf(id,claim,quote,page=None,frm=(),deferred=False,salient=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":Q(quote),"from":list(frm)}
    if page: n["page"]=page
    if deferred: n["deferred"]=True
    if salient: n["salient"]=salient
    return n
def show(id,claim,method,mot,children,page=None,frm=(),adds=(),salient=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":mot,"children":children,"from":list(frm)}
    if page: n["page"]=page
    if adds: n["adds"]=[dict(symbol=a,name=b,meaning=c,relation=d) for a,b,c,d in adds]
    if salient: n["salient"]=salient
    return n
def mot(text,src,quote=None):
    m={"text":text,"source":src}
    if quote: m["quote"]=Q(quote)
    return m

S1=show("S1","Two fixed finite linear networks, one over $\\mathbb F_2$ and one over $\\mathbb Z[i,1/2]$, exchange two data banks while restoring every scratch wire, and admit frames whose edge changes need $s$ smaller calls in total with $s<Wm$.",
 "build the scalar exchange from three-subset invocations, attach nested subspace labels to its gates, and count the residual dimensions on the edges",
 mot("Turning each edge's change of frame into smaller calls of the same procedure only pays off if the total number of such calls is less than wires times label dimension; keeping the dimension lost on decreasing edges small achieves that.","explicit","The saving will come from keeping the total dimension lost on decreasing"),
 [
  inf("S1.1","A schedule that first subtracts the effect of the old scratch values, then adds the source effect, then undoes the scratch updates, has a net effect independent of the arbitrary initial scratch contents.","This cancellation of arbitrary initial scratch values is a linear",page="scratch-restoration",frm=["linear-network"]),
  inf("S1.2","A forward invocation of the three-subset gather/scatter/side-wire construction adds $x_S$ to $y_S$ and leaves every other value unchanged.","invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",page="subset-construction",frm=["scratch-restoration","binary-field-xor","gaussian-dyadics","subsets-and-binomial-coefficients"]),
  inf("S1.3","Forward, inverse and forward invocations along the three tensor coordinates send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every auxiliary wire.","Performing a forward invocation from $X$ to $Y$ at stage 1,",page="bank-exchange",frm=["subset-construction"]),
  inf("S1.4","Because a common frame commutes with a pointwise linear gate, the network on arrays implements $D_{\\rm out}\\mathsf S_\\Omega D_{\\rm in}^{-1}$ and the intermediate frames cancel.","Thus the common frame commutes with the pointwise gate, and",page="frames",frm=["linear-network","tape-array-layout"]),
  inf("S1.5","Labelling gates and terminals by nested nondegenerate subspaces of an $m$-dimensional bilinear space, the only decreasing edges are the central-wire returns, and the absolute label changes sum to $Wm-2N+2L$.","Every edge joins comparable nondegenerate labels.",page="subspace-labels",frm=["bilinear-forms","tensor-products","frames","bank-exchange"]),
  inf("S1.6","With projection frames on the labels, the XOR bit network applies the shear $H\\gets H+D$ on every role, with total edge rank $s_{\\rm b}<W_{\\rm b}m$.","The bit network has $W_{\\rm b}$ wires, uses only pointwise XOR gates,",page="bit-network-interface",frm=["address-shear","rank-deficit","frames","binary-field-xor"]),
  inf("S1.7","With binary phase frames, the complex network needs $s_{\\rm c}<W_{\\rm c}m$ translation kernels and, after endpoint corrections, applies $C^{\\otimes m}$ on every role.","After source and sink diagonal corrections, and undoing the signed",page="binary-phase-interface",frm=["phase-kernel-c","phase-frames","rank-deficit","bank-exchange"]),
  inf("S1.8","Both relative deficits exceed $20\\cdot2^{-50}$, so $s/W<m^{\\tau}$ with $\\tau=\\sigma=1-2^{-50}$ for both networks.","Both exact deficits displayed above are greater than $20\\cdot2^{-50}$.",page="motif-exponents",frm=["rank-deficit"]),
 ],page="rank-deficit",frm=["linear-network","frames","subspace-labels","bank-exchange","binary-field-xor","gaussian-dyadics"],
 adds=[("W","wire count","The number of wires of the network, including scratch wires.","count"),
       ("m","label dimension","The dimension of the ambient bilinear label space, $h^3=10^6$.","count"),
       ("s","edge rank sum","The total number of smaller calls the edges of the network need.","count")],
 salient="The strict inequality $s<Wm$: the edges need fewer smaller calls than wires times dimension, which is the whole source of the power saving.")

S2=show("S2","Two disjoint $u$-bit address chunks of a tape array of volume $V$ can be interchanged in $O(Vu^{\\tau})$ time with fixed $\\tau<1$.",
 "turn the bit network into a recursive shear: realize each rational edge matrix by triangular factors and smaller interchanges, recurse on role streams of volume $V/W$, then remove the width and row restrictions",
 mot("An edge matrix of rank $a$ costs $a$ smaller interchanges on a $1/W$ share of the volume, and since total rank is below $Wm$ the volume-normalized recurrence saves a power of the width.","explicit","Because the sum of these ranks is less than the number of wires times"),
 [
  inf("S2.1","Every rational matrix of rank $a$ factors as $E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ a partial permutation with $a$ ones.","Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",page="lower-triangular-factorization",frm=["linear-algebra-rank","gaussian-elimination"]),
  inf("S2.2","The shear $(H,D)\\mapsto(H+AD,D)$ by a fixed rational matrix of rank $a$ costs exactly $a$ interchanges of smaller field pairs plus $O(V)$ work.","can be performed with exactly $a$ interchanges of pairs of $b$-digit",page="matrix-shear-cost",frm=["lower-triangular-factorization","controlled-shifts","address-shear","modular-arithmetic"]),
  inf("S2.3","For chunks of $e=m^k$ digits with enough rows, the bit network with recursive shears interchanges the chunks in $O(Ve^{\\tau})$ time on fixed tapes.","The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every",page="power-width-interchange",frm=["bit-network-interface","matrix-shear-cost","volume-normalized-recurrence","elementary-stream-ops","motif-exponents","depth-first-traversal"]),
  inf("S2.4","Padding to a power width and supplying rows from a few high digits extends the bound to arbitrary widths $u$.","Rows for a general array can be supplied by a few of its own high digits.",frm=["power-width-interchange"]),
 ],page="chunk-interchange",frm=["power-width-interchange","tape-array-layout"],
 adds=[("u","chunk width","The number of address bits in each interchanged chunk.","count"),
       ("V","stored volume","The number of data bits stored in the array.","count")],
 salient="Although the result is a pure permutation, it costs sublinearly in the width $u$ per bit, less than any digit-by-digit movement, because it computes XOR combinations of data.")

S3=show("S3","The normalized butterfly $H_0$ can be applied on the same bit position of up to $d$ address chunks at once, exactly in Gaussian dyadics followed by one truncation, in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$.",
 "write $H_0^{\\otimes D}$ through layers of the kernel $C$, realize $C^{\\otimes e}$ by the complex network with phase frames, implement basis changes by packed selected-bit additions, recurse on role streams, and bound coefficient growth",
 mot("Applying the $d$ butterflies separately costs $d$ whole-array passes; expressing the layer through the complex network lets each recursive call act on fewer selected axes on a $1/W$ share of the volume, and $s_{\\rm c}<W_{\\rm c}m$ makes the recurrence sublinear in $d$.","recoverable"),
 [
  inf("S3.1","The Gaussian dyadic kernel $C=aI+bX$ satisfies $H_0=b\\mathsf SC\\mathsf S$, so a layer of $C$ converts into a normalized butterfly layer.","H_0=b\\mathsf SC\\mathsf S",page="phase-kernel-c",frm=["butterfly-h0","gaussian-dyadics","tensor-products"]),
  inf("S3.2","Between nested binary labels the phase frame changes by one translation kernel $aI+bX_v$ per orthonormal residual vector, implementable in coordinate slots after a binary change of basis.","The number of directional kernels is precisely",page="phase-frames",frm=["phase-kernel-c","frames","subspace-labels","binary-field-xor","gaussian-elimination"]),
  inf("S3.2b","XORing selected bit $x$ into bit $y$ at regularly spaced positions of two chunks is done by cyclic shifts with a guard chunk plus deterministic repair of an explicitly bounded exceptional set.","We implement a binary row addition on corresponding selected bits in two",page="packed-selected-bit-addition",frm=["controlled-shifts","chunk-interchange","binary-field-xor","elementary-stream-ops"]),
  inf("S3.3","Applying $C$ on $e=mf$ selected axes splits rows among the $W$ roles, so each of the $s$ recursive calls acts on $f$ axes and volume $V/W$.","one role stream with volume exactly \\(1/W\\) of its parent's logical",page="layer-recursion",frm=["binary-phase-interface","packed-selected-bit-addition","volume-normalized-recurrence","motif-exponents"]),
  inf("S3.4","Denominator and magnitude growth inside one layer is bounded so a coefficient width of $O(p)$ bits represents every intermediate value exactly.","component represents every intermediate coefficient exactly and",page="guard-width",frm=["gaussian-dyadics","layer-recursion"]),
 ],page="simultaneous-butterfly-layer",frm=["layer-recursion","guard-width","fixed-point-grid","butterfly-h0"],
 adds=[("d","chunk count bound","The maximum number of address chunks whose selected bits are transformed together.","count"),
       ("p","precision","The number of fractional bits of the fixed-point grid.","count")],
 salient="All $d$ butterflies together cost $O(Vd^{\\lambda'})$, strictly less than the $d$ passes of applying them one at a time.")

S4=show("S4","The normalized cyclic convolution of arrays over $\\mathbb C[y]/(y^r+1)$ can be approximated with small error by two forward synthetic transforms, pointwise packed products, and the opposite transform.",
 "evaluate Nussbaumer's synthetic transforms with simultaneous butterfly layers on a suitable layout, multiply records by signed packing, and apply the opposite transform in the retained frequency order",
 mot("In the polynomial ring the roots of unity are powers of $y$, acting by signed shifts, so the transforms reduce to address moves and butterflies, which the two tape procedures accelerate.","explicit","where the required roots of unity act by exact signed permutations"),
 [
  inf("S4.1","With $\\omega_t=y^{2r/t}$ the normalized synthetic transforms are contractions satisfying $F_t^+F_t^-=t^{-1}I$.","For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.",page="synthetic-transforms",frm=["negacyclic-ring","dft","butterfly-h0"]),
  inf("S4.2","A layout placing selected bits at a common offset in consecutive $K$-bit chunks lets each transform round use one simultaneous layer, and the forward frequency order is retained for the opposite transform.","we must place the selected bits of the participating axes at a common",page="transform-layout",frm=["synthetic-transforms","simultaneous-butterfly-layer","chunk-interchange"]),
  inf("S4.3","Signed Kronecker packing lets the $O(n\\log n)$ multiplier compute exact products of records in $\\mathbb C[y]/(y^r+1)$ in $O(rp\\log(rp))$ time.","One can compute the exact Gaussian integer",page="signed-packing",frm=["negacyclic-ring","hvdh-multiplier","fixed-point-grid"]),
  inf("S4.4","Performing both forward transforms in the common retained order, multiplying pointwise, and applying the opposite transform gives the normalized convolution.","Perform both forward transforms and retain their common $LB$ order.",frm=["cyclic-convolution","multidimensional-dft","transform-layout","signed-packing"]),
 ],page="synthetic-convolution",frm=["transform-layout","signed-packing","cyclic-convolution","multidimensional-dft"])

S5=show("S5","Fourier transforms on the coprime source lengths can be expressed through power-of-two tensor transforms and convolutions, with the source and target permutations kept in the formula and cancelled rather than executed.",
 "adapt Gaussian resampling with permutations retained, take tensor products line by line, convert the middle transform by a chirp, and cancel the source permutation across the convolution",
 mot("The transform lengths are pairwise coprime while the fast synthetic transforms need powers of two; resampling bridges them, and keeping its two permutations in the formula avoids two full sorts per coordinate.","explicit","The transform lengths needed for the integer product are pairwise coprime,"),
 [
  inf("S5.1","For coprime $s<t$ there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$.","There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and",page="gaussian-resampling",frm=["dft","fixed-point-grid","hvdh-multiplier"]),
  inf("S5.2","Tensoring the one-dimensional identities gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, applied one coordinate line at a time with chunk interchanges moving axis fields.","For the tensor product, apply the one-dimensional maps to one coordinate",frm=["gaussian-resampling","multidimensional-dft","chunk-interchange"]),
  inf("S5.3","The middle factor $QF_{\\boldsymbol t}$, including its target permutation, equals chirp multiplication, cyclic convolution with the chirp, and chirp multiplication.","The chirp identity below performs the frequency change",page="bluestein-chirp",frm=["dft","cyclic-convolution"]),
  inf("S5.4","The retained source permutation $R$ cancels: $(RF_{\\boldsymbol s}^+)[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$.","retained source permutation $R$ cancels when computing a convolution.",page="permutation-cancellation",frm=["tensor-resampling","cyclic-convolution"]),
 ],page="tensor-resampling",frm=["gaussian-resampling","multidimensional-dft","chunk-interchange"])

S6=show("S6","An explicit fixed-tape algorithm computes approximations to the radix-$2^b$ digit convolution of the inputs through the CRT map, two forward resampled source transforms, a pointwise product and the inverse transform.",
 "fix the rational parameters, map digits to prime axes by the CRT, convert the power-of-two convolution to the polynomial ring by a twist, build the source-transform procedures, and run them on the digit arrays",
 mot("Multiplication is a digit convolution, and convolution becomes pointwise multiplication after Fourier transforms; every transform needed is supplied by the preceding procedures once the parameters fit together.","recoverable"),
 [
  inf("S6.1","The fixed rational constants $\\tau=\\sigma=1-2^{-50}$, $\\lambda'=1-2^{-54}$, $c=2^{-56}$, $\\epsilon=2^{-75}$, $\\kappa=2^{-182}$ satisfy all layer and cost conditions.","These constants are deliberately conservative; no optimization is claimed.",page="parameter-choice",frm=["motif-exponents","simultaneous-butterfly-layer"]),
  inf("S6.2","The Agarwal--Cooley map turns a cyclic convolution of length $S=\\prod s_i$ into a multidimensional cyclic convolution on coprime axes, implemented by triangular controlled shifts.","theorem to convert one cyclic convolution into multidimensional cyclic",page="crt-map",frm=["cyclic-convolution","chinese-remainder-theorem","modular-inverses-and-units","controlled-shifts","chunk-interchange"]),
  inf("S6.3","The twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$ turns the last cyclic coordinate into $\\mathbb C[y]/(y^r+1)$ while preserving convolution.","Untwisting therefore recovers the cyclic coefficient with the correct",page="coefficient-twist",frm=["negacyclic-ring","cyclic-convolution","euler-s-formula-and-complex-roots-of-unity"]),
  inf("S6.4","The middle factor is evaluated by chirps and the twisted synthetic convolution, then composed with the Gaussian maps to give the source-transform procedures.","We next use the complex convolution to evaluate the middle factor",frm=["bluestein-chirp","coefficient-twist","synthetic-convolution","tensor-resampling"]),
  inf("S6.5","Splitting into digits, mapping by $\\Phi$, two forward source transforms, a pointwise product, the inverse transform, rescaling, rounding and carries form the algorithm.","The source-transform procedures now supply the three transforms needed",frm=["multiplication-as-convolution","crt-map","permutation-cancellation"]),
 ],page="multiplication-algorithm",frm=["multiplication-as-convolution","crt-map","coefficient-twist","synthetic-convolution","permutation-cancellation","parameter-choice"])

root=show("S0","One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ worst-case time with $\\kappa=2^{-182}$, disproving the $n\\log n$ optimality conjecture in that model.",
 "build two fast tape procedures (address interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, assemble them into the transform-based convolution algorithm, prove exact recovery and bound the total time",
 mot("Scanning $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so beating $n\\log n$ requires savings in both data movement and arithmetic.","explicit","We therefore need savings in both movement and arithmetic."),
 [S1,S2,S3,S4,S5,S6,
  inf("S7","Every call stays in the unit disk and the recovered coefficients have error below $1/2$, so rounding gives the exact integer convolution.","The strict error below $1/2$ makes the nearest integer to",page="exact-recovery",frm=["multiplication-algorithm","fixed-point-grid"]),
  inf("S8","Every dominant normalized cost is a power of $p$ at most $1-2\\kappa$, so the total time is $O(n(\\log n)^{1-\\kappa})$.","Each of the seven displayed powers is at most $1-2\\kappa$ by",page="time-bound",frm=["multiplication-algorithm","parameter-choice","exact-recovery","chunk-interchange","simultaneous-butterfly-layer"]),
  inf("S9","The bound gives $T_A(n)/(n\\lg n)\\to0$, refuting an eventual $\\Omega(n\\lg n)$ lower bound for every fixed machine.","The power saving proved here gives a limit of zero through all input lengths,",frm=["nlogn-conjecture","time-bound","big-omega-and-big-theta-notation"],deferred=True),
 ],page="main-theorem",frm=["time-bound","exact-recovery","nlogn-conjecture","turing-machines"],
 adds=[("\\kappa","saving exponent","The fixed exponent $2^{-182}$ by which the logarithmic factor is reduced.","direct")],
 salient="The saving $\\kappa=2^{-182}$ is minuscule yet a strict power of $\\lg n$, contradicting a conjecture that held since 1971.")
json.dump({"root":root},open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N2/exegenius/tasks/0003-argument.answer.json','w'),indent=1,ensure_ascii=False)
