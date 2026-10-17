import re
import json
p='exegenius/tasks/0171-write-subspace-labels.answer.md'
t=open(p).read()
def sent(start, end):
    i=t.index(start); j=t.index(end,i)+len(end)
    return t[i:j]
def chk(q):
    assert q in t or q in re.sub(r" <cite[^>]*>.*?</cite>","",t), q
    return q
s_open=sent("The labelling chooses","the recursion needs.")
s_nondeg=sent("A subspace $U$ is *nondegenerate*","$U\\perp U^\\perp$.")
s_F=sent("Bit labels live in","for vectors $x,y\\in F$.")
import re
s_F=re.sub(r" <cite[^>]*>.*?</cite>","",s_F)
print(s_F)
t_strip=re.sub(r" <cite[^>]*>.*?</cite>","",t)

s_tri=sent("For *triples*","\\bmod 2$.")
s_tens=sent("Labels are built as","whose form multiplies factorwise.")
s_banks=sent("Banks $X$ and $Y$","=161700$).")
s_Ua="With $U_a=\\langle t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}\\rangle$ the terminal labels are"
s_L=sent("If decreasing edges lose","keep $L$ small.")
s_ABPK=sent("In one invocation of stage $j$","(empty products are scalars).")
s_next=sent("It is the next stage's","stage $j+1$'s inputs.")
s_tXY=sent("Suppressing $K$","(times bracketed) are")
s_Lbc=sent("Each of the $I=3v^2$","centre wires per invocation")
s_Pi=sent("A vertex labelled $U$ gets","else $0$.")
s_V=sent("For $U\\subset V$,","as does its negative.")
s_sb=sent("So $s_{\\rm b}","<W_{\\rm b}m$")
s_sc=sent("[Binary phase frames]","<W_{\\rm c}m$.")
sym=lambda s,n,m,r,q: {"symbol":s,"name":n,"meaning":m,"relation":r,"quote":chk(q)}
symbols=[
 sym("s","number of smaller calls","The total number of smaller calls that the edges of the network cost.","count",s_open),
 sym("W","wire count","The number of wires of the network under consideration.","count",s_open),
 sym("U","a label subspace","A subspace of the label space, such as the label of a vertex.","direct",s_nondeg),
 sym("F","one-factor label space","The space $\\mathbb Q^h$ with the form $x\\cdot y-\\frac19(\\sum_ix_i)(\\sum_iy_i)$ for the bit network, or $\\mathbb F_2^h$ with the dot product for the complex network.","direct",s_F),
 sym("x","vector of F","A vector of $F$, the first argument of the bilinear form.","direct",s_F),
 sym("y","vector of F","A vector of $F$, the second argument of the bilinear form.","direct",s_F),
 sym("T","a triple","A three-element subset of $[h]$ (not the padded size used on other pages).","direct",s_tri),
 sym("t_T","triple indicator","The indicator vector in $F$ of the triple $T$.","direct",s_tri),
 sym("\\mathcal F","ambient label space","The space $F^{\\otimes3}$, of dimension $m=h^3$, in which all labels lie.","direct",s_tens),
 sym("X","X bank","The bank of data wires $X_a$.","direct",s_banks),
 sym("Y","Y bank","The bank of data wires $Y_a$.","direct",s_banks),
 sym("U_a","terminal line","The line spanned by $t_{a_1}\\otimes t_{a_2}\\otimes t_{a_3}$, the source label of $X_a$.","direct",s_Ua),
 sym("L","total dimension loss","The total number of dimensions lost on decreasing edges.","count",s_L),
 sym("j","stage number","The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.","direct",s_ABPK),
 sym("A","exposed factor space","The tensor product $F^{\\otimes(j-1)}$ of the factors exposed before stage $j$.","direct",s_ABPK),
 sym("P","earlier tensor line","The line spanned by $t_{a_1}\\otimes\\cdots\\otimes t_{a_{j-1}}$ inside $A$.","direct",s_ABPK),
 sym("B","complement of P","The orthogonal complement of $P$ inside $A$.","direct",s_ABPK),
 sym("K","later tensor line","The line spanned by $t_{a_{j+1}}\\otimes\\cdots\\otimes t_{a_3}$, tensored onto every label of stage $j$.","direct",s_ABPK),
 sym("A'","next exposed space","The next stage's $A$, equal to $A\\otimes F$.","direct",s_next),
 sym("P'","next earlier line","The next stage's $P$, equal to $P\\otimes\\langle t_{a_j}\\rangle$.","direct",s_next),
 sym("B'","next complement","The next stage's $B$, the orthogonal complement of $P'$ in $A'$.","direct",s_next),
 sym("K'","next later line","The next stage's $K$, with $K=\\langle t_{a_{j+1}}\\rangle\\otimes K'$.","direct",s_next),
 sym("t_X","X-bank indicator","The indicator of the X-bank triple of a gate or side wire in one invocation.","direct",s_tXY),
 sym("t_Y","Y-bank indicator","The indicator of the Y-bank triple of a gate or side wire in one invocation.","direct",s_tXY),
 sym("L_{\\rm b}","bit dimension loss","The total dimension lost on decreasing edges of the bit network.","count",s_Lbc),
 sym("L_{\\rm c}","complex dimension loss","The total dimension lost on decreasing edges of the complex network.","count",s_Lbc),
 sym("\\Pi_U","projection onto a label","The rational projection onto the label $U$ along $U^\\perp$, the matrix of a bit-network vertex labelled $U$.","direct",s_Pi),
 sym("V","larger label","A label containing the label $U$ at the other end of an edge.","direct",s_V),
 sym("s_{\\rm b}","bit smaller calls","The number of smaller calls, the total rational rank of edge matrix differences, in the bit network.","count",s_sb),
 sym("s_{\\rm c}","complex smaller calls","The number of smaller calls, the total number of phase kernels, in the complex network.","count",s_sc),
]
relations=[
 {"prerequisite":"array-frames","predicate":"chooses the frames of","quote":chk(s_open)},
 {"prerequisite":"tensor-product-of-spaces","predicate":"has labels built as","quote":chk(s_tens)},
]
der=[
 ("S1.3.1", sent("Its matrix fixes zero-sum vectors","are orthogonal.")),
 ("S1.3.2", sent("Source dimensions total $N$","=Wm-N$.")),
 ("S1.3.3", sent("A wire enters and leaves each gate","total $Wm-2N$.")),
 ("S1.3.4", sent("Splitting $A=B\\perp P$","ends at $\\mathcal F,U_a^\\perp$.")),
 ("S1.3.5", sent("The same splitting shows","true as $t_X\\perp t_Y$.")),
 ("S1.3.6", sent("The same splitting shows","centre wires per invocation")),
 ("S1.3.9", sent("As $N=v^3$,","Both are below $1/2$.")),
 ("S1.3.7", sent("A vertex labelled $U$ gets","<W_{\\rm b}m$")),
]
for s,q in der:
    assert '<cite' not in q, s
out={"symbols":symbols,"relations":relations,"derivations":[{"step":s,"quote":chk(q)} for s,q in der]}
json.dump(out,open('exegenius/tasks/0171-write-subspace-labels.answer.json','w'),indent=1,ensure_ascii=False)
print("ok")
