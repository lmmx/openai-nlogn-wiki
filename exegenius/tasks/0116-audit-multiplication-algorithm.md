# exegenius task 0116-audit-multiplication-algorithm

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

A term, symbol or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term, symbol or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- symbol: notation used without being defined on the page.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed-tape machine)
- Exact integer multiplication (also: n-bit product)
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Cyclic convolution (also: convolution modulo x^S - 1)
- Radix-digit convolution (also: digit convolution)
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Bluestein chirp identity (also: chirp transform)
- Coefficient phase twist (also: twisted negacyclic convolution)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Precision and exact recovery (also: coefficient rounding)
- Parameter choice (also: size parameters)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
- Linear contraction (also: contraction)
- Normalized cost (also: costs after division by V, normalized recursive cost)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Record](record.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Row of an array](row-of-array.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Coefficient phase twist](phase-twist.md)
- [Disk-grid values](disk-grid-values.md)
- [Normalized cost](normalized-cost.md)
- [Linear convolution](linear-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Page to audit

````markdown
# Multiplication algorithm

The multiplication algorithm combines the earlier reductions into one procedure for exact integer multiplication. It splits each input into radix-$2^b$ digits, lays the coefficients on a padded power-of-two box, computes three transforms, multiplies them pointwise, and recovers the integer product by rounding and carries.

Let $q = \lceil n/b \rceil$ and $S$ be the padded length. The two inputs become polynomials of degree below $q$ in $2^b$, so their product has degree at most $2q - 2 < S$. Thus the [radix-digit convolution](radix-digit-convolution.md) is a cyclic convolution of length $S$ with no wraparound. The [parameter choice](parameter-choice.md) fixes $S$, $b$, and $p$.

The main steps, following the paper, are:

1. Apply the coefficient-address map $\Phi$ from the [Chinese-remainder address map](chinese-remainder-map.md) to the two source arrays $u$ and $v$. Their coefficients are exact $p$-bit [grid values](disk-grid-values.md).
2. Compute the forward source transforms $\hat u$ and $\hat v$. These use [Gaussian resampling](gaussian-resampling.md) together with the [Bluestein chirp identity](bluestein-chirp-identity.md), and each layer is a [synthetic transform](synthetic-transform.md) evaluated with [simultaneous butterfly layers](simultaneous-butterfly-layer.md). The coordinate layouts are changed by the [address-field interchange](address-interchange.md) procedure.
3. Multiply the complex coefficients of $\hat u$ and $\hat v$ pointwise, and truncate each part to $p$ fractional bits. Call the result $z$. The products of polynomial records in this step use [signed coefficient packing](signed-packing.md).
4. Compute the opposite-sign transform $\hat z^{+}$, and multiply its numerators by $S$. Call the result $w$. The [phase twist](phase-twist.md) is applied to the last coordinate in these transforms.
5. Multiply the numerators of $w$ by $2^{2b+4} S$, round each value to the nearest integer, and apply $\Phi^{-1}$ to restore the ordinary coefficient order.
6. Propagate radix-$2^{b}$ carries from low to high coefficients, and output exactly $2n$ bits, most significant first.

The two factors of $S$ undo two different normalizations. Without them, the transform identity gives $(u \ast v)/S^2$ as the exact counterpart after the three transforms. After the first scale the result is $(u \ast v)/S$, and the second scale gives $2^{2b+4}(u \ast v)$, whose inverse image under $\Phi$ is the integer coefficient convolution.

The permutations that appear in the transform identity are not executed as separate sorts. The paper shows that they cancel across the two forward transforms, their pointwise product, and the opposite-sign transform, so that the net effect is the identity. The [precision and exact recovery](precision-and-rounding.md) argument shows that the rounding in step 5 returns the true coefficients.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term or symbol, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "symbol",
          "description": "Notation used without being defined on the page.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every gap on the page; empty if the reader can follow all of it.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    }
  },
  "required": [
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0116-audit-multiplication-algorithm.answer.json`, then run `exegenius submit 0116-audit-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer file and submit again.
