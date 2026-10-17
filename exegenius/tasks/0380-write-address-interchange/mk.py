import json
md=open('/home/user/e2e-run/exegenius/tasks/0380-write-address-interchange.answer.md').read()
def S(a,b):
    i=md.index(a); j=md.index(b,i)+len(b); return md[i:j]
Q={}
Q['1']=S("Write each chunk as $m$ consecutive","$\\mathbb Z/q^b\\mathbb Z$.")
Q['2']=S("Whole rows are split cyclically","(stream-ops.md).")
Q['3']=S("Each role stream has logical volume","one level down.")
Q['4']=S("On every circuit edge apply","$b$-digit fields.")
Q['5a']=S("By [Frames on wire arrays]","pointwise bit gate.")
Q['5b']=S("By the endpoint contract","=\\Phi_{I_m}f_w$.")
Q['5c']=S("Merging row $x$","initial values were arbitrary.")
Q['5d']=S("The interchange of the two full chunks","uses the circuit.")
Q['5e']=S("The number of recursive calls is","exactly $s$.")
Q['5g']=S("Therefore $F_0=O(1)$","of each.")
Q['5f']=S("Splitting, merging, gates,","node's own volume.")
Q['6']=S("Unrolling $F_k","$c=s/W<m^\\tau$.")
Q['61']=Q['6']
Q['62']=S("If $c\\le1$, every term","O(m^{k\\tau})$.")
Q['63']=S("If $c>1$, the geometric series","m^{k\\tau}$.")
Q['64']=S("Hence, since $e=m^k$","$F_k=O(e^\\tau)$.")
Q['t1']=S("Altogether one fixed","payloads $z$")
Q['t2']=S("For chunks of range","\\rceil$.")
Q['t3']=S("Put $\\nu=","\\nu=O(\\log 2e)$.")
Q['t4']=S("Interchange the top $\\nu$ digits","remaining chunks")
Q['t5']=S("This row field has range","W^k$.")
Q['t6']=S("Pad with zero rows,","$W^j$.")
Q['t7']=S("Write the remaining width in base","same row field.")
Q['t8']=S("The total cost is","=O(Ve^\\tau)$.")
Q['t9']=S("The bound $a_j<m$","order $e^\\tau$")
Q['t10']=S("For binary chunks of width","O(u)$")
der=[{'step':'S1.5.2','quote':S("Take chunks of","$F_k=O(e^\\tau)$.")},{'step':'S1.5.3','quote':S("For chunks of range","payloads $z$")}]
addr=S("An address is","chunk width).")
def sym(s,n,m,r,q): return {'symbol':s,'name':n,'meaning':m,'relation':r,'quote':q}
S_=[]
for s,n,m in [('u','chunk width','The number of bits in each of the two address chunks.'),
 ('p','prefix','The address field before the first chunk.'),('h','first chunk','The first of the two address chunks being interchanged.'),
 ('g','gap','The address field between the two chunks.'),('d','second chunk','The second of the two address chunks being interchanged.'),
 ('z','suffix','The address field after the second chunk.')]:
    S_.append(sym(s,n,m,'count' if s=='u' else 'direct',addr))
S_.append(sym('q','digit radix','The fixed prime radix of the stored digits.','direct',"Digits have a fixed prime radix $q$."))
take=S("Take chunks of","recursion levels.")
S_.append(sym('e','chunk digits','The number of radix-$q$ digits in each chunk, a power of $m$.','count',take))
S_.append(sym('m','fields per chunk','The number of fields into which a chunk is cut.','count',take))
S_.append(sym('k','recursion levels','The number of recursion levels, with $e=m^k$.','count',take))
S_.append(sym('b','digits per field','The number of digits in one field of a chunk, $e/m$.','count',Q['1']))
S_.append(sym('H','first chunk vector','The vector of the $m$ fields of the first chunk, over the integers mod $q^b$.','direct',Q['1']))
S_.append(sym('D','second chunk vector','The vector of the $m$ fields of the second chunk, over the integers mod $q^b$.','direct',Q['1']))
mat=S("Each vertex carries","\\mathrm{tail}(i)}$.")
S_.append(sym('M','vertex matrix','The rational $m\\times m$ matrix carried by a vertex of the network.','direct',mat))
S_.append(sym('i','edge index','The index of an edge of the network.','direct',mat))
S_.append(sym('A_i','edge matrix','The difference of the vertex matrices at the head and tail of edge $i$.','direct',mat))
route=S("Input wire $w$","identity.")
S_.append(sym('w','wire index','The index of an input wire of the network, also naming its role stream.','direct',route))
S_.append(sym('I_m','identity matrix','The $m\\times m$ identity matrix.','direct',route))
S_.append(sym('\\Phi_M','address shear','The array permutation moving the entry at address $(H,D)$ to $(H+MD,D)$.','direct',S("Let $\\Phi_M$ move","spectators unchanged;")))
S_.append(sym('x','stream row','The row number within a role stream.','direct',Q['2']))
S_.append(sym('f_w','physical input','The array physically stored on input wire $w$.','direct',S("Read the physical input","tape operation.")))
S_.append(sym("f'_{\\rho(w)}",'physical output','The array physically stored on output role $\\rho(w)$.','direct',Q['5b']))
S_.append(sym('F_k','time per volume','The time per unit volume of an interchange of width $m^k$.','direct',S("Let $F_k$ be","$m^k$.")))
S_.append(sym('c','call ratio','The number of calls $s$ times the volume fraction $1/W$ of each, $c=s/W$.','direct',Q['5g']))
S_.append(sym('\\tau','interchange exponent','The fixed exponent below $1$ in the cost $O(Vu^\\tau)$ of the interchange.','direct',"with the interchange exponent $\\tau=1-2^{-50}$."))
S_.append(sym('j','recursion level','The index of a recursion level, indexing the terms of the unrolled sum; also the exponent of a piece width $m^j$.','direct',S("Unrolling $F_k","recursion levels $j$,")))
S_.append(sym('\\nu','top digit count','The number of top digits of each chunk set aside to form the row field.','count',Q['t3']))
S_.append(sym('h^+','first chunk top','The top $\\nu$ digits of the first chunk.','direct',S("write each chunk as top digits","$d^+,d^-$.")))
S_.append(sym('h^-','first chunk rest','The remaining digits of the first chunk.','direct',S("write each chunk as top digits","$d^+,d^-$.")))
S_.append(sym('d^+','second chunk top','The top $\\nu$ digits of the second chunk.','direct',S("write each chunk as top digits","$d^+,d^-$.")))
S_.append(sym('d^-','second chunk rest','The remaining digits of the second chunk.','direct',S("write each chunk as top digits","$d^+,d^-$.")))
S_.append(sym('\\Lambda','row field range','The number of values of the row field, $q^{2\\nu}$.','count',Q['t5']))
S_.append(sym("\\Lambda'",'padded rows','The number of rows after padding with zero rows.','count',S("Pad with zero rows,","<2\\Lambda$ rows,")))
S_.append(sym('a_j','piece count','The base-$m$ digit of $e-\\nu$ giving the number of pieces of width $m^j$.','count',Q['t7']))
rel=[
{'prerequisite':'rank-recurrence','predicate':'takes its power saving from','quote':"The interchange takes its power saving from the recurrence of [Recursive power saving](rank-recurrence.md)."},
{'prerequisite':'matrix-shear','predicate':'performs each edge shear by','quote':"The interchange performs each edge shear by [Matrix shear by triangular factorization](matrix-shear.md)"},
{'prerequisite':'stream-ops','predicate':'splits rows using the scans of','quote':Q['2']},
]
json.dump({'derivations':der,'relations':rel,'symbols':S_},open('/home/user/e2e-run/exegenius/tasks/0380-write-address-interchange.answer.json','w'),indent=1)
