# exegenius task 0021-write-gaussian-resampling

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
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: discrete mathematics through modular arithmetic, primes, gcds and the Euclidean algorithm, and the binary (radix) representation of integers; a first course in linear algebra over the reals covering vector spaces, bases, dimension, matrices, rank and invertibility; and the basics of complex numbers and roots of unity. They have not studied finite fields beyond GF(2), bilinear forms, tensor products, rings beyond polynomials, or the fast Fourier transform as a specialist topic, so those are explained by the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution (also: convolution of two vectors)
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

## This page

Concept: Gaussian resampling
Gloss: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
Also called: Harvey–van der Hoeven resampling

## This page in the argument

The step: The Gaussian identity $TP_sF_s = P_tF_tS$ holds, with $S$ and $T$ Gaussian-weighted maps from length-$s$ to length-$t$ vectors, and the near-identity operator $N = CTD$ is invertible.
How: write both transforms through a Gaussian-weighted resampling operator $N=CTD$ whose error from the identity is small
Why: The Gaussian weight at the selected coordinate cancels the diagonal factor, so $N$ differs from the identity by a small amount that a Neumann series can invert. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The Gaussian identity $TP_sF_s = P_tF_tS$ holds.
- $\|N-I\|<1/2$, so $N$ is invertible by the Neumann series.

It serves these steps, from the main result down:

- The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts.; how: invert the Gaussian resampling identity, which keeps both permutations, to a pair of contractions and normalize the constants (on [Transform identity with retained permutations](transform-identity.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary string to multiply, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary string to multiply, of length n.
- $n$ (input bit length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $\mathrm{val}$ (integer value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer z, padded on the left with zeros to k bits.
- $k$ (padded output length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation.
- $k$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in one radix digit.
- $m$ (digits per integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each integer.
- $u$ (first integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The first of the two integers to be multiplied, below $2^{km}$.
- $v$ (second integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The second of the two integers to be multiplied, below $2^{km}$.
- $u_i$ (digit of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix-$2^k$ digit of $u$.
- $v_i$ (digit of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The $i$-th radix-$2^k$ digit of $v$.
- $z$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): The variable of the digit polynomials, an indeterminate.
- $U$ (digit polynomial of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of $u$.
- $V$ (digit polynomial of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of $v$.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product polynomial $UV$.
- $w_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient of $z^j$ in $W$, a sum of products of digits.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in each vector, which is the length of the transform.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, whose powers are the weights of the transform.
- $F_q$ (transform map), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The discrete Fourier transform of length $q$, which maps an input vector $x$ to the output vector $y = F_q x$.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An input vector of $q$ complex values.
- $y$ (output vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of $x$, a vector of $q$ values.
- $j$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of an input entry, running from $0$ to $q-1$.
- $l$ (inverse index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An index of an entry of the recovered vector $x$ in the inverse transform.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Gaussian resampling *<predicate>* Discrete Fourier transform
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Gaussian resampling *<predicate>* Radix-digit convolution
- [Operator norm](operator-norm.md): The norm of a linear map L is the supremum of ‖Lu‖ over vectors u with ‖u‖ ≤ 1, where the vector norm of a complex vector is the largest modulus among its coordinates; a linear contraction is a linear map of norm at most one.
  Shown as: Gaussian resampling *<predicate>* Operator norm

## Pages that build on this one

- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations. Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n). We therefore need savings in both movem


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "With this choice the other terms give $\|N-I\|<1/2$ in the operator norm for the maximum-modulus vector norm." (The cited bound is the key fact that makes N invertible. The page says theta is a second parameter with alpha^2 theta > 1, but never says what theta is in the construction or how it enters N = CTD, so the reader cannot see why this choice gives the bound. The claim stands in for how the concept works, and its content and role are not given.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Expanding $(Nu)_j=\sum_i" (The expansion is presented as following from the definitions, but the page does not say how C selects coordinate l_j of TDu, what the summation range over i is (all integers with u_i taken modulo s, or 0 <= i < s), or how the modulo convention interacts with l_j. The reader cannot check the formula from what the page gives.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "and its sum is $N^{-1}$, which has norm less than $2$." (The page asserts that the sum of E^m is the inverse of N and that its norm is below 2, without the telescoping argument (I-E) times the partial sums giving I - E^(M+1), or the bound on the norm of the sum. These need the operator norm, which the reader does not know.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The other sub-step is the Gaussian identity $TP_sF_s=P_tF_tS$." (The identity is stated and its proof is left to the source, but the page gives no computation of the transform of the Gaussian weights with the scaling by s, t and alpha. The reason offered ('The Fourier transform of a Gaussian is again a Gaussian') is a heuristic that the reader cannot turn into a check of this specific identity.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "the lengths its transforms require are pairwise coprime rather than powers of two" (The page asserts what lengths integer multiplication requires, without giving the construction. The reader cannot check that they are pairwise coprime from this page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Inverting $N$ turns this identity into the form used in the" (The page says inverting N gives the form used on the linked page, but does not state that form or show the algebra (multiplying the identity by N inverse and rearranging). The reader cannot check the result from this page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "$(Cv)_j=v_{\ell_j}$" (The page never says what v denotes; from the domain C^t of C the reader can only guess that v is a vector of t complex coordinates.)
- Say what $i$ denotes where it is first used (for a size or count, what it counts): "Expanding $(Nu)_j=\sum_i" (The index of the sum is never introduced; the page does not say its range (all integers, or 0 to s-1 with subscripts mod s).)
- Say what $m$ denotes where it is first used (for a size or count, what it counts): "Then $\sum_{m\ge0}E^m$ converges" (The page never says what m denotes here; it is the summation index of the Neumann series. The earlier binding of m (digits per integer, on radix-digit-convolution) does not apply to this use.)
- Explain "Gaussian (function, weight)" in a sentence where it is first used.
- "operator norm and maximum-modulus vector norm" is the concept [Operator norm](operator-norm.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 342 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 427 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two. <cite data-source="paper">it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Integer multiplication needs this, since the lengths its transforms require are pairwise coprime rather than powers of two. Gaussian resampling replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by transforms on power-of-two axes.

Let $s$ and $t$ be the number of coordinates of source and target vectors. Write $F_s$ and $P_s$ for the normalized Fourier transform and the coordinate permutation of length-$s$ vectors, and likewise $F_t$ and $P_t$ for length-$t$ vectors.

The identity uses two Gaussian-weighted maps $S,T$ from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of the Gaussian weights. For a length-$s$ vector $u$ with entries $u_j$, $0\le j<s$, and an index $0\le k<t$, they are

$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$

where subscripts are taken modulo $s$. $S$ gathers the entries of $u$ near the position $sk/t$, and $T$ spreads each entry $u_j$ over the targets near $tj/s$.

Let $\ell_j$ be the integer nearest to $tj/s$, with ties rounded upward, for $0\le j<s$, and let $\beta_j=tj/s-\ell_j$. Let $C:\mathbb C^t\to\mathbb C^s$ be the map $(Cv)_j=v_{\ell_j}$ that selects these coordinates, let $D:\mathbb C^s\to\mathbb C^s$ be the diagonal map $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$, an operator on length-$s$ vectors.

Expanding $(Nu)_j=\sum_i e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i$, the term $i=j$ has $ti/s-\ell_j=\beta_j$, so its two exponentials cancel and the term equals $u_j$. The Gaussian weight at the selected coordinate thus cancels the diagonal factor, and $N$ differs from the identity only through the other terms.

The paper uses a second parameter $\theta$, chosen so that $\alpha^2\theta>1$. With this choice the other terms give $\|N-I\|<1/2$ in the operator norm for the maximum-modulus vector norm. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite>

A Neumann series inverts $N$: write $N=I-E$ with $\|E\|<1/2$. Then $\sum_{m\ge0}E^m$ converges, since $\|E^m\|\le\|E\|^m$, and its sum is $N^{-1}$, which has norm less than $2$.

The other sub-step is the Gaussian identity $TP_sF_s=P_tF_tS$. It says that applying $F_s$, then $P_s$ and $T$, gives the same result as applying $S$, then $F_t$ and $P_t$. The Fourier transform of a Gaussian is again a Gaussian, which is why such weights move between the two sets of frequencies. Its proof is in Harvey and van der Hoeven <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Inverting $N$ turns this identity into the form used in the [transform identity with retained permutations](transform-identity.md).

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

Write the body to `exegenius/tasks/0021-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0021-write-gaussian-resampling.answer.json`, then run `exegenius submit 0021-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
