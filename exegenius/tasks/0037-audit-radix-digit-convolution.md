# exegenius task 0037-audit-radix-digit-convolution

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`radix-digit-convolution`)

````markdown
# Radix-digit convolution

Radix-digit convolution is a reduction of [exact integer multiplication](exact-integer-multiplication.md) that writes each input as a polynomial in a power of two whose coefficients are its digits, so that the product becomes a convolution of short integer coefficients. It is the first step of the argument for [Integer multiplication below n log n](main-theorem.md): the [Chinese-remainder map](chinese-remainder-map.md) and [carry propagation](carry-propagation.md) pages build on the coefficients it produces.

The paper states the reduction in one sentence:

The input length $n$ is the number of bits in each input. Let $x$ and $y$ be the two inputs, each a binary string of $n$ bits. Fix a digit width $b$: each digit is a block of $b$ bits. The paper takes, so that $2^b \ge n$. Split each input into blocks of $b$ bits, counting from the least significant end. A block is a digit in base $2^b$, the radix: its value lies between $0$ and $2^b - 1$. The inputs have $q = \lceil n/b \rceil$ digits each. Here $i$ is the position of a digit, running from $0$ to $q-1$. The digits of $x$ are $x_0$ through $x_{q-1}$, where $x_i$ is the digit of weight $(2^b)^i$, so that $x = \sum_i x_i (2^b)^i$. The digits of $y$ are $y_0$ through $y_{q-1}$, with $y_i$ defined the same way.

Here $z$ is a formal variable, and each input becomes a polynomial in $z$ whose coefficients are its digits. Substituting $z = 2^b$ into that polynomial returns the input.

Multiplying the two digit polynomials gives a polynomial of degree at most $2q-2$. Here $j$ is the position of a product coefficient, running from $0$ to $2q-2$. The coefficient $c_j$ is the integer multiplying $z^j$ in the product of the two digit polynomials. It is the sum
$$c_j = \sum_i x_i\, y_{j-i},$$
taken over all $i$ with $0 \le i \le q-1$ and $0 \le j-i \le q-1$. This sum is the convolution of the digit sequences $(x_i)$ and $(y_i)$. Substituting $z = 2^b$ into the product gives the identity $xy = \sum_j c_j (2^b)^j$, so the integer product is recovered from the sequence $(c_j)$ once the coefficients are known.

Each $c_j$ is a sum of at most $q$ products $x_i\, y_{j-i}$, and each product is at most $(2^b-1)^2$, so $0 \le c_j \le q(2^b-1)^2$. Since $q \le n \le 2^b$, every coefficient is below $2^{3b}$, so it fits in $3b$ bits. this bound.

Take $n = 4$. Then $b = 2$ and $q = 2$. Let $x = 1101$ (value 13) and $y = 1011$ (value 11). Splitting into base-4 digits from the least significant end gives $x_0 = 1$, $x_1 = 3$, $y_0 = 3$ and $y_1 = 2$. The coefficients are $c_0 = x_0 y_0 = 3$, $c_1 = x_0 y_1 + x_1 y_0 = 2 + 9 = 11$ and $c_2 = x_1 y_1 = 6$. Check: $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$. The coefficient $c_1 = 11$ is larger than a digit, so the sequence is not yet the binary product. Carry propagation converts it into one.

The reason for the split is cost. Each coefficient has $O(\log n)$ bits, so arithmetic on a single coefficient is cheap, and the convolution is no longer a problem about individual bits. Its work is set by how the transforms move the $2q-1$ coefficients. The transforms are the expensive part, since each transform level scans the stored bits. The paper's count of this is that The later pages reduce that cost.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
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
          "description": "The term, or a short label for the step.",
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
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0037-audit-radix-digit-convolution.answer.json`, then run `exegenius submit 0037-audit-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
