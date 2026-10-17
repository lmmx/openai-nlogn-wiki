import json
S=[]
def here(sym,q): S.append({"symbol":sym,"anchor":{"kind":"here","quote":q}})
def page(sym,p): S.append({"symbol":sym,"anchor":{"kind":"page","page":p}})
def conc(sym,c): S.append({"symbol":sym,"anchor":{"kind":"concept","concept":c}})
def bg(sym,n): S.append({"symbol":sym,"anchor":{"kind":"background","note":n}})
def unb(sym,q,n): S.append({"symbol":sym,"anchor":{"kind":"unbound","quote":q,"note":n}})

here("V","On a stream of $V$ bits")
here("K","address chunks of $K$ bits")
here("p","coefficients of $p$ fractional bits")
here("D","one bit in each of $D\\le d$ chunks")
page("d","packed-bit-addition")
here("\\lambda'","in time $O(Vd^{\\lambda'}),\\ \\lambda'<1,$")
page("H_0","phase-kernel")
bg("v","Dummy argument of the function H_0(u,v); ordinary function notation from discrete mathematics.")
unb("u","leaves add $O(\\gamma^ju)\\le O(e^\\sigma u^{1-\\sigma})","In the leaf bound u is used without saying what it denotes (in the paper it is e/m^j, the number of active chunks in a leaf after j levels); only in H_0(u,v) is it a dummy argument.")
page("X","phase-kernel")
page("\\mathsf S","phase-kernel")
page("C","phase-kernel")
page("a","phase-kernel")
page("b","phase-kernel")
bg("I","Identity matrix, from the linear algebra course in the reader profile.")
bg("i","Imaginary unit; complex numbers are in the reader profile.")
here("\\mathcal S_D","(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x)")
here("x_1","For selected address bits $x_1,\\dots,x_D,$")
unb("z","(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x)","The page never says z is the array of stored records (a function of the address) that the layer acts on.")
bg("x","Argument of the function z(x) / the address variable in x -> Mx; ordinary function notation.")
here("e","On $e=mf$ axes in $m$ slots of $f$ bits")
page("m","rank-recurrence")
page("f","rank-recurrence")
here("\\eta_h","products of kernels $C^{\\eta_h}$ along residual vectors")
here("v_h","along residual vectors $v_h\\in\\mathbb F_2^m")
bg("h","Index of an indexed family (slot / residual vector number), ordinary subscript notation.")
bg("\\mathbb F_2","The field of two elements; bitwise XOR / arithmetic mod 2 and vector spaces are in the reader profile.")
here("M","For invertible $M$ with first columns $v_h,$")
here("\\mathcal P_M","the address permutation $\\mathcal P_M:x\\mapsto Mx$")
unb("X_v","$\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$","The page defines only X(u,v)=(v,u); it never says what X_v (the shift of the address by v, (X_v f)(x)=f(x+v)) is.")
unb("X_{Mv}","$\\mathcal P_MX_v\\mathcal P_M^{-1}=X_{Mv}$","Same as X_v: the operator X indexed by a vector is never defined.")
here("Z","Z=\\operatorname{diag}(1,-1)")
page("s","rank-recurrence")
page("\\tau","packed-bit-addition")
here("W","Let $W$ be the network's wire count")
here("F(e)","Let $W$ be the network's wire count and $F(e)$ the time divided by volume.")
here("q_0","to the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks")
unb("g","row $Wg+w$","The page does not say that g is the quotient and w the remainder (0<=w<W) of the row index modulo W, so the row-to-wire rule is not fully specified.")
here("w","row $Wg+w$")
here("\\beta","\\ (e<d^\\beta),\\ \\beta=\\frac12.")
here("\\lambda","for fixed $\\max\\{\\tau,\\sigma\\}<\\lambda<1.$")
unb("\\sigma","$\\max\\{\\tau,\\sigma\\}<\\lambda<1.$","sigma is never introduced; the reader is not told it is a fixed exponent below 1 with s/W <= m^sigma.")
unb("c","As $K\\le d^c\\le e^{c/\\beta},$","The exponent c (K = floor(d^c)) is never introduced; the page does not even say K is tied to d.")
here("\\gamma","With $\\gamma=s/W\\le m^\\sigma<m^\\lambda,$")
unb("G","$Ge^\\lambda\\sum_{j\\ge0}","G is never said to be a constant (the implied constant of the overhead).")
bg("j","Summation index in a geometric series (summation notation is in the reader profile).")
unb("A","Chains satisfy $A(e)\\le sA(e/m)+E,","A(e) and the word chains are never defined (in the paper A(e) bounds the number of arithmetic operations on a dependency chain).")
here("E","E=64(W+m+1)^3")
here("B","since $sx+E\\le Bx$ for $B=s+E,$")
here("\\nu","\\nu=\\min\\{j\\ge1:m^j\\ge B\\}")
here("\\ell","After $\\ell$ operations a value lies in")
page("\\Delta","fixed-point")
unb("C_0","\\Delta=\\lceil C_0d^{C_1}\\rceil","C_0 is never given a value or role.")
unb("C_1","\\Delta=\\lceil C_0d^{C_1}\\rceil","C_1 is never given a value or role (paper: C_1=max{20,nu+3}, equal to 20 here).")
unb("\\epsilon","For $d=\\Theta(p^\\epsilon),\\ \\epsilon C_1<1$","epsilon is never introduced (paper: a fixed exponent with 0<epsilon<1 relating d to p).")
bg("\\Theta","Asymptotic notation, extending big-O in the reader profile.")
bg("O","Big-O notation.")
bg("o","Little-o asymptotic notation, a companion of big-O in the reader profile.")
page("\\mathcal H","frequency-order")
page("Q_p","fixed-point")
bg("\\mathbb Z","Integers; Z[i] is the set of complex numbers with integer real and imaginary parts (complex numbers and discrete mathematics).")
bg("\\infty","Sup (max) norm subscript; norms are in the reader profile.")
bg("\\lceil","Logarithms and floors/ceilings are in the reader profile (algorithms course).")
bg("\\lfloor","Logarithms and floors/ceilings are in the reader profile (algorithms course).")
bg("\\log_2","Logarithms and floors/ceilings are in the reader profile (algorithms course).")
bg("\\log_m","Logarithms and floors/ceilings are in the reader profile (algorithms course).")

G=[]
def gap(term,q,note): G.append({"term":term,"quote":q,"kind":"step","note":note})
gap("overhead is O(e^lambda): hypothesis missing",
 "the overhead is $O(e^\\lambda)$ for fixed $\\max\\{\\tau,\\sigma\\}<\\lambda<1.$",
 "The overhead is O((eK)^tau+1) with K<=d^c<=e^{c/beta}, i.e. O(e^{tau(1+c/beta)}). That is O(e^lambda) only if tau(1+c/beta)<lambda, which the paper requires (lines 2398-2399 and 2414-2415) but the page omits; max{tau,sigma}<lambda<1 alone does not give it. The page also never states K=floor(d^c).")
gap("edge identity and column recipe",
 "So apply $\\mathcal P_M^{-1}$ per column",
 "The page never states the edge identity that this recipe implements (frame change = P_M (prod C_{e_j}^{eta_j}) P_M^{-1}, paper eq. phase-edge-coordinate, lines 1855-1862), never defines X_v or C_v = aI+bX_v, and never explains the column vectors (x_{1,j},...,x_{m,j}) of the m slots on which P_M acts. The cited conjugation identity is thus not tied to the claim that follows.")
gap("q_0 individual kernels",
 "Applying $C$ individually to the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks makes their bits a row index",
 "This requires D>q_0; the paper (lines 2313-2316) treats D<=q_0 separately by applying individual C kernels throughout, at cost O(V log d). The page states the row construction without that hypothesis and never explains why the row index range is large enough or why the cost of this preprocessing is within the bound.")
gap("leaf bound",
 "leaves add $O(\\gamma^ju)\\le O(e^\\sigma u^{1-\\sigma})\\le O(e^\\sigma d^{\\beta(1-\\sigma)}).$",
 "u and j are not defined on the page (paper lines 2421-2430: u=e/m^j<d^beta active chunks per leaf after j levels), so the reader cannot check the two inequalities, which use gamma^j<=m^{j sigma}=(e/u)^sigma and u<d^beta.")
gap("base-m pieces",
 "Base-$m$ pieces give",
 "The page never says that the remaining D-q_0 chunks are written in base m and split into at most (m-1)(1+floor(log_m d)) consecutive pieces of m^j chunks (paper lines 2432-2436), which is where the log(2d) factor comes from. The cited result cannot be followed without it.")
gap("lambda' value",
 "the saving is slight: $\\lambda'=1-2^{-54}$ (cited)",
 "The value lambda'=1-2^{-54} depends on the fixed choices tau=sigma=1-2^{-50}, beta=1/2, c=2^{-56}, lambda=1-2^{-52} (paper lines 4010-4026), none of which except beta appears on the page, so the reader cannot check that max{lambda,sigma+beta(1-sigma)}<lambda'<1 holds. 's/W<m^sigma' alone does not give this value.")
gap("depth recurrence A(e)",
 "Chains satisfy $A(e)\\le sA(e/m)+E,\\ E=64(W+m+1)^3,$",
 "The page never says what A(e) or a chain is, nor derives the recurrence: the constant E=64(W+m+1)^3 comes from counting scalar gates (at most 12W gates, 2W^2 operations each), inverse-child and bank corrections (4s+4W+4) in paper lines 2490-2509, none of which is given. The recurrence has to be taken on trust.")
gap("sx+E<=Bx needs x>=1",
 "since $sx+E\\le Bx$ for $B=s+E,$",
 "sx+E<=(s+E)x holds only for x>=1 (paper line 2524); the page omits the hypothesis. The step to A(e)<=8B^2 d^{nu+1} also needs the depth k<=ceil(log_m d) of the recursion, e<=d, and B^{k+1}<=B^2 d^{log_m B}<=B^2 d^nu (paper lines 2523-2534), none of which is given.")
gap("operation count to Delta",
 "So with $\\Delta=\\lceil C_0d^{C_1}\\rceil,$ reserving",
 "C_0 and C_1 are never given. The bound A(e)<=8B^2 d^{nu+1} covers one group of e axes only; the paper (lines 2536-2560) adds the concatenated pieces (8mB^2 d^{nu+2}), preprocessing kernels, the outer diagonals and the scalar b^D to reach C_0=128mB^2, C_1=max{20,nu+3}. The page's Delta is therefore not shown to dominate the operation count.")
gap("value bounds after l operations",
 "After $\\ell$ operations a value lies in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$",
 "This holds only for values obtained from inputs in the unit disk lying on the grid 2^{-p}Z[i] (paper lines 2562-2565, by induction on depth); the page states it with no starting hypothesis and for 'operations' rather than depth along a dependency chain.")
gap("row sums multiply",
 "row sums multiply under tensor products",
 "The conclusion is about absolute row sums. Ordinary row sums also multiply under tensor products, but the second row of H_0 has sum 0, so they would not give 1. The correct statement is that the absolute row sum of H_0 is 1 for each row (|1/2|+|+-1/2|) and absolute row sums multiply, so every row of H_0^{(x)D} has absolute row sum one (paper line 2751).")
print(json.dumps({"symbols":S,"gaps":G},indent=1))
