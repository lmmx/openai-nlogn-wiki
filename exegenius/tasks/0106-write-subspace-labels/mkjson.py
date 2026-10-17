import json,re
page=open('exegenius/tasks/0106-write-subspace-labels.answer.md').read()
stripped=re.sub(r'\s*<cite.*?</cite>','',page,flags=re.S)
def sent(start, end=None):
    i=stripped.index(start)
    if end is None:
        return start
    j=stripped.index(end,i)+len(end)
    return stripped[i:j]
S1="Nested subspace labels give each vertex of the [exchange network](exchange-network.md) a subspace of an $m$-dimensional space, nested along edges, whose dimension changes count each edge's *smaller calls*, recursive calls at an $m$ times smaller parameter."
S2="They choose the frames of [Frames on wire arrays](array-frames.md) so that $W$ wires cost $s<Wm$ smaller calls."
QF=sent("Bit labels live in", "with the dot product.")
QT=sent("For *triples*", "\\bmod 2$.")
QFF=sent("Labels are built as", "multiplies factorwise.")
QX=sent("Banks $X$ and $Y$", "of triples.")
QU=sent("With $U_a=", "the terminal labels are")
QL=sent("If decreasing edges lose", "keep $L$ small.")
QJ=sent("Stage $j$ acts", "coordinate $a_j$.")
QA=sent("In one invocation put", "(empty products are scalars).")
QAp=sent("It is the next stage's", "are stage $j+1$'s inputs.")
QtX=sent("Suppressing $K$", "(times bracketed) are")
QLb=sent("With $I$ invocations", "both below $1/2$.")
QPi=sent("Bit vertices labelled", "other sources ($0$).")
Qsb=sent("So $s_{\\rm b}=", "<W_{\\rm b}m$.")
Qsc=sent("[Binary phase frames](phase-frames.md) give", "<W_{\\rm c}m$.")
def b(sym,name,meaning,rel,q): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=q)
symbols=[
 b("s","number of smaller calls","The total number of smaller calls that the edges of the network cost.","count",S2),
 b("W","wire count","The number of wires of the network under consideration.","count",S2),
 b("F","one-factor label space","The space $\\mathbb Q^h$ with the form $x^{\\mathsf T}y-\\frac19(\\sum_ix_i)(\\sum_iy_i)$ for the bit network, or $\\mathbb F_2^h$ with the dot product for the complex network.","direct",QF),
 b("S","a triple","A three-element subset of $[h]$, used with $T$ to state the indicator inner products.","direct",QT),
 b("T","a triple","A three-element subset of $[h]$ (not the padded size used on other pages).","direct",QT),
 b("t_T","triple indicator","The indicator vector in $F$ of the triple $T$.","direct",QT),
 b("\\mathcal F","ambient label space","The space $F^{\\otimes3}$, of dimension $m=h^3$, in which all labels lie.","direct",QFF),
 b("X","X bank","The bank of data wires $X_a$.","direct",QX),
 b("Y","Y bank","The bank of data wires $Y_a$.","direct",QX),
 b("a","triple tuple","A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.","direct",QX),
 b("U_a","terminal line","The line spanned by $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, the source label of $X_a$.","direct",QU),
 b("L","total dimension loss","The total number of dimensions lost on decreasing edges.","count",QL),
 b("j","stage number","The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.","direct",QJ),
 b("A","exposed factor space","The tensor product $F^{\\otimes(j-1)}$ of the factors exposed before stage $j$.","direct",QA),
 b("P","earlier tensor line","The line spanned by $t_{a_1}\\otimes\\cdots\\otimes t_{a_{j-1}}$ inside $A$.","direct",QA),
 b("B","complement of P","The orthogonal complement of $P$ inside $A$.","direct",QA),
 b("K","later tensor line","The line spanned by $t_{a_{j+1}}\\otimes\\cdots\\otimes t_{a_3}$, tensored onto every label of stage $j$.","direct",QA),
 b("A'","next exposed space","The next stage's $A$, equal to $A\\otimes F$.","direct",QAp),
 b("P'","next earlier line","The next stage's $P$, equal to $P\\otimes\\langle t_{a_j}\\rangle$.","direct",QAp),
 b("B'","next complement","The next stage's $B$, the orthogonal complement of $P'$ in $A'$.","direct",QAp),
 b("K'","next later line","The next stage's $K$, with $K=\\langle t_{a_{j+1}}\\rangle\\otimes K'$.","direct",QAp),
 b("t_X","X-bank indicator","The indicator of the X-bank triple of a gate or wire in one invocation.","direct",QtX),
 b("t_Y","Y-bank indicator","The indicator of the Y-bank triple of a gate or wire in one invocation.","direct",QtX),
 b("L_{\\rm b}","bit dimension loss","The total dimension lost on decreasing edges of the bit network.","count",QLb),
 b("L_{\\rm c}","complex dimension loss","The total dimension lost on decreasing edges of the complex network.","count",QLb),
 b("\\Pi_U","projection onto a label","The rational projection onto the label $U$ along $U^\\perp$, the matrix of a bit-network vertex labelled $U$.","direct",QPi),
 b("s_{\\rm b}","bit smaller calls","The number of smaller calls, the total rational rank of edge matrix changes, in the bit network.","count",Qsb),
 b("s_{\\rm c}","complex smaller calls","The number of smaller calls, the total number of phase kernels, in the complex network.","count",Qsc),
]
relations=[
 dict(prerequisite="array-frames",predicate="chooses the frames of",quote=S2),
 dict(prerequisite="tensor-product-of-spaces",predicate="builds its labels as",quote=QFF),
]
D=lambda st,q: dict(step=st,quote=q)
derivations=[
 D("S1.3.1", sent("For *triples*", "are orthogonal.")),
 D("S1.3.2", sent("Source dimensions total $N$", "=Wm-N$.")),
 D("S1.3.3", sent("A wire enters and leaves", "to $Wm-2N$.")),
 D("S1.3.4", sent("Splitting $A=B", "are stage $j+1$'s inputs.")),
 D("S1.3.5", sent("The same splitting shows", "from $t_X\\perp t_Y$.")),
 D("S1.3.6", sent("The same splitting shows", "loses $L_{\\rm b}=Ic_{\\rm b}h$")),
 D("S1.3.9", sent("as $I=3\\binom h3^2$", "both below $1/2$")),
 D("S1.3.7", sent("For $U\\subset V$", "<W_{\\rm b}m$")),
]
for x in symbols+relations+derivations:
    assert x['quote'] in stripped, x
json.dump(dict(symbols=symbols,relations=relations,derivations=derivations),open('exegenius/tasks/0106-write-subspace-labels.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
