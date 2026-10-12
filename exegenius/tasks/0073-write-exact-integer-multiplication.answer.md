Exact integer multiplication is computing the full product of two binary integers, with no rounding or error. It is the target problem of this wiki, so its input and output must be fixed precisely first.

Let $n$ be the common length of the two inputs. The input is two binary strings $x$ and $y$ of length $n$, and the output is the $2n$-bit binary representation of their product. On a tape the input is written as $x\#y$, with $\#$ a separator symbol.

Write $\mathrm{val}(x)$ for the nonnegative integer whose binary digits are $x$, with the leftmost bit most significant, so $\mathrm{val}(10)=2$ and $\mathrm{val}(11)=3$. For a nonnegative integer $z < 2^{2n}$, write $\mathrm{bin}_{2n}(z)$ for its binary representation padded on the left with zeros to exactly $2n$ bits.

The required output is $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$. Since $\mathrm{val}(x)\,\mathrm{val}(y) < 2^{2n}$, the product always fits in $2n$ bits. For $n=2$, $x=10$ and $y=11$, the product is $2 \cdot 3 = 6$, so the output is $\mathrm{bin}_4(6)=0110$.

In the main result of this wiki, exact integer multiplication is computed by a deterministic [fixed-tape machine](fixed-tape-model.md) in time below $n\lg n$. The result is stated for one fixed machine. <cite data-source="paper">There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs.</cite>
