from lib import *


def gaussian_resampling():
    neumann = show(
        r"The Neumann sum $\widetilde{\mathsf J}'u=\sum_{j<k}(-1)^j\widetilde v^{(j)}$ with $k=\lceil p/(\alpha^2\theta)\rceil\le\alpha^2+1$ terms costs $O(tp\sqrt p\,\alpha)$.",
        "Evaluate $N^{-1}=\\sum(-E)^j$ by iterating the rounded map $\\widetilde E$, whose window of radius $\\lceil\\sqrt p/(2\\alpha)\\rceil$ is scanned once per iterate.",
        mot("Each term of the series is one pass of a short window over records of $O(p)$ bits, and there are only about $\\alpha^2$ terms.", "recoverable"),
        [
            infer(r"The $\mathsf S'$ procedure uses a periodic input window of radius $\lceil\sqrt p\rceil\alpha$ per output, so visiting these $O(p)$-bit records costs $O(tp\sqrt p\,\alpha)$ tape steps.",
                  3742, r"The $\mathsf S'$ procedure uses a consecutive periodic input", r"$O(tp\sqrt p\alpha)$ tape steps."),
            infer(r"The iterates $\widetilde v^{(0)}=Q_p(u/2)$, $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$ stay in $\mathbb D_p^s$ by induction, and $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$.",
                  3759, r"For $u\in\mathbb D_p^s$, Lemma~4.12 rounds the real and imaginary parts", r"(-1)^j\widetilde v^{(j)}$."),
            infer(r"The $k-1$ calls of $\widetilde E$ cost $O((\alpha^2+1)tp(1+\sqrt p/\alpha))=O(tp\sqrt p\,\alpha)$, using $2\le\alpha<\sqrt p$.",
                  3778, r"The $k-1$ calls therefore spend", r"using $2\leq\alpha<\sqrt p$."),
        ],
        frm=["summation-geometric-series-and-products"])
    return show(
        r"For coprime $2\le s<t<2^p$ with $\theta=t/s-1>p/\alpha^4$ there are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, each computable with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$.",
        "Use Gaussian-weighted resampling maps $\\mathsf S,\\mathsf T$ with $\\mathsf TP_sF_s=P_tF_t\\mathsf S$, select nearby points to get $N=C\\mathsf T\\mathsf D\\approx I$, invert $N$ by a Neumann series, and absorb the normalisations into $A$ and $B_0$.",
        mot("The usual implementation sorts twice on each coordinate; here both permutations are retained in the transform formula and that formula is computed directly.", "explicit",
            (3501, r"Its usual implementation sorts twice on each coordinate.", r"compute that formula directly.")),
        [
            infer(r"Setting $N=C\mathsf T\mathsf D$, the summand of index $j$ in $(Nu)_j$ is exactly $u_j$ because $\mathsf D$ cancels the Gaussian factor at the selected coordinate, and the other summands form $((N-I)u)_j$.",
                  3598, r"Set $N=C\mathsf T\mathsf D$.", r"form $((N-I)u)_j$."),
            infer(r"The exact Gaussian identity $\mathsf TP_sF_s=P_tF_t\mathsf S$ and the estimate $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ are proved by Harvey and van der Hoeven.",
                  3601, r"The exact Gaussian identity and inverse estimate proved in", r"2^{-\alpha^2\theta}."),
            infer(r"Since $\alpha^2\theta>p/\alpha^2>1$ we get $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series.",
                  3611, r"Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have", r"by the Neumann series."),
            infer(r"With $A=\mathsf S'=\mathsf S/2$ and $B_0=\mathsf D'\mathsf J'C$ where $\mathsf J'=N^{-1}/2$ and $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, all norm bounds $3/4,7/8,1$ and $\|C\|=1$ make $A,B_0$ contractions.",
                  3625, r"Now set $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$.", r"both are contractions."),
            infer(r"Since $\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$, applying it to the Gaussian identity gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$, and the normalisations multiply to $2^{-(2\alpha^2-2)}\cdot2^{-1}\cdot2^{-1}=2^{-2\alpha^2}$, giving the stated identity.",
                  3626, r"The diagonal map $\mathsf D$ is invertible, and $C\mathsf T=N\mathsf D^{-1}$, so", r"which is \eqref{eq:no-sort-one-dimensional}."),
            infer(r"The ordered maps $\widetilde{\mathsf S}',\widetilde{\mathsf J}',\widetilde{\mathsf D}'$ have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.",
                  3654, r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\", r"\widetilde{\mathsf D}'&4&O(tp^{1+\delta})"),
            infer(r"The selection $C$ takes an ordered subsequence, since $q_0=0$, $q_{s-1}<t$ and $q_{j+1}>q_j$ because $t/s>1$.",
                  3659, r"For $C$, observe that $q_0=0$,", r"selects an ordered subsequence."),
            infer(r"The selected indices are generated in order with $tj=sf_j+e_j$; since $e_j+\rho<2s$ the carry $c_j$ is the only possible one, so $C$ costs $O(tp)$ with no numerical error.",
                  3675, r"Here $e_j+\rho<2s$, so $c_j$ is the only possible carry;", r"$t(j+1)=sf_{j+1}+e_{j+1}$."),
            infer(r"Taking $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$ gives errors $16p<p^2$ and $4+3p^2/4<p^2$, with the costs adding to the claimed bound.",
                  3688, r"Contraction of the exact maps yields errors less than", r"claimed bound."),
            neumann,
        ],
        page="gaussian-resampling",
        frm=["dft", "error-accounting", "fixed-point-disk", "established-multiplier", "summation-geometric-series-and-products",
             "triangle-inequality-and-norms", "permutations", "primes-coprimality-and-gcd"],
        adds=[bind(r"\theta", "relative gap", "the relative gap $t/s-1$ between the target and source lengths", "direct"),
              bind(r"A", "expansion map", "the Gaussian-weighted contraction from $\\mathbb C^s$ to $\\mathbb C^t$", "direct"),
              bind(r"B_0", "compression map", "the Gaussian contraction from $\\mathbb C^t$ to $\\mathbb C^s$ that includes the Neumann-series inverse", "direct")],
        salient="The two sides differ by exactly the power of two $2^{2\\alpha^2}$, because the three normalisations multiply to $2^{-2\\alpha^2}$; this factor is later undone by a pure shift.")


def tensor_resampling():
    return show(
        r"On a zero-padded box of $T=\prod_it_i$ entries, applying the one-dimensional maps line by line gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$, error below $dp^2$ per map, and cost $O(dTp^{3/2+\delta}\alpha)$ plus $O(Tpd^2(1+\ell^\tau))$ for movement.",
        "Tensor the one-dimensional identity, expand or compress one axis at a time on valid lines only, and expose each axis as the innermost field by chunk interchanges.",
        mot("Apply the one-dimensional maps to one coordinate line at a time, with the chunk-swap algorithm supplying the movement of axis fields.", "explicit",
            (3796, r"For the tensor product, apply the one-dimensional maps to one coordinate", r"line at a time.")),
        [
            infer(r"Tensoring the one-dimensional identity gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$.",
                  3837, r"Tensoring \eqref{eq:no-sort-one-dimensional} proves"),
            infer(r"Embedding the input in the padded box and expanding the axes one at a time keeps valid entries in $[0,t_i)$ on expanded axes and $[0,s_i)$ otherwise, every other entry zero.",
                  3840, r"Expand the axes one at a time.", r"every other entry is zero."),
            infer(r"Each axis map acts independently on valid lines and is zero elsewhere, so it is a contraction with error below $p^2$, and the $d$ axes compose to error below $dp^2$.",
                  3857, r"For a fixed axis, the exact map acts independently on its valid lines", r"less than $dp^2$."),
            infer(r"At most $T/t_i$ lines invoke the one-dimensional algorithm on axis $i$, so the cost is $\sum_{i}\frac T{t_i}O(t_ip^{3/2+\delta}\alpha)=O(dTp^{3/2+\delta}\alpha)$.",
                  3862, r"At most $T/t_i$ lines invoke the one-dimensional algorithm for axis $i$,", r"=O(dTp^{3/2+\delta}\alpha)."),
            infer(r"For axes of unequal widths $\ell$ and $\ell-1$, peel the leading bit of the longer field, interchange the equal-width parts, and move the bit back.",
                  3878, r"For unequal widths, write the longer field as", r"obtaining $y\,e\,x$."),
            infer(r"Each adjacent interchange costs $O(Tp(1+\ell^\tau))$ and exposing and restoring one axis needs $O(d)$ of them, so all axes need $O(d^2)$ interchanges.",
                  3885, r"Each adjacent interchange therefore", r"all axes need $O(d^2)$."),
            infer(r"Since $t_i\ge r/2$, each tensor map invokes at most $2dT/r$ lines, so setup of $O(p^c)$ per line totals $O(dTp^c/r)=o(Tp)$.",
                  3891, r"Since $t_i\geq r/2$, each tensor map invokes at most", r"$O(dTp^c/r)=o(Tp)$"),
        ],
        page="padded-box-tensor-resampling",
        frm=["gaussian-resampling", "multidimensional-dft", "arbitrary-width-interchange", "error-accounting", "stream-operations"])


def bluestein():
    return show(
        r"With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$ and all $t_i$ even, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$: a pointwise phase, a cyclic convolution with the chirp, and another phase.",
        "Expand the coefficient of $u_{\\boldsymbol k}$: the three chirp factors combine to $\\exp(2\\pi i\\sum s_ij_ik_i/t_i)$, which is exactly the entry of $QF_{\\boldsymbol t}$.",
        mot("The chirp identity performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array.", "explicit",
            (3902, r"The chirp identity below performs the frequency change", r"in $Q$ without applying $Q$ as a separate permutation of the array.")),
        [
            infer(r"The chirp has period $t_i$ in coordinate $i$ because replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\pi is_i(2j_i+t_i)$, an integral multiple of $2\pi i$ when $t_i$ is even.",
                  3939, r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by", r"an integral multiple of $2\pi i$."),
            infer(r"The coefficient of $u_{\boldsymbol k}$ on the right is $\frac1T\overline a_{\boldsymbol j}a_{\boldsymbol j-\boldsymbol k}\overline a_{\boldsymbol k}=\frac1T\exp(2\pi i\sum_is_ij_ik_i/t_i)$, the coefficient of $QF_{\boldsymbol t}$ since $Q$ reads frequency $(-s_ij_i)_i$.",
                  3941, r"The coefficient of $u_{\boldsymbol k}$ in the right side of", r"from the negative-sign transform."),
        ],
        page="bluestein-chirp",
        frm=["dft", "cyclic-convolution", "multidimensional-dft", "complex-numbers", "roots-of-unity"])


def perm_cancel():
    return show(
        r"With $S=\prod_is_i$ and the source permutation $R$, $RF^+_{\boldsymbol s}\bigl[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)\bigr]=(u*v)/S^2$, so $R$ cancels although it is applied three times.",
        "Show $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$ from the dilation identity, move $R$ through the pointwise product, and apply the convolution theorem.",
        mot("The retained source permutation $R$ must cancel across the two forward transforms, the pointwise product and the opposite transform so that no full sort is executed.", "explicit",
            (3905, r"The second identity shows how the", r"retained source permutation $R$ cancels when computing a convolution.")),
        [
            infer(r"For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$.",
                  3953, r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$.", r"=(R_c^{-1}F_q^+z)_j."),
            infer(r"Because each $t_i$ is a unit modulo $s_i$, tensoring gives $F^+_{\boldsymbol s}R=R^{-1}F^+_{\boldsymbol s}$ and hence $RF^+_{\boldsymbol s}R=F^+_{\boldsymbol s}$.",
                  3960, r"Each $t_i$ is a unit modulo $s_i$", r"RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$."),
            infer(r"A coordinate permutation commutes with pointwise products, so $(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)=R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$.",
                  3963, r"because a coordinate permutation commutes with pointwise products."),
            infer(r"The convolution rule $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)(F_{\boldsymbol s}v)$ and $F^+_{\boldsymbol s}F_{\boldsymbol s}=I/S$ give $F^+_{\boldsymbol s}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$.",
                  3973, r"The normalized convolution rule is", r"=\frac{u*v}{S^2},"),
            infer(r"Conjugating input and output turns an algorithm for $RF_{\boldsymbol s}$ into one for $RF^+_{\boldsymbol s}$, commuting with the real permutation $R$ and preserving grid, norm and error.",
                  3983, r"Finally, conjugation changes the negative Fourier sign to the positive one", r"error bound."),
        ],
        page="permutation-cancellation",
        frm=["gaussian-resampling", "bluestein-chirp", "dft", "cyclic-convolution", "multidimensional-dft", "permutations", "modular-arithmetic"],
        salient="Applied three times, the permutation $R$ leaves no trace: the result equals the convolution (scaled by $1/S^2$) as if no permutation had been used.")
