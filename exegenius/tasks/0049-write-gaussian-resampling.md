# exegenius task 0049-write-gaussian-resampling

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

Concept: Gaussian resampling
Gloss: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
Also called: Harvey–van der Hoeven resampling

## This page in the argument

The step: For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$.
How: factor the resampling through two Gaussian maps and a near-identity correction, invert the correction by a Neumann series, then normalize
Why: The two Gaussian maps relate the two frequency grids, and the correction is close to the identity, so it is invertible and its inverse can be bounded. (the sources leave this for the reader to work out: spell it out)
Striking feature: the constant $2^{2\alpha^2}$ is uniform in $p$, $s$, $t$ and $\alpha$ (explain why it holds, from the method)

Its sub-steps, in order:

- $TP_sF_s=P_tF_tS$, the Gaussian identity relating the two resampled transforms.
- $\|N-I\|<1/2$, so the correction $N$ is invertible by a Neumann series.
- $A=S/2$ and $B_0=2^{-(2\alpha^2-2)}DN^{-1}C/2$ are set as contractions.
- $DN^{-1}CP_tF_tS=P_sF_s$, the left inverse applied to the first identity.
- $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$, which is the one-dimensional identity.

It serves these steps, from the main result down:

- The Gaussian resampling identity $RF_s=2^{2d\alpha^2}B_0QF_tA$ holds with the permutations $R$ and $Q$ kept in the formula, and the source permutation $R$ cancels across a convolution: $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$.; how: prove the one-dimensional identity with both permutations kept, lift it to a tensor product, then cancel the source permutation in a convolution (on [Transform identity with retained permutations](transform-identity.md))

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Gaussian resampling *<predicate>* Radix-digit convolution
- [Coprime integers](coprime-integers.md): Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime.
  Shown as: Gaussian resampling *<predicate>* Coprime integers
- [Modular arithmetic](modular-arithmetic.md): Arithmetic in which values are reduced to their remainders on division by a fixed modulus q, so that index positions wrap around after q.
  Shown as: Gaussian resampling *<predicate>* Modular arithmetic
- [Operator norm](operator-norm.md): For a linear map, the largest factor by which it stretches a vector measured in a fixed norm, taken over all vectors of norm at most one.
  Shown as: Gaussian resampling *<predicate>* Operator norm
- [Gaussian function](gaussian-function.md): The bell-shaped function x ↦ e^(−x²), or a scaled and shifted copy of it, used as a smooth weight that decays rapidly away from its centre.
  Shown as: Gaussian resampling *<predicate>* Gaussian function

## Pages that build on this one

- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Linear map](linear-map.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Tensor product](tensor-product.md)
- [Convolution theorem](convolution-theorem.md)
- [Transform](transform.md)
- [Axis length](axis-length.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations. Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n). We therefore need savings in both movem


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Since $\alpha^2<p$ and $\theta>p/\alpha^4$" (The page gives no reason for alpha^2 < p. Its stated constraints are only alpha >= 2 an integer and theta > p/alpha^4, so the reader cannot check this inequality, and the next bound alpha^2 theta > 1 depends on it.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "Harvey and van der Hoeven prove the Gaussian identity $TP_sF_s = P_tF_tS$" (The identity is stated as proven by the sources but is not marked (cited), and the page gives no argument for it. Every later step uses it as a premise, so the reader cannot check it from the page.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $s$ denotes where it is first used: the page uses it before saying so in "where $s$ is the number of coordinates of the source vector"
- Say what $t$ denotes where it is first used: the page uses it before saying so in "and $t$ the number of coordinates of the target"
- Say what $\alpha$ denotes where it is first used: the page uses it before saying so in "$\alpha \ge 2$ is an integer Gaussian width"
- Say what $p$ denotes where it is first used: the page uses it before saying so in "$p$ is the integer precision of the numerical approximation"
- Say what $F_s$ denotes where it is first used (for a size or count, what it counts): "Harvey and van der Hoeven prove the Gaussian identity $TP_sF_s = P_tF_tS$" (No sentence says what F_s denotes; it is presumably the transform on the source grid, but the page never says so and the discrete-fourier-transform page does not bind F.)
- Say what $F_t$ denotes where it is first used (for a size or count, what it counts): "Harvey and van der Hoeven prove the Gaussian identity $TP_sF_s = P_tF_tS$" (No sentence says what F_t denotes; it is presumably the transform on the target grid, but the page never says so and the discrete-fourier-transform page does not bind F.)
- Say what $A$ denotes where it is first used: the page uses it before saying so in "where $A$ maps length-$s$ vectors to length-$t$ vectors and $B_0$ maps back."
- Say what $B_0$ denotes where it is first used: the page uses it before saying so in "where $A$ maps length-$s$ vectors to length-$t$ vectors and $B_0$ maps back."
- "Gaussian (weight or function)" is the concept [Gaussian function](gaussian-function.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 404 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 505 words. Pages that grow with every repair stop being self-contained explanations of one concept.

Gaussian resampling is an identity that replaces the [Discrete Fourier transform](discrete-fourier-transform.md) of an arbitrary length by transforms whose lengths are powers of two. It serves the [Radix-digit convolution](radix-digit-convolution.md) of digit vectors, which needs such transforms. <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

The identity is restricted to [coprime integers](coprime-integers.md) $s<t$, where $s$ is the number of coordinates of the source vector and $t$ the number of coordinates of the target. Let $\theta = t/s-1$ be the relative excess of $t$ over $s$. The identity needs $\theta > p/\alpha^4$, where $\alpha \ge 2$ is an integer Gaussian width (a larger $\alpha$ gives wider weights below) and $p$ is the integer precision of the numerical approximation.

Here $u$ is a vector of $s$ coordinates and $v$ a vector of $t$ coordinates. Its permutations $P_s$ and $P_t$ are defined using [modular arithmetic](modular-arithmetic.md) on their indices: $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$.

$S$ maps vectors of $s$ coordinates to vectors of $t$ coordinates by $(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j$, and $T$ maps them by $(Tu)_k=\sum_{j\in\mathbb{Z}} e^{-\pi\alpha^{2}(tj/s-k)^2}u_j$. Subscripts of vectors are taken modulo their length. Harvey and van der Hoeven prove the Gaussian identity $TP_sF_s = P_tF_tS$: transforming on the source grid and then applying $T$ agrees with applying $S$ and then transforming on the target grid.

$C$ selects, for each $j<s$, the entry of a length-$t$ vector at $m_j$, the integer nearest to $tj/s$. $D$ is the diagonal map $(Du)_j = e^{\pi\alpha^2(tj/s-m_j)^2}u_j$ on length-$s$ vectors, which cancels the Gaussian factor of $T$ at that entry. Put $N = CTD$, the correction map on length-$s$ vectors. Its $j$th entry is $u_j$ plus other terms, so $N$ is close to the identity.

Here $I$ is the identity map, which leaves every vector unchanged. The size of $N-I$ is measured by its [operator norm](operator-norm.md), $\|N-I\|$, and the sources bound it by $2^{-\alpha^2\theta}$. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, we have $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$. Then $N$ is invertible by the Neumann series $N^{-1}=\sum_{k\ge 0}(I-N)^k$, whose $k$th term has norm at most $2^{-k}$, so the series converges.

Because $CT = ND^{-1}$, the map $DN^{-1}C$ is a left inverse of $T$, since $(DN^{-1}C)T = I$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS = P_sF_s$. The two Gaussian maps relate the two frequency grids, and this inverse turns the identity into one for $P_sF_s$ alone.

Write $D'=2^{-(2\alpha^2-2)}D$ for the scaled diagonal map. Set $A = S/2$ and $B_0 = 2^{-(2\alpha^2-2)}DN^{-1}C/2$, where $A$ maps length-$s$ vectors to length-$t$ vectors and $B_0$ maps back. Both are contractions, that is, linear maps of norm at most one. The sources bound $\|S/2\|<3/4$, $\|N^{-1}/2\|<7/8$ and $\|D'\|<1$ <cite data-source="paper">∥D′ ∥ < 1</cite>, and $\|C\|=1$ because $C$ only copies entries. So $\|A\|<3/4$ and $\|B_0\|<7/8$.

The scalars $2^{-(2\alpha^2-2)}$, $\tfrac12$ and $\tfrac12$ multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA = 2^{-2\alpha^2}P_sF_s$. This is the one-dimensional identity, and $P_sF_s = 2^{2\alpha^2}B_0P_tF_tA$. The constant $2^{2\alpha^2}$ is uniform because the norm bounds $3/4$, $7/8$ and $1$ are fixed numbers, and $\alpha$ enters only through the normalization $2^{-(2\alpha^2-2)}$ of $D$, which the constant cancels. <cite data-source="paper">The constant is uniform in p, s, t, α.</cite>

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

Write the body to `exegenius/tasks/0049-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0049-write-gaussian-resampling.answer.json`, then run `exegenius submit 0049-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
