import json
S=[]
def here(sym,q): S.append({"symbol":sym,"anchor":{"kind":"here","quote":q}})
def page(sym,p): S.append({"symbol":sym,"anchor":{"kind":"page","page":p}})
def conc(sym,c): S.append({"symbol":sym,"anchor":{"kind":"concept","concept":c}})
def bg(sym,n): S.append({"symbol":sym,"anchor":{"kind":"background","note":n}})
bg(r"\mathbb F_2","Arithmetic mod 2 / F_2 is covered by the XOR and modular arithmetic background.")
page("m","exchange-network")
Q1=r"Labels are subspaces of $\mathbb F_2^m$, and $u,v,w,z$ are vectors of $\mathbb F_2^m$ here."
for s in "uvwz": here(s,Q1)
Q2=r"Write $\operatorname{wt}(x)$ for the Hamming weight of an address $x\in\mathbb F_2^m$"
here(r"\operatorname{wt}",Q2); here("x",Q2)
Q3=r"$[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$"
here("[b]",Q3); here("b",Q3)
Q4=r"$P_U$ for projection onto a label $U$"
here("P_U",Q4); here("U",Q4)
here(r"\cdot",r"$z\cdot w$ for the dot product")
here("q_U",r"Put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$.")
bg(r"\bmod","Modular arithmetic is covered by elementary number theory.")
page("H","phase-kernel")
bg(r"\operatorname{diag}","Diagonal matrices are covered by first linear algebra.")
bg("i","Imaginary unit, covered by complex numbers in the profile.")
here(r"\mathcal C_U",r"the phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$")
bg(r"\otimes","Tensor power notation is covered by the profile.")
page("C","phase-kernel"); page("a","phase-kernel"); page("I","phase-kernel"); page("X","phase-kernel")
here("X_v",r"$X_v$ the translation $(X_vf)(x)=f(x+v)$")
here("f",r"$X_v$ the translation $(X_vf)(x)=f(x+v)$")
S.append({"symbol":r"\operatorname{supp}","anchor":{"kind":"unbound","quote":r"\operatorname{supp}(z)\cap\operatorname{supp}(w)","note":"The page never says what the support of a vector is (presumably the set of coordinates where it is 1)."}})
Q5=r"Take an edge from $U$ to $V=U\perp E$, with the residual $E$ having orthonormal basis $\mathcal B$."
here("V",Q5); here("E",Q5); here(r"\mathcal B",Q5)
bg(r"\perp","Orthogonal complement and orthogonality are covered by the linear algebra course.")
bg(r"\sum","Summation notation is covered by discrete mathematics.")
here(r"\varepsilon",r"Each term is thus $\varepsilon[v\cdot x]$ with $\varepsilon=\pm1$, including the edge direction.")
here(r"L_{\rm c}",r"Let $L_{\rm c}$ be the total dimension lost on decreasing edges of the complex network.")
page(r"W_{\rm c}","exchange-network"); page("N","exchange-network"); page(r"s_{\rm c}","subspace-labels")
page(r"\mathcal F","subspace-labels"); page("U_a","subspace-labels")
QR=r"Roles (wire names) are scratch wires and data banks $X_a,Y_a$, indexed by $a$ (not the coefficient)."
here("X_a",QR); here("Y_a",QR)
here("a_1",r"$u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$")
here("u_a",r"with $U_a$ the line spanned by $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, each $t_{a_j}$ the indicator of a triple")
here("t_{a_j}",r"each $t_{a_j}$ the indicator of a triple")
bg("j","Index of a product or sum, covered by summation and product notation.")
bg("x_j","The jth coordinate of the bit vector x, covered by bit strings.")
here("k",r"For $k$ columns (addresses are $k$-tuples)")
here("Z",r"With $Z=\operatorname{diag}(1,-1)$")
here("Z_{a,k}",r"Let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column.")
bg(r"\prod","Product notation is covered by discrete mathematics.")
G=[{"term":"support of a vector","quote":r"|\operatorname{supp}(z)\cap\operatorname{supp}(w)|","kind":"term","note":"supp is used without definition; the reader is not told it means the set of coordinates where the vector is 1."}]
json.dump({"symbols":S,"gaps":G},open("/home/user/e2e-run/exegenius/tasks/0147-audit-phase-frames.answer.json","w"),indent=1)
