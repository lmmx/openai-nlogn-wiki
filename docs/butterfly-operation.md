# Butterfly operation

!!! info "Before this page"

    Butterfly operation *is a scaled length-2 case of* [Discrete Fourier transform](fourier-transform.md "The butterfly is a scaled length-2 case of the discrete Fourier transform."). Assumed known: Complex numbers.

!!! abstract "Where this fits"

    - Relied on to show: A simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. ([Simultaneous butterfly layer](simultaneous-butterfly-layer.md "A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer."))

The butterfly operation is the two-point map that serves as the basic step of a fast transform: a transform on many values is carried out in layers, and each layer applies the butterfly to pairs of values.

Let $u$ and $v$ be two input values, and let $H_0$ denote the butterfly map, so that $H_0(u,v)=\left(\frac{u+v}{2},\frac{u-v}{2}\right)$. On column vectors this is multiplication by the matrix
$$H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$
For example, $H_0(3,1)=(2,1)$.

The butterfly is not its own inverse. Squaring the matrix gives $H_0^2=\frac14\begin{pmatrix}2&0\\0&2\end{pmatrix}=\frac12 I$, where $I$ denotes the $2\times 2$ identity matrix. So applying the butterfly twice returns the pair divided by two: $H_0(H_0(u,v))=\left(\frac u2,\frac v2\right)$. Check with the example: $H_0(2,1)=\left(\frac32,\frac12\right)$, which is $\frac12(3,1)$.

The butterfly is a scaled length-2 case of the [discrete Fourier transform](fourier-transform.md "The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity."). The length-2 transform uses the [root of unity](glossary.md#roots-of-unity "A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1.") $-1$ and returns the unscaled sums $u+v$ and $u-v$; the butterfly divides both by $2$. The factor $\frac12$ keeps magnitudes from growing across layers: $\left|\frac{u\pm v}{2}\right|\le\max(|u|,|v|)$, since $|u\pm v|\le|u|+|v|\le 2\max(|u|,|v|)$.

The paper's transform calculation uses address rearrangements (moving stored values to other addresses), signed shifts (multiplying a value by a signed power of two), and the butterfly steps<cite class="exegenius-ref" data-source="paper" data-locator="§1.1 The two tape operations" data-quote="two-point butterfly operations" title="two-point butterfly operations"> (see §1.1 The two tape operations)</cite>.

Each butterfly touches only two values, so the cost of a level is set by how many pairs it processes. A [simultaneous butterfly layer](simultaneous-butterfly-layer.md "A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.") applies the same butterfly to one address bit of every stored record at once.

## Connections

```mermaid
flowchart LR
  n0["Discrete Fourier transform"]
  click n0 href "../fourier-transform/" "The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity."
  n1["Butterfly operation"]
  class n1 current
  n2["Simultaneous butterfly layer"]
  click n2 href "../simultaneous-butterfly-layer/" "A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer."
  n0 --> n1
  n1 --> n2
  classDef current stroke-width:3px,font-weight:bold
```

Used by:

- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md "A simultaneous butterfly layer applies the butterfly operation to one selected address bit of every record at once.") *applies* Butterfly operation

??? quote "From the sources"

    > two-point butterfly operations
    >
    > — [Integer multiplication below n log n (OpenAI, 2026)](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/Integer-multiplication-below-n-log-n-September-23-2026)
