import json
md=open('../0039-write-cost-accounting.answer.md').read()
def sent(start,end=None):
    i=md.index(start)
    j=md.index('\n',i) if end is None else md.index(end,i)+len(end)
    return md[i:j]
q1=sent("Cost accounting totals","saved exponent.")
q2=sent("Let $T$","the volume.")
q3=sent("Here $d$","of axis $i$.")
q4=sent("The fixed exponents","$\\alpha=\\Theta(p^{1/4+\\epsilon/2})$.")
q5=sent("Fixed exponents $A$","the total is small")
d1=sent("Dividing by $V$","absorbed into them.") if "absorbed into them." in md else sent("Dividing by $V$","Seven dominate.")
d2=sent("Substituting the fixed","=2\\kappa$")
d3=sent("The layout needs","=O(pK^{\\tau-1})$.")
d3b=sent("Each of at most $\\ell$","layer](simultaneous-layer.md).")
d4=sent("Repairing the fraction","prime search.")
d5=sent("Each of the seven powers","^{1-\\kappa})$")
S=lambda sym,name,mean,rel,q:dict(symbol=sym,name=name,meaning=mean,relation=rel,quote=q)
ans=dict(
symbols=[
S("\\kappa","saved exponent","The exponent saved below one in the time bound, 2^{-182}.","direct",q1),
S("T","coefficient count","The number of coefficients in the padded array.","count",q2),
S("p","precision","The number of bits per coefficient.","count",q2),
S("V","volume","The number of stored bits, Tp = Theta(n).","count",q2),
S("d","axis count","The number of transform axes.","count",q3),
S("K","chunk width","The width of an exchanged address chunk.","direct",q3),
S("\\ell","record address bits","The number of address bits of a record, log_2 r.","count",q3),
S("\\alpha","Gaussian window width","The width of the Gaussian window in resampling.","direct",q3),
S("t_i","axis length","The length of axis i.","direct",q3),
S("\\epsilon","axis exponent","Fixed exponent 2^{-75} with d = Theta(p^epsilon).","direct",q4),
S("c","chunk exponent","Fixed exponent 2^{-56} with K = Theta(p^{epsilon c}).","direct",q4),
S("\\delta","resampling exponent","Fixed exponent 1/16 in the Gaussian resampling cost.","direct",q4),
S("\\tau","interchange exponent","Fixed exponent 1-2^{-50} of the chunk interchange cost.","direct",q4),
S("\\lambda'","butterfly exponent","Fixed exponent 1-2^{-54} of the simultaneous butterfly layer cost.","direct",q4),
S("A","visit exponent","Fixed exponent bounding the number of recursion visits by p^A.","direct",q5),
S("C","setup exponent","Fixed exponent bounding the setup per visit by p^C.","direct",q5),
],
relations=[
dict(prerequisite="multiplication-algorithm",predicate="totals the running time of",quote=q1),
dict(prerequisite="address-interchange",predicate="bounds each cost in",quote=d3),
dict(prerequisite="simultaneous-layer",predicate="bounds rounds in",quote=d3b),
],
derivations=[dict(step=s,quote=q) for s,q in [("S6.1",d1),("S6.2",d2),("S6.3",d3),("S6.4",d4),("S6.5",d5)]])
json.dump(ans,open('../0039-write-cost-accounting.answer.json','w'),indent=1)
