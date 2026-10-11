Coprime integers are integers with no common factor greater than 1; the argument needs them because the transform lengths for an exact integer product must be pairwise coprime. Two integers are coprime when their greatest common divisor, the largest integer dividing both, is 1. A family of integers is pairwise coprime when every two of its members are coprime.

Exact integer multiplication needs pairwise coprime transform lengths. <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, whereas powers of two need not be.

For example, $\gcd(4,9)=1$, since $4=2^2$ and $9=3^2$ share no prime factor, so 4 and 9 are coprime. By contrast $\gcd(4,6)=2$, so 4 and 6 are not. The family 4, 9, 25 is pairwise coprime. The family 4, 6, 9 is not, because 4 and 6 share the factor 2 and 6 and 9 share the factor 3.

Coprimality is also the hypothesis of the Chinese remainder theorem, which says that integers modulo a product of pairwise coprime lengths correspond one-to-one to tuples of remainders, one remainder for each length. Coprime integers enable the splitting of one [cyclic convolution](cyclic-convolution.md) into a multidimensional one over the same lengths.
