# exegenius task 0012-audit-gaussian-resampling

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: discrete mathematics through modular arithmetic, primes, gcds and the Euclidean algorithm, and the binary (radix) representation of integers; a first course in linear algebra over the reals covering vector spaces, bases, dimension, matrices, rank and invertibility; and the basics of complex numbers and roots of unity. They have not studied finite fields beyond GF(2), bilinear forms, tensor products, rings beyond polynomials, or the fast Fourier transform as a specialist topic, so those are explained by the wiki.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Positional (radix) representation of integers (also: binary representation, base-2 representation, radix-q digits, radix representation, binary string, bit string)
- Logarithm (also: base-2 logarithm, log2, lg)
- Modular arithmetic (also: congruence modulo m, residue arithmetic, integers modulo m, Z/mZ, mod m)
- Greatest common divisor and coprimality (also: gcd, highest common factor, coprime, relatively prime, pairwise coprime)
- Euclidean algorithm and modular inverses (also: extended Euclidean algorithm, Bezout coefficients, multiplicative inverse modulo m)
- Prime numbers (also: prime, distinct odd primes, prime factorization, primality)
- Roots of unity (also: q-th root of unity, primitive root of unity, root of unity, powers of a root of unity)
- Vector space, subspace, basis and dimension (also: linear subspace, span, linear independence, basis, dimension of a vector space, dim)
- Matrix, linear map, rank and invertibility (also: linear transformation, matrix of a linear map, rank of a matrix, invertible matrix, nonsingular matrix, inverse matrix, kernel, image)
- Dot product and orthogonality (also: inner product, standard inner product, orthogonal vectors, orthogonal complement, perpendicular)
- Field of two elements (also: GF(2), F_2, binary field, Z/2Z, mod 2 arithmetic, XOR as addition)

## Symbols bound on earlier pages

- $k$ (padded output length), bound on `exact-integer-multiplication`: The number of bits in the padded binary representation.
- $k$ (digit width), bound on `radix-digit-convolution`: The number of bits in one radix digit.
- $m$ (digits per integer), bound on `radix-digit-convolution`: The number of digits in each integer.
- $u$ (first integer), bound on `radix-digit-convolution`: The first of the two integers to be multiplied, below $2^{km}$.
- $v$ (second integer), bound on `radix-digit-convolution`: The second of the two integers to be multiplied, below $2^{km}$.
- $u_i$ (digit of u), bound on `radix-digit-convolution`: The $i$-th radix-$2^k$ digit of $u$.
- $j$ (output index), bound on `discrete-fourier-transform`: An index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on `discrete-fourier-transform`: An index of an input entry, running from $0$ to $q-1$.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two. (cited)

Integer multiplication needs this, since the lengths its transforms require are pairwise coprime rather than powers of two. Gaussian resampling replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by transforms on power-of-two axes.

Let $s$ and $t$ be the number of coordinates of source and target vectors. Write $F_s$ and $P_s$ for the normalized Fourier transform and the coordinate permutation of length-$s$ vectors, and likewise $F_t$ and $P_t$ for length-$t$ vectors.

The identity uses two Gaussian-weighted maps $S,T$ from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of the Gaussian weights. For a length-$s$ vector $u$ with entries $u_j$, $0\le j<s$, and an index $0\le k<t$, they are

$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$

where subscripts are taken modulo $s$. $S$ gathers the entries of $u$ near the position $sk/t$, and $T$ spreads each entry $u_j$ over the targets near $tj/s$.

Let $\ell_j$ be the integer nearest to $tj/s$, with ties rounded upward, for $0\le j<s$, and let $\beta_j=tj/s-\ell_j$. Let $C:\mathbb C^t\to\mathbb C^s$ be the map $(Cv)_j=v_{\ell_j}$ that selects these coordinates, let $D:\mathbb C^s\to\mathbb C^s$ be the diagonal map $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$, an operator on length-$s$ vectors.

Expanding $(Nu)_j=\sum_i e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i$, the term $i=j$ has $ti/s-\ell_j=\beta_j$, so its two exponentials cancel and the term equals $u_j$. The Gaussian weight at the selected coordinate thus cancels the diagonal factor, and $N$ differs from the identity only through the other terms.

The paper uses a second parameter $\theta$, chosen so that $\alpha^2\theta>1$. With this choice the other terms give $\|N-I\|<1/2$ in the operator norm for the maximum-modulus vector norm. (cited)

A Neumann series inverts $N$: write $N=I-E$ with $\|E\|<1/2$. Then $\sum_{m\ge0}E^m$ converges, since $\|E^m\|\le\|E\|^m$, and its sum is $N^{-1}$, which has norm less than $2$.

The other sub-step is the Gaussian identity $TP_sF_s=P_tF_tS$. It says that applying $F_s$, then $P_s$ and $T$, gives the same result as applying $S$, then $F_t$ and $P_t$. The Fourier transform of a Gaussian is again a Gaussian, which is why such weights move between the two sets of frequencies. Its proof is in Harvey and van der Hoeven (cited).

Inverting $N$ turns this identity into the form used in the [transform identity with retained permutations](transform-identity.md).
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

Write the answer to `exegenius/tasks/0012-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0012-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
