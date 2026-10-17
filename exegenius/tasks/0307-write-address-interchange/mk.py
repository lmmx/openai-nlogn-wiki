import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0307-write-address-interchange.answer.md').read()
plain=re.sub(r'<cite.*?</cite>','',t,flags=re.S)
def Q(a):
    assert a in plain,a
    return a
rec=Q("So $F_k$, the time divided by logical volume at width $m^k$, obeys $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md), because each of the $s$ calls has $1/W$ of the volume.")
tot=Q("The total cost is $O(V)\\sum_ja_jm^{j\\tau}=O(Ve^\\tau)$, since $a_j<m$ and $m^{k'}<me$ make this a geometric sum of order $e^\\tau$.")
unr=Q("Unrolling over the levels $j$ gives $F_k=O\\big(\\sum_{j=0}^k (s/W)^j\\big)$.")
interch=Q("The interchange of the two full chunks is $D\\gets D-H$, then $H\\gets H+D$, then $D\\gets H-D$, componentwise; only the middle shear uses the circuit.")
streams=Q("The [Elementary stream operations](stream-ops.md) split whole rows cyclically into $W$ role streams within each prefix: the row with number remainder $w-1$ modulo $W$ goes to stream $w$.")
shearq=Q("On every circuit edge we apply $\\Phi_{A_i}$ to that role stream, performed by [Matrix shear by triangular factorization](matrix-shear.md), recursively interchanging each pivot pair of $b$-digit fields")
frame=Q("In [Frames on wire arrays](array-frames.md), the frame at a vertex with matrix $M$ is the address permutation $\\Phi_M$ and every edge changes it by $\\Phi_{M'-M}$; a common address permutation commutes with every pointwise bit gate.")
outp=Q("By the shear contract, the physical output is $f'_{\\rho(w)}=\\Phi_{M_{\\mathrm{out}(\\rho(w))}}\\Phi_{-M_{\\mathrm{in}(w)}}f_w=\\Phi_{I_m}f_w$.")
merge=Q("Merging each row of role $\\rho(w)$ back to its original row undoes $\\rho$, and the result is $H\\gets H+D$ on every original row, including rows assigned to scratch roles whose initial values were arbitrary.")
letters=re.search(r'Letters change meaning:.*?stage number\.',plain).group(0)
arr=Q("The array holds $V$ bits, addressed by $(p,h,g,d,z)$: a prefix $p$, chunks $h$ and $d$ of $u$ bits each, a gap $g$ and a suffix $z$.")
ech=Q("Let each chunk have $e=m^k$ radix-$q$ digits, where $k$ counts recursion levels and $m$ is the label-space dimension below.")
mat=Q("Each source, gate and sink carries a rational $m\\times m$ matrix $M$, and edge $i$ carries $A_i=M_{\\mathrm{head}(i)}-M_{\\mathrm{tail}(i)}$.")
contract=Q("The shear contract routes input wire $w$ to an output role $\\rho(w)$ with $M_{\\mathrm{out}(\\rho(w))}-M_{\\mathrm{in}(w)}=I_m$.")
phi=Q("Let $\\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$")
fw=Q("Read the input $f_w$ of wire $w$ as the logical array $\\Phi_{-M_{\\mathrm{in}(w)}}f_w$.")
kp=Q("let $k'=\\lceil\\log_m e\\rceil$ be the levels needed")
nu=Q("$\\nu=\\lceil k'\\log W/(2\\log q)\\rceil$ the number of top digits set aside, so $q^{2\\nu}\\ge W^{k'}$ and, for large $e$, $\\nu=O(\\log 2e)$.")
lam=Q("The first two fields form a row field of range $\\Lambda=q^{2\\nu}\\ge W^{k'}$ before both remaining chunks.")
pad=Q("Pad with zero rows, separately within each prefix, to the padded row count $\\Lambda'=W^{k'}\\lceil\\Lambda/W^{k'}\\rceil<2\\Lambda$, so the volume stays below $2V$.")
base=Q("Write the remaining width in base $m$: $e-\\nu=\\sum_{j=0}^{k'}a_jm^j$ with $0\\le a_j<m$, where $a_j$ is the number of pieces of width $m^j$ in each chunk.")
bit=Q("For $u$-bit chunks, let $e$ be the least integer with $q^e\\ge2^u$ and pad each chunk range from $2^u$ values to $q^e$ values, with zeros.")
split=Q("Splitting, merging, gates and the parking-stack scheduling of the $s$ calls cost $O(V)$ at the node, a fixed number of operations on its own volume.")
ncalls=Q("The number of recursive calls is the sum of the edge ranks, exactly $s$")
d=lambda s,q:{"step":s,"quote":q}
der=[d("S1.5.2",rec),d("S1.5.3",tot),
 d("S1.5.2.1",Q("Write each chunk as $m$ consecutive $b=e/m$ digit fields, giving vectors $H,D$ over $\\mathbb Z/q^b\\mathbb Z$, and first construct the shear $H\\gets H+D$.")),
 d("S1.5.2.2",streams),
 d("S1.5.2.3",Q("Each stream has logical volume $V/W$ and its row count is divisible by $W^{k-1}$, so the same argument applies one level down.")),
 d("S1.5.2.4",shearq),d("S1.5.2.5a",frame),d("S1.5.2.5b",outp),d("S1.5.2.5c",merge),d("S1.5.2.5d",interch),
 d("S1.5.2.5e",ncalls),d("S1.5.2.5f",split),d("S1.5.2.5g",rec),d("S1.5.2.6",unr),d("S1.5.2.6.1",unr),
 d("S1.5.2.6.2",Q("If $s/W\\le1$, every term is at most $1$, so the sum is at most $k+1=O(m^{k\\tau})$.")),
 d("S1.5.2.6.3",Q("If $s/W>1$, the geometric series gives $O((s/W)^k)$, and $(s/W)^k<m^{k\\tau}$.")),
 d("S1.5.2.6.4",Q("So, since $e=m^k$, $F_k=O(e^\\tau)$")),
 d("S1.5.3.1",Q("The procedure takes $O(Vu^\\tau)$ steps")),
 d("S1.5.3.2",kp),d("S1.5.3.3",nu),
 d("S1.5.3.4",Q("Interchange the top digits pairwise and join them: $(h^+,h^-,g,d^+,d^-)$ becomes $(d^+,h^+,h^-,g,d^-)$.")),
 d("S1.5.3.5",lam),d("S1.5.3.6",pad),d("S1.5.3.7",base),d("S1.5.3.8",tot),d("S1.5.3.9",tot),d("S1.5.3.10",bit)]
rel=[
 {"prerequisite":"rank-recurrence","predicate":"obeys the recurrence of","quote":rec},
 {"prerequisite":"matrix-shear","predicate":"performs each edge shear by","quote":shearq},
 {"prerequisite":"stream-ops","predicate":"splits whole rows into role streams by","quote":streams}]
def S(sym,name,meaning,q,r="direct"):
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":r,"quote":q}
sy=[S("u","chunk width","The number of bits in each of the two address chunks.",arr,"count"),
 S("p","address prefix","The prefix field of an address, before the first chunk.",arr),
 S("h","first chunk","The first of the two address chunks being interchanged.",arr),
 S("d","second chunk","The second of the two address chunks being interchanged.",arr),
 S("g","gap","The address field between the two chunks.",arr),
 S("z","suffix","The address field after the second chunk.",arr),
 S("q","digit radix","The fixed odd prime radix of the stored digits.",letters),
 S("j","recursion level","An index of a recursion level in the unrolled sum.",letters),
 S("e","digit count","The number of radix-q digits in each chunk.",ech,"count"),
 S("k","recursion levels","The number of recursion levels, with e = m^k.",ech,"count"),
 S("M","vertex matrix","The rational m by m matrix carried by a source, gate or sink of the network.",mat),
 S("A_i","edge matrix","The difference of the matrices at the two ends of edge i.",mat),
 S("\\rho","output role","The output role to which input wire w is routed.",contract),
 S("w","wire index","The index of an input wire of the network.",contract),
 S("\\Phi_M","address shear","The array permutation moving the entry at address (H,D) to (H+MD,D).",phi),
 S("f_w","wire input","The physical input array of wire w.",fw),
 S("k'","levels needed","The number of recursion levels needed for chunks of e digits.",kp,"count"),
 S("\\nu","set-aside digits","The number of top digits of each chunk set aside to form the row field.",nu,"count"),
 S("\\Lambda","row range","The range of the row field formed by the top digits of both chunks.",lam),
 S("\\Lambda'","padded row count","The row count after padding with zero rows to a multiple of W^{k'}.",pad,"count"),
 S("a_j","piece count","The number of pieces of width m^j in each chunk.",base,"count")]
json.dump({"symbols":sy,"relations":rel,"derivations":der},open('/home/user/e2e-run/exegenius/tasks/0307-write-address-interchange.answer.json','w'),indent=1)
