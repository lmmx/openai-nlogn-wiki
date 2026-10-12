A simultaneous butterfly layer applies a two-point map to several selected address bits at once, computing the tensor product exactly in one pass instead of one axis at a time. It is the step that makes the transforms of the multiplication cheap.

On the layouts of the multiplication algorithm, the same bit position is selected in each of at most $d$ equal-width address chunks. The layer acts on $D$ selected chunks, where $1 \le D \le d$. It acts coefficientwise on the polynomial record at each address and preserves all other address fields. Here $V$ is the logical bit volume of the stored array.

The two-point map is $H_0(u,v) = ((u+v)/2, (u-v)/2)$. The map $H_0$ is the normalized [discrete Fourier transform](discrete-fourier-transform.md) of length 2, so the layer is a tensor product of such transforms. For $D=2$, the four values $x_{00}, x_{01}, x_{10}, x_{11}$ indexed by the two selected bits become four sums and differences, each divided by 4; the value at index 00 becomes $(x_{00}+x_{01}+x_{10}+x_{11})/4$.

The method has two steps. The complex two-point kernel $C$ is a $2\times 2$ complex matrix. The tensor product of $C$ is realized by a [complex phase network](complex-phase-network.md) with dyadic frame changes. The layer keeps its intermediate values exact in [Gaussian dyadics](gaussian-dyadics.md). Diagonal phase operations and a dyadic scale then turn the completed complex layer into the normalized $H_0$ layer.

The frame changes between groups of selected bits are binary changes of basis. The layer moves its address chunks by [address-field interchange](address-interchange.md), which realizes these changes of basis.

Why split the work this way: applying the factors separately would need $D$ whole-array passes <cite data-source="paper">separate butterfly factors would require D whole-array passes</cite>. The phase frames instead write the tensor product on smaller groups of selected bits, and the network's wire roles split each complete row among those groups. Each recursive call then handles a smaller volume of the array.

Here $\lambda'$ is a fixed exponent below 1, so the cost grows more slowly than $d$ full passes over the array. The layer costs $O(V d^{\lambda'})$ <cite data-source="paper">the cost is O(V dλ ) for a fixed λ′ < 1</cite>.
