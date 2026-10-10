# exegenius task 0042-audit-bluestein-chirp-identity

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
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Subset-intersection subspace construction (also: nested subspaces)
- Recursive rank saving (also: power saving)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Address-field interchange](address-interchange.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Coefficient phase twist](phase-twist.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Page to audit

````markdown
# Bluestein chirp identity

Bluestein's chirp identity rewrites a [discrete Fourier transform](discrete-fourier-transform.md) as a convolution. It is the step that turns the middle transform in the paper's algorithm into a [cyclic convolution](cyclic-convolution.md).

Let $\omega = \zeta^2$ be a root of unity, with $\zeta$ itself a root of unity of twice the order. The DFT entry $\omega^{jk}$ can be split using the identity

$$2jk = j^2 + k^2 - (k - j)^2.$$

So $\zeta^{2jk} = \zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(k-j)^2}$. The factors $\zeta^{j^2}$ and $\zeta^{-(k-j)^2}$ are the chirp: a quadratic-phase sequence whose phases grow with the square of the index. Substituting into the DFT gives

$$\hat a_k = \zeta^{k^2} \sum_{j} \bigl(a_j \zeta^{j^2}\bigr)\, \zeta^{-(k-j)^2}.$$

The sum is a convolution of the sequence $u_j = a_j \zeta^{j^2}$ with the fixed sequence $v_m = \zeta^{-m^2}$. The output is then multiplied by $\zeta^{k^2}$.

For a small check, take $N = 2$, $\omega = -1$, and $\zeta = i$. The identity gives $\hat a_0 = a_0 + a_1$ and $\hat a_1 = i\,(a_0 \cdot i^{0} \cdot i^{-1} + a_1 \cdot i^{1} \cdot i^{0}) = i(-i\,a_0 + i\,a_1) = a_0 - a_1$, which is the DFT of $(a_0, a_1)$.

The paper applies the identity to a middle transform with its target permutation included. This yields a normalized cyclic convolution on power-of-two axes, which is then handled by the [phase twist](phase-twist.md) and the polynomial-ring convolution. The identity is applied after the [Gaussian resampling](gaussian-resampling.md) step, which reduces the transform to the form it needs.
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

Write the answer to `exegenius/tasks/0042-audit-bluestein-chirp-identity.answer.json`, then run `exegenius submit 0042-audit-bluestein-chirp-identity` in the project directory. If submit rejects the answer, fix the answer file and submit again.
