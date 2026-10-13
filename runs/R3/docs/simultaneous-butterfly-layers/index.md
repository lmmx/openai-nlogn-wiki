# Simultaneous butterfly layers

A butterfly layer acts on many address bits at once, and the cost must be kept below a linear multiple of the data volume. [Fixed-point precision](../fixed-point-precision.md "Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.") guarantees that rounding recovers exact coefficients despite the arithmetic. The [fast butterfly layers](../fast-butterfly-layers.md "Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.") combine this with the interchange from the previous part.

## Pages

1. [Fixed-point precision and exact recovery](../fixed-point-precision.md "Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.") — Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
2. [Fast simultaneous butterfly layers](../fast-butterfly-layers.md "Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.") — Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Fixed-point precision and exact recovery"]
  click n0 href "../fixed-point-precision/" "Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product."
  n1["Fast simultaneous butterfly layers"]
  click n1 href "../fast-butterfly-layers/" "Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end."
  n0 --> n1
```
