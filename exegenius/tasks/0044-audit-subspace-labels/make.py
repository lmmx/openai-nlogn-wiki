import json
def here(s,q): return {"symbol":s,"anchor":{"kind":"here","quote":q}}
def page(s,p): return {"symbol":s,"anchor":{"kind":"page","page":p}}
def conc(s,c): return {"symbol":s,"anchor":{"kind":"concept","concept":c}}
def bg(s,n): return {"symbol":s,"anchor":{"kind":"background","note":n}}
PQ=r"Stage $j$ varies $a_j$; put $A=F^{\otimes(j-1)},\ P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle,\ B=P^\perp\cap A,\ K=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$"
PQ=r"put $A=F^{\otimes(j-1)},\ P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle,\ B=P^\perp\cap A,\ K=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$"
AP=r"With $A'=A\otimes F,\ B'=(P\otimes\langle t_{a_j}\rangle)^\perp_{A'},\ K=\langle t_{a_{j+1}}\rangle\otimes K'$"
sy=[
here("F",r"bit labels live in $F=\mathbb Q^h$"),
bg(r"\mathbb Q","Rational numbers, covered by the undergraduate background (discrete mathematics, linear algebra over the rationals)."),
page("h","exchange-network"),
bg("x","Generic vectors in the bilinear form; standard linear algebra."),
bg("y","Generic vectors in the bilinear form; standard linear algebra."),
bg("z","Generic vector in the tensor product; standard linear algebra."),
here(r"\langle x,y\rangle",r"the nondegenerate form $\langle x,y\rangle=x^{\mathsf T}y"),
bg(r"\mathsf T","Matrix transpose, from a first linear algebra course."),
bg("i","Summation/array index, standard summation notation."),
bg("k","Array index, standard notation."),
bg("l","Array index, standard notation."),
here("S",r"Indicator vectors $t_S,t_T$ of triples $S,T$"),
here("T",r"Indicator vectors $t_S,t_T$ of triples $S,T$"),
here("t_S",r"Indicator vectors $t_S,t_T$ of triples $S,T$"),
here("t_T",r"Indicator vectors $t_S,t_T$ of triples $S,T$"),
bg(r"\cap","Set intersection and cardinality, from discrete mathematics."),
conc(r"\mathbb F_2","bitwise-xor-and-arithmetic-mod-2"),
conc(r"\perp","orthogonality-and-inner-products"),
here(r"\otimes",r"$x\otimes y\otimes z$ has entries $x_iy_kz_l$"),
here(r"\mathcal F",r"The space $\mathcal F=F^{\otimes3}$ of $h\times h\times h$ arrays has dimension $m=h^3$"),
page("m","exchange-network"),
conc(r"\dim","vector-spaces-subspaces-dimension-and-rank"),
bg("U","Generic subspaces; standard linear algebra."),
bg("V","Generic subspaces; standard linear algebra."),
page("N","exchange-network"),
here("a",r"$N$ counts the tuples $a=(a_1,a_2,a_3)$ of triples indexing the data wires $X_a,Y_a$"),
here("a_1",r"$N$ counts the tuples $a=(a_1,a_2,a_3)$ of triples indexing the data wires $X_a,Y_a$"),
here("X_a",r"the data wires $X_a,Y_a$"),
here("Y_a",r"the data wires $X_a,Y_a$"),
here("U_a",r"With $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$ the terminal labels are"),
here("W",r"a network of $W$ wires makes $s<Wm$ smaller calls"),
here("s",r"a network of $W$ wires makes $s<Wm$ smaller calls"),
here("L",r"If decreasing edges lose $L$ dimensions in all"),
here("j",r"Stage $j$ varies $a_j$"),
here("A",PQ),here("P",PQ),here("B",PQ),here("K",PQ),
here("A'",AP),here("B'",AP),here("K'",AP),
here("t_X",r"$t_X,t_Y$ the $X$ and $Y$ triples a side wire joins"),
here("t_Y",r"$t_X,t_Y$ the $X$ and $Y$ triples a side wire joins"),
here("X",r"$t_X,t_Y$ the $X$ and $Y$ triples a side wire joins"),
here("Y",r"$t_X,t_Y$ the $X$ and $Y$ triples a side wire joins"),
page("I","exchange-network"),
here(r"\gamma",r"With $I$ invocations of $\gamma$ central wires each"),
bg(r"\binom h3","Binomial coefficient, from discrete mathematics."),
here(r"\Pi_U",r"get the rational projection $\Pi_U$ onto $U$ along $U^\perp$"),
here(r"\Pi_V",r"For $U\subset V$, $\Pi_V-\Pi_U$"),
bg(r"\mathrm{Id}","Identity matrix, from linear algebra."),
page("W_{\\rm b}","exchange-network"),
page("W_{\\rm c}","exchange-network"),
here("s_{\\rm b}",r"An edge costs one smaller call per unit of rank (cited), so $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N"),
here("s_{\\rm c}",r"give the complex network $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$"),
here("L_{\\rm b}",r"$L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ for $\gamma=100,101$"),
here("L_{\\rm c}",r"$L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ for $\gamma=100,101$"),
]
gaps=[
{"term":"tensor product of subspaces","quote":r"forms multiply factorwise and $\dim(U\otimes V)=\dim U\dim V$","kind":"term",
 "note":"The reader has not been taught tensor products. The page gives entries only for x⊗y⊗z of vectors, but then uses U⊗V for subspaces (B⊗F, P⊗⟨t⟩, (…)⊗K, orthogonal complements inside A⊗F) without saying that U⊗V is the span of the products u⊗v, or how it sits inside 𝓕."},
{"term":"Y output label equals B' (identity never stated)","quote":r"are stage $j+1$'s inputs","kind":"step",
 "note":"The page writes the Y output as (P⊗⟨t⟩)^⊥ inside A⊗F, the next stage's B' uses that, and the side/Y rows of the stage table give the same label at time 5 as (B⊗F)⊥(P⊗t_Y^⊥). The page never states that (P⊗⟨t⟩)^⊥_{A⊗F} = (B⊗F)⊥(P⊗t^⊥) (paper lines 921-930), so the reader cannot check that the table's time-5 label matches the Y output or the next stage's input."},
]
json.dump({"symbols":sy,"gaps":gaps},open("/home/user/e2e-run/exegenius/tasks/0044-audit-subspace-labels.answer.json","w"),indent=1,ensure_ascii=False)
