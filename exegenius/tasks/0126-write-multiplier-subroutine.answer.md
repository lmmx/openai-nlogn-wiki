The established fast multiplier is the known deterministic algorithm of Harvey and van der Hoeven that multiplies two integers of $n$ bits each in $O(n\log n)$ time. The argument treats it as a black box: it does not reprove the algorithm, but uses only its behaviour (two integers in, their product out) and its time bound, and calls it whenever the product of two shorter integers is needed.

Within the argument the multiplier runs on a [Fixed-tape machine model](fixed-tape-model.md). Its calls are ordinary subroutine calls. <cite data-source="paper">they do not invoke the improved theorem recursively.</cite>

The improved theorem is the result the argument proves: a multiplier with time $O(n(\lg n)^{1-\kappa})$ on the same model. If a call used it, a call on $m$-bit integers would cost on the order of $m(\lg m)^{1-\kappa}$, so the cost of each call would depend on the very bound being proved, and the proof would assume its own conclusion.

The multiplier is needed for polynomial products, which [Signed coefficient packing](signed-packing.md) turns into single integer products: packing places each coefficient at its own bit offset, so one product carries a whole polynomial product. The multiplier computes these integer products.
