import json
P='paper'
def ev(q): return {"source":P,"quote":q}
def inf(id,claim,quote,page=None,frm=(),salient=None,deferred=None):
    n={"id":id,"intention":"infer","claim":claim,"quote":ev(quote),"page":page,"from":list(frm)}
    if salient: n["salient"]=salient
    if deferred: n["deferred"]=True
    return n
def show(id,claim,method,mot,children,page=None,frm=(),salient=None,adds=None):
    n={"id":id,"intention":"show","claim":claim,"method":method,"motivation":mot,"children":children,"page":page,"from":list(frm)}
    if salient: n["salient"]=salient
    if adds: n["adds"]=adds
    return n
def expl(text,q): return {"text":text,"source":"explicit","quote":ev(q)}
def rec(text): return {"text":text,"source":"recoverable","quote":None}
def rcn(text): return {"text":text,"source":"reconstructed","quote":None}

S1=show("S1","The elementary scans a fixed-tape machine needs (splitting, merging, digit moves, controlled shifts) all cost time linear in the logical volume $V$.",
 "state the two linear-time toolkits the later procedures call: elementary stream operations and controlled shifts",
 rec("Every later procedure is built from a fixed number of such scans, so they must not add more than $O(V)$ or the power saving would be lost."),
 [inf("S1.1","Splitting, merging and fixed permutations of radix-$q$ digits of an array of volume $V$ take $O(V)$ steps on a fixed number of tapes.",
      "volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:","streams",
      ["fixed-tape-model","tape-basics","lexicographic-order-and-mixed-radix-indices","division-with-remainder"]),
  inf("S1.2","Updating a later address field by an offset computed from earlier fields, or multiplying it by a fixed unit modulo $q^b$, costs $O(V)$.",
      "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the","controlled-shifts",
      ["streams","modular-arithmetic","primes-divisibility-and-coprimality","two-s-complement-and-truncation","binary-representation-and-integer-arithmetic"])],
 frm=["fixed-tape-model","tape-basics"])

S2=show("S2","A fixed linear network exchanging two banks of values and restoring all scratch wires, with nested subspace labels on its gates and terminals, makes the total rank $s$ of edge changes strictly smaller than $Wm$.",
 "build the scalar exchange network, make the stored arrays carry frames that commute with its pointwise gates, and choose labels from triple indicator vectors so the dimension changes can be counted",
 expl("The whole saving rests on the rank count $s<Wm$, so the network and its labels are constructed to make exactly that count.","number $s$ of smaller calls satisfies $s<Wm$."),
 [inf("S2.1","For arbitrary initial scratch values, three forward stages send $(X,Y)$ to $(-Y,X)$ and restore every scratch wire.",
      "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value","scalar-exchange-network",
      ["three-subset-pairing","xor-and-arithmetic-over-f₂","matrices-and-linear-maps","sets-functions-and-permutations"],
      salient="The exchange works for every initial value of the scratch wires, which are returned unchanged: the unwanted central and side coefficients cancel exactly, whatever the scratch contents."),
  inf("S2.2","If stored arrays are $D_v$ applied to logical arrays, pointwise linear gates commute with the common frame, so the network implements $D_{\\rm out}\\mathsf S D_{\\rm in}^{-1}$ and only the edge changes $D_vD_u^{-1}$ must be paid for.",
      "Thus the common frame commutes with the pointwise gate, and","frames",
      ["scalar-exchange-network","matrices-and-linear-maps","sets-functions-and-permutations"]),
  inf("S2.3","Indicator vectors of three-element subsets of a 100-element set have pairings $|S\\cap T|-1$ over $\\mathbb Q$ or $|S\\cap T|\\bmod 2$ over $\\mathbb F_2$, so neighboring triples are orthogonal and every triple line is nondegenerate.",
      "Thus every triple line is nondegenerate, and neighboring triple lines","three-subset-pairing",
      ["linear-algebra","matrices-and-linear-maps","xor-and-arithmetic-over-f₂","sets-functions-and-permutations"]),
  inf("S2.4","Nested nondegenerate subspace labels give every edge a residual, and the only decreasing edges are the central-wire edges, so the total rank $s$ of edge changes satisfies $s<Wm$ for $W$ wires and an $m$-dimensional label space.",
      "Label dimension is nondecreasing along every edge except center $3\\to4$, which removes","subspace-labels",
      ["linear-algebra","three-subset-pairing","scalar-exchange-network","frames"],
      salient="The saving is strict but tiny: the relative deficit $(Wm-s)/(Wm)$ is only about $10^{-11}$ to $10^{-13}$, yet this strict inequality is all the recursion needs. The labels at neighboring gates are nested because neighboring triples are orthogonal, and the only dimension lost is on the central wires."),
  inf("S2.5","The bit network on $W$ wires sends every input role to its partner with endpoint matrices differing by $I_m$, and its rank sum $s=Wm-N+2L$ is below $Wm$, giving the address shear $H\\leftarrow H+D$.",
      "Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.","bit-network",
      ["subspace-labels","frames","scalar-exchange-network","linear-algebra","modular-arithmetic"])],
 frm=["linear-algebra","matrices-and-linear-maps"],
 adds=[{"symbol":"W","name":"wire count","meaning":"the number of wires (roles) of the fixed network","relation":"count"},
       {"symbol":"m","name":"label dimension","meaning":"the dimension of the space whose subspaces label the gates and terminals","relation":"direct"},
       {"symbol":"s","name":"total edge rank","meaning":"the sum over edges of the rank of the change of frame, equal to the number of smaller calls","relation":"count"}])

S3=show("S3","Two disjoint contiguous $u$-bit address fields of an array of volume $V$ can be interchanged in $O(Vu^\\tau)$ time for a fixed $\\tau<1$.",
 "run the bit network on row streams, paying each edge by address shears whose cost is the matrix rank in smaller interchanges, and solve the resulting recurrence",
 expl("Each edge costs one smaller interchange per unit of rank, and the ranks sum to less than $W$ times $m$, so the cost recurrence has a ratio below $m$ per level of width.","Because the sum of these ranks is less than the number of wires times"),
 [inf("S3.1","Every rational matrix $A$ of rank $a$ equals $E_1\\Pi E_2$ with $E_1,E_2$ lower triangular and $\\Pi$ a partial permutation with $a$ ones.",
      "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization","lower-triangular-factorization",
      ["linear-algebra","matrices-and-linear-maps"]),
  inf("S3.2","The shear $(H,D)\\mapsto(H+AD,D)$ modulo $q^b$ is done with exactly $\\operatorname{rank}(A)$ interchanges of $b$-digit fields plus $O(V)$ further work.",
      "can be performed with exactly $a$ interchanges of pairs of $b$-digit","address-shear",
      ["lower-triangular-factorization","controlled-shifts","streams","modular-arithmetic","bit-network"],
      salient="The shear costs exactly rank-many interchanges, not $m$ of them: the triangular factors are free (controlled shifts), so only the $a$ ones of the partial permutation need a recursive interchange."),
  inf("S3.3","Because the network makes $s<Wm$ calls on streams of volume $V/W$, the per-volume cost satisfies $F_k\\le(s/W)F_{k-1}+O(1)$, so the cost at width $e=m^k$ is $O(Ve^\\tau)$.",
      "F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).","power-saving-recursion",
      ["subspace-labels","frames","recurrences-and-divide-and-conquer","asymptotic-notation-beyond-big-o","streams"],
      salient="A strict inequality $s/W<m^\\tau$ with $\\tau<1$ turns a recursion with $s$ children on $1/W$ of the volume into a polynomial saving $e^\\tau$ over the width $e=m^k$ instead of the full factor $e$."),
  inf("S3.4","Removing the power-width and row restrictions by padding and splitting off high digits gives the interchange of two arbitrary $u$-bit chunks in $O(Vu^\\tau)$ steps.",
      "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",None,
      ["streams","controlled-shifts","power-saving-recursion","address-shear"])],
 page="chunk-interchange",
 frm=["bit-network","streams","controlled-shifts"],
 salient="Although the final effect is an exact permutation, the intermediate steps form XOR combinations of data, and the cost $O(Vu^\\tau)$ with $\\tau=1-2^{-50}$ beats the $O(Vu)$ of moving one digit at a time.")

S4=show("S4","A normalized butterfly $H_0$ applied to the same bit position of $D\\le d$ address chunks of a polynomial array is computed at once in $O(Vd^{\\lambda'})$ time, with a single truncation at the end.",
 "express the tensor power of the two-point kernel through the complex phase network and bit-network recursion on $e=mf$ axes, using exact dyadic arithmetic throughout",
 expl("Doing the $D$ butterfly factors separately costs $D$ passes over the data, so the factors are bundled into one recursion whose children are fewer and smaller.","factors would require $D$ whole-array passes."),
 [inf("S4.1","The complex network with binary labels has frame differences that are products of translation kernels $aI+bX_v$ and gives $C\\otimes\\dots\\otimes C$ on every role, where $H_0=b\\,\\mathsf S C\\mathsf S$.",
      "H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad","phase-frames",
      ["subspace-labels","frames","scalar-exchange-network","three-subset-pairing","linear-algebra","butterfly","complex-numbers","xor-and-arithmetic-over-f₂"],
      salient="The same tensor power $C^{\\otimes m}$ appears on every role, including roles carrying only scratch values, because the frames telescope along the network."),
  inf("S4.2","Adding corresponding selected bits of address chunks is done by a constant number of cyclic shifts of whole chunks, followed by repair of an explicitly bounded exceptional set of addresses.",
      "record payload; in particular, it restores the entire chunk $z$ for","packed-selected-bits",
      ["chunk-interchange","controlled-shifts","streams","xor-and-arithmetic-over-f₂","two-s-complement-and-truncation"]),
  inf("S4.3","Each node of the recursion on $e=mf$ axes makes exactly $s$ child calls on $f$ axes, each on $1/W$ of the volume, and the other work per node is $O(V((eK)^\\tau+1))$, giving cost $O(Vd^{\\lambda'})$.",
      "The phase construction supplies one recursive call on a slot for each",None,
      ["power-saving-recursion","phase-frames","packed-selected-bits","chunk-interchange"]),
  inf("S4.4","Intermediate values of the whole layer are Gaussian dyadics whose size is bounded by $O(d^{C_1})$ guard bits, so the layer is evaluated exactly and truncated once.",
      "The accelerated network is evaluated exactly until an entire","dyadic-exact",
      ["fixed-point","two-s-complement-and-truncation","binary-representation-and-integer-arithmetic","complex-numbers"]),
  inf("S4.5","For fixed rational exponents the layer returns $Q_p(\\mathcal H z)$ with error below $\\sqrt2\\,2^{-p}$ in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$.",
      "The procedure returns $Q_p(\\mathcal H z)$ in the same array,",None,
      ["fixed-point","dyadic-exact","phase-frames","packed-selected-bits","power-saving-recursion"])],
 page="simultaneous-layer",
 frm=["fixed-point","butterfly","chunk-interchange","power-saving-recursion"],
 salient="The cost $O(Vd^{\\lambda'})$ with $\\lambda'<1$ is a power of $d$ below the $D\\le d$ passes of separate layers, because a strict rank deficit $s<Wm$ also holds for the complex network.")

S5=show("S5","A forward synthetic transform over $\\mathbb C[y]/(y^r+1)$, laid out so each radix-two round is one simultaneous layer, costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ and leaves its output in bit-reversed order.",
 "write the transform as rounds of butterflies and signed-shift twiddles, then place the selected bits of the participating axes at a common offset so each round is a simultaneous layer",
 expl("The fast layer applies only to bits at a common offset in consecutive $K$-bit chunks, so the layout has to put each round's bits there, and its movement cost is charged.","we must place the selected bits of the participating axes at a common"),
 [inf("S5.1","Over $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$ the roots of unity $\\omega_t=y^{2r/t}$ are signed shifts, and the transform is computed by decimation-in-frequency rounds of $H_0$ butterflies.",
      "decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for","synthetic-transform",
      ["ring-mod-yr-plus-1","dft","butterfly","fast-fourier-transform-as-an-algorithm","complex-numbers","polynomials"],
      salient="Every twiddle multiplication is only a signed cyclic shift of a coefficient list, because $y^r=-1$ makes powers of $y$ roots of unity of every power-of-two order dividing $2r$."),
  inf("S5.2","The forward transform writes entry $j$ at slot $\\operatorname{rev}_a(j)$; the pointwise product and the opposite transform use this same order, so no reordering is executed.",
      "entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.","stored-order",
      ["synthetic-transform","butterfly"],
      salient="The bit-reversal permutation is never applied: it comes out of the recursion for free, and the opposite transform consumes the same order."),
  inf("S5.3","With the selected bits placed at a common offset, each of the $\\ell$ rounds uses the simultaneous layer, and layout construction and restoration are charged in the stated cost.",
      "Both layout construction and final restoration are charged in this",None,
      ["simultaneous-layer","chunk-interchange","stored-order","synthetic-transform"])],
 page="transform-layout",
 frm=["simultaneous-layer","chunk-interchange","fixed-point","synthetic-transform","stored-order"])

S6=show("S6","Two forward synthetic transforms, a pointwise ring product by signed packing and the opposite transform give the normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathbb C[y]/(y^r+1)$ with error about $3\\ell M2^{-p}$.",
 "apply the convolution theorem in the ring, keeping the retained frequency order between the three transforms",
 expl("Pointwise multiplication commutes with a common permutation of the records, so the forward outputs can be multiplied in their stored order and passed straight to the opposite transform.","Pointwise multiplication commutes with applying the same record"),
 [inf("S6.1","Evaluating polynomials at $2^{4p}$ (signed Kronecker substitution) turns one ring product into four integer products by the established multiplier, and centered coefficients are read back.",
      "numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time","signed-packing",
      ["ring-mod-yr-plus-1","hvdh-multiplier","fixed-point","polynomials","two-s-complement-and-truncation"]),
  inf("S6.2","Perform both forward transforms, multiply pointwise, apply the opposite transform and rescale by $M$; the normalization $F^+F^-=I/M$ gives $\\mathcal M_r$ and the error stays below $\\sqrt2 M(3\\ell+1)2^{-p}$.",
      "Perform both forward transforms and retain their common $LB$ order.",None,
      ["transform-layout","stored-order","dft","convolution","inequalities-for-error-bounds"])],
 page="synthetic-convolution",
 frm=["transform-layout","stored-order","signed-packing","convolution","hvdh-multiplier"])

S7=show("S7","The Gaussian-resampling identity, the Bluestein chirp and the cancellation of the source permutation express a convolution on prime axes through the power-of-two synthetic convolution without executing the coordinate permutations.",
 "keep the two coordinate permutations of Gaussian resampling inside the transform formula, absorb the target one in the chirp and cancel the source one across the pointwise product",
 expl("The usual implementation sorts twice on each coordinate, which is exactly the data movement the paper is trying to avoid, so both permutations are retained in the formula.","coordinate. We retain both permutations in the transform formula and"),
 [inf("S7.1","For coprime $s<t$ with $t/s-1$ large enough there are contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable in time $O(tp^{3/2+\\delta}\\alpha)$.",
      "P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.","gaussian-resampling",
      ["dft","complex-numbers","primes-divisibility-and-coprimality","inequalities-for-error-bounds"]),
  inf("S7.2","The identity extends to $d$ coordinates by tensor products, $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$, with linewise errors below $dp^2$.",
      "Both $\\mathcal A$ and $\\mathcal B_0$ are contractions.",None,
      ["gaussian-resampling","dft"]),
  inf("S7.3","Bluestein's chirp identity writes the middle transform $QF_{\\boldsymbol t}$, with its target permutation, as a phase multiplication, a cyclic convolution with the chirp array $a$, and another phase multiplication.",
      "Then $a$ has period $t_i$ in coordinate $i$, and","bluestein-chirp",
      ["dft","convolution","complex-numbers","gaussian-resampling"]),
  inf("S7.4","Because $F^+_{\\boldsymbol s}R=R^{-1}F^+_{\\boldsymbol s}$, the source permutation $R$ cancels across two forward transforms, a pointwise product and the opposite transform, leaving $(u*v)/S^2$.",
      "proving \\eqref{eq:source-permutation-cancel}. Finally, conjugation",None,
      ["dft","convolution","modular-arithmetic","primes-divisibility-and-coprimality"],
      salient="The permutation never has to be undone: the same $R$ appears at both ends because every $t_i$ is a unit modulo $s_i$.")],
 page="retained-permutations",
 frm=["gaussian-resampling","bluestein-chirp","stored-order","dft","convolution"])

SP=show("D1","Sizes and prime source lengths can be chosen so that $Tp=\\Theta(n)$, the ring degree $r$ outgrows every power of $p$, and every hypothesis of the resampling and layer lemmas holds.",
 "fix the sizes from $n$, then find distinct odd primes just below each power of two by a deterministic search",
 expl("The product of the prime lengths must fill a fixed fraction of the padded box while each ratio $t_i/s_i$ leaves enough separation for resampling.","The distinct prime lengths $s_i$ must be close to the powers of two"),
 [inf("D1.1","Take $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, a power of two $T\\in[4n/b,8n/b)$ and ring degree $r=2^\\ell$ with $d$ axis lengths $t_i\\in\\{r/2,r\\}$, so $Tp=\\Theta(n)$ and $r=2^{\\Theta(p^{1-\\epsilon})}$.",
      "Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),",None,
      ["logarithms-floors-and-ceilings","asymptotic-notation-beyond-big-o","binary-representation-and-integer-arithmetic"]),
  inf("D1.2","Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist and are found in $n^{o(1)}$ time, giving $T/2<S<T$ for $S=\\prod_is_i$ and $\\gcd(s_i,t_i)=1$.",
      "We may therefore choose distinct odd primes satisfying",None,
      ["primes-divisibility-and-coprimality","inequalities-for-error-bounds"])],
 page="size-parameters",
 frm=["logarithms-floors-and-ceilings","primes-divisibility-and-coprimality"],
 adds=[{"symbol":"b","name":"digit width","meaning":"the number of bits per radix digit, $\\lceil\\log_2 n\\rceil$","relation":"direct"},
       {"symbol":"p","name":"working precision","meaning":"the number of fractional bits of the fixed-point grid, $6b$","relation":"direct"},
       {"symbol":"d","name":"axis count","meaning":"the number of power-of-two axes of the transform array","relation":"count"},
       {"symbol":"T","name":"padded length","meaning":"the power-of-two number of entries of the padded box","relation":"direct"},
       {"symbol":"r","name":"ring degree","meaning":"the power-of-two degree of the polynomial ring modulo $y^r+1$","relation":"direct"}])

ER=show("D2.6","Undoing the known scales shows every recovered coefficient has error below $1/2$, so rounding and radix-$2^b$ carry propagation give the exact $2n$-bit product.",
 "bound the accumulated numerical error against the integrality of the coefficients, then recover the digits",
 rec("The true coefficients are integers, so once the computed value is within $1/2$ of it, rounding is exact; the carries then only convert the coefficients into binary digits."),
 [inf("D2.6.1","The accumulated error of all transforms, scales $S$ and $2^{2b+4}$ is below $448b\\,2^{-b+\\gamma}\\le448b\\,2^{-3b/4}<1/2$.",
      "448b\\,2^{-b+\\gamma}",None,["inequalities-for-error-bounds","fixed-point"]),
  inf("D2.6.2","The strict error bound makes the nearest integer to each computed coefficient the unique correct one, and it lies in $[0,2^{3b})$.",
      "The strict error below $1/2$ makes the nearest integer to",None,["inequalities-for-error-bounds","digit-convolution","two-s-complement-and-truncation"]),
  inf("D2.6.3","Carries $k_{j+1}=\\lfloor(c_j+k_j)/2^b\\rfloor$ stay below $2^{2b}$, and propagating them in increasing order yields the radix digits of the product.",
      "To propagate carries, let $Q_0=2^b$.",None,["division-with-remainder","binary-representation-and-integer-arithmetic","digit-convolution"])],
 page="exact-recovery",
 frm=["digit-convolution","inequalities-for-error-bounds","fixed-point","division-with-remainder"])

MA=show("D2","The assembled algorithm places the radix digits on prime axes by the Chinese-remainder map, applies two source transforms, a pointwise product and one opposite transform, then rescales, rounds and carries to give the exact product.",
 "reduce the integer product to a convolution, move it step by step to the ring convolution of the earlier sections, and recover the integer by rounding",
 rec("Each reduction in the flow from digit convolution to prime axes to power-of-two axes to the ring changes only the problem's representation, so the faster transforms can be used at the end and the answer pulled back."),
 [inf("D2.1","Writing both inputs in radix $2^b$ with $q=\\lceil n/b\\rceil$ digits, the product coefficients are a convolution modulo $x^S-1$ with capacity below $2^{3b}$ and no wraparound.",
      "Thus convolution modulo $x^S-1$ has no nonzero wraparound.","digit-convolution",
      ["convolution","polynomials","binary-representation-and-integer-arithmetic"]),
  inf("D2.2","The map $x\\mapsto\\prod_ix_i^{\\mu_i}$ is an isomorphism from cyclic convolution of length $S$ onto convolution on a product of prime cyclic axes, realized by triangular controlled shifts.",
      "$\\Phi$ is an isomorphism and preserves cyclic convolution.","crt-cyclic-axes",
      ["convolution","controlled-shifts","chunk-interchange","primes-divisibility-and-coprimality","modular-arithmetic","lexicographic-order-and-mixed-radix-indices"]),
  inf("D2.3","Multiplying coefficient $k$ by $\\zeta^k$ with $\\zeta=e^{\\pi i/r}$ maps $\\mathbb C[x]/(x^r-1)$ isomorphically onto $\\mathbb C[y]/(y^r+1)$, so negative wrap becomes cyclic wrap.",
      "multiplying coefficient $k$ by the nonzero number $\\zeta^k$.","phase-twist",
      ["ring-mod-yr-plus-1","convolution","complex-numbers"]),
  inf("D2.4","The source transform applies the Gaussian maps linewise, the chirp transform via complex convolution by twist, and a final exact scale $2^\\gamma$, with exact counterpart $RF_{\\boldsymbol s}$.",
      "For a source disk-grid tensor of norm at most $.5$, write",None,
      ["retained-permutations","synthetic-convolution","phase-twist","bluestein-chirp","gaussian-resampling"]),
  inf("D2.5","Place the digits by $\\Phi$, transform both operands, multiply pointwise, apply the opposite transform, and rescale by $S$ and $2^{2b+4}$ to obtain the integer coefficient convolution.",
      "The source-transform procedures now supply the three transforms needed",None,
      ["crt-cyclic-axes","retained-permutations","synthetic-convolution","digit-convolution"]),
  ER],
 page="multiplication-algorithm",
 frm=["size-parameters","retained-permutations","synthetic-convolution","crt-cyclic-axes","phase-twist","digit-convolution","exact-recovery"])

CA=show("D3","Dividing each cost term by $Tp$ gives powers of $p$ with margins below one, the smallest being $2\\kappa$ with $\\kappa=2^{-182}$, so the total time is $O(n(\\lg n)^{1-\\kappa})$.",
 "tabulate the normalized cost of each phase and compare each power of $p$ with $1-2\\kappa$",
 expl("The slack $2\\kappa$ is chosen so that any remaining fixed power of $\\log p$ is absorbed.","any remaining fixed power of $\\log p$."),
 [inf("D3.1","Normalized by $V=Tp$, the cost terms are $dK$, $pK^{\\tau-1}$, $\\ell d^{\\lambda'}$, $d^2(1+\\ell^\\tau)$, $dp^{1/2+\\delta}\\alpha$, $dp^\\delta$ and $\\log(rp)$.",
      "Table~\\ref{tab:costs} lists costs after division",None,
      ["transform-layout","synthetic-convolution","retained-permutations","hvdh-multiplier","asymptotic-notation-beyond-big-o"]),
  inf("D3.2","The seven margins $g_i$ below one are all at least $2^{-181}$, so $\\min_ig_i=2\\kappa$ with $\\kappa=2^{-182}$.",
      "Thus $\\min_i g_i=2^{-181}=2\\kappa$.",None,["asymptotic-notation-beyond-big-o","inequalities-for-error-bounds"],
      salient="The exponent $\\kappa=2^{-182}$ is astronomically small and is set by the smallest margin, $g_2=\\epsilon c(1-\\tau)$, which is the product of three tiny fixed exponents."),
  inf("D3.3","Every term is at most $p^{1-2\\kappa}$ and any fixed power of $\\log p$ is at most $p^\\kappa$, so the large-input bound is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
      "The complete large-input bound is consequently",None,["asymptotic-notation-beyond-big-o","big-o"])],
 page="cost-accounting",
 frm=["transform-layout","synthetic-convolution","retained-permutations","multiplication-algorithm","size-parameters"])

A=show("A","Two tape procedures, an address-chunk interchange and a simultaneous butterfly layer, each cost a power $u^\\tau$ or $d^{\\lambda'}$ below the naive factor.",
 "derive both procedures from fixed linear networks whose rank deficit $s<Wm$ gives a recursion that saves a power",
 expl("A strict inequality between the number of smaller calls per level and the growth of the width is where the power saving comes from.","is the source of the power saving."),
 [S1,S2,S3,S4],frm=["fixed-tape-model","tape-basics"])

B=show("B","Synthetic polynomial transforms and ring convolution run in $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$ time.",
 "implement the Fourier transforms over the ring where roots of unity are signed shifts, using the simultaneous layers, then multiply pointwise",
 rec("The expensive parts of a transform are address movement and butterflies, which the two procedures speed up, while the ring makes the twiddle factors free."),
 [S5,S6],frm=["fixed-point","ring-mod-yr-plus-1"])

D=show("D","The sizes, the assembled algorithm with exact recovery, and the cost bound complete the multiplication.",
 "choose parameters compatible with all earlier interfaces, run the pipeline, prove exactness, and sum the costs",
 expl("The proof places the procedures inside the multiplication reduction and accounts for every change of representation.","The remaining proof places these procedures inside the multiplication"),
 [SP,MA,CA],frm=["hvdh-multiplier"])

root=show("S0","A deterministic fixed-tape Turing machine multiplies $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "build two tape procedures that save a power of the width, use them inside the Harvey and van der Hoeven Gaussian-resampling multiplication with polynomial transforms and retained permutations, then choose parameters, prove exactness and sum the costs",
 expl("Scanning the data at each of $\\log n$ transform levels already costs $n\\log n$, so beating it needs savings in both movement and arithmetic.","We therefore need savings in both movement and arithmetic."),
 [A,B,S7,D],page="main-theorem",
 frm=["fixed-tape-model","nlogn-conjecture","hvdh-multiplier","big-o"],
 salient="The exponent $\\kappa=2^{-182}$ is astronomically small, yet strictly positive: the saving is a power of $\\log n$ for all input lengths, and it disproves the $n\\log n$ conjecture in this model.")
json.dump({"root":root},open('exegenius/tasks/0003-argument.answer.json','w'),indent=1,ensure_ascii=False)
