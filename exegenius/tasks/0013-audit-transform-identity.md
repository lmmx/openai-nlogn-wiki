# exegenius task 0013-audit-transform-identity

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
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
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
- $u$ (first integer), bound on `radix-digit-convolution`: The first of the two integers to be multiplied, below $2^{km}$.
- $v$ (second integer), bound on `radix-digit-convolution`: The second of the two integers to be multiplied, below $2^{km}$.
- $q$ (vector length), bound on `discrete-fourier-transform`: The number of entries in each vector, which is the length of the transform.
- $j$ (output index), bound on `discrete-fourier-transform`: An index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on `discrete-fourier-transform`: An index of an input entry, running from $0$ to $q-1$.
- $s$ (source length), bound on `gaussian-resampling`: $s$ is the number of coordinates of a source vector.
- $t$ (target length), bound on `gaussian-resampling`: $t$ is the number of coordinates of a target vector.
- $F_s$ (source transform), bound on `gaussian-resampling`: $F_s$ is the normalized Fourier transform of length-$s$ vectors.
- $P_s$ (source permutation), bound on `gaussian-resampling`: $P_s$ is the coordinate permutation of length-$s$ vectors.
- $F_t$ (target transform), bound on `gaussian-resampling`: $F_t$ is the normalized Fourier transform of length-$t$ vectors.
- $P_t$ (target permutation), bound on `gaussian-resampling`: $P_t$ is the coordinate permutation of length-$t$ vectors.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: $\alpha$ is the parameter that sets the width of the Gaussian weights.
- $u$ (source vector), bound on `gaussian-resampling`: $u$ is a length-$s$ vector with entries $u_j$.
- $j$ (entry index), bound on `gaussian-resampling`: $j$ indexes the entries $u_j$ of a source vector, $0\le j<s$.
- $k$ (target index), bound on `gaussian-resampling`: $k$ is an index of a target coordinate, $0\le k<t$.
- $S$ (Gaussian source map), bound on `gaussian-resampling`: $S$ is the Gaussian-weighted map from length-$s$ to length-$t$ vectors.
- $T$ (Gaussian target map), bound on `gaussian-resampling`: $T$ is the Gaussian-weighted map from length-$s$ to length-$t$ vectors.
- $C$ (selection map), bound on `gaussian-resampling`: $C$ is the map from length-$t$ to length-$s$ vectors that selects the coordinates $\ell_j$.
- $D$ (diagonal map), bound on `gaussian-resampling`: $D$ is the diagonal map on length-$s$ vectors that multiplies entry $j$ by $e^{\pi\alpha^2\beta_j^2}$.
- $N$ (near-identity operator), bound on `gaussian-resampling`: $N=CTD$ is an operator on length-$s$ vectors.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

The transform identity with retained permutations is an exact identity relating two Fourier transforms of different lengths, with both coordinate permutations kept as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. (cited) Keeping the permutations as factors lets them cancel across a convolution instead of being executed as sorts.

The integer $s$ is the number of coordinates of a source vector. The integer $t$ is the number of coordinates of a target vector, with $2\le s<t$ and $\gcd(s,t)=1$. The integer $\alpha\ge 2$ sets the width of the Gaussian weights. $F_s$ is the normalized Fourier transform of length $s$, and $F_t$ that of length $t$. $P_s$ is the permutation $(P_su)_j=u_{tj}$ of length-$s$ vectors, with subscripts taken modulo $s$. $P_t$ is the permutation $(P_tv)_k=v_{-sk}$ of length-$t$ vectors, with subscripts taken modulo $t$.

A linear contraction is a linear map of norm at most one. $A$ is a linear contraction from length-$s$ to length-$t$ vectors. $B_0$ is a linear contraction from length-$t$ to length-$s$ vectors. The step claims
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
and its proof sits under (cited).

The proof uses two Gaussian-weighted maps $S$ and $T$ from length-$s$ to length-$t$ vectors, defined by the sums below.
$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
They satisfy the Gaussian identity $TP_sF_s=P_tF_tS$.

For $0\le j<s$, $q_j$ is the integer nearest $tj/s$, with ties rounded upward. The map $C$ selects the coordinates $q_0,\dots,q_{s-1}$ from a length-$t$ vector. The map $D$ is the diagonal map $(Du)_j=e^{\pi\alpha^2(tj/s-q_j)^2}u_j$ on length-$s$ vectors, whose factor cancels the Gaussian factor of $T$ at $q_j$.

The operator $N=CTD$ is near the identity. Its $j$-th output is $u_j$ plus a small error, so $\|N-I\|<1/2$. Hence $N$ is invertible, with $N^{-1}=\sum_{k\ge 0}(I-N)^k$ by the Neumann series.

Since $(DN^{-1}C)T=I$, the map $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$.

Scaled copies $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$ have norms $\|S'\|<3/4$, $\|J'\|<7/8$ and $\|D'\|<1$. With $\|C\|=1$, this makes $A=S'$ and $B_0=D'J'C$ contractions. The three normalizations multiply to $2^{-(2\alpha^2-2)}\cdot 2^{-1}\cdot 2^{-1}=2^{-2\alpha^2}$, so
$$B_0P_tF_tA=2^{-2\alpha^2}DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s,$$
which is the claimed identity.

The constant is a power of two that depends only on $\alpha$, because the only scalar factors are these three normalizations. The $s$- and $t$-dependence lies in $C$, $T$, $D$ and $N$, none of which carries such a factor.
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

Write the answer to `exegenius/tasks/0013-audit-transform-identity.answer.json`, then run `exegenius submit 0013-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
