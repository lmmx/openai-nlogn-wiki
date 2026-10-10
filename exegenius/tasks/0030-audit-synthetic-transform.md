# exegenius task 0030-audit-synthetic-transform

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
- Exact integer multiplication (also: n-bit product)
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)

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
# Synthetic polynomial transform

A synthetic polynomial transform is a discrete Fourier-type transform whose roots of unity are powers of $y$ in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). Multiplying by $y^k$ only shifts coefficients and changes some signs, so each stage of the transform is made of address rearrangements, signed shifts, and two-point butterfly operations.

The paper credits this construction to Nussbaumer and to Quandalle and Nussbaumer. Its role here is to evaluate the transforms of the convolution on the axes that carry a polynomial coordinate.

Take $r = 4$ and a coefficient list $(a_0, a_1, a_2, a_3)$. Multiplying by $y$ gives $(-a_3, a_0, a_1, a_2)$, as in the ring page. Multiplying by $y^2$ applies this twice, giving $(-a_2, -a_3, a_0, a_1)$. Both are a shift followed by sign changes, which costs no multiplications.

A butterfly on two records $u$ and $v$ has the form $(u + v, u - v)$, possibly with a shift applied to one input first. Combining shifts and butterflies in layers gives a transform of polynomial length, and the same layers run in reverse to invert it.

In the paper, the transform is computed in simultaneous layers on a tape. The cost of each layer is governed by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) procedure, which is the reason these transforms can be applied on a fixed number of tapes.
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

Write the answer to `exegenius/tasks/0030-audit-synthetic-transform.answer.json`, then run `exegenius submit 0030-audit-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer file and submit again.
