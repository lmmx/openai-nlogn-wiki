Exact integer multiplication is the task of computing the full product of two integers given in binary, with no rounding or truncation. It is the problem whose running time the target result improves.

The input is two binary strings separated by $\#$. Let $n$ be the number of bits in each input. Let $x$ be the first binary string, of length $n$. Let $y$ be the second binary string, also of length $n$. Both lie in $\{0,1\}^n$.

For a binary string $x$ of length $n$, let $\mathrm{val}(x)$ be its nonnegative integer value, with the leftmost bit most significant. Let $k$ be a length in bits. Let $z$ be a nonnegative integer below $2^k$, and let $\mathrm{bin}_k(z)$ be the binary representation of $z$, padded on the left with zeros to length $k$.

The output is $\mathrm{bin}_{2n}(\mathrm{val}(x)\,\mathrm{val}(y))$, the $2n$-bit representation of the product. Two $n$-bit numbers have a product below $2^{2n}$, so $2n$ bits always suffice. For $n = 2$, $x = 10$ and $y = 11$ give $\mathrm{val}(x) = 2$ and $\mathrm{val}(y) = 3$, and the output is $\mathrm{bin}_4(6) = 0110$.

Running time is the worst case over all inputs of length $n$, as a function of $n$, on a deterministic multitape Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.

In 1971, Schönhage and Strassen gave a multitape Turing machine for this task with running time $O(n \log n \log\log n)$ <cite data-source="paper">can be multiplied in O(n log n log log n) time on a multitape Turing machine</cite>. Harvey and van der Hoeven then obtained an unconditional $O(n \log n)$ bound <cite data-source="paper">unconditional O(n log n) upper bound</cite>. The target result is a strict power saving in the logarithmic factor <cite data-source="paper">in the same fixed finite-tape model</cite>.
