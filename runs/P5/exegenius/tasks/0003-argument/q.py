import sys
t=open('sources/paper.tex').read()
qs=[
"volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:",
"costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the",
"invocation changes $y_S$ to $y_S+x_S$ and leaves every other value",
"Thus the common frame commutes with the pointwise gate, and",
"Thus every triple line is nondegenerate, and neighboring triple lines",
"Label dimension is nondecreasing along every edge except center $3\\to4$, which removes",
"Its deficit from $W_{\\rm b}m$ is $N-2L_{\\rm b}>0$.",
"Every rational $m\\times m$ matrix $A$ of rank $a$ has a factorization",
"can be performed with exactly $a$ interchanges of pairs of $b$-digit",
"F_0=O(1),\\qquad F_k\\le(s/W)F_{k-1}+O(1).",
"in $O(Vu^\\tau)$ steps, where $V=PG B\\,2^{2u}$.",
"H_0=b\\mathsf SC\\mathsf S,\\qquad C^2=X,\\qquad C^4=I,\\qquad",
"y_{j_i}\\longleftarrow y_{j_i}\\mathbin\\oplus x_{j_i}",
"The phase construction supplies one recursive call on a slot for each",
"The accelerated network is evaluated exactly until an entire",
"The procedure returns $Q_p(\\mathcal H z)$ in the same array,",
"decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for",
"entry $(F_t^-z)_j$ occupies slot $\\operatorname{rev}_a(j)$.",
"Both layout construction and final restoration are charged in this",
"numerators of $fg$, and then return $Q_p(fg/r)$ in that same format, in time",
"Perform both forward transforms and retain their common $LB$ order.",
"P_sF_s=2^{2\\alpha^2}B_0P_tF_tA.",
"Both $\\mathcal A$ and $\\mathcal B_0$ are contractions.",
"QF_{\\boldsymbol t}u=\\overline a\\mathbin{\\cdot}",
"proving \\eqref{eq:source-permutation-cancel}. Finally, conjugation",
"Tp=\\Theta(n),\\quad d=\\Theta(p^\\epsilon),",
"We may therefore choose distinct odd primes satisfying",
"Thus convolution modulo $x^S-1$ has no nonzero wraparound.",
"$\\Phi$ is an isomorphism and preserves cyclic convolution.",
"multiplying coefficient $k$ by the nonzero number $\\zeta^k$.",
"For a source disk-grid tensor of norm at most $.5$, write",
"The source-transform procedures now supply the three transforms needed",
"448b\\,2^{-b+\\gamma}",
"The strict error below $1/2$ makes the nearest integer to",
"To propagate carries, let $Q_0=2^b$.",
"Table~\\ref{tab:costs} lists costs after division",
"Thus $\\min_i g_i=2^{-181}=2\\kappa$.",
"The complete large-input bound is consequently",
]
pos=-1;bad=0
for q in qs:
    c=t.count(q); i=t.find(q)
    ln=t[:i].count('\n')+1 if i>=0 else -1
    flag=''
    if c!=1: flag+=' COUNT=%d'%c
    if i<pos: flag+=' ORDER'
    pos=max(pos,i)
    print(ln,flag,q[:60])
