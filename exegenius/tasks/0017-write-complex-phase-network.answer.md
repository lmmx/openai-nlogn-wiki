A complex phase network is built on a [Subset-intersection network](subset-intersection-network.md), with a frame change on each edge. It carries the completed complex layer to the simultaneous $H_0$ layer, where $H_0$ is the two-point map applied to several selected address bits at once ([Simultaneous butterfly layer](simultaneous-butterfly-layer.md)).

Each frame change is a product of two-point kernels $aI+bX$, where $a$ and $b$ are the two scalars of the kernel, $I$ is the identity on two points, and $X$ is the swap of the two points. For $a=2$ and $b=1$, the kernel sends $(1,0)$ to $(2,1)$.

Each frame change takes its scalars from [Gaussian dyadics](gaussian-dyadics.md), so sums and products stay exact with no rounding. Exactness matters because the result is an exact multiplication, not an approximation.

Its cost is controlled by the inclusions of [Subspace labels](subspace-labels.md) on its wires.

Once the complex layer is computed, multiplying each entry by a unit complex number (a diagonal phase operation) and then by a dyadic scale gives the normalized $H_0$ layer.
