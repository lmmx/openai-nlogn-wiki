# exegenius task 0051-outline

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

## Pages, in reading order

- `exact-integer-multiplication`: [Exact integer multiplication](exact-integer-multiplication.md) — Given binary strings x and y of length n, output the 2n-bit binary representation of their product. (293 words, used by 1)
- `linear-map`: [Linear map](linear-map.md) — A map between vectors of numbers that preserves addition and scalar multiplication, so that each output coordinate is a fixed weighted sum of the input coordinates. (219 words, used by 4)
- `discrete-fourier-transform`: [Discrete Fourier transform](discrete-fourier-transform.md) — The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q. Needs: linear-map. (292 words, used by 3)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two sequences in which indices wrap around modulo the sequence length. (271 words, used by 2)
- `coprime-integers`: [Coprime integers](coprime-integers.md) — Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime. Needs: cyclic-convolution. (192 words, used by 2)
- `modular-arithmetic`: [Modular arithmetic](modular-arithmetic.md) — Arithmetic in which values are reduced to their remainders on division by a fixed modulus q, so that index positions wrap around after q. (160 words, used by 1)
- `operator-norm`: [Operator norm](operator-norm.md) — For a linear map, the largest factor by which it stretches a vector measured in a fixed norm, taken over all vectors of norm at most one. Needs: linear-map. (275 words, used by 1)
- `tensor-product`: [Tensor product](tensor-product.md) — The product of two linear maps or arrays acting on separate coordinates, so that applying the product acts on each coordinate in turn. Needs: linear-map. (197 words, used by 2)
- `convolution-theorem`: [Convolution theorem](convolution-theorem.md) — The fact that the transform of a convolution of two sequences is the pointwise product of their transforms. Needs: discrete-fourier-transform, cyclic-convolution. (215 words, used by 1)
- `gaussian-function`: [Gaussian function](gaussian-function.md) — The bell-shaped function x ↦ e^(−x²), or a scaled and shifted copy of it, used as a smooth weight that decays rapidly away from its centre. (259 words, used by 1)
- `transform`: [Transform](transform.md) — A linear map from one array of values to another array of the same kind, each output being a fixed weighted sum of the inputs, such as a discrete Fourier transform. Needs: linear-map. (169 words, used by 1)
- `axis-length`: [Axis length](axis-length.md) — The number of positions along one coordinate axis of a multidimensional array; a multidimensional transform is applied along each axis in turn, with its own length. Needs: tensor-product, transform. (203 words, used by 1)
- `radix-digit-convolution`: [Radix-digit convolution](radix-digit-convolution.md) — Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients. Needs: exact-integer-multiplication, discrete-fourier-transform, axis-length. (408 words, used by 1)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. Needs: discrete-fourier-transform, radix-digit-convolution, coprime-integers, modular-arithmetic, operator-norm, gaussian-function. (502 words, used by 1)
- `transform-identity`: [Transform identity with retained permutations](transform-identity.md) — The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts. Needs: gaussian-resampling, coprime-integers, tensor-product, convolution-theorem. (315 words, used by 0)

## The argument's main steps

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. Pages: `gaussian-resampling`.
- $RF_s=2^{2d\alpha^2}B_0QF_tA$: the one-dimensional identity tensors into the identity with permutations $R$ and $Q$ kept.
- $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$, so the source permutation cancels across the convolution.

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

Write the answer to `exegenius/tasks/0051-outline.answer.json`, then run `exegenius submit 0051-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
