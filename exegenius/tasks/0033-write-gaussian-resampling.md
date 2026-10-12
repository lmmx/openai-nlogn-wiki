# exegenius task 0033-write-gaussian-resampling

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

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two binary strings to be multiplied.
- $x$ (first input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first of the two binary strings to be multiplied, of length $n$.
- $y$ (second input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second of the two binary strings to be multiplied, of length $n$.
- $s$ (binary string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A generic binary string whose integer value is taken by the function val.
- $\mathrm{val}$ (string value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $k$ (padded output length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
- $z$ (integer to represent), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than $2^k$, whose binary representation is padded to length $k$.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to length $k$.
- $b$ (digit bit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in one radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each integer.
- $u$ (first integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer whose i-th digit is u_i.
- $v$ (second integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer whose i-th digit is v_i.
- $u_i$ (digit of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th digit of u, in the set $\{0,\dots,2^b-1\}$.
- $v_i$ (digit of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th digit of v, in the set $\{0,\dots,2^b-1\}$.
- $i$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): An index of the digits of u and v, running from 0 to m-1.
- $l$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): A second index of the digits of u and v, running from 0 to m-1.
- $j$ (coefficient index), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a coefficient of W.
- $z$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal symbol that is not a number, the variable of the polynomials U, V and W.
- $U$ (digit polynomial of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of u.
- $V$ (digit polynomial of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of v.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product UV, whose coefficient list is the convolution of the digit lists.
- $w_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th coefficient of W, the sum of the products u_i v_l with i+l=j.
- $a$ (first sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two input sequences, with entries $a_0, \dots, a_{q-1}$.
- $b$ (second sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two input sequences, with entries $b_0, \dots, b_{q-1}$.
- $q$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two sequences.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The sequence $a \ast b$ of the same length, whose entries are given by the cyclic convolution sum.
- $i$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index of the terms in the sum that defines each output entry.
- $t$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of the output entry $c_t$.
- $q$ (entry count), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of complex entries in each input and output vector.
- $j$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry, running from $0$ to $q-1$.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, the weight base of the transform.
- $F_q$ (discrete Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The normalized transform on vectors of length $q$, with $y = F_q x$.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ values on this page, not the integer inputs above.
- $y$ (output vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of $x$ on this page, not the integer inputs above.
- $l$ (entry index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an entry of $x$, running from $0$ to $q-1$.
- $m$ (integer exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent in a sum of powers of $\omega$.
- $a$ (first vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The first vector of the convolution, of length $q$.
- $b$ (second vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The second vector of the convolution, of length $q$.
- $t$ (shifted index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.
- $w$ (complex vector), bound on [Operator norm](operator-norm.md): A complex vector of length q, whose vector norm is taken.
- $L$ (linear map), bound on [Operator norm](operator-norm.md): A linear map from complex vectors to complex vectors, whose operator norm is taken.

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

- Cite or cut this step: "The weights in $S$ have Fourier transform constant $\alpha$, which cancels the $1/\alpha$ in $S$." (Claims the Fourier transform of the Gaussian weights and their normalisation without giving the transform or any way to check it.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Cite or cut this step: "Harvey and van der Hoeven bound them by $2^{-\alpha^2\theta}$, which shrinks as $\theta$ grows." (The page does not say the bound is on the operator norm of E, nor what hypotheses the cited lemma needs or why they hold; the conditions alpha^2 < p and theta > p/alpha^4 are used as if given.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Cite or cut this step: "and $\beta_i$ depends only on $i \bmod s$" (beta_i is used for all integers i, but the page only defines beta_j for 0 <= j < s, so the claim that beta_i depends only on i mod s is never justified from a stated construction.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Say what $\beta_i$ denotes where it is first used (for a size or count, what it counts): "e^{\pi\alpha^2\beta_i^2}u_i" (The page gives beta_j only for 0 <= j < s; for other indices it says only that beta_i depends on i mod s, without giving the construction.)
- Explain "Poisson summation" in a sentence where it is first used.
- Explain "Fourier series" in a sentence where it is first used.

## Previous version (revise it)

It has 407 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 508 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Gaussian resampling replaces a [discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. It replaces the transforms for the [radix-digit convolution](radix-digit-convolution.md) of two integers by such transforms. <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose</cite>

Let $s$ and $t$ be the numbers of coordinates of source and target vectors, with $\gcd(s,t)=1$ and $\theta=t/s-1$, the relative gap between the lengths. Here $u$ is a length-$s$ source vector, $b$ a length-$t$ target vector, and $j$ and $k$ index their entries. Let $F_s$ and $P_s$ be the normalized Fourier transform and the coordinate permutation $(P_su)_j=u_{tj}$ on length-$s$ vectors, and let $F_t$ and $P_t$ be the same on length-$t$ vectors with $(P_tb)_k=b_{-sk}$.

$S$ and $T$ are Gaussian-weighted maps from length-$s$ to length-$t$ vectors. The parameter $\alpha$ sets the width of their weights, which are bell-shaped functions that decay quickly away from their centres. $S$ gathers the entries of $u$ near $sk/t$, and $T$ spreads each $u_j$ over the targets near $tj/s$:
$$(Su)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$
where $u_j=u_{j \bmod s}$.

For $0\le j<s$, let $\ell_j$ be the integer nearest $tj/s$, ties rounded up, and $\beta_j=tj/s-\ell_j$. Let $C$ select coordinates, $(Cb)_j=b_{\ell_j}$, let $D$ be diagonal with $(Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$, and set $N=CTD$. Expanding,
$$(Nu)_j=\sum_{i\in\mathbb Z}e^{-\pi\alpha^2(ti/s-\ell_j)^2}e^{\pi\alpha^2\beta_i^2}u_i,$$
where $i$ is a summation index over all integers and $\beta_i$ depends only on $i \bmod s$. The term $i=j$ has $ti/s-\ell_j=\beta_j$, so its exponentials cancel and it equals $u_j$. The other terms form $N-I$, whose size is measured in the [operator norm](operator-norm.md) for the maximum-modulus vector norm.

These other terms are small. Harvey and van der Hoeven bound them by $2^{-\alpha^2\theta}$, which shrinks as $\theta$ grows. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite> Here $p$ is the integer precision of the cited lemma. Since $\alpha^2<p$ and $\theta>p/\alpha^4$, the bound is below $1/2$, as $\alpha^2\theta>p/\alpha^2>1$.

Write $N=I-E$, where $E=I-N$ is the error, and $\|E\|<1/2$. The Neumann series $\sum_{m\ge0}E^m$, with $m$ its summation index, has partial sums of norm at most $1/(1-\|E\|)<2$, since $\|E^m\|\le\|E\|^m$. Here $M$ is the last index of the partial sum $\sum_{m=0}^{M}E^m$, which multiplied by $I-E$ telescopes to $I-E^{M+1}$. Since $\|E^{M+1}\|\to0$, the series sums to $N^{-1}$, whose norm is less than $2$.

The Gaussian identity $TP_sF_s=P_tF_tS$ rests on Poisson summation: a sum of Gaussians over the integers is a Fourier series whose coefficients are Gaussians of reciprocal width. The weights in $S$ have Fourier transform constant $\alpha$, which cancels the $1/\alpha$ in $S$. The full bookkeeping is in Harvey and van der Hoeven, <cite data-source="paper">proved in [15, Theorem 4.2 and Lemma 4.6]</cite>.

Multiply $TP_sF_s=P_tF_tS$ on the left by $C$, and use $CT=ND^{-1}$, which holds since $D$ is invertible. This gives $ND^{-1}P_sF_s=CP_tF_tS$. Multiplying on the left by $N^{-1}$ and then by $D$ gives $P_sF_s=DN^{-1}C\,P_tF_tS$. This has the form $P_sF_s=BP_tF_tA$, where $A=S$ and $B=DN^{-1}C$ are maps. It is the form used on the [transform identity with retained permutations](transform-identity.md) page.

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

Write the body to `exegenius/tasks/0033-write-gaussian-resampling.answer.md` and the JSON to `exegenius/tasks/0033-write-gaussian-resampling.answer.json`, then run `exegenius submit 0033-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
