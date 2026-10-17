import json
page=open('/home/user/e2e-run/exegenius/tasks/0103-write-precision-recovery.answer.md').read()
D=[]
def d(step,q):
    assert q in page,(step,q)
    D.append({"step":step,"quote":q})
d("S5.7.1","Each [Synthetic polynomial transform](synthetic-transform.md) has error below $L$")
d("S5.7.2","Error $a$ means sup-norm error under $ah_p$")
d("S5.7.3","A bilinear $\\mathcal M$ with $\\|\\mathcal M(f,g)\\|\\le\\|f\\|\\|g\\|$ satisfies")
d("S5.7.4","so for disk operands input errors add.")
d("S5.7.5","truncation $Q_p$ adds under $\\sqrt2h_p$, so $\\|Q_p(\\widetilde ex)-ex\\|<(2\\|x\\|+\\sqrt2)h_p<4h_p$; and $|\\widetilde e|\\le1$ gives $\\|Q_p(\\widetilde ex)\\|\\le\\|x\\|$.")
d("S5.7.6","Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$, giving $E_{\\rm ring}:=M(3L+2)<5TL$.")
d("S5.7.7","Two twists and an untwist add $4$ each, so the complex convolution errs by under")
d("S5.7.8","The chirp transform $\\widetilde{\\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\\boldsymbol t$ the axis lengths, $F_{\\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:")
d("S5.7.9","As $2dp^2<TL$ eventually, error is under $E_sh_p$, $E_s=9\\cdot2^\\gamma TL$.")
d("S5.7.10","has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\\|z-U\\cdot V_1\\|<(2E_s+2)h_p$.")
d("S5.7.11","The computed one is within $E_sh_p$ of $Gz$, and $G$ is a contraction, so the total is under $(3E_s+2)h_p$.")
d("S5.7.12","Multiplying exactly by $S$, $\\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$:")
d("S5.7.13","The integer coefficients are $2^{2b+4}Sw$, undoing digit scales and $1/S$.")
d("S5.7.14","With $S\\le T<2^b$ and $L<b$ the absolute error is under")
d("S5.7.15","Here $p=6b$ leaves margin $2^{-b}$ against amplification up to $2^{5b+4}$.")
d("S5.7.16","The coefficients are integers, so error below $1/2$ makes the nearest integer to the represented value correct.")
d("S5.7.17","With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy")
d("S5.7.18","Then $0\\le k_j\\le q(Q_0-1)<Q_0^2$: if so at $j$, then $c_j+k_j\\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$.")
d("S5.7.19","from $j$ to $j+1$. Unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed.")
d("S5.7.20","The product is below $2^{2n}$, so bits above position $2n-1$ are zero and $2n$ bits are output.")
R=[
("fixed-point","runs on","The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits; $b=\\lceil\\log_2n\\rceil$ is the digit width."),
("contraction-maps","adds errors through","It adds errors through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product."),
("chirp","evaluates","The chirp transform $\\widetilde{\\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\\boldsymbol t$ the axis lengths, $F_{\\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:"),
("radix-digit-reduction","rebuilds the binary product from","Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\\le q(2^b-1)^2$ and $q=\\lceil n/b\\rceil\\le2^b$."),
]
for _,_,q in R: assert q in page,q
SY=[
("h_p","grid step","The grid step, 2^{-p}.","Let $h_p=2^{-p}$, $L=\\log_2T$, $S\\le T$; for large $n$, $T<8n/b$ gives $T<2^b$ and $L<b$."),
("L","log of padded size","The base-2 logarithm of T.","Let $h_p=2^{-p}$, $L=\\log_2T$, $S\\le T$; for large $n$, $T<8n/b$ gives $T<2^b$ and $L<b$."),
("E_{\\rm ring}","ring convolution error","The error bound of the ring convolution, M(3L+2).","Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$, giving $E_{\\rm ring}:=M(3L+2)<5TL$."),
("\\boldsymbol t","axis lengths","The tuple of axis lengths.","The chirp transform $\\widetilde{\\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\\boldsymbol t$ the axis lengths, $F_{\\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:"),
("F_{\\boldsymbol t}","exact Fourier transform","The exact Fourier transform with axis lengths t.","The chirp transform $\\widetilde{\\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\\boldsymbol t$ the axis lengths, $F_{\\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:"),
("\\gamma","source scale exponent","The exponent of the source scale 2^gamma.","A source transform applies [Gaussian resampling](gaussian-resampling.md) maps and a chirp transform (error under $2dp^2+8TL$), then scales exactly by the source scale $2^\\gamma$ ($b\\ge2^{24}$ gives $\\gamma\\le b/4$ <cite data-source=\"paper\">$b\\ge2^{24}$ implies $\\gamma\\le b/4$</cite>)."),
("E_s","source transform error","The error bound, in units of h_p, of a source transform.","As $2dp^2<TL$ eventually, error is under $E_sh_p$, $E_s=9\\cdot2^\\gamma TL$."),
("u","scaled digit array","The array of scaled digits of the first input.","Here $u,v$ denote the scaled digit arrays (letters redefined): a digit $a$ is stored as $a2^{-b-2}$, norm under $1/4$."),
("v","scaled digit array","The array of scaled digits of the second input.","Here $u,v$ denote the scaled digit arrays (letters redefined): a digit $a$ is stored as $a2^{-b-2}$, norm under $1/4$."),
("U","exact transform of u","The exact source transform of u.","Let $U,V_1$ be their exact source transforms and $\\widetilde U,\\widetilde V_1$ the computed ones, of norm under $.26$."),
("V_1","exact transform of v","The exact source transform of v.","Let $U,V_1$ be their exact source transforms and $\\widetilde U,\\widetilde V_1$ the computed ones, of norm under $.26$."),
("G","exact opposite transform","The exact opposite source transform.","Both source Fourier transforms, $F$ and $F^+$, carry $1/S$, so $F(u*v)=S\\,Fu\\cdot Fv$ and $F^+F=I/S$; the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)), so the exact opposite transform $G$ gives $G(U\\cdot V_1)=(u*v)/S^2$"),
("E_w","first-scaling error","The error bound, in units of h_p, after multiplying by S.","Multiplying exactly by $S$, $\\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$:"),
("Q_0","radix","The radix 2^b of the digits.","With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy"),
("d_j","output digit","The j-th output digit.","With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy"),
("k_j","carry","The carry into position j.","With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy"),
]
sy=[]
for s,n,m,q in SY:
    q=q.replace(' <cite data-source="paper">$b\\ge2^{24}$ implies $\\gamma\\le b/4$</cite>','')
    sy.append({"symbol":s,"name":n,"meaning":m,"relation":"direct","quote":q})
out={"derivations":D,"relations":[{"prerequisite":a,"predicate":b,"quote":c} for a,b,c in R],"symbols":sy}
json.dump(out,open('/home/user/e2e-run/exegenius/tasks/0103-write-precision-recovery.answer.json','w'),indent=1)
