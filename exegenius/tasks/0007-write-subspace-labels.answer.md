Nested subspace labels give each vertex of the [exchange network](exchange-network.md) a subspace of an $m$-dimensional space, nested along every edge. Dimension changes count an edge's smaller calls <cite data-source="paper">Their dimension changes count the smaller operations needed on an edge</cite>. They choose the frames of [Frames on wire arrays](array-frames.md) so that a network of $W$ wires makes $s<Wm$ smaller calls in total.

The network is indexed by *triples*, three-element subsets of a ground set of size $h=100$, and bit labels live in $F=\mathbb Q^h$, complex ones in $F=\mathbb F_2^h$. The bit form $\langle x,y\rangle=x^{\mathsf T}y-\frac19(\sum_ix_i)(\sum_iy_i)$ is nondegenerate <cite data-source="paper">This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate</cite>; the complex form is the dot product. Indicator vectors $t_S,t_T$ of triples $S,T$ satisfy $t_S^{\mathsf T}t_T=|S\cap T|$ and sum to $3$, so $\langle t_S,t_T\rangle=|S\cap T|-1$, while over $\mathbb F_2$ the dot product is $|S\cap T|\bmod 2$. Thus $\langle t_T,t_T\rangle\neq0$, so each line $\langle t_T\rangle$ is *nondegenerate* ($F=\langle t_T\rangle\perp t_T^\perp$), and neighbours, meeting in one element (bit) or evenly (complex), are orthogonal.

The space $\mathcal F=F^{\otimes3}$ of $h\times h\times h$ arrays has dimension $m=h^3$; $x\otimes y\otimes z$ has entries $x_iy_kz_l$, forms multiply factorwise and $\dim(U\otimes V)=\dim U\dim V$. $N$ counts the tuples $a=(a_1,a_2,a_3)$ of triples indexing the data wires $X_a,Y_a$. With $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$ the terminal labels are

$$
\begin{array}{c|cc}&\text{source}&\text{sink}\\\hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{scratch}&0&\mathcal F\end{array}
$$

Source dimensions sum to $N$ and sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$. Since a gate's wires share its label, signed changes telescope along each wire, totalling $Wm-2N$. If decreasing edges lose $L$ dimensions in total, absolute changes total $Wm-2N+2L$: the saving needs small $L$.

Stage $j$ varies $a_j$; put $A=F^{\otimes(j-1)},\ P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle,\ B=P^\perp\cap A,\ K=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$, empty products being scalars. Data labels move

$$
X:\ A\otimes\langle t_{a_j}\rangle\otimes K\to A\otimes F\otimes K,\qquad Y:\ B\otimes\langle t_{a_j}\rangle\otimes K\to(P\otimes\langle t_{a_j}\rangle)^\perp_{A\otimes F}\otimes K.
$$

With $A'=A\otimes F,\ B'=(P\otimes\langle t_{a_j}\rangle)^\perp_{A'},\ K=\langle t_{a_{j+1}}\rangle\otimes K'$ the outputs are $A'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$, stage $j+1$'s inputs; stage $1$ starts at $U_a,0$ (there $B=0$) and stage $3$ ends at $\mathcal F,U_a^\perp$.

Within a stage (times in parentheses; gate labels tensored by $K$; $t_X,t_Y$ indicate the triples a side wire joins):

$$
\begin{aligned}\text{centre: }&0\to B\otimes F\,(1)\to A\otimes F\,(3)\to B\otimes F\,(4)\to A\otimes F\,(6)\to\mathcal F\\ \text{side: }&0\to B\otimes\langle t_Y\rangle\,(0)\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\to A\otimes F\,(7)\to\mathcal F\\ X:\ &A\otimes\langle t_X\rangle\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to A\otimes F\,(3,6,7)\\ Y:\ &B\otimes\langle t_Y\rangle\,(0)\to B\otimes F\,(1,4)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\end{aligned}
$$

Splitting $A=B\perp P$ and $F=\langle t_T\rangle\perp t_T^\perp$ shows every arrow is a growing inclusion except centre $3\to4$, which drops $P\otimes F$ of dimension $h$; side $2\to5$ needs $t_X\perp t_Y$. With $I$ invocations of $\gamma$ central wires each, $L=I\gamma h$. As $I=3\binom h3^2$ and $N=\binom h3^3$ we get $L/N=3\gamma h/\binom h3$, below $1/2$ for $\gamma=100$ (bit) and $\gamma=101$ (complex): $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ <cite data-source="paper">\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}</cite>.

Bit vertices get rational $m\times m$ matrices: $\Pi_U$, the projection onto $U$ along $U^\perp$, where the label is $U$, except $-\Pi_{U_a}$ at $X_a$'s source and $0$ at other sources. For $U\subset V$ the difference $\Pi_V-\Pi_U$ is the identity on $V\cap U^\perp$ and zero on $U\perp V^\perp$, so has rank $\dim V-\dim U$ either way round. Only $X_a$'s first edge differs: its gate is labelled $U_a$, so $2\Pi_{U_a}$ has rank one with no dimension change. An edge costs one smaller call per unit of rank <cite data-source="paper">implements an edge change with one smaller interchange per unit of its rational rank</cite>, so $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$ <cite data-source="paper">=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m</cite>. Every route's endpoint difference is $\mathrm{Id}$: $\Pi_{U_a^\perp}+\Pi_{U_a}$ from $X_a$ and $\mathrm{Id}-0$ otherwise. The complex network has $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$ via [Binary phase frames](phase-frames.md).

The relative saving $(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000\approx1.5\cdot10^{-11}$ <cite data-source="paper">=\frac{339}{22587335000000}</cite> is positive as $L_{\rm b}/N<1/2$, yet tiny: at most $N$ is saved, while side wires alone cost $m$ each and $W_{\rm b}m/N\approx4\cdot10^{10}$.
