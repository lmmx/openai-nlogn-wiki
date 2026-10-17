import json
def s(sym,name,meaning,rel,quote): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=quote)
d={
"symbols":[
 s("d","axis count","The number of axes of the arrays f and g.","count","Let $f$ and $g$ be complex arrays with $d$ axes, the last of length $r$, and $T$ entries in all."),
 s("f","first array","A complex array with d axes, the last of length r.","direct","Let $f$ and $g$ be complex arrays with $d$ axes, the last of length $r$, and $T$ entries in all."),
 s("g","second array","The second complex array, with the same shape as f.","direct","Let $f$ and $g$ be complex arrays with $d$ axes, the last of length $r$, and $T$ entries in all."),
 s("x_d","last axis variable","The variable of the last cyclic axis.","direct","But convolution along it is multiplication in $\\mathbb C[x_d]/(x_d^r-1)$, where $x_d$ is the variable of that axis and the wrap is cyclic, whereas in $\\mathcal R_r$ the wrap changes sign."),
 s("\\mathcal R_r","negacyclic ring","The ring of polynomials in y modulo y^r+1 over the complex numbers.","direct","The fast convolution of the later stages, [Convolution from the retained transform layout](ring-convolution.md), convolves the first $d-1$ axes of an array whose entries are records in $\\mathcal R_r=\\mathbb C[y]/(y^r+1)$."),
 s("\\zeta","twist phase","The complex number e^{\\pi i/r}, with \\zeta^r=-1.","direct","Let $\\zeta=e^{\\pi i/r}$, so $\\zeta^r=-1$."),
 s("\\Theta","twist map","The ring isomorphism from C[x_d]/(x_d^r-1) to R_r sending x_d to \\zeta y.","direct","Define $\\Theta:\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$ by $x_d\\mapsto\\zeta y$."),
 s("k","coefficient index","The index of a coefficient along the last axis (here not a depth).","direct","Here $k$ and $l$ index coefficients along the last axis (not depth)."),
 s("l","second coefficient index","The index of a second coefficient along the last axis.","direct","Here $k$ and $l$ index coefficients along the last axis (not depth)."),
 s("j","wrapped position","The position in 0..r-1 of a product term after reduction.","direct","Take $k,l<r$ and write $k+l=j+hr$, with $j<r$ the resulting position and $h\\in\\{0,1\\}$ the wrap indicator."),
 s("h","wrap indicator","Zero or one, the number of times the index k+l wraps past r.","direct","Take $k,l<r$ and write $k+l=j+hr$, with $j<r$ the resulting position and $h\\in\\{0,1\\}$ the wrap indicator."),
 s("M","line count","The number of lines along the last axis, T/r.","count","Then $M=T/r$ is the number of lines along the last axis."),
 s("\\iota","line-to-record map","Reads each line along the last axis as a polynomial in y, giving an array of M records in R_r.","direct","Let $\\iota$ read each line $(f_{\\boldsymbol j,k})_k$ as the polynomial $\\sum_k f_{\\boldsymbol j,k}y^k$, giving an array of $M$ records in $\\mathcal R_r$, and let $(D_\\pm f)_{\\boldsymbol j,k}=\\zeta^{\\pm k}f_{\\boldsymbol j,k}$ multiply entry $k$ of each line by $\\zeta^{\\pm k}$."),
 s("D_\\pm","twist and untwist","Multiplication of entry k of each line by \\zeta^{\\pm k}.","direct","Let $\\iota$ read each line $(f_{\\boldsymbol j,k})_k$ as the polynomial $\\sum_k f_{\\boldsymbol j,k}y^k$, giving an array of $M$ records in $\\mathcal R_r$, and let $(D_\\pm f)_{\\boldsymbol j,k}=\\zeta^{\\pm k}f_{\\boldsymbol j,k}$ multiply entry $k$ of each line by $\\zeta^{\\pm k}$."),
 s("\\mathcal M_r","ring convolution","The normalized convolution of the first d-1 axes over R_r, dividing by T.","direct","Let $\\mathcal M_r$ be the ring convolution: it convolves the first $d-1$ axes over $\\mathcal R_r$, dividing by $T$."),
 s("\\mathcal M_{\\mathbb C}","complex convolution","The normalized complex cyclic convolution, equal to f*g/T.","direct","The normalized complex cyclic convolution $\\mathcal M_{\\mathbb C}$ is"),
 s("\\|f\\|","sup norm","The largest modulus of a scalar coefficient of f.","direct","Let $\\|f\\|$ be the sup norm of $f$, the largest modulus of a scalar coefficient."),
],
"relations":[
 dict(prerequisite="ring-y",predicate="converts the last cyclic axis into",quote="The twist converts the last cyclic axis into the coordinate of the [Polynomial ring modulo y^r + 1](ring-y.md), and the sign is repaired by a phase."),
 dict(prerequisite="convolution",predicate="reproduces",quote="The twist reproduces [Cyclic convolution](convolution.md) on that axis."),
],
"derivations":[
 dict(step="S5.4.1",quote="Let $\\zeta=e^{\\pi i/r}$, so $\\zeta^r=-1$. Define $\\Theta:\\mathbb C[x_d]/(x_d^r-1)\\to\\mathcal R_r$ by $x_d\\mapsto\\zeta y$."),
 dict(step="S5.4.2",quote="It is well defined because $(\\zeta y)^r=(-1)(-1)=1$."),
 dict(step="S5.4.3",quote="After twisting, the term carries $\\zeta^{k+l}$, and negacyclic reduction contributes $(-1)^h$, so the factor is"),
 dict(step="S5.4.4",quote="The normalized complex cyclic convolution $\\mathcal M_{\\mathbb C}$ is"),
]}
json.dump(d,open('0368-write-phase-twist.answer.json','w'),indent=1)
