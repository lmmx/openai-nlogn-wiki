import json
md=open('../0038-write-multiplication-algorithm.answer.md').read()
sents={}
def S(s):
    assert s in md, s
    return s
q_sizes=S("Here $b=\\lceil\\log_2 n\\rceil$ is the digit width in bits and $p=6b$ is the number of fractional bits kept.")
q_axes=S("Axis lengths are primes $s_i$ with product $S$, and padded lengths $t_i$ with product $T$.")
q_q=S("Each input splits into $q=\\lceil n/b\\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md).")
q_crt=S("The convolution is addressed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\\Phi$.")
q_chirp=S("The [Bluestein chirp identity](chirp.md) gives $QF_{\\boldsymbol t}x=\\overline a\\cdot\\mathcal M_{\\mathbb C}(a,\\overline a\\cdot x)$: phase, convolution with the chirp, phase.")
q_twist=S("Here $F_{\\boldsymbol t}$ is the transform on the axes $t_i$, and $\\mathcal M_{\\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md).")
q_x0=S("With $\\widetilde a$ the approximation of $a$ and $Q_p$ truncation to $p$ fractional bits, the computed version forms $x_0=Q_p(\\overline{\\widetilde a}\\cdot x)$, the data operand after the first endpoint phase.")
q_c=S("The computed chirp transform is $\\widetilde{\\mathscr C}(x)=Q_p(\\overline{\\widetilde a}\\cdot y_0)$ with $y_0=\\widetilde{\\mathcal M}_{\\mathbb C}(\\widetilde a,x_0)$.")
q_g=S("The source transform $\\widetilde{\\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\\mathcal A$, then $\\widetilde{\\mathscr C}$, then the resampling map $\\mathcal B_0$, then multiplies exactly by $2^\\gamma$, where $\\gamma$ counts the zero bits appended to each word.")
q_f=S("Replacing each numerical subroutine by the exact map it approximates, the exact counterpart is $\\mathscr F=2^\\gamma\\mathcal B_0QF_{\\boldsymbol t}\\mathcal A=RF_{\\boldsymbol s}$, with $R$ a retained permutation.")
q_dig=S("Digit $a_j$ is stored as the exact grid numerator $a_j2^{p-b-2}$ in a signed real word, representing $a_j2^{-b-2}$; $S-q$ zero records are appended.")
i1=S("Apply $\\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.")
i2=S("Compute $\\widetilde{\\mathscr F}(u)$ and $\\widetilde{\\mathscr F}(v)$.")
i3=S("Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.")
i4=S("Compute $\\widetilde{\\mathscr F}^{+}(z)$ and multiply its grid numerators by $S$, obtaining $\\widetilde w$.")
i5=S("Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\\Phi^{-1}$.")
i6=S("Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits")
q_perm=S("By [Retained permutation cancellation](retained-permutations.md), $R$ is never executed as a sort and the counterpart after the three transforms is $(u*v)/S^2$.")
q_sc=S("So after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$, cancelling the factor $2^{-b-2}$.")
q_sz=S("It takes its sizes from [Parameter and prime-length choice](parameter-choice.md).")
q_ex=S("Exactness is justified by [Error tracking and exact recovery](precision-recovery.md): the error on the recovered integer coefficients is below $1/2$.")
D=lambda s,q:{"step":s,"quote":q}
ans={
"derivations":[
 D("S5.5",md[md.index("The [Bluestein"):md.index("with $R$ a retained permutation.")+len("with $R$ a retained permutation.")]),
 D("S5.6",md[md.index("Digit $a_j$"):md.index(" <cite", md.index("1. Apply"))] if False else q_dig+" Then:\n\n"+md[md.index("1. Apply"):md.index("\n6. Propagate")] ),
],
"symbols":[
 {"symbol":"b","name":"digit width","meaning":"The number of bits in each radix digit, $\\lceil\\log_2 n\\rceil$.","relation":"count","quote":q_sizes},
 {"symbol":"p","name":"precision","meaning":"The number of fractional bits kept, $6b$.","relation":"count","quote":q_sizes},
 {"symbol":"s_i","name":"prime axis length","meaning":"The length of the i-th prime axis; their product is S.","relation":"direct","quote":q_axes},
 {"symbol":"S","name":"cyclic length","meaning":"The product of the prime axis lengths, the length of the cyclic convolution.","relation":"direct","quote":q_axes},
 {"symbol":"t_i","name":"padded axis length","meaning":"The padded power-of-two length of the i-th axis; their product is T.","relation":"direct","quote":q_axes},
 {"symbol":"T","name":"padded size","meaning":"The product of the padded axis lengths.","relation":"direct","quote":q_axes},
 {"symbol":"q","name":"digit count","meaning":"The number of radix-$2^b$ digits of each input, $\\lceil n/b\\rceil$.","relation":"count","quote":q_q},
 {"symbol":"a_j","name":"radix digit","meaning":"The j-th radix-$2^b$ digit of an input.","relation":"direct","quote":q_q},
 {"symbol":"\\widetilde a","name":"stored chirp","meaning":"The stored approximation of the chirp array a.","relation":"direct","quote":q_x0},
 {"symbol":"\\gamma","name":"scale exponent","meaning":"The number of zero bits appended to each word by the exact scale $2^\\gamma$.","relation":"count","quote":q_g}],
"relations":[
 {"prerequisite":"radix-digit-reduction","predicate":"splits inputs into digits as in","quote":q_q},
 {"prerequisite":"crt-map","predicate":"addresses the convolution by","quote":q_crt},
 {"prerequisite":"retained-permutations","predicate":"never executes a sort, by","quote":q_perm},
 {"prerequisite":"phase-twist","predicate":"is computed through","quote":q_twist},
 {"prerequisite":"ring-convolution","predicate":"is computed through","quote":q_twist},
 {"prerequisite":"parameter-choice","predicate":"takes its sizes from","quote":q_sz},
 {"prerequisite":"precision-recovery","predicate":"is justified by","quote":q_ex}]}
json.dump(ans,open('../0038-write-multiplication-algorithm.answer.json','w'),indent=1)
