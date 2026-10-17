import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0268-write-precision-recovery.answer.md').read()
def span(start,end):
    i=t.index(start); j=t.index(end,i)+len(end)
    q=t[i:j]
    assert '<cite' not in q,(start)
    return q
D=[]
def d(step,start,end): D.append({"step":step,"quote":span(start,end)})
d("S5.7.1","Each [synthetic transform]","for all large $n$")
d("S5.7.2","Write $h_p=2^{-p}$","below $ah_p$.")
d("S5.7.3","Hence $\\|\\mathcal M(f',g')","\\|g'-g\\|$.")
d("S5.7.4","For operands in the disk,","input errors add.")
d("S5.7.5","The approximation moves the product","since $|\\widetilde e|\\le1$.")
d("S5.7.6","The returned convolution","<.701$")
d("S5.7.7","The computed complex convolution","<6TLh_p$.")
d("S5.7.8","With $\\boldsymbol t$ the axis lengths","<8TLh_p$.")
d("S5.7.9","Expansion and compression add","E_s=9\\cdot2^\\gamma TL$")
d("S5.7.10","Since $\\widetilde U\\cdot","<(2E_s+2)h_p$.")
d("S5.7.11","Since $\\|z\\|<.5$","<(3E_s+2)h_p$.")
d("S5.7.12","Exact multiplication by $S$","since $S\\le T$.")
d("S5.7.13","After this second scaling","2^{-6b}$.")
d("S5.7.14","Using $S\\le T<2^b$","$28\\cdot2^4=448$.")
d("S5.7.15","Since $\\gamma\\le b/4$ for","<\\tfrac12$")
d("S5.7.16","The true coefficients are integers","correct coefficient.")
d("S5.7.17","For $0\\le j<S$ the carries obey","\\rfloor$")
d("S5.7.18","Then $0\\le k_j","$k_{j+1}\\le q(Q_0-1)$.")
d("S5.7.19","Since $c_j+k_j=d_j+Q_0k_{j+1}$","are fixed.")
d("S5.7.20","The product is less than $2^{2n}$","are output.")
R=[
("fixed-point","runs on","The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits"),
("radix-digit-reduction","rebuilds the binary product from","Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md)"),
("contraction-maps","adds errors through","Errors add through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product."),
("chirp","is built from","The computed chirp transform $\\widetilde{\\mathscr C}$ is built from the [Bluestein chirp identity](chirp.md)"),
]
Rl=[]
for pid,pred,q in R:
    assert q in t,q
    Rl.append({"prerequisite":pid+".md" if False else pid,"predicate":pred,"quote":q})
S=[]
def s(sym,name,meaning,start,end,rel="direct"):
    S.append({"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":span(start,end)})
s("h_p","grid spacing","The spacing $2^{-p}$ of the fixed-point grid.","Write $h_p=2^{-p}$","below $ah_p$.")
s("a","error size","The size of an error, counted in grid spacings $h_p$.","Write $h_p=2^{-p}$","below $ah_p$.","count")
s("L","log of padded length","The base-2 logarithm of the padded length $T$; not the linear map $L$ of the contractions page.","Put $L=\\log_2T$","contractions page.")
s("e","unit phase","A phase of modulus one that multiplies an array.","A phase multiplication computes","in the disk.")
s("\\widetilde e","phase approximation","A grid approximation of the unit phase $e$ within $2h_p$.","A phase multiplication computes","in the disk.")
s("x","disk array","An arbitrary array in the unit disk to which a phase or chirp transform is applied; not the digit-polynomial variable.","A phase multiplication computes","in the disk.")
s("E_{\\rm ring}","ring convolution error","The error bound $M(3L+2)$ of the returned ring convolution, in units of $h_p$.","The returned convolution","<5TL$")
s("\\widetilde{\\mathcal M}_{\\mathbb C}","computed complex convolution","The computed complex cyclic convolution built from twists and the ring convolution.","The computed complex convolution","untwists the output")
s("\\widetilde{\\mathscr C}","computed chirp transform","The computed chirp transform built from phase products and a complex convolution.","The computed chirp transform","last phase product.")
s("\\widetilde{\\mathscr F}","computed source transform","The computed source transform: expansion, chirp transform, compression, then scaling by $2^\\gamma$.","The computed source transform","scaling by $2^\\gamma$.")
s("E_s","source transform error","The error bound $9\\cdot2^\\gamma TL$ of the computed source transform, in units of $h_p$.","As $2dp^2<TL$ eventually","E_s=9\\cdot2^\\gamma TL$")
s("\\widetilde{\\mathscr F}^{+}","computed opposite transform","The computed opposite-sign source transform.","The opposite transform $\\widetilde{\\mathscr F}^{+}$","same error.")
s("u","scaled digit array","The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.","Here $u$ and $v$ denote","below $1/4$.")
s("v","scaled digit array","The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.","Here $u$ and $v$ denote","below $1/4$.")
for sym,nm,mm in [("U","exact first transform","The exact source transform of the first digit array."),("V_1","exact second transform","The exact source transform of the second digit array."),("\\widetilde U","computed first transform","The computed source transform of the first digit array."),("\\widetilde V_1","computed second transform","The computed source transform of the second digit array.")]:
    s(sym,nm,mm,"Let $U=RF_{\\boldsymbol s}u$","<.26$.")
s("z","truncated product","The truncated pointwise product of the two computed source transforms.","Then $z=Q_p","<.5$.")
s("G","exact opposite transform","The exact opposite-sign source transform $RF_{\\boldsymbol s}^+$, a contraction.","Let $G=RF_{\\boldsymbol s}^+$","opposite transform.")
s("w","first scaled result","The convolution $(u*v)/S$ of the digit arrays divided by $S$, whose scaling by $2^{2b+4}S$ gives the integer coefficients.","Exact multiplication by $S$","since $S\\le T$.")
s("\\widetilde w","computed first scaled result","The computed approximation of $w$ after exact multiplication by $S$.","Exact multiplication by $S$","since $S\\le T$.")
s("E_w","scaled error","The error bound $S(3E_s+2)$ of $\\widetilde w$, in units of $h_p$.","Exact multiplication by $S$","since $S\\le T$.")
s("Q_0","radix","The radix $2^b$ of the digits used in carry propagation.","Put $Q_0=2^b$.","Put $Q_0=2^b$.")
s("k_j","carry","The carry into position $j$ in carry propagation.","For $0\\le j<S$ the carries obey","output digit.")
s("d_j","output digit","The $j$-th radix-$2^b$ digit of the product.","For $0\\le j<S$ the carries obey","output digit.")
json.dump({"derivations":D,"relations":Rl,"symbols":S},open('/home/user/e2e-run/exegenius/tasks/0268-write-precision-recovery.answer.json','w'),indent=1)
