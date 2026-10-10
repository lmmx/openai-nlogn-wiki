# exegenius task 0187-audit-indicator-vector

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
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition, CRT)
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
- Multiplication algorithm (also: exact product algorithm)
- Bit complexity (also: bit-complexity bound)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction, pairing formulas)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
- Linear contraction (also: contraction)
- Normalized cost (also: costs after division by V, normalized recursive cost)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)
- Linear index-code decoding (also: linear index-coding decoding)
- Middle transform (also: middle factor)
- Complex modulus (norm of a coefficient) (also: norm of a complex number, absolute value, norm)
- Rational bilinear form
- Source and target permutations (also: target permutation)
- Transform identity

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
- [Rational bilinear form](rational-bilinear-form.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Linear index-code decoding](linear-index-coding-decoding.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity](transform-identity.md)
- [Source and target permutations](target-permutation.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Middle transform](middle-transform.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Coefficient phase twist](phase-twist.md)
- [Complex modulus (norm of a coefficient)](complex-modulus.md)
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
# Indicator vector

Let $U$ be a finite set, often called the ground set. For a subset $A \subseteq U$, its indicator vector is the vector $\mathbf{1}_A$ indexed by the elements of $U$, with entry $1$ at each element of $A$ and $0$ at each element not in $A$.

For example, if $U = \{1, 2, 3, 4\}$ and $A = \{2, 4\}$, then $\mathbf{1}_A = (0, 1, 0, 1)$. For two subsets $A$ and $B$, the dot product of their indicator vectors is $\mathbf{1}_A \cdot \mathbf{1}_B = |A \cap B|$, the number of common elements. Take $B = \{4\}$ as an example: $\mathbf{1}_A \cdot \mathbf{1}_B = 0 \cdot 0 + 1 \cdot 0 + 0 \cdot 0 + 1 \cdot 1 = 1$, which is $|A \cap B| = |\{4\}| = 1$.

This identity is why indicator vectors are useful for intersections. Counting common elements becomes an inner product, which is a linear-algebra computation.

The paper uses indicator vectors of three-element subsets of a ground set. It notes that orthogonality of these vectors is what permits the subspace assignments of the [subset-intersection construction](subspace-intersection-network.md).
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

Write the answer to `exegenius/tasks/0187-audit-indicator-vector.answer.json`, then run `exegenius submit 0187-audit-indicator-vector` in the project directory. If submit rejects the answer, fix the answer file and submit again.
