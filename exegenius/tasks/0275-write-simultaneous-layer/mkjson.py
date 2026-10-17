import json
t=open('0275-write-simultaneous-layer.answer.md').read()
def q(s):
    assert s in t, s
    return s
D=[]
def der(step,s): D.append({"step":step,"quote":q(s)})
der("S1.6.1","With $\\mathsf S=\\operatorname{diag}(1,i),$ the [Two-point kernel C](phase-kernel.md) $C=aI+bX$ satisfies $H_0=b\\,\\mathsf SC\\mathsf S,$ $C^2=X$ and $C^4=I$")
der("S1.6.2","Apply $\\mathcal P_\\Gamma^{-1},$ then $(C^{\\eta_\\xi})^{\\otimes f}$ to the $f$ bits of slot $\\xi,$ then $\\mathcal P_\\Gamma:$ one child on $f=e/m$ axes per residual vector, exactly $s$ in all.")
der("S1.6.2b","Phases and $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$ are exact Gaussian dyadic, leaving $C^{\\otimes D}.$")
der("S1.6.3b","Their number is fixed, so the basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\\tau+1))$")
der("S1.6.4","As $s/W\\le m^\\sigma,$ $\\sigma<1,$ internal levels sum geometrically, leaves add $O(e^\\sigma d^{\\beta(1-\\sigma)}),$ and $\\log d$ pieces give $O(d^{\\lambda'}).$")
der("S1.6.5","A depth-$\\ell$ value lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell,$ since addition at most doubles modulus and halving adds a denominator bit.")
der("S1.6.6","Absolute row sums multiply under tensor products, so each row of $\\mathcal H=H_0^{\\otimes D}$ has absolute row sum one")
der("S1.6.7","Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\\|Q_p(\\mathcal Hz)-\\mathcal Hz\\|_\\infty<\\sqrt2\\,2^{-p}$")
R=[]
def rel(pr,pred,s): R.append({"prerequisite":pr,"predicate":pred,"quote":q(s)})
rel("phase-frames","is computed by","$C^{\\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md), with $W$ wires and $s$ smaller calls.")
rel("rank-recurrence","obeys the recursion of","The layer obeys the recursion of [Recursive power saving](rank-recurrence.md).")
rel("packed-bit-addition","XORs selected bits by","[Packed selected-bit addition](packed-bit-addition.md) XORs selected bits by cyclic shifts of whole chunk ranges plus a repair of exceptional addresses.")
rel("fixed-point","is evaluated in","The layer is evaluated in [Fixed-point Gaussian dyadic records](fixed-point.md).")
S=[]
def sym(s,name,meaning,rel_,quote): S.append({"symbol":s,"name":name,"meaning":meaning,"relation":rel_,"quote":q(quote)})
sym("D","selected chunk count","The number of selected address chunks, at most d.","count","The simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\\le d$ selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\\lambda'}),$ $\\lambda'<1,$ instead of $D$ passes ($D$ counts chunks, not the source group of the shear page).")
sym("e","selected axis count","The number of selected axes in a group, e = mf.","count","A group of $e=mf$ selected axes ($e$ counts axes, not digits of a chunk) has $m$ slots of $f$ axes; a column holds one bit per slot, in $\\mathbb F_2^m.$")
sym("z","array","An array on which the diagonal operator acts.","direct","With $x_1,\\dots,x_D$ the selected bits of an address $x,$ this gives $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D,$ where the diagonal operator $\\mathcal S_D$ acts on an array $z$ (not a suffix) by $(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x).$")
sym("\\xi","residual index","The index of a residual basis vector and its slot.","direct","Each edge changes the frame on every column by $\\prod_\\xi C_{v_\\xi}^{\\eta_\\xi},$ with residual basis vectors $v_\\xi$ indexed by $\\xi,$ $\\eta_\\xi=\\pm1,$ $C_v=aI+bX_v$ and $X_v$ shifting a column by $v.$")
QG="Let $\\Gamma$ be an invertible $\\mathbb F_2$-matrix with first columns $v_\\xi$ and $\\mathcal P_\\Gamma:x\\mapsto\\Gamma x$ an address permutation."
sym("\\Gamma","basis-change matrix","An invertible F_2 matrix whose first columns are the residual basis vectors.","direct",QG)
sym("\\mathcal P_\\Gamma","address permutation","The address permutation sending x to Gamma x.","direct",QG)
sym("\\mathbf 1_\\xi","standard basis vector","The xi-th standard basis vector.","direct","so the edge change is $\\mathcal P_\\Gamma(\\prod_\\xi C_{\\mathbf 1_\\xi}^{\\eta_\\xi})\\mathcal P_\\Gamma^{-1},$ $\\mathbf 1_\\xi$ the $\\xi$-th standard basis vector.")
sym("q_0","individual chunks","The number of leading chunks given individual C kernels, whose bits form the row index.","count","So the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks get individual $C$ kernels, in $O(V\\log d),$ and their bits form a row index of range at least $W^{\\lceil\\log_md\\rceil}.$")
sym("\\chi","chain operation bound","A bound on the operations on a chain from an input to an intermediate coefficient.","count","Let $\\chi(e)$ bound the operations on a chain from an input to an intermediate coefficient ($E$ below is an operation bound, not a tensor factor).")
sym("E","invocation operation bound","A bound on the operations in one invocation of the network.","count","Let $\\chi(e)$ bound the operations on a chain from an input to an intermediate coefficient ($E$ below is an operation bound, not a tensor factor).")
sym("\\Psi","level factor","The sum s + psi, the factor by which the chain bound grows per level.","direct","With $\\Psi=s+E,$ $s\\varphi+E\\le\\Psi\\varphi$ for any bound $\\varphi\\ge1,$ so $\\chi(e)\\le8d\\Psi^{\\lceil\\log_md\\rceil+1}.$")
sym("\\varphi","chain bound value","Any bound of at least one on a chain length.","direct","With $\\Psi=s+E,$ $s\\varphi+E\\le\\Psi\\varphi$ for any bound $\\varphi\\ge1,$ so $\\chi(e)\\le8d\\Psi^{\\lceil\\log_md\\rceil+1}.$")
sym("\\vartheta","exponent of m","The least j at least 1 with m^j at least Psi; an exponent, not a digit count.","direct","With $\\vartheta=\\min\\{j\\ge1:m^j\\ge\\Psi\\}$ (an exponent of $m,$ not a digit count), $\\Psi^{\\lceil\\log_md\\rceil+1}\\le\\Psi^{\\log_md+2}=\\Psi^2d^{\\log_m\\Psi}\\le\\Psi^2d^\\vartheta,$ so $\\chi(e)\\le8\\Psi^2d^{\\vartheta+1}.$")
sym("C_0","guard constant","The constant 128 m Psi^2 in the guard width Delta.","direct","The total is at most $8m\\Psi^2d^{\\vartheta+2}+18d<128m\\Psi^2d^{\\vartheta+3}\\le\\Delta=\\lceil C_0d^{C_1}\\rceil,$ with $C_0=128m\\Psi^2,$ $C_1=\\max\\{20,\\vartheta+3\\}.$")
json.dump({"derivations":D,"relations":R,"symbols":S},open('0275-write-simultaneous-layer.answer.json','w'),indent=1)
