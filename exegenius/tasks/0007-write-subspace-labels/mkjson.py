import json,re,sys
page=open('0007-write-subspace-labels.answer.md').read()
def find(start,end):
    i=page.index(start); j=page.index(end,i)+len(end)
    return page[i:j]
symbols=[
 dict(symbol="m",name="label dimension",meaning="The dimension of the ambient label space, $m=h^3=10^6$.",relation="direct",
      quote=find("Nested subspace labels give","nested along every edge.")),
 dict(symbol="s",name="number of smaller calls",meaning="The total number of smaller calls that the edges of the network cost.",relation="count",
      quote=find("They choose the frames","number of wires.")),
 dict(symbol="W",name="wire count",meaning="The number of wires of the network under consideration.",relation="count",
      quote=find("They choose the frames","number of wires.")),
 dict(symbol="h",name="ground-set size",meaning="The size of the ground set whose three-element subsets index the network, $h=100$.",relation="count",
      quote=find("With $h=100$","$F=\\mathbb F_2^h$.")),
 dict(symbol="F",name="label field space",meaning="The space $\\mathbb Q^h$ (bit network) or $\\mathbb F_2^h$ (complex network) in which the one-coordinate labels live.",relation="direct",
      quote=find("With $h=100$","$F=\\mathbb F_2^h$.")),
 dict(symbol="t_T",name="triple indicator",meaning="The indicator vector in $F$ of a triple $T$.",relation="direct",
      quote="For a triple $T$, $t_T$ is its indicator vector."),
 dict(symbol="\\mathcal F",name="ambient label space",meaning="The space $F^{\\otimes3}$ of $h\\times h\\times h$ arrays, of dimension $m$, in which all labels lie.",relation="direct",
      quote=find("$\\mathcal F=F^{\\otimes3}$, of dimension","\\dim U\\dim V$.")),
 dict(symbol="N",name="bank size",meaning="The number of index tuples $a$, so the number of wires in each data bank.",relation="count",
      quote=find("Data wires $X_a,Y_a$","such tuples.")),
 dict(symbol="U_a",name="terminal line",meaning="The line spanned by $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, the source label of $X_a$.",relation="direct",
      quote=find("With $U_a=","the terminal labels are")),
 dict(symbol="L",name="total dimension loss",meaning="The total dimension lost on decreasing edges.",relation="count",
      quote=find("If decreasing edges lose","keeping $L$ small.")),
]
stage=find("At stage $j$, invocations vary","at stage $1$).")
for sym,name,mean in [("j","stage number","The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$."),
    ("A","earlier factor space","The tensor product $F^{\\otimes(j-1)}$ of the factors already exposed at stage $j$."),
    ("P","earlier tensor line","The line spanned by $t_{a_1}\\otimes\\cdots\\otimes t_{a_{j-1}}$ inside $A$."),
    ("B","complement of P","The orthogonal complement of $P$ inside $A$."),
    ("K","later tensor line","The line spanned by $t_{a_{j+1}}\\otimes\\cdots\\otimes t_{a_3}$.")]:
    symbols.append(dict(symbol=sym,name=name,meaning=mean,relation="count" if sym=="j" and False else "direct",quote=stage))
symbols.append(dict(symbol="I",name="invocation count",meaning="The number of invocations over the three stages.",relation="count",
      quote="With $I$ invocations of $\\gamma$ central wires each, $L=I\\gamma h$."))
symbols.append(dict(symbol="\\gamma",name="central wires per invocation",meaning="The number of central wires in each invocation, 100 (bit) or 101 (complex).",relation="count",
      quote="With $I$ invocations of $\\gamma$ central wires each, $L=I\\gamma h$."))
symbols.append(dict(symbol="\\Pi_U",name="projection onto a label",meaning="The projection onto the label $U$ along $U^\\perp$, the matrix assigned to a gate or sink labelled $U$.",relation="direct",
      quote=find("In the bit network each vertex gets","at other sources.")))
relations=[dict(prerequisite="array-frames",predicate="choose the frames of",quote=find("They choose the frames","number of wires."))]
derivations=[
 dict(step="S1.3.1",quote=find("As $t_S^{\\mathsf T}t_T","have orthogonal indicators.")),
 dict(step="S1.3.2",quote=find("Source dimensions sum to $N$","=Wm-N$.")),
 dict(step="S1.3.3",quote=find("Each gate's wires carry","$Wm-2N$ in total.")),
 dict(step="S1.3.4",quote=find("With $A'=A\\otimes F$","$\\mathcal F$, $U_a^\\perp$.")),
 dict(step="S1.3.5",quote=find("Splitting $A=B\\perp P$","needs $t_X\\perp t_Y$.")),
 dict(step="S1.3.6",quote=find("Splitting $A=B\\perp P$","$L=I\\gamma h$.")+" "),
 dict(step="S1.3.9",quote=find("As $I=3\\binom h3^2$","$\\gamma=101$ (complex).")),
 dict(step="S1.3.7",quote=find("For $U\\subset V$, $\\Pi_V-\\Pi_U$","with no dimension change.")),
]
derivations[5]["quote"]=derivations[5]["quote"].strip()
json.dump(dict(symbols=symbols,relations=relations,derivations=derivations),open('0007-write-subspace-labels.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
