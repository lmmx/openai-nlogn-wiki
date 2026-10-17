import json
def here(s,q): return {"symbol":s,"anchor":{"kind":"here","quote":q}}
def page(s,p): return {"symbol":s,"anchor":{"kind":"page","page":p}}
def bg(s,n): return {"symbol":s,"anchor":{"kind":"background","note":n}}
Q1="swaps two disjoint $u$-bit address fields of an array of $V$ bits (volume)"
Q2="An address is $(p,h,g,d,z)$: prefix $p$, chunks $h,d$, gap $g$, suffix $z$"
Q3="Let each chunk have $e=m^k$ digits ($k$ recursion levels)."
Q4="Cut it into $m$ fields of $b=e/m$ digits"
Q5="edge $i$ carries $A_i=M_{\\mathrm{head}(i)}-M_{\\mathrm{tail}(i)}$"
S=[here("u",Q1),here("V",Q1),
page("\\tau","parameter-choice"),
here("p",Q2),here("h",Q2),here("g",Q2),here("d",Q2),here("z",Q2),
here("H","For chunk values $H,D$"),here("D","For chunk values $H,D$"),
here("q","Digits are radix $q$ (a fixed prime)."),
here("e",Q3),here("k",Q3),
page("m","exchange-network"),
here("b",Q4),
bg("\\mathbb Z","Integers and modular arithmetic Z/nZ, covered by elementary number theory in the profile."),
here("W","has $W$ wires"),
here("M","each terminal and gate carries a rational $m\\times m$ matrix $M$"),
here("A_i",Q5),here("i",Q5),
here("s","with $s=\\sum_i\\operatorname{rank}A_i$"),
here("I_m","$M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$ (the identity)"),
here("\\rho","input wire $w$ ends at output role $\\rho(w)$"),
here("w","input wire $w$ ends at output role $\\rho(w)$"),
here("\\Phi_M","Let $\\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$."),
here("M'","For another matrix $M'$"),
page("a","matrix-shear"),
here("x","row $Wx+w-1$ goes to stream $w$ as row $x$"),
here("f_w","Read wire $w$'s input $f_w$ as the logical array"),
here("f'_{\\rho(w)}","the output is $f'_{\\rho(w)}"),
here("F_k","The time per unit volume $F_k$ at width $m^k$"),
here("j","Unrolled over levels $j$"),
here("k'","put $k'=\\lceil\\log_m e\\rceil$"),
here("\\nu","$\\nu=\\lceil k'\\log W/(2\\log q)\\rceil$"),
here("h^+","Split each chunk into top $\\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$"),
here("h^-","Split each chunk into top $\\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$"),
here("d^+","Split each chunk into top $\\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$"),
here("d^-","Split each chunk into top $\\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$"),
here("\\Lambda","form a row field of range $\\Lambda=q^{2\\nu}\\ge W^{k'}$"),
here("\\Lambda'","Pad with zero rows to $\\Lambda'=W^{k'}\\lceil \\Lambda/W^{k'}\\rceil<2\\Lambda$ rows"),
here("a_j","Split each remaining chunk into $a_j$ pieces of width $m^j$"),
bg("O","Big-O notation is covered by the profile."),
bg("\\log","Logarithms are covered by the profile (discrete mathematics and algorithms)."),
]
json.dump({"symbols":S,"gaps":[]},open("/home/user/e2e-run/exegenius/tasks/0146-audit-address-interchange.answer.json","w"),indent=1)
