import sys, json
sys.path.insert(0,'/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F5Y/exegenius/tasks/0003-argument')
from lib import *
import part1, part2, part3, part4, part5
root = sh("S0",
  "A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in time $O(n(\\lg n)^{1-\\kappa})$ with $\\kappa=2^{-182}$.",
  "Reduce the product to a cyclic convolution of radix-digit polynomials, evaluate it by Fourier transforms made cheap with Gaussian resampling, Bluestein chirps and synthetic polynomial transforms over $\\mathbb C[y]/(y^r+1)$, and speed up the two bottlenecks of that evaluation, address rearrangement and butterfly layers, with two linear-network tape procedures that each save a power of the width; then verify exactness and total the costs.",
  "A transform of $\\Theta(n)$ stored bits with $\\Theta(\\log n)$ levels already costs $\\Theta(n\\log n)$ just to scan, so a power saving in the logarithmic factor needs a saving in the cost of moving data between layouts and in the cost of the butterfly arithmetic.",
  "explicit",
  [*part1.s1(), part1.s2(), part2.s3(), part2.s4(), part3.s5(), part3.s6(), part4.s7(), part5.s8(), part5.s9()],
  mquote="We therefore need savings in both movement and arithmetic.",
  page="main-theorem",
  frm=["nlogn-conjecture", "big-o", "turing-machine-basics"],
  adds=[B("n", "input length", "The number of bits of each of the two integers to be multiplied.", "count"),
        B("\\kappa", "saving exponent", "The fixed constant $2^{-182}$ such that the running time is $O(n(\\lg n)^{1-\\kappa})$.", "direct")],
  salient="The saving is a genuine power $(\\lg n)^{-\\kappa}$ of the logarithmic factor, but with $\\kappa=2^{-182}$ it is astronomically small; it comes entirely from one strict inequality, the total edge rank $s<Wm$ of two fixed linear networks.")
bad, pages = verify(root)
json.dump({"root": root}, open('/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F5Y/exegenius/tasks/0003-argument.answer.json','w'), indent=1)
print("bad", bad)
