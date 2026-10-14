import json

SRC = '/home/user/openai-nlogn-wiki/runs/K1/sources/paper.tex'
OUT = '/home/user/openai-nlogn-wiki/runs/K1/exegenius/tasks/0003-argument.answer.json'
LINES = open(SRC, encoding='utf-8').read().split('\n')

READING = ['integer-multiplication-problem','polynomial-ring-mod','gaussian-dyadics',
 'harvey-hoeven-multiplier','signed-kronecker-packing','fixed-tape-model','sch-conjecture',
 'stream-scans','linear-subspaces','bank-exchange-network','frames','address-shear',
 'three-element-subsets','complex-phase-network','scratch-restoring-exchange',
 'rank-saving-recursion','bruhat-factorization','fast-address-interchange','cyclic-convolution',
 'radix-digit-convolution','approximate-contraction','truncation','simultaneous-butterfly-layer',
 'fourier-transform','synthetic-polynomial-transform','bluestein-chirp','phase-twist',
 'normalized-ring-convolution','chinese-remainder-axes','gaussian-resampling','sort-free-resampling',
 'permutation-cancellation','rounding-carry-recovery','multiplication-pipeline','parameter-choice-cost',
 'sub-linearithmic-integer-multiplication']
RANK = {p: i for i, p in enumerate(READING)}

def ev(q):
    hits = [i + 1 for i, l in enumerate(LINES) if q in l]
    assert len(hits) == 1, (len(hits), q)
    return {"source": "paper", "quote": q}

def B(sym, name, meaning, rel):
    return {"symbol": sym, "name": name, "meaning": meaning, "relation": rel}

def infer(id_, claim, quote, page=None, frm=()):
    n = {"id": id_, "intention": "infer", "claim": claim, "quote": ev(quote), "from": list(frm)}
    if page:
        n["page"] = page
    return n

def show(id_, claim, method, mtext, msrc, mquote, children, page=None, frm=(), adds=None, salient=None):
    mot = {"text": mtext, "source": msrc}
    mot["quote"] = ev(mquote) if msrc == "explicit" else None
    n = {"id": id_, "intention": "show", "claim": claim, "method": method,
         "motivation": mot, "children": children, "from": list(frm)}
    if page:
        n["page"] = page
    if adds:
        n["adds"] = adds
    if salient:
        n["salient"] = salient
    return n

# ---------- Section A: tape procedures (intro order: fast interchange, then network) ----------
S11 = show("S1.1",
 "A fixed linear network exchanges the banks $X_a$ and $Y_a$ with prescribed signs and restores every scratch wire.",
 "three stages of scalar invocations over triples; each stage is a forward schedule, and the scratch wires are restored",
 "The scratch wires have arbitrary initial values, so the network must cancel their effect and restore them.",
 "recoverable", None,
 [
  show("S1.1.1",
   "A forward invocation adds one bank into the other, and three invocations exchange $X_a$ and $Y_a$ with a sign while restoring every auxiliary value.",
   "a fixed eight-row schedule of copy, gather, side-injection and scatter gates, applied as forward, inverse and forward invocations",
   "The scratch values are arbitrary, so the schedule first removes their effect and later restores them.",
   "recoverable", None,
   [
    infer("S1.1.1.1",
     "A forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, for arbitrary initial auxiliary values.",
     "For arbitrary initial values of its auxiliary wires, a forward"),
    infer("S1.1.1.2",
     "A forward invocation from $X$ to $Y$, an inverse forward schedule from $Y$ to $X$, and a forward invocation from $X$ to $Y$ send $(X_a,Y_a)\\mapsto(-Y_a,X_a)$ and restore every auxiliary value.",
     "Performing a forward invocation from $X$ to $Y$ at stage 1,"),
   ], page="scratch-restoring-exchange", frm=[]),
  infer("S1.1.2",
   "In the bit construction the central coefficient from $x_T$ to $y_S$ is $|S\\cap T|\\bmod 2$, and the side injection cancels the intersection-one cases, so the net map is $y\\gets y+x$.",
   "In the bit case, the central coefficient from $x_T$ to $y_S$ is", page="three-element-subsets", frm=["linear-subspaces"]),
 ], page="bank-exchange-network", frm=["linear-subspaces"])

S12 = infer("S1.2",
 "The implemented operator is $D_{\\rm out}\\,\\mathsf S_\\Omega\\,D_{\\rm in}^{-1}$, so each route applies $\\varepsilon_w D_{\\mathrm{sink}(\\rho(w))}D_{\\mathrm{source}(w)}^{-1}$ to its input array.",
 "The implemented operator is therefore", page="frames", frm=["linear-subspaces","bank-exchange-network"])

S13 = show("S1.3",
 "The total rank $s$ of the edge differences satisfies $s<Wm$, so multiplying the recursion parameter by $m$ multiplies the recursive cost by $s/W<m$.",
 "bound each edge's rank change by the dimension of an orthogonal residual of nested subspace labels, then sum over all edges so that the gate contributions telescope",
 "The strict inequality $s/W<m$ per level is the power saving, so the rank total must be bounded.",
 "explicit", "is the source of the power saving.",
 [
  infer("S1.3.1", "Every edge joins comparable nondegenerate labels, so each edge residual is the orthogonal complement of the smaller label inside the larger one.",
        "Every edge joins comparable nondegenerate labels.", frm=["linear-subspaces"]),
  infer("S1.3.2", "The signed sum of dimension changes over all edges equals $Wm-2N$, because the gate contributions cancel, and the absolute sum is $Wm-2N+2L$.",
        "The signed sum of dimension changes telescopes at every gate: each"),
  infer("S1.3.3", "The loss ratios are $L_b/N=100/539$ and $L_c/N=101/539$, both smaller than $1/2$.",
        "The loss ratios have the exact values"),
  infer("S1.3.4", "The total rank $s$ of the edge differences of the bit network equals $W_bm-N+2L_b$, which is less than $W_bm$.",
        "The sum of the rational ranks of all edge differences is"),
  infer("S1.3.5", "Each complex edge's phase-frame difference is a product of one translation kernel per vector of an orthonormal basis of its residual, so the complex network has total count $s_c<W_cm$.",
        "$\\mathcal C_V\\mathcal C_U^{-1}$ is a product of one translation", page="complex-phase-network",
        frm=["gaussian-dyadics","bank-exchange-network","three-element-subsets","frames"]),
  infer("S1.3.6", "The relative rank deficits exceed $20\\cdot 2^{-50}$, so $s/W<m^\\tau$ with $\\tau=\\sigma=1-2^{-50}$ for both networks.",
        "Both exact deficits displayed above are greater than"),
 ],
 page="rank-saving-recursion", frm=["linear-subspaces","frames","bank-exchange-network","three-element-subsets"],
 adds=[B("W","wire count","the number of wires in the network, counting scratch wires","count"),
       B("m","label dimension","the dimension of the ambient label space","count"),
       B("s","rank total","the sum of the rational ranks of the edge differences, which is the number of smaller calls","count")],
 salient="the total rank $s$ of all edge differences is strictly less than $Wm$, so each recursion level saves a factor $m$ on the recursive cost")

S14 = infer("S1.4",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ factors as $A=E_1\\Pi E_2$ with invertible lower-triangular $E_1,E_2$ and a partial permutation matrix $\\Pi$ having $a$ ones.",
 "Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization", page="bruhat-factorization", frm=["address-shear"])

S15 = infer("S1.5",
 "The permutation $(H,D)\\mapsto(H+AD,D)$ of rational rank $a$ can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work.",
 "can be performed with exactly $a$ interchanges of pairs of $b$-digit", frm=["bruhat-factorization","stream-scans"])

S16 = show("S1.6",
 "Two chunks of $e=m^k$ digits are interchanged in $O(Ve^\\tau)$ time, because the recursive calls obey $F_k\\le(s/W)F_{k-1}+O(1)$ with ratio $s/W<m^\\tau$.",
 "solve the recurrence for the cost per unit volume by a geometric sum over the recursion depth",
 "Each recursive call uses $s$ calls on a stream of volume $V/W$, so the recurrence has ratio $s/W$.",
 "recoverable", None,
 [
  infer("S1.6.1", "For $a=s/W<m^\\tau$ the sum $\\sum_{j=0}^k a^j$ is $O(m^{k\\tau})$.",
        "For $a=s/W<m^\\tau$ the geometric sum"),
  infer("S1.6.2", "The cost per unit volume satisfies $F_k=O(e^\\tau)$.", "Hence $F_k=O(e^\\tau)$."),
 ])

S17 = infer("S1.7",
 "For positive integers $P,G,B$ and $u\\ge1$, an arbitrary bit array of volume $V$ with chunk width $u$ is interchanged in $O(Vu^{\\tau})$ steps for a fixed $0<\\tau<1$.",
 "There exist fixed $0<\\tau<1$ and one fixed finite-alphabet multitape", frm=["stream-scans"])

S1 = show("S1",
 "Two disjoint equal-width address chunks of $u$ bits in an array of stored volume $V$ are interchanged in $O(Vu^{\\tau})$ time for a fixed exponent $\\tau<1$.",
 "write the interchange as a shear realized by a fixed bit network, implement each network edge by a smaller interchange, and count the recursion",
 "Because each edge needs only as many smaller interchanges as its rank, the total rank saves a power of the chunk width.",
 "explicit", "Because the sum of these ranks is less than the number of wires times",
 [S11, S12, S13, S14, S15, S16, S17],
 page="fast-address-interchange", frm=["stream-scans","address-shear"],
 adds=[B("u","chunk width","the number of bits in each of the two address chunks to be interchanged","count"),
       B("V","stored volume","the number of stored data bits in the array","count"),
       B("\\tau","saving exponent","a fixed exponent strictly below one that bounds the cost as a power of the chunk width","direct")],
 salient="the exponent $\\tau<1$ is fixed and strictly below one, so the cost is a power of the chunk width below linear")

# ---------- Section B: butterfly layer ----------
S2 = show("S2",
 "A common butterfly layer $H_0$ on $D\\le d$ selected bits of complex polynomial records runs in $O(Vd^{\\lambda'})$ time with $\\lambda'<1$.",
 "apply the complex phase network to the layer, whose phase frames telescope to tensor products of two-point kernels, and truncate once after the completed layer",
 "Intermediate values stay exact Gaussian dyadics, so a single truncation after the contractive layer suffices.",
 "recoverable", None,
 [
  infer("S2.1", "The phase identities express each edge's residual operator as a product of two-point kernels on the selected directions.",
        "Hold the unselected address bits fixed and regard the stored complex"),
  infer("S2.2", "For $p\\ge p_0$ the simultaneous normalized butterfly layer is one fixed finite-alphabet procedure with cost $O(Vd^{\\lambda'})$.",
        "there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure,"),
 ], page="simultaneous-butterfly-layer", frm=["gaussian-dyadics","truncation","fast-address-interchange","complex-phase-network"])

# ---------- Section C: synthetic transforms ----------
S3 = show("S3",
 "The normalized transforms $F_t^\\pm$ over $\\mathcal R_r$ are contractions computed by radix-two butterflies, and the stored frequency order is consumed exactly by the inverse.",
 "radix-two decimation steps whose roots of unity are powers of $y$, with the inverse traversing the same recursion in reverse",
 "Multiplication by a root of unity is then a signed shift of the coefficient list.",
 "explicit", "such a root is a signed shift of the coefficient list.",
 [
  infer("S3.1", "Every power of $\\omega_t$ is an isometry and each transform entry averages $t$ such images, so $F_t^\\pm$ are contractions.",
        "Every power of $\\omega_t$ is an isometry, and each transform entry is"),
  infer("S3.2", "The root sums cancel, so $F_t^+F_t^-=t^{-1}I$ holds without dividing by $\\omega_t^j-1$.",
        "The ring has zero divisors, so we verify character cancellation"),
  infer("S3.3", "The two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$, so the inverse consumes the stored frequency order.",
        "The procedure consuming this stored order traverses the recursion in"),
  infer("S3.4", "A round is a parallel butterfly $\\mathcal H$ followed by a recordwise monomial $J_E$, and each completed round is a contraction.",
        "A round applies one current $H_0$ on each participating axis."),
  infer("S3.5", "The selected bits of the participating axes are placed at a common offset in consecutive $K$-bit chunks, using single-bit moves and chunk interchanges.",
        "To apply Proposition~\\ref{prop:simultaneous-layer} in a transform round,", frm=["fast-address-interchange","stream-scans"]),
 ], page="synthetic-polynomial-transform", frm=["polynomial-ring-mod","fourier-transform","truncation","simultaneous-butterfly-layer"])

# ---------- Section D: exact ring products ----------
S4 = show("S4",
 "The normalized convolution $\\mathcal M_r(f,g)=(f*g)/T$ over $\\mathcal R_r$ is a bilinear contraction, computed from the retained layout with error below $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
 "reduce each record product to one signed integer product by packing, then compute the cyclic convolution from the transform layout",
 "The packed products reuse the established multiplier as an ordinary subroutine, so only the packing and recovery need proof.",
 "recoverable", None,
 [
  infer("S4.1", "The reduction of a polynomial product to one integer product is a signed form of Kronecker substitution.",
        "reduction is a signed form of Kronecker substitution; compare", page="signed-kronecker-packing", frm=["harvey-hoeven-multiplier"]),
  infer("S4.2", "The exact Gaussian integer numerators of $fg$ are computed and the rounded value $Q_p(fg/r)$ is returned in time $O(rp\\log(rp))$.",
        "One can compute the exact Gaussian integer", frm=["polynomial-ring-mod","gaussian-dyadics"]),
  infer("S4.3", "$\\mathcal M_r$ is a bilinear contraction, with $\\|\\mathcal M_r(f,g)\\|_\\infty\\le\\|f\\|_\\infty\\|g\\|_\\infty$.",
        "is a bilinear"),
  infer("S4.4", "On disk-grid operands $\\mathcal M_r$ has an approximation with error less than $\\sqrt2\\,M(3\\ell+1)2^{-p}$.",
        "Under the hypotheses of Lemma~\\ref{lem:synthetic-transform-cost},", frm=["approximate-contraction"]),
 ], page="normalized-ring-convolution", frm=["polynomial-ring-mod","harvey-hoeven-multiplier","cyclic-convolution","synthetic-polynomial-transform","approximate-contraction","truncation"])

# ---------- Section E: Gaussian resampling ----------
S5 = show("S5",
 "A Fourier transform whose length is not a power of two is expressed through a tensor transform with power-of-two axis lengths, using Gaussian-weighted resampling.",
 "apply the one-dimensional resampling identity to each coordinate line, tensor it over the $d$ axes, and move axes by chunk interchanges",
 "The transform lengths needed for the product are pairwise coprime, whereas the synthetic transforms use powers of two.",
 "explicit", "whereas the synthetic transforms use powers of two.",
 [
  infer("S5.1", "For coprime $s<t$ with $t/s-1>p/\\alpha^4$ there are linear contractions $A$ and $B_0$ such that the resampling holds without executing the coordinate permutations.",
        "There are linear contractions $A:\\mathbb C^s\\to\\mathbb C^t$ and", page="sort-free-resampling", frm=["fourier-transform","approximate-contraction"]),
  infer("S5.2", "The tensor product of the one-dimensional resampling maps satisfies the tensor identity with the same contraction bounds.",
        "Suppose every pair $(s_i,t_i)$, $1\\leq i\\leq d$, satisfies"),
 ], page="gaussian-resampling", frm=["fourier-transform","synthetic-polynomial-transform","fast-address-interchange"])

# ---------- Section F: chirp and cancellation ----------
S6 = show("S6",
 "A transform with quadratic phase factors equals a pointwise chirp, a cyclic convolution normalized by $T$, and a pointwise conjugate chirp.",
 "complete the square in the exponent to write the middle transform as chirp multiplication, cyclic convolution, and conjugate chirp",
 "The chirp converts the middle transform into a cyclic convolution, which the fast convolution computes.",
 "recoverable", None,
 [
  infer("S6.1", "With chirp $a_{\\boldsymbol j}=\\exp(-\\pi i\\sum_i s_i j_i^2/t_i)$ the transform equals $\\overline a\\cdot(a*(\\overline a\\cdot u))/T$.",
        "Then $a$ has period $t_i$ in coordinate $i$, and"),
  infer("S6.2", "The retained source permutation cancels: $(RF_s^+)[(RF_su)\\cdot(RF_sv)]=(u*v)/S^2$.",
        "If $S=\\prod_i s_i$, then", page="permutation-cancellation", frm=["sort-free-resampling","fourier-transform"]),
 ], page="bluestein-chirp", frm=["cyclic-convolution","fourier-transform"])

# ---------- Section G: CRT layout and twist ----------
S7 = infer("S7",
 "The coordinate of $\\Phi(x^k)$ in axis $i$ is $b_i=a_i+\\mu_i\\sum_{j<i}a_jP_j \\pmod{s_i}$, a triangular controlled shift.",
 "The coordinate of $\\Phi(x^k)$ in axis $i$ is", page="chinese-remainder-axes", frm=["cyclic-convolution","radix-digit-convolution"])

S8 = infer("S8",
 "The power-of-two complex convolution is obtained from the synthetic convolution by a phase twist $x_d\\mapsto\\zeta y$ with $\\zeta=e^{\\pi i/r}$.",
 "obtained from the synthetic convolution by a coefficient twist.", page="phase-twist", frm=["polynomial-ring-mod","bluestein-chirp","cyclic-convolution"])

# ---------- Section H: multiplication pipeline ----------
P1 = infer("S9.1", "The source-transform procedures supply the three transforms needed for the radix-digit convolution.",
           "The source-transform procedures now supply the three transforms needed", frm=["gaussian-resampling"])
P0 = infer("S9.2", "Reading each operand in groups of $b$ bits gives the radix-$2^b$ digits $a_0,\\ldots,a_{q-1}$ in increasing coefficient order.",
           "This produces the radix-$2^b$ digits", page="radix-digit-convolution", frm=["cyclic-convolution"])
P2 = infer("S9.3", "The coefficient-address map $\\Phi$ gives source arrays $u,v$ whose exact $p$-bit grid values have norm less than $1/4$.",
           "Apply the coefficient-address map $\\Phi$, with its padded layout, to obtain", frm=["chinese-remainder-axes"])
P3 = infer("S9.4", "The pointwise product of the two computed transforms is truncated to the common component format, giving the array $z$.",
           "Multiply corresponding complex coefficients exactly and truncate", frm=["truncation"])
P4 = infer("S9.5", "The opposite transform of $z$ multiplied by $S$ gives $\\widetilde w$ approximating $w=(u*v)/S$.",
           "Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid", frm=["permutation-cancellation"])
RC = show("S9.6",
 "The scaled coefficients round to integers and carries propagate, so the output is exactly the $2n$-bit product.",
 "round each recovered coefficient with error below one half, then propagate carries in increasing coefficient order",
 "The known normalizations are removed by exact scaling, so only the rounding error needs control.",
 "recoverable", None,
 [
  infer("S9.6.1", "Each represented real value is rounded to the nearest integer and written as a signed $(3b+1)$-bit word.",
        "Round the represented real"),
  infer("S9.6.2", "Carries propagate in increasing coefficient order, and the output is exactly $2n$ bits.",
        "Propagate radix-$2^b$ carries in increasing coefficient order."),
  infer("S9.6.3", "The final absolute error is below $1/2$, so the nearest integer to each represented value is the unique correct coefficient.",
        "The strict error below $1/2$ makes the nearest integer to"),
 ], page="rounding-carry-recovery", frm=["truncation","approximate-contraction"])
S9 = show("S9",
 "The exact product of two $n$-bit integers is computed by the transform reductions in order: radix-digit input, source transforms, pointwise product, opposite transform, rounding, and carry propagation.",
 "compose the reductions of the convolution route in the order of the algorithm, and recover the exact integer coefficients by rounding and carries",
 "Each reduction preserves the convolution it computes, so composing them computes the product.",
 "recoverable", None,
 [P1, P0, P2, P3, P4, RC], page="multiplication-pipeline",
 frm=["radix-digit-convolution","chinese-remainder-axes","gaussian-resampling","bluestein-chirp","phase-twist","normalized-ring-convolution","permutation-cancellation","truncation","approximate-contraction"])

# ---------- Section I: parameters and cost ----------
S10 = show("S10",
 "With the fixed rational exponents $\\tau=\\sigma=1-2^{-50}$ and $\\kappa=2^{-182}$, every term of the cost table is within $O(n(\\lg n)^{1-\\kappa})$ after division by the stored volume $V$.",
 "bound each cost row by a power of $p$, then check that the smallest margin is at least $2\\kappa$",
 "The margins are explicit rational powers, so the bound can be checked by substitution.",
 "recoverable", None,
 [
  infer("S10.1", "The smallest margin among the seven dominant powers is $2^{-181}=2\\kappa$.",
        "Thus $\\min_i g_i=2^{-181}=2\\kappa$."),
  infer("S10.2", "The total time is $O(Tp\\,p^{1-\\kappa})=O(n(\\log n)^{1-\\kappa})$.",
        "The complete large-input bound is consequently"),
 ], page="parameter-choice-cost", frm=["fixed-tape-model"])

ROOT = show("S0",
 "A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\\lg n)^{1-\\kappa})$ worst-case time, with $\\kappa=2^{-182}$.",
 "reduce the product to a transform pipeline whose tape-costly layers each save a power of their width, then fix rational exponents so that every cost term is within the bound",
 "Scanning the stored bits at every transform level already costs $n\\log n$, so savings in both movement and arithmetic are needed.",
 "explicit", "We therefore need savings in both movement and arithmetic.",
 [S1, S2, S3, S4, S5, S6, S7, S8, S9, S10],
 page="sub-linearithmic-integer-multiplication",
 frm=["integer-multiplication-problem","fixed-tape-model","sch-conjecture"])

answer = {"root": ROOT}

# ---------- validation ----------
def walk(n, out):
    out.append(n)
    for c in n.get("children", []):
        walk(c, out)
    return out

nodes = walk(ROOT, [])
ids = [n["id"] for n in nodes]
assert len(ids) == len(set(ids)), "duplicate ids"

# infer quotes in DFS order must be in increasing source line
def line_of(q):
    return [i + 1 for i, l in enumerate(LINES) if q in l][0]
infer_nodes = [n for n in nodes if n["intention"] == "infer"]
pos = [line_of(n["quote"]["quote"]) for n in infer_nodes]
for a, b, n1, n2 in zip(pos, pos[1:], infer_nodes, infer_nodes[1:]):
    if not b > a:
        print("ORDER PROBLEM", n1["id"], a, n2["id"], b)

# pages: each at most once; from pages earlier than step page
page_nodes = {}
cur_page = None
def assign(n, inherited):
    p = n.get("page", inherited)
    for c in n.get("children", []):
        assign(c, p)
    n["_eff_page"] = p
assign(ROOT, None)
seen = {}
for n in nodes:
    if "page" in n:
        assert n["page"] not in seen, ("page twice", n["page"], n["id"], seen.get(n["page"]))
        seen[n["page"]] = n["id"]
for n in nodes:
    p = n["_eff_page"]
    for f in n.get("from", []):
        if f in RANK and p in RANK and RANK[f] >= RANK[p]:
            print("FROM ORDER PROBLEM", n["id"], "page", p, "from", f)
# pages not presented must be in some from
allfrom = set(f for n in nodes for f in n.get("from", []))
for p in READING:
    if p not in seen and p not in allfrom:
        print("UNCOVERED PAGE", p)
# strip internal key
for n in nodes:
    n.pop("_eff_page", None)
json.dump(answer, open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("nodes", len(nodes), "infer", len(infer_nodes), "pages presented", sorted(seen))
