import sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F3Y/exegenius/tasks/0003-argument')
from lib import *
import part1, part2, part3, part4, part5, part6

OUT = '/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F3Y/exegenius/tasks/0003-argument.answer.json'

PAGES = """schonhage-strassen-conjecture hh-multiplier tape-stream-operations controlled-shift exchange-network frames subspace-labels rank-saving matrix-factorization matrix-shear power-width-interchange chunk-interchange packed-selected-bit-addition negacyclic-ring kronecker-packing contraction-error guard-bits cyclic-convolution radix-digit-convolution phase-twist exact-recovery dft fft-butterfly chirp-identity phase-frames simultaneous-butterfly-layer multidimensional-transform synthetic-transform bit-reversed-order transform-layout ring-convolution gaussian-resampling permutation-cancellation crt-axis-map prime-axis-lengths parameter-choice multiplication-algorithm time-bound main-theorem""".split()
CONCEPTS = """big-o-notation polynomials complex-numbers multitape-turing-machine asymptotic-notation-beyond-big-o limits-and-limit-inferior logarithms-exponentials-floors-and-ceilings recurrences-and-geometric-sums positional-number-systems-and-carries schoolbook-and-karatsuba-multiplication bitwise-operations-and-xor modular-arithmetic primes-coprimality-and-the-extended-euclidean-algorithm roots-of-unity matrices-and-linear-maps vector-spaces-subspaces-dimension-and-rank inner-products-bilinear-forms-and-orthogonal-complements gaussian-elimination-and-triangular-matrices permutations-bijections-and-permutation-matrices arithmetic-modulo-2-and-linear-algebra-over-f-2 finite-sets-subsets-and-counting circuits-and-directed-acyclic-graphs vector-norms-and-the-triangle-inequality fixed-point-numbers-dyadic-rationals-and-rounding row-major-order-and-matrix-transposition subroutines-and-reductions-between-problems convolution-of-sequences""".split()
PIDX = {p: i for i, p in enumerate(PAGES)}


def find(root, id):
    if root['id'] == id:
        return root
    for c in root.get('children', []):
        r = find(c, id)
        if r:
            return r
    return None


# ---- S1 assembly
S1 = show(
    "S1",
    r"Two recursive tape procedures cost a strict power less than a full pass per level: interchanging two $u$-bit address chunks costs $O(Vu^{\tau})$, and applying the butterfly $H_0$ to one selected bit in each of up to $d$ address chunks costs $O(Vd^{\lambda'})$, for fixed $\tau,\lambda'<1$.",
    r"Exchange two banks of values by a fixed linear network of $W$ wires, give each wire's array a frame so that every edge becomes a smaller call of the same procedure, show that the total number $s$ of smaller calls is less than $Wm$, and unroll the recursion $F(mf)\le(s/W)F(f)+\text{overhead}$ for the bit network (address interchange) and for the complex network (butterfly layer).",
    mot("Multiplying the parameter by $m$ multiplies the recursive contribution by $s/W<m$; this strict inequality is the source of the power saving.", "explicit",
        r"is the source of the power saving."),
    [part1.s11, part1.s12, part1.s13, part1.s14, part2.s15, part3.s16],
    adds=[
        add(r"V", "bit volume", "The number of stored data bits of the array an operation acts on, the logical volume used to normalize costs.", "count"),
        add(r"W", "wire count", "The number of wires (roles) of the fixed network, $W_{\\rm b}$ or $W_{\\rm c}$ for the bit or complex network.", "count"),
        add(r"m", "label dimension", "The dimension $h^3=10^6$ of the fixed bilinear label space; one recursion level multiplies the parameter by $m$.", "count"),
        add(r"s", "smaller calls", "The total number of smaller calls (sum of the ranks of all edge changes) one invocation of the network makes.", "count"),
        add(r"u", "chunk bit width", "The number of bits of each of the two address chunks being interchanged.", "count"),
    ],
    frm=["recurrences-and-geometric-sums", "vector-spaces-subspaces-dimension-and-rank", "circuits-and-directed-acyclic-graphs", "tape-stream-operations", "controlled-shift", "bitwise-operations-and-xor"],
    salient=r"The saving rests on a single strict inequality, $s<Wm$: the total number of smaller calls is less than the number of wires times the label dimension, by a relative margin of only about $1.5\times10^{-11}$ for the bit network; every later exponent $\tau,\lambda'$ is only barely below one because of it.")

root_children = [S1, part4.r2, part5.s3, part5.s4, part6.s5, part6.s6, part6.s7]

ROOT = show(
    "S0",
    r"A single deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, which refutes the $n\log n$ optimality conjecture of Schönhage and Strassen in this model.".replace(r"ö", "ö"),
    r"Save a power of the logarithmic factor in both address movement and Fourier arithmetic: build two recursive tape procedures that exploit a strict rank deficit, use them to run synthetic transforms over $\mathbb C[y]/(y^r+1)$, embed the radix-digit convolution into that ring by a Chinese-remainder map, Gaussian resampling, a chirp convolution and a phase twist, recover the exact product by rounding and carries, and add up the cost table.",
    mot("Scanning an array at each of $\\Theta(\\log n)$ transform levels already costs $\\Theta(n\\log n)$, so a power saving needs savings in both movement and arithmetic.", "explicit",
        r"We therefore need savings in both movement and arithmetic."),
    root_children,
    page="main-theorem",
    frm=["schonhage-strassen-conjecture", "hh-multiplier", "big-o-notation", "asymptotic-notation-beyond-big-o", "multitape-turing-machine", "logarithms-exponentials-floors-and-ceilings", "schoolbook-and-karatsuba-multiplication", "limits-and-limit-inferior", "time-bound", "multiplication-algorithm"],
    adds=[
        add(r"n", "input length", "The number of bits of each of the two operands.", "count"),
        add(r"\kappa", "saving exponent", "The exponent $2^{-182}$ by which the logarithmic factor is reduced in the running time $O(n(\\lg n)^{1-\\kappa})$.", "direct"),
        add(r"p", "precision", "The number of fractional bits of the fixed-point grid $2^{-p}\\mathbb Z[i]$ of the complex coefficients; the algorithm takes $p=6\\lceil\\log_2n\\rceil$.", "count"),
        add(r"d", "number of axes", "The number of axes (address chunks) of the transform array, $d=\\Theta(p^\\epsilon)$; the algorithm takes $d=\\lfloor b^\\epsilon\\rfloor$.", "count"),
        add(r"K", "chunk width", "The width $\\lfloor d^c\\rfloor$ in bits of an address chunk.", "count"),
        add(r"r", "record length", "The number of complex coefficients of a polynomial record in $\\mathbb C[y]/(y^r+1)$, a power of two $2^\\ell$ with $r=2^{\\Theta(p/d)}$.", "count"),
        add(r"\ell", "log record length", "The integer $\\log_2r$.", "count"),
        add(r"T", "entry count", "The number of complex coefficients in the padded transform array, a power of two in $[4n/b,8n/b)$ for the algorithm, so that the logical bit volume is $\\Theta(Tp)=\\Theta(n)$.", "count"),
        add(r"\tau", "interchange exponent", "The fixed exponent $1-2^{-50}$ in the cost $O(Vu^\\tau)$ of the address interchange.", "direct"),
        add(r"\sigma", "complex recurrence exponent", "A rational upper bound for the logarithmic exponent of the complex recurrence, $\\sigma=1-2^{-50}$.", "direct"),
        add(r"\lambda", "overhead exponent", "A fixed exponent with $\\max\\{\\tau,\\sigma\\}<\\lambda<1$ and $\\tau(1+c/\\beta)<\\lambda$; the parameter choice fixes $\\lambda=1-2^{-52}$.", "direct"),
        add(r"\lambda'", "layer exponent", "The fixed exponent in the cost $O(Vd^{\\lambda'})$ of the simultaneous butterfly layer, with $\\max\\{\\lambda,\\sigma+\\beta(1-\\sigma)\\}<\\lambda'<1$; the parameter choice fixes $\\lambda'=1-2^{-54}$.", "direct"),
        add(r"\beta", "stopping exponent", "The fixed exponent $1/2$ at which the layer recursion stops, when fewer than $d^\\beta$ chunks remain.", "direct"),
        add(r"\delta", "multiplier exponent", "The fixed exponent $1/16$, below $1/8$, in the cost $O(N^{1+\\delta})$-type routines for exponentials and Gaussian line maps.", "direct"),
        add(r"c", "chunk exponent", "The fixed rational exponent $2^{-56}$ in $K=\\lfloor d^c\\rfloor$.", "direct"),
        add(r"\epsilon", "axis exponent", "The fixed rational exponent $2^{-75}$ in $d=\\Theta(p^\\epsilon)$.", "direct"),
        add(r"C_1", "guard exponent", "The fixed exponent $20$ in the guard width $\\Delta=\\lceil C_0d^{C_1}\\rceil$ of the exact layer evaluation.", "count"),
    ],
    salient=r"The exponent $\kappa=2^{-182}$ is astronomically small but strictly positive: the log factor is reduced by a genuine power of $\lg n$, not merely by an iterated-logarithm factor, and the algorithm is still an ordinary deterministic fixed-tape machine.")

# ---- edits to avoid duplicate / out-of-scope adds
def drop(node, symbols):
    n = find(ROOT, node)
    n['adds'] = [a for a in n.get('adds', []) if a['symbol'] not in symbols]
    if not n['adds']:
        del n['adds']


drop("S1.4", [r"\sigma"])
drop("S1.6", ["K", "p", "r", "c", r"\epsilon", r"\lambda", r"\beta"])
drop("S1.6.2", ["K"])
drop("S1.6.4", ["C_1"])
drop("S2", [])
drop("S3.1", [r"\delta"])
drop("S3.2", ["R", "Q", r"\gamma"])
drop("S3.4", ["S"])
drop("S2.2", ["M"])
drop("S2.3", ["T", r"\ell"])
n = find(ROOT, "S2")
n['adds'].append(add("M", "cyclic address count", "The product $\\prod_it_i$ of the axis lengths, the number of ring records in an array, so $T=rM$.", "count"))
n = find(ROOT, "S3")
n['adds'] = [
    add("R", "source permutation tensor", "The tensor product $\\bigotimes_iP_{s_i}$ of the source coordinate permutations.", "direct"),
    add("Q", "target permutation tensor", "The tensor product $\\bigotimes_iP_{t_i}$ of the target coordinate permutations.", "direct"),
    add(r"\gamma", "resampling scale", "The integer $2d\\alpha^2$ such that the tensor resampling identity carries the factor $2^\\gamma$.", "count"),
    add("S", "source length product", "The product $\\prod_is_i$ of the pairwise coprime prime source lengths.", "count"),
    add(r"\mathcal A", "tensor expansion", "The tensor product of the one-dimensional expansion contractions $A_i$.", "direct"),
    add(r"\mathcal B_0", "tensor compression", "The tensor product of the one-dimensional compression contractions $B_{0,i}$.", "direct"),
]

# fix S3 from
n = find(ROOT, "S3")
n['from'] = ["gaussian-resampling", "chirp-identity", "multidimensional-transform", "dft", "cyclic-convolution", "chunk-interchange", "synthetic-transform"]

def fix(x):
    if isinstance(x, dict):
        return {k: fix(v) for k, v in x.items()}
    if isinstance(x, list):
        return [fix(v) for v in x]
    if isinstance(x, str):
        for ch, rep in (("\x08", "\\b"), ("\t", "\\t"), ("\r", "\\r"), ("\x0c", "\\f"), ("\x07", "\\a"), ("\x0b", "\\v"), ("\n", "\\n")):
            x = x.replace(ch, rep)
        return x
    return x


ROOT = fix(ROOT)
json.dump({"root": ROOT}, open(OUT, 'w'), indent=1, ensure_ascii=False)
print("written")
