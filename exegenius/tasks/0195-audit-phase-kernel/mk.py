import json
h=lambda s,q:{"symbol":s,"anchor":{"kind":"here","quote":q}}
syms=[
h("a","Let $a=\\frac{1+i}{2}$ and $b=\\frac{1-i}{2}$ be two complex constants"),
h("b","Let $a=\\frac{1+i}{2}$ and $b=\\frac{1-i}{2}$ be two complex constants"),
{"symbol":"i","anchor":{"kind":"background","note":"Imaginary unit of complex numbers, covered by the profile."}},
h("I","Let $I$ be the $2\\times 2$ identity matrix"),
h("X","let $X=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ be the bit flip, which swaps the two entries of a pair $(u,v)$"),
h("u","which swaps the two entries of a pair $(u,v)$"),
h("v","which swaps the two entries of a pair $(u,v)$"),
h("C","The kernel is $C=aI+bX$."),
h("\\mathsf S","Let $\\mathsf S=\\operatorname{diag}(1,i)$ be the phase matrix that multiplies the second entry of a pair by $i$."),
h("H_0","Let $H_0=\\frac12\\begin{pmatrix}1&1\\\\1&-1\\end{pmatrix}$ be the matrix of the averaging and differencing step"),
h("H","let $H=\\sqrt2\\,H_0$ be the normalized Hadamard matrix"),
]
json.dump({"symbols":syms,"gaps":[]},open("exegenius/tasks/0195-audit-phase-kernel.answer.json","w"),indent=1)
