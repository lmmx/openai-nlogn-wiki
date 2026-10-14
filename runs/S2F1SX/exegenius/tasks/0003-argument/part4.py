from lib import *

one_dim = show(
    "S5.1",
    r"For coprime lengths $s<t$ with $\theta=t/s-1>p/\alpha^4$ there are contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, each approximable with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.",
    r"Start from the Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$, invert $\mathsf T$ from the left through a Neumann series, scale each factor into a contraction, and leave both coordinate permutations in the formula.",
    ("recoverable", "A Fourier transform of coprime length is expressed through one of power-of-two length by Gaussian weights; the permutations appear in the identity itself, so keeping them costs nothing and saves the two sorts."),
    [
        inf("S5.1a",
            r"The Gaussian identity (Harvey and van der Hoeven) is $\mathsf TP_sF_s=P_tF_t\mathsf S$, and $N=C\mathsf T\mathsf D$ satisfies $\|N-I\|<2^{-\alpha^2\theta}$, where $C$ selects the coordinates nearest to $tj/s$ and $\mathsf D$ is a diagonal map.",
            r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
        inf("S5.1b",
            r"Since $\alpha^2<p$ and $\theta>p/\alpha^4$ give $\alpha^2\theta>p/\alpha^2>1$, one has $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series.",
            r"by the Neumann series. Put"),
        inf("S5.1c",
            r"Setting $A=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ with $\mathsf J'=N^{-1}/2$ and $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$ gives contractions whose normalizations multiply to $2^{-2\alpha^2}$, hence $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.",
            r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$."),
        inf("S5.1d",
            r"The ordered numerical maps have errors $16p$, $3p^2/4$ and $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$, and $C$ is an ordered subsequence selection costing $O(tp)$, so $\widetilde A$ and $\widetilde B_0$ have error below $p^2$ and the stated time.",
            r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"),
        inf("S5.1e",
            r"The original construction implements $P_t$ and $P_s^{-1}$ by two label-and-sort operations of cost $O(tp\log t)$ each; here they remain in the identity and are not executed.",
            r"implement $P_t$ and $P_s^{-1}$, each costing $O(tp\log t)$.",
            salient=r"The two coordinate permutations are not executed at all: they are part of the transform formula that the later chirp and cancellation steps absorb."),
    ],
    frm=["dft", "exponential-function-and-gaussian-function", "vector-norms-and-error-bounds", "modular-arithmetic"],
)

tensor = show(
    "S5.2",
    r"Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, and applying the line maps axis by axis in the zero-padded box of $T$ entries costs $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tpd^2(1+\ell^\tau))$ for axis movement, with error below $dp^2$.",
    "Embed the input in the padded box, expand and compress one axis at a time with the line algorithm on the innermost field, and move axes past each other with the chunk interchange.",
    ("recoverable", "The one-dimensional maps act on lines, so each axis in turn must be made the innermost address field; the chunk interchange supplies that movement."),
    [
        inf("S5.2a",
            r"Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, and $\mathcal A,\mathcal B_0$ are contractions.",
            r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
        inf("S5.2b",
            r"To apply $\mathcal A$, embed the input in the padded box with zeros and expand the axes one at a time: on a line whose other coordinates are valid, apply $\widetilde A_i$ to the first $s_i$ values and write $t_i$ values, and write $t_i$ zeros on every other line; compression is analogous.",
            r"To implement $\mathcal A$, first embed its"),
        inf("S5.2c",
            r"At most $T/t_i$ lines invoke the line algorithm for axis $i$, so the total is $\sum_i(T/t_i)O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$, and the error is below $dp^2$.",
            r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,"),
        inf("S5.2d",
            r"Exposing and restoring one axis needs $O(d)$ adjacent interchanges of $\ell$- or $(\ell-1)$-bit fields (equal widths by the chunk interchange, unequal widths after moving the leading bit), each costing $O(Tp(1+\ell^\tau))$, so all axes cost $O(Tpd^2(1+\ell^\tau))$.",
            r"costs $O(Tp(1+\ell^\tau))$. Exposing and restoring one axis needs",
            frm=["chunk-interchange"]),
        inf("S5.2e",
            r"Since $t_i\ge r/2$ at most $2dT/r$ lines are processed per tensor map, so any fixed polynomial in $p$ of setup per line totals $o(Tp)$ because $r$ exceeds every fixed power of $p$.",
            r"Since $t_i\geq r/2$, each tensor map invokes at most"),
    ],
    frm=["multidim-transform", "chunk-interchange", "fixed-point-disk-grid"],
)

resampling = show(
    "S5",
    r"For pairwise coprime $s_i$ and powers of two $t_i$ with $t_i/s_i-1$ large enough, the source Fourier transform with its coordinate permutations satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, evaluated line by line in time $O(dTp^{3/2+\delta}\alpha)$ with error below $dp^2$, without sorting.",
    "Use Harvey and van der Hoeven's Gaussian resampling identity but retain the two coordinate permutations in the formula, prove the one-dimensional interface, then take tensor products and apply it axis by axis in a padded box.",
    ("explicit", "The usual implementation sorts twice on each coordinate; here both permutations are kept in the transform formula and computed directly.",
     r"coordinate. We retain both permutations in the transform formula and"),
    [one_dim, tensor],
    page="gaussian-resampling",
    frm=["dft", "multidim-transform", "fixed-point-disk-grid", "nlogn-multiplier", "exponential-function-and-gaussian-function"],
    adds=[
        sym("\\alpha", "Gaussian width", "The width parameter of the Gaussian weights, with $2\\le\\alpha<\\sqrt p$; larger $\\alpha$ shrinks the resampling error but lengthens each window.", "direct"),
        sym("\\delta", "multiplier exponent", "A fixed exponent $0<\\delta<1/8$ in the cost $O(\\max(p,\\log k)^{1+\\delta})$ of the cited exponential and multiplication routines.", "direct"),
        sym("\\gamma", "source scale exponent", "The exponent $\\gamma=2d\\alpha^2$ of the power of two by which the compressed transform is scaled.", "direct"),
    ],
)

chirp = inf(
    "S6",
    r"With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ of period $t_i$ (all $t_i$ even), the permuted transform is $QF_{\boldsymbol t}u=\overline a\cdot\big(a*(\overline a\cdot u)\big)/T$, a pointwise phase, a cyclic convolution with the chirp, and another pointwise phase.",
    r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because",
    page="chirp-identity",
    frm=["dft", "cyclic-convolution", "multidim-transform", "gaussian-resampling"],
    salient=r"The frequency permutation $j\mapsto -sj$ inside $QF_{\boldsymbol t}$ costs nothing: the kernel $\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}$ equals $\exp(2\pi i\sum s_ij_ik_i/t_i)$ because $j^2-(j-k)^2+k^2=2jk$, which is exactly the permuted transform's coefficient.",
)

cancel = show(
    "S7",
    r"The retained source permutation $R$ cancels across the two forward source transforms, their pointwise product and the opposite-sign transform: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, so no sort is executed.",
    "Show that the opposite transform is unchanged by conjugating with the unit dilation $R$, slide $R$ through the pointwise product, and finish with the normalized convolution rule.",
    ("explicit", "The second identity shows that the retained source permutation cancels when computing a convolution.",
     r"retained source permutation $R$ cancels when computing a convolution."),
    [
        inf("S7a",
            r"A dilation $R_c$ by a unit $c$ modulo $q$ satisfies $F_q^+R_c=R_c^{-1}F_q^+$, so tensoring over the axes, where each $t_i$ is a unit modulo $s_i$, gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$.",
            r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
        inf("S7b",
            r"A coordinate permutation commutes with pointwise products, so $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$ and the left side equals $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
            r"because a coordinate permutation commutes with pointwise products."),
        inf("S7c",
            r"By $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, one gets $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
            r"The normalized convolution rule is",
            frm=["convolution-theorem"]),
    ],
    page="permutation-cancellation",
    frm=["gaussian-resampling", "convolution-theorem", "functions-bijections-and-permutations", "primes-coprimality-and-gcd"],
    salient=r"The source permutation $R$ disappears from the final answer entirely, although it appears in both forward transforms and the opposite transform: dilation by a unit conjugates the opposite transform to itself, and permutations commute with pointwise products.",
)
