The transform identity with retained permutations is the Gaussian resampling identity written so that the source and target coordinate permutations stay inside the formula. Its job on the way to the target is to let a convolution run on transforms without executing those permutations as sorts.

[Gaussian resampling](gaussian-resampling.md) replaces a transform of arbitrary length by transforms whose lengths are powers of two. Its usual implementation sorts each coordinate twice, once into the source order and once into the target order. On a fixed tape, each sort is paid for in full.

This identity rewrites [Gaussian resampling](gaussian-resampling.md) so that the two permutations stay in the formula instead of being run as sorts, and the formula is then computed directly. The identity keeps both permutations in the transform formula, so they need not be executed as separate sorts. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

Take four coordinates whose source order reverses them. Building that order by sorting moves every coordinate once, and undoing it moves them again. With the permutation kept symbolic, nothing moves. Because the permutations are explicit, a convolution can compose them, and a pair that cancels is never executed.
