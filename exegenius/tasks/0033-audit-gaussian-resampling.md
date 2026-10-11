# exegenius task 0033-audit-gaussian-resampling

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

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source, which the reader can consult: it is followable by reference, so do not report it as a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, Fourier transform)
- Axis length
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)
- Operator norm (also: norm of a linear map)

## Symbols bound on earlier pages

- $m$ (input length), bound on `linear-map`: The number of input coordinates of a linear map.
- $k$ (output length), bound on `linear-map`: The number of output coordinates of a linear map.
- $u$ (input vector), bound on `linear-map`: The vector of m complex numbers that a linear map takes as input.
- $v$ (output vector), bound on `linear-map`: The vector of k complex numbers that a linear map returns.
- $u_j$ (input coordinate), bound on `linear-map`: The j-th coordinate of the input vector.
- $m$ (exponent), bound on `discrete-fourier-transform`: An integer exponent of $\omega$, with $0<m<q$.
- $j$ (input position), bound on `discrete-fourier-transform`: The position of an input value, running from $0$ to $q-1$.
- $k$ (output position), bound on `discrete-fourier-transform`: The position of an output value, running from $0$ to $q-1$.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ values.
- $v$ (second vector), bound on `discrete-fourier-transform`: A second vector of $q$ values, for forming a convolution.
- $B$ (radix), bound on `radix-digit-convolution`: The base in which each integer is written, equal to 2^k.
- $k$ (bits per digit), bound on `radix-digit-convolution`: The number of bits in each radix digit, so that the radix is 2^k.
- $u$ (test vector), bound on `operator-norm`: A vector whose length matches the input length of the map, over which the supremum is taken.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Axis length](axis-length.md)
- [Linear map](linear-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Coprime integers](coprime-integers.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor product](tensor-product.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling is an identity that replaces the [Discrete Fourier transform](discrete-fourier-transform.md) of an arbitrary length by transforms whose lengths are powers of two. It serves the [Radix-digit convolution](radix-digit-convolution.md) of digit vectors, which needs such transforms. (cited)

The identity is restricted to [coprime integers](coprime-integers.md) $s<t$, where $s$ is the number of coordinates of the source vector and $t$ the number of coordinates of the target. Let $\theta = t/s-1$ be the relative excess of $t$ over $s$. The identity needs $\theta > p/\alpha^4$, where $\alpha \ge 2$ is an integer Gaussian width (a larger $\alpha$ gives wider weights below) and $p$ is the integer precision of the numerical approximation.

Here $u$ is a vector of $s$ coordinates and $v$ a vector of $t$ coordinates. Its permutations $P_s$ and $P_t$ are defined using [modular arithmetic](modular-arithmetic.md) on their indices: $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$.

$S$ maps vectors of $s$ coordinates to vectors of $t$ coordinates by $(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$, and $T$ maps them by $(Tu)_k=\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{2}(tj/s-k)^2}u_j$. Subscripts of vectors are taken modulo their length. Harvey and van der Hoeven prove the Gaussian identity $TP_sF_s = P_tF_tS$: transforming on the source grid and then applying $T$ agrees with applying $S$ and then transforming on the target grid.

$C$ selects, for each $j<s$, the entry of a length-$t$ vector at $m_j$, the integer nearest to $tj/s$. $D$ is the diagonal map $(Du)_j = e^{\pi\alpha^2(tj/s-m_j)^2}u_j$ on length-$s$ vectors, which cancels the Gaussian factor of $T$ at that entry. Put $N = CTD$, the correction map on length-$s$ vectors. Its $j$th entry is $u_j$ plus other terms, so $N$ is close to the identity.

Here $I$ is the identity map, which leaves every vector unchanged. The size of $N-I$ is measured by its [operator norm](operator-norm.md), $\|N-I\|$, and the sources bound it by $2^{-\alpha^2\theta}$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$. Then $N$ is invertible by the Neumann series $N^{-1}=\sum_{k\ge 0}(I-N)^k$, whose $k$th term has norm at most $2^{-k}$, so the series converges.

Because $CT = ND^{-1}$, the map $DN^{-1}C$ is a left inverse of $T$, since $(DN^{-1}C)T = I$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS = P_sF_s$. The two Gaussian maps relate the two frequency grids, and this inverse turns the identity into one for $P_sF_s$ alone.

Write $D'=2^{-(2\alpha^2-2)}D$ for the scaled diagonal map. Set $A = S/2$ and $B_0 = 2^{-(2\alpha^2-2)}DN^{-1}C/2$, where $A$ maps length-$s$ vectors to length-$t$ vectors and $B_0$ maps back. Both are contractions, that is, linear maps of norm at most one. The sources bound $\|S/2\|<3/4$, $\|N^{-1}/2\|<7/8$ and $\|D'\|<1$ (cited), and $\|C\|=1$ because $C$ only copies entries. So $\|A\|<3/4$ and $\|B_0\|<7/8$.

The scalars $2^{-(2\alpha^2-2)}$, $\tfrac12$ and $\tfrac12$ multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA = 2^{-2\alpha^2}P_sF_s$. This is the one-dimensional identity, and $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$. The constant $2^{2\alpha^2}$ is uniform because the norm bounds $3/4$, $7/8$ and $1$ are fixed numbers, and $\alpha$ enters only through the normalization $2^{-(2\alpha^2-2)}$ of $D$, which the constant cancels. (cited)
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

Write the answer to `exegenius/tasks/0033-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0033-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
