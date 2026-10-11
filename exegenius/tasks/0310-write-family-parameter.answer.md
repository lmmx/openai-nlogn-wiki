A family parameter is the integer that picks out one member of a family of constructions and fixes how large that member is. The rank-saving recursion depends on this idea: it bounds a count of smaller calls in terms of the sizes that such a parameter sets, so the sizes of the members must be controlled by a single index.

Let $\tau$ be the family parameter: a nonnegative integer that indexes the members of a family. Let $C_\tau$ be the member of the family built with parameter $\tau$. A family is a collection of constructions, one for each allowed value of $\tau$. The size of a construction is the number of entries it takes as input, and the family parameter is the quantity that controls it.

For example, let $C_\tau$ be the cyclic convolution of two sequences of length $2^\tau$. Then $\tau = 3$ gives sequences of length $8$, and $\tau = 4$ gives sequences of length $16$. Each increase of $\tau$ by one doubles the size.

A family is used by choosing the parameter from the input. For an input of length $n \ge 1$, take $\tau = \lceil \log_2 n \rceil$. Then $2^\tau \ge n$, and $2^\tau < 2n$ because $\tau < \log_2 n + 1$. So $C_\tau$ has size at least $n$ and less than $2n$: the parameter fixes the size to within a factor of two.
