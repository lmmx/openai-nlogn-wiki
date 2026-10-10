The bit complexity of an algorithm is its running time counted in elementary bit operations on a fixed machine model. A machine that works on bits, such as a [multitape Turing machine](turing-machine-model.md), counts one step for each cell it reads or writes and each move of a head. Bit complexity therefore charges for every bit of every number that is moved or combined.

This differs from counting arithmetic operations on machine words. If a computer multiplies two 64-bit words in one instruction, an arithmetic count records one operation, while the bit count charges for each of the bits involved. For problems on large integers, the bit count is the honest measure, because the numbers themselves grow with $n$.

For example, adding two $n$-bit integers by reading the bits from least to most significant takes $O(n)$ bit steps. Adding them as single operations would hide the length of the numbers, so the bit count is what distinguishes the cost of the addition for different $n$.

The paper's main result is a bound on the bit complexity of exact integer multiplication. Its statement that the algorithm establishes a bit-complexity bound means that the worst-case number of bit steps on the fixed tape model is $O(n(\lg n)^{1-\kappa})$, as in the [main theorem](main-theorem.md).
