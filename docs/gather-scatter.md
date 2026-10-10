# Gather and scatter operations

Gather and scatter are the operations, on the wires of a [linear network](linear-network-frames.md), that build the coefficients of the subset-intersection construction. They work on three-element subsets of a ground set, and they are the reason the coefficients depend only on intersection sizes.

The paper describes their form as that of [linear index-code decoding](linear-index-coding-decoding.md). A low-rank linear summary of several values gives the wanted coordinate, plus contributions from neighbouring coordinates that are already known. Decoding subtracts those known contributions, leaving the wanted coordinate. Gather forms such a summary, and scatter places the result back on the wires.

The paper's sentence on the construction states the outcome: gather and scatter create coefficients depending on intersection size. So the coefficient that links two subsets is determined by how many elements the subsets share, which can be $0$, $1$, $2$, or $3$ for three-element subsets.

Auxiliary wires then cancel the coefficients that should not appear. Together with the [indicator vectors](indicator-vector.md) of the subsets, this fixes the coefficients of the network. The [subset-intersection construction](subspace-intersection-network.md) uses these operations to assign subspaces to the gates.

## Prerequisites

- [Linear networks with frames](linear-network-frames.md)
- [Linear index-code decoding](linear-index-coding-decoding.md)

## Used by

- [Subset-intersection subspace construction](subspace-intersection-network.md)

## Sources

> gather and scatter create coefficients depending on intersection size
>
> — Integer multiplication below n log n (OpenAI, 2026)
