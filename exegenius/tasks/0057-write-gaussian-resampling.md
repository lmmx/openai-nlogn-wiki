# exegenius task 0057-write-gaussian-resampling

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

- $j$ means source index here, but output index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Use another letter for the source index on gaussian-resampling (the DFT page's j is an output index, the transform's frequency), or say on this page that j here is a position in the source vector u, not the DFT output index.
- $r$ means Neumann index here, but shifted index on [Discrete Fourier transform](discrete-fourier-transform.md), which this page builds on: Use another letter for the Neumann summation index on gaussian-resampling, since r on the DFT page is the shifted index (l-k) mod q running over 0 to q-1.
- $p$ means precision parameter here, but first integer on [Radix-digit convolution](radix-digit-convolution.md), which this page builds on: Use another letter for the precision parameter on gaussian-resampling, since p on the radix-digit convolution page is the first integer being multiplied.

## Previous version (revise it)

It has 490 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 612 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. It replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by such transforms. <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Let $s$ and $t$ be the lengths of the source and target vectors, with $\gcd(s,t)=1$ and $\theta=t/s-1$ the relative gap between them. Here $s$ and $t$ are lengths, not the binary string and output index of earlier pages. Let $u$ be a length-$s$ source vector and $g$ a length-$t$ target vector. Entries of $u$ are indexed by $j$, entries of $g$ by $k$, and an index is read modulo the length, so $u_j=u_{j \bmod s}$ for every integer $j$.

Let $F_s$ be the normalized Fourier transform on length-$s$ vectors and $P_s$ the coordinate permutation $(P_s u)_j=u_{tj}$. Let $F_t$ and $P_t$ be the transform and the permutation $(P_t g)_k=g_{-sk}$ on length-$t$ vectors.

Let $S$ and $T$ be the maps from length-$s$ to length-$t$ vectors given by
$$(Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j.$$
The integer $\alpha$ sets the width of the Gaussian weights, which are bell-shaped functions of $j$ that decay quickly away from their centres. $S$ gathers the entries of $u$ near $sk/t$, and $T$ spreads each $u_j$ over the targets near $tj/s$.

For $0\le j<s$, let $\ell_j$ be the integer nearest $tj/s$, ties rounded up, and $\beta_j=tj/s-\ell_j$. The same rule defines $\ell_h$ and $\beta_h$ for every integer $h$, which is the summation index used below. Since $\ell_{h+s}=\ell_h+t$, we get $\beta_{h+s}=\beta_h$. For example, with $s=2$ and $t=3$, $\ell_1=2$ and $\beta_1=-\tfrac12$.

Let $C$ select coordinates, $(Cg)_j=g_{\ell_j}$, let $D$ be the diagonal map $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$, a map from length-$s$ to length-$s$ vectors. Expanding,
$$(Nu)_j=\sum_{h\in\mathbb Z}e^{-\pi\alpha^2(th/s-\ell_j)^2}e^{\pi\alpha^2\beta_h^2}u_h.$$
The term $h=j$ has $tj/s-\ell_j=\beta_j$, so its two exponentials cancel and it equals $u_j$. The Gaussian weight of $T$ at the selected coordinate cancels the diagonal factor of $D$, so $N$ is close to the identity.

Let $I$ be the identity map on length-$s$ vectors, so $N-I$ collects the remaining terms. Write $E=I-N$ for the error, so $N=I-E$. The error $E$ is measured in the [operator norm](operator-norm.md) for the maximum-modulus vector norm, and $\|E\|=\|N-I\|$.

The Gaussian identity $TP_sF_s=P_tF_tS$ holds. Poisson summation, a standard identity that equates a sum over all integers of a Gaussian with a Fourier series, explains it. Harvey and van der Hoeven establish this identity and the inverse estimate $\|N-I\|<2^{-\alpha^2\theta}$ <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Here $p>100$ is an integer precision parameter, and the estimate applies when $\alpha$ is an integer with $2\le\alpha<p$, $\gcd(s,t)=1$ and $\theta>p/\alpha^4$. The argument also needs $\alpha^2<p$, which the range $2\le\alpha<p$ does not give by itself. With $\alpha^2<p$, we get $\alpha^2\theta>p/\alpha^2>1$, so $\|E\|<2^{-\alpha^2\theta}<1/2$.

The Neumann series is the operator version of the geometric series, $\sum_{r\ge0}E^r$, with $r$ its summation index. Let $R$ be the last index of a partial sum $\sum_{r=0}^{R}E^r$. Multiplying it by $I-E=N$ telescopes to $I-E^{R+1}$. Since $\|E^r\|\le\|E\|^r$, the series converges absolutely and $\|E^{R+1}\|\to0$, so the series sums to $N^{-1}$. Hence $N$ is invertible.

Multiply $TP_sF_s=P_tF_tS$ on the left by $C$, and use $CT=ND^{-1}$, which holds since $D$ is invertible. This gives $ND^{-1}P_sF_s=CP_tF_tS$. Multiplying on the left by $N^{-1}$ and then by $D$ gives $P_sF_s=DN^{-1}C\,P_tF_tS$, which has the form $P_sF_s=BP_tF_tS$ with $B=DN^{-1}C$ a linear map. Both permutations stay in this formula, which is the form used on the [transform identity with retained permutations](transform-identity.md) page.

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

Write the body to `exegenius/tasks/0057-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0057-write-gaussian-resampling.answer.json`, then run `exegenius submit 0057-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
