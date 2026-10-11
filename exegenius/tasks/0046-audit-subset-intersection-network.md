# exegenius task 0046-audit-subset-intersection-network

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
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange)
- Address shear
- Gaussian dyadics

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $y$ (second input string), bound on `exact-integer-multiplication`: A binary string of length n, the second input to the product.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each input string.
- $n$ (input length), bound on `n-log-n-conjecture`: The number of bits in each of the two input integers.
- $A$ (multiplication machine), bound on `n-log-n-conjecture`: A fixed Turing machine that computes exact products.
- $n$ (input length), bound on `radix-digit-convolution`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $y$ (second input), bound on `radix-digit-convolution`: The second input, a binary string of $n$ bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $y$ (indeterminate), bound on `signed-packing`: The indeterminate of the polynomial ring, the variable in which the packed polynomials are written.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $g$ (second packed polynomial), bound on `signed-packing`: A second polynomial in y with r integer coefficients, multiplied with f by one integer product.
- $h$ (product polynomial), bound on `signed-packing`: The ordinary polynomial product fg, whose coefficients are read back from the integer product.
- $n$ (input length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $A$ (fixed machine), bound on `fixed-tape-model`: A fixed multiplication machine, whose alphabet and tape count do not depend on the input.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $y$ (second field), bound on `address-interchange`: The value of the second field, a block of bits at matching positions.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $h$ (value of H), bound on `address-shear`: The current value of H when m = 1.
- $h$ (ground set size), bound on `subspace-labels`: The number of elements of the ground set on which triples are taken.
- $T$ (triple), bound on `subspace-labels`: A three-element subset of the ground set.
- $t_T$ (triple indicator vector), bound on `subspace-labels`: The indicator vector of a triple $T$ in $\mathbb{Q}^h$, with a one in each coordinate of an element of $T$ and zero elsewhere.
- $S$ (other triple), bound on `subspace-labels`: Another triple of the ground set, compared with $T$ through the form.

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

## Page to audit (`subset-intersection-network`)

````markdown
# Subset-intersection network

A subset-intersection network is a fixed linear network whose wires carry single scalars and whose gates combine them according to how much two three-element subsets overlap. It exchanges two banks of values while restoring every scratch wire, and this exchange is the finite step on which the main result, [Integer multiplication below n log n](main-theorem.md), builds.

Fix $h$, the number of elements in the ground set $[h]=\{1,\dots,h\}$. A *triple* is a three-element subset of $[h]$, and $\mathcal{K}$ is the set of all triples. A *bank* is a family of values indexed by $a=(a_1,a_2,a_3)\in\mathcal{K}^3$; the two banks are $X$ and $Y$, with entries $x_a$ and $y_a$.

Each wire carries one scalar. A gate is a fixed linear map on a chosen set of wires, and wires it does not touch keep their values. A *scratch wire* is an auxiliary wire whose initial value may be arbitrary; the network must return every scratch wire to the value it started with.

For a triple $T$, its indicator vector $t_T$ is the $0/1$ vector on $[h]$ with a $1$ in the coordinate of each element $i$ of $T$ and $0$ elsewhere. Two distinct triples $S$ and $T$ are *neighbours* when they share exactly one element. In the bit construction the source uses this definition:

**The bit construction.** All arithmetic is mod 2. For each ordered neighbouring pair $(S,T)$ there is a side wire $A_{ST}$, and for each element $i\in[h]$ there is a central wire $C_i$. Four gates act on the wires:

- copy: adds $x_T$ to $A_{ST}$ for each neighbouring pair $(S,T)$;
- side injection: adds $\sum_{T \text{ neighbour of } S} A_{ST}$ to $y_S$;
- gather: adds $\sum_{T\ni i} x_T$ to $C_i$ for each $i\in[h]$;
- scatter: adds $\sum_{i\in S} C_i$ to $y_S$.

A *forward invocation* from $X$ to $Y$ runs the following eight rows in order. Each row is one gate, applied to the wires named in its grouping.

| row | operation | gate grouping |
|---|---|---|
| 0 | subtract side injection | one gate per target |
| 1 | subtract scatter | one gate on targets and centre |
| 2 | copy | one gate per source |
| 3 | gather | one gate on sources and centre |
| 4 | scatter | one gate on targets and centre |
| 5 | side injection | one gate per target |
| 6 | undo gather | one gate on sources and centre |
| 7 | undo copy | one gate per source |

Rows 0 and 1 subtract whatever the scratch wires already hold, so the arbitrary starting values cancel. Rows 2 to 5 load the source values and add their effect to the target, and rows 6 and 7 restore the scratch wires.

**Worked check.** Take $h\ge 5$, $S=\{1,2,3\}$, and look at the coefficient of each $x_T$ in the final $y_S$. The central route (gather then scatter) contributes $|S\cap T| \bmod 2$ to that coefficient, because each shared element is counted once. The side route contributes $1$ exactly when $T$ is a neighbour of $S$. Three cases cover all $T$:

- $T=S$: the central route gives $|S\cap S| \bmod 2 = 1$, and $S$ is not its own neighbour, so the coefficient is $1$.
- $T=\{1,4,5\}$, so $|S\cap T|=1$: the central route gives $1$ and the side route gives $1$, so the total is $1+1=0$.
- $|S\cap T|\in\{0,2\}$: the central route gives $0$, and $T$ is not a neighbour, so the total is $0$.

So the net change is $y_S\leftarrow y_S+x_S$, and every other $y$ value is unchanged, whatever the scratch wires held at the start. The side wires exist to cancel the intersection-one terms.

**Exchanging the banks.** Using the forward invocation, the construction runs three stages, one per coordinate of $a$, with the other coordinates fixed. Over $\mathbb{F}_2$ signs disappear, and the three-invocation sequence from $X$ to $Y$, from $Y$ to $X$, and from $X$ to $Y$ takes $(x,y)$ to $(x,\,x+y)$, then $(y,\,x+y)$, then $(y,\,x)$. The paper states the outcome as and Ya, with every auxiliary wire restored.

**Why the wires carry subspaces.** A subspace labelled on a gate tells the network how much work a change of representation costs. Each gate is labelled by [Subspace labels](subspace-labels.md): a nondegenerate subspace of a fixed bilinear space, meaning one on which the form restricts to a nonsingular form, so that the whole space splits as the subspace plus its orthogonal complement. On every edge one label contains the other, and the change in dimension between them is the dimension of the orthogonal residual, the part of the larger label orthogonal to the smaller one., so keeping the dimension change small keeps the cost small.

The labels are chosen from the indicator vectors. Each indicator line $\langle t_T\rangle$ is nondegenerate, so it splits off its complement cleanly. Neighbouring lines are orthogonal to each other, so the line of a neighbour lies inside the complement of $t_T$ and can be split from it without disturbing the rest of the label. Hence moving from one triple's label to a neighbour's changes the label by one nondegenerate piece, and the orthogonality of neighbours is what makes the nesting work.

The complex variant uses the same schedule with the scalars and neighbour rule changed: even intersection.

The network is built within the framework of [Linear networks and frames](linear-network-frames.md): every wire is a role and every gate carries a frame, so the same scalar gates can act on arrays.
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

Write the answer to `exegenius/tasks/0046-audit-subset-intersection-network.answer.json`, then run `exegenius submit 0046-audit-subset-intersection-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
