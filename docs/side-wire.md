# Side wire

A side wire is a wire of the subset-intersection network that joins two neighbouring physical triples. A physical triple is a group of three wires attached to one three-element subset, and a side wire carries values between the triples of two neighbouring subsets. Side wires belong to the [linear network](linear-network-frames.md) as edges, alongside the central wires and the data wires.

The paper counts side wires for each invocation of the construction. It states that the count is $vz$ rather than $vz/2$, because ordered pairs of neighbouring triples must be counted, and each pair gets its own side wire.

Along a side wire the gate labels change in a controlled way. If the wire joins triples with indicator vectors $t_X$ and $t_Y$, the common component of the label grows, while the remaining component passes through a residual that is orthogonal to $t_X$. The paper tracks this residual edge by edge.

Side wires are scratch wires. Like the other auxiliary wires, their initial values may be arbitrary, and the construction makes the final result independent of them. Side wires are the part of the network that the [linear index-code decoding](linear-index-coding-decoding.md) subtraction uses to remove known contributions.

## Prerequisites

- [Linear networks with frames](linear-network-frames.md)

## Used by

- [Linear index-code decoding](linear-index-coding-decoding.md)

## Sources

> On a side wire joining neighboring physical triples
>
> — Integer multiplication below n log n (OpenAI, 2026)
