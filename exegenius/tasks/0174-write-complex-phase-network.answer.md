A complex phase network is built on a [Subset-intersection network](subset-intersection-network.md) with a frame change on each edge. It is the device that turns the completed complex layer into the simultaneous $H_0$ layer.

Each frame change is a product of two-point kernels, where $I$ is the identity on two points and $X$ is the map that swaps them. Each kernel is $\alpha I+\beta X$, where $\alpha$ is the first scalar of the kernel and $\beta$ is the second scalar. Acting on a pair $(u,v)$, the kernel sends it to $(\alpha u+\beta v,\ \beta u+\alpha v)$. For $\alpha=\frac{1+i}{2}$ and $\beta=\frac{1-i}{2}$, the kernel sends $(1,0)$ to $\left(\frac{1+i}{2},\frac{1-i}{2}\right)$.

Each frame change takes its scalars from [Gaussian dyadics](gaussian-dyadics.md), so every sum and product stays exact, with no rounding. Each wire is labelled by [Subspace labels](subspace-labels.md).

Applied to all selected address bits at once, the network is a [Tensor product](tensor-product.md) of one kernel per bit, evaluated on all addresses. This is the completed complex layer.

Here $H_0$ sends $u$ and $v$ to their halved sum and halved difference. For the kernel above, multiplying the second point by $i$ before and after the kernel gives $\frac{1+i}{2}$ times the map that sends $(u,v)$ to $(u+v,\,u-v)$. Scaling by $\beta=\frac{1-i}{2}$ cancels the factor $\frac{1+i}{2}$ and halves both outputs, since

$$\frac{1-i}{2}\,\frac{1+i}{2}=\frac{1}{2},$$

so the result is $H_0$ on two points. Multiplying by $i$ changes no magnitude, and each output of $H_0$ is at most the largest input in magnitude; this is what normalized means here.

Applying these operations to the completed complex layer gives the simultaneous $H_0$ layer, the map applied to several selected address bits at once ([Simultaneous butterfly layer](simultaneous-butterfly-layer.md)), <cite data-source="paper">after diagonal phase operations and a dyadic scale</cite>.
