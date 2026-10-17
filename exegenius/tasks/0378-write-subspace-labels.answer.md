Nested subspace labels attach to each source, gate and sink of the [exchange network](exchange-network.md) a subspace of a fixed $m$-dimensional space, nested along every edge, so that an edge's dimension change counts its *smaller calls*, recursive calls at an $m$ times smaller parameter. The labels choose the frames of [Frames on wire arrays](array-frames.md) so that the network's $W$ wires ($W$ is now a wire count, $W_{\rm b}$ or $W_{\rm c}$) cost $s<Wm$ smaller calls ($s_{\rm b}$ or $s_{\rm c}$), the strict saving the recursion needs.

A subspace $U$ is *nondegenerate* when the form restricted to it is; then the space is $U\perp U^\perp$, where $\perp$ joins orthogonal subspaces. Bit labels use $F=\mathbb Q^h$ with the form $x\cdot y-\frac19(x\cdot\mathbf 1)(y\cdot\mathbf 1)$ for vectors $x,y\in F$, nondegenerate as its matrix fixes zero-sum vectors and scales the all-ones vector $\mathbf 1$ by $1-h/9=-91/9$. Complex labels use $F=\mathbb F_2^h$ with the dot product.

Triples $S,S'\in\mathcal T$ have indicator vectors $t_S,t_{S'}$ with dot product $|S\cap S'|$ and entry sums $3$, so $\langle t_S,t_{S'}\rangle=|S\cap S'|-1$; over $\mathbb F_2$, $t_S\cdot t_{S'}=|S\cap S'|\bmod2$. So each *triple line* $\langle t_S\rangle$, spanned by $t_S$, is nondegenerate ($\langle t_S,t_S\rangle\in\{2,1\}$), and *neighbours* are orthogonal: triples sharing one element (bit), or distinct triples sharing zero or two (complex).

Label dimensions are computed from three facts about [tensor products of subspaces](tensor-product-of-spaces.md): for subspaces $E,E',G$ of tensor powers of $F$, $\dim(E\otimes G)=\dim E\cdot\dim G$; the form multiplies factorwise, so products of nondegenerate subspaces are nondegenerate; and $(E\perp E')\otimes G=(E\otimes G)\perp(E'\otimes G)$. Labels lie in $\mathcal F=F\otimes F\otimes F$, of dimension $h^3=m$. With $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$ for each data index $a$, the terminal labels are

$$
\begin{array}{c|cc}&\text{source}&\text{sink}\\\hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{scratch}&0&\mathcal F\end{array}
$$

Source dimensions sum to $N$, sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$. A wire enters and leaves each gate with that gate's label, so its signed changes telescope to sink minus source dimension; over all wires they sum to $Wm-2N$. If decreasing edges lose $L$ dimensions in total ($L_{\rm b}$ or $L_{\rm c}$), absolute changes sum to $Wm-2N+2L$. Bit-network edges cost their absolute change, plus one call per input $X_a$ (below), so $s_{\rm b}=W_{\rm b}m-(N-2L_{\rm b})$: the saving is what the loss leaves of the budget $N$, so the labels confine all loss to one small edge.

Stage $j\in\{1,2,3\}$ ($j$ is now a stage index) varies $a_j$. In one of its invocations let $A=F^{\otimes(j-1)}$, of dimension $h^{j-1}$; $P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle$, the line of the earlier factors; $B=P^\perp$ in $A$; and $Q=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$, the line of the later ones. Empty products are the scalars, so at stage 1, $B=0$. As $P$ is nondegenerate, $A=B\perp P$ and $\dim B=h^{j-1}-1$. For subspaces $G,E\subseteq F$ write

$$
[G\mid E]=\bigl((B\otimes G)\perp(P\otimes E)\bigr)\otimes Q ,
$$

of dimension $(h^{j-1}-1)\dim G+\dim E$; it lies in $[G'\mid E']$ whenever $G\subseteq G'$ and $E\subseteq E'$, as its parts lie in the orthogonal pieces $B\otimes F\otimes Q$ and $P\otimes F\otimes Q$. With $t_{a_j}$ the indicator of the wire's $j$th triple, the data labels move as

$$
X_a:\ [\langle t_{a_j}\rangle\mid\langle t_{a_j}\rangle]\to[F\mid F],\qquad Y_a:\ [\langle t_{a_j}\rangle\mid0]\to[F\mid t_{a_j}^\perp].
$$

They fit: the next stage has $A'=A\otimes F$ and $P'=P\otimes\langle t_{a_j}\rangle$. Splitting $A=B\perp P$ and $F=\langle t_{a_j}\rangle\perp t_{a_j}^\perp$ cuts $A'$ into four orthogonal pieces, so $B'=P'^\perp$ is the other three, $(B\otimes F)\perp(P\otimes t_{a_j}^\perp)$. With $Q=\langle t_{a_{j+1}}\rangle\otimes Q'$, the outgoing labels are $A'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes Q'$, stage $j+1$'s incoming labels. Stage 1 starts at $U_a$ and $0$; stage 3 ends at $\mathcal F$ and, as $P'=U_a$ there, $U_a^\perp$.

Gates act at times $0,\dots,7$, each giving all its wires one label. With $t_X,t_Y$ the indicators of the $j$th triples of the $X$- and $Y$-entries a wire serves (for a side wire, the neighbours it joins), each wire's labels, with gate times as subscripts, are

$$
\begin{aligned}\text{centre: }&0\to[F\mid0]_1\to[F\mid F]_3\to[F\mid0]_4\to[F\mid F]_6\to\mathcal F\\ \text{side: }&0\to[\langle t_Y\rangle\mid0]_0\to[F\mid\langle t_X\rangle]_2\to[F\mid t_Y^\perp]_5\to[F\mid F]_7\to\mathcal F\\ X:\ &[\langle t_X\rangle\mid\langle t_X\rangle]\to[F\mid\langle t_X\rangle]_2\to[F\mid F]_{3,6,7}\\ Y:\ &[\langle t_Y\rangle\mid0]_0\to[F\mid0]_{1,4}\to[F\mid t_Y^\perp]_5\end{aligned}
$$

Rows sharing a time meet at that gate and agree there. Comparing entries, every arrow is an inclusion except centre $3\to4$, which drops $P\otimes F\otimes Q$, of dimension $h$; side $2\to5$ needs $\langle t_X\rangle\subseteq t_Y^\perp$, true as neighbours are orthogonal. All labels are nondegenerate, as their pieces are. Each of the $I=3v^2$ invocations has $c_{\rm b}=100$ (bit) or $c_{\rm c}=101$ (complex) centre wires, each losing $h$ once, so $L_{\rm b}=Ic_{\rm b}h$ and $L_{\rm c}=Ic_{\rm c}h$. As $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$ and $L_{\rm c}/N=101/539$. Both are below $1/2$ <cite data-source="paper">In particular, both are smaller than $1/2$.</cite>.

In the bit network a vertex labelled $U$ gets the projection $\Pi_U$ onto $U$ along $U^\perp$, except sources: $-\Pi_{U_a}$ at $X_a$, else $0=\Pi_0$. Each matrix gives a frame adding it times one address chunk to another, so an edge shears by its endpoint matrices' difference, costing one smaller call per unit of rational rank (rank over $\mathbb Q$) <cite data-source="paper">implements an edge change with one smaller interchange per unit of its rational rank</cite>.

For nondegenerate $U\subseteq U'$, a vector of $U'$ minus its projection onto $U$ lies in $U'\cap U^\perp$, so $\mathcal F=U\perp(U'\cap U^\perp)\perp U'^\perp$. Both projections fix $U$ and vanish on $U'^\perp$; only $\Pi_{U'}$ fixes $U'\cap U^\perp$. So $\Pi_{U'}-\Pi_U$ projects onto $U'\cap U^\perp$, of rank $\dim U'-\dim U$, as does its negative on a reversed edge. So each edge's rank is its absolute dimension change, except the first edge of each $X_a$. At stage 1, $B=0$, so that edge joins $U_a$ to $[F\mid\langle t_{a_1}\rangle]=U_a$, a zero change, yet its matrix $\Pi_{U_a}-(-\Pi_{U_a})=2\Pi_{U_a}$ has image the line $U_a$: rank one. Hence

$$
s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m
$$

<cite data-source="paper">=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m</cite>. The negative source makes every route's endpoint difference $\mathrm{Id}$ ($\Pi_{U_a^\perp}+\Pi_{U_a}$ from $X_a$ to $Y_a$, $\Pi_{\mathcal F}-0$ elsewhere), so every role gets the same shear. [Binary phase frames](phase-frames.md) turn the same count, without the source extra, into the complex network's $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.

The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive as $L_{\rm b}/N<1/2$, but tiny: with $Iv=3N$ and $Ic_{\rm b}=N/539$, $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, mostly side wires, each costing $m$. So $s_{\rm b}/W_{\rm b}=m\bigl(1-\frac{339}{22587335\,m}\bigr)$, a relative deficit of $\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$ <cite data-source="paper">=\frac{339}{22587335000000}</cite>.
