# exegenius task 0026-write-chinese-remainder-map

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

Concept: Chinese-remainder map
Gloss: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
Also called: Agarwal–Cooley map

## Where the argument relies on this page

- Distinct odd primes $s_1,\dots,s_d$ exist with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ for every axis $i$, and their product $S=\prod_i s_i$ satisfies $T/2<S<T$. (on [Prime source lengths](prime-source-lengths.md))
- Each $\gcd(s_i,t_i)$ equals one, since $t_i$ is a power of two.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Chinese-remainder map *<predicate>* Radix-digit convolution

## Pages that build on this one

- Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Prime source lengths](prime-source-lengths.md)

## Evidence from the sources, with the paragraph around each quote

- "a Chinese-remainder map that preserves convolution" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section 9 implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section 8 retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts. Next, Bluestein’s chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo y r + 1; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections 6 and 7 compute convolution on the remaining axes over this polynom


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Relabeling the coefficients by $\phi$ therefore turns the cyclic convolution of length $T$ into the $d$-dimensional cyclic convolution on the box" (The page asserts with "therefore" that relabeling by phi turns the length-T cyclic convolution into a d-dimensional box convolution, but it never writes out the summation or the coefficient identity. The reader knows only 1-D cyclic convolution, so the claim that the sum over u+v mod T regroups into the per-axis wraparound sum over the box cannot be checked from the page.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.

## Previous version (revise it)

It has 204 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 255 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The Chinese-remainder map relabels cyclic positions so that one cyclic convolution becomes a convolution over a box of several cyclic axes, which lets later steps treat each axis on its own.

Let $d$ be the number of cyclic axes. Each $t_i$ is the number of positions along axis $i$, and the lengths $t_1,\dots,t_d$ are pairwise coprime. Put $T = t_1 t_2 \cdots t_d$, which is the total number of positions.

The map $\phi$ sends a position $n$, for $0 \le n < T$, to the tuple of its residues:

$$\phi(n) = (n \bmod t_1,\dots,n \bmod t_d).$$

The Chinese remainder theorem says $\phi$ is a bijection, and it respects sums: for each axis $r$, the $r$th coordinate of a sum of two positions is the sum of their $r$th coordinates, reduced modulo $t_r$. So a product term at positions $u$ and $v$ lands, after relabeling, at the box point $\phi(u)+\phi(v)$, with each coordinate reduced modulo its axis length. Relabeling the coefficients by $\phi$ therefore turns the cyclic convolution of length $T$ into the $d$-dimensional cyclic convolution on the box $t_1\times\cdots\times t_d$, in which each axis wraps around independently.

Example. Take $T=6=2\cdot 3$, so $t_1=2$ and $t_2=3$. The map sends $0,1,2,3,4,5$ to $(0,0)$, $(1,1)$, $(0,2)$, $(1,0)$, $(0,1)$, $(1,2)$. Check $u=2$ and $v=5$: $(u+v) \bmod 6 = 1$, and $(0,2)+(1,2)=(1,1)$ coordinatewise, which is $\phi(1)$.

The map is applied to the coefficient list of [Radix-digit convolution](radix-digit-convolution.md). The paper uses it this way. <cite data-source="paper">the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>.

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

Write the body to `exegenius/tasks/0026-write-chinese-remainder-map.answer.md` and the JSON to `exegenius/tasks/0026-write-chinese-remainder-map.answer.json`, then run `exegenius submit 0026-write-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
