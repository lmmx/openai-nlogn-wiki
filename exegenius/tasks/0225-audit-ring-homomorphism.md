# exegenius task 0225-audit-ring-homomorphism

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
- Discrete Fourier transform (also: normalized Fourier transform, transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Transform identity with retained permutations (also: target permutation)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $w$ (input wire), bound on `linear-network-frames`: An input wire of the network.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $w$ (input role), bound on `endpoint-operator`: An input role of the network, whose route starts at its source vertex.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $\lambda$ (scalar multiplier), bound on `line-spanned-by-vector`: A scalar in K, an element of the scalar field, used to scale v.
- $Q$ (second matrix), bound on `tensor-product`: A second matrix, which is copied once for each entry of P in the tensor product P \otimes Q.
- $w$ (key width), bound on `stable-radix-sort`: The number of bits in each key.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $\xi$ (first input value), bound on `butterfly`: The first of the two values that the butterfly takes as input.
- $\eta$ (second input value), bound on `butterfly`: The second of the two values that the butterfly takes as input.
- $w$ (array entry), bound on `array-norm`: A single entry of the array X, which is a complex number.
- $w$ (input vector), bound on `linear-contraction`: A vector in the input space of a linear map, with m complex coordinates.
- $\eta$ (error vector), bound on `linear-contraction`: The difference between a computed input and the exact input w.
- $w$ (class member), bound on `congruence-modulo`: An integer in the residue class of d modulo m.
- $w$ (formal variable), bound on `cyclic-convolution`: A formal variable in which a sequence is written as a polynomial, never evaluated.
- $\Phi$ (coefficient layout map), bound on `cyclic-convolution`: The map of the paper's Section 9.3 from a cyclic convolution to a multidimensional one.
- $w$ (second argument), bound on `bilinear-map`: A vector of W, the second argument of the bilinear map.
- $\xi$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\eta$ (vector), bound on `bilinear-form`: A vector of $X$.
- $\xi$ (source vector), bound on `subset-intersection-network`: The vector of source-bank entries on one line, indexed by triples.
- $\eta$ (target vector), bound on `subset-intersection-network`: The vector of target-bank entries on one line, indexed by triples.
- $\lambda$ (constant lambda), bound on `complex-phase-network`: The constant $(1+i)/2$.
- $\mu$ (constant mu), bound on `complex-phase-network`: The constant $(1-i)/2$.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $\mu$ (first value), bound on `simultaneous-butterfly-layer`: The first of the two values of a pair, the first input of the two-point map.
- $\mu$ (source dimension sum), bound on `rank-saving-recursion`: The sum of the dimensions of the source labels.
- $\eta$ (twiddle exponent), bound on `transform-round`: The exponent of y at an address, an integer taken modulo 2r.
- $Q$ (box size), bound on `padded-transform-box`: The number of entries of the padded transform box, the product of the padded lengths of all axes.
- $\varphi$ (function being bounded), bound on `little-o-notation`: A map from the positive reals to the positive reals, the function that the little-o statement bounds.
- $\psi$ (comparison function), bound on `little-o-notation`: A map from the positive reals to the positive reals, positive for all large arguments, against which the function being bounded is compared.
- $\lambda$ (limit variable), bound on `little-o-notation`: The real point at which both functions are evaluated, taken to infinity in the limit.
- $\eta$ (per-level operation count), bound on `guard-width-bound`: The fixed count $64(W+m+1)^3$ of operations that a level adds beyond its $s$ child calls.
- $\mu$ (modular inverse), bound on `modular-inverse`: The integer with $\beta\mu$ congruent to $1$ modulo $M$.
- $\xi$ (cyclic generator), bound on `modular-inverse`: A generator of a cyclic group of order $S$, which the map sends to $\prod_i \xi_i^{\mu_i}$.
- $\lambda$ (chunk width), bound on `packed-bit-addition`: The number of address bits in each chunk, equal to the number of segments times the segment width.
- $\mu$ (segment width), bound on `packed-bit-addition`: The number of bits in each segment of a chunk.
- $\xi$ (target segment value), bound on `packed-bit-addition`: The value of a segment of the target chunk during the eight updates.
- $\eta$ (scratch segment value), bound on `packed-bit-addition`: The value of the corresponding segment of the scratch chunk during the eight updates.
- $w$ (second vector), bound on `transform-identity`: A second complex vector of length q, paired with u in the permutation and product formulas.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.
- $w$ (scaled input), bound on `bluestein-chirp-identity`: The input vector u with each entry divided by the corresponding chirp entry.

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

## Page to audit (`ring-homomorphism`)

````markdown
# Ring homomorphism and isomorphism

A ring homomorphism is a map $\varphi: Q \to Q'$ between two rings that preserves both operations, so that $\varphi(\xi+\eta)=\varphi(\xi)+\varphi(\eta)$ and $\varphi(\xi\eta)=\varphi(\xi)\varphi(\eta)$ for all $\xi,\eta\in Q$, and $\varphi(1)=1$. Ring homomorphisms carry a convolution from one ring to another without changing its values, which is how the paper moves convolution on the remaining axes into a polynomial ring where it can be computed.

A ring is a set with addition, subtraction, a zero, and an associative multiplication with identity $1$ that distributes over addition. A ring homomorphism is an isomorphism when it is also bijective (one-to-one and onto). Then $Q$ and $Q'$ have the same structure, and each sum or product in one ring corresponds to exactly one in the other: the inverse map also preserves both operations, so a product computed in $Q'$ maps back to the product in $Q$.

**Checking that a map is a homomorphism.** Let $Q=\mathbb{C}[w]/(w^2-1)$, the ring in which the indeterminate $w$ satisfies $w^2=1$. Every element of $Q$ has the form $\lambda+\mu w$ with $\lambda,\mu\in\mathbb{C}$, where $\lambda$ and $\mu$ are its coefficients. A map out of $Q$ is determined by the image of $w$, and it is well defined only if that image satisfies the relation $w^2=1$. A ring homomorphism into the quotient ring [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md) is checked in that ring by substituting $y^r=-1$. The paper uses this same check for its map $\Phi$ from a cyclic quotient ring into a multivariate quotient ring:

**Example.** Let $Q'=\mathbb{C}[y]/(y^2+1)$, where $y^2=-1$, and define $\varphi: Q \to Q'$ by $\varphi(\lambda+\mu w)=\lambda+\mu\sqrt{-1}\,y$. The image of $w$ is $\sqrt{-1}\,y$, and $(\sqrt{-1}\,y)^2=-y^2=1$ in $Q'$, so the relation $w^2=1$ is respected and $\varphi$ is well defined. It also preserves products. In $Q$, $(1+w)^2=2+2w$, while in $Q'$
$$(1+\sqrt{-1}\,y)^2=1+2\sqrt{-1}\,y+(\sqrt{-1}\,y)^2=2+2\sqrt{-1}\,y=\varphi(2+2w).$$
The map is bijective because it is $\mathbb{C}$-linear and sends the basis $1,w$ of $Q$ to the basis $1,\sqrt{-1}\,y$ of $Q'$. Its inverse sends $1+y$ to $1-\sqrt{-1}\,w$, since $\varphi(1-\sqrt{-1}\,w)=1-\sqrt{-1}\cdot\sqrt{-1}\,y=1+y$. So $\varphi$ is an isomorphism.

**A map that is not an isomorphism.** Let $\psi: Q \to \mathbb{C}$ be $\psi(\lambda+\mu w)=\lambda+\mu$. This is a ring homomorphism, because $\psi(w)=1$ satisfies $w^2=1$. It is not bijective: $w-1$ is nonzero in $Q$ but $\psi(w-1)=0$. So $Q$ and $\mathbb{C}$ do not have the same structure, and the values of $\psi$ do not determine the element of $Q$ they came from.

**Why the paper needs it.** The paper's map $\Phi$ sends a generator to a monomial whose powers cover the target basis, so it is bijective as well as a homomorphism: The paper concludes that convolution. An isomorphism of this kind [preserves cyclic convolution](cyclic-convolution.md): the convolution of two sequences in one ring maps to the convolution of their images in the other.
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

Write the answer to `exegenius/tasks/0225-audit-ring-homomorphism.answer.json`, then run `exegenius submit 0225-audit-ring-homomorphism` in the project directory. If submit rejects the answer, fix the answer and submit again.
