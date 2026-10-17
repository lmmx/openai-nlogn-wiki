import json
page=open('/home/user/e2e-run/exegenius/tasks/0103-write-precision-recovery.answer.md').read()
D=[]
def d(step,q):
    assert q in page,(step,q)
    D.append({"step":step,"quote":q})
S=lambda s:s
d("S5.7.1","By the paper's cost lemma each [Synthetic polynomial transform](synthetic-transform.md) has error below $L$")
d("S5.7.2","Error $a$ means sup-norm error less than $ah_p$")
d("S5.7.3","a bilinear $\\mathcal M$ with $\\|\\mathcal M(f,g)\\|\\le\\|f\\|\\|g\\|$ satisfies")
d("S5.7.4","For disk operands the two input errors add.")
d("S5.7.5","Truncation $Q_p$ adds under $\\sqrt2h_p$, so $\\|Q_p(\\widetilde ex)-ex\\|<(2\\|x\\|+\\sqrt2)h_p<4h_p$; and $|\\widetilde e|\\le1$ gives $\\|Q_p(\\widetilde ex)\\|\\le\\|x\\|$.")
d("S5.7.6","Its transforms and truncation give error under $3L+2$ before a final exact multiplication by $M=T/r$, which scales the error:")
d("S5.7.7","The complex convolution adds two input twists and an output untwist, each under $4$: error under $(E_{\\rm ring}+4+4+4)h_p<6TLh_p$.")
d("S5.7.8","the kernel adds $2$, the first phase $4$, the convolution $6TL$, the last phase $4$:")
d("S5.7.9","As $2dp^2<TL$ eventually, the error is under $E_sh_p$, $E_s=9\\cdot2^\\gamma TL$.")
d("S5.7.10","has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.")
d("S5.7.11","The computed opposite transform accepts $z$ and is within $E_sh_p$ of $Gz$, while $G$ is a contraction, so the total is under $(3E_s+2)h_p$.")
d("S5.7.12","Multiplying exactly by $S$, $\\widetilde w$ approximates $w=(u*v)/S$ with error under $E_wh_p$:")
d("S5.7.13","The integer coefficients are $2^{2b+4}Sw$, undoing the digit scales and the $1/S$.")
d("S5.7.14","With $S\\le T<2^b$ and $L<b$, the absolute error is under")
d("S5.7.15","The amplification up to $2^{5b+4}$ is absorbed because $p=6b$ leaves margin $2^{-b}$.")
d("S5.7.16","The coefficients are integers, so this strict error makes the nearest integer to the represented value the unique correct one.")
d("S5.7.17","With $Q_0=2^b$ and $k_0=0$,")
d("S5.7.18","Then $0\\le k_j\\le q(Q_0-1)<Q_0^2$: if this holds at $j$, then $c_j+k_j\\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.")
d("S5.7.19","The unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed.")
d("S5.7.20","The product is less than $2^{2n}$, so bits above position $2n-1$ are zero and $2n$ bits are output.")
R=[
("fixed-point","runs on","The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits, where $b=\\lceil\\log_2n\\rceil$ is the digit width."),
("contraction-maps","adds errors through","It adds errors through the [Contractions and bilinear contractions](contraction-maps.md) making up each normalized transform and product: a linear one does not enlarge an input error, and a bilinear $\\mathcal M$ with $\\|\\mathcal M(f,g)\\|\\le\\|f\\|\\|g\\|$ satisfies"),
("chirp","evaluates","The chirp transform $\\widetilde{\\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md) as phase product, convolution, phase product."),
("radix-digit-reduction","rebuilds the binary product from","Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\\le q(2^b-1)^2$ and $q=\\lceil n/b\\rceil\\le2^b$."),
]
for _,_,q in R: assert q in page,q
sy=[
("h_p","grid step","The grid step: $2^{-p}$.","direct","Let $h_p=2^{-p}$, $L=\\log_2T$, $S\\le T$;"),
]
out={"derivations":D,"relations":[{"prerequisite":a,"predicate":b,"quote":c} for a,b,c in R],"symbols":[]}
json.dump(out,open('/home/user/e2e-run/exegenius/tasks/0103-write-precision-recovery.answer.json','w'),indent=1)
