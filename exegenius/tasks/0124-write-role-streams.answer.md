A role stream is the share of an array's rows that one role of a fixed network carries, obtained by dealing the rows out cyclically. The [Fast interchange of address chunks](tape-interchange.md) step needs each wire to hold an equal share of the data.

A prefix is the fixed leading part of an array's address. A row is the complete ordered suffix of the active address fields (the fields that the procedure exchanges), taken at a fixed prefix and row index $i$, its position among the rows that share that prefix, counted from 0.

Let $W$ denote the number of roles, that is, the number of fixed wire places in the network. For each prefix, let $R$ denote the padded row count: the row count padded up to a multiple of $W$. Row $i$ goes to role $i \bmod W$. For example, with $W = 4$ and six rows, padding gives eight rows, and role 0 receives rows 0 and 4.

Role streams are carried by the wires of a [Linear network](linear-network.md): each role is one wire place of it.

Let $V$ denote the node volume after padding, the number of bits the node holds once its rows are padded. This is the sum over all prefixes of $R$ times the bit length of a row.

Fix one prefix with padded row count $R$. Since $R$ is a multiple of $W$, each role receives exactly $R/W$ rows of this prefix. All rows of a prefix have the same bit length, since they take the same active fields. So each role gets $1/W$ of the prefix's bits, and summing over prefixes gives $V/W$ bits per role. Every role stream also covers the same local address set. Each role stream therefore holds $V/W$ bits of the node. <cite data-source="paper">each contains $V/W$ bits</cite>

A scalar gate, an operation on single values, is applied pointwise: it acts on the values at matching local addresses of the roles it touches.
