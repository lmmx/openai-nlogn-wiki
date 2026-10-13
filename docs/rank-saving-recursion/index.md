# Rank-saving recursion

This part gives the combinatorial core. [Subset-intersection networks](../subset-network.md "A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].") realise the scalar exchange of two banks by intersection sizes, and [nested subspace labels](../subspace-labels.md "Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.") bound the work on each edge by dimension drops. The [rank-saving recursion](../recursive-saving.md "A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.") turns these bounds into a cost that grows by less than $m$ when the parameter grows by $m$, which is the source of the saving.

## Pages

1. [Subset-intersection finite network](../subset-network.md "A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].") — A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].
2. [Nested subspace labels](../subspace-labels.md "Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.") — Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.
3. [Rank-saving recursion](../recursive-saving.md "A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.") — A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Subset-intersection finite network"]
  click n0 href "../subset-network/" "A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2]."
  n1["Nested subspace labels"]
  click n1 href "../subspace-labels/" "Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge."
  n2["Rank-saving recursion"]
  click n2 href "../recursive-saving/" "A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume."
  n0 --> n1
  n1 --> n2
```
