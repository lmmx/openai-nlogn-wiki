import json
H=lambda q:{"kind":"here","quote":q}
P=lambda p:{"kind":"page","page":p}
C=lambda c:{"kind":"concept","concept":c}
B=lambda n:{"kind":"background","note":n}
q1="Take $d$ axes with pairwise coprime prime lengths $s_i$"
q2="power-of-two lengths $t_i>s_i$"
q3="Write $\\boldsymbol s=(s_1,\\dots,s_d)$, $\\boldsymbol t=(t_1,\\dots,t_d)$, $S=\\prod_is_i$, $T=\\prod_it_i$"
q4="For operators $X_i$ acting on vectors of length $q_i$"
q5="For a vector $z$ of $q$ entries"
q6="$\\bigotimes_iX_i$ applies $X_i$ along every line of axis $i$"
q7="Put $R=\\bigotimes_iP_{s_i}$ (a permutation, not a ring), $Q=\\bigotimes_iP_{t_i}$, $\\mathcal A=\\bigotimes_iA_i$, $\\mathcal B_0=\\bigotimes_iB_{0,i}$"
q8="let $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ ($u,v$ are complex arrays here, not integers)"
q9="For a unit $c$ modulo $q$, let $(R_cz)_j=z_{cj}$"
S=[
("d",H(q1)),("s_i",H(q1)),("t_i",H(q2)),("i",P("multidim-transform")),
("\\boldsymbol s",H(q3)),("\\boldsymbol t",H(q3)),("S",H(q3)),("T",H(q3)),
("X_i",H(q4)),("q_i",H(q4)),("Y_i",H("for further operators $Y_i$")),
("\\bigotimes",H(q6)),("q",H(q5)),("z",H(q5)),
("F_q",P("contraction-maps")),
("j",B("Summation index, summation notation from discrete mathematics.")),("k",B("Index of the output, summation notation from discrete mathematics.")),("j'",B("Second summation index, from discrete mathematics.")),
("I",B("Identity matrix from first linear algebra.")),
("F_q^+",H("$F_q^+$ is the same with the exponent's sign reversed")),
("\\boldsymbol q",H("For a tuple $\\boldsymbol q$ of axis lengths")),
("F_{\\boldsymbol q}",H("$F_{\\boldsymbol q}=\\bigotimes_iF_{q_i}$ and $F_{\\boldsymbol q}^+=\\bigotimes_iF_{q_i}^+$")),
("F_{\\boldsymbol q}^+",H("$F_{\\boldsymbol q}=\\bigotimes_iF_{q_i}$ and $F_{\\boldsymbol q}^+=\\bigotimes_iF_{q_i}^+$")),
("F_{\\boldsymbol s}",B("F_{\\boldsymbol q} with q=s, as defined on this page.")),("F_{\\boldsymbol s}^+",B("F^+_{\\boldsymbol q} with q=s, as defined on this page.")),("F_{\\boldsymbol t}",B("F_{\\boldsymbol q} with q=t, as defined on this page.")),
("p",P("fixed-point")),("\\alpha",P("multidim-transform")),
("\\delta",H("$\\delta$ the fixed exponent in its time bound")),
("P_s",H(q8)),("P_t",H(q8)),("u",H(q8)),("v",H(q8)),
("s",P("gaussian-resampling")),("t",P("gaussian-resampling")),
("F_s",B("F_q with q=s, as defined on this page.")),("F_t",B("F_q with q=t, as defined on this page.")),
("A",H("That page gives linear contractions $A$, $B_0$")),("B_0",H("That page gives linear contractions $A$, $B_0$")),
("R",H(q7)),("Q",H(q7)),("\\mathcal A",H(q7)),("\\mathcal B_0",H(q7)),
("P_{s_i}",H(q7)),("P_{t_i}",H(q7)),("A_i",H(q7)),("B_{0,i}",H(q7)),
("\\gamma",P("multidim-transform")),
("\\ell",P("crt-map")),("\\tau",P("crt-map")),
("t_{\\max}",H("$t_{\\max}=2^\\ell$")),
("g",H("($g$ a fixed exponent)")),
("a",P("chirp")),("\\boldsymbol j",P("chirp")),
("\\overline a",B("Complex conjugation, covered by complex numbers.")),
("*",B("Cyclic convolution, a known concept; the symbol is its standard notation.")),
("c",H(q9)),("R_c",H(q9)),
("h",H("with $h$ the summation index")),
("R_c^{-1}",B("Inverse of a permutation, from permutations and bijections.")),
("\\gcd",B("gcd from elementary number theory.")),
("e",B("Base of the complex exponential, covered by complex numbers and roots of unity.")),
("\\pi",B("Standard constant.")),
("\\sum",B("Summation notation from discrete mathematics.")),
("\\prod",B("Product notation, as for summation.")),
("O",B("Big-O notation.")),("o",B("Little-o, asymptotics from the algorithms course.")),
("\\cdot",B("Coordinatewise product; standard multiplication notation.")),
("\\exp",B("Complex exponential from complex numbers.")),
]
G=[
{"term":"t_i a unit modulo s_i","quote":"Each $t_i$ is a unit modulo $s_i$ by the coprimality assumed","kind":"step","note":"The page only assumes gcd(s_i,t_i)=1 for odd s_i (prime lengths, power-of-two t_i), so s_i=2 is allowed and then t_i is not a unit mod 2. The paper's lemma (lines 3550-3552) assumes gcd(s,t)=1 for every axis, and the tensor lemma (line 3802) assumes every pair satisfies it. The page should assume gcd(s_i,t_i)=1 for all i, or all s_i odd."},
{"term":"substitution h=ck","quote":"Substituting $h=ck$ in the Fourier sum, with $h$ the summation index","kind":"step","note":"The Fourier sum is over j with (R_c z)_j = z_{cj}, so the substitution that gives F_q^+ R_c = R_c^{-1} F_q^+ is h = cj (j = c^{-1}h), not h = ck; k is the output index on this page and the page shows no computation. The paper (line 3953) has the same slip, but the reader cannot check the identity from this statement."},
{"term":"error below dp^2","quote":"error below $dp^2$","kind":"step","note":"The page never states the error of the one-axis algorithms for A and B_0 (the paper's Lemma at line 3566 gives error less than p^2 for each, and line 3861 sums d of them), so the reader cannot check where p^2, or the total dp^2, comes from."},
]
json.dump({"symbols":[{"symbol":a,"anchor":b} for a,b in S],"gaps":G},open("/home/user/e2e-run/exegenius/tasks/0200-audit-retained-permutations.answer.json","w"),indent=1)
