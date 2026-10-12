Exact integer multiplication is the problem of computing the full product of two binary integers, with no rounding and no error. The main result of this wiki is a faster machine for this problem, so its input and output must be fixed precisely first.

Let $n$ be the common length of the two inputs. Its input is two binary strings $x$ and $y$ of length $n$, and its output is the $2n$-bit binary representation of their product. On a tape the input is written as $x\#y$, with $\#$ a separator symbol.

Write $\mathrm{val}(x)$ for the nonnegative integer whose binary digits are $x$, with the leftmost bit most significant. So $\mathrm{val}(10)=2$ and $\mathrm{val}(11)=3$. Let $k$ be the number of bits the representation occupies. For $0 \le z < 2^k$, write $\mathrm{bin}_k(z)$ for the binary representation of $z$ padded on the left with zeros to exactly $k$ bits.

The required output is $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$. Since $\mathrm{val}(x)\,\mathrm{val}(y) < 2^{2n}$, the product always fits in $2n$ bits. For $n=2$, $x=10$ and $y=11$, the product is $2 \cdot 3 = 6$, so the output is $\mathrm{bin}_4(6)=0110$.

The main result of this wiki gives a deterministic fixed-tape machine that computes this product in time below $n\lg n$. The result is stated for one fixed machine. <cite data-source="paper">There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs.</cite>
