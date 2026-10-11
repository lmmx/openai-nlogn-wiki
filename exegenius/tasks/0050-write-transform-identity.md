# exegenius task 0050-write-transform-identity

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
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Axis length
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)
- Operator norm (also: norm of a linear map)
- Tensor product
- Convolution theorem
- Gaussian function (also: Gaussian weight, Gaussian (weight or function))
- Transform

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
- $m$ (input length), bound on [Linear map](linear-map.md): The number of input coordinates of a linear map.
- $k$ (output length), bound on [Linear map](linear-map.md): The number of output coordinates of a linear map.
- $L$ (linear map), bound on [Linear map](linear-map.md): The rule sending a vector of m complex numbers to a vector of k complex numbers.
- $u$ (input vector), bound on [Linear map](linear-map.md): The vector of m complex numbers that a linear map takes as input.
- $v$ (output vector), bound on [Linear map](linear-map.md): The vector of k complex numbers that a linear map returns.
- $u_j$ (input coordinate), bound on [Linear map](linear-map.md): The j-th coordinate of the input vector.
- $v_i$ (output coordinate), bound on [Linear map](linear-map.md): The i-th coordinate of the output vector.
- $a_{ij}$ (weight), bound on [Linear map](linear-map.md): The fixed complex number by which output i multiplies input j.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of values in each vector.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, with $\omega^q=1$.
- $m$ (exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent of $\omega$, with $0<m<q$.
- $j$ (input position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The position of an input value, running from $0$ to $q-1$.
- $k$ (output position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The position of an output value, running from $0$ to $q-1$.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ values.
- $F_q$ (transform map), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of $q$ values to its normalized transform.
- $F_q^+$ (opposite transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform with $\omega^{-1}$ in place of $\omega$.
- $v$ (second vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A second vector of $q$ values, for forming a convolution.
- $L$ (linear map), bound on [Operator norm](operator-norm.md): The linear map whose stretching of vectors the operator norm measures.
- $u$ (test vector), bound on [Operator norm](operator-norm.md): A vector whose length matches the input length of the map, over which the supremum is taken.
- $L$ (first map), bound on [Tensor product](tensor-product.md): A linear map on vectors of length $s$.
- $M$ (second map), bound on [Tensor product](tensor-product.md): A linear map on vectors of length $t$.
- $\otimes$ (tensor product), bound on [Tensor product](tensor-product.md): The operator that combines $L$ and $M$ into a linear map on arrays with $s$ rows and $t$ columns.
- $u$ (array), bound on [Tensor product](tensor-product.md): An array with $s$ rows and $t$ columns, whose entries are $u_{hg}$.
- $i$ (output row index), bound on [Tensor product](tensor-product.md): The index of an output row, which is the first coordinate of an output position.
- $m$ (output column index), bound on [Tensor product](tensor-product.md): The index of an output column, which is the second coordinate of an output position.
- $h$ (input row index), bound on [Tensor product](tensor-product.md): The index of an input row of the array $u$.
- $g$ (input column index), bound on [Tensor product](tensor-product.md): The index of an input column of the array $u$.
- $\ell_1$ (first axis length), bound on [Axis length](axis-length.md): The number of positions along the first axis of a two-dimensional array, a count.
- $\ell_2$ (second axis length), bound on [Axis length](axis-length.md): The number of positions along the second axis of a two-dimensional array, a count.
- $B$ (radix), bound on [Radix-digit convolution](radix-digit-convolution.md): The base in which each integer is written, equal to 2^k.
- $k$ (bits per digit), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in each radix digit, so that the radix is 2^k.
- $d$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of radix digits of each input.
- $a$ (digit list of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient list of x, the vector of its d radix digits a_0 through a_{d-1}.
- $z$ (formal variable), bound on [Radix-digit convolution](radix-digit-convolution.md): A placeholder variable for the powers of a polynomial.
- $b$ (digit list of y), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient list of y, the vector of its d radix digits.
- $c$ (convolution), bound on [Radix-digit convolution](radix-digit-convolution.md): The convolution of the coefficient lists a and b, whose entries c_m are sums of products of digits.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of the source vector, a count.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of coordinates of the target vector, a count.
- $\theta$ (relative excess), bound on [Gaussian resampling](gaussian-resampling.md): The relative excess $t/s-1$ of the target length over the source length.
- $u$ (source vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of $s$ coordinates.
- $v$ (target vector), bound on [Gaussian resampling](gaussian-resampling.md): A vector of $t$ coordinates.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on length-$s$ vectors with $(P_s u)_j = u_{tj}$.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation on length-$t$ vectors with $(P_t v)_k = v_{-sk}$.
- $p$ (precision), bound on [Gaussian resampling](gaussian-resampling.md): The integer precision of the numerical approximation.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): An integer at least 2 setting the width of the Gaussian weights.
- $S$ (Gaussian map S), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-$s$ to length-$t$ vectors with Gaussian weights $e^{-\pi\alpha^{-2}(j-sk/t)^2}$.
- $T$ (Gaussian map T), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-$s$ to length-$t$ vectors with Gaussian weights $e^{-\pi\alpha^{2}(tj/s-k)^2}$.
- $m_j$ (nearest target index), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest to $tj/s$, for each $j<s$.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): The map selecting, for each $j<s$, the entry of a length-$t$ vector at $m_j$.
- $D$ (correction diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map on length-$s$ vectors that cancels the Gaussian factor of $T$ at the selected entry.
- $N$ (correction map), bound on [Gaussian resampling](gaussian-resampling.md): The map $CTD$ on length-$s$ vectors, close to the identity.
- $I$ (identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map that leaves every vector unchanged.
- $D'$ (scaled diagonal), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map $2^{-(2\alpha^2-2)}D$.
- $A$ (first contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $S/2$, from length-$s$ to length-$t$ vectors.
- $B_0$ (second contraction), bound on [Gaussian resampling](gaussian-resampling.md): The contraction $2^{-(2\alpha^2-2)}DN^{-1}C/2$, from length-$t$ to length-$s$ vectors.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Transform identity with retained permutations *<predicate>* Gaussian resampling
- [Coprime integers](coprime-integers.md): Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime.
  Shown as: Transform identity with retained permutations *<predicate>* Coprime integers
- [Tensor product](tensor-product.md): The product of two linear maps or arrays acting on separate coordinates, so that applying the product acts on each coordinate in turn.
  Shown as: Transform identity with retained permutations *<predicate>* Tensor product
- [Convolution theorem](convolution-theorem.md): The fact that the transform of a convolution of two sequences is the pointwise product of their transforms.
  Shown as: Transform identity with retained permutations *<predicate>* Convolution theorem

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Linear map](linear-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Gaussian function](gaussian-function.md)
- [Transform](transform.md)
- [Axis length](axis-length.md)
- [Radix-digit convolution](radix-digit-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "We retain both permutations in the transform formula" (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows. For an integer q ≥ 1, write q−1


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Let $R^+$ be the inverse of $R$, so $RF_s^+=F_s^+R^+$" (The page presents RF_s^+ = F_s^+R^+ as following from R^+ being the inverse of R, but that needs a property of the transform with respect to coordinate permutations which the page never states or justifies.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "so this equals $u*v$ up to scale" (The explicit factor 1/(prod s_i)^2 depends on the normalization of the transform, which the page never gives, so the reader cannot check the scale.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $F_s$ denotes where it is first used (for a size or count, what it counts): "$P_sF_s=2^{2\alpha^2}B_0P_tF_tA$" (Nothing on the page or in the earlier bindings says what F_s denotes; the page only refers to 'the transform' and to F_s^+ as 'the opposite transform'.)
- Say what $F_t$ denotes where it is first used (for a size or count, what it counts): "$P_sF_s=2^{2\alpha^2}B_0P_tF_tA$" (Nothing on the page or in the earlier bindings says what F_t denotes; it is used in the same way as F_s.)
- Say what $X$ denotes where it is first used (for a size or count, what it counts): "Since $(X_1\otimes\cdots\otimes X_d)(Y_1\otimes\cdots\otimes Y_d)=(X_1Y_1)\otimes\cdots\otimes(X_dY_d)$" (X is a generic factor of the one-dimensional identities; the page never says what it stands for.)
- Say what $Y$ denotes where it is first used (for a size or count, what it counts): "Since $(X_1\otimes\cdots\otimes X_d)(Y_1\otimes\cdots\otimes Y_d)=(X_1Y_1)\otimes\cdots\otimes(X_dY_d)$" (Y is a generic factor of the one-dimensional identities; the page never says what it stands for.)
- Say what $F_s^+$ denotes where it is first used: the page uses it before saying so in "with $F_s^+$ the opposite transform."
- Say what $*$ denotes where it is first used (for a size or count, what it counts): "the transform of $u*v$ is a pointwise product of transforms" (The convolution operator * is never defined; the page only names convolution in the convolution theorem and no known concept's name contains this symbol.)
- "convolution theorem" is the concept [Convolution theorem](convolution-theorem.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 224 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 280 words. Pages that grow with every repair stop being self-contained explanations of one concept.

Transform identity with retained permutations is the form of the Gaussian resampling identity in which the source and target coordinate permutations stay in the formula, so that they cancel across a convolution instead of being executed as sorts.

The one-dimensional identity is derived from [Gaussian resampling](gaussian-resampling.md) and holds for [coprime](coprime-integers.md) $s<t$ with $\theta=t/s-1$ large enough: $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$.

Here $d$ is the number of coordinates, not the digit count, and $s_i$ is the number of entries along coordinate $i$. Here $R$ permutes the source coordinates, and $Q$ permutes the target coordinates. The identity is lifted to $d$ coordinates by a [tensor product](tensor-product.md) of the $d$ one-dimensional identities. Since $(X_1\otimes\cdots\otimes X_d)(Y_1\otimes\cdots\otimes Y_d)=(X_1Y_1)\otimes\cdots\otimes(X_dY_d)$, multiplying the identities gives $RF_s$ on the left and $B_0QF_tA$ on the right, where $R=\bigotimes_i P_{s_i}$ and $Q=\bigotimes_i P_{t_i}$. Each coordinate contributes a factor $2^{2\alpha^2}$, so the factors multiply to $2^{2d\alpha^2}$:
$$RF_s=2^{2d\alpha^2}B_0QF_tA.$$

Let $R^+$ be the inverse of $R$, so $RF_s^+=F_s^+R^+$ with $F_s^+$ the opposite transform. Here $u$ is the first input array, with one entry for each point of the source grid of shape $s_1\times\cdots\times s_d$, and $v$ is the second. A permutation commutes with the pointwise product $\cdot$, so $(RF_su)\cdot(RF_sv)=R\big((F_su)\cdot(F_sv)\big)$. Applying $RF_s^+=F_s^+R^+$ and $R^+R$ = identity removes $R$, leaving $F_s^+\big((F_su)\cdot(F_sv)\big)$. By the convolution theorem, the transform of $u*v$ is a pointwise product of transforms, so this equals $u*v$ up to scale:
$$(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}.$$
The source permutation $R$ is never executed. Sorting is avoided because the usual implementation sorts twice on each coordinate, while this formula is computed directly. <cite data-source="paper">We retain both permutations in the transform formula</cite>.

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

Write the body to `exegenius/tasks/0050-write-transform-identity.answer.md` and the JSON to `exegenius/tasks/0050-write-transform-identity.answer.json`, then run `exegenius submit 0050-write-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
