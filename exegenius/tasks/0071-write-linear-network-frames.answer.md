A linear network is a fixed wiring diagram of gates that transforms stored values by linear operations. It is the device the paper uses to rearrange data inside an array without losing any of it. Each gate combines the values on its input wires linearly. The wires carry *banks* of values, one value per wire, and each vertex (a node of the diagram) carries an invertible linear operator called its *frame*.

The network is fixed in two senses: its wiring does not depend on the data, and each wire has a fixed place in it, which the paper calls its role <cite data-source="paper">A wire’s fixed place in the network is called its role.</cite>. Each procedure in the paper uses its own fixed linear network, which exchanges two banks of values and restores every auxiliary value. The auxiliary wires are scratch space: they may hold arbitrary values during the computation, but they end with the values they started with.

Because every gate is linear, composing the gates gives a linear map from the input values to the output values. The input and output have the same wires, so this map is a square matrix acting on the stacked banks (all values listed as one column).

The smallest case shows the exchange. Take two banks of one value each, with a network whose only gate swaps them. Its matrix is

$$
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
$$

which sends the pair of values to the same pair in reversed order.

The network acts on whole arrays. An *address* is the binary label of one entry of the array. A *scalar gate* applies one fixed linear rule to the values at each address on the wires it touches, the same rule at every address. Rows of the array are distributed among the roles, so one operator acts identically on every address.
