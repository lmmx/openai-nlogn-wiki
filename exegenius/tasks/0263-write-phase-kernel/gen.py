import json
md=open('/home/user/e2e-run/exegenius/tasks/0263-write-phase-kernel.answer.md').read()
def q(s):
    assert s in md, s
    return s
hq="Let $H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ be the matrix of the averaging and differencing step $(u,v)\\mapsto\\bigl(\\tfrac{u+v}{2},\\tfrac{u-v}{2}\\bigr)$, and let $H=\\sqrt2\\,H_0$ be the normalized Hadamard matrix, which is symmetric and satisfies $H^2=I$."
abq="Let $a=\\frac{1+i}{2}$ and $b=\\frac{1-i}{2}$ be two complex constants (here $b$ is this coefficient, not a bit index, and $a$ is not a bank index)."
syms=[
("a","kernel coefficient",abq,"The complex constant (1+i)/2, a coefficient of the kernel."),
("b","kernel coefficient",abq,"The complex constant (1-i)/2, a coefficient of the kernel; not a bit index."),
("I","identity matrix","Let $I$ be the $2\\times 2$ identity matrix, and let $X=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ be the bit flip, which swaps the two entries of a pair $(u,v)$.","The 2 by 2 identity matrix."),
("X","bit flip","Let $I$ be the $2\\times 2$ identity matrix, and let $X=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ be the bit flip, which swaps the two entries of a pair $(u,v)$.","The 2 by 2 matrix swapping the two entries of a pair."),
("C","two-point kernel","The kernel is $C=aI+bX$.","The two-point kernel aI + bX."),
("\\mathsf S","phase matrix","Let $\\mathsf S=\\operatorname{diag}(1,i)$ be the phase matrix that multiplies the second entry of a pair by $i$.","The diagonal matrix diag(1,i) multiplying the second entry of a pair by i."),
("H_0","averaging step matrix",hq,"The matrix of the two-point averaging and differencing step."),
("H","normalized Hadamard",hq,"The Hadamard matrix sqrt(2) H_0."),
]
out={"symbols":[{"symbol":s,"name":n,"meaning":m,"relation":"direct","quote":q(qq)} for s,n,qq,m in syms],
"relations":[{"prerequisite":"butterfly","predicate":"is obtained from","quote":q("The kernel $C$ is obtained from the two-point step of [Butterflies and the fast transform](butterfly.md) by conjugating with $\\mathsf S$ and rescaling:")}]}
json.dump(out,open('/home/user/e2e-run/exegenius/tasks/0263-write-phase-kernel.answer.json','w'),indent=1)
