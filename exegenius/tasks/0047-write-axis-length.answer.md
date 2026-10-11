An axis length is the number of positions along one coordinate axis of a multidimensional array, and it sets the length of the [Transform](transform.md) applied along that axis. A multidimensional transform is applied along each axis in turn.

For a two-dimensional array with axis lengths $\ell_1$ and $\ell_2$, the first axis has $\ell_1$ positions and the second has $\ell_2$. For example, a $2 \times 4$ array has $\ell_1 = 2$ and $\ell_2 = 4$: a length-2 transform runs down each of the 4 columns, and a length-4 transform runs along each of the 2 rows.

Each axis length is one factor in the [Tensor product](tensor-product.md) that gives the full transform. This is what lets the target identity be checked one axis at a time. The composite of two such products is the product of the composites on each axis, so if the one-dimensional identity for each axis holds, the tensor product of those identities is the identity for the whole array.

The starting point of the paper, a reduction of Harvey and van der Hoeven, uses transforms whose axis lengths are powers of two <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two</cite>.
