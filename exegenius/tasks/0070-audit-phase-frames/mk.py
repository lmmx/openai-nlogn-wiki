import json
def here(s,q): return {"symbol":s,"anchor":{"kind":"here","quote":q}}
def page(s,p): return {"symbol":s,"anchor":{"kind":"page","page":p}}
def conc(s,c): return {"symbol":s,"anchor":{"kind":"concept","concept":c}}
def bg(s,n): return {"symbol":s,"anchor":{"kind":"background","note":n}}
def unb(s,q,n): return {"symbol":s,"anchor":{"kind":"unbound","quote":q,"note":n}}
syms=[
here("m","Here $m$ is the number of binary coordinates of an address $x$"),
here("x","Here $m$ is the number of binary coordinates of an address $x$"),
here("U","a label $U$ is a subspace of $\\mathbb F_2^m$"),
bg("\\mathbb F_2","Field with two elements: arithmetic mod 2 / XOR from the machine-level binary background."),
here("\\operatorname{wt}","Write $\\operatorname{wt}(x)$ for Hamming weight"),
here("[b]","$[b]\\in\\{0,1\\}$ for the integer representative of $b\\in\\mathbb F_2$"),
here("P_U","$P_U$ for the projection onto $U$ over $\\mathbb F_2$"),
here("q_U","Put $q_U(x)=\\operatorname{wt}(P_Ux)\\bmod 4$"),
here("H","With $H=\\tfrac1{\\sqrt2}\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$"),
bg("i","Complex numbers: imaginary unit."),
bg("\\operatorname{diag}","Matrices (diagonal matrix) from first linear algebra course."),
here("\\mathcal C_U","the phase frame is $\\mathcal C_U=H^{\\otimes m}\\operatorname{diag}_x(i^{q_U(x)})H^{\\otimes m}$"),
page("C","phase-kernel"),
page("a","phase-kernel"),
page("b","phase-kernel"),
page("X","phase-kernel"),
bg("I","Identity matrix, first linear algebra course."),
here("X_v","$X_v$ the translation $(X_vf)(x)=f(x+v)$"),
here("v","$X_v$ the translation $(X_vf)(x)=f(x+v)$"),
bg("f","Generic function of the address, as in the page's own formula (X_v f)(x)=f(x+v)."),
here("z","For binary vectors $z,w$"),
here("w","For binary vectors $z,w$"),
bg("\\operatorname{supp}","Support (set of nonzero coordinates) of a binary vector; discrete mathematics/linear algebra."),
here("V","Take an edge from $U$ to $V=U\\perp E$"),
here("E","with residual $E$ orthogonal to $U$"),
here("\\mathcal B","orthonormal basis $\\mathcal B$"),
here("\\varepsilon","so each term is $\\varepsilon[v\\cdot x]$, $\\varepsilon=\\pm1$"),
page("W_{\\rm c}","exchange-network"),
page("N","exchange-network"),
unb("L_{\\rm c}","$N$, $L_{\\rm c}$ are constants of the labels page","The page only says it is a constant of the labels page; it does not say what it counts (the total dimension loss on decreasing edges of the complex network)."),
here("s_{\\rm c}","the number of translation-kernel factors is $s_{\\rm c}=W_{\\rm c}m-2N+2L_{\\rm c}"),
here("d","A residual of dimension $d$ costs $d$ such calls"),
page("U_a","subspace-labels"),
unb("u","For the pair $X_a\\to Y_a$, take $u=u_a$ of binary norm one and weight $27$.","The page never says what u_a is (a vector generating the line U_a, presumably), nor how it is obtained."),
unb("X_a","For the pair $X_a\\to Y_a$","X_a is not defined on this page; it names a role of the network, not explained here."),
unb("Y_a","For the pair $X_a\\to Y_a$","Y_a is not defined on this page; it names a role of the network, not explained here."),
here("Z","Let $Z=\\operatorname{diag}(1,-1)$"),
here("k","For $k$ columns, let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column."),
here("Z_{a,k}","let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column"),
]
gaps=[
{"term":"columns","kind":"term","quote":"For $k$ columns, let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column.",
 "note":"The page never says what a column is: the idea of an address for k columns (k-fold tuples of addresses, with every frame and edge operator taken as a tensor power over the columns) is not introduced, though C^{\\otimes mk} depends on it. In the paper (around lines 1195-1200) this is set up before the proposition."},
{"term":"the exceptional pair X_a to Y_a and u_a","kind":"step","quote":"For the pair $X_a\\to Y_a$, take $u=u_a$ of binary norm one and weight $27$.",
 "note":"The page does not say what X_a, Y_a, u_a are, why this pair is different from the others, why u_a has weight 27 (paper line 1291: 3^3=27), or that the edge runs from the label U_a to U_a^perp. The reader cannot check these from the page."},
{"term":"orthogonal additivity for U_a^perp","kind":"step","quote":"Orthogonal additivity gives $\\operatorname{wt}(x)-2\\operatorname{wt}(u)[u\\cdot x]$",
 "note":"The page never states that x splits as P_{U_a}x plus P_{U_a^perp}x with orthogonal parts, so wt(x)=q_U+q_{U^perp} mod 4 and q_{U^perp}-q_U=wt(x)-2q_U with q_U(x)=wt(u)[u.x]. The single-edge computation was done for V=U perp E, not this setting, so the formula does not follow from what the page gives."},
{"term":"all roles receive C^{\\otimes mk}","kind":"step","quote":"so every role, scratch roles included, receives $C^{\\otimes mk}$",
 "note":"The page never says what the other roles receive (zero label has frame I, full label has frame C^{\\otimes m} since q_F(x)=wt(x); source and sink corrections; undoing the signed exchange and the minus sign on X outputs; paper lines 1280-1310). The conclusion for scratch roles is asserted without these steps."},
]
json.dump({"symbols":syms,"gaps":gaps},open("/home/user/e2e-run/exegenius/tasks/0070-audit-phase-frames.answer.json","w"),indent=1)
