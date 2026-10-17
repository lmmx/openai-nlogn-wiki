import json
P="Linear exchange network with restored scratch wires"
def s(sym,name,meaning,rel,quote): return dict(symbol=sym,name=name,meaning=meaning,relation=rel,quote=quote)
symbols=[
 s("X","first data bank","One of the two data banks, with entries X_a.","direct","There are two data banks $X=(X_a)$ and $Y=(Y_a)$, indexed by $a\\in\\mathcal T^3$ ($a$ here is a triple of triples, not a shift exponent)."),
 s("Y","second data bank","The other data bank, with entries Y_a.","direct","There are two data banks $X=(X_a)$ and $Y=(Y_a)$, indexed by $a\\in\\mathcal T^3$ ($a$ here is a triple of triples, not a shift exponent)."),
 s("a","bank index","A triple of three-element subsets of [h] indexing the entries of the banks.","direct","There are two data banks $X=(X_a)$ and $Y=(Y_a)$, indexed by $a\\in\\mathcal T^3$ ($a$ here is a triple of triples, not a shift exponent)."),
 s("h","ground-set size","The size of the ground set [h] whose three-element subsets index the banks.","direct","Fix the ground-set size $h=100$ and write $[h]=\\{1,\\dots,h\\}$."),
 s("\\mathcal T","triple set","The set of three-element subsets of [h].","direct","Let $\\mathcal T$ be the set of three-element subsets of $[h]$, so that $v=\\binom h3=161700$ counts them."),
 s("v","number of triples","The number of three-element subsets of [h].","count","Let $\\mathcal T$ be the set of three-element subsets of $[h]$, so that $v=\\binom h3=161700$ counts them."),
 s("N","bank size","The number of values in each data bank.","count","Set $N=v^3=4227952113000000$ for the size of each bank, and $m=h^3=1000000$ for the dimension of the label space used later."),
 s("m","label-space dimension","The dimension of the label space used on later pages.","direct","Set $N=v^3=4227952113000000$ for the size of each bank, and $m=h^3=1000000$ for the dimension of the label space used later."),
 s("I","invocation count","The number of invocations over all three stages.","count","A stage covers all $v^2$ choices of the other two coordinates, each with its own invocation and scratch wires, so there are $I=3v^2=78440670000$ invocations."),
 s("z_{\\rm b}","bit neighbour count","The number of neighbours of a fixed triple in the bit construction.","count","A triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ neighbours in the bit construction"),
 s("z_{\\rm c}","complex neighbour count","The number of neighbours of a fixed triple in the complex construction.","count","It has $z_{\\rm c}=\\binom{97}{3}+3\\cdot97=147731$ neighbours in the complex construction (intersection zero plus two)"),
 s("c_{\\rm b}","bit central wires","The number of central wires per invocation in the bit network.","count","There are $c_{\\rm b}=100$ central wires per invocation in the bit network and $c_{\\rm c}=101$ in the complex one."),
 s("c_{\\rm c}","complex central wires","The number of central wires per invocation in the complex network.","count","There are $c_{\\rm b}=100$ central wires per invocation in the bit network and $c_{\\rm c}=101$ in the complex one."),
 s("W_{\\rm b}","bit wire count","The total number of wires in the bit network.","count","The bit network has $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})=177176569091445000000$ wires"),
 s("W_{\\rm c}","complex wire count","The total number of wires in the complex network.","count","The complex network has $W_{\\rm c}=2N+I(vz_{\\rm c}+c_{\\rm c})=1873807244643542670000$ wires"),
]
def d(step,q): return dict(step=step,quote=q)
body=open("0257-write-exchange-network.answer.md").read()
der=[
 d("S1.1.1","Fix the ground-set size $h=100$ and write $[h]=\\{1,\\dots,h\\}$. Let $\\mathcal T$ be the set of three-element subsets of $[h]$, so that $v=\\binom h3=161700$ counts them."),
 d("S1.1.2","Set $N=v^3=4227952113000000$ for the size of each bank, and $m=h^3=1000000$ for the dimension of the label space used later."),
 d("S1.1.3","A stage covers all $v^2$ choices of the other two coordinates, each with its own invocation and scratch wires, so there are $I=3v^2=78440670000$ invocations."),
 d("S1.1.4a","In the bit construction, scalars lie in $\\mathbb F_2$ and $S,S'$ are neighbours when $|S\\cap S'|=1$."),
 d("S1.1.4b","In the complex construction the network keeps its scalars in $\\mathbb Z[i,1/2]$, the values of [Fixed-point Gaussian dyadic records](fixed-point.md), and the neighbours of a triple are the distinct triples with even intersection (zero or two)."),
 d("S1.1.5","The net change of $y$ is $(\\mathcal J\\mathcal V+\\mathcal R\\mathcal G)x$, free of $\\sigma,\\gamma$; by the coefficients above it is $y\\gets y+x$. So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged"),
 d("S1.1.6","Run forward $X\\to Y$ at stage 1, inverse $Y\\to X$ at stage 2 and forward $X\\to Y$ at stage 3. At every $a$,\n$$(x,y)\\mapsto(x,y+x)\\mapsto(-y,y+x)\\mapsto(-y,x),$$\nthat is $(X_a,Y_a)\\mapsto(-Y_a,X_a)$"),
 d("S1.1.7a","A triple has $z_{\\rm b}=3\\binom{97}{2}=13968$ neighbours in the bit construction"),
 d("S1.1.7b","It has $z_{\\rm c}=\\binom{97}{3}+3\\cdot97=147731$ neighbours in the complex construction (intersection zero plus two)"),
 d("S1.1.7c","There are $c_{\\rm b}=100$ central wires per invocation in the bit network and $c_{\\rm c}=101$ in the complex one."),
 d("S1.1.8a","The bit network has $W_{\\rm b}=2N+I(vz_{\\rm b}+c_{\\rm b})=177176569091445000000$ wires"),
 d("S1.1.8b","The complex network has $W_{\\rm c}=2N+I(vz_{\\rm c}+c_{\\rm c})=1873807244643542670000$ wires"),
]
for x in der+symbols:
    assert x["quote"] in body, x["quote"]
rel=[dict(prerequisite="fixed-point",predicate="keeps its scalars in",quote="In the complex construction the network keeps its scalars in $\\mathbb Z[i,1/2]$, the values of [Fixed-point Gaussian dyadic records](fixed-point.md), and the neighbours of a triple are the distinct triples with even intersection (zero or two).")]
assert rel[0]["quote"] in body
json.dump(dict(symbols=symbols,relations=rel,derivations=der),open("0257-write-exchange-network.answer.json","w"),indent=1)
