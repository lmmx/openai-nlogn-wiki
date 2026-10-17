import json,re
t=open('/home/user/e2e-run/exegenius/tasks/0111-write-simultaneous-layer.answer.md').read()
def span(a,b,after=0):
    i=t.index(a,after); j=t.index(b,i)+len(b); return t[i:j]
S=[]
def sym(name,symbol,meaning,quote,rel='direct'):
    S.append(dict(symbol=symbol,name=name,meaning=meaning,relation=rel,quote=quote))
s1=span("The simultaneous butterfly","instead of $D$ passes.")
sym('selected chunk count','D','The number of address chunks carrying a selected bit.',s1,'count')
sym('chunk bound','d','An upper bound on the number of chunks a layer acts on.',s1)
s2=span("For records $z$","$b.$")
sym('record array','z','The array of records, a function of the address x.',s2)
sym('address','x','An address of the array, with selected bits x_1,...,x_D.',s2)
sym('phase diagonal','\\mathcal S_D','The diagonal operator multiplying the record at address x by i^{x_1+...+x_D}.',s2)
s3=span("A group of $e=mf$","in $\\mathbb F_2^m.$")
sym('group axis count','e','The number of axes in a group, e = mf.',s3,'count')
hq=span("Each edge changes frame","by $v).$")
sym('slot index','h','Index of a slot, and of the residual basis vector placed on it.',hq)
sym('residual vector','v_h','A vector of a basis of the edge\'s residual space, in F_2^m.',hq)
sym('edge sign','\\eta_h','The sign +1 or -1 of the kernel exponent attached to residual vector v_h.',hq)
sym('shifted kernel','C_v','The matrix aI+bX_v, the kernel C applied along the column direction v.',hq)
sym('column shift','X_v','The operator shifting the address of a column by v.',hq)
gq=span("For invertible $G$","X_{Gv}$")
sym('basis matrix','G','An invertible binary m by m matrix whose first columns are the residual vectors v_h.',gq)
sym('basis permutation','\\mathcal P_G','The address permutation moving a column value x to Gx.',gq)
sym('standard basis vector','e_h','The h-th standard basis vector of F_2^m.',span(", so the edge change is","standard basis)."))
sym('sign matrix','Z','The diagonal matrix diag(1,-1).',span("As $(C^{-1})","phases."))
rq=span("Row $Wq+w$","$V/W.$")
sym('row quotient','q','The quotient of a row index on division by W.',rq)
sym('row remainder','w','The remainder of a row index modulo W, which is the wire role.',rq)
sym('row chunk count','q_0','The number of leading chunks whose bits form the row index.',span("The first $q_0=","volume."),'count')
sym('step ratio','\\gamma','The ratio s/W, at most m^sigma.',span("Take $\\sigma<1$","$\\tau(1+c/\\beta)<\\lambda.$"))
sym('level index','j','The index of a recursion level, counted from 0.',span("Levels indexed by","=O(e^\\lambda).$"),'count')
lq=span("A leaf at level","d^{\\beta(1-\\sigma)}).$")
sym('leaf chunks','u','The number of active chunks in a leaf at level j, e/m^j.',lq,'count')
sym('piece digit','a_j','The base-m digit of D-q_0 at position j, the number of pieces of m^j chunks.',span("Writing $D-q_0","factor:"),'count')
sym('chain bound','A','A(e) bounds the number of arithmetic operations on a chain from an input to an intermediate coefficient in a group of e axes.',span("Let $A(e)$","coefficient."))
sym('invocation bound','E','The bound 64(W+m+1)^3 on operations added on a chain by one network invocation.',span("One invocation adds","children:"))
bq=t[t.index("$$A(e)")+2:t.index("$$",t.index("$$A(e)")+2)]
bq=span("Since $s\\xi","d^{\\nu+1}.$")
sym('bound','\\xi','Any bound of at least 1 on the chain operation count.',bq)
sym('recurrence base','B','The sum s+E.',bq)
sym('depth exponent','\\nu','The least j at least 1 with m^j at least B.',bq)
sym('guard constant','C_0','The constant 128mB^2 in the guard width.',span("Adding pieces,","here."))
sym('chain depth','\\ell','The number of operations along a chain, the depth of a value.',span("For disk inputs","denominator bit."),'count')
sym('axis exponent','\\epsilon','A fixed exponent with d = Theta(p^epsilon).',span("For $d=\\Theta","width $O(p).$"))
R=[
dict(prerequisite='phase-frames',predicate='is computed by the network of',quote=span("On the group,","(phase-frames.md)."))
,dict(prerequisite='packed-bit-addition',predicate='performs its row additions by',quote=span("Gaussian elimination writes","(packed-bit-addition.md)."))
,dict(prerequisite='rank-recurrence',predicate='saves power as in',quote=span("It saves power","(rank-recurrence.md)."))
,dict(prerequisite='fixed-point',predicate='is evaluated exactly in',quote=span("The layer is evaluated","(fixed-point.md)."))
]
Dv=[
('S1.6.1',span("The [two-point kernel","$\\mathsf S=\\operatorname{diag}(1,i)$")),
('S1.6.2',span("Gaussian elimination writes","inverse children need only signs and phases.")),
('S1.6.2b',s2),
('S1.6.3b',span("So the complete basis change","$O(V((eK)^\\tau+1))$")),
('S1.6.4',span("For $e\\ge d^\\beta,$","d^{\\beta(1-\\sigma)}).$")),
('S1.6.5',span("For disk inputs","represent every intermediate coefficient exactly")),
('S1.6.6',span("Each row of $H_0$","H_0^{\\otimes D}$ has absolute row sum one")),
('S1.6.7',span("Truncation toward zero","\\sqrt2\\,2^{-p}$")),
]
json.dump(dict(symbols=S,relations=R,derivations=[dict(step=a,quote=b) for a,b in Dv]),open('/home/user/e2e-run/exegenius/tasks/0111-write-simultaneous-layer.answer.json','w'),indent=1)
