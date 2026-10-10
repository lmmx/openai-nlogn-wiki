The established multiplier is a known deterministic algorithm that multiplies two $N$-bit integers in $O(N \log N)$ time on a multitape Turing machine. Harvey and van der Hoeven proved this unconditional bound, and the paper uses it as a black box. It is the same kind of object as the [exact integer multiplication](exact-integer-multiplication.md) problem, but for the smaller records that appear inside the main algorithm.

The paper's main construction does not call itself recursively on its own large integers. It calls the established multiplier on records whose length is $O(rp)$, where $r$ is a power of two and $p$ is a precision parameter. The paper shows that this length is $o(n)$, so these calls are on inputs much shorter than the original problem.

The paper states that these calls are ordinary subroutine calls, and that they do not invoke the improved theorem recursively. So the bound it proves does not depend on any assumption about the subroutine beyond its known $O(N \log N)$ cost.

These calls are used in [signed coefficient packing](signed-packing.md), which turns a product of polynomials into one integer product. The cost of that product is charged once per record, and the total cost of all such products is part of the final cost bound.
