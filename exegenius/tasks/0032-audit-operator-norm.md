# exegenius task 0032-audit-operator-norm

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

## Symbols bound on earlier pages

- $L$ (linear map), bound on `linear-map`: The rule sending a vector of m complex numbers to a vector of k complex numbers.
- $u$ (input vector), bound on `linear-map`: The vector of m complex numbers that a linear map takes as input.
- $q$ (vector length), bound on `discrete-fourier-transform`: The number of values in each vector.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of $q$ values.
- $F_q$ (transform map), bound on `discrete-fourier-transform`: The map sending a vector of $q$ values to its normalized transform.
- $B$ (radix), bound on `radix-digit-convolution`: The base in which each integer is written, equal to 2^k.

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

## Page to audit (`operator-norm`)

````markdown
# Operator norm

The operator norm measures how much a linear map can enlarge a vector. It gives each map a single number, which lets a bound on one step of a computation carry over to the next. Here $L$ denotes a [linear map](linear-map.md). The operator norm is defined for any [linear map](linear-map.md), and it is the largest factor by which $L$ stretches a vector.

The variable $u$ denotes a vector whose length matches the input length of $L$. The norm of $u$ is the largest modulus (absolute value) among its coordinates, and operator norms are taken with respect to this norm. (cited). Then

$$\|L\| = \sup_{\|u\| \le 1} \|Lu\|,$$

where $\sup$ is the supremum, the least upper bound of the values $\|Lu\|$ over all $u$ with $\|u\| \le 1$.

For example, let $L$ send $(u_0, u_1)$ to $(u_0+u_1,\ u_0-u_1)$. If every coordinate of $u$ has modulus at most one, each output coordinate has modulus at most $2$, and $u=(1,1)$ gives $Lu=(2,0)$. Hence $\|L\|=2$.

A map with $\|L\| \le 1$ never increases the norm of a vector, and is called a contraction. The normalized Fourier transform $F_q$ is one, because (cited).

Operator norms also bound compositions: $\|LM\| \le \|L\|\,\|M\|$, so the norm of a product of maps is at most the product of their norms. On the [Gaussian resampling](gaussian-resampling.md) page, the factors $A$ and $B_0$ are contractions, so they cannot increase the norm of what they are applied to.
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

Write the answer to `exegenius/tasks/0032-audit-operator-norm.answer.json`, then run `exegenius submit 0032-audit-operator-norm` in the project directory. If submit rejects the answer, fix the answer and submit again.
