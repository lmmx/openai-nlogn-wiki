import json
t=open('/home/user/e2e-run/exegenius/tasks/0086-write-phase-twist.answer.md').read()
def S(sym,name,meaning,rel,q): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=q)
q_fg="Let $f$ and $g$ be two complex arrays with $d$ axes, the last of length $r$, and $T$ entries in all."
q_R="The twist converts the last cyclic axis into the coordinate of the [Polynomial ring modulo y^r + 1](ring-y.md), written $\\mathcal R_r$, where $y^r=-1$ instead."
q_x="Convolution along the last axis is multiplication in $\\mathbb C[x_d]/(x_d^r-1)$, where $x_d$ is the variable of that axis."
q_z="Let $\\zeta=e^{\\pi i/r}$, so $\\zeta^r=-1$."
q_T="Define the ring map $\\Theta$ from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathcal R_r$ by $x_d\\mapsto\\zeta y$."
q_kl="Here $k$ and $l$ index coefficients, not operations."
q_jh="Take $k,l<r$ and write $k+l=j+hr$, with $j<r$ the resulting position and $h\\in\\{0,1\\}$ the wrap indicator."
q_i="$\\iota$ reads each line $(f_{\\boldsymbol j,k})_k$ as the polynomial $\\sum_k f_{\\boldsymbol j,k}y^k$, giving an array of $M$ records in $\\mathcal R_r$."
q_D="Let $(D_\\pm f)_{\\boldsymbol j,k}=\\zeta^{\\pm k}f_{\\boldsymbol j,k}$ multiply entry $k$ of each line by $\\zeta^{\\pm k}$."
q_Mr="Let $\\mathcal M_r$ be the ring convolution of [Convolution from the retained transform layout](ring-convolution.md): it convolves the first $d-1$ axes over $\\mathcal R_r$, dividing by $T$."
q_MC="The composite $\\mathcal M_{\\mathbb C}$, the normalized complex cyclic convolution, is"
q_n="Write $\\|f\\|$ for the sup norm of an array $f$: the largest modulus of a scalar coefficient."
q_rel2="The twist reproduces [Cyclic convolution](convolution.md) on that axis."
for q in [q_fg,q_R,q_x,q_z,q_T,q_kl,q_jh,q_i,q_D,q_Mr,q_MC,q_n,q_rel2]:
    assert q in t,q
d1="Define the ring map $\\Theta$ from $\\mathbb C[x_d]/(x_d^r-1)$ to $\\mathcal R_r$ by $x_d\\mapsto\\zeta y$."
d2="Since $\\Theta(x_d^k)=\\zeta^k y^k$, $\\Theta$ is diagonal on the bases $(x_d^k)$ and $(y^k)$, multiplying coefficient $k$ by $\\zeta^k\\ne0$. It is therefore an isomorphism, with inverse multiplying by $\\zeta^{-k}$."
d3="The coefficient of $y^j$ is thus $\\zeta^j$ times the cyclic coefficient; untwisting by $\\zeta^{-j}$ restores it with the correct sign."
d4="The maps $\\iota^{\\pm1}$ only regroup scalars, and $D_\\pm$ multiplies by numbers of modulus $1$, so all are linear and keep the sup norm."
for q in [d1,d2,d3,d4]: assert q in t,q
ans=dict(
 derivations=[dict(step="S5.4.1",quote=d1),dict(step="S5.4.2",quote=d2),dict(step="S5.4.3",quote=d3),dict(step="S5.4.4",quote=d4)],
 relations=[dict(prerequisite="ring-y",predicate="converts the last cyclic axis into the coordinate of",quote=q_R),
            dict(prerequisite="convolution",predicate="reproduces",quote=q_rel2)],
 symbols=[
  S("f","first array","The first complex array being convolved.","direct",q_fg),
  S("g","second array","The second complex array being convolved with f.","direct",q_fg),
  S("d","axis count","The number of axes of the arrays.","count",q_fg),
  S("x_d","last-axis variable","The variable of the last cyclic axis.","direct",q_x),
  S("\\mathcal R_r","negacyclic ring","The ring of polynomials modulo y^r+1.","direct",q_R),
  S("\\zeta","twist root","The primitive 2r-th root of unity e^{\\pi i/r}, with zeta^r=-1.","direct",q_z),
  S("\\Theta","twist map","The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.","direct",q_T),
  S("k","coefficient index","An index of a coefficient (not an operation count).","direct",q_kl),
  S("l","second coefficient index","An index of a coefficient of the second factor.","direct",q_kl),
  S("j","wrapped position","The position k+l reduced modulo r.","direct",q_jh),
  S("h","wrap indicator","Zero or one according to whether k+l wrapped past r.","direct",q_jh),
  S("\\iota","record reading","The map reading each line along the last axis as a polynomial in R_r.","direct",q_i),
  S("D_\\pm","diagonal twist","The maps multiplying entry k of each line by zeta^{+-k}.","direct",q_D),
  S("\\mathcal M_r","ring convolution","Normalized convolution of the first d-1 axes over R_r, including division by T.","direct",q_Mr),
  S("\\mathcal M_{\\mathbb C}","complex convolution","The normalized complex cyclic convolution of two arrays.","direct",q_MC),
  S("\\|f\\|","sup norm","The largest modulus of a scalar coefficient of f.","direct",q_n),
 ])
json.dump(ans,open('/home/user/e2e-run/exegenius/tasks/0086-write-phase-twist.answer.json','w'),indent=1)
