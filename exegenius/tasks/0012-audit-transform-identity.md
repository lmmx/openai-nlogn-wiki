# exegenius task 0012-audit-transform-identity

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
- Discrete Fourier transform (also: normalized Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)

## Symbols bound on earlier pages

- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length $n$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length $n$.
- $B$ (radix), bound on `radix-digit-convolution`: The base $2^k$ in which each integer is written.
- $d$ (digit count), bound on `radix-digit-convolution`: The number of radix digits of each input.
- $x$ (first input), bound on `radix-digit-convolution`: The first of the two inputs, a nonnegative integer below $B^d$.
- $y$ (second input), bound on `radix-digit-convolution`: The second of the two inputs, a nonnegative integer below $B^d$.
- $s$ (source length), bound on `gaussian-resampling`: The number of coordinates of the source vector, which is the length of the source transform.
- $t$ (target length), bound on `gaussian-resampling`: The number of coordinates of the target vector, which is the length of the target transform.
- $F_s$ (source transform), bound on `gaussian-resampling`: The normalized Fourier transform of length $s$.
- $F_t$ (target transform), bound on `gaussian-resampling`: The normalized Fourier transform of length $t$.
- $P_s$ (source permutation), bound on `gaussian-resampling`: The coordinate permutation on length-$s$ vectors that sends $u$ to the vector with entries $u_{tj}$.
- $P_t$ (target permutation), bound on `gaussian-resampling`: The coordinate permutation on length-$t$ vectors that sends $v$ to the vector with entries $v_{-sk}$.
- $\theta$ (length excess), bound on `gaussian-resampling`: The relative excess $t/s-1$ of the target length over the source length.
- $\alpha$ (Gaussian width), bound on `gaussian-resampling`: The integer width of the Gaussians used in the maps, with $\alpha \ge 2$.
- $A$ (source contraction), bound on `gaussian-resampling`: The contraction $S/2$ from length-$s$ vectors to length-$t$ vectors.
- $B_0$ (target contraction), bound on `gaussian-resampling`: The contraction $2^{-(2\alpha^2-2)}DN^{-1}C/2$ from length-$t$ vectors to length-$s$ vectors.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`transform-identity`)

````markdown
# Transform identity with retained permutations

Transform identity with retained permutations keeps the source and target coordinate permutations inside the Gaussian resampling identity, so that they cancel across a convolution instead of being executed as sorts. It is the form of the identity used for exact integer multiplication.

The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md): for coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$. Here $P_s$ and $P_t$ are the permutations of that identity.

Here $d$ is the number of coordinates, and $s_i$ is the length of coordinate $i$. Lifting to $d$ coordinates is a tensor product: each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$. $R$ permutes the source coordinates, and $Q$ permutes the target coordinates. The lifted identity is
$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Let $F_s^+$ and $R^+$ be the inverses of $F_s$ and $R$, so that $RF_s^+$ is the inverse of $RF_s$ and equals $F_s^+R^+$. The symbol $\cdot$ denotes the pointwise product and $*$ denotes convolution. A permutation commutes with the pointwise product, $R(x)\cdot R(y)=R(x\cdot y)$, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$. Applying $F_s^+R^+$ removes the outer $R$, because $R^+R$ is the identity. What remains is the untwisted product, which gives the convolution up to scale:
$$(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}.$$
So the source permutation $R$ never has to be executed.

Sorting is avoided because the usual implementation sorts twice on each coordinate, while this formula is computed directly. (cited).
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

Write the answer to `exegenius/tasks/0012-audit-transform-identity.answer.json`, then run `exegenius submit 0012-audit-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
