import json
md=open('/home/user/e2e-run/exegenius/tasks/0029-write-chirp.answer.md').read()
def q(s):
    assert s in md, s
    return s
sym=[
("d","number of axes","count","where $d$ is the number of axes."),
("t_i","axis length","count","On axis $i$, $t_i$ is the even number of entries along that axis and $s_i$ is an integer coprime to $t_i$."),
("s_i","coprime integer","direct","On axis $i$, $t_i$ is the even number of entries along that axis and $s_i$ is an integer coprime to $t_i$."),
("T","total entries","count","Put $T=\\prod_i t_i$, the total number of entries."),
("Q","target permutation","direct","The permutation $Q$ is the target permutation: output position $\\boldsymbol j$ reads frequency $\\boldsymbol f=(-s_ij_i)_i$."),
("a","chirp","direct","Define the chirp $a_{\\boldsymbol j}=\\exp\\left(-\\pi i\\sum_{i=1}^d s_ij_i^2/t_i\\right)$, a phase quadratic in the index, and let $\\overline a$ be its complex conjugate."),
]
meaning={"d":"The number of axes (coordinates) of an index.","t_i":"The even number of entries along axis i.","s_i":"An integer coprime to t_i, scaling the frequency read along axis i.","T":"The total number of entries, the product of the t_i.","Q":"The target permutation, reading frequency (-s_i j_i)_i at output position j.","a":"The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i)."}
out={"symbols":[{"symbol":s,"name":n,"meaning":meaning[s],"relation":r,"quote":q(qt)} for s,n,r,qt in sym],
"relations":[
{"prerequisite":"dft","predicate":"rewrites","quote":q("The Bluestein chirp identity rewrites a permuted [Discrete Fourier transform](dft.md) as a pointwise chirp phase, a [cyclic convolution](convolution.md), and another chirp phase, so the target permutation of resampling is absorbed into the convolution and never executed as a sort.")},
{"prerequisite":"convolution","predicate":"is reduced to","quote":q("The permuted transform is thus reduced to one [Cyclic convolution](convolution.md) of length $T$ between two pointwise phase multiplications.")}],
"derivations":[
{"step":"S4.3.1","quote":q("Define the chirp $a_{\\boldsymbol j}=\\exp\\left(-\\pi i\\sum_{i=1}^d s_ij_i^2/t_i\\right)$, a phase quadratic in the index, and let $\\overline a$ be its complex conjugate.")},
{"step":"S4.3.2","quote":q("Replacing $j_i$ by $j_i+t_i$ changes the exponent by $-\\pi i s_i\\frac{(j_i+t_i)^2-j_i^2}{t_i}=-\\pi i s_i(2j_i+t_i)$, which is an integral multiple of $2\\pi i$ because $t_i$ is even, so $a$ has period $t_i$ in coordinate $i$.")},
{"step":"S4.3.3","quote":q("Using $(j_i-k_i)^2=j_i^2-2j_ik_i+k_i^2$, the exponent of this product is $\\sum_i\\frac{\\pi i s_i}{t_i}\\bigl(j_i^2-(j_i^2-2j_ik_i+k_i^2)+k_i^2\\bigr)$, where the squares cancel, so the coefficient is $\\frac1T\\overline a_{\\boldsymbol j}a_{\\boldsymbol j-\\boldsymbol k}\\overline a_{\\boldsymbol k}=\\frac1T\\exp(2\\pi i\\sum_is_ij_ik_i/t_i)$.")},
{"step":"S4.3.4","quote":q("This is precisely the coefficient of $QF_{\\boldsymbol t}$ found above, because $Q$ reads frequency $(-s_ij_i)_i$ from the negative-sign transform.")}]}
json.dump(out,open('/home/user/e2e-run/exegenius/tasks/0029-write-chirp.answer.json','w'),indent=1)
