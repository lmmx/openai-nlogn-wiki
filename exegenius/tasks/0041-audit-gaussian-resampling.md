# exegenius task 0041-audit-gaussian-resampling

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
# Gaussian resampling

Gaussian resampling is the step that replaces a [discrete Fourier transform](discrete-fourier-transform.md) of a length that is not a power of two by a transform whose axes all have power-of-two lengths. The paper adapts the identity of Harvey and van der Hoeven.

The idea is to move values between two grids of different sizes. Let $s < t$ be coprime integers. A length-$s$ grid and a length-$t$ grid are related by two coordinate permutations. The paper defines them as $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$, where indices are taken modulo the length. When $\gcd(s,t) = 1$, the map $j \mapsto tj \bmod s$ is a bijection.

For a small case, take $s = 3$ and $t = 4$. The map $j \mapsto 4j \bmod 3$ sends $0, 1, 2$ to $0, 1, 2$, so it is a permutation. The gcd condition is what makes this hold in general.

The resampling itself uses linear contractions $A : \mathbb{C}^s \to \mathbb{C}^t$ and $B_0 : \mathbb{C}^t \to \mathbb{C}^s$, which approximate a Gaussian-weighted interpolation. The Gaussian window makes the error small when $t/s - 1$ is large compared with the precision parameter, and this is what allows an approximate resampling with a fixed number of bits of precision.

The payoff is that each source Fourier transform can be expressed through a transform whose axes have power-of-two lengths, together with these resampling maps. The remaining middle transform is then turned into a convolution by the [Bluestein chirp identity](bluestein-chirp-identity.md).

The paper proves that the two permutations need not be executed as separate full sorts. They can be left in the transform identity and cancelled later.
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

Write the answer to `exegenius/tasks/0041-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0041-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer file and submit again.
