# exegenius task 0191-audit-polynomial-ring-mod-yr-plus-1

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
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Ground set
- Indicator vector
- Limit inferior
- Line spanned by a vector
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $k$ (term index), bound on `limit-inferior`: The position of a term in the sequence $x$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $z$ (integer to encode), bound on `exact-integer-multiplication`: A nonnegative integer less than $2^k$, which is written in binary by the padded representation.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $k$ (offset), bound on `cyclic-shift`: The integer, taken modulo L, by which the cyclic shift rotates the block.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $k$ (level count), bound on `address-interchange`: The number of recursion levels, log base m of the field width.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $z$ (input array), bound on `truncation`: An array of complex coefficients that is truncated by $Q_p$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $k$ (key), bound on `stable-radix-sort`: The key of a record, written as a string of $w$ bits.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $\zeta$ (phase factor), bound on `phase-factor`: A complex number of modulus one, the factor multiplied into coefficients.
- $a$ (numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of an element $a/2^k$ of $\mathbb{D}$.
- $k$ (denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of an element of $\mathbb{D}$.
- $q$ (transform length), bound on `discrete-fourier-transform`: The number of coordinates of each vector the transform acts on.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $z$ (formal variable), bound on `radix-digit-convolution`: A formal variable in which each input is written as a polynomial.
- $m$ (input position), bound on `multidimensional-transform`: A position in the input array, with each coordinate below its axis length.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $R_r$ (record ring), bound on `synthetic-transforms`: The ring of polynomials with complex coefficients in which $y^r$ is identified with $-1$; records are its elements.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $m$ (coefficient position), bound on `synthetic-transforms`: The position of a coefficient in a record, running from $0$ to $r-1$.

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

## Page to audit (`polynomial-ring-mod-yr-plus-1`)

````markdown
# Polynomial ring modulo $y^r + 1$

The polynomial ring modulo $y^r+1$ is the set of polynomials with complex coefficients in which $y^r$ is identified with $-1$, so that $y$ has order $2r$ and wrap-around flips a sign. One coordinate of the array is stored in this ring, and the [convolution over this ring](polynomial-ring-convolution.md) is built on it.

Here $y$ is the polynomial variable, an indeterminate (a symbol with no numeric value) whose powers act as roots of unity. Here $r$ is the record length, the number of complex coefficients in a polynomial record, which is a power of two. We write $R_r$ for this ring, $R_r=\mathbb{C}[y]/(y^r+1)$: two polynomials are identified when they differ by a multiple of $y^r+1$.

In the argument, one coordinate of the array is stored. Here $z$ is one element of $R_r$, a polynomial with complex coefficients; this is a different meaning from the letter $z$ on the synthetic-transforms page.

The degree is the largest exponent with a nonzero coefficient. A polynomial of any degree is reduced by replacing each power $y^e$, with $e \ge r$ an integer exponent, by $-y^{e-r}$, which is valid because $y^e = y^{e-r}\,y^r = -y^{e-r}$. Repeating this gives a representative of degree less than $r$. This representative is unique. If two representatives of degree less than $r$ denoted the same element, their difference would be $q\,(y^r+1)$ for some nonzero polynomial $q$. That product has degree $\deg q + r \ge r$, because $y^r+1$ has leading coefficient $1$. But the difference of two polynomials of degree less than $r$ has degree less than $r$, so the difference must be zero.

Let $k$ be the position of a coefficient, running from $0$ to $r-1$, and let $z_k$ be the $k$-th coefficient of $z$. Then each element is $z=\sum_{k=0}^{r-1} z_k y^k$. The list $(z_0,\dots,z_{r-1})$ is the coefficient list of $z$. Addition is coefficientwise.

A root of unity is a complex number $\zeta$ for which some positive integer power equals $1$. The exponent is written $m$, a positive integer, the number of factors of $\zeta$ whose product is $1$, so $\zeta^m=1$. The order of $\zeta$ is the least such $m$. Since $y^r=-1$, we get $y^{2r}=(-1)^2=1$. No smaller positive power of $y$ equals $1$. For $0<k<r$, $y^k$ is a representative of degree $k\ge 1$, while $1$ has degree $0$, so $y^k \ne 1$ by uniqueness. For $r\le k<2r$, $y^k=-y^{k-r}$ is a representative of degree less than $r$ that is not $1$: it equals $-1$ when $k=r$, and has degree $k-r\ge 1$ otherwise. So $y$ has order $2r$.

Take $r=4$. Then $y^4=-1$, and $z=1+2y$ has coefficient list $(1,2,0,0)$. Multiplying by $y^3$ gives $zy^3=y^3+2y^4=y^3-2$, with coefficient list $(-2,0,0,1)$. The coefficient $1$ at position $0$ moves to position $3$. The coefficient $2$ at position $1$ would move to position $4$, which is position $0$ with its sign reversed, giving $-2$ there.

In general, let $a$ be the shift amount, with $0 \le a < r$. Multiplying by $y^a$ moves $z_k$ to position $k+a$ when $k+a<r$. Otherwise $y^{k+a}=-y^{k+a-r}$, so $z_k$ moves to position $k+a-r$ with its sign reversed. This wrap-around is why the ring is called negacyclic. In a cyclic wrap-around, as in [cyclic convolution](cyclic-convolution.md), a coefficient that passes the end re-enters at the start with its sign unchanged.

Transforms need roots of unity, and powers of $y$ supply them. The powers $y^a$ with $0 \le a < 2r$ are roots of unity of order dividing $2r$. Transforms multiply entries by roots of unity, which would normally cost complex multiplications. Here coefficient list. So it costs data movement, not complex multiplications.

This ring gives the arithmetic for the [synthetic polynomial transforms](synthetic-transforms.md), whose roots of unity are powers of $y$.
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

Write the answer to `exegenius/tasks/0191-audit-polynomial-ring-mod-yr-plus-1.answer.json`, then run `exegenius submit 0191-audit-polynomial-ring-mod-yr-plus-1` in the project directory. If submit rejects the answer, fix the answer and submit again.
