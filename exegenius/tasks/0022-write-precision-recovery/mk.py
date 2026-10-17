import json,re
t=open('0022-write-precision-recovery.answer.md').read()
def sent(start,end):
    i=t.index(start); j=t.index(end,i)+len(end); return t[i:j]
D=[]
def d(step,start,end): D.append({"step":step,"quote":sent(start,end)})
d("S5.7.1","Each synthetic transform has error less than","$L=\\log_2T,$")
d("S5.7.2","Use $h_p=2^{-p}$","less than $ah_p.$")
d("S5.7.3","Replacing the operands of a bilinear","(f,g'-g).$")
d("S5.7.4","Hence, for disk operands","errors add.")
d("S5.7.5","A computed phase product satisfies","$\\|Q_p(\\widetilde ex)\\|\\le\\|x\\|,$")
d("S5.7.6","the ring convolution error is","at most $.7.$")
d("S5.7.7","The computed complex convolution has error","the output untwist.")
d("S5.7.8","The chirp transform has error","8TLh_p.$")
d("S5.7.9","The source transform (error","eventually.")
d("S5.7.10","The computed product $z=","plus truncation.")
d("S5.7.11","The opposite transform gives error","with $G$ exact.")
d("S5.7.12","After the first exact multiplication by $S:$","T^2L.$")
d("S5.7.13","After the second scaling by","2^{-6b}.$")
d("S5.7.14","Using $S\\le T<2^b,$","2^{-b+\\gamma}.$")
d("S5.7.15","Since $\\gamma\\le b/4$","<1/2.$")
d("S5.7.16","The true coefficients are integers","correct coefficient.")
d("S5.7.17","The carries obey $k_0=0,$","$Q_0=2^b.$")
d("S5.7.18","The carries satisfy $0\\le k_j","qQ_0(Q_0-1).$")
d("S5.7.19","The invariant $\\sum","are fixed.")
d("S5.7.20","The exact product is less than","are output.")
R=[{"prerequisite":"fixed-point","predicate":"runs on","quote":sent("The computation runs on","(fixed-point.md).")},
{"prerequisite":"radix-digit-reduction","predicate":"recovers the coefficients of","quote":sent("We recover the coefficients","an $n$-bit input.")}]
def B(sym,name,mean,quote,rel="direct"):
    return {"symbol":sym,"name":name,"meaning":mean,"relation":rel,"quote":quote}
q1=sent("Let $b$ be","axis count.")
S=[B("b","digit width","The number of bits in a radix digit.",q1,"count"),
B("p","fractional bits","The number of fractional bits of the fixed-point grid, equal to $6b$.",q1,"count"),
B("T","padded array size","The number of records in the padded array.",q1,"count"),
B("S","convolution length","The length of the cyclic convolution.",q1,"count"),
B("L","log of T","The base-2 logarithm of $T$.",q1),
B("\\gamma","source scale exponent","The exponent of the source-transform scale $2^\\gamma$.",q1),
B("d","axis count","The number of transform axes.",q1,"count"),
B("h_p","grid step","The grid step $2^{-p}$.",sent("Use $h_p=2^{-p}$","less than $ah_p.$")),
B("\\ell","log of r","The base-2 logarithm of the record length $r$.",sent("Each synthetic transform has error","$\\ell=\\log_2r.$")),
B("M","ring record count","The ratio $T/r$, the number of ring records.",sent("With $M=T/r$","at most $.7.$")),
B("q","digit count","The number of radix digits of an $n$-bit input.",sent("We recover the coefficients","an $n$-bit input."),"count"),
B("Q_0","radix","The radix $2^b$ of the digits.",sent("The carries obey $k_0=0,$","$Q_0=2^b.$")),
]
json.dump({"derivations":D,"relations":R,"symbols":S},open('0022-write-precision-recovery.answer.json','w'),indent=1)
