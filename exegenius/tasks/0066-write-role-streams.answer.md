A role stream is the share of an array's rows that one role of a fixed network carries, obtained by dealing the rows out cyclically. The [Fast interchange of address chunks](tape-interchange.md) step relies on it.

A row is the complete ordered suffix of the active address fields (the address fields that the current procedure exchanges), taken at a fixed prefix and row index $i$, its position among the rows that share that prefix, counted from 0.

Let $W$ denote the number of roles, that is, the number of fixed wire places in the network. For each prefix, the row count is padded to a multiple of $W$, and the rows are then dealt cyclically: row $i$ goes to role $i \bmod W$. Take $W = 4$ and six rows. Padding adds two rows to make eight, so role 0 receives rows 0 and 4, role 1 receives rows 1 and 5, and so on.

Role streams are carried by the wires of a [Linear network](linear-network.md): each role is one wire place of it. Let $V$ denote the node volume after padding, the number of bits the node holds once its rows are padded.

For a prefix whose padded row count is $R$, a multiple of $W$, each role receives exactly $R/W$ rows, since the cyclic deal hands one row to each role in turn. Every row of a prefix has the same length, because all rows take the same active address fields. So all role streams have the same local address set, the addresses that the bits of a role stream's rows cover. Each role stream therefore holds $V/W$ bits of the node <cite data-source="paper">each contains $V/W$ bits</cite>.

A scalar gate, an operation on single values, is applied pointwise to the values at matching addresses of the roles it touches.
