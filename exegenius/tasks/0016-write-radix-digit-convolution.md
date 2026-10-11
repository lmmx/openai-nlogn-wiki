# exegenius task 0016-write-radix-digit-convolution

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

For these sources: This reader has an undergraduate computer science degree: discrete mathematics (modular arithmetic, gcd and primes, binomial counting, induction), linear algebra over the reals and small fields (subspaces, rank, elimination, eigenvalues, dot-product orthogonal complements and projections), and algorithms (divide-and-conquer recurrences, Karatsuba multiplication, and the DFT and cyclic convolution as used for FFT-based polynomial multiplication). Complex numbers are known as far as roots of unity and Gaussian integers, Turing machines are known with multiple tapes, and basic probability reaches the union bound. Tensor products, bilinear forms beyond the dot product, quotient rings and the sources' network and address constructions are not part of this background.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution
- Carry propagation
- Vector spaces, subspaces, bases and dimension (also: linear subspace, span, basis, linear independence, dimension of a vector space)
- Rank of a matrix (also: row rank, column rank, dimension of the column space)
- Invertible matrices and inverses (also: nonsingular matrix, matrix inverse, identity matrix, diagonal matrix)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, elementary matrix, lower triangular matrix, upper triangular matrix)
- Eigenvalues and diagonalization (also: eigenvector, eigendecomposition, characteristic polynomial, diagonalizable matrix)
- Dot product, orthogonal complement and projection (also: inner product, orthogonal projection, perpendicular subspace, orthogonal complement)
- Permutations and permutation matrices (also: permutation of coordinates, reordering of indices, permutation matrix)
- Modular arithmetic (also: congruence modulo q, residue classes, clock arithmetic, Z/qZ, residue ring)
- Greatest common divisor and coprimality (also: gcd, relatively prime, Euclid's algorithm, extended Euclidean algorithm, Bezout identity)
- Prime numbers (also: primes, odd prime, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remainder theorem for coprime moduli)
- Binary field GF(2) (also: F2, F_2, Z/2Z, XOR arithmetic, binary field)
- Hamming weight (also: popcount, number of ones, weight of a binary string, Hamming norm)
- Indicator vector of a set (also: characteristic vector, characteristic function, incidence vector, indicator function)
- Binomial coefficients (also: n choose k, binomial coefficient, number of k-element subsets)
- Positional and mixed-radix notation (also: radix representation, base-b expansion, mixed radix, mixed-radix digits, place value)
- Dyadic rationals (also: binary fractions, binary fixed-point numbers, dyadic numbers)
- Gaussian integers (also: Z[i], ring of Gaussian integers)
- Roots of unity (also: nth root of unity, primitive nth root of unity, complex roots of unity)
- Mathematical induction (also: induction, strong induction, proof by induction)
- Recurrence relations and geometric sums (also: recursion unrolling, divide-and-conquer recurrence, recursion tree, geometric series, geometric sum)
- Iterated logarithm (also: log star, log*, iterated log)
- Logarithms, floor and ceiling (also: lg, log base 2, log2, floor function, ceiling function)
- Union bound (also: Boole's inequality, sum of probabilities bound)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba-Ofman multiplication, three-product splitting)

## This page

Concept: Radix-digit convolution
Gloss: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## Where the argument relies on this page

- Distinct odd primes $s_1,\dots,s_d$ exist with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ for every axis $i$, and their product $S=\prod_i s_i$ satisfies $T/2<S<T$. (on [Prime source lengths](prime-source-lengths.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): One of the two binary input strings, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The other binary input string, of length $n$.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string, counting the bits of $x$ and of $y$ separately.
- $\mathrm{val}$ (integer value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $m$ (integer argument), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer that is written in binary by $\mathrm{bin}_k$, and is below $2^k$.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation $\mathrm{bin}_k(m)$.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer, padded on the left with zeros to $k$ bits.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Radix-digit convolution *<predicate>* Exact integer multiplication

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.

## Other pages you may link to

- [Gaussian resampling](gaussian-resampling.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements,


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $l$ denotes where it is first used (for a size or count, what it counts): "\sum_{j+l=m} x_j y_l" (The page never says that l is a position index or what range it takes; the reader can only infer it as a dummy index of the sum, by analogy with j.)

## Previous version (revise it)

It has 228 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 285 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, a form that fast convolution methods can evaluate. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

Fix a digit width $k$, the number of bits in one digit. Let $B = 2^k$ be the radix. Pad both inputs to $d$ digits, where $d$ is a count: the number of digit positions in each input.

For integers $x$ and $y$, let $x_j$ and $y_j$ be the $j$th digits of $x$ and $y$, each in $\{0,\dots,B-1\}$. Then
$$x=\sum_{j=0}^{d-1}x_jB^j,\qquad y=\sum_{j=0}^{d-1}y_jB^j.$$
So multiplying the integers is the same as multiplying the polynomials whose coefficient lists are these digits, and then evaluating the product at $B$. The product polynomial has the coefficient $c_m = \sum_{j+l=m} x_j y_l$ at each position $m$, the convolution of the two digit sequences, and $xy = \sum_m c_m B^m$.

The convolution is the expensive part. The sources compute it with Fourier transforms, and later pages replace these by transforms whose lengths are powers of two. The coefficients are short: each term $x_j y_l$ is at most $(B-1)^2 < 2^{2k}$, and $c_m$ has at most $d$ terms, so $c_m < d\,2^{2k}$, about $2k + \lg d$ bits.

The integer is recovered from the $c_m$ by carry propagation. For example, take $k=2$, so $B=4$, with $x=11$ and $y=6$. Their digits are $x_0=3$, $x_1=2$, $y_0=2$, $y_1=1$, giving $c_0=6$, $c_1=7$, $c_2=2$. As a check, $6+7\cdot 4+2\cdot 16=66=11\cdot 6$. Carrying from the lowest position: $6=1\cdot 4+2$ writes $2$ and carries $1$; $7+1=8=2\cdot 4$ writes $0$ and carries $2$; $2+2=4=1\cdot 4$ writes $0$ and carries $1$; the last carry is the top digit $1$. The digits from lowest to highest are $2,0,0,1$, which is $66$.

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

Write the body to `exegenius/tasks/0016-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0016-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0016-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
