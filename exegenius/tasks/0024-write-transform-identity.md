# exegenius task 0024-write-transform-identity

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Axis length
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)
- Operator norm (also: norm of a linear map)
- Tensor product

## This page

Concept: Transform identity with retained permutations
Gloss: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## This page in the argument

The step: The Gaussian resampling identity $RF_s=2^{2d\alpha^2}B_0QF_tA$ holds with the permutations $R$ and $Q$ kept in the formula, and the source permutation $R$ cancels across a convolution: $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$.
How: prove the one-dimensional identity with both permutations kept, lift it to a tensor product, then cancel the source permutation in a convolution
Why: Retaining the two permutations in the formula avoids executing each of them as a separate full sort on every coordinate. (the sources say so: "Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly." (paper))

Its sub-steps, in order:

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))
- $RF_s=2^{2d\alpha^2}B_0QF_tA$: the one-dimensional identity tensors into the identity with permutations $R$ and $Q$ kept.
- $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$, so the source permutation cancels across the convolution.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of values in the vector, which is the count of entries the transform acts on.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive q-th root of unity, a complex number whose powers are the weights of the transform.
- $F_q$ (transform map), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The normalized discrete Fourier transform of length q, mapping a vector of q values to a vector of q values.
- $j$ (input position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry, running from 0 to q-1.
- $k$ (output position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry, running from 0 to q-1.
- $F_q^+$ (opposite transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of length q that uses the root omega inverse in place of omega.
- $B$ (radix), bound on [Radix-digit convolution](radix-digit-convolution.md): The base $2^k$ in which each integer is written.
- $d$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits of each input.
- $x$ (first input), bound on [Radix-digit convolution](radix-digit-convolution.md): The first of the two inputs, a nonnegative integer below $B^d$.
- $y$ (second input), bound on [Radix-digit convolution](radix-digit-convolution.md): The second of the two inputs, a nonnegative integer below $B^d$.
- $a$ (coefficient list of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The list of radix digits $(a_0, \dots, a_{d-1})$ of $x$, from least significant to most significant.
- $b$ (coefficient list of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The list of radix digits of $y$, written in the same way as $a$.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): The variable of the polynomials whose coefficients are digit lists.
- $c$ (convolution), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial convolution of $a$ and $b$, whose coefficient $c_m$ sums the products $a_i b_j$ with $i+j=m$.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of the source vector, which is the length of the source transform.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of the target vector, which is the length of the target transform.
- $F_s$ (source transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length $s$.
- $F_t$ (target transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform of length $t$.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on length-$s$ vectors that sends $u$ to the vector with entries $u_{tj}$.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on length-$t$ vectors that sends $v$ to the vector with entries $v_{-sk}$.
- $\theta$ (length excess), bound on [Gaussian resampling](gaussian-resampling.md): The relative excess $t/s-1$ of the target length over the source length.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): The integer width of the Gaussians used in the maps, with $\alpha \ge 2$.
- $p$ (precision), bound on [Gaussian resampling](gaussian-resampling.md): The integer precision of the numerical approximation.
- $S$ (source-to-target Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian map from length-$s$ vectors to length-$t$ vectors defined by $(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$.
- $T$ (second Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The Gaussian map from length-$s$ vectors to length-$t$ vectors defined by $(Tu)_k=\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{2}(tj/s-k)^2}u_j$.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-$t$ vectors to length-$s$ vectors that picks out, for each $j$, the entry at the integer nearest to $tj/s$.
- $D$ (diagonal correction), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map on length-$s$ vectors that multiplies entry $j$ by the reciprocal of the Gaussian factor at the entry that $C$ selects.
- $N$ (correction map), bound on [Gaussian resampling](gaussian-resampling.md): The map $CTD$ on length-$s$ vectors, which is close to the identity.
- $A$ (source contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $S/2$ from length-$s$ vectors to length-$t$ vectors.
- $B_0$ (target contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $2^{-(2\alpha^2-2)}DN^{-1}C/2$ from length-$t$ vectors to length-$s$ vectors.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Transform identity with retained permutations *<predicate>* Gaussian resampling
- [Coprime integers](coprime-integers.md): Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime.
  Shown as: Transform identity with retained permutations *<predicate>* Coprime integers
- [Tensor product](tensor-product.md): The product of two linear maps or arrays acting on separate coordinates, so that applying the product acts on each coordinate in turn.
  Shown as: Transform identity with retained permutations *<predicate>* Tensor product

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Axis length](axis-length.md)
- [Linear map](linear-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)

## Evidence from the sources, with the paragraph around each quote

- "We retain both permutations in the transform formula" (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows. For an integer q ≥ 1, write q−1


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Lifting to $d$ coordinates is a tensor product: each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$." (The page presents the lifted identity RF_s=2^{2d\alpha^2}B_0QF_tA as following from the one-dimensional identity, but the reader cannot check how a tensor product of the transforms and permutations gives it.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "What remains is the untwisted product, which gives the convolution up to scale:" (The reader cannot check from the page that the pointwise product of the untwisted transforms equals the convolution divided by the square of the product of the lengths.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "$(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$" (Nothing on the page or earlier pages says what the input vector u denotes; the page only uses it.)
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "$(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$" (Nothing on the page or earlier pages says what the input vector v denotes; the page only uses it.)
- "coprime" is the concept [Coprime integers](coprime-integers.md), now a prerequisite: link it where the term is used.
- "tensor product" is the concept [Tensor product](tensor-product.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 199 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 249 words. Pages that grow with every repair stop being self-contained explanations of one concept.

Transform identity with retained permutations keeps the source and target coordinate permutations inside the Gaussian resampling identity, so that they cancel across a convolution instead of being executed as sorts. It is the form of the identity used for exact integer multiplication.

The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md): for coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$. Here $P_s$ and $P_t$ are the permutations of that identity.

Here $d$ is the number of coordinates, and $s_i$ is the length of coordinate $i$. Lifting to $d$ coordinates is a tensor product: each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$. $R$ permutes the source coordinates, and $Q$ permutes the target coordinates. The lifted identity is
$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Let $F_s^+$ and $R^+$ be the inverses of $F_s$ and $R$, so that $RF_s^+$ is the inverse of $RF_s$ and equals $F_s^+R^+$. The symbol $\cdot$ denotes the pointwise product and $*$ denotes convolution. A permutation commutes with the pointwise product, $R(x)\cdot R(y)=R(x\cdot y)$, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$. Applying $F_s^+R^+$ removes the outer $R$, because $R^+R$ is the identity. What remains is the untwisted product, which gives the convolution up to scale:
$$(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}.$$
So the source permutation $R$ never has to be executed.

Sorting is avoided because the usual implementation sorts twice on each coordinate, while this formula is computed directly. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0024-write-transform-identity.answer.md` and the JSON to `exegenius/tasks/0024-write-transform-identity.answer.json`, then run `exegenius submit 0024-write-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
