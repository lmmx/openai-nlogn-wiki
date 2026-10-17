import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0307-write-address-interchange.answer.md').read()
plain=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
def Q(a):
    assert a in plain,a
    return a
rec=Q("So the time per unit volume $F_k$ at width $m^k$ obeys $F_0=O(1)$, $F_k\\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md).")
tot=Q("The total is $O(V)\\sum_ja_jm^{j\\tau}\\le O(V)\\,m\\sum_jm^{j\\tau}=O(Ve^\\tau)$, since $m^{k'}<me$ makes $\\sum_jm^{j\\tau}$ a geometric sum.")
shearq=Q("The interchange performs each edge shear by [Matrix shear by triangular factorization](matrix-shear.md): if $A_i$ has rank $a$, then $\\Phi_{A_i}$ costs $a$ interchanges of $b$-digit fields")
streams=Q("Rows are split into role streams by [Elementary stream operations](stream-ops.md)")
open_=re.search(r'it swaps two disjoint address fields.*?stored bits \(a volume, not a label\)',plain,re.S).group(0)
addr=re.search(r'An address is .*?cyclic convolution pages\)\.',plain,re.S).group(0)
pq=Q("Digits are radix $q$, a fixed prime (here $q$ means the digit radix, not a sequence length as on the discrete Fourier transform and cyclic convolution pages).")
ech=Q("Let each chunk have $e=m^k$ digits, with $k$ recursion levels (not the depth of a value).")
tau=Q("where $\\tau=1-2^{-50}$ is the saving exponent")
mat=Q("each terminal and gate carries a rational $m\\times m$ matrix $M$ (here $M$ means the vertex matrix of the network, not the number of cyclic addresses as on the cyclic convolution page), and edge $i$ carries $A_i=M_{\\mathrm{head}(i)}-M_{\\mathrm{tail}(i)}$")
contract=Q("The shear contract: input wire $w$ is routed to an output role $\\rho(w)$ with $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$")
phi=Q("Let $\\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$")
fw=Q("Read wire $w$'s input $f_w$ as the logical array $\\Phi_{-M_{\\mathrm{in}(w)}}f_w$.")
xq=Q("row $Wx+w-1$ goes to stream $w$ as row $x$ (here $x$ means the stream row number, not a vector of $F$ as on the nested-subspace-labels page)")
jq=Q("Unrolled over the recursion levels $j$ (here $j$ means a recursion level index, not a digit value as on the elementary-stream-operations page, a wrap count as on the controlled-shifts page, or a stage number as on the nested-subspace-labels page)")
kp=Q("put $k'=\\lceil\\log_m e\\rceil$, the number of levels needed")
nu=Q("let $\\nu=\\lceil k'\\log W/(2\\log q)\\rceil$ be the number of top digits of each chunk set aside")
lam=Q("Now $d^+,h^+$ form a row field of range $\\Lambda=q^{2\\nu}\\ge W^{k'}$ before both remaining chunks.")
pad=Q("Pad with zero rows to $\\Lambda'=W^{k'}\\lceil \\Lambda/W^{k'}\\rceil<2\\Lambda$ rows, so the volume stays below $2V$.")
base=Q("where the base-$m$ digit $a_j$ is the number of pieces of width $m^j$ into which each remaining chunk is cut")
vol=open_
der=[{"step":"S1.5.2","quote":rec},{"step":"S1.5.3","quote":tot}]
rel=[
 {"prerequisite":"rank-recurrence","predicate":"obeys the recurrence of","quote":rec},
 {"prerequisite":"matrix-shear","predicate":"performs each edge shear by","quote":shearq},
 {"prerequisite":"stream-ops","predicate":"splits rows into streams by","quote":streams}]
def S(sym,name,meaning,q,r="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":r,"quote":q}
sy=[S("u","chunk width","The number of bits in each of the two address chunks.",vol,"count"),
 S("p","address prefix","The prefix field of an address, before the first chunk.",addr),
 S("h","first chunk","The first of the two address chunks being interchanged.",addr),
 S("d","second chunk","The second of the two address chunks being interchanged.",addr),
 S("g","gap","The address field between the two chunks.",addr),
 S("z","suffix","The address field after the second chunk.",addr),
 S("q","digit radix","The fixed prime radix of the stored digits.",pq),
 S("\\tau","saving exponent","The exponent below 1 in the interchange cost, equal to 1 - 2^{-50}.",tau),
 S("e","digit count","The number of radix-q digits in each chunk.",ech,"count"),
 S("k","recursion levels","The number of recursion levels, with e = m^k.",ech,"count"),
 S("M","vertex matrix","The rational m by m matrix carried by a terminal or gate of the network.",mat),
 S("A_i","edge matrix","The difference of the matrices at the two ends of edge i.",mat),
 S("\\rho","output role","The output role to which input wire w is routed.",contract),
 S("w","wire index","The index of an input wire of the network.",contract),
 S("\\Phi_M","address shear","The array permutation moving the entry at address (H,D) to (H+MD,D).",phi),
 S("f_w","wire input","The physical input array of wire w.",fw),
 S("x","stream row number","The row number within a role stream.",xq),
 S("j","recursion level index","An index of a recursion level in the unrolled sum.",jq),
 S("k'","levels needed","The number of recursion levels needed for chunks of e digits.",kp,"count"),
 S("\\nu","set-aside digits","The number of top digits of each chunk set aside to form the row field.",nu,"count"),
 S("\\Lambda","row range","The range of the row field formed by the top digits of both chunks.",lam),
 S("\\Lambda'","padded row count","The row count after padding with zero rows to a multiple of W^{k'}.",pad,"count"),
 S("a_j","piece count","The number of pieces of width m^j into which each remaining chunk is cut.",base,"count")]
json.dump({"symbols":sy,"relations":rel,"derivations":der},open('/home/user/e2e-run/exegenius/tasks/0307-write-address-interchange.answer.json','w'),indent=1)
