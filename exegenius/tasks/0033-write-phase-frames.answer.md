A binary phase frame attaches to each label of [Nested subspace labels and rank deficit](subspace-labels.md) a basis for arrays of binary addresses, so that the change of basis along an edge is a product of two-point kernels. Here $m$ is the number of binary coordinates of an address $x$, and a label $U$ is a subspace of $\mathbb F_2^m$.

Write $\operatorname{wt}(x)$ for Hamming weight, $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$, and $P_U$ for the projection onto $U$ over $\mathbb F_2$. Put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$. With $H=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, the phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries. <cite data-source="paper">Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$</cite> Let $C=H\operatorname{diag}(1,i)H=aI+bX$, with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$, $X$ the coordinate swap, and $X_v$ the translation $(X_vf)(x)=f(x+v)$.

## One edge

For binary vectors $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$. The dot product $z\cdot w$ is that intersection size mod $2$. If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.

Take an edge from $U$ to $V=U\perp E$, with residual $E$ orthogonal to $U$ and orthonormal basis $\mathcal B$ (distinct vectors have dot product $0$, and $v\cdot v=1$). Then $P_Vx=P_Ux+\sum_{v\in\mathcal B}[v\cdot x]\,v$ so $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$, negated on a decreasing edge, and each $\operatorname{wt}(v)$ is odd.

Odd weight is $\pm1$ modulo four, so each term is $\varepsilon[v\cdot x]$, $\varepsilon=\pm1$. The function $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$.

Since $H^2=I$, $\mathcal C_V\mathcal C_U^{-1}=H^{\otimes m}\operatorname{diag}(i^{q_V-q_U})H^{\otimes m}$, one phase per $v$. The character $(-1)^{v\cdot x}$ is $\operatorname{diag}(1,-1)$ on $\operatorname{supp}(v)$. Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse ($\varepsilon=-1$).

Each edge factor is built as a translate $aI+bX_v$ of [Two-point kernel C](phase-kernel.md), combining only $f(x)$ and $f(x+v)$, a butterfly-type operation. A residual of dimension $d$ costs $d$ such calls, one smaller call per dimension, as the recursion needs.

## Counting

Here $W_{\rm c}$ is the number of wires of the complex network, and $N$, $L_{\rm c}$ are constants of the labels page. Over the network the number of translation-kernel factors is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$. <cite data-source="paper">s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}</cite> The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$. <cite data-source="paper">The deficit is $2N-2L_{\rm c}>0$.</cite>

## The exceptional pair

For the pair $X_a\to Y_a$, take $u=u_a$ of binary norm one and weight $27$. Orthogonal additivity gives $\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]$, and $27$ is odd, so $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.

Let $Z=\operatorname{diag}(1,-1)$; then $C=iZC^{-1}Z$. For $k$ columns, let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column. The identity $C=iZC^{-1}Z$ turns each of the $27k$ inverse factors into $C$ after applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, so every role, scratch roles included, receives $C^{\otimes mk}$.
