from lib import *
from key2 import KEY
from tools import ACI, FBL


def ST():
    return show(
        "With $\\omega_t=y^{2r/t}$ acting as a signed coefficient shift, radix-two decimation-in-frequency rounds with twiddle monomials compute $B_tF_t^-$ with outputs left in bit-reversed order, and the reversed procedure computes the opposite transform $F_t^+B_t^{-1}$, with product $1/t$.",
        "Prove character cancellation directly in the ring, derive the decimation-in-frequency recursion, track the named bit slots through the rounds to identify the stored order, and run the rounds in reverse for the opposite transform.",
        "The ring has zero divisors, so one cannot divide by $\\omega_t^j-1$ and character cancellation must be verified directly.",
        "explicit",
        mq=r"directly instead of dividing by $\omega_t^j-1$.",
        page="synthetic-transform",
        frm=["polynomial-ring-mod", "dft", "multidimensional-dft", "butterfly", "roots-of-unity", "fast-fourier-transform-and-divide-and-conquer"],
        salient="Powers of $y$ are exact roots of unity of order $2r$ that act only by signed shifts of the coefficient list, and the transform's output order (bit reversal) is never undone: the opposite transform consumes it as it is.",
        adds=[("t", "transform length", "The power-of-two length of one axis, dividing $2r$.", "count"),
              ("\\omega_t", "synthetic root", "The element $y^{2r/t}$ of the ring, a signed coefficient shift acting as a primitive $t$-th root of unity.", "direct")],
        children=[
            infer("Summing $\\omega_t^{jk}$ over $k$ gives $t$ if $t\\mid j$ and $0$ otherwise, and hence $F_t^+F_t^-=t^{-1}I$.",
                  r"F_t^+F_t^-=t^{-1}I."),
            infer("For $t\\nmid j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$.",
                  r"Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes"),
            infer("The sum therefore vanishes because the additive group of the ring has no two-torsion.",
                  r"$\mathcal R_r$ has no two-torsion."),
            infer("Decimation in frequency pairs $z_k$ with $z_{k+t/2}$ by $H_0$, multiplies the $b=1$ output by $\\omega_t^{-k}$, and recurses on the two halves, computing $F_t^-$.",
                  r"the $b=1$ output by $\omega_t^{-k}$, and then apply the length-$t/2$"),
            infer("After all $a$ rounds the named slots from high to low contain the frequency bits from low to high, so entry $j$ sits at slot $\\mathrm{rev}_a(j)$; the output record permutation is $B_t$.",
                  r"After all $a$ rounds, the named slots from high to low therefore"),
            infer("The consuming procedure traverses the recursion in reverse: process the smaller branches, apply the inverse monomial, then $H_0$.",
                  r"The procedure consuming this stored order traverses the recursion in"),
            infer("Since $H_0^2=I/2$, each reversed level is half the inverse of its forward level, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$.",
                  r"As $H_0^2=I/2$, the reversed level is half the inverse"),
            infer("The two exact procedures therefore implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
                  r"B_tF_t^-,\qquad F_t^+B_t^{-1},"),
            infer("For several axes, individual axis steps group into one parallel butterfly followed by one recordwise monomial multiplication $y^E$ with an address-dependent exponent $E$.",
                  r"Consequently the individual axis steps may be grouped as a parallel"),
        ])


def LAY():
    return show(
        "Placing the selected bits of the participating axes at a common offset in consecutive $K$-bit chunks by $O(dK)$ single-slot moves and $O(p/K)$ chunk exchanges lets every transform round use the fast layer, so a forward or opposite transform costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ with error below $\\sqrt2\\,\\ell\\,2^{-p}$.",
        "Move the low slots of each axis into a prefix, exchange chunks so that chunk index $j$ of all axes becomes adjacent, run the rounds on the remaining chunks with the fast layer and the prefix rounds individually, and add the three costs and the per-round truncation errors.",
        "The fast layer needs the selected bits of all participating axes at the same offset in consecutive equal chunks, so the stored layout of the axes must be rearranged first, at a cost that must itself be below the saving.",
        "explicit",
        mq=r"we must place the selected bits of the participating axes at a common",
        frm=["fast-butterfly-layer", "address-chunk-interchange", "synthetic-transform", "tape-address-model", "permutations-and-cartesian-products"],
        children=[
            infer("Each procedure has error below $\\sqrt2\\,\\ell\\,2^{-p}$ and costs $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$ for axis lengths $t_i\\in\\{2^{\\ell-1},2^\\ell\\}$ and chunk width $K\\le\\ell-1$.",
                  r"O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right)."),
            infer("With $b=(\\ell-1)\\bmod K$ and $q=\\lfloor(\\ell-1)/K\\rfloor$, the top slot of each long axis and the low $b$ slots of every axis go to a prefix.",
                  r"b=(\ell-1)\bmod K,"),
            infer("There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$.",
                  r"There are at most $D(b+1)=O(dK)$"),
            infer("Reordering the $Dq$ chunks to chunk-index-major order takes at most $Dq-1$ exchanges of width-$K$ chunks, even when nonadjacent.",
                  r"exchanges of width-$K$ address chunks, even when the chunks are"),
            infer("Each exchange costs $O(TpK^\\tau)$, so all exchanges cost $O(Tp\\,DqK^\\tau)=O(Tp\\,pK^{\\tau-1})$ because $Dq\\le d\\ell/K=O(p/K)$.",
                  r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
            infer("Each of the at most $\\ell$ rounds on the remaining chunks is one fast layer, costing $O(Tpd^{\\lambda'})$ per round and $O(Tp\\ell d^{\\lambda'})$ in total.",
                  r"The simultaneous-layer procedure therefore applies at cost"),
            infer("Rounds on prefix slots process bits individually with exact dyadics, one truncation per round, and there are at most $b+1\\le K$ of them, costing $O(TpdK)$.",
                  r"In a round on prefix slots, process the participating bits individually."),
            infer("Truncation toward zero is odd, so $J_EQ_p(\\mathcal Hz)=Q_p(J_E\\mathcal Hz)$ and the actual call sequence truncates once after the exact contraction round.",
                  r"J_EQ_p(\mathcal H z)=Q_p(J_E\mathcal H z)."),
            infer("A contraction does not increase the difference between computed and exact arrays and each truncation adds less than $\\sqrt2\\,2^{-p}$, so starting from zero error at most $\\ell$ rounds give the claimed error.",
                  r"zero error, at most $\ell$ rounds therefore"),
        ])


def SP():
    return show(
        "Two disk polynomials of degree below $r$ with $p$-bit Gaussian coefficients are multiplied exactly in $O(rp\\log(rp))$ time by evaluating their coefficients at $B_0=2^{4p}$, multiplying with the established multiplier, and reading coefficients back by centered residues and carries, giving $Q_p(fg/r)$.",
        "Use a signed Kronecker substitution: evaluate at $B_0$, form four integer products for the real and imaginary parts, recover signed product coefficients by a centered residue and carry recurrence, reduce modulo $y^r+1$, and shift to the normalization.",
        "Product coefficients have size below $B_0/2$, so a centered residue modulo $B_0$ identifies each coefficient uniquely even for negative values.",
        "recoverable",
        page="signed-packing",
        frm=["polynomial-ring-mod", "established-multiplier", "fixed-point-truncation", "binary-representation-and-bit-operations"],
        adds=[("B_0", "packing base", "The base $2^{4p}$ at which polynomial coefficients are evaluated to form integers.", "direct")],
        children=[
            infer("One can compute the exact Gaussian integer numerators of $fg$ and return $Q_p(fg/r)$ in time $O(rp\\log(rp))$ on a fixed number of tapes.",
                  r"One can compute the exact Gaussian integer"),
            infer("Write $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ and set $B_0=2^{4p}$; the signed evaluation integers are $A_u=u(B_0)$ for $u\\in\\{a,b,c,e\\}$.",
                  r"Set $B_0=2^{4p}$"),
            infer("The four absolute-value products are formed by the established multiplier and signs restored.",
                  r"pairs of absolute values using the established multiplier and restore"),
            infer("Every coefficient of any ordinary product satisfies $|h_j|\\le r2^{2p}<2^{3p}<B_0/2$, so no two adjacent fields interfere.",
                  r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2."),
            infer("While forming $A_u$ blockwise, the carry stays in $\\{-1,0\\}$, so $A_u$ has a two's-complement encoding in $r$ blocks of $4p$ bits.",
                  r"the carry stays in $\{-1,0\}$."),
            infer("While extracting, the carry belongs to $\\{0,1\\}$ and the centered residue of $q_j+\\rho_j$ equals $h_j$ itself by the separation bound.",
                  r"The carry belongs to $\{0,1\}$: if $\rho_j$ has this property, then"),
            infer("By the residual identity, $\\widehat h_j=h_j$, and a negative product ends with final carry $1$ canceled by its sign extension.",
                  r"Thus $\widehat h_j=h_j$."),
            infer("The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reducing modulo $y^r+1$ subtracts the coefficient at $j+r$ from that at $j$.",
                  r"The real and imaginary numerator streams are respectively"),
            infer("Each reduced Gaussian integer coefficient is a sum of exactly $r$ signed products of modulus at most $2^p$, so $|H_j|\\le r2^{2p}$.",
                  r"|H_j|\leq r2^{2p}."),
            infer("Four exact integer products dominate the linear packing, extraction, combination and truncation costs.",
                  r"Four exact integer products dominate the linear"),
        ])


def RCI():
    return show(
        "Retaining the common stored order of the two forward transforms, multiplying polynomial records pointwise by signed packing, applying the opposite transform and scaling exactly by $M$ gives the normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
        "Show that pointwise multiplication commutes with the record permutation $LB$, check the normalization from the convolution theorem, and propagate truncation errors through the bilinear contraction.",
        "The opposite transform consumes the forward output order, so no permutation needs to be undone before the pointwise product.",
        "explicit",
        mq=r"forward outputs in their retained order and pass that order directly",
        frm=["synthetic-transform", "signed-packing", "cyclic-convolution", "norms-absolute-values-and-error-bounds"],
        adds=[("M", "record count", "The number $T/r$ of polynomial records, equal to the product of the $d-1$ axis lengths.", "count")],
        children=[
            infer("The normalized convolution is $\\mathcal M_r(f,g)=(f*g)/(rM)=(f*g)/T$.",
                  r"\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}."),
            infer("Each output coefficient averages $rM$ signed scalar products, so $\\mathcal M_r$ is a bilinear contraction: $\\|\\mathcal M_r(f,g)\\|\\le\\|f\\|\\|g\\|$.",
                  r"\leq\|f\|_\infty\|g\|_\infty."),
            infer("Perform both forward transforms retaining their common $LB$ order, multiply corresponding records by the signed product, apply the opposite procedure, and multiply by $M$.",
                  r"Perform both forward transforms and retain their common $LB$ order."),
            infer("Expansion of the finite sums gives $F_{\\boldsymbol t}^-(f*g)=M(F_{\\boldsymbol t}^-f)(F_{\\boldsymbol t}^-g)$.",
                  r"=M(F_{\boldsymbol t}^-f)(F_{\boldsymbol t}^-g)."),
            infer("Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so $\\mathcal T_+$ applied to the pointwise product of stored forward outputs equals $F^+_{\\boldsymbol t}P(F^-f,F^-g)$.",
                  r"Since $LB$ permutes records and leaves their polynomial suffixes"),
            infer("With $\\delta=\\sqrt2\\ell2^{-p}$ and $\\eta=\\sqrt2\\,2^{-p}$, the bilinear contraction bound and truncation give $\\|\\widetilde z-z_*\\|<2\\delta+\\eta$.",
                  r"$\|\widetilde z-z_*\|_\infty<2\delta+\eta$."),
            infer("Since $\\mathcal T_+$ is a contraction, the opposite transform's own error gives $\\|\\widetilde h-\\mathcal T_+z_*\\|<3\\delta+\\eta$.",
                  r"<3\delta+\eta."),
            infer("The final exact multiplication by $M$ gives error less than $M(3\\delta+\\eta)=\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
                  r"The final exact multiplication by $M$ therefore gives error less than"),
            infer("There are $M=T/r$ pointwise polynomial products, costing $O(Tp\\log(rp))$ in total.",
                  r"There are $M=T/r$ pointwise polynomial products."),
        ])


def RC():
    return show(
        "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes is computed with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$ in time $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}+\\log(rp)])$.",
        "Compute two forward synthetic transforms with the same retained frequency order, multiply records pointwise by signed packing, and apply the opposite transform, with every layer a simultaneous butterfly layer and every axis alignment a fast chunk interchange.",
        "Entries of the transform are short polynomials in a quotient where the required roots of unity act by exact signed permutations of coefficient lists, so every transform step is a butterfly layer or a signed shift.",
        "explicit",
        mq=r"where the required roots of unity act by exact signed permutations",
        page="ring-convolution",
        frm=["dft", "multidimensional-dft", "polynomial-ring-mod", "cyclic-convolution", "fixed-point-truncation", "established-multiplier", "synthetic-transform", "signed-packing", "fast-butterfly-layer", "address-chunk-interchange"],
        adds=[("\\tau", "interchange exponent", "The fixed exponent $\\tau=1-2^{-50}<1$ with which an interchange of $u$-bit chunks costs $O(Vu^\\tau)$.", "direct"),
              ("\\lambda'", "layer exponent", "The fixed exponent $\\lambda'=1-2^{-54}<1$ with which a simultaneous butterfly layer on $d$ axes costs $O(Vd^{\\lambda'})$.", "direct"),
              ("\\sigma", "complex exponent", "The fixed exponent $\\sigma=\\tau$ bounding the logarithmic order of the complex network's recurrence.", "direct"),
              ("C", "two-point kernel", "The $2\\times2$ complex kernel $C=H\\,\\mathrm{diag}(1,i)\\,H=\\mu I+\\nu X$ from which the butterfly layer is built.", "direct"),
              ("\\mu", "kernel coefficient", "The coefficient $(1+i)/2$ of the identity in the kernel $C$.", "direct"),
              ("\\nu", "flip coefficient", "The coefficient $(1-i)/2$ of the bit flip $X$ in the kernel $C$.", "direct"),
              ("\\lambda", "internal exponent", "A fixed exponent with $\\max\\{\\tau,\\sigma\\}<\\lambda<\\lambda'<1$ bounding the node overhead of the layer recursion.", "direct"),
              ("\\beta", "cutoff exponent", "The fixed exponent $1/2$ with which recursion stops once the number of chunks falls below $d^\\beta$.", "direct")],
        children=[
            KEY(),
            ACI(),
            FBL(),
            ST(),
            LAY(),
            SP(),
            RCI(),
        ])
