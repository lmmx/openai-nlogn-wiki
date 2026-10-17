import json
H=lambda q:{"kind":"here","quote":q}
P=lambda p:{"kind":"page","page":p}
C=lambda c:{"kind":"concept","concept":c}
B=lambda n:{"kind":"background","note":n}
S=[]
def add(s,a): S.append({"symbol":s,"anchor":a})
add("m",H(r"($m$ the label dimension)"))
add(r"\mathbb F_2",C("Bitwise XOR and arithmetic mod 2"))
for s in "uvwz":
    add(s,H(r"and $u,v,w,z$ are vectors of $\mathbb F_2^m$ here"))
add(r"\operatorname{supp}",H(r"The support $\operatorname{supp}(z)$ of a vector is the set of coordinates where it is $1$."))
add(r"\operatorname{wt}",H(r"Write $\operatorname{wt}(x)=|\operatorname{supp}(x)|$ for the Hamming weight"))
add("x",B("A generic argument of a function or definition (x in f(x), wt(x)); function notation from the profile."))
add("f",B("A generic function being acted on; function notation from the profile."))
add("a",H(r"with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$"))
add("b",H(r"with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$"))
add("P_U",H(r"$P_U$ for projection onto a label $U$"))
add("U",P("subspace-labels"))
add("X_v",H(r"Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$"))
add("X",P("phase-kernel"))
add("C",P("phase-kernel"))
add("H",P("phase-kernel"))
add("I",P("phase-kernel"))
add("i",C("Complex numbers"))
add(r"\operatorname{diag}",C("Matrices and linear operators"))
add("q_U",H(r"For a label $U$ put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$"))
add(r"\mathcal C_U",H(r"The phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$"))
add("V",H(r"Take an edge from $U$ to $V=U\perp E$"))
add("E",H(r"where $E$, the edge residual, has orthonormal basis $\mathcal B$"))
add(r"\mathcal B",H(r"where $E$, the edge residual, has orthonormal basis $\mathcal B$"))
add(r"\varepsilon",H(r"Each term is therefore $\varepsilon[v\cdot x]$ with $\varepsilon=\pm1$ modulo four"))
add("L_{\\rm c}",P("subspace-labels"))
add("N",P("exchange-network"))
add("W_{\\rm c}",P("exchange-network"))
add("s_{\\rm c}",P("subspace-labels"))
add(r"\mathcal F",P("subspace-labels"))
add("U_a",P("subspace-labels"))
add("X_a",P("exchange-network"))
add("Y_a",P("exchange-network"))
add("u_a",H(r"with $U_a$ the line spanned by $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$"))
add("t",{"kind":"unbound","quote":r"$u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$","note":"The page never says what t_{a_j} is (an indicator vector of the three-element subset a_j in F_2^h); t is bound on other pages only as a gate input count or a transform length."})
add("k",H(r"For $k$ columns (an address is a $k$-tuple;"))
add("j",B("Generic coordinate index in a product or sum (x_j, summation notation)."))
add("Z",H(r"With $Z=\operatorname{diag}(1,-1)$"))
add("Z_{a,k}",H(r"Let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column"))
gaps=[{"term":"weight of u_a is 27","quote":"For it take $u=u_a$, with $3^3=27$ ones","kind":"step",
"note":"The page never says what t_{a_j} is. The 27 ones come from each t being the weight-3 indicator vector of a three-element subset of [h] (paper line 861 and 879), so the tensor product has weight 3^3 = 27. The reader cannot check the weight, and the odd weight is what gives u.u=1 and the phase i^{-x_j} on exactly 27 coordinates."}]
json.dump({"symbols":S,"gaps":gaps},open("/home/user/e2e-run/exegenius/tasks/0207-audit-phase-frames.answer.json","w"),indent=1)
