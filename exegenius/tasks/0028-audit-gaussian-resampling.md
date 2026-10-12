# exegenius task 0028-audit-gaussian-resampling

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
- Cyclic convolution (also: convolution of two vectors)
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
- Operator norm (also: norm of a linear map, operator norm and maximum-modulus vector norm)

## Symbols bound on earlier pages

- $s$ (binary string), bound on `exact-integer-multiplication`: A generic binary string whose integer value is taken by the function val.
- $k$ (padded output length), bound on `exact-integer-multiplication`: The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
- $b$ (digit bit count), bound on `radix-digit-convolution`: The number of bits in one radix digit.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each integer.
- $u$ (first integer), bound on `radix-digit-convolution`: The integer whose i-th digit is u_i.
- $u_i$ (digit of u), bound on `radix-digit-convolution`: The i-th digit of u, in the set $\{0,\dots,2^b-1\}$.
- $i$ (digit index), bound on `radix-digit-convolution`: An index of the digits of u and v, running from 0 to m-1.
- $j$ (coefficient index), bound on `radix-digit-convolution`: The index of a coefficient of W.
- $b$ (second sequence), bound on `cyclic-convolution`: The second of the two input sequences, with entries $b_0, \dots, b_{q-1}$.
- $i$ (summation index), bound on `cyclic-convolution`: The index of the terms in the sum that defines each output entry.
- $t$ (output index), bound on `cyclic-convolution`: The index of the output entry $c_t$.
- $j$ (output index), bound on `discrete-fourier-transform`: The index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on `discrete-fourier-transform`: The index of an input entry, running from $0$ to $q-1$.
- $m$ (integer exponent), bound on `discrete-fourier-transform`: An integer exponent in a sum of powers of $\omega$.
- $b$ (second vector), bound on `discrete-fourier-transform`: The second vector of the convolution, of length $q$.
- $t$ (shifted index), bound on `discrete-fourier-transform`: The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. It replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by such transforms. (cited)

Let $s$ and $t$ be the numbers of coordinates of source and target vectors, with $\gcd(s,t)=1$ and $\theta=t/s-1$, the relative gap between the lengths. Here $u$ is a length-$s$ source vector, $b$ a length-$t$ target vector, and $j$ and $k$ index their entries. Let $F_s$ and $P_s$ be the normalized Fourier transform and the coordinate permutation $(P_su)_j=u_{tj}$ on length-$s$ vectors, and let $F_t$ and $P_t$ be the same on length-$t$ vectors with $(P_tb)_k=b_{-sk}$.

$S$ and $T$ are Gaussian-weighted maps from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of their weights, which are bell-shaped functions that decay quickly away from their centres. $S$ gathers the entries of $u$ near $sk/t$, and $T$ spreads each $u_j$ over the targets near $tj/s$:
$$(Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$
where $u_j=u_{j \bmod s}$.

For $0\le j<s$, let $\ell_j$ be the integer nearest $tj/s$, ties rounded up, and $\beta_j=tj/s-\ell_j$. Let $C$ select coordinates, $(Cb)_j=b_{\ell_j}$, let $D$ be diagonal with $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$. Expanding,
$$(Nu)_j=\sum_{i\in\mathbb Z}e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i,$$
where $i$ is a summation index over all integers and $\beta_i$ depends only on $i \bmod s$. The term $i=j$ has $ti/s-\ell_j=\beta_j$, so its exponentials cancel and it equals $u_j$. The other terms form $N-I$, whose size is measured in the [operator norm](operator-norm.md) for the maximum-modulus vector norm.

These other terms are small. Harvey and van der Hoeven bound them by $2^{-\alpha^2\theta}$, which shrinks as $\theta$ grows. (cited) Here $p$ is the integer precision of the cited lemma. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, the bound is below $1/2$, as $\alpha^2\theta>p/\alpha^2>1$.

Write $N=I-E$, where $E=I-N$ is the error, and $\|E\|<1/2$. The Neumann series $\sum_{m\ge0}E^m$, with $m$ its summation index, has partial sums of norm at most $1/(1-\|E\|)<2$, since $\|E^m\|\le\|E\|^m$. Here $M$ is the last index of the partial sum $\sum_{m=0}^{M}E^m$, which multiplied by $I-E$ telescopes to $I-E^{M+1}$. Since $\|E^{M+1}\|\to0$, the series sums to $N^{-1}$, whose norm is less than $2$.

The Gaussian identity $TP_sF_s=P_tF_tS$ rests on Poisson summation: a sum of Gaussians over the integers is a Fourier series whose coefficients are Gaussians of reciprocal width. The weights in $S$ have Fourier transform constant $\alpha$, which cancels the $1/\alpha$ in $S$. The full bookkeeping is in Harvey and van der Hoeven, (cited).

Multiply $TP_sF_s=P_tF_tS$ on the left by $C$, and use $CT=ND^{-1}$, which holds since $D$ is invertible. This gives $ND^{-1}P_sF_s=CP_tF_tS$. Multiplying on the left by $N^{-1}$ and then by $D$ gives $P_sF_s=DN^{-1}C\,P_tF_tS$. This has the form $P_sF_s=BP_tF_tA$, where $A=S$ and $B=DN^{-1}C$ are maps. It is the form used on the [transform identity with retained permutations](transform-identity.md) page.
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

Write the answer to `exegenius/tasks/0028-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0028-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
