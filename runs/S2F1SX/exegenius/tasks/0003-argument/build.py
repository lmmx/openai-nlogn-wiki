import json
from lib import *
from part1 import S1
from part2 import S2
from part3 import layout, ring_conv
from part4 import resampling, chirp, cancel
from part5 import S9

root = show(
    "S0",
    r"There is one deterministic fixed-alphabet, fixed-tape Turing machine that multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in this model.",
    "Reduce the product to a convolution evaluated by Fourier-type transforms over a polynomial ring, speed up the transforms' address movement and butterfly arithmetic with two recursive tape procedures that each save a power of the width, then assemble the reduction and balance the parameters so that every cost row stays a power below $\\log n$.",
    ("explicit", "Scanning the data at each of the logarithmically many transform levels already costs $n\\log n$, so both movement and arithmetic must be made cheaper.",
     r"We therefore need savings in both movement and arithmetic."),
    [S1, S2, layout, ring_conv, resampling, chirp, cancel, S9],
    page="main-theorem",
    frm=["fixed-tape-model", "nlogn-conjecture", "nlogn-multiplier", "big-o", "asymptotic-notation-beyond-big-o", "determinism-and-exact-versus-approximate-computation"],
    adds=[
        sym("p", "working precision", "The number of fractional bits kept for each real or imaginary component of a stored complex value; $p=6\\lceil\\log_2n\\rceil$.", "count"),
        sym("d", "axis count", "The number of axes of the multidimensional transform, equal to $\\lfloor b^\\epsilon\\rfloor$ and so a small power of $p$.", "count"),
        sym("K", "chunk width", "The number of bits in each address chunk that a simultaneous butterfly layer treats at once.", "count"),
        sym("T", "box size", "The number of entries of the padded power-of-two box on which the transforms act, the product of the axis lengths.", "count"),
        sym("\\ell", "log ring dimension", "The base-two logarithm of the ring dimension $r$.", "direct"),
        sym("M", "record count", "The number of polynomial records, equal to $T/r$, when the last axis is stored as the coefficient list of a ring element.", "count"),
        sym("s_i", "prime length", "The distinct odd prime length of the source axis $i$, chosen just below $t_i$.", "direct"),
        sym("t_i", "padded axis length", "The power-of-two length of axis $i$ of the padded box, equal to $r/2$ or $r$.", "direct"),
        sym("\\epsilon", "axis exponent", "The tiny fixed exponent $2^{-75}$ with $d=\\Theta(p^\\epsilon)$.", "direct"),
        sym("c", "chunk exponent", "The tiny fixed exponent $2^{-56}$ with $K=\\lfloor d^c\\rfloor$.", "direct"),
    ],
)
ans = {"root": root}
s = json.dumps(ans, ensure_ascii=False)
for bad in ['\r', '\x0c', '\t', '\x08', '\x07', '\x0b']:
    assert bad not in s, repr(bad)
json.dump(ans, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1SX/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
print("written")
