import json
Q1=r"Here $b=\lceil\log_2 n\rceil$ is the digit width in bits and $p=6b$ is the number of fractional bits kept."
Q2=r"Axis lengths are primes $s_i$ with product $S$, and padded lengths $t_i$ with product $T$."
Q3=r"Let $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ be the chirp array."
Q4=r"Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$"
Q5=r"the computed version forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, the data operand after the first endpoint phase"
Q6=r"The computed chirp transform is $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$ with $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$."
Q7=r"Replacing each numerical subroutine by the exact map it approximates, the exact counterpart is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, with $R$ a retained permutation."
Q8=r"The source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the resampling map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ counts the zero bits appended to each word."
H=lambda q:{"kind":"here","quote":q}
S=[
("n",{"kind":"page","page":"conjecture"}),
("b",H(Q1)),("p",H(Q1)),
("s_i",H(Q2)),("S",H(Q2)),("t_i",H(Q2)),("T",H(Q2)),
("q",H(Q4)),("a_j",H(Q4)),
("x",{"kind":"page","page":"radix-digit-reduction"}),
("\\Phi",H(r"The convolution is addressed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\Phi$.")),
("a_{\\boldsymbol j}",H(Q3)),("\\boldsymbol j",H(Q3)),
("i",{"kind":"background","note":"Index of summation over axes; also the imaginary unit of complex numbers, both covered by the discrete mathematics and complex numbers background."}),
("j",{"kind":"background","note":"Ordinary summation/array index, covered by discrete mathematics (summation notation)."}),
("\\pi",{"kind":"background","note":"The constant pi, covered by calculus."}),
("\\exp",{"kind":"background","note":"Complex exponential, covered by complex numbers and calculus."}),
("Q",{"kind":"page","page":"chirp"}),
("F_{\\boldsymbol t}",H(r"Here $F_{\boldsymbol t}$ is the transform on the axes $t_i$")),
("\\overline a",{"kind":"background","note":"Overline is complex conjugation, covered by complex numbers."}),
("\\cdot",{"kind":"background","note":"Coordinatewise (pointwise) product of arrays; elementary multiplication of complex numbers."}),
("\\mathcal M_{\\mathbb C}",H(r"$\mathcal M_{\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md)")),
("f",H(r"$\mathcal M_{\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md)")),
("g",H(r"$\mathcal M_{\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md)")),
("*",{"kind":"background","note":"Convolution notation f*g, covered by the algorithms course (polynomial multiplication as convolution)."}),
("\\widetilde a",H(r"With $\widetilde a$ the approximation of $a$")),
("a",H(r"Let $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ be the chirp array.")),
("Q_p",H(r"$Q_p$ truncation to $p$ fractional bits")),
("x_0",H(Q5)),
("\\widetilde{\\mathscr C}",H(Q6)),
("y_0",H(Q6)),
("\\widetilde{\\mathcal M}_{\\mathbb C}",{"kind":"unbound","quote":r"$y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$","note":"The page never says that the tilde version is the computed (approximate) convolution; the reader can only guess by analogy with the tilde on a."}),
("\\widetilde{\\mathscr F}",H(Q8)),
("\\mathcal A",H(Q8)),("\\mathcal B_0",H(Q8)),("\\gamma",H(Q8)),
("\\mathscr F",H(Q7)),("R",H(Q7)),
("F_{\\boldsymbol s}",{"kind":"unbound","quote":r"$\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$","note":"Only F_t is described as the transform on the axes t_i; F_s (presumably the transform on the prime axes s_i) is never stated."}),
("u",H(r"Apply $\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.")),
("v",H(r"Apply $\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.")),
("z",H(r"Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.")),
("\\widetilde{\\mathscr F}^{+}",{"kind":"unbound","quote":r"Compute $\widetilde{\mathscr F}^{+}(z)$","note":"The page never defines the + version of the source transform (opposite-sign transform, conjugate of F tilde applied to conjugate of the input), nor that its exact counterpart is R F_s^+."}),
("\\widetilde w",H(r"multiply its grid numerators by $S$, obtaining $\widetilde w$")),
("w",H(r"So after the first scale it is $w=(u*v)/S$")),
]
G=[
{"term":"opposite-sign source transform","quote":r"Compute $\widetilde{\mathscr F}^{+}(z)$","kind":"step","note":"Step 4 uses a transform F tilde plus that the page never defines. The reader is not told it is the opposite-sign (inverse-direction) version obtained by conjugating input and output of F tilde, nor that its exact counterpart is R F_s^+ (paper lines 4478-4484), which is what the later claim that the three transforms give (u*v)/S^2 depends on."},
{"term":"cancelled scale factor","quote":r"cancelling the factor $2^{-b-2}$","kind":"step","note":"Wrong exponent. Each stored operand carries the factor 2^{-b-2}, so the convolution u*v carries (2^{-b-2})^2 = 2^{-2b-4}. Multiplying by 2^{2b+4} cancels 2^{-2b-4}, not 2^{-b-2}. The paper (lines 4540 and 4719-4720) says 2^{2b+4} reverses the two input scalings."},
]
json.dump({"symbols":[{"symbol":s,"anchor":a} for s,a in S],"gaps":G},open("/home/user/e2e-run/exegenius/tasks/0075-audit-multiplication-algorithm.answer.json","w"),indent=1)
