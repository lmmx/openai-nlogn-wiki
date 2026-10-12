# exegenius task 0040-outline

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Organise the finished pages of an explanatory wiki into parts, and write its front page. The wiki explains a target result to a specific reader, one concept per page.

- Group the pages into parts that the reader works through in order, each a coherent stage of the explanation (for example: background, the main construction, the analysis). Aim for 3 to 8 parts; a small wiki may need fewer.
- Put every page in exactly one part, or in the glossary. Each page's prerequisites (listed below) must be in the glossary, the same part or an earlier one; submit rejects an outline that breaks this. Pages within a part are shown in reading order automatically, so their order in your list does not matter.
- Glossary: minor pages that define a term in a few sentences rather than explain an idea, such as a short page on a piece of terminology that one or two other pages use. They move to a glossary page, out of the reading order; links to them still work. Keep every page that explains a method, construction, result or argument in a part. Never put the target in the glossary. The word count and the number of pages using each page are listed to help.
- If the argument's main steps are listed below, base the parts on them where the prerequisites allow: a part per main step, with the pages that present its sub-steps, and background parts for the concepts the steps rely on.
- Part titles: 2 to 5 words, plain text, no numbering.
- Part intros: 2 to 4 sentences on what the part covers and why the reader needs it for what comes next. Link pages as `[Name](id.md)`.
- Overview: the front page, 150 to 350 words, for the reader described below. Say what the target result is and why it matters, then the route the wiki takes to it, part by part, naming the key ideas and linking their pages as `[Name](id.md)`. No headings.
- Write for this reader: concrete and specific, with no filler and no rhetorical flourishes. Mathematics in LaTeX ($...$). Links to anything other than the pages listed are rejected; external URLs are allowed.

## Target

Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: discrete mathematics through modular arithmetic, primes, gcds and the Euclidean algorithm, and the binary (radix) representation of integers; a first course in linear algebra over the reals covering vector spaces, bases, dimension, matrices, rank and invertibility; and the basics of complex numbers and roots of unity. They have not studied finite fields beyond GF(2), bilinear forms, tensor products, rings beyond polynomials, or the fast Fourier transform as a specialist topic, so those are explained by the wiki.

## Pages, in reading order

- `exact-integer-multiplication`: [Exact integer multiplication](exact-integer-multiplication.md) — Given binary strings x and y of length n, output the 2n-bit binary representation of their product. (390 words, used by 1)
- `radix-digit-convolution`: [Radix-digit convolution](radix-digit-convolution.md) — Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients. Needs: exact-integer-multiplication. (355 words, used by 1)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two sequences in which indices wrap around modulo the sequence length. (289 words, used by 1)
- `discrete-fourier-transform`: [Discrete Fourier transform](discrete-fourier-transform.md) — The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q. Needs: cyclic-convolution. (281 words, used by 1)
- `operator-norm`: [Operator norm](operator-norm.md) — The norm of a linear map L is the supremum of ‖Lu‖ over vectors u with ‖u‖ ≤ 1, where the vector norm of a complex vector is the largest modulus among its coordinates; a linear contraction is a linear map of norm at most one. (295 words, used by 2)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. Needs: discrete-fourier-transform, radix-digit-convolution, operator-norm. (582 words, used by 1)
- `transform-identity`: [Transform identity with retained permutations](transform-identity.md) — The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts. Needs: gaussian-resampling, operator-norm. (469 words, used by 0)

## The argument's main steps

- The Gaussian identity $TP_sF_s = P_tF_tS$ holds, with $S$ and $T$ Gaussian-weighted maps from length-$s$ to length-$t$ vectors, and the near-identity operator $N = CTD$ is invertible. Pages: `gaussian-resampling`.
- The maps $A=S'$ and $B_0=D'J'C$ are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds.
- The left inverse $DN^{-1}C$ of $TD^{-1}$ applied to the Gaussian identity gives $DN^{-1}CP_tF_tS = P_sF_s$.
- The normalizations $2^{-2\alpha^2}$ give $B_0P_tF_tA = 2^{-2\alpha^2}P_sF_s$, which is the transform identity (33) with the power of two $2^{2\alpha^2}$.

The page bodies are in `exegenius/pages/<id>.md`; read them if the glosses are not enough to write the overview.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Part": {
      "additionalProperties": false,
      "properties": {
        "intro": {
          "description": "What the part covers and why the reader needs it, as markdown.",
          "type": "string"
        },
        "pages": {
          "description": "Ids of the pages in this part.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "title": {
          "description": "Short title, plain text, no numbering.",
          "type": "string"
        }
      },
      "required": [
        "title",
        "intro",
        "pages"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "glossary": {
      "default": [],
      "description": "Ids of minor pages to move to the glossary.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "overview": {
      "description": "The front page, as markdown, with no headings.",
      "type": "string"
    },
    "parts": {
      "description": "The parts, in reading order.",
      "items": {
        "$ref": "#/$defs/Part"
      },
      "type": "array"
    }
  },
  "required": [
    "overview",
    "parts"
  ],
  "title": "OutlineAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0040-outline.answer.json`, then run `exegenius submit 0040-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
