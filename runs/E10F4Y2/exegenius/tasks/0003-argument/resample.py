from lib import *


def GR():
    return show(
        "For coprime integers $2\\le s<t<2^p$ with $\\theta=t/s-1>p/\\alpha^4$ there are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and $B_0:\\mathbb C^t\\to\\mathbb C^s$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$, computable with error below $p^2$ in time $O(tp^{3/2+\\delta}\\alpha)$, so neither coordinate permutation $P_s,P_t$ ever has to be executed.",
        "Use the exact Gaussian resampling identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ and the near-identity $N=C\\mathsf T\\mathsf D$ to build a left inverse by a Neumann series, then rescale each factor to a contraction.",
        "The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two; Gaussian resampling connects these two shapes.",
        "explicit",
        mq=r"whereas the synthetic transforms use powers of two. Gaussian resampling",
        page="gaussian-resampling",
        frm=["dft", "multidimensional-dft", "fixed-point-truncation", "established-multiplier", "complex-numbers", "primes-coprimality-and-gcd", "norms-absolute-values-and-error-bounds"],
        salient="The two coordinate permutations that the usual implementation executes as sorts stay inside the identity, so only the three arithmetic maps and the selection $C$ are ever executed.",
        adds=[("s", "source length", "The (prime) length of the source transform, smaller than $t$.", "count"),
              ("t", "target length", "The power-of-two length of the transform actually computed, with $t>s$.", "count"),
              ("\\alpha", "Gaussian width", "The integer width parameter of the Gaussian weights, with $2\\le\\alpha<\\sqrt p$.", "direct"),
              ("\\theta", "length gap", "The relative gap $t/s-1$, required to exceed $p/\\alpha^4$.", "direct"),
              ("\\delta", "cost exponent", "The fixed exponent $1/16<1/8$ in the cost of the cited exponential and Gaussian routines.", "direct"),
              ("B_0", "compression map", "The contraction $\\mathsf D'\\mathsf J'C:\\mathbb C^t\\to\\mathbb C^s$ built from selection and a Neumann series.", "direct")],
        children=[
            infer("The condition is $\\theta=t/s-1>p/\\alpha^4$ for integers $p>100$, $2\\le s<t<2^p$, $2\\le\\alpha<\\sqrt p$ and $\\gcd(s,t)=1$.",
                  r"\theta:=t/s-1>p/\alpha^4."),
            infer("The two coordinate permutations are $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$.",
                  r"(P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}."),
            infer("The claimed identity is $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$ for linear contractions $A,B_0$.",
                  r"P_sF_s=2^{2\alpha^2}B_0P_tF_tA."),
            infer("The Gaussian identity $\\mathsf TP_sF_s=P_tF_t\\mathsf S$ holds exactly for the Gaussian resampling maps $\\mathsf S,\\mathsf T$.",
                  r"\mathsf T P_sF_s=P_tF_t\mathsf S,"),
            infer("With $N=C\\mathsf T\\mathsf D$ the error satisfies $\\|N-I\\|<2.01e^{-\\pi\\alpha^2\\theta/2}<2^{-\\alpha^2\\theta}$.",
                  r"\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}."),
            infer("Since $\\alpha^2\\theta>p/\\alpha^2>1$ we get $\\|N-I\\|<1/2$ and $N$ is invertible by the Neumann series.",
                  r"Thus $\|N-I\|<1/2$, so $N$ is invertible"),
            infer("After the rescalings $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$, the norms are below $3/4$, $7/8$, $1$.",
                  r"\|\mathsf S'\|<\frac34,\qquad"),
            infer("Using the left inverse $\\mathsf DN^{-1}C$ of $\\mathsf T$, the product of normalizations is $2^{-(2\\alpha^2-2)}2^{-1}2^{-1}=2^{-2\\alpha^2}$, giving $B_0P_tF_tA=2^{-2\\alpha^2}P_sF_s$.",
                  r"=2^{-2\alpha^2}P_sF_s,"),
            infer("The ordered numerical maps have errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\\delta}\\alpha)$, $O(tp^{3/2+\\delta}\\alpha)$, $O(tp^{1+\\delta})$.",
                  r"\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)"),
            infer("The selection $C$ takes an ordered subsequence because $t/s>1$, copying a record exactly when the running coordinate equals the next $q_j$, with zero numerical error.",
                  r"because $t/s>1$. Thus $C$ selects an ordered subsequence."),
            infer("The original algorithm implemented the two permutations by two label-and-sort operations each costing $O(tp\\log t)$; in the identity here they are not executed.",
                  r"The original proof of Proposition~4.7(ii) implements"),
        ])


def TEN():
    return show(
        "Tensoring the one-dimensional identity over $d$ axes gives $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$, implemented line by line on the padded box in time $O(dTp^{3/2+\\delta}\\alpha)$ plus $O(Tp\\,d^2(1+\\ell^\\tau))$ for exposing and restoring the axes.",
        "Tensor the identity, expand the axes one at a time inside the padded power-of-two box with zero lines outside the valid ranges, and move each axis next to the line machine by fast chunk interchanges.",
        "The one-dimensional lemma works on one coordinate line at a time, so the algorithm must expose each axis of the box as the innermost field, which is where the fast interchange enters.",
        "recoverable",
        frm=["gaussian-resampling", "address-chunk-interchange", "multidimensional-dft"],
        adds=[("\\gamma", "scale exponent", "The total scale $2d\\alpha^2$, the exponent of the power of two removed from the tensor identity.", "direct")],
        children=[
            infer("The tensor identity is $RF_{\\boldsymbol s}=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A$ with $\\gamma=2d\\alpha^2$ and $R,Q$ tensor products of the $P_{s_i},P_{t_i}$.",
                  r"=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A,"),
            infer("The total time in the one-dimensional algorithms is $O(dTp^{3/2+\\delta}\\alpha)$ since at most $T/t_i$ lines are processed for axis $i$.",
                  r"with a constant independent of $d$."),
            infer("Exposing and restoring all the lines costs $O(Tp\\,d^2(1+\\ell^\\tau))$ via $O(d^2)$ adjacent axis interchanges.",
                  r"then exposing and restoring all the lines costs"),
            infer("Composing $d$ axis maps, each with error below $p^2$, gives error less than $dp^2$.",
                  r"Composing the $d$ axis maps gives error less than $dp^2$."),
        ])


def BC():
    return show(
        "For even $t_i$ and $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$, which has period $t_i$ in coordinate $i$, the permuted transform is a chirp-weighted convolution: $QF_{\\boldsymbol t}u=\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
        "Expand the right side: the coefficient of $u_{\\boldsymbol k}$ is $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}$, and $-(j-k)^2+j^2+k^2=2jk$ turns the product of chirps into the Fourier kernel.",
        "The factor $QF_{\\boldsymbol t}$ is a Fourier transform composed with a permutation of frequencies; a chirp identity expresses this as one cyclic convolution and two pointwise phase products, avoiding the permutation.",
        "explicit",
        mq=r"computed from a cyclic convolution and two pointwise phase",
        page="bluestein-chirp",
        frm=["dft", "multidimensional-dft", "cyclic-convolution", "complex-numbers"],
        adds=[("a", "chirp array", "The array $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_ij_i^2/t_i)$ of unit complex numbers, periodic in each coordinate.", "direct")],
        children=[
            infer("The identity is $QF_{\\boldsymbol t}u=\\overline a\\cdot\\frac{a*(\\overline a\\cdot u)}{T}$.",
                  r"\frac{a*(\overline a\mathbin{\cdot}u)}{T}."),
            infer("Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by $-\\pi is_i(2j_i+t_i)$, an integral multiple of $2\\pi i$, so $a$ is periodic.",
                  r"Replacing $j_i$ by $j_i+t_i$ changes the exponent defining $a$ by"),
            infer("The coefficient of $u_{\\boldsymbol k}$ on the right side equals $\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$, which is the coefficient of $QF_{\\boldsymbol t}$ because $Q$ reads frequency $-s_ij_i$ from the negative-sign transform.",
                  r"This is precisely the coefficient in $QF_{\boldsymbol t}$, because"),
        ])


def PCh():
    return show(
        "The source permutation $R$ cancels: $RF_{\\boldsymbol s}^+[(RF_{\\boldsymbol s}u)\\cdot(RF_{\\boldsymbol s}v)]=(u*v)/S^2$ for $S=\\prod_is_i$, so the source permutation never has to be executed.",
        "Show that dilation by a unit commutes through the opposite Fourier sum as $F^+R=R^{-1}F^+$, hence $RF^+R=F^+$, commute $R$ with the pointwise product, and finish with the convolution theorem $F(u*v)=S(Fu)(Fv)$ and $F^+F=I/S$.",
        "Because each $t_i$ is a unit modulo $s_i$, the source permutation is a dilation, and dilations transform simply under Fourier transforms; one forward-forward-inverse sandwich cancels it.",
        "recoverable",
        page="permutation-cancellation",
        frm=["bluestein-chirp", "gaussian-resampling", "dft", "multidimensional-dft", "cyclic-convolution", "modular-arithmetic"],
        salient="The nontrivial permutation $R$ disappears entirely: it is applied after each of the two forward transforms and again after the opposite one, and these three occurrences cancel each other.",
        children=[
            infer("For a unit $c$ modulo $q$ and $(R_cz)_j=z_{cj}$, substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$.",
                  r"For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$"),
            infer("Tensoring over axes gives $F_{\\boldsymbol s}^+R=R^{-1}F_{\\boldsymbol s}^+$ and hence $RF^+_{\\boldsymbol s}R=F^+_{\\boldsymbol s}$.",
                  r"$F_{\boldsymbol s}^+R=R^{-1}F_{\boldsymbol s}^+$ and hence"),
            infer("A coordinate permutation commutes with pointwise products, so $(RFu)\\cdot(RFv)=R(Fu\\cdot Fv)$.",
                  r"because a coordinate permutation commutes with pointwise products."),
            infer("The normalized convolution rule is $F(u*v)=S\\,(Fu)\\cdot(Fv)$ and $F^+F=I/S$.",
                  r"$F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot}"),
            infer("Hence $F^+_{\\boldsymbol s}(Fu\\cdot Fv)=\\frac1SF^+F(u*v)=(u*v)/S^2$.",
                  r"=\frac{u*v}{S^2},"),
        ])
