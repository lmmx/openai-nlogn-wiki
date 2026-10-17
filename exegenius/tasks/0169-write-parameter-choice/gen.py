import json
t=open('/home/user/e2e-run/exegenius/tasks/0169-write-parameter-choice.answer.md').read()
def span(a,b):
    i=t.index(a); j=t.index(b,i)+len(b)
    return t[i:j]
D=[]
def d(s,a,b): D.append({"step":s,"quote":span(a,b)})
d("S5.1.1","Take $\\tau=\\sigma","$\\delta=1/16$.")
d("S5.1.2","Take $\\lambda=1-2^{-52}$","$c=2^{-56}$.")
d("S5.1.3","Take $\\lambda'=1-2^{-54}$.","$\\lambda'=1-2^{-54}$.")
d("S5.1.4","Take $C_1=20$","$\\kappa=2^{-182}$.")
d("S5.1.5","The layer conditions hold with room to spare:","$\\lambda=1-8\\cdot2^{-55}$.")
d("S5.1.6","Also $\\sigma+\\beta(1-\\sigma)","$\\epsilon C_1=20\\cdot2^{-75}<1$.")
d("S5.1.7","For large $n$ put","$d=\\lfloor b^\\epsilon\\rfloor$.")
d("S5.1.8","Put $K=","address chunk.")
d("S5.1.9","Take the power of two $T$","$Tp\\in[24n,48n)$.")
d("S5.1.10","Let $r=2^","with the last axis of length $r$.")
d("S5.1.11","Thus $t_i\\in","$t_d=r$.")
d("S5.1.12","These choices give $Tp=","fixed for all lengths at once.")
d("S5.1.13","Put $\\alpha=","resampling.")
d("S5.1.14","Put $\\gamma=2d\\alpha^2$","$\\eta=1/(4d)$.")
d("S5.1.15","As $\\lceil A\\rceil","$\\gamma=o(b)$.")
d("S5.1.16","Both $x=r/2$","=o(\\log x)$.")
d("S5.1.17","Choose distinct odd primes","power of two.")
d("S5.1.18","Multiplying the lower bounds","1-d/(2d)$.")
d("S5.1.19","With $s_i<t_i$ this gives","$T/2<S<T$.")
d("S5.1.20","With $\\theta_i","<2^p$.")
d("S5.1.21","The deterministic search","not given as advice.")
R=[
{"prerequisite":"gaussian-resampling","predicate":"fixes size for the hypotheses of","quote":span("This page fixes","hold at once.")},
{"prerequisite":"crt-map","predicate":"supplies the prime axis lengths of","quote":span("This choice supplies the prime axis lengths","(crt-map.md).")},
{"prerequisite":"fixed-point","predicate":"sets the precision of","quote":span("Here $b$ is the digit width","axis count.")},
]
big=span("In the [simultaneous butterfly layer]","resampling-cost slack.")
def S(sym,name,meaning,rel,quote): return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":quote}
syms=[
S("\\tau","chunk-interchange exponent","The exponent in the cost of a chunk interchange.","direct",big),
S("\\sigma","recursion growth exponent","An exponent bounding the growth of the number of recursive calls.","direct",big),
S("\\beta","active-chunk threshold exponent","The exponent in the threshold d^beta below which active chunks are handled singly.","direct",big),
S("\\lambda","overhead exponent","The per-node overhead exponent.","direct",big),
S("\\lambda'","final cost exponent","The final exponent of the cost V d^lambda' on bit volume V.","direct",big),
S("V","bit volume","The number of bits of the logical array the layer acts on.","count",big),
S("c","chunk-width exponent","The exponent of the address-chunk width (a new meaning of c).","direct",big),
S("\\epsilon","axis-count exponent","The exponent of the axis count.","direct",big),
S("C_1","guard-bit exponent","The exponent of the guard bits.","direct",big),
S("\\delta","resampling slack","The slack in the exponent of the resampling cost.","direct",big),
S("K","chunk width","The width in bits of an address chunk.","count",span("Put $K=","address chunk.")),
S("\\eta","prime window offset","The smallest relative distance at which a prime s_i may lie below t_i.","direct",span("Put $\\gamma=2d\\alpha^2$","below $t_i$.")),
]
json.dump({"derivations":D,"relations":R,"symbols":syms},open('/home/user/e2e-run/exegenius/tasks/0169-write-parameter-choice.answer.json','w'),indent=1)
