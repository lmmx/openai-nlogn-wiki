# exegenius task 0156-audit-linear-network-frames

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
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Convolution
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $v$ (vertex), bound on `linear-algebra-basics`: A vertex of the network in the paper, at which a frame is placed.
- $D_v$ (frame), bound on `linear-algebra-basics`: The invertible linear operator on arrays attached to vertex $v$.
- $g$ (logical array), bound on `linear-algebra-basics`: The array of values that the network computes on, before its frame is applied.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`linear-network-frames`)

````markdown
# Linear networks and frames

A linear network is a fixed wiring of linear gates that exchanges two banks of values and restores its scratch values. A frame is built from an invertible [linear operator](linear-algebra-basics.md) attached to a vertex of a network, saying how the array on its wires is stored. Each tape procedure is realised as one such network acting on arrays, and frames let its gates act on those arrays without changing their representation.

A tape procedure is an operation on the tapes of a Turing machine. A scratch (auxiliary) wire carries no input or output and is restored at the end.

A gate is a fixed linear map on a specified set of wires, and; the segment between consecutive vertices is an edge.: a role is a fixed place in the network, not the value there.

The logical array $g$ of a wire at a vertex is the array the wire is meant to represent before any frame is applied. To run the network on arrays, let each scalar be an array indexed by a common set of addresses, and let each gate act separately at each address. Let $G$ be a pointwise linear gate. $t$ is the number of input arrays the gate takes, and $g_1,\dots,g_t$ are its logical input arrays. Each $c_j$ is the fixed weight of input $j$, the same at every address, so $G(g_1,\dots,g_t)=\sum_j c_j g_j$ at each address.

At each vertex $v$ (a source, gate or sink) choose an invertible linear operator $D_v$ on arrays over the common addresses, and call $D_v$ the frame of $v$. The stored array at $v$ is $D_v g$. Along an edge from $u$ to $v$, where $u$ is the earlier vertex, from $D_u g$ to $D_v g$, while $g$ does not change.

The key identity is

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

It holds for every linear $D_v$, because $D_v$ is linear on whole arrays: $\sum_j c_j D_v g_j = D_v \sum_j c_j g_j$, with the same weights at every address. For example, take $t = 2$ and $G(g_1, g_2) = g_1 + g_2$ on arrays with two addresses, and let $D_v$ be the $2\times 2$ matrix with rows $(1, 1)$ and $(0, 1)$. For $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs are $(1, 0)$ and $(1, 1)$; the gate gives $(2, 1)$, which is $D_v(1, 1)$.

The inputs of a gate must share one representation for the combination to be the logical sum, and

. Write $\mathrm{sink}(r)$ for the sink vertex of output role $r$. Write $w$ for an input wire, $f_w$ for the supplied physical array on it, and $\mathrm{source}(w)$ for its source vertex. Its logical array is $g_w = D_{\mathrm{source}(w)}^{-1} f_w$.

The scalar network sends input role $w$ to output role $\rho(w)$, where $\rho$ is this permutation of roles, and multiplies the value by a fixed sign $\varepsilon_w$ on the way. The logical array on $\rho(w)$ is therefore $\varepsilon_w g_w$, with stored array $D_{\mathrm{sink}(\rho(w))}\,\varepsilon_w g_w$ at the sink. Along the route the edge operators telescope,, leaving

$$\varepsilon_w\, D_{\mathrm{sink}(\rho(w))}\, D_{\mathrm{source}(w)}^{-1} f_w.$$

The bit procedure is built from a network of pointwise XOR gates, since, and the frames act on the [address fields](address-field.md) of each array., which updates one field by adding the other.

The claim this page supports is that each tape procedure is such a network:. Its construction chooses a scalar network that exchanges the two banks and restores the scratch values; the endpoint formula then gives the operator on the arrays.
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

Write the answer to `exegenius/tasks/0156-audit-linear-network-frames.answer.json`, then run `exegenius submit 0156-audit-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.
