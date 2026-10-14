import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F6Y/exegenius/tasks/0003-argument')
from lib import *
from part_key import S2
from part_rest import S1, S3, S4
from part_end import S5, S6, S7, S8, S9, S10

ROOT = sh(
    "S0",
    r"A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture.",
    "Reduce the product to a convolution over $\\mathbb C[y]/(y^r+1)$ (radix digits, Chinese-remainder address map, Gaussian resampling with chirps, coefficient twist), evaluate the transforms with two tape procedures that come from one rank-saving linear network, then recover the exact product and add up the costs.",
    mot("Scanning an array of $\\Theta(n)$ stored bits at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so savings are needed both in the movement of data and in the arithmetic.",
        "explicit", "We therefore need savings in both movement and arithmetic."),
    [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10],
    page="multiplication-below-nlogn",
    frm=["big-o", "turing-machines", "polynomial-time-and-computational-cost-on-tapes", "hvdh-multiplier", "negacyclic-ring", "discrete-fourier-transform", "radix-two-fft", "fast-fourier-transform-as-a-known-algorithm"],
    adds=[
        ad("n", "input length", "The number of bits of each of the two integers to be multiplied.", "count"),
        ad("\\kappa", "saving exponent", "The fixed exponent $\\kappa=2^{-182}$ by which the logarithmic factor of the running time is reduced."),
    ],
    salient="The saving is a genuine power of the logarithm, $(\\lg n)^{-\\kappa}$ with $\\kappa=2^{-182}$, which is astronomically small yet fixed, so the running time divided by $n\\lg n$ tends to zero.",
)
problems = check(ROOT)
out = {"root": ROOT}
json.dump(out, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F6Y/exegenius/tasks/0003-argument.answer.json', 'w'), indent=1, ensure_ascii=False)
print("written")
