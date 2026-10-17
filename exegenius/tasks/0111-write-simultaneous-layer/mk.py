import json,re
t=open('0111-write-simultaneous-layer.answer.md').read()
S=[]
def sym(name,symbol,meaning,quote,rel='direct'):
    S.append(dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote))

sym('selected chunk count','D','The number of address chunks carrying a selected bit.',"The simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\\le d$ address chunks of $K$ bits at once, in time $O(Vd^{\\lambda'})$ for fixed $\\lambda'<1$ rather than $D$ whole-array passes.",'count')
sym('record array','z','The array of records, a function of the address x.',"Let $z$ be the array of records at addresses $x$, with selected bits $x_1,\\dots,x_D$.")
sym('address','x','An address of the array, with selected bits x_1,...,x_D.',"Let $z$ be the array of records at addresses $x$, with selected bits $x_1,\\dots,x_D$.")
sym('phase diagonal','\\mathcal S_D','The diagonal operator multiplying the record at address x by i^{x_1+...+x_D}.',"Then $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with $(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x)$, an exact Gaussian dyadic operation: $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$ is a shift, a phase and at most one factor $b$.")
sym('group axis count','e','The number of axes in a group, e = mf.',"A group of $e=mf$ axes ($e$ counts them) forms $m$ slots of $f$ axes; a column is the vector in $\\mathbb F_2^m$ of the same bit of each slot.",'count')
hq="Each edge changes frame by $\\prod_hC_{v_h}^{\\eta_h}$ on every column, over a basis $v_h$ of its residual space, $\\eta_h=\\pm1$, $C_v=aI+bX_v$, $X_v$ shifting a column by $v$."
sym('slot index','h','Index of a slot, and of the residual basis vector placed on it.',hq)
sym('residual vector','v_h','A vector of a basis of the edge\'s residual space, in F_2^m.',hq)
sym('edge sign','\\eta_h','The sign +1 or -1 of the kernel exponent attached to residual vector v_h.',hq)
sym('shifted kernel','C_v','The matrix aI+bX_v, the kernel C applied along the column direction v.',hq)
sym('column shift','X_v','The operator shifting the address of a column by v.',hq)
gq="For invertible $G$ with first columns $v_h$ and $\\mathcal P_G:x\\mapsto Gx$, $\\mathcal P_GX_v\\mathcal P_G^{-1}=X_{Gv}$"
sym('basis matrix','G','An invertible binary m by m matrix whose first columns are the residual vectors v_h.',gq)
sym('basis permutation','\\mathcal P_G','The address permutation moving a column value x to Gx.',gq)
sym('standard basis vector','e_h','The h-th standard basis vector of F_2^m.',"so the edge change is $\\mathcal P_G\\bigl(\\prod_hC_{e_h}^{\\eta_h}\\bigr)\\mathcal P_G^{-1}$, $e_h$ standard basis vectors.")
sym('sign matrix','Z','The diagonal matrix diag(1,-1).',"As $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$, $Z=\\operatorname{diag}(1,-1)$, inverse children need only signs and phases.")
rq="Row $Wg+w$ (quotient $g$, remainder $0\\le w<W$) goes to wire role $w$, so children have volume $V/W$."
sym('row quotient','g','The quotient of a row index on division by W.',rq)
sym('row remainder','w','The remainder of a row index modulo W, which is the wire role.',rq)
sym('row chunk count','q_0','The number of leading chunks whose bits form the row index.',"The rows are the bits of the first $q_0=\\lceil\\log_2W\\rceil\\lceil\\log_m(2d)\\rceil$ chunks, $q_0$ counting chunks, handled individually in $O(V\\log d)$, all chunks if $D\\le q_0$.",'count')
sym('step ratio','\\gamma','The ratio s/W, at most m^sigma.',"Take $\\sigma<1$ with $\\gamma=s/W\\le m^\\sigma$, $K\\le d^c$ for fixed $c>0$, and $\\lambda$ with $\\max\\{\\tau,\\sigma\\}<\\lambda<1$, $\\tau(1+c/\\beta)<\\lambda$.")
lq="After $j$ levels a leaf has $u=e/m^j<d^\\beta$ chunks and $\\gamma^j\\le(e/u)^\\sigma$, so leaves add $O(\\gamma^ju)\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$."
sym('level count','j','The number of recursion levels descended.',lq,'count')
sym('leaf chunks','u','The number of active chunks in a leaf after j levels, e/m^j.',lq,'count')
sym('piece digit','a_j','The base-m digit of D-q_0 at position j, the number of pieces of m^j chunks.',"Writing $D-q_0=\\sum_ja_jm^j$, $0\\le a_j<m$, gives $a_j$ pieces of $m^j$ chunks, at most $(m-1)(1+\\lfloor\\log_md\\rfloor)$, hence a $\\log(2d)$ factor:",'count')
sym('chain bound','A','A(e) bounds the number of arithmetic operations on a chain from an input coefficient to an intermediate one in a group of e axes.',"Let $A(e)$ bound the operations on a chain from an input coefficient to an intermediate one.")
sym('invocation bound','E','The bound 64(W+m+1)^3 on operations added on a chain by one network invocation.',"An invocation adds fewer than $E=64(W+m+1)^3$ (gates $24W^3$, corrections $4s+4W+4$, $s<Wm$), and chains concatenate the $s$ children: $A(e)\\le sA(e/m)+E$, $A(e)\\le8e$ at leaves.")
bq="For any bound $\\xi\\ge1$, $s\\xi+E\\le B\\xi$, $B=s+E$;"
sym('bound','\\xi','Any bound of at least 1 on the chain length.',bq)
sym('recurrence base','B','The sum s+E.',bq)
sym('depth exponent','\\nu','The least j at least 1 with m^j at least B.',"with $\\nu=\\min\\{j\\ge1:m^j\\ge B\\}$ and at most $\\lceil\\log_md\\rceil$ levels, $A(e)\\le8B^2d^{\\nu+1}$.")
sym('guard constant','C_0','The constant 128mB^2 in the guard width.',"Adding pieces, diagonals and $b^D$ stays below $\\Delta=\\lceil C_0d^{C_1}\\rceil$, $C_0=128mB^2$, $C_1=\\max\\{20,\\nu+3\\}=20$ here.")
sym('chain depth','\\ell','The number of operations along a chain, the depth of a value.',"By induction on chain depth $\\ell$, values lie in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$: addition doubles modulus, halving adds a denominator bit.",'count')
sym('axis exponent','\\epsilon','A fixed exponent with d = Theta(p^epsilon).',"For $d=\\Theta(p^\\epsilon)$ with fixed exponent $\\epsilon$ and $\\epsilon C_1<1$, $\\Delta=o(p)$: width $O(p)$.")
R=[
dict(prerequisite='phase-frames',predicate='is computed by the network of',quote="The network of [Binary phase frames](phase-frames.md) computes $C^{\\otimes e}$."),
dict(prerequisite='packed-bit-addition',predicate='performs its row additions by',quote="Gaussian elimination writes $G$ as at most $m(m-1)+3m$ row additions, each XORing selected bits of two slots, performed by [Packed selected-bit addition](packed-bit-addition.md)."),
dict(prerequisite='rank-recurrence',predicate='gets its power saving from',quote="The layer gets its power saving from [Recursive power saving](rank-recurrence.md), whose recurrence this is."),
dict(prerequisite='fixed-point',predicate='is evaluated exactly in',quote="The layer is evaluated exactly in [fixed-point Gaussian dyadic records](fixed-point.md)."),
]
Dv=[
('S1.6.1',"The [two-point kernel $C$](phase-kernel.md), $C=aI+bX$, with $\\mathsf S=\\operatorname{diag}(1,i)$ satisfies $H_0=b\\,\\mathsf SC\\mathsf S$, $C^2=X$, $C^4=I$"),
('S1.6.2',"Gaussian elimination writes $G$ as at most $m(m-1)+3m$ row additions, each XORing selected bits of two slots, performed by [Packed selected-bit addition](packed-bit-addition.md). Apply $\\mathcal P_G^{-1}$ per column, then $(C^{\\eta_h})^{\\otimes f}$ to the $f$ bits of slot $h$, then $\\mathcal P_G$: one child on $f=e/m$ axes per residual vector, exactly $s$ in all. As $(C^{-1})^{\\otimes f}=(-i)^fZ^{\\otimes f}C^{\\otimes f}Z^{\\otimes f}$, $Z=\\operatorname{diag}(1,-1)$, inverse children need only signs and phases."),
('S1.6.2b',"Then $H_0^{\\otimes D}=b^D\\mathcal S_DC^{\\otimes D}\\mathcal S_D$ with $(\\mathcal S_Dz)(x)=i^{x_1+\\dots+x_D}z(x)$, an exact Gaussian dyadic operation: $b^D=(-i/2)^{\\lfloor D/2\\rfloor}b^{D\\bmod2}$ is a shift, a phase and at most one factor $b$."),
('S1.6.3b',"So the complete basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\\tau+1))$"),
('S1.6.4',"As $K\\le e^{c/\\beta}$ for $e\\ge d^\\beta$, overhead is $O(e^\\lambda)$ and internal levels sum to $O(e^\\lambda)\\sum_{j\\ge0}(\\gamma/m^\\lambda)^j=O(e^\\lambda)$. After $j$ levels a leaf has $u=e/m^j<d^\\beta$ chunks and $\\gamma^j\\le(e/u)^\\sigma$, so leaves add $O(\\gamma^ju)\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$."),
('S1.6.5',"By induction on chain depth $\\ell$, values lie in $2^{-(p+\\ell)}\\mathbb Z[i]$ with modulus at most $2^\\ell$: addition doubles modulus, halving adds a denominator bit. So $p+\\Delta$ fractional and $\\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly"),
('S1.6.6',"Each row of $H_0$ has absolute row sum one, and absolute row sums multiply under tensor products, so every row of $\\mathcal H=H_0^{\\otimes D}$ has absolute row sum one"),
('S1.6.7',"Truncation toward zero cannot increase either component's absolute value, so $Q_p$ keeps the disk and changes each component by less than $2^{-p}$: $\\|Q_p(\\mathcal Hz)-\\mathcal Hz\\|_\\infty<\\sqrt2\\,2^{-p}$"),
]
bad=0
for q in [s['quote'] for s in S]+[r['quote'] for r in R]+[d[1] for d in Dv]:
    if q not in t: print("MISSING",q[:80]); bad+=1
json.dump(dict(symbols=S,relations=R,derivations=[dict(step=a,quote=b) for a,b in Dv]),open('0111-write-simultaneous-layer.answer.json','w'),indent=1)
print(bad)
