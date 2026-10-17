import json
s=open('../0083-write-exchange-network.answer.md').read()
d=[]
def D(step,q):
    assert q in s,q
    d.append({"step":step,"quote":q})
D("S1.1.1","Fix the ground-set size $h=100$ and let $v=\\binom h3=161700$ be the number of three-element subsets of $[h]$")
D("S1.1.2","Set $N=v^3=4227952113000000$ for the size of each data bank, and $m=h^3=1000000$ for the label-space dimension used later.")
D("S1.1.3","Three stages each run $v^2$ invocations with their own scratch wires, so there are $I=3v^2=78440670000$ invocations.")
D("S1.1.4a","two triples $S,S'$ are neighbours when $|S\\cap S'|=1$")
D("S1.1.4b","the neighbours of a triple are the distinct triples with even intersection (zero or two)")
D("S1.1.5","The net change of $y$ is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$ and is independent of $\\sigma,\\gamma$; by the cancellations above it is $y\\gets y+x$.")
D("S1.1.6","A forward invocation $X\\to Y$ at stage 1, the inverse schedule $Y\\to X$ at stage 2 and a forward invocation $X\\to Y$ at stage 3 give")
D("S1.1.7a","A fixed triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ neighbours in the bit construction")
D("S1.1.7b","It has $z_{\\rm c}=\\binom{97}{3}+3\\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two).")
D("S1.1.7c","There are $c_{\\rm b}=100$ central wires per invocation in the bit network and $c_{\\rm c}=101$ in the complex one.")
D("S1.1.8a","The bit network has $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})=177176569091445000000$ wires")
D("S1.1.8b","The complex network has $W_{\\rm c}=2N+I(vz_{\\rm c}+c_{\\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length.")
def B(sym,name,meaning,rel,q):
    assert q in s,q
    return {"symbol":sym,"name":name,"meaning":meaning,"relation":rel,"quote":q}
Q1="Fix the ground-set size $h=100$ and let $v=\\binom h3=161700$ be the number of three-element subsets of $[h]$"
QN="Set $N=v^3=4227952113000000$ for the size of each data bank, and $m=h^3=1000000$ for the label-space dimension used later."
QS="Fixing two coordinates of $a$ leaves values $x_S,y_S$ indexed by triples $S\\in\\mathcal T$; $x$ and $y$ denote the vectors of all $x_S$ and all $y_S$."
QC="There are $c_{\\rm b}=100$ central wires per invocation in the bit network and $c_{\\rm c}=101$ in the complex one."
sy=[
B("h","ground-set size","The size of the ground set [h] whose three-element subsets index the values.","direct",Q1),
B("v","triple count","The number of three-element subsets of [h].","count",Q1),
B("\\mathcal T","triple set","The set of three-element subsets of [h].","direct","and let $\\mathcal T$ be the set of these subsets"),
B("N","bank size","The size of each data bank.","count",QN),
B("m","label dimension","The dimension of the label space used later.","direct",QN),
B("S","triple","A three-element subset of [h], indexing a value in a bank.","direct",QS),
B("x","source vector","The vector of all values x_S.","direct",QS),
B("y","target vector","The vector of all values y_S.","direct",QS),
B("S'","other triple","A second triple, the index of a source value x_{S'}.","direct","Through central wires $C_i$, $i\\in[h]$, gather adds $\\sum_{S'\\ni i}x_{S'}$ to $C_i$, with $S'$ another triple, and scatter adds $\\sum_{i\\in S}C_i$ to $y_S$."),
B("a","bank index","The index of a value in a data bank, a triple of triples.","direct","Banks $X_a,Y_a$ are indexed by $a\\in\\mathcal T^3$, a triple of triples."),
B("\\sigma","side scratch vector","The initial values of the side scratch wires.","direct","Let $\\sigma,\\gamma$ be the initial side and central scratch vectors; $\\mathcal V,\\mathcal G,\\mathcal J,\\mathcal R$ are the copy, gather, injection and scatter maps."),
B("\\gamma","central scratch vector","The initial values of the central scratch wires.","direct","Let $\\sigma,\\gamma$ be the initial side and central scratch vectors; $\\mathcal V,\\mathcal G,\\mathcal J,\\mathcal R$ are the copy, gather, injection and scatter maps."),
B("I","invocation count","The number of invocations.","count","Three stages each run $v^2$ invocations with their own scratch wires, so there are $I=3v^2=78440670000$ invocations."),
B("z_{\\rm b}","bit neighbours","The number of neighbours of a fixed triple in the bit construction.","count","A fixed triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ neighbours in the bit construction"),
B("z_{\\rm c}","complex neighbours","The number of neighbours of a fixed triple in the complex construction.","count","It has $z_{\\rm c}=\\binom{97}{3}+3\\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two)."),
B("c_{\\rm b}","bit central wires","The number of central wires per invocation in the bit network.","count",QC),
B("c_{\\rm c}","complex central wires","The number of central wires per invocation in the complex network.","count",QC),
B("W_{\\rm b}","bit wire count","The number of wires of the bit network.","count","The bit network has $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})=177176569091445000000$ wires"),
B("W_{\\rm c}","complex wire count","The number of wires of the complex network.","count","The complex network has $W_{\\rm c}=2N+I(vz_{\\rm c}+c_{\\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length."),
]
q="In the complex construction, the network has scalars in $\\mathbb Z[i,1/2]$, the Gaussian integers over powers of two of [Fixed-point Gaussian dyadic records](fixed-point.md), and the neighbours of a triple are the distinct triples with even intersection (zero or two)."
assert q in s
json.dump({"derivations":d,"symbols":sy,"relations":[{"prerequisite":"fixed-point","predicate":"has scalars in","quote":q}]},open('../0083-write-exchange-network.answer.json','w'),indent=1)
