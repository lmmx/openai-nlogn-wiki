# exegenius task 0058-write-transform-identity

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

- $n$ (bit length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two binary strings to multiply, a count of bits.
- $x$ (first input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first of the two binary strings to multiply, of length n.
- $y$ (second input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second of the two binary strings to multiply, of length n.
- $w$ (generic binary string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string whose value val(w) is taken.
- $L$ (padded output length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded output, that is, the length to which bin_L pads a binary representation.
- $z$ (integer to represent), bound on [Exact integer multiplication](exact-integer-multiplication.md): An integer with 0 at most z below 2^L, whose binary representation bin_L(z) is taken.
- $b$ (digit bit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in one radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each integer.
- $i$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): The position of a digit, running from 0 to m-1.
- $j$ (coefficient index), bound on [Radix-digit convolution](radix-digit-convolution.md): The power of X whose coefficient in W is taken.
- $p$ (first integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The first of the two integers being multiplied, below 2^{bm}.
- $q$ (second integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The second of the two integers being multiplied, below 2^{bm}.
- $X$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): An indeterminate, a symbol that is not a number.
- $P$ (first digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in X whose coefficient list is the digits of p.
- $Q$ (second digit polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial in X whose coefficient list is the digits of q.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product PQ, a polynomial in X whose coefficients are convolutions of the digit lists.
- $w_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient of X^j in W, a sum of products of digits.
- $a$ (first sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two sequences whose cyclic convolution is taken, with entries a_0 through a_{q-1}.
- $b$ (second sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two sequences whose cyclic convolution is taken, with entries b_0 through b_{q-1}.
- $q$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the sequences a and b, which is also the length of their cyclic convolution.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The sequence a \ast b of the same length q, whose entries are the cyclic convolution sums c_o.
- $o$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of an entry of the cyclic convolution c, running from 0 to q-1.
- $i$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index of the terms of the sum for c_o, running from 0 to q-1; it replaces its earlier meaning as a digit index.
- $q$ (sequence length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of entries in each vector of the transform, and the order of the root of unity.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, whose powers are the weights of the transform.
- $F_q$ (discrete Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector $x$ of length $q$ to the vector $y = F_q x$ defined by the weighted sum above.
- $j$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry of the transform, running from 0 to q-1.
- $k$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry of the transform, running from 0 to q-1.
- $l$ (inverse index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an entry of the recovered vector in the inverse map, running from 0 to q-1.
- $d$ (integer exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent of the root of unity in the orthogonality sum.
- $r$ (shifted index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index $(l-k) \bmod q$ for fixed $k$, which runs over $0,\dots,q-1$ as $l$ does.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The input vector $(x_0,\dots,x_{q-1})$ of the transform, not the integer inputs of earlier pages.
- $y$ (output vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The output vector $F_q x$ of the transform, not the integer inputs of earlier pages.
- $w$ (complex vector), bound on [Operator norm](operator-norm.md): A complex vector of length q, whose vector norm is its largest coordinate modulus.
- $L$ (linear map), bound on [Operator norm](operator-norm.md): A linear map from complex vectors to complex vectors, whose operator norm is taken.
- $M$ (second linear map), bound on [Operator norm](operator-norm.md): Another linear map, composed with L in the product LM.
- $S'$ (scaled Gaussian map), bound on [Operator norm](operator-norm.md): Half of a Gaussian resampling map, used as the map A.
- $J'$ (scaled inverse map), bound on [Operator norm](operator-norm.md): Half the inverse of an invertible map close to the identity.
- $D'$ (scaled diagonal map), bound on [Operator norm](operator-norm.md): A diagonal map scaled by a fixed factor at most one.
- $C$ (coordinate selection), bound on [Operator norm](operator-norm.md): A map that selects some coordinates of its input vector, so that each output entry copies one input entry.
- $s$ (source length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the source vector u.
- $t$ (target length), bound on [Gaussian resampling](gaussian-resampling.md): The number of entries in the target vector g.
- $\theta$ (relative gap), bound on [Gaussian resampling](gaussian-resampling.md): The ratio t/s minus one, the relative gap between the two lengths.
- $u$ (source vector), bound on [Gaussian resampling](gaussian-resampling.md): A length-s vector of input values.
- $g$ (target vector), bound on [Gaussian resampling](gaussian-resampling.md): A length-t vector of output values.
- $j$ (source index), bound on [Gaussian resampling](gaussian-resampling.md): An index of the entries of u, read modulo s.
- $k$ (target index), bound on [Gaussian resampling](gaussian-resampling.md): An index of the entries of g, read modulo t.
- $h$ (summation index), bound on [Gaussian resampling](gaussian-resampling.md): The index of the sum over all integers defining the entries of Nu.
- $F_s$ (length-s transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform on length-s vectors.
- $P_s$ (source permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation $(P_s u)_j=u_{tj}$ on length-s vectors.
- $F_t$ (length-t transform), bound on [Gaussian resampling](gaussian-resampling.md): The normalized Fourier transform on length-t vectors.
- $P_t$ (target permutation), bound on [Gaussian resampling](gaussian-resampling.md): The coordinate permutation $(P_t g)_k=g_{-sk}$ on length-t vectors.
- $S$ (source Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-s to length-t vectors that gathers the entries of u near sk/t.
- $T$ (target Gaussian map), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-s to length-t vectors that spreads each entry of u over the targets near tj/s.
- $\alpha$ (Gaussian width parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer parameter that sets the width of the Gaussian weights.
- $\ell_j$ (nearest coordinate), bound on [Gaussian resampling](gaussian-resampling.md): The integer nearest tj/s, with ties rounded up, which is the coordinate selected for index j.
- $\beta_j$ (rounding offset), bound on [Gaussian resampling](gaussian-resampling.md): The offset tj/s minus its nearest integer, the amount by which the Gaussian weight is cancelled.
- $D$ (diagonal factor), bound on [Gaussian resampling](gaussian-resampling.md): The diagonal map multiplying entry j by $e^{\pi\alpha^2\beta_j^2}$.
- $N$ (near-identity map), bound on [Gaussian resampling](gaussian-resampling.md): The map $N=CTD$ from length-s to length-s vectors, which is close to the identity.
- $I$ (identity map), bound on [Gaussian resampling](gaussian-resampling.md): The identity map on length-s vectors.
- $E$ (error map), bound on [Gaussian resampling](gaussian-resampling.md): The error $I-N$, whose operator norm is small.
- $B$ (output map), bound on [Gaussian resampling](gaussian-resampling.md): The linear map $DN^{-1}C$ from length-t to length-s vectors.
- $r$ (Neumann index), bound on [Gaussian resampling](gaussian-resampling.md): The summation index of the Neumann series $\sum_{r\ge0}E^r$.
- $R$ (last partial-sum index), bound on [Gaussian resampling](gaussian-resampling.md): The last index of the partial sum $\sum_{r=0}^{R}E^r$.
- $p$ (precision parameter), bound on [Gaussian resampling](gaussian-resampling.md): The integer precision parameter, greater than 100, in the hypotheses of the estimate.
- $C$ (coordinate selection), bound on [Gaussian resampling](gaussian-resampling.md): The map from length-t to length-s vectors that selects the coordinates $\ell_j$, so that each output entry copies one input entry.

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

- The quotation does not support the claim it is attached to (unsupported): "The inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$" cites "inverse estimate proved in [15, Theorem 4.2 and Lemma 4.6]": The quotation only points to where the inverse estimate is proved ([15, Theorem 4.2 and Lemma 4.6]); it does not state the bound ||N-I|| < 2^{-α²θ}. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 359 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 448 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which both coordinate permutations stay as explicit factors, so that they can cancel across a convolution. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate, and keeping both permutations in the formula avoids those sorts. The paper makes this choice explicitly <cite data-source="paper">We retain both permutations in the transform formula</cite>.

Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. The permutations $P_s$ and $P_t$ are those of the Gaussian resampling page: $P_s$ permutes coordinates of length-$s$ vectors and $P_t$ permutes coordinates of length-$t$ vectors, with subscripts taken modulo $s$ and $t$. The identity is
$$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
Here $A$ is a linear map from length-$s$ to length-$t$ vectors and $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The letters $A$ and $B_0$ are new maps here, not the $A=S$ and $B=DN^{-1}C$ of the Gaussian resampling page. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm. The claim is stated in <cite data-source="paper">Lemma 19 (Resampling without executing the two permutations)</cite>.

The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
$$TP_sF_s=P_tF_tS.$$
It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. It applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$, and prior work proves it.

The inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$ <cite data-source="paper">inverse estimate proved in [15, Theorem 4.2 and Lemma 4.6]</cite>, which is below $1/2$ because $\alpha^2\theta>1$. So $\|E\|<1$ with $E=I-N$, and the Neumann series $\sum_{r\ge 0}E^r$, the matrix analogue of the geometric series, converges, so $N$ is invertible.

The scaled maps are $S'=S/2$, $J'=N^{-1}/2$ and $D'=2^{-(2\alpha^2-2)}D$. Set $A=S'$ and $B_0=D'J'C$, where $C$ is the selection map of the Gaussian resampling page. Both are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their bounds.

Since $N=CTD$ and $D$ is invertible, $CT=ND^{-1}$, so $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$. Thus $DN^{-1}C$ is a left inverse of $T$. Applying it to the Gaussian identity gives $DN^{-1}CP_tF_tS=P_sF_s$, and therefore
$$B_0P_tF_tA=2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12\,DN^{-1}CP_tF_tS=2^{-2\alpha^2}P_sF_s.$$
Multiplying by $2^{2\alpha^2}$ gives the identity.

The constant $2^{2\alpha^2}$ depends only on $\alpha$. Its three normalizations multiply to $2^{-(2\alpha^2-2)}\cdot\tfrac12\cdot\tfrac12=2^{-2\alpha^2}$. The Gaussian weights, the factor $1/\alpha$ in $S$, and the lengths $s$ and $t$ sit inside the maps $S$, $T$ and $N$, so they never reach the constant.

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

Write the body to `exegenius/tasks/0058-write-transform-identity.answer.md` and the JSON to `exegenius/tasks/0058-write-transform-identity.answer.json`, then run `exegenius submit 0058-write-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
