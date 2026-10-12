# exegenius task 0039-audit-transform-identity

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
- Operator norm (also: norm of a linear map, operator norm and maximum-modulus vector norm)

## Symbols bound on earlier pages

- $s$ (binary string), bound on `exact-integer-multiplication`: A generic binary string whose integer value is taken by the function val.
- $k$ (padded output length), bound on `exact-integer-multiplication`: The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
- $u$ (first integer), bound on `radix-digit-convolution`: The integer whose i-th digit is u_i.
- $v$ (second integer), bound on `radix-digit-convolution`: The integer whose i-th digit is v_i.
- $j$ (coefficient index), bound on `radix-digit-convolution`: The index of a coefficient of W.
- $t$ (output index), bound on `cyclic-convolution`: The index of an output entry of the cyclic convolution, running from 0 to q-1.
- $j$ (output index), bound on `discrete-fourier-transform`: The index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on `discrete-fourier-transform`: The index of an input entry, running from $0$ to $q-1$.
- $t$ (shifted index), bound on `discrete-fourier-transform`: The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.
- $S'$ (scaled Gaussian map), bound on `operator-norm`: Half of a Gaussian resampling map, used as the map A.
- $J'$ (scaled inverse map), bound on `operator-norm`: Half the inverse of an invertible map close to the identity.
- $D'$ (scaled diagonal map), bound on `operator-norm`: A diagonal map scaled by a fixed factor at most one.
- $C$ (coordinate selection), bound on `operator-norm`: A map that selects some coordinates of its input vector, so that each output entry copies one input entry.
- $s$ (source length), bound on `gaussian-resampling`: The number of entries in each source vector, the length of the source vectors.
- $t$ (target length), bound on `gaussian-resampling`: The number of entries in each target vector, the length of the target vectors.
- $\theta$ (relative gap), bound on `gaussian-resampling`: The relative gap $t/s-1$ between the target and source lengths.
- $u$ (source vector), bound on `gaussian-resampling`: A length-s vector, the input of the maps S, T and N.
- $j$ (source entry index), bound on `gaussian-resampling`: The index of an entry of a source vector, which is read modulo s.
- $k$ (target entry index), bound on `gaussian-resampling`: The index of an entry of a target vector.
- $F_s$ (source transform), bound on `gaussian-resampling`: The normalized Fourier transform on length-s vectors.
- $P_s$ (source permutation), bound on `gaussian-resampling`: The coordinate permutation $(P_su)_j=u_{tj}$ on length-s vectors.
- $F_t$ (target transform), bound on `gaussian-resampling`: The normalized Fourier transform on length-t vectors.
- $P_t$ (target permutation), bound on `gaussian-resampling`: The coordinate permutation $(P_tb)_k=b_{-sk}$ on length-t vectors.
- $S$ (source-to-target weights), bound on `gaussian-resampling`: The Gaussian-weighted map from length-s to length-t vectors defined by $(Su)_k$.
- $T$ (target-spreading map), bound on `gaussian-resampling`: The Gaussian-weighted map from length-s to length-t vectors defined by $(Tu)_k$.
- $\alpha$ (weight width parameter), bound on `gaussian-resampling`: The integer parameter that sets the width of the Gaussian weights.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map that selects the coordinates $\ell_j$ of a length-t vector.
- $D$ (diagonal factor), bound on `gaussian-resampling`: The diagonal map with entries $e^{\pi\alpha^2\beta_j^2}$ on length-s vectors.
- $N$ (near-identity operator), bound on `gaussian-resampling`: The map $N=CTD$ on length-s vectors, whose error from the identity is small.
- $I$ (identity map), bound on `gaussian-resampling`: The identity map on length-s vectors.
- $A$ (source contraction map), bound on `gaussian-resampling`: The map A=S from length-s to length-t vectors in the factored identity.
- $B$ (target contraction map), bound on `gaussian-resampling`: The map $B=DN^{-1}C$ from length-t to length-s vectors in the factored identity.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which both coordinate permutations $P_s$ and $P_t$ stay as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula avoids those sorts and lets them cancel across a convolution. The paper makes this choice explicitly (cited)

Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. Here $v$ is a generic length-$t$ vector, not the second integer of radix-digit convolution. The permutations are $(P_su)_j=u_{tj}$ for a length-$s$ vector $u$, and $(P_tv)_k=v_{-sk}$ for a length-$t$ vector $v$, with subscripts taken modulo $s$ and $t$. The identity is
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
where $A$ is a linear map from length-$s$ to length-$t$ vectors and $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The letters $A$ and $B_0$ mean these new maps here, not the $A=S$ and $B=DN^{-1}C$ of the Gaussian resampling page. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm. The claim is stated in (cited).

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
$$TP_sF_s=P_tF_tS.$$
It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. Prior work establishes it, with the proof in (cited), and it applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$.

Let $I$ denote the identity map. The operator $N=CTD$ is close to $I$: the inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$ (cited), which is below $1/2$ because $\alpha^2\theta>1$. (cited) The Neumann series is the matrix analogue of the geometric series, and it converges when $\|I-N\|<1$.

The scaled maps are $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$. Set $A=S'$ and $B_0=D'J'C$, where $C$ is the selection map from the Gaussian resampling page. (cited)

Since $N=CTD$ and $D$ is invertible, $CT=ND^{-1}$. Hence $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$, so $DN^{-1}C$ is a left inverse of $T$, meaning it maps $T$ back to the identity. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$. Therefore
$$B_0P_tF_tA=D'J'C\,P_tF_t\,S'=2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s.$$

The constant $2^{2\alpha^2}$ depends only on $\alpha$. The only scalar factors are the three normalizations, whose product is $2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12=2^{-2\alpha^2}$. The Gaussian weights, the factor $1/\alpha$ in $S$, and the lengths $s$ and $t$ sit inside the maps, so they do not appear in the constant.
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

Write the answer to `exegenius/tasks/0039-audit-transform-identity.answer.json`, then run `exegenius submit 0039-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
