import json
def H(s,q): return {"symbol":s,"anchor":{"kind":"here","quote":q}}
def P(s,p): return {"symbol":s,"anchor":{"kind":"page","page":p}}
def B(s,n): return {"symbol":s,"anchor":{"kind":"background","note":n}}
q1="Let $h_p=2^{-p}$, $L=\\log_2T$, $S\\le T$"
q2="Let $U,V_1$ be their exact source transforms and $\\widetilde U,\\widetilde V_1$ the computed ones"
q3="With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy"
q4="Multiplying exactly by $S$, $\\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$"
syms=[P("p","fixed-point"),P("b","radix-digit-reduction"),P("n","conjecture"),
H("h_p",q1),H("L",q1),P("T","radix-digit-reduction"),P("S","radix-digit-reduction"),
H("a","Error $a$ means sup-norm error under $ah_p$"),
P("f","contraction-maps"),P("g","contraction-maps"),P("\\mathcal M","contraction-maps"),
P("f'","contraction-maps"),P("g'","contraction-maps"),P("\\|f\\|","phase-twist"),
H("e","For a unit phase $e$"),
H("\\widetilde e","a disk-grid approximation $\\widetilde e$ with"),
H("x","and a disk operand $x$"),
P("Q_p","fixed-point"),
H("M","a final exact multiplication by $M=T/r$"),
P("r","ring-y"),
H("E_{\\rm ring}","giving $E_{\\rm ring}:=M(3L+2)<5TL$"),
P("\\mathcal M_r","phase-twist"),
B("*","Convolution f*g is covered by the known concept Cyclic convolution."),
H("\\widetilde{\\mathscr C}","The chirp transform $\\widetilde{\\mathscr C}$ evaluates"),
H("\\boldsymbol t","with $\\boldsymbol t$ the axis lengths"),
H("F_{\\boldsymbol t}","$F_{\\boldsymbol t}$ the exact Fourier transform"),
P("Q","chirp"),
H("E_s","error is under $E_sh_p$, $E_s=9\\cdot2^\\gamma TL$"),
P("\\gamma","multidim-transform"),
P("d","phase-twist"),
H("E_w",q4),H("w",q4),H("\\widetilde w",q4),
H("u","Here $u,v$ denote the scaled digit arrays"),H("v","Here $u,v$ denote the scaled digit arrays"),
H("U",q2),H("V_1",q2),H("\\widetilde U",q2),H("\\widetilde V_1",q2),
H("z","Then $z=Q_p(\\widetilde U\\cdot\\widetilde V_1)$ has norm under $.5$"),
H("F","Both source Fourier transforms, $F$ and $F^+$, carry $1/S$"),
H("F^+","Both source Fourier transforms, $F$ and $F^+$, carry $1/S$"),
B("I","Identity matrix, covered by the first linear algebra course."),
H("G","so the exact opposite transform $G$ gives"),
P("c_j","radix-digit-reduction"),P("q","radix-digit-reduction"),
H("Q_0",q3),H("k_0",q3),H("k_j",q3),H("d_j",q3),H("j",q3),
B("h","Summation index in sums over h<j; covered by summation notation in discrete mathematics.")]
gaps=[
{"term":"margin claim for p=6b","quote":"leaves margin $2^{-b}$ against amplification up to $2^{5b+4}$","kind":"step","note":"Not in the paper and not supported by the page's own bound. The amplification is 2^{2b+4}S with errors up to about 28*2^gamma*T^2*L, so 2^{5b+4}*2^{-6b}=2^{-b+4}, not 2^{-b}; the displayed bound actually obtained is 448 b 2^{-b+gamma}, which exceeds 2^{-b}. The correct statement is the displayed bound 448 b 2^{-b+gamma} <= 448 b 2^{-3b/4} < 1/2 (paper lines 4722-4727)."},
{"term":"3L+2 count for ring convolution","quote":"Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$","kind":"step","note":"The page never says what the ring convolution consists of (two forward synthetic transforms, a pointwise polynomial product with truncation under 2, one opposite transform), so the reader cannot check that three transforms at L each plus 2 gives 3L+2."},
{"term":"error 2dp^2+8TL of a source transform","quote":"a chirp transform (error under $2dp^2+8TL$)","kind":"step","note":"The page gives no source for the 2dp^2 term (computed expansion and compression maps of Gaussian resampling, error under dp^2 each side); the reader cannot check it from what is given."},
{"term":"norm under .26 of computed transforms","quote":"the computed ones, of norm under $.26$","kind":"step","note":"Needs 1/4+E_s h_p<.26, i.e. E_s h_p<.01, which the page never states (it only states 5TLh_p<10^{-3} for the ring convolution); the cutoff making E_s h_p small is not given."}
]
json.dump({"symbols":syms,"gaps":gaps},open("/home/user/e2e-run/exegenius/tasks/0141-audit-precision-recovery.answer.json","w"),indent=1)
