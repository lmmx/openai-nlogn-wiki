import json
t=open('/home/user/e2e-run/exegenius/tasks/0313-write-multiplication-algorithm.answer.md').read()
def sent(start,end=None):
    i=t.index(start)
    j=t.index("\n",i) if end is None else t.index(end,i)+len(end)
    return t[i:j]
sizes=sent("It takes its sizes from","$T$.")
radix=sent("Each input splits into","(radix-digit-reduction.md).")
crt=sent("The convolution is placed","$\\Phi$.")
conv=sent("Let $\\mathcal M_{\\mathbb C}(f,g)","(ring-convolution.md).")
fdef=sent("Let $F_{\\boldsymbol s}$ be","$1/T$.")
chirp=sent("The computed version uses","$p$ fractional bits.")
chirp2=sent("It forms the operand","\\cdot y_0)$.")
exact=sent("Its exact counterpart","row count.")
opp=sent("For an array $z$","F_{\\boldsymbol s}^{+}$.")
step4=sent("4. ","\n")[3:]
perm=sent("Permutations commute","drops out.")
prec=sent("Exactness is shown by","is exact.")
scal=sent("Steps 2 to 4 have exact counterpart","Step 5 gives $2^{2b+4}(u*v)$.")
step1=sent("1. ")[3:]
wsent=sent("4. ")[3:]
def B(sym,name,mean,q): return dict(symbol=sym,name=name,meaning=mean,relation="direct",quote=q)
symbols=[
 B("b","digit width","The number of bits in one radix digit.",sizes),
 B("a_j","radix digit","The j-th radix-2^b digit of an input.",radix),
 B("F_{\\boldsymbol s}","source transform","The discrete Fourier transform on the prime axes s_i, normalized by 1/S.",fdef),
 B("F_{\\boldsymbol s}^+","opposite source transform","The source transform with the opposite sign in the exponent.",fdef),
 B("\\widetilde a","computed chirp","The grid approximation of the chirp a.",chirp),
 B("x_0","first-phase operand","The data operand after the first phase of the computed chirp transform.",chirp2),
 B("y_0","chirp convolution","The computed convolution of the approximate chirp with the data operand.",chirp2),
 B("\\widetilde{\\mathcal M}_{\\mathbb C}","computed convolution","The computed normalized complex cyclic convolution.",chirp2),
 B("R","source permutation","The retained permutation of coordinates from resampling.",exact),
 B("\\widetilde{\\mathscr F}^{+}","computed opposite transform","The computed source transform with the opposite exponent sign.",opp),
 B("z","product array","The array given to the opposite transform: the truncated pointwise product of the two computed source transforms.",opp),
 B("u","source array","The first source array of grid values.",step1),
 B("v","source array","The second source array of grid values.",step1),
 B("w","scaled exact array","The exact array (u*v)/S.",wsent),
 B("\\widetilde w","computed scaled array","The computed approximation of w after multiplying by S.",wsent),
]
def E(pre,pred,q): return dict(prerequisite=pre,predicate=pred,quote=q)
rel=[
 E("parameter-choice","takes its sizes from",sizes),
 E("radix-digit-reduction","splits each input as in",radix),
 E("crt-map","is placed on prime axes by",crt),
 E("phase-twist","is computed through",conv),
 E("ring-convolution","is computed through",conv),
 E("retained-permutations","drops out by",perm),
 E("precision-recovery","has exactness shown by",prec),
]
d=[dict(step="S5.5",quote=exact),dict(step="S5.6",quote=scal)]
for x in d+rel+symbols: assert x['quote'] in t, x['quote']
json.dump(dict(symbols=symbols,relations=rel,derivations=d),open('/home/user/e2e-run/exegenius/tasks/0313-write-multiplication-algorithm.answer.json','w'),indent=1)
