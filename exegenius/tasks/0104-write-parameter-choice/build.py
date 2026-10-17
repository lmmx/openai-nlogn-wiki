import json
t=open('0104-write-parameter-choice.answer.md').read()
def seg(start,end=None):
    i=t.index(start)
    j=i+len(start) if end is None else t.index(end,i)+len(end)
    return t[i:j]
D=[]
def d(s,q): D.append({"step":s,"quote":q})
d("S5.1.1",seg("Take $\\tau=\\sigma=1-2^{-50}$, $\\beta=1/2$ and $\\delta=1/16$."))
d("S5.1.2",seg("Take $\\lambda=1-2^{-52}$ and $c=2^{-56}$."))
d("S5.1.3",seg("Take $\\lambda'=1-2^{-54}$."))
d("S5.1.4",seg("Take $C_1=20$, $\\epsilon=2^{-75}$ and $\\kappa=2^{-182}$."))
d("S5.1.5",seg("The layer conditions hold with room to spare","and $\\lambda=1-8\\cdot2^{-55}$."))
d("S5.1.6",seg("Also $\\sigma+\\beta(1-\\sigma)","$\\epsilon C_1=20\\cdot2^{-75}<1$."))
d("S5.1.7",seg("For large $n$ put","$d=\\lfloor b^\\epsilon\\rfloor$."))
d("S5.1.8",seg("Put $K=\\lfloor d^c\\rfloor$","address-chunk width in bits."))
d("S5.1.9",seg("Take the power of two $T$ in $[4n/b,8n/b)$."))
d("S5.1.10",seg("Let $r=2^{","=T$."))
d("S5.1.11",seg("Thus $t_i\\in\\{r/2,r\\}$","$t_d=r$."))
d("S5.1.12",seg("The lemmas assume","at once."))
d("S5.1.13",seg("Put $\\alpha=\\lceil(12d^2b)^{1/4}\\rceil$."))
d("S5.1.14",seg("Put $\\gamma=2d\\alpha^2$ and $\\eta=1/(4d)$."))
d("S5.1.15",seg("As $\\lceil x\\rceil","$\\gamma=o(b)$."))
d("S5.1.16",seg("; both $x=r/2$","o(\\log x)$."))
d("S5.1.17",seg("Choose distinct odd primes","power of two."))
d("S5.1.18",seg("Multiplying the lower bounds","for $d\\ge2$."))
d("S5.1.19",seg("With $s_i<t_i$ this gives $T/2<S<T$."))
d("S5.1.20",seg("With the relative gap","T<2^p$."))
d("S5.1.21",seg("Trial division","not given as advice."))
S=[]
def sym(s,name,mean,rel,q): S.append({"symbol":s,"name":name,"meaning":mean,"relation":rel,"quote":q})
Q1=seg("In the [simultaneous butterfly layer]","resampling-cost exponent.")
for s,n,m in [("\\tau","chunk-swap exponent","An exponent bounding the cost of an equal-width chunk interchange."),
 ("\\sigma","recursion exponent","An exponent bounding the growth of the layer's recursion."),
 ("\\beta","threshold exponent","The exponent of the threshold d^beta of active chunks handled singly."),
 ("\\lambda","node overhead exponent","The exponent of the per-node overhead in the butterfly layer."),
 ("\\lambda'","layer cost exponent","The exponent in the final layer cost O(V d^lambda')."),
 ("c","chunk-width exponent","The exponent giving the chunk width K = floor(d^c)."),
 ("\\epsilon","axis-count exponent","The exponent giving the axis count d = floor(b^epsilon)."),
 ("C_1","guard-bit exponent","The exponent of d in the number of reserved guard bits."),
 ("\\delta","resampling-cost exponent","The exponent delta in the cost of the Gaussian resampling maps.")]:
    sym(s,n,m,"direct",Q1)
sym("V","bit volume","The logical bit volume of the data the layer acts on.","count",Q1)
sym("K","chunk width","The number of bits in an address chunk.","count",seg("Put $K=\\lfloor d^c\\rfloor$","address-chunk width in bits."))
Q2=seg("The lemmas assume","$a_d,b_d,a_r,b_r,C_\\ell$.")
for s,n,m in [("a_d","lower axis constant","The constant in the lower bound a_d p^epsilon <= d."),
 ("b_d","upper axis constant","The constant in the upper bound d <= b_d p^epsilon."),
 ("a_r","lower record constant","The constant in the lower bound 2^{a_r p/d} <= r."),
 ("b_r","upper record constant","The constant in the upper bound r <= 2^{b_r p/d}."),
 ("C_\\ell","address-bit constant","The constant in the bound d*ell <= C_ell p on the total address bits.")]:
    sym(s,n,m,"direct",Q2)
sym("\\eta","relative gap","The relative gap of s_i below t_i, equal to 1/(4d).","direct",seg("Here $\\alpha$ sets","below $t_i$."))
sym("\\theta_i","axis relative gap","The relative gap t_i/s_i - 1 of axis i.","direct",seg("With the relative gap","T<2^p$."))
Q3=seg("Here $x$ is real","o(\\log x)$.")
sym("x","real argument","A real number, the length at which the prime interval is taken.","direct",Q3)
sym("q","integer in interval","An integer, in the prime interval.","direct",Q3)
R=[{"prerequisite":"gaussian-resampling","predicate":"sets the Gaussian width of","quote":seg("Here $\\alpha$ sets","below $t_i$.")},
 {"prerequisite":"crt-map","predicate":"supplies the prime axis lengths of","quote":seg("Put $S=\\prod_is_i$","(crt-map.md).")},
 {"prerequisite":"fixed-point","predicate":"sets the precision of","quote":seg("So $p$ sets","counts the axes.")}]
json.dump({"derivations":D,"symbols":S,"relations":R},open('0104-write-parameter-choice.answer.json','w'),indent=1)
