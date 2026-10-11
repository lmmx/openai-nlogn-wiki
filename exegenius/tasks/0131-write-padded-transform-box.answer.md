The padded transform box is the full array on which a transform over several axes is computed, after every axis has been padded to a chosen length. The [transform identity](transform-identity.md) works inside this one fixed array, so its coordinate permutations rearrange entries of the box rather than sorting the data into a new array.

An axis is one coordinate direction of the data grid. Let $d$ be the number of axes, the count of coordinate directions along which the data is laid out. For each axis $\nu$, with $\nu$ running from $1$ to $d$, let $w_\nu$ be the valid length of that axis, the number of data entries along it, and let $M_\nu \ge w_\nu$ be its padded length. Padding an axis means appending zero entries until it has length $M_\nu$.

The box has $Q = M_1 M_2 \cdots M_d$ entries, the number of entries of the full array. An address $\mathbf{e} = (e_1,\dots,e_d)$ with $0 \le e_\nu < M_\nu$ for every $\nu$ names one entry of the box. The valid region is the set of addresses with $e_\nu < w_\nu$ for every $\nu$. Entries at addresses outside the valid region are zero, so the box holds the data in the valid region and zeros everywhere else.

Each step that moves data between valid and invalid addresses keeps the box at its full size: <cite data-source="paper">The box therefore keeps its full size</cite>. The entry count $Q$ therefore does not change during such a step.

Take $d = 2$, $M_1 = 8$, $w_1 = 5$, $M_2 = 4$ and $w_2 = 3$. The box has $Q = 32$ entries. The valid region is the $15$ addresses with $e_1 < 5$ and $e_2 < 3$, and the remaining $17$ entries are zero.

The padded transform box is the array of a [multidimensional transform](multidimensional-transform.md) over its $d$ padded axes.
