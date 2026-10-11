Axis length is the number of positions along one coordinate axis of a multidimensional array. A multidimensional transform is applied along each axis in turn, and the transform on each axis has that axis's length. This is what lets the target identity be checked one axis at a time, since each axis contributes its own one-dimensional identity.

For a two-dimensional array with axis lengths $\ell_1$ and $\ell_2$, the first axis has $\ell_1$ positions and the second has $\ell_2$. For example, a $2 \times 4$ array has $\ell_1 = 2$ and $\ell_2 = 4$: a length-2 transform runs down each of the 4 columns, and a length-4 transform runs along each of the 2 rows.

Each axis length is one factor in the tensor product that gives the full transform. The method of Harvey and van der Hoeven uses transforms whose axis lengths are powers of two <cite data-source="paper">axis lengths are powers of two</cite>.
