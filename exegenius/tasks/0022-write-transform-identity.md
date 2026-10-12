# exegenius task 0022-write-transform-identity

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
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
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

Concept: Transform identity with retained permutations
Gloss: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## This page in the argument

The step: The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts.
How: invert the Gaussian resampling identity, which keeps both permutations, to a pair of contractions and normalize the constants
Why: The usual implementation sorts twice on each coordinate, so keeping both permutations in the transform formula and computing that formula directly avoids those sorts and lets the permutations cancel across a convolution. (the sources say so: "We retain both permutations in the transform formula and compute that formula directly." (paper))
Striking feature: the constant in front, $2^{2\alpha^2}$, is a power of two that depends only on $\alpha$, not on the coordinate lengths $s$ and $t$ (explain why it holds, from the method)

Its sub-steps, in order:

- The Gaussian identity $TP_sF_s = P_tF_tS$ holds, with $S$ and $T$ Gaussian-weighted maps from length-$s$ to length-$t$ vectors, and the near-identity operator $N = CTD$ is invertible. (on [Gaussian resampling](gaussian-resampling.md))
- The maps $A=S'$ and $B_0=D'J'C$ are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds.
- The left inverse $DN^{-1}C$ of $TD^{-1}$ applied to the Gaussian identity gives $DN^{-1}CP_tF_tS = P_sF_s$.
- The normalizations $2^{-2\alpha^2}$ give $B_0P_tF_tA = 2^{-2\alpha^2}P_sF_s$, which is the transform identity (33) with the power of two $2^{2\alpha^2}$.

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
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): $s$ is the number of coordinates of a source vector.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): $t$ is the number of coordinates of a target vector.
- $F_s$ (source transform), bound on [Gaussian resampling](gaussian-resampling.md): $F_s$ is the normalized Fourier transform of length-$s$ vectors.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): $P_s$ is the coordinate permutation of length-$s$ vectors.
- $F_t$ (target transform), bound on [Gaussian resampling](gaussian-resampling.md): $F_t$ is the normalized Fourier transform of length-$t$ vectors.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): $P_t$ is the coordinate permutation of length-$t$ vectors.
- $\alpha$ (Gaussian width), bound on [Gaussian resampling](gaussian-resampling.md): $\alpha$ is the parameter that sets the width of the Gaussian weights.
- $\theta$ (second parameter), bound on [Gaussian resampling](gaussian-resampling.md): $\theta$ is a second parameter, chosen so that $\alpha^2\theta>1$.
- $u$ (source vector), bound on [Gaussian resampling](gaussian-resampling.md): $u$ is a length-$s$ vector with entries $u_j$.
- $j$ (entry index), bound on [Gaussian resampling](gaussian-resampling.md): $j$ indexes the entries $u_j$ of a source vector, $0\le j<s$.
- $k$ (target index), bound on [Gaussian resampling](gaussian-resampling.md): $k$ is an index of a target coordinate, $0\le k<t$.
- $S$ (Gaussian source map), bound on [Gaussian resampling](gaussian-resampling.md): $S$ is the Gaussian-weighted map from length-$s$ to length-$t$ vectors.
- $T$ (Gaussian target map), bound on [Gaussian resampling](gaussian-resampling.md): $T$ is the Gaussian-weighted map from length-$s$ to length-$t$ vectors.
- $\ell_j$ (nearest target coordinate), bound on [Gaussian resampling](gaussian-resampling.md): $\ell_j$ is the integer nearest to $tj/s$, for $0\le j<s$.
- $\beta_j$ (rounding error), bound on [Gaussian resampling](gaussian-resampling.md): $\beta_j$ is the difference $tj/s-\ell_j$.
- $C$ (selection map), bound on [Gaussian resampling](gaussian-resampling.md): $C$ is the map from length-$t$ to length-$s$ vectors that selects the coordinates $\ell_j$.
- $D$ (diagonal map), bound on [Gaussian resampling](gaussian-resampling.md): $D$ is the diagonal map on length-$s$ vectors that multiplies entry $j$ by $e^{\pi\alpha^2\beta_j^2}$.
- $N$ (near-identity operator), bound on [Gaussian resampling](gaussian-resampling.md): $N=CTD$ is an operator on length-$s$ vectors.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Transform identity with retained permutations *<predicate>* Gaussian resampling
- [Operator norm](operator-norm.md): The norm of a linear map L is the supremum of ‖Lu‖ over vectors u with ‖u‖ ≤ 1, where the vector norm of a complex vector is the largest modulus among its coordinates; a linear contraction is a linear map of norm at most one.
  Shown as: Transform identity with retained permutations *<predicate>* Operator norm

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)

## Evidence from the sources, with the paragraph around each quote

- "We retain both permutations in the transform formula" (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows. For an integer q ≥ 1, write q−1


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "They satisfy the Gaussian identity $TP_sF_s=P_tF_tS$." (The identity is asserted with no proof, no citation, and no statement that it is the Gaussian resampling identity. The reader cannot check it from the page, and the whole argument depends on it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Its $j$-th output is $u_j$ plus a small error, so $\|N-I\|<1/2$." (The page gives no estimate of the error term in N u, so the reader cannot check that the operator norm of N - I is below 1/2.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "have norms $\|S'\|<3/4$, $\|J'\|<7/8$ and $\|D'\|<1$" (The page gives no computation for these bounds. They would need bounds on the norms of S, N^{-1} and D (for example, from the size of the Gaussian weights and the entries of D), none of which the page states.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "With $\|C\|=1$, this makes $A=S'$ and $B_0=D'J'C$ contractions." (The page does not say why the indices q_j are distinct (which is what makes C a coordinate selection of norm one), nor how the norm of a selection map is computed. The reader cannot check ||C|| = 1.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "$(P_tv)_k=v_{-sk}$" (The page never says what v denotes; it only says P_t acts on length-t vectors, so v is presumably a length-t vector, but this is not stated. The earlier binding of v (second integer, radix-digit-convolution) is a different meaning.)
- "norm of a linear map" is the concept [Operator norm](operator-norm.md), now a prerequisite: link it where the term is used.
- Explain "Neumann series" in a sentence where it is first used.

## Previous version (revise it)

It has 330 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 412 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The transform identity with retained permutations is an exact identity relating two Fourier transforms of different lengths, with both coordinate permutations kept as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. <cite data-source="paper">Its usual implementation sorts twice on each coordinate.</cite> Keeping the permutations as factors lets them cancel across a convolution instead of being executed as sorts.

The integer $s$ is the number of coordinates of a source vector. The integer $t$ is the number of coordinates of a target vector, with $2\le s<t$ and $\gcd(s,t)=1$. The integer $\alpha\ge 2$ sets the width of the Gaussian weights. $F_s$ is the normalized Fourier transform of length $s$, and $F_t$ that of length $t$. $P_s$ is the permutation $(P_su)_j=u_{tj}$ of length-$s$ vectors, with subscripts taken modulo $s$. $P_t$ is the permutation $(P_tv)_k=v_{-sk}$ of length-$t$ vectors, with subscripts taken modulo $t$.

A linear contraction is a linear map of norm at most one. $A$ is a linear contraction from length-$s$ to length-$t$ vectors. $B_0$ is a linear contraction from length-$t$ to length-$s$ vectors. The step claims
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
and its proof sits under <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses two Gaussian-weighted maps $S$ and $T$ from length-$s$ to length-$t$ vectors, defined by the sums below.
$$(Su)_k=\frac{1}{\alpha}\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
They satisfy the Gaussian identity $TP_sF_s=P_tF_tS$.

For $0\le j<s$, $q_j$ is the integer nearest $tj/s$, with ties rounded upward. The map $C$ selects the coordinates $q_0,\dots,q_{s-1}$ from a length-$t$ vector. The map $D$ is the diagonal map $(Du)_j=e^{\pi\alpha^2(tj/s-q_j)^2}u_j$ on length-$s$ vectors, whose factor cancels the Gaussian factor of $T$ at $q_j$.

The operator $N=CTD$ is near the identity. Its $j$-th output is $u_j$ plus a small error, so $\|N-I\|<1/2$. Hence $N$ is invertible, with $N^{-1}=\sum_{k\ge 0}(I-N)^k$ by the Neumann series.

Since $(DN^{-1}C)T=I$, the map $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$.

Scaled copies $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$ have norms $\|S'\|<3/4$, $\|J'\|<7/8$ and $\|D'\|<1$. With $\|C\|=1$, this makes $A=S'$ and $B_0=D'J'C$ contractions. The three normalizations multiply to $2^{-(2\alpha^2-2)}\cdot 2^{-1}\cdot 2^{-1}=2^{-2\alpha^2}$, so
$$B_0P_tF_tA=2^{-2\alpha^2}DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s,$$
which is the claimed identity.

The constant is a power of two that depends only on $\alpha$, because the only scalar factors are these three normalizations. The $s$- and $t$-dependence lies in $C$, $T$, $D$ and $N$, none of which carries such a factor.

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

Write the body to `exegenius/tasks/0022-write-transform-identity.answer.md` and the JSON to `exegenius/tasks/0022-write-transform-identity.answer.json`, then run `exegenius submit 0022-write-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
