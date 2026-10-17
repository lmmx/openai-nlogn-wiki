Nested subspace labels give each vertex of the [exchange network](exchange-network.md) a subspace of an $m$-dimensional space, nested along edges, whose dimension changes count each edge's *smaller calls*, recursive calls at an $m$ times smaller parameter. They choose the frames of [Frames on wire arrays](array-frames.md) so that $W$ wires cost $s<Wm$ smaller calls.

A subspace $U$ is *nondegenerate* when the form restricted to it is; then the space splits as $U\perp U^\perp$. *Triples* are three-element subsets of $[h]$. Bit labels live in $F=\mathbb Q^h$ with the nondegenerate form $\langle x,y\rangle=x^{\mathsf T}y-\frac19(\sum_ix_i)(\sum_iy_i)$ <cite data-source="paper">This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate</cite>, complex ones in $F=\mathbb F_2^h$ with the dot product. For triples $S,T$, the indicator vectors $t_S,t_T$ have $t_S^{\mathsf T}t_T=|S\cap T|$ and entry sum $3$, so $\langle t_S,t_T\rangle=|S\cap T|-1$; over $\mathbb F_2$, $t_S\cdot t_T=|S\cap T|\bmod 2$. Each line $\langle t_T\rangle$ is thus nondegenerate ($\langle t_T,t_T\rangle\neq0$), and neighbours (sharing one element, or an even number) are orthogonal.

Labels are built as [tensor products of subspaces](tensor-product-of-spaces.md) inside $\mathcal F=F^{\otimes3}$, of dimension $m=h^3$, where the form multiplies factorwise. Banks $X$ and $Y$ hold the data wires $X_a,Y_a$, indexed by the $N$ tuples $a=(a_1,a_2,a_3)$ of triples. With $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$ the terminal labels are

$$
\begin{array}{c|cc}&\text{source}&\text{sink}\\\hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{scratch}&0&\mathcal F\end{array}
$$

Source dimensions total $N$ and sink dimensions $Nm+N(m-1)+(W-2N)m=Wm-N$. A wire enters and leaves each gate with the gate's label, so signed changes telescope along wires to $Wm-2N$. If decreasing edges lose $L$ dimensions in all, absolute changes total $Wm-2N+2L$; the labels keep $L$ small.

Stage $j$ acts on coordinate $a_j$. In one invocation put $A=F^{\otimes(j-1)},\ P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle,\ B=P^\perp\cap A,\ K=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$ (empty products are scalars). Data labels move

$$
X:\ A\otimes\langle t_{a_j}\rangle\otimes K\to A\otimes F\otimes K,\qquad Y:\ B\otimes\langle t_{a_j}\rangle\otimes K\to\bigl((B\otimes F)\perp(P\otimes t_{a_j}^\perp)\bigr)\otimes K.
$$

Splitting $A=B\perp P$ and $F=\langle t_{a_j}\rangle\perp t_{a_j}^\perp$ cuts $A\otimes F$ into four orthogonal nondegenerate pieces; the complement of $P\otimes\langle t_{a_j}\rangle$ is the other three: $(P\otimes\langle t_{a_j}\rangle)^\perp_{A\otimes F}=(B\otimes F)\perp(P\otimes t_{a_j}^\perp)$. It is the next stage's $B'$, for $A'=A\otimes F$ and $P'=P\otimes\langle t_{a_j}\rangle$; with $K=\langle t_{a_{j+1}}\rangle\otimes K'$ the outputs $A'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$ are stage $j+1$'s inputs. Stage $1$ starts at $U_a,0$ ($B=0$) and stage $3$ ends at $\mathcal F,U_a^\perp$.

Gates act at times $0,\dots,7$, each giving one data wire and its side wires, or all centre wires, one label. Suppressing $K$, with $t_X,t_Y$ the indicators of the $X$- and $Y$-bank triples involved, each wire's labels (times bracketed) are

$$
\begin{aligned}\text{centre: }&0\to B\otimes F\,(1)\to A\otimes F\,(3)\to B\otimes F\,(4)\to A\otimes F\,(6)\to\mathcal F\\ \text{side: }&0\to B\otimes\langle t_Y\rangle\,(0)\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\to A\otimes F\,(7)\to\mathcal F\\ X:\ &A\otimes\langle t_X\rangle\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to A\otimes F\,(3,6,7)\\ Y:\ &B\otimes\langle t_Y\rangle\,(0)\to B\otimes F\,(1,4)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\end{aligned}
$$

The same splitting shows every arrow is an inclusion except centre $3\to4$, dropping $P\otimes F$ of dimension $h$; side $2\to5$ uses $\langle t_X\rangle\subset t_Y^\perp$, from $t_X\perp t_Y$. With $I$ invocations of $c_{\rm b}$ centre wires, the bit network loses $L_{\rm b}=Ic_{\rm b}h$; as $I=3\binom h3^2$ and $N=\binom h3^3$, $L_{\rm b}/N=3c_{\rm b}h/\binom h3=100/539$, and likewise $L_{\rm c}/N=101/539$, both below $1/2$ <cite data-source="paper">\frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}</cite>.

Bit vertices labelled $U$ get the projection $\Pi_U$ onto $U$ along $U^\perp$, except $X_a$'s source ($-\Pi_{U_a}$) and other sources ($0$). An edge costs one smaller call per unit of rank of its matrix difference <cite data-source="paper">implements an edge change with one smaller interchange per unit of its rational rank</cite>. For $U\subset V$, $\Pi_V-\Pi_U$ (identity on $V\cap U^\perp$, zero on $U\perp V^\perp$) has rank $\dim V-\dim U$, as does its negative. Only $X_a$'s first edge, into a gate labelled $U_a$, differs: $2\Pi_{U_a}$ has rank one, its dimension change zero. So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$ <cite data-source="paper">=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m</cite>. Endpoint differences, $\Pi_{U_a^\perp}+\Pi_{U_a}$ from $X_a$ to $Y_a$ and $\mathrm{Id}-0$ otherwise, all equal $\mathrm{Id}$. [Binary phase frames](phase-frames.md) give the complex network $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.

The saving is positive as $L_{\rm b}/N<1/2$, but tiny: $(W_{\rm b}m-s_{\rm b})/(W_{\rm b}m)=339/22587335000000\approx1.5\cdot10^{-11}$ <cite data-source="paper">=\frac{339}{22587335000000}</cite>, as $N-2L_{\rm b}<N$ while side wires make $W_{\rm b}m\approx4\cdot10^{10}N$.
