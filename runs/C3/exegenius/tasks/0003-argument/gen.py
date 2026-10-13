import json
def inf(id,claim,quote,page=None,frm=(),salient=None):
    d={"id":id,"intention":"infer","claim":claim,"quote":{"source":"paper","quote":quote},"from":list(frm)}
    if page:d["page"]=page
    if salient:d["salient"]=salient
    return d
def mot(text,src,q=None):
    return {"text":text,"source":src,"quote":({"source":"paper","quote":q} if q else None)}
def B(s,n,m,r="direct"):return {"symbol":s,"name":n,"meaning":m,"relation":r}

S1=inf("S1","Moving data on a fixed-tape machine costs time: scanning $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.",
 "$\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$.","tape-streams",["turing-machine","big-o","finite-state-and-constant-size-alphabets"])

S2=inf("S2.1","A fixed linear exchange network with a common invertible frame at each gate lets arrays flow through pointwise, so only the endpoint frame operators remain on each of the $W$ roles.",
 "At a pointwise linear gate $G$, the common frame commutes with the gate:","linear-network",["linear-algebra-over-the-reals-and-complex-numbers","address-fields","tape-streams"])
S22=inf("S2.2","A finite three-subset network with nested subspaces on gates makes the total number $s$ of smaller calls satisfy $s<Wm$.",
 "number $s$ of smaller calls satisfies $s<Wm$.","subset-network",["linear-network","linear-algebra-over-gf-2","linear-algebra-over-the-reals-and-complex-numbers","cartesian-products-and-mixed-radix-indexing"],
 salient="The saving $s<Wm$ is strict, yet the network has exactly the same endpoint operator (an identical shear) on every role; the page should explain why the subspace labels give a strict rank deficit.")
S23=inf("S2.3","A recursive call at parameter $mf$ uses $s$ calls on streams of volume $V/W$, so the cost per volume grows by a factor $s/W<m$ per factor $m$ in the parameter, a power saving.",
 "increases the recursive contribution by $s/W<m$. This strict inequality","recursive-power-saving",["subset-network","linear-network","geometric-series-and-recurrences","big-o"],
 salient="The exponent $\\tau<1$ arises from the strict inequality $s/W<m$; with equality there would be no saving.")
S24=inf("S2.4","A rational matrix shear $(H,D)\\mapsto(H+AD,D)$ of rank $a$ costs exactly $a$ smaller interchanges plus $O(V)$ work, via a lower triangular factorization.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit","shear-factorization",["address-fields","triangular-matrices-and-gaussian-elimination","modular-arithmetic-and-prime-numbers"])
S25=inf("S2.5","For power widths $e=m^k$ with enough rows, the recursion on the rank-saving network interchanges the two chunks in $O(Ve^\\tau)$ time.",
 "The chunks can be interchanged in $O(Ve^\\tau)$ time, preserving every")
S26=inf("S2.6","Removing the power-width and row restrictions, two chunks of $u$ bits are interchanged in $O(Vu^\\tau)$ steps for any width.",
 "in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.")
S2n={"id":"S2","intention":"show","page":"fast-interchange",
 "claim":"Two equal address chunks of $u$ digits of an array of volume $V$ can be interchanged in time $O(Vu^\\tau)$ for a fixed $\\tau<1$.",
 "method":"Build a fixed linear exchange network whose endpoint operator is an address shear, show its total edge rank $s$ is below $Wm$, and recurse on smaller interchanges",
 "motivation":mot("Plain sorting of address fields costs a pass per level; a recursion whose number of smaller calls is less than the number of roles times the dimension saves a power of the chunk width.","explicit",
   "Because the sum of these ranks is less than the number of wires times"),
 "adds":[B("W","number of roles","The number of wires (roles) of the fixed network.","count"),
         B("m","network dimension","The dimension of the fixed space whose subspaces label the gates; a chunk is split into $m$ fields.","direct"),
         B("s","smaller-call count","The total number of smaller interchange calls over all edges of the network.","count"),
         B("e","chunk width","The number of digits in each of the two chunks being interchanged.","direct")],
 "salient":"The final effect is an exact permutation, although the intermediate steps compute XOR combinations of data; and the saving is a power $u^\\tau$ with $\\tau<1$ uniformly in the shape.",
 "from":["tape-streams","address-fields","linear-network","subset-network","recursive-power-saving","shear-factorization","linear-algebra-over-gf-2","big-o"],
 "children":[S2,S22,S23,S24,S25,S26]}

S3c=[inf("S3.1","The butterfly layer is a tensor product of an auxiliary two-point kernel whose phase frames use smaller groups of selected bits separated by binary changes of basis.",
 "We first construct tensor products of the auxiliary two-point kernel"),
 inf("S3.2","The changes of basis are implemented by whole address chunk moves, using the fast interchange, and splitting complete rows among the network's roles reduces the volume of each recursive call.",
 "selected bits, separated by binary changes of basis. We implement those"),
 inf("S3.3","The intermediate dyadic values are bounded and the completed layer is converted to the normalized $H_0$ layer, evaluated exactly before one truncation.",
 "call. Finally, we bound the intermediate dyadic values and convert the"),
 inf("S3.4","The simultaneous normalized butterfly layer returns $Q_p(\\mathcal H z)$ in time $O(Vd^{\\lambda'})$ with error below $\\sqrt2\\,2^{-p}$.",
 "coefficient order, and component format in $O(Vd^{\\lambda'})$ time,")]
S3={"id":"S3","intention":"show","page":"fast-butterfly-layers",
 "claim":"The two-point butterfly $H_0$ can be applied at the same bit position in each of $d$ address chunks of an array of polynomial records of volume $V$ in time $O(Vd^{\\lambda'})$ with $\\lambda'<1$.",
 "method":"Apply the complex phase network with the same rank-saving recursion, using fast chunk interchanges for the changes of basis and exact dyadic arithmetic",
 "motivation":mot("Doing the $d$ butterfly factors separately needs $d$ whole-array passes; the same rank-saving recursion that speeds interchange applies to a common layer and makes it cost a power $d^{\\lambda'}$ of a pass.","explicit",
   "whereas separate butterfly factors would require $D$ whole-array passes."),
 "adds":[B("d","chunk count","The maximum number of equal-width address chunks in which one common bit is butterflied.","count"),
         B("V","stored volume","The number of stored data bits of the array.","count")],
 "salient":"The exponent $\\lambda'<1$ is a power saving over $d$ separate passes, coming from the same strict inequality of the complex network.",
 "from":["butterfly","fixed-point-dyadics","linear-network","subset-network","recursive-power-saving","fast-interchange","address-fields","polynomial-ring"],
 "children":S3c}

S4c=[inf("S4.1","Over $\\mathbb C[y]/(y^r+1)$ multiplication by a power of $y$ is a signed cyclic shift and an isometry, so powers of $y$ act as roots of unity.",
 "Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes","polynomial-ring",["polynomials","complex-numbers","convolution","roots-of-unity-and-euler-s-formula"]),
 inf("S4.2","With $\\omega_t=y^{2r/t}$ the normalized synthetic transforms are contractions, and $F_t^+F_t^-=t^{-1}I$ so the opposite transform inverts it.",
 "For a power of two $t$ dividing $2r$, define $\\omega_t=y^{2r/t}$.","synthetic-transform",["dft","polynomial-ring","roots-of-unity-and-euler-s-formula","polynomials"]),
 inf("S4.3","Transforms on several axes are computed by simultaneous butterfly layers on a tape layout that keeps the frequency order, within the stated cost.",
 "\\begin{lemma}[Transform layout and cost]","transform-layout",["synthetic-transform","butterfly","fast-butterfly-layers","fast-interchange","address-fields"]),
 inf("S4.4","Polynomial products over the ring are done by signed Kronecker packing into integers and one call to the established $O(N\\log N)$ integer multiplier.",
 "One can compute the exact Gaussian integer","signed-packing",["polynomial-ring","hvdh-multiplier","big-o","binary-and-two-s-complement-representation"]),
 inf("S4.5","Performing both forward transforms in the retained order, the pointwise ring products and the opposite transform gives the normalized convolution $\\mathcal M_r$.",
 "Perform both forward transforms and retain their common $LB$ order.")]
S4={"id":"S4","intention":"show","page":"ring-convolution",
 "claim":"Normalized convolution of arrays over $\\mathbb C[y]/(y^r+1)$ on power-of-two axes can be computed with the retained transform layout at the stated cost.",
 "method":"Transform both operands forward with synthetic transforms, multiply pointwise by signed packing, and apply the opposite transform to the same retained frequency order",
 "motivation":mot("The transform turns convolution into pointwise product, and powers of $y$ are cheap roots of unity, so only layer arithmetic and short ring products remain.","recoverable"),
 "from":["convolution","dft","polynomial-ring","synthetic-transform","transform-layout","signed-packing","hvdh-multiplier","fast-butterfly-layers"],
 "children":S4c}

S5c=[inf("S5.1","Gaussian resampling gives linear contractions $A,B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, expressing a Fourier transform of coprime length through a power-of-two-length transform with permutations.",
 "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and","gaussian-resampling",["dft","fixed-point-dyadics","hvdh-multiplier","complex-numbers"]),
 inf("S5.2","Tensoring the one-dimensional identity gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ in any dimension, with the axis movement costed by chunk swaps.",
 "Tensoring \\eqref{eq:no-sort-one-dimensional} proves"),
 inf("S5.3","Bluestein's chirp identity writes the middle transform $QF_{\\boldsymbol t}$, including its permutation $Q$, as a cyclic convolution and two pointwise phase multiplications.",
 "computed from a cyclic convolution and two pointwise phase","bluestein",["dft","convolution","roots-of-unity-and-euler-s-formula"]),
 inf("S5.4","The retained source permutation $R$ cancels across the two forward transforms, the pointwise product and the opposite transform, giving $(u*v)/S^2$.",
 "(RF_{\\boldsymbol s}^+)")]
S5={"id":"S5","intention":"show","page":"retained-permutations",
 "claim":"Fourier transforms of pairwise coprime lengths can be done through power-of-two transforms with the resampling permutations left inside the transform, so that no separate sorts are run.",
 "method":"Use the Gaussian resampling identity with permutations kept in the formula, convert the middle transform to convolution by Bluestein's chirp, and show the source permutation cancels",
 "motivation":mot("The usual implementation sorts twice on each coordinate, which would cost a full sort per axis; keeping the permutations inside the identity lets them cancel.","explicit",
   "Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each"),
 "adds":[B("S","total source length","The product of the pairwise coprime source lengths $s_i$.","direct")],
 "salient":"The source permutation $R$ appears in both forward transforms and in the inverse, and cancels exactly in the convolution identity.",
 "from":["gaussian-resampling","bluestein","dft","convolution","permutations-and-sorting","cartesian-products-and-mixed-radix-indexing","ring-convolution"],
 "children":S5c}

S6c=[inf("S6.1","The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map $\\Phi$ made of controlled shifts.",
 "Let $s_1,\\ldots,s_d$ be the pairwise coprime","crt-address-map",["convolution","modular-arithmetic-and-prime-numbers","address-fields","cartesian-products-and-mixed-radix-indexing"]),
 inf("S6.2","A coefficient twist $x_d\\mapsto\\zeta y$ turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap yields the cyclic wrap after untwisting.",
 "The power-of-two complex convolution used in the chirp identity is","phase-twist",["polynomial-ring","convolution","roots-of-unity-and-euler-s-formula"]),
 inf("S6.3","Each operand is split into radix-$2^b$ digits stored as scaled fixed-point values, to be convolved, rounded, and carried.",
 "Read each stored operand backward from its least significant end in groups of $b$ bits.","radix-digit-reduction",["convolution","schoolbook-multiplication-and-carries","fixed-point-dyadics","binary-and-two-s-complement-representation"]),
 inf("S6.4","With the chosen parameters the accumulated error in the recovered coefficients is below $1/2$, so rounding gives the exact integer convolution and carries give the product.",
 "less than $1/2$; it also justifies the rounding, carries, and output","precision-recovery",["fixed-point-dyadics","vector-norms-and-inequalities","floor-ceiling-rounding-and-logarithms","schoolbook-multiplication-and-carries"]),
 inf("S6.5","Each of the seven cost-table powers of $p$ is at most $1-2\\kappa$, so the total time is $O(n(\\log n)^{1-\\kappa})$.",
 "Each of the seven displayed powers is at most $1-2\\kappa$ by"),
 inf("S6.6","The resulting single fixed-tape deterministic machine produces the $2n$-bit product in worst-case time $O(n(\\lg n)^{1-\\kappa})$ for every input length.",
 "$O(n(\\lg n)^{1-\\kappa})$ for every input length and produces precisely")]
S6={"id":"S6","intention":"show","page":"multiplication-algorithm",
 "claim":"The exact product of two $n$-bit integers is obtained by CRT address map, two source transforms, pointwise product, inverse transform, scaling, rounding and carries, in total cost $O(n(\\lg n)^{1-\\kappa})$.",
 "method":"Compose the preceding procedures into one pipeline, prove exact recovery by an error bound below $1/2$, and total the cost table for a fixed rational parameter choice",
 "motivation":mot("Each stage is only approximate or only a change of representation; one must track every normalization and error and charge every representation change to see that exact rounding and the power saving survive.","recoverable"),
 "adds":[B("p","precision","The number of fractional bits of the fixed-point values.","direct"),
         B("\\kappa","saving exponent","The fixed exponent $2^{-182}$ of the logarithmic saving.","direct")],
 "salient":"The final exponent $\\kappa=2^{-182}$ is astronomically small, but strictly positive, because every table power is at most $1-2\\kappa$.",
 "from":["convolution","ring-convolution","retained-permutations","fixed-point-dyadics","hvdh-multiplier","fast-interchange","fast-butterfly-layers","big-o","asymptotic-conventions"],
 "children":S6c}

root={"id":"S0","intention":"show","page":"main-theorem",
 "claim":"A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in $O(n(\\lg n)^{1-\\kappa})$ time with $\\kappa=2^{-182}$.",
 "method":"Reduce multiplication to digit convolution computed by Fourier transforms, and speed up the two bottlenecks, address rearrangement and butterfly layers, by a recursion with a strict rank saving",
 "motivation":mot("Plain transform multiplication spends $\\Theta(\\log n)$ scans of the data; shaving a power off that factor requires savings in both movement and arithmetic.","explicit",
   "We therefore need savings in both movement and arithmetic. Two tape"),
 "salient":"The saving is a fixed power $(\\lg n)^{-\\kappa}$ of the logarithm, not a smaller factor such as $\\log\\log n$, and it refutes the $n\\log n$ conjecture.",
 "from":["nlogn-conjecture","convolution","hvdh-multiplier"],
 "children":[S1,S2n,S3,S4,S5,S6]}
json.dump({"root":root},open("/home/user/openai-nlogn-wiki/runs/C3/exegenius/tasks/0003-argument.answer.json","w"),indent=1)
