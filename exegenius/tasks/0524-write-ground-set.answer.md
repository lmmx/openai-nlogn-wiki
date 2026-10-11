A *ground set* is a finite set from which the subsets under consideration are chosen. It fixes one universe of elements, so every subset is built from the same elements and all subsets can be compared against one common set.

The [subset-intersection network](subset-intersection-network.md) is a linear network on the three-element subsets of a ground set. A ground set indexes the wires and gates of a [network of wires and gates](linear-network-frames.md) through its three-element subsets.

Here $h$ is the number of elements of the ground set. Write $[h]=\{1,2,\dots,h\}$ for that set. A subset is any collection of some of these elements. Write $\mathcal{T}$ for the set of three-element subsets of $[h]$.

Take $h=4$. Then $[4]=\{1,2,3,4\}$ and $\mathcal{T}$ has four members, $\{1,2,3\}$, $\{1,2,4\}$, $\{1,3,4\}$ and $\{2,3,4\}$. Each member is a set and an element of $\mathcal{T}$, not of $[4]$. The intersection of two sets is the set of elements they have in common, so $\{1,2,3\}\cap\{1,2,4\}=\{1,2\}$. Two different members can share one or two elements. With $h=4$ they always share two, since each omits a different one of the four elements. Sharing one element needs $h\ge 5$: in $[5]$, $\{1,2,3\}\cap\{3,4,5\}=\{3\}$.
