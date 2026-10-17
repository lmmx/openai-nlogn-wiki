The established multiplier is the earlier Harvey–van der Hoeven algorithm, which multiplies two integers in $O(N\log N)$ time, where $N$ is the number of bits in each of the two integers being multiplied; the new algorithm uses it as a black-box subroutine for the large integer products it cannot avoid.

The multiplier runs in the [Fixed finite-tape machine model](machine-model.md): a Turing machine with a fixed alphabet and a fixed number of one-dimensional tapes. This is the same model as the main result, so a call costs exactly its $O(N\log N)$ steps, with no change of machine to account for. The paper takes the bound $O(N\log N)$ for integer products of this kind from Harvey and van der Hoeven <cite data-source="paper">We use the established $O(N\log N)$ integer multiplier of</cite>, and we take it as given: its proof is in their paper and is not reproduced here.

The bound is the one conjectured optimal by Schönhage and Strassen, which is why this multiplier is the benchmark the main result improves on.

## How it is used

The multiplier is not the source of the saving. The new algorithm reduces its Fourier transforms to polynomial products over $\mathbb C[y]/(y^r+1)$. Each such product is turned into a few ordinary integer products by [Signed packing](signed-packing.md), and those integer products are handed to the established multiplier. The packed integers are short, so the $O(N\log N)$ price is paid only on small records, and the saving comes from the transforms around them.

A call is a plain subroutine call. Calls to the multiplier are ordinary subroutine calls <cite data-source="paper">Calls to the established $O(n\log n)$ multiplier are ordinary subroutine</cite>, and they do not invoke the improved theorem recursively. The new algorithm therefore never calls itself on smaller inputs, so no recurrence is needed for it, and the running time of each call is charged as a separate term in the total cost.
