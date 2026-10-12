A linear network is a fixed wiring diagram of gates that transforms stored values by linear operations, and it is the device the paper uses to rearrange data inside an array without losing any of it. Its wires carry a *bank* of values, meaning one value per wire, and each vertex carries an invertible linear operator called its frame.

The network is fixed in two senses: its wiring does not depend on the data, and each wire has a fixed place in it, which the paper calls its role <cite data-source="paper">A wire’s fixed place in the network is called its role.</cite>. Each procedure in the paper uses its own fixed linear network, which exchanges two banks of values and restores every auxiliary value, with prescribed signs <cite data-source="paper">exchanges two banks of values, with prescribed signs, and restores every auxiliary value</cite>. The auxiliary wires are scratch space. They may hold arbitrary values during the computation, but they end with the values they started with.

Because every gate is linear and every frame is invertible, the whole network is a linear map on the values, given by a square invertible matrix acting on the stacked banks. An invertible map can be undone, which is why scratch values can be cancelled rather than destroyed.

The smallest case shows the exchange. Take two banks of one value each, with a network whose only gate swaps them. Its matrix is

$$
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
$$

which sends the pair of values to the same pair in reversed order.

The network is applied to whole arrays, not single values. Rows of the array are distributed among the roles, and a scalar gate is applied pointwise to matching addresses on the roles it touches, so one operator acts identically on every address. A frame is the invertible operator at one vertex of that network.
