# exegenius task 0035-write-prime-source-lengths

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
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Chinese-remainder map (also: Agarwal–Cooley map)
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

Concept: Prime source lengths
Gloss: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.

## This page in the argument

The step: Distinct odd primes $s_1,\dots,s_d$ exist with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ for every axis $i$, and their product $S=\prod_i s_i$ satisfies $T/2<S<T$.
How: pick each $s_i$ as a prime in a prime-dense interval just below the padded length $t_i$, then bound the product of the ratios
Why: Each prime must be close to its power of two so that the product fills a fixed fraction of the padded box, and each ratio must leave room for resampling; a prime in a dense interval below $t_i$ meets both. (the sources say so: "fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling." (paper))
Striking feature: The product $S$ lies strictly between $T/2$ and $T$, a fixed fraction of the padded box, although each prime is chosen independently within its own interval. (explain why it holds, from the method)

Its sub-steps, in order:

- For $x\in\{r/2,r\}$ the interval $((1-2\eta)x,(1-\eta)x]$ contains more than $d$ primes.
- Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ can be chosen, one for each axis $i$, because the two intervals are disjoint and lie above $2$.
- Each $\gcd(s_i,t_i)$ equals one, since $t_i$ is a power of two.
- The product $S=\prod_i s_i$ satisfies $T/2<S<T$.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the first factor of the product.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): A binary string of length n, the second factor of the product.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the inputs x and y.
- $z$ (generic binary string), bound on [Exact integer multiplication](exact-integer-multiplication.md): An arbitrary binary string whose integer value is taken by val.
- $\mathrm{val}$ (integer value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation bin_k, that is, the length it pads to.
- $m$ (padded integer), bound on [Exact integer multiplication](exact-integer-multiplication.md): The nonnegative integer, below 2^k, whose binary representation is taken.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer, padded on the left with zeros to length k.
- $\#$ (input separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol placed between the two inputs x and y on the input tape, not a bit.
- $k$ (digit width), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in one digit; the letter changes meaning from the padded length on the earlier page.
- $B$ (radix), bound on [Radix-digit convolution](radix-digit-convolution.md): The base $2^k$ in which the digits of each integer are expanded.
- $d$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digit positions in each padded input.
- $x$ (first integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer represented by the first input string.
- $y$ (second integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer represented by the second input string.
- $x_j$ (digit of x), bound on [Radix-digit convolution](radix-digit-convolution.md): The $j$th radix-$B$ digit of the integer $x$, lying in $\{0,\dots,B-1\}$.
- $j$ (digit position), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a digit position, running over $0,\dots,d-1$.
- $l$ (second digit position), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a digit position in the second input, running over $0,\dots,d-1$.
- $m$ (coefficient position), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a coefficient of the product polynomial, running over $0,\dots,2d-2$; the letter changes meaning from the integer argument of $\mathrm{bin}_k$.
- $c_m$ (product coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The coefficient of position $m$ in the product polynomial of the two digit sequences.
- $L$ (axis length), bound on [Gaussian resampling](gaussian-resampling.md): The number of points along one axis of the transform being computed; it need not be a power of two.
- $u$ (point index), bound on [Gaussian resampling](gaussian-resampling.md): An index of a point along an axis, running over 0 to L-1.
- $v$ (second point index), bound on [Gaussian resampling](gaussian-resampling.md): A second index of a point along an axis, running over 0 to L-1, used with u in the Gaussian weights.
- $i$ (imaginary unit), bound on [Gaussian resampling](gaussian-resampling.md): The imaginary unit, with i squared equal to -1.
- $d$ (cyclic axis count), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of cyclic axes, which is the number of coordinates of a box point.
- $t_i$ (axis length), bound on [Chinese-remainder map](chinese-remainder-map.md): The number of positions along axis i; the lengths are pairwise coprime.
- $T$ (total positions), bound on [Chinese-remainder map](chinese-remainder-map.md): The total number of positions, the product of the axis lengths, which is the length of the cyclic convolution.
- $n$ (position), bound on [Chinese-remainder map](chinese-remainder-map.md): A position in the cyclic convolution, ranging over 0 to T-1.
- $\phi$ (Chinese-remainder map), bound on [Chinese-remainder map](chinese-remainder-map.md): The map sending a position to the tuple of its residues modulo the axis lengths.
- $u$ (first position), bound on [Chinese-remainder map](chinese-remainder-map.md): A position in the cyclic convolution, one of the two summed positions.
- $v$ (second position), bound on [Chinese-remainder map](chinese-remainder-map.md): A position in the cyclic convolution, the other of the two summed positions.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder map](chinese-remainder-map.md): A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
  Shown as: Prime source lengths *<predicate>* Chinese-remainder map
- [Gaussian resampling](gaussian-resampling.md): A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
  Shown as: Prime source lengths *<predicate>* Gaussian resampling

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "The distinct prime lengths si must be close to the powers of two ti" (paper)

  > The distinct prime lengths si must be close to the powers of two ti : their product must occupy a fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling. We verify both requirements for the parameters just chosen. The prime-interval result [15, Lemma 5.1], based on explicit estimates of Rosser and Schoenfeld [23], gives the following bound: for 0 < η < 1/4 and x > e2/η , the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes. Here log is the natural logarithm. The size bounds in (39) give d = Θ(pϵ ) and log r = Θ(p/d). For large n we have d ≥ 2, so 0 < η < 1/4, and log(r/2) = Θ(p1−2ϵ ) −→ ∞. d Thus both x = r/2 and x = r satisfy log x > 8d = 2/η. For either choice, the stated lower bound for the number of primes is x/(8d log x) and exceeds d: indeed, log x = Θ(p1−ϵ ), whereas log(8d2 log x) = O(log p) = o(log x), so x > 8d2 log x eventually. The two intervals are disjoint because (1 − η)r/2 < (1 − 2η)r for η < 1/4, and both intervals lie above 2. We may therefore choose distinct odd primes satisfying (1 − 2η)ti < si ≤ (1 − η)ti . Every gcd(si , ti ) equals one because ti is a power of two. Put S = bounds on si and applying strict Bernoulli inequality gives S 1 > 1− T 2d 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $i$ means axis index here, but imaginary unit on [Gaussian resampling](gaussian-resampling.md), which this page builds on: Prime-source-lengths is the later page: use another letter (for example j or a) for the axis index, since i is the imaginary unit on the gaussian-resampling page.
- $x$ means padded length variable here, but first integer on [Radix-digit convolution](radix-digit-convolution.md), which this page builds on: Prime-source-lengths is the later page: use another letter (for example X or L) for the real padded-length variable, since x is the integer represented by the first input on the radix-digit-convolution page. If x is kept, say here that it is a real padded length, not the integer input.
- $x$ means padded length variable here, but first input on [Exact integer multiplication](exact-integer-multiplication.md), which this page builds on: Prime-source-lengths is the later page: use another letter (for example X or L) for the real padded-length variable, since x is the binary input string on the exact-integer-multiplication page. If x is kept, say here that it is a real padded length, not an input string.

## Previous version (revise it)

It has 356 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 445 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Here $i$ indexes the $d$ axes, $i=1,\dots,d$, and $t_i$ is a power of two, the padded length of axis $i$. A prime source length is an odd prime $s_i$ chosen just below the padded length of its axis. Write $S=\prod_i s_i$ for the product of the source lengths and $T=\prod_i t_i$ for the padded box. The lengths $s_i$ are the moduli of the [Chinese-remainder map](chinese-remainder-map.md), which turns one cyclic convolution of length $S$ into a multidimensional one over the $s_i$. Distinct primes are pairwise coprime, which that map requires.

The primes are chosen so that $S$ fills a fixed fraction of $T$ and each ratio leaves room for resampling <cite data-source="paper">their product must occupy a fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling.</cite>. Take $\eta=1/(4d)$, which gives $0<\eta<1/4$ for $d\ge2$. Each prime is taken in the window $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, so each ratio $s_i/t_i$ lies in $(1-2\eta,1-\eta]$. The primes are sized for [Gaussian resampling](gaussian-resampling.md), which needs each ratio $t_i/s_i$ to leave separation.

Let $x$ be a real number standing for a padded length; the letter $x$ means an input string on earlier pages, and it changes meaning here. Let $q$ denote a prime. For $0<\eta<1/4$ and $x>e^2/\eta$, the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes <cite data-source="paper">the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes</cite>, where $\log$ is the natural logarithm.

The construction takes each $t_i$ to be $x$ or $2x$ for a large power of two $x$. With $\eta=1/(4d)$ the count is $x/(8d\log x)$, which exceeds $d$ for large $x$, so each window holds more than $d$ primes. The windows for $x$ and $2x$ are disjoint, since $(1-\eta)x<(1-2\eta)2x$ when $\eta<1/3$. Axes with different padded lengths therefore take primes from disjoint windows, and axes with the same padded length can be given distinct primes one at a time. Each $s_i$ is odd because the windows lie above $2$, and $\gcd(s_i,t_i)=1$ because $t_i$ is a power of two.

Let $S/T=\prod_i s_i/t_i$. Each factor exceeds $1-2\eta$, so $S/T>(1-2\eta)^d$. The strict Bernoulli inequality says that for $d\ge2$ a product of $d$ factors $1-2\eta$ exceeds $1-2d\eta$; induction on $d$ shows this. With $\eta=1/(4d)$ we have $1-2d\eta=1/2$, so $S/T>1/2$. Each factor is at most $1-\eta$, so $S/T\le(1-\eta)^d<1$. Hence $T/2<S<T$.

The product lands in this range although the primes are chosen independently, because each ratio is pinned in a window just below one: every ratio is below $1-\eta$, and together the $d$ ratios stay above $1-2d\eta$.

For example, take $d=2$, $t_1=8$, $t_2=16$, so $\eta=1/8$. The windows are $(6,7]$ and $(12,14]$, which hold $s_1=7$ and $s_2=13$. Then $S=91$, $T=128$, and $64<91<128$.

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

Write the body to `exegenius/tasks/0035-write-prime-source-lengths.answer.md` and the JSON to `exegenius/tasks/0035-write-prime-source-lengths.answer.json`, then run `exegenius submit 0035-write-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
