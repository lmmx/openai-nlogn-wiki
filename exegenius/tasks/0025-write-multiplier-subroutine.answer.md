The established fast multiplier is the known deterministic algorithm of Harvey and van der Hoeven that multiplies two integers, each with $n$ bits, in $O(n\log n)$ time, where $n$ denotes the bit length of each integer. The argument does not reprove it: it is a black box, called whenever a product of two shorter integers is needed.

Within the argument, the multiplier runs on a [Fixed-tape machine model](fixed-tape-model.md). Each call to it is an ordinary subroutine call; <cite data-source="paper">they do not invoke the improved theorem recursively.</cite>

The multiplier is needed for polynomial products. Those products are formed by [Signed coefficient packing](signed-packing.md), which packs polynomial coefficients into one integer, so that a single integer product carries a whole polynomial product. The multiplier computes these integer products.
