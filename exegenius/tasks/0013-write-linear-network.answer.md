A linear network is a fixed arrangement of wires and gates that transforms the values on the wires by fixed linear maps. The argument uses it to exchange two banks of values while restoring every auxiliary value, which is the building block for interchanging address chunks.

A *wire* carries one value. A *gate* is attached to some input wires and some output wires, and it writes to each output a fixed linear combination of the input values, with coefficients chosen in advance. A *bank* is a group of values held on the wires of one side of an exchange, and an *auxiliary value* is a value held on an extra wire that takes no part in the exchange and starts at a known value, such as zero. A network restores its auxiliary values if they hold their starting values again when it finishes.

Because the wires and coefficients are fixed, the network performs the same computation on every input. It has no data-dependent branching, and it moves no data as a tape machine does.

Example. Let $a$ be the value of the first bank and $b$ the value of the second, each on one wire. A gate that outputs $b$ on the first wire and $a$ on the second exchanges the banks. In matrix form the gate is
$$\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}b\\a\end{pmatrix}.$$
This map is invertible, since applying it twice returns $(a,b)$, so no value is lost. Prescribed signs are handled the same way: a coefficient $-1$ on one output negates the value it carries.

In the sources, each procedure is a fixed linear network of this kind. <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.</cite>
