# exegenius task 0036-audit-discrete-fourier-transform

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

## Symbols bound on earlier pages

- $x$ (first input string), bound on `exact-integer-multiplication`: The first of the two binary strings to be multiplied, of length $n$.
- $y$ (second input string), bound on `exact-integer-multiplication`: The second of the two binary strings to be multiplied, of length $n$.
- $k$ (padded output length), bound on `exact-integer-multiplication`: The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
- $b$ (digit bit count), bound on `radix-digit-convolution`: The number of bits in one radix digit.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each integer.
- $l$ (digit index), bound on `radix-digit-convolution`: A second index of the digits of u and v, running from 0 to m-1.
- $j$ (coefficient index), bound on `radix-digit-convolution`: The index of a coefficient of W.
- $a$ (first sequence), bound on `cyclic-convolution`: The first of the two sequences of length q being convolved, with entries a_0 through a_{q-1}.
- $b$ (second sequence), bound on `cyclic-convolution`: The second of the two sequences of length q being convolved, with entries b_0 through b_{q-1}.
- $q$ (sequence length), bound on `cyclic-convolution`: The number of entries in each of the two sequences a and b, and the modulus of the wrap-around.
- $t$ (output index), bound on `cyclic-convolution`: The index of an output entry of the cyclic convolution, running from 0 to q-1.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`discrete-fourier-transform`)

````markdown
# Discrete Fourier transform

The discrete Fourier transform is the linear map that sends a vector of complex values to a vector of the same length, each entry a weighted sum of the inputs with powers of a root of unity as weights. It is the tool behind the [radix-digit convolution](radix-digit-convolution.md) step of the paper's integer multiplication.

Let $q$ be the number of entries in each vector. Here $j$ indexes the output entries and $k$ the input entries, both from $0$ to $q-1$. Let $\omega$ be a primitive $q$-th root of unity, so $\omega^q=1$ and $\omega^j\ne1$ for $0<j<q$.

The transform $F_q$ maps the input vector $x = (x_0,\dots,x_{q-1})$ to the output vector $y = F_q x$, with
$$y_j = \frac{1}{q}\sum_{k=0}^{q-1}\omega^{jk}x_k.$$
Here $x$ and $y$ are these vectors, not the integer inputs above.

The map is invertible, with inverse $x_l=\sum_{j=0}^{q-1}\omega^{-jl}y_j$, where $l$ indexes the entries of $x$ and there is no factor $1/q$. Substituting the formula for $y_j$ gives
$$\sum_{j=0}^{q-1}\omega^{-jl}y_j=\frac{1}{q}\sum_{k=0}^{q-1}x_k\sum_{j=0}^{q-1}\omega^{j(k-l)}.$$
Let $m$ be an integer and consider $\sum_{j=0}^{q-1}\omega^{jm}$. If $q$ divides $m$, every term is $1$ and the sum is $q$. Otherwise $\omega^m\ne1$, since $\omega^m=\omega^{m \bmod q}$ with $0<(m \bmod q)<q$, and $(\omega^m-1)\sum_{j}\omega^{jm}=(\omega^m)^q-1=0$, so the sum is $0$. Since $k$ and $l$ lie in $0,\dots,q-1$, $q$ divides $k-l$ only when $k=l$. The $1/q$ then cancels the $q$ from the sum, leaving $x_l$.

The transform [reduces cyclic convolution](cyclic-convolution.md) to a pointwise product. For vectors $a$ and $b$ of length $q$, put $(a\ast b)_l=\sum_{k=0}^{q-1}a_k\,b_{(l-k)\bmod q}$. For fixed $k$, put $t=(l-k)\bmod q$, which runs over $0,\dots,q-1$ as $l$ does. Since $\omega^{jl}=\omega^{jk}\omega^{jt}$ when $\omega^q=1$,
$$\sum_{l}\omega^{jl}(a\ast b)_l=\sum_{k}a_k\omega^{jk}\sum_{t}b_t\omega^{jt}=q^2(F_qa)_j(F_qb)_j,$$
so $(F_q(a\ast b))_j=q\,(F_qa)_j\,(F_qb)_j$. Applying the inverse to this gives
$$\sum_{j}\omega^{-jl}(F_qa)_j(F_qb)_j=\frac{1}{q}\sum_{j}\omega^{-jl}(F_q(a\ast b))_j=\frac{1}{q}(a\ast b)_l.$$
So transforming, multiplying pointwise and inverting gives the convolution divided by $q$.
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

Write the answer to `exegenius/tasks/0036-audit-discrete-fourier-transform.answer.json`, then run `exegenius submit 0036-audit-discrete-fourier-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
