# exegenius task 0036-audit-linear-network-frames

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
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
# Linear networks with frames

A linear network is a fixed directed graph whose nodes are sources, gates and sinks, which exchange banks of values along its edges. Each wire at a fixed place in the network is called a *role*. To run the network on a tape array, the array's rows are distributed cyclically among $W$ roles, so each role receives a stream of $V/W$ bits. A pointwise scalar gate is applied to matching addresses on the roles it touches.

The new idea is a *frame*. At each source, gate, or sink $v$ we choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. The stored array on that node is $D_v g$, where $g$ is the logical array. All edges of one gate use the same frame.

Along an edge from $u$ to $v$, the stored array changes from $D_u g$ to $D_v g$, so the change of representation is $D_v D_u^{-1}$. For example, if $D_u = 2$ and $D_v = 1$ on scalar arrays, the edge multiplies the stored value by $1/2$. Along a route through the network, these changes cancel in pairs, so a route from input role $w$ to output role $\rho(w)$ applies only $D_{\text{sink}}\, D_{\text{source}}^{-1}$.

The frames also commute with pointwise linear gates: if $G$ is a pointwise linear gate, then $G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t)$. So a gate can be placed anywhere in the network without changing its effect on the frames.

The network exchanges two banks of values with prescribed signs, and it restores every auxiliary value it touches, so scratch registers can start with arbitrary contents. The [subset-intersection construction](subspace-intersection-network.md) attaches subspaces to these gates, and the [address-field interchange](address-interchange.md) is built from such a network.
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

Write the answer to `exegenius/tasks/0036-audit-linear-network-frames.answer.json`, then run `exegenius submit 0036-audit-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer file and submit again.
