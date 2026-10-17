import re
t=open('0275-write-simultaneous-layer/prev.md').read()
def r(a,b):
    global t
    assert a in t,a
    t=t.replace(a,b)
r("instead of $D$ passes.","instead of $D$ passes ($D$ counts chunks, not the source group of the shear page).")
r("acts on an array $z$ by","acts on an array $z$ (not a suffix) by")
r("A group of $e=mf$ axes has","A group of $e=mf$ selected axes ($e$ counts axes, not digits of a chunk) has")
r("$v_h$ indexed by $h,$ $\\eta_h=\\pm1,$","$v_\\xi$ indexed by $\\xi,$ $\\eta_\\xi=\\pm1,$")
r("Let $G$ be an invertible $\\mathbb F_2$-matrix with first columns $v_h$ and $\\mathcal P_G:x\\mapsto Gx$ an address permutation.","Let $\\Gamma$ be an invertible $\\mathbb F_2$-matrix with first columns $v_\\xi$ and $\\mathcal P_\\Gamma:x\\mapsto\\Gamma x$ an address permutation.")
r("$\\mathcal P_GX_v\\mathcal P_G^{-1}=X_{Gv}$","$\\mathcal P_\\Gamma X_v\\mathcal P_\\Gamma^{-1}=X_{\\Gamma v}$")
r("$\\mathcal P_G(\\prod_hC_{e_h}^{\\eta_h})\\mathcal P_G^{-1},$ $e_h$ the $h$-th standard basis vector.","$\\mathcal P_\\Gamma(\\prod_\\xi C_{\\mathbf 1_\\xi}^{\\eta_\\xi})\\mathcal P_\\Gamma^{-1},$ $\\mathbf 1_\\xi$ the $\\xi$-th standard basis vector.")
r("Apply $\\mathcal P_G^{-1},$ then $(C^{\\eta_h})^{\\otimes f}$ to the $f$ bits of slot $h,$ then $\\mathcal P_G:$","Apply $\\mathcal P_\\Gamma^{-1},$ then $(C^{\\eta_\\xi})^{\\otimes f}$ to the $f$ bits of slot $\\xi,$ then $\\mathcal P_\\Gamma:$")
r("Elimination writes $G$ as","Elimination writes $\\Gamma$ as")
r("the recursion of [Recursive power saving](rank-recurrence.md).","The layer obeys the recursion of [Recursive power saving](rank-recurrence.md).")
i=t.index("The layer is evaluated in")
j=t.index("A depth-$\\ell$")
seg=t[i:j]
seg=seg.replace("A(e)","\\chi(e)").replace("$B=s+E,$","$\\Psi=s+\\psi,$")
seg=re.sub(r'\bE\b','\\\\psi',seg)
seg=seg.replace("\\nu","\\vartheta")
seg=re.sub(r'(?<![\\A-Za-z])B(?![A-Za-z])','\\\\Psi',seg)
seg=seg.replace("\\log_mB","\\log_m\\Psi")
seg=seg.replace("m^j\\ge B","m^j\\ge\\Psi")
seg=seg.replace("\\vartheta=\\min\\{j\\ge1:m^j\\ge\\Psi\\},$","\\vartheta=\\min\\{j\\ge1:m^j\\ge\\Psi\\}$ (an exponent of $m,$ not a digit count),")
t=t[:i]+seg+t[j:]
open('0275-write-simultaneous-layer.answer.md','w').write(t)
print(seg)
t2=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
t2=re.sub(r'\$\$.*?\$\$','',t2,flags=re.S)
t2=re.sub(r'\$.*?\$','',t2)
print(len(t2.split()))
