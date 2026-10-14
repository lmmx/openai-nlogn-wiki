from lib import *
from resample import GR, TEN, BC, PCh


def RDC():
    return show(
        "Writing each input as a polynomial in $2^b$ with $q=\\lceil n/b\\rceil$ digits, the integer product is the polynomial product, of degree $2q-2<S$ so that convolution modulo $x^S-1$ has no wraparound, and each product coefficient lies in $[0,2^{3b})$.",
        "Bound the degree of the product by the padded box size and bound each coefficient by the number of terms times the squared digit bound.",
        "A cyclic convolution of length $S$ equals the ordinary polynomial product exactly when the product has degree below $S$, and carries can be recovered when each coefficient has a known bound.",
        "recoverable",
        page="radix-digit-convolution",
        frm=["polynomials", "cyclic-convolution", "floor-ceiling-and-summation-notation", "binary-representation-and-bit-operations"],
        children=[
            infer("Write the two inputs as polynomials in $2^b$, each with $q=\\lceil n/b\\rceil$ nonnegative digits.",
                  r"Write the two inputs as polynomials in $2^b$, each with"),
            infer("The product has degree at most $2q-2<2n/b\\le T/2<S$.",
                  r"2q-2<2n/b\le T/2<S."),
            infer("Hence convolution modulo $x^S-1$ has no nonzero wraparound.",
                  r"Thus convolution modulo $x^S-1$ has no nonzero wraparound."),
            infer("Every product coefficient obeys $0\\le c_j\\le q(2^b-1)^2<2^{3b}$, since $q\\le n\\le2^b$.",
                  r"0\le c_j\le q(2^b-1)^2<2^{3b},"),
        ])


def PAR():
    primes = show(
        "Distinct odd primes $s_i$ with $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ exist and satisfy $T/2<S<T$ and $\\alpha^4\\theta_i>p$, and they are found deterministically in $n^{o(1)}$ time.",
        "Apply the explicit prime-interval bound of Rosser and Schoenfeld to the two intervals below $r/2$ and $r$, multiply the lower bounds using Bernoulli's inequality, and search by trial division.",
        "Resampling needs $t_i/s_i>1+p/\\alpha^4$ while the CRT box must keep a fixed fraction of the power-of-two box; primes in a window just below $t_i$ meet both needs, and a window of relative width $\\eta=1/(4d)$ is wide enough to contain more than $d$ primes.",
        "explicit",
        mq=r"while each ratio $t_i/s_i$ must leave enough separation for resampling.",
        children=[
            infer("For $0<\\eta<1/4$ and $x>e^{2/\\eta}$ the interval $(1-2\\eta)x<q\\le(1-\\eta)x$ contains at least $\\eta x/(2\\log x)$ primes, which here exceeds $d$ for $x=r/2$ and $x=r$.",
                  r"contains at least $\eta x/(2\log x)$ primes."),
            infer("The two intervals are disjoint, so distinct odd primes can be chosen.",
                  r"We may therefore choose distinct odd primes satisfying"),
            infer("The primes satisfy $(1-2\\eta)t_i<s_i\\le(1-\\eta)t_i$ with $\\eta=1/(4d)$.",
                  r"(1-2\eta)t_i<s_i\leq(1-\eta)t_i."),
            infer("By strict Bernoulli, $S/T>(1-\\frac1{2d})^d>\\frac12$, and with $s_i<t_i$ this gives $T/2<S<T$.",
                  r"Together with $s_i<t_i$, this gives $T/2<S<T$."),
            infer("Since $\\theta_i\\ge\\eta/(1-\\eta)>\\eta$ and $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, we get $\\alpha^4\\theta_i>\\frac{12d^2b}{4d}=3db\\ge6b=p$, the hypothesis of the resampling lemma.",
                  r"\alpha^4\theta_i>\frac{12d^2b}{4d}=3db\geq6b=p."),
            infer("Trial division over both intervals takes $O(dr^{3/2}\\mathrm{poly}(p))$ time, whose logarithm is $o(p)$, so the search takes $n^{o(1)}=o(n)$ time.",
                  r"Since $p=6\lceil\log_2 n\rceil=\Theta(\log n)$, the search takes"),
        ])
    return show(
        "The size parameters $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$, a power of two $T\\in[4n/b,8n/b)$, axis lengths $t_i\\in\\{r/2,r\\}$ and distinct primes $s_i$ just below $t_i$ with $T/2<S<T$ satisfy all hypotheses of the resampling, layer and transform lemmas for large $n$.",
        "Fix the rational exponents and constants, choose the integer sizes from $n$, check the comparison bands $a_d,b_d,a_r,b_r$ used by the layer and transform interfaces, and then pick the prime source lengths.",
        "Each tape lemma has hypotheses that interlock (precision against axes, record length against polynomial overhead, prime gap against Gaussian width), so a single compatible choice of parameters must be exhibited and checked once.",
        "reconstructed",
        page="parameter-choice",
        frm=["crt-address-map", "gaussian-resampling", "radix-digit-convolution", "polynomial-ring-mod", "primes-coprimality-and-gcd", "logarithms-and-iterated-logarithm-notation", "floor-ceiling-and-summation-notation"],
        adds=[("\\eta", "prime window", "The relative window width $1/(4d)$ for the interval containing each prime.", "direct"),
              ("\\gamma", "scale exponent", "The value $2d\\alpha^2$ of the total power of two in the tensor identity.", "direct"),
              ("\\alpha", "Gaussian width", "The width parameter $\\lceil(12d^2b)^{1/4}\\rceil$ used by every Gaussian resampling map.", "direct")],
        salient="The exponents are astronomically small ($\\epsilon=2^{-75}$, $c=2^{-56}$), chosen only so that every tape lemma applies at once; no optimisation is claimed.",
        children=[
            infer("Fixed rational exponents: $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$, $\\delta=1/16$.",
                  r"\tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},"),
            infer("Further constants: $\\lambda=1-2^{-52}$, $c=2^{-56}$, $\\lambda'=1-2^{-54}$.",
                  r"\lambda=1-2^{-52},\qquad c=2^{-56},\qquad"),
            infer("Finally $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$; the constants are deliberately conservative.",
                  r"C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}."),
            infer("For large $n$: $b=\\lceil\\log_2n\\rceil$, $p=6b$, $d=\\lfloor b^\\epsilon\\rfloor$, $K=\\lfloor d^c\\rfloor$.",
                  r"b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor,"),
            infer("Take the power of two $T$ in $[4n/b,8n/b)$, $r=2^{\\lceil(\\log_2T)/d\\rceil}$, $\\ell=\\log_2r$, and choose $d\\ell-\\log_2T$ of the axis lengths to be $r/2$ and the rest $r$, with $t_d=r$.",
                  r"Take the power of two $T$ in $[4n/b,8n/b)$, and let"),
            infer("The sizes satisfy $Tp=\\Theta(n)$, $d=\\Theta(p^\\epsilon)$, $K=\\Theta(p^{\\epsilon c})$, $\\ell=\\Theta(p^{1-\\epsilon})$ and $r=2^{\\Theta(p^{1-\\epsilon})}$, with comparison constants $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$.",
                  r"Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad"),
            infer("The Gaussian width is $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$, with $\\gamma=2d\\alpha^2<28d^2\\sqrt b\\le28b^{2/3}=o(b)$.",
                  r"\alpha=\left\lceil(12d^2b)^{1/4}\right\rceil,"),
            primes,
            RDC(),
        ])
