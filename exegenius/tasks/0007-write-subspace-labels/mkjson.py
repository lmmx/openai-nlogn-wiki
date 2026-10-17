import json
page=open('0007-write-subspace-labels.answer.md').read()
def find(start,end):
    i=page.index(start); j=page.index(end,i)+len(end)
    return page[i:j]
S=[]
def sym(symbol,name,meaning,relation,quote): S.append(dict(symbol=symbol,name=name,meaning=meaning,relation=relation,quote=quote))
first=find("Nested subspace labels give","the edge's smaller calls.")
frames=find("They choose the frames","smaller calls.")
import re
triples=re.sub(r" <cite[^>]*>.*?</cite>","",find("*Triples* (three-element","with the dot product."))
stage=find("Stage $j$ varies","(empty products are scalars).")
inv="With $I$ invocations of $\\gamma$ central wires each, $L=I\\gamma h$."
sym("m","label-space dimension","The dimension of the ambient label space, $m=h^3=10^6$.","direct",first)
sym("W","wire count","The number of wires of the network under consideration.","count",frames)
sym("s","number of smaller calls","The total number of smaller calls that the network's edges cost.","count",frames)
sym("h","ground-set size","The size of the ground set whose three-element subsets index the network, $h=100$.","count",triples)
sym("F","one-factor label space","The space $\\mathbb Q^h$ (bit network) or $\\mathbb F_2^h$ (complex network) with its bilinear form.","direct",triples)
sym("t_T","triple indicator","The indicator vector in $F$ of a triple $T$.","direct",find("Indicator vectors $t_S,t_T$","\\bmod 2$."))
sym("\\mathcal F","ambient label space","The space $F^{\\otimes3}$ of $h\\times h\\times h$ arrays, of dimension $m$, in which all labels lie.","direct",find("The space $\\mathcal F","\\dim U\\dim V$."))
sym("N","bank size","The number of index tuples $a$ of triples, so the number of wires in each data bank.","count",find("$N$ counts the tuples","$X_a,Y_a$."))
sym("U_a","terminal line","The line spanned by $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, the source label of $X_a$.","direct",find("With $U_a=","the terminal labels are"))
sym("L","total dimension loss","The total dimension lost on decreasing edges.","count",find("If decreasing edges lose","small $L$."))
sym("j","stage number","The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.","direct",stage)
sym("A","exposed factor space","The tensor product $F^{\\otimes(j-1)}$ of the factors already exposed before stage $j$.","direct",stage)
sym("P","earlier tensor line","The line spanned by $t_{a_1}\\otimes\\cdots\\otimes t_{a_{j-1}}$ inside $A$.","direct",stage)
sym("B","complement of P","The orthogonal complement of $P$ inside $A$.","direct",stage)
sym("K","later tensor line","The line spanned by $t_{a_{j+1}}\\otimes\\cdots\\otimes t_{a_3}$, tensored onto every label of stage $j$.","direct",stage)
sym("I","invocation count","The number of invocations over all three stages.","count",inv)
sym("\\gamma","central wires per invocation","The number of central wires in one invocation: 100 in the bit network, 101 in the complex one.","count",inv)
sym("\\Pi_U","projection onto a label","The rational projection onto the label $U$ along $U^\\perp$, the matrix given to a bit-network vertex labelled $U$.","direct",find("Bit vertices labelled $U$","($-\\Pi_{U_a}$)."))
relations=[dict(prerequisite="array-frames",predicate="choose the frames of",quote=frames)]
derivations=[
 dict(step="S1.3.1",quote=find("Indicator vectors $t_S,t_T$","are orthogonal.")),
 dict(step="S1.3.2",quote=find("Source dimensions total","=Wm-N$.")),
 dict(step="S1.3.3",quote=find("Gate wires share","to $Wm-2N$.")),
 dict(step="S1.3.4",quote=find("With $A'=A\\otimes F","$\\mathcal F,U_a^\\perp$.")),
 dict(step="S1.3.5",quote=find("Splitting $A=B\\perp P$","needs $t_X\\perp t_Y$.")),
 dict(step="S1.3.6",quote=find("Splitting $A=B\\perp P$","$L=I\\gamma h$.")),
 dict(step="S1.3.9",quote=find("As $I=3\\binom h3^2$","for $\\gamma=100,101$")),
 dict(step="S1.3.7",quote=find("For $U\\subset V$","its dimension change zero.")),
]
json.dump(dict(symbols=S,relations=relations,derivations=derivations),open('0007-write-subspace-labels.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
