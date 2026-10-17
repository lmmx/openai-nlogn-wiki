Elementary stream operations are linear-time scans of an array stored on tape in lexicographic order; they are the data-movement primitives that the later procedures for interchanging address fields are assembled from.

Throughout, $V$ is the volume of an array, the number of radix-$q$ digits it stores, and $q\ge 2$ is the radix, the number of values one digit can take.

All four operations below run on the [Fixed finite-tape machine model](machine-model.md), where each head moves at most one cell per step, so one pass over the array costs time proportional to $V$. Passes must be this cheap because a scan at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$ <cite data-source="paper">Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$</cite>, so only few linear passes are affordable.

For a fixed radix, each of the following takes $O(V)$ steps on a fixed number of one-dimensional tapes <cite data-source="paper">Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes</cite>:

1. Permuting the pair of values at two chosen digit positions, adjacent or not.
2. Moving one chosen digit to another position, keeping the order of the positions in between.
3. Splitting on one chosen digit, applying a fixed pointwise map to the aligned streams, and merging them back.
4. For an array on $[P]\times[R]\times[B]$ (a prefix of $P$ values, $R$ rows, $B$ entries per row), dealing whole rows cyclically into $W$ streams, where $W$ is the fixed number of streams, and, when $W$ divides $R$, merging the streams in any fixed order of the row classes.

The bounds include setting up counters and returning the work tapes to their initial state, and the constants depend on the radix, the pointwise map and $W$ <cite data-source="paper">The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes.</cite>

The idea behind splitting is a stable partition. A head scanning the array tracks its position with a counter and copies each entry onto the tape belonging to the value of the chosen digit, preserving order within each tape. Reading the $q$ tapes one after another lists the entries grouped by that digit, with the remaining digits still in their original order, which is exactly that digit moved to the front. For example, with digits $(a,b,c)$ and $b$ chosen, the stream for each value $j$ of $b$ holds the entries $(a,j,c)$ in their original order, and concatenating the streams gives the order $(j,a,c)$.
