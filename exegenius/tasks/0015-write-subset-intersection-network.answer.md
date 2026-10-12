A subset-intersection network is a fixed linear network on the three-element subsets of a ground set. It exchanges two banks of scalars while restoring every scratch wire, that is, every auxiliary wire ends with the value it started with. It is the exchange step that the [address-field interchange](address-interchange.md) applies recursively.

The network is based on [linear networks and frames](linear-network-frames.md). Its wires carry scalars, and its gates combine them according to the size of the intersection of their subsets. Take the ground set $\{1,2,3,4\}$. Two distinct three-element subsets of it always meet in exactly two elements, so a gate that depends only on intersection size treats every pair of distinct subsets alike, and treats a subset paired with itself, which meets in three elements, differently.

Gates are the vertices that combine values, and terminals are the endpoints where the two banks attach. The network attaches [subspace labels](subspace-labels.md) to its gates and terminals. Here $m$ is the dimension of the fixed space from which the labels are drawn.

Gather and scatter create coefficients that depend on intersection size, and auxiliary wires cancel the unwanted ones. <cite data-source="paper">The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.</cite> The point is that such coefficients, with the rest cancelled, give an exchange whose subspace ranks can be controlled.

Here $s$ is the total number of smaller calls made by one call. Here $W$ is the factor by which the stream volume shrinks, so each smaller call works on a stream of $1/W$ of the volume.

The inequality $s<Wm$ is the property the rest of the argument needs. <cite data-source="paper">The decisive property is that the total number s of smaller calls satisfies s < W m.</cite>
