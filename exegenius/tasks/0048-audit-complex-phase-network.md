# exegenius task 0048-audit-complex-phase-network

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
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: A binary string of length n, the first input to the product.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each digit.
- $q$ (digits per input), bound on `radix-digit-convolution`: The number of radix-$2^b$ digits in each input.
- $x$ (first input), bound on `radix-digit-convolution`: The first input, a binary string of $n$ bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit, running from $0$ to $q-1$.
- $z$ (formal variable), bound on `radix-digit-convolution`: A formal variable in which each input is written as a polynomial whose coefficients are its digits.
- $a$ (Gaussian integer numerator), bound on `gaussian-dyadics`: A Gaussian integer, the numerator of a Gaussian dyadic over a power of two.
- $g$ (logical array), bound on `linear-network-frames`: The array a wire is meant to represent before any frame is applied.
- $r$ (coefficient count), bound on `signed-packing`: The number of coefficients of each polynomial being packed.
- $p$ (coefficient bit bound), bound on `signed-packing`: The number of bits in the magnitude bound on each coefficient, so every coefficient has magnitude at most 2^p.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial in y with r integer coefficients, packed as the integer f(B).
- $g$ (second packed polynomial), bound on `signed-packing`: A second polynomial in y with r integer coefficients, multiplied with f by one integer product.
- $B$ (block base), bound on `signed-packing`: The base 2^{4p} of the integer encoding, one block of 4p bits per coefficient.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $V$ (stored volume), bound on `address-interchange`: The number of stored bits in the array.
- $x$ (first field), bound on `address-interchange`: The value of the first field, a block of bits at matching positions.
- $H$ (address field H), bound on `address-shear`: The first of the two address fields, a vector of m fields, which the shear updates.
- $m$ (fields per vector), bound on `address-shear`: The number of fields in each of the vectors H and D.
- $b$ (digits per field), bound on `address-shear`: The number of radix-q digits in each field.
- $q$ (radix prime), bound on `address-shear`: A fixed odd prime, the base of the digits.
- $a$ (rational rank), bound on `address-shear`: The number of interchanges used for the shear with matrix M, equal to the rank of M over the rational numbers.
- $V$ (stored bit volume), bound on `address-shear`: The number of stored bits in the array.
- $d$ (value of D), bound on `address-shear`: The current value of D when m = 1.
- $E$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space that contains every label, with bilinear form $\langle\cdot,\cdot\rangle$.
- $m$ (ambient dimension), bound on `subspace-labels`: The dimension of $E$, which counts the coordinates of a vector of $E$.
- $U$ (label), bound on `subspace-labels`: A nondegenerate subspace of $E$ attached to a gate or terminal.
- $V$ (head label), bound on `subspace-labels`: The label at the head of an edge, whose tail label is $U$.
- $C_U$ (label frame), bound on `subspace-labels`: The frame at a vertex whose label is $U$.
- $a$ (bank index), bound on `subset-intersection-network`: An index $a=(a_1,a_2,a_3)$ of one entry of a bank, a triple of triples.
- $X$ (source bank), bound on `subset-intersection-network`: One of the two banks of values, with entries $x_a$, that the network exchanges.
- $i$ (ground element), bound on `subset-intersection-network`: An element of the ground set $[h]$, one coordinate of an indicator vector.
- $s$ (smaller call count), bound on `rank-saving-recursion`: The number of smaller calls that one call makes.
- $m$ (label dimension), bound on `rank-saving-recursion`: The dimension of the fixed ambient space in which the labels are subspaces.
- $V$ (data volume), bound on `rank-saving-recursion`: The number of stored data bits in the array that a call works on.
- $f$ (call parameter), bound on `rank-saving-recursion`: The parameter of a call, which counts the digits of the field being interchanged or the selected axes of a numerical layer.
- $g$ (normalized cost), bound on `rank-saving-recursion`: The function giving the cost of a call at parameter f divided by its volume.

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

## Page to audit (`complex-phase-network`)

````markdown
# Complex phase network

The complex phase network is obtained from the [subset-intersection network](subset-intersection-network.md) by replacing each wire's scalar with an array of complex values, and it changes the frame of those arrays along each edge by a product of two-point kernels. It supplies the frame identity that the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) uses to apply a butterfly on several address bits at once, one step toward the [main theorem](main-theorem.md).

The constants are $a = (1+i)/2$ and $b = (1-i)/2$. Here $x \in \mathbb{F}_2^m$ is a binary address, and $m$ is the number of its coordinates.

Let $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ be the normalized Hadamard matrix. Let $X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ be the bit-flip matrix, which swaps the two coordinates of a vector.

The two-point kernel is $C = H\,\mathrm{diag}(1, i)\,H = aI + bX$, where $I$ is the identity. Since $a^2+b^2=0$ and $2ab=1$, squaring gives $C^2 = X$. Also $C^{-1} = bI + aX$, because $(aI+bX)(bI+aX) = I$.

The complex phase network is indexed by [subspace labels](subspace-labels.md), with one binary label at each vertex. A label $U$ is a subspace of $\mathbb{F}_2^m$. The frame at a vertex with label $U$ is the matrix $C_U$ defined below.

Let $\mathrm{wt}(x)$ be the Hamming weight of a binary vector $x$, the number of its coordinates equal to 1, read as an integer. Let $P_U$ be the projection onto $U$ over $\mathbb{F}_2$. For a label $U$, let $q_U(x)$ be the Hamming weight of $P_U x$ modulo 4, so that $q_U(x) = \mathrm{wt}(P_U x) \pmod 4$.

For a label $U$, the frame is
$$C_U = H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_U(x)}\big)\,H^{\otimes m},$$
where $\mathrm{diag}_x(i^{q_U(x)})$ multiplies the value at each address $x$ by $i^{q_U(x)}$, and $H^{\otimes m}$ is the $m$-fold tensor power of $H$. Each entry of $C_U$ and of its inverse is therefore a Gaussian integer divided by $2^m$, so $C_U$ and its inverse preserve arrays of Gaussian dyadic values.

For an edge from label $U$ to label $V$, the frame change is $C_V C_U^{-1}$, where $V$ is the head label.

Let $E$ be the orthogonal residual of the edge, so that $V = U \perp E$ on an increasing edge. Let $B$ be an orthonormal basis of $E$. Each $v \in B$ is a binary vector with $v \cdot v = 1$. Since $v \cdot v = 1$, $\mathrm{wt}(v)$ is odd, so for each $v$ there is a sign $\varepsilon \in \{1,-1\}$ with $\mathrm{wt}(v) \equiv \varepsilon \pmod 4$, where the sign also carries the edge direction. Then $q_V(x) - q_U(x) = \sum_{v\in B} \mathrm{wt}(v)\,[v\cdot x] \pmod 4$, where $[v\cdot x]$ is 1 when $v\cdot x = 1$ and 0 otherwise, and the right side is negated on a decreasing edge. The reason is the weight identity with the correction term $-2|\mathrm{supp}(z) \cap \mathrm{supp}(w)|$, where $\mathrm{supp}(z)$ is the set of coordinates at which $z$ is 1. If $z\cdot w = 0$, the intersection has even size, so the weight is additive modulo 4.

For each $v \in B$, the factor is $i^{\varepsilon[v\cdot x]} = \frac{1+i\varepsilon}{2} + \frac{1-i\varepsilon}{2}(-1)^{v\cdot x}$, since both sides equal 1 when $v\cdot x = 0$, and the right side equals $i\varepsilon$ when $v\cdot x = 1$. tensored over the coordinates in the support of $v$ turns the character $(-1)^{v\cdot x}$ into a translation. The translation $X_v$ is defined by $(X_v f)(x) = f(x+v)$. So the factor is $\frac{1+i\varepsilon}{2}I + \frac{1-i\varepsilon}{2}X_v$. This is $aI + bX_v$ for $\varepsilon = 1$, and $bI + aX_v$ for $\varepsilon = -1$, which is the inverse of $aI + bX_v$ by the same computation as for $C$, using $X_v^2 = I$.

The frame change on the edge is therefore a product, over $v \in B$, of one such kernel, each $aI + bX_v$ or its inverse. Along a route of edges the intermediate frames cancel, so the composite change depends only on its endpoints.

The complex phase network has coefficients in [Gaussian dyadics](gaussian-dyadics.md): each entry of $C_U$ and of its inverse is a Gaussian integer divided by $2^m$.

Take $m=1$ and the two labels $\{0\}$ and $\mathbb{F}_2$. For $\{0\}$, $q_{\{0\}}(x)=0$, so $C_{\{0\}} = H\,I\,H = I$. For $\mathbb{F}_2$, $P_{\mathbb{F}_2}$ is the identity, so $q_{\mathbb{F}_2}(x) = x$ and $C_{\mathbb{F}_2} = C$. The edge from $\{0\}$ to $\mathbb{F}_2$ has residual $E = \mathbb{F}_2$ with orthonormal basis $B = \{1\}$, because $\mathrm{wt}(1) = 1$ and $\varepsilon = 1$. Its frame change is $C_{\mathbb{F}_2} C_{\{0\}}^{-1} = C = aI + bX_1$. Here $X_1 = X$, since $X_1$ maps $f(x)$ to $f(x+1)$, which swaps the two values of $f$.
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

Write the answer to `exegenius/tasks/0048-audit-complex-phase-network.answer.json`, then run `exegenius submit 0048-audit-complex-phase-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
