Cyclic convolution is the product of two sequences of the same length in which indices wrap around modulo that length. The argument later computes this product with transforms, so the reader needs its exact definition and a small example.

Let $a = (a_0, \dots, a_{t-1})$ and $b = (b_0,\dots,b_{t-1})$ be two sequences of complex numbers of length $t$, a positive integer. Their cyclic convolution $c = a \ast b$ is the sequence of length $t$ given by the rule below. Here $i$ and $j$ index the entries of $a$ and $b$, and $k$ indexes the entries of $c$.

$$c_k = \sum_{\substack{0 \le i,\, j \le t-1 \\ i+j \equiv k \pmod{t}}} a_i\, b_j, \qquad 0 \le k \le t-1.$$

The condition $i+j \equiv k \pmod{t}$ means that $i+j$ and $k$ leave the same remainder on division by $t$. An index sum that runs past $t-1$ therefore wraps around to the start. In ordinary (linear) convolution the term $a_i b_j$ would sit at position $i+j$, which can reach $2t-2$. In cyclic convolution it is folded back onto a position between $0$ and $t-1$.

Example: take $t=3$, $a=(1,2,3)$ and $b=(4,5,6)$. The pairs with $i+j \equiv 0 \pmod 3$ are $(0,0)$, $(1,2)$ and $(2,1)$, so $c_0 = 4 + 12 + 15 = 31$. Similarly $c_1 = 5 + 8 + 18 = 31$ and $c_2 = 6 + 10 + 12 = 28$.

The paper uses the symbol $\ast$ for this product <cite data-source="paper">denote cyclic convolution in the displayed axes</cite>.
