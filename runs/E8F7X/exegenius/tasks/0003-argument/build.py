import sys, json
sys.path.insert(0, '.')
from lib import *
from tree1 import *
from tree2 import *
from tree3 import *
from tree4 import *
from tree5 import *
from tree6 import *

GA = show(
    r"Address-chunk interchange of $u$-bit fields costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.",
    "Prove both from one construction: elementary linear-time stream scans, one fixed linear network whose edge changes are smaller calls with total $s<Wm$, then specialise it to the bit network (address interchange) and to the complex network (butterfly layer).",
    mot("Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.", "explicit",
        (120, r"Each procedure arises from its own fixed linear network that exchanges two", r"restores every auxiliary")),
    [
        stream_ops(),
        controlled_shifts(),
        show(
            r"Each tape procedure recurses on a fixed linear network of $W$ wires whose edge changes cost smaller calls totalling $s<Wm$, so a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ and the normalized cost grows only like the parameter to a power $\tau<1$.",
            "Build a network that exchanges two banks and restores scratch, give its wires frames and nested subspace labels so that every edge is a few smaller calls, and count the calls: their total rank is below $Wm$.",
            mot("After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$; this strict inequality is the source of the power saving.",
                "explicit", (173, r"After dividing cost by volume, multiplying the parameter by $m$", r"is the source of the power saving.")),
            [
                xor_network(),
                frames(),
                subset_labels(),
                rank_deficit(),
                infer(r"A recursive call at parameter $mf$ uses $s$ calls at parameter $f$, each on a stream of volume $V/W$, so after dividing by volume the recursive contribution is multiplied by $s/W<m$.",
                      170, r"A recursive call at parameter $mf$ therefore uses $s$ calls at parameter", r"each on a stream of volume $V/W$.", deferred=True),
            ],
            page="power-saving-recurrence",
            frm=["xor-linear-network", "frames", "subset-labels", "rank-deficit", "recursion-and-divide-and-conquer-recurrences"],
            adds=[bind(r"W", "wire count", "the number of wires of the fixed network, each carrying one role stream", "count"),
                  bind(r"m", "label dimension", "the dimension of the fixed label space, the number of fields in each address vector", "count"),
                  bind(r"s", "call count", "the total rank of all edge differences, which is the number of smaller calls made by one call", "count"),
                  bind(r"N", "bank size", "the number of entries in each of the two data banks, $N=\\binom{100}{3}^3$", "count"),
                  bind(r"L", "lost dimension", "the total label dimension lost on decreasing edges", "count")],
            salient="The saving is real but astronomically small: the rank deficit is positive yet only a fraction of order $10^{-11}$ of $Wm$, so the exponent $\\tau$ is $1-2^{-50}$."),
        arbitrary_width(),
        butterfly_layer(),
    ],
    frm=["fixed-tape-model"])

GC = show(
    r"A Fourier transform of pairwise coprime lengths $s_i$ is computed through power-of-two-length transforms: Gaussian resampling gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, Bluestein's chirp turns $QF_{\boldsymbol t}$ into a cyclic convolution, and the retained permutation $R$ cancels across two forward transforms and one opposite transform.",
    "Prove the three identities separately (one-dimensional resampling, its tensor form on a padded box, the chirp identity) and then the cancellation of the retained permutation, so that no full sort is ever executed.",
    mot("The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two; Gaussian resampling connects these two shapes.", "explicit",
        (3499, r"The transform lengths needed for the integer product are pairwise coprime,", r"connects these two shapes.")),
    [gaussian_resampling(), tensor_resampling(), bluestein(), perm_cancel()],
    frm=["dft", "cyclic-convolution", "multidimensional-dft"],
    adds=[bind(r"\alpha", "Gaussian width", "the integer parameter controlling the width of the Gaussian weights in resampling", "direct"),
          bind(r"\gamma", "power-of-two exponent", "the exponent $2d\\alpha^2$ of the power of two separating the two sides of the resampling identity", "direct"),
          bind(r"R", "source permutation", "the dilation permutation of the source coordinates that is left inside the transform", "direct"),
          bind(r"Q", "target permutation", "the dilation permutation of the target frequencies absorbed by the chirp identity", "direct")])

GD = show(
    r"Placing the radix-digit coefficients on prime cyclic axes, resampling and chirping them into a convolution over $\mathbb C[y]/(y^r+1)$, then rescaling, rounding and carrying produces the exact $2n$-bit product.",
    "Follow the chain of reductions: integer product, radix-digit convolution, cyclic convolution on distinct prime axes, normalized convolution on power-of-two axes, convolution over the polynomial ring; then undo the known scales, round and carry.",
    mot("The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation.", "explicit",
        (183, r"The remaining proof places these procedures inside the multiplication reduction", r"accounts for every change of representation.")),
    [prime_axes(), radix_digits(), crt_map(), phase_twist(), source_transform(), mult_algorithm()],
    frm=["schoolbook-integer-arithmetic"],
    adds=[bind(r"\alpha", "Gaussian width", "the integer $\\lceil(12d^2b)^{1/4}\\rceil$ fixing the Gaussian width of resampling", "direct"),
          bind(r"\gamma", "scale exponent", "the exponent $2d\\alpha^2$ of the power-of-two scale of the source transform", "direct"),
          bind(r"S", "prime product", "the product of the distinct prime axis lengths $s_i$, with $T/2<S<T$", "direct"),
          bind(r"t_i", "axis length", "the length of the $i$-th power-of-two axis, equal to $r/2$ or $r$", "direct"),
          bind(r"s_i", "prime length", "the prime just below $t_i$ used as the $i$-th source axis length", "direct"),
          bind(r"\ell", "axis bits", "the base-2 logarithm of $r$", "direct")])

root = show(
    r"One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.",
    "Build the multiplier bottom-up: first the two power-saving tape procedures, then a convolution over a polynomial ring made from them, then the Gaussian-resampling and Bluestein reductions, then assemble the algorithm and add up its costs.",
    mot("Scanning an array of $\\Theta(n)$ bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed in both address movement and arithmetic.", "explicit",
        (90, r"Scanning an array of $\Theta(n)$ stored bits at each of", r"We therefore need savings in both movement and arithmetic.")),
    [GA, synth_convolution(), GC, GD, cost_accounting()],
    page="main-theorem",
    frm=["nlogn-history", "fixed-tape-model", "established-multiplier", "big-o", "asymptotic-notation-beyond-big-o", "schoolbook-integer-arithmetic"],
    adds=[bind(r"n", "input length", "the number of bits of each factor", "count"),
          bind(r"b", "digit width", "the number of bits in one radix digit, $\\lceil\\log_2n\\rceil$", "count"),
          bind(r"p", "precision", "the number of fractional bits kept in every stored complex coefficient, $6b$", "count"),
          bind(r"d", "axis count", "the number of axes of the padded box, also the maximum number of chunks in a butterfly layer", "count"),
          bind(r"r", "record length", "the number of complex coefficients in a polynomial record", "count"),
          bind(r"K", "chunk width", "the number of address bits in one chunk, $\\lfloor d^c\\rfloor$", "count"),
          bind(r"T", "box size", "the number of entries of the padded box, the product of the axis lengths", "count")],
    salient="The saving is a power of the logarithm, $(\\lg n)^{-\\kappa}$ with $\\kappa=2^{-182}$: tiny, but it breaks the long-standing $n\\log n$ barrier because it comes from beating the per-level cost of both address movement and butterflies.")

probs = list(ERRS) + validate(root)
for p in probs:
    print("PROBLEM:", p)
if probs:
    sys.exit(1)
out = {"root": to_json(root, "S0")}
json.dump(out, open("../0003-argument.answer.json", "w"), indent=1, ensure_ascii=False)
print("ok; nodes:", len(walk(root)))
