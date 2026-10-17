import json
t=open('/home/user/e2e-run/exegenius/tasks/0268-write-precision-recovery.answer.md').read()
def span(start,end):
    i=t.index(start); j=t.index(end,i)+len(end)
    q=t[i:j]
    assert '<cite' not in q,(start)
    return q
D=[]
def d(step,start,end): D.append({"step":step,"quote":span(start,end)})
d("S5.7.1","Each [synthetic transform]","has error below $L$")
d("S5.7.2","Write $h_p=2^{-p}$","(norm $\\le1$).")
d("S5.7.3","$$\\|\\mathcal M(f',g')","\\|g'-g\\|,$$")
d("S5.7.4","so for disk operands","errors add.")
d("S5.7.5","For a unit phase $e$,","since $|\\widetilde e|\\le1$.")
d("S5.7.6","Together they err by under","<5TL$$")
d("S5.7.7","The complex convolution adds","it errs by under")
d("S5.7.8","With $\\boldsymbol t$ the axis lengths","$4$ give")
d("S5.7.9","The error before scaling is under","with")
d("S5.7.10","has two terms under","<(2E_s+2)h_p$.")
d("S5.7.11","The computed opposite transform is within","contraction, so")
d("S5.7.12","Exact multiplication by $S$ makes","where")
d("S5.7.13","The integer coefficients are","remaining $1/S$.")
d("S5.7.14","Here $2^{2b+4}ST^2<2^{5b+4}$","fractional bits.")
d("S5.7.15","With $h_p=2^{-6b}$","is under")
d("S5.7.16","The true coefficients are integers","correct coefficient.")
d("S5.7.17","Put $Q_0=2^b$ and $k_0=0$","output digit:")
d("S5.7.18","Then $0\\le k_j","=qQ_0(Q_0-1)$.")
d("S5.7.19","Unprocessed terms are multiples","are fixed.")
d("S5.7.20","The product is below $2^{2n}$","are output.")
R=[
("fixed-point","runs on","The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits"),
("radix-digit-reduction","rebuilds the binary product from","Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md)"),
("contraction-maps","adds errors through","Errors add through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product."),
("chirp","is built from","The computed chirp transform $\\widetilde{\\mathscr C}$ is built from the [Bluestein chirp identity](chirp.md)"),
]
Rl=[]
for pid,pred,q in R:
    assert q in t,q
    Rl.append({"prerequisite":pid,"predicate":pred,"quote":q})
S=[]
def s(sym,name,meaning,start,end,rel="direct"):
    S.append({"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":span(start,end)})
s("h_p","grid spacing","The spacing $2^{-p}$ of the fixed-point grid.","Write $h_p=2^{-p}$","contractions page).")
s("L","log of padded length","The base-2 logarithm of the padded length $T$; not the linear map $L$ of the contractions page.","Write $h_p=2^{-p}$","contractions page).")
s("a","error size","The size of an error, counted in grid spacings $h_p$.","Norms are sup norms","(norm $\\le1$).")
s("e","unit phase","A phase of modulus one that multiplies an array.","For a unit phase $e$,","$|\\widetilde e-e|<2h_p$")
s("\\widetilde e","phase approximation","A grid approximation of the unit phase $e$ within $2h_p$.","For a unit phase $e$,","$|\\widetilde e-e|<2h_p$")
s("x","disk operand","An array in the unit disk to which a phase or chirp transform is applied; not the digit-polynomial variable.","For a unit phase $e$,","disk operand $x$")
s("E_{\\rm ring}","ring convolution error","The error bound $M(3L+2)$ of the returned ring convolution, in units of $h_p$.","Together they err by under","<5TL$$")
s("E_s","source transform error","The error bound $9\\cdot2^\\gamma TL$ of the computed source transform, in units of $h_p$.","As $2dp^2<TL$ eventually","with")
s("\\widetilde{\\mathscr C}","computed chirp transform","The computed chirp transform built from phase products and a complex convolution.","The computed chirp transform","last phase product.")
s("\\widetilde{\\mathscr F}","computed source transform","The computed source transform: expansion, chirp transform, compression, then scaling by $2^\\gamma$.","The computed source transform","scaling by $2^\\gamma$.")
s("u","scaled digit array","The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.","Now $u,v$ are scaled digit arrays","below $1/4$.")
s("v","scaled digit array","The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.","Now $u,v$ are scaled digit arrays","below $1/4$.")
for sym,nm,mm in [("U","exact first transform","The exact source transform of the first digit array."),("V_1","exact second transform","The exact source transform of the second digit array."),("\\widetilde U","computed first transform","The computed source transform of the first digit array."),("\\widetilde V_1","computed second transform","The computed source transform of the second digit array.")]:
    s(sym,nm,mm,"Let $U=RF_{\\boldsymbol s}u$","<.26$.")
s("z","truncated product","The truncated pointwise product of the two computed source transforms.","Then $z=Q_p","<.5$, and")
s("G","exact opposite transform","The exact opposite-sign source transform $RF_{\\boldsymbol s}^+$, a contraction.","With $F_{\\boldsymbol s}$","$G(U\\cdot V_1)=(u*v)/S^2$")
s("w","first scaled result","The convolution $(u*v)/S$ of the digit arrays divided by $S$, whose scaling by $2^{2b+4}S$ gives the integer coefficients.","Exact multiplication by $S$","where")
s("\\widetilde w","computed first scaled result","The computed approximation of $w$ after exact multiplication by $S$.","Exact multiplication by $S$","where")
s("E_w","scaled error","The error bound $S(3E_s+2)$ of $\\widetilde w$, in units of $h_p$.","Exact multiplication by $S$","where")
s("Q_0","radix","The radix $2^b$ of the digits used in carry propagation.","Put $Q_0=2^b$ and $k_0=0$","output digit:")
s("k_j","carry","The carry into position $j$ in carry propagation.","Put $Q_0=2^b$ and $k_0=0$","output digit:")
s("d_j","output digit","The $j$-th radix-$2^b$ digit of the product.","Put $Q_0=2^b$ and $k_0=0$","output digit:")
json.dump({"derivations":D,"relations":Rl,"symbols":S},open('/home/user/e2e-run/exegenius/tasks/0268-write-precision-recovery.answer.json','w'),indent=1)
