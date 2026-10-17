import json
Q_first="Gaussian resampling expresses a Fourier transform of length $s$ through one of a nearby larger length $t$"
Q_p="Let $s<t<2^p$ be coprime integers, where $p>100$ counts the fractional bits of each real and imaginary component"
Q_al="let $\\alpha$, the width parameter of the Gaussian weights below, be an integer with $2\\le\\alpha<\\sqrt p$"
Q_th="Assume $\\theta:=t/s-1>p/\\alpha^4$."
Q_F="Here $F_q$ is the normalised [Discrete Fourier transform](dft.md) of length $q$"
Q_P="Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ (coordinate indices $j$, $k$ taken modulo $s$, $t$)"
Q_AB="There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\\alpha^2}B_0P_tF_tA$."
Q_ST="Harvey and van der Hoeven's maps $\\mathsf S,\\mathsf T$ from length-$s$ to length-$t$ complex vectors"
Q_q="To undo $\\mathsf T$, let $q_j$ be the integer nearest $tj/s$ and $\\beta_j=tj/s-q_j$."
Q_C="Let $C$ select coordinates from length-$t$ to length-$s$ vectors, $(Cv)_j=v_{q_j}$"
Q_D="$(\\mathsf Du)_j=e^{\\pi\\alpha^2\\beta_j^2}u_j$"
Q_N="Put $N=C\\mathsf T\\mathsf D$."
Q_pr="Set $\\mathsf S'=\\mathsf S/2$, $\\mathsf J'=N^{-1}/2$, $\\mathsf D'=2^{-(2\\alpha^2-2)}\\mathsf D$"
Q_Dp="Let $\\mathbb D_p$ be the grid of [Fixed-point Gaussian dyadic records](fixed-point.md)."
Q_L="An approximation $\\widetilde L$ of a contraction $L$ has error below a bound"
Q_d="Fix $0<\\delta<1/8$, the time-exponent slack."
Q_tl="The cited algorithms give approximations $\\widetilde{\\mathsf S}'$, $\\widetilde{\\mathsf J}'$, $\\widetilde{\\mathsf D}'$"
Q_AB2="Take $\\widetilde A=\\widetilde{\\mathsf S}'$ and $\\widetilde B_0=\\widetilde{\\mathsf D}'\\widetilde{\\mathsf J}'C$."
Q_E="Let $E=N-I$ and $k=\\lceil p/(\\alpha^2\\theta)\\rceil$, the number of series terms kept (a new meaning of $k$)."
Q_Et="Let $\\widetilde E$ be the approximation of $E$ on $\\mathbb D_p$"
Q_v0="Start from $\\widetilde v^{(0)}$, the rounding of $u/2$"
Q_vj="set $\\widetilde v^{(j)}=\\widetilde E\\widetilde v^{(j-1)}$"
h=lambda q:{"kind":"here","quote":q}
bg=lambda n:{"kind":"background","note":n}
S=[
("s",h(Q_first)),("t",h(Q_first)),("p",h(Q_p)),("\\alpha",h(Q_al)),("\\theta",h(Q_th)),
("F_q",h(Q_F)),("q",h(Q_F)),("P_s",h(Q_P)),("P_t",h(Q_P)),("j",h(Q_P)),("k",h(Q_P)),
("u",bg("Generic vector argument of an operator in a definition; ordinary linear algebra notation.")),
("v",bg("Generic vector argument of an operator in a definition; ordinary linear algebra notation.")),
("z",bg("Generic vector argument in a statement 'for every z'; ordinary notation.")),
("A",h(Q_AB)),("B_0",h(Q_AB)),
("\\mathsf S",h(Q_ST)),("\\mathsf T",h(Q_ST)),
("e",bg("Euler's number in the exponential function; calculus.")),
("\\pi",bg("The constant pi; calculus.")),
("i",bg("Summation index in a sum; summation notation from discrete mathematics.")),
("q_j",h(Q_q)),("\\beta_j",h(Q_q)),("C",h(Q_C)),("\\mathsf D",h(Q_D)),("N",h(Q_N)),
("I",bg("Identity operator/matrix; first linear algebra course.")),
("\\mathsf S'",h(Q_pr)),("\\mathsf J'",h(Q_pr)),("\\mathsf D'",h(Q_pr)),
("\\mathbb D_p",h(Q_Dp)),("\\widetilde L",h(Q_L)),("L",{"kind":"page","page":"contraction-maps"}),
("\\delta",h(Q_d)),
("\\widetilde{\\mathsf S}'",h(Q_tl)),("\\widetilde{\\mathsf J}'",h(Q_tl)),("\\widetilde{\\mathsf D}'",h(Q_tl)),
("\\widetilde A",h(Q_AB2)),("\\widetilde B_0",h(Q_AB2)),
("E",h(Q_E)),("\\widetilde E",h(Q_Et)),
("\\widetilde v^{(0)}",h(Q_v0)),("\\widetilde v^{(j)}",h(Q_vj)),
]
ans={"symbols":[{"symbol":a,"anchor":b} for a,b in S],"gaps":[]}
json.dump(ans,open("/home/user/e2e-run/exegenius/tasks/0139-audit-gaussian-resampling.answer.json","w"),indent=1)
