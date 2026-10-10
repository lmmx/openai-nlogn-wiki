# Record

A record is a fixed-width block of stored data that the procedures treat as one unit. In the paper's numerical procedures, a record is a polynomial whose coefficients are complex fixed-point numbers. The butterfly procedure makes this concrete: its map $H_0(u, v) = \left(\frac{u+v}{2}, \frac{u-v}{2}\right)$ acts on each coefficient of the records $u$ and $v$, so one application handles every coefficient of a pair of records.

Records also set the cost. The paper writes the width of a record of length $r$ with $p$-bit coefficients as $O(rp)$ bits. The [established multiplier](established-multiplier.md) is applied to records of this kind when the paper uses it as a subroutine, and the bound $O(rp)$ is the length of each such call.

A record is a unit of data, not a unit of arithmetic. Operations on records, such as applying the butterfly map to a pair of records, cost time in proportion to the total number of stored bits they touch.

## Prerequisites

- Polynomials (assumed known)

## Used by

- [Established O(n log n) multiplier](established-multiplier.md)

## Sources

> Each record is a polynomial with complex fixed-point coefficients
>
> — Integer multiplication below n log n (OpenAI, 2026)
