Exact integer multiplication is the task of computing the full product of two integers given in binary, with no rounding or truncation. The target result is a faster algorithm for this task, measured by its running time.

The input is two binary strings separated by $\#$. Let $n$ be the number of bits in each input. Let $x$ be the first binary string, of length $n$. Let $y$ be the second binary string, also of length $n$. Both lie in $\{0,1\}^n$.

For a binary string $x$ of length $n$, let $\mathrm{val}(x)$ be its nonnegative integer value, with the leftmost bit most significant. For $0 \le z < 2^k$, let $\mathrm{bin}_k(z)$ be the binary representation of $z$, padded on the left with zeros to length $k$.

The output is $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$, the $2n$-bit representation of the product. Two $n$-bit numbers have a product below $2^{2n}$, so $2n$ bits always suffice.

For $n = 2$, $x = 10$ and $y = 11$ give $\mathrm{val}(x) = 2$ and $\mathrm{val}(y) = 3$, and the output is $\mathrm{bin}_4(6) = 0110$.

Running time is counted on a deterministic multitape Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, working for every $n$. It is the worst case over all inputs of length $n$, as a function of $n$.

In 1971, Schönhage and Strassen gave a multitape Turing machine for this task with running time $O(n \log n \log\log n)$ <cite data-source="paper">can be multiplied in O(n log n log log n) time on a multitape Turing machine</cite>. Harvey and van der Hoeven then obtained an unconditional $O(n \log n)$ bound <cite data-source="paper">unconditional O(n log n) upper bound</cite>.

The target result gives a strict power saving in the logarithmic factor, <cite data-source="paper">in the same fixed finite-tape model</cite>.
