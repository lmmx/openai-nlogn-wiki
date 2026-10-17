import json
b=open('body.md').read()
P=[p for p in b.split('\n\n')]
def sent(p,start,end=None):
    i=p.index(start); 
    return p[i:] if end is None else p[i:p.index(end)+len(end)]
d=[
("S1.2.1",sent(P[2],"At each source, gate and sink")),
("S1.2.2",sent(P[3],"The invariant is that the stored array at $v$ equals $D_v$ applied to the logical array. It holds at the sources by definition")+""),
("S1.2.3",sent(P[4],"At a gate $G$ with $t$ input arrays",None)),
("S1.2.4",P[5].split('\n')[0]+"\n"+P[5].split('\n')[1]),
("S1.2.5",sent(P[6],"So if the scalar network")),
]
# fix S1.2.2 to full paragraph text
d[1]=("S1.2.2",P[3])
d[2]=("S1.2.3",P[4].replace(' <cite data-source="paper">the common frame commutes with the pointwise gate</cite>',' '))
d[2]=("S1.2.3","Because $D_v$ is $R$-linear, $\\sum_j c_jD_v\\varphi_j=D_v\\bigl(\\sum_j c_j\\varphi_j\\bigr)$. So $G(D_vg_1,\\dots,D_vg_t)=D_vG(g_1,\\dots,g_t)$ for any arrays $g_1,\\dots,g_t$")
d[3]=("S1.2.4","With $D_{\\rm out}=\\bigoplus_w D_{\\mathrm{sink}(w)}$, the implemented operator is therefore")
q=lambda s:s
sym=[
("R","scalar ring","The ring of scalars carried by the wires.","direct","Let $R$ be the ring of scalars carried by the wires, and let $\\Omega$ be a finite set of addresses indexing every array."),
("\\Omega","address set","A finite set of addresses indexing every array.","direct","Let $R$ be the ring of scalars carried by the wires, and let $\\Omega$ be a finite set of addresses indexing every array."),
("D_v","frame","The invertible R-linear operator on R^Omega assigned to a source, gate or sink v.","direct","At each source, gate and sink $v$, assign an invertible $R$-linear operator $D_v$ on $R^\\Omega$, called its frame."),
("t","gate input count","The number of input arrays of a gate.","count","At a gate $G$ with $t$ input arrays, every incoming array has the common frame $D_v$, and a gate output combines the logical inputs $\\varphi_1,\\dots,\\varphi_t$ with coefficients $c_j\\in R$."),
]
out={"derivations":[{"step":s,"quote":x} for s,x in d],
"symbols":[{"symbol":a,"name":n,"meaning":m,"relation":r,"quote":qq} for a,n,m,r,qq in sym],
"relations":[{"prerequisite":"exchange-network","predicate":"extend","quote":"They extend the [linear exchange network with restored scratch wires](exchange-network.md) from scalars to arrays while keeping each edge cheap."}]}
json.dump(out,open('../0084-write-array-frames.answer.json','w'),indent=1)
open('../0084-write-array-frames.answer.md','w').write(b)
