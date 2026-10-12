# exegenius task 0026-outline

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

Subset-intersection network: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education at introductory depth: discrete mathematics (integers, divisibility, modular arithmetic, gcd and primes, binomial coefficients, induction, the field of two elements with XOR), algorithms (the big-O family, divide-and-conquer recurrences, the RAM and multitape Turing models), calculus (limits, convergence of sequences and series, geometric series, basic integrals), elementary linear algebra over the reals and F_2 (vector spaces, linear maps, rank, dot products, matrix products), and complex numbers with modulus and polar form. The reader has not reached specialist algebra, tensor products, bilinear forms, eigen-theory beyond the basics, analysis (liminf and limsup), or numerical analysis, so the main theorem's proof and its network and transform machinery must be explained.

## Pages, in reading order

- `linear-algebra`: [Linear algebra over a field](linear-algebra.md) — The theory of vector spaces, linear maps, invertible operators, subspaces, and the rank of a linear map. (349 words, used by 2)
- `fixed-tape-machine`: [Fixed-tape machine model](fixed-tape-machine.md) — A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step moves each head by at most one cell. (257 words, used by 1)
- `linear-network`: [Linear network that restores auxiliary values](linear-network.md) — A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state. Needs: linear-algebra, fixed-tape-machine. (474 words, used by 2)
- `frame`: [Frame of a network vertex](frame.md) — An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented. Needs: linear-network. (371 words, used by 1)
- `subset-network`: [Subset-intersection network](subset-network.md) — A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension. Needs: linear-network, linear-algebra, frame. (447 words, used by 0)

## The argument's main steps

- A fixed linear network of three-element-subset gates exchanges the banks $X_a$ and $Y_a$ with signs and restores every scratch wire. Pages: `linear-network`.
- On every route of the network the operator on each role is $D_{\mathrm{sink}}D_{\mathrm{source}}^{-1}$, so only the endpoint frames determine it. Pages: `frame`.
- The subspace labels satisfy $L=Ich$ and the sum of absolute label changes equals $Wm-2N+2L$, with loss $L<N/2$.
- For the bit network the total rational rank $s$ of the edge differences satisfies $s<Wm$.
- For the complex network the total rank of the phase translation factors, $s_{\rm c}$, is strictly below $W_{\rm c}m$.

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

Write the answer to `exegenius/tasks/0026-outline.answer.json`, then run `exegenius submit 0026-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
