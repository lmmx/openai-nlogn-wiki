A linear network is a fixed arrangement of wires and gates that transforms the values on the wires by fixed linear maps. The argument uses it to exchange two banks of values while restoring every auxiliary value. Interchanging address chunks, that is, two equal-width groups of address bits of an array, is built from such exchanges, so the exchange is the piece to understand first.

A *wire* carries one value. A *gate* reads some input wires and writes to each output wire a fixed linear combination of the input values, with coefficients chosen in advance. A *bank* is a group of values held on one side of an exchange. An *auxiliary value* is a value on an extra wire that takes no part in the exchange and starts at a known value, such as zero. A network *restores* its auxiliary values if they hold their starting values again when it finishes.

Because the wires and coefficients are fixed, the network performs the same computation on every input. It has no data-dependent branching, and it moves no data as a tape machine does.

Example. Let $x$ be the value of the first bank and $y$ the value of the second, each on one wire. A gate that outputs $y$ on the first wire and $x$ on the second exchanges the banks:
$$\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}y\\x\end{pmatrix}.$$
Applying this map twice returns $(x,y)$, so no value is lost.

The exchanges in the sources also use coefficients $\pm 1$. The gate $(x,y)\mapsto(y,-x)$, with matrix $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, is invertible: applying it twice gives $(x,y)\mapsto(-x,-y)$, and applying it four times returns the input. Its inverse $(x,y)\mapsto(-y,x)$ is again a gate with coefficients $\pm 1$, so a coefficient $-1$ never destroys a value.

In the sources, each procedure is a fixed linear network of this kind. <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.</cite>
