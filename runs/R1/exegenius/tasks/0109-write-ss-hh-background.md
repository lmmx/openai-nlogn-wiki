# exegenius task 0109-write-ss-hh-background

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers (also: Gaussian integer)
- Multitape Turing machine
- Fixed-tape machine model and stream operations (also: fixed-tape machine)
- Convolution
- Discrete Fourier transform and butterflies (also: transform (the DFT/FFT the layout is for), twiddle factor, bit-reversed input, forward transform of length S)
- The n log n optimality conjecture
- Reduction of integer product to digit convolution
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map, norm)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Schönhage–Strassen to Harvey–van der Hoeven multiplication
Gloss: Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.

## Where the argument relies on this page

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$. (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $A$ (fixed machine), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The paper's deterministic Turing machine that multiplies integers.
- $T_A$ (running time of A), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The worst-case running time of the machine A on pairs of n-bit inputs.
- $\kappa$ (savings exponent), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The fixed positive constant 2^{-182} that gives the exponent of the logarithm in the bound.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input, $\lceil n/b\rceil$.
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $x$, an integer with $0\le x_j<2^b$.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $y$, an integer with $0\le y_j<2^b$.
- $c_k$ (digit coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution, the sum of $x_i\,y_j$ over all $i+j=k$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation, a nonnegative integer.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$, with $0\le d_k<2^b$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element, a power of two.
- $j$ (rule index), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The index of the coefficient that the wrap rule $y^{r+j}=-y^j$ reduces to, ranging over $0\le j<r$.
- $k$ (shift exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of the power $y^k$ that acts as a signed shift, with $0\le k<r$.
- $L$ (axis length), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $m$ (cell position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in the array, which is also its address written in binary.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits the array holds in total.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\ne1$ for $0<m<n$.
- $m$ (frequency index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $a$: the list of $n$ entries $A_m$ defined by the sum.
- $u$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The first input of a butterfly.
- $v$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The second input of a butterfly.
- $s$ (butterfly exponent), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The exponent of the power $\omega^s$ that a butterfly applies to its second input.
- $E$ (even-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the even-indexed entries of $a$.
- $O$ (odd-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $h$ (block length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of entries in a block at a level.
- $t$ (block offset), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The offset of an entry within a block.
- $B$ (transform of b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $b$.
- $C$ (transform of c), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the cyclic convolution $c$.
- $l$ (paired index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index into $b$ paired with $i$ at output $k$, $l=(k-i)\bmod n$.
- $d$ (index difference), bound on [Discrete Fourier transform and butterflies](dft-fft.md): An integer, the difference of two output indices in the inverse sum.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform and butterflies](dft-fft.md): Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
  Shown as: Schönhage–Strassen to Harvey–van der Hoeven multiplication *<predicate>* Discrete Fourier transform and butterflies
- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers.
  Shown as: Schönhage–Strassen to Harvey–van der Hoeven multiplication *<predicate>* The n log n optimality conjecture

## Pages that build on this one

- Signed coefficient packing (Kronecker substitution): Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier.

## Other pages you may link to

- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper" (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Cite or cut this step: "this recursion produces the extra $\log\log n$ factor" (The page does not say how large the entrywise products are (the sizes of the sub-integers are never given), so the reader cannot calculate that the recursion yields exactly one extra log log n factor. The claim is presented as following from the scheme but is not derivable from what the page gives.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- The reader cannot follow this step: "$y$ is a root of unity of order $2r$, since $y^r=-1$" (The stated reason y^r = -1 gives y^(2r) = 1 but does not show that no smaller positive power of y equals 1 in the ring. Minimality of the order is not argued, and the reader cannot check it from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.

## Previous version (revise it)

It has 292 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 365 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Schönhage–Strassen to Harvey–van der Hoeven multiplication is a chain of multitape algorithms that lowers the cost of multiplying two integers from $O(n\log n\log\log n)$ to $O(n\log n)$. The main theorem's power saving is measured against the ends of this chain. Here $n$ is the number of bits in each integer being multiplied.

Schönhage and Strassen showed that two $n$-bit integers can be multiplied <cite data-source="paper">in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. Each algorithm in the chain computes its transforms by the [Discrete Fourier transform and butterflies](dft-fft.md), evaluating its coefficient lists at roots of unity in a suitable ring.

The method splits each integer into $q$ digits of $b$ bits, so the product is a convolution of two digit lists with $q$ entries each. That linear convolution has $2q-1$ coefficients. Padding the lists to a power of two $S \ge 2q-1$ makes the cyclic convolution of length $S$ equal to the linear one, because no coefficient wraps around. Transform both padded lists, multiply the transforms entry by entry, and invert the transform. The entrywise products are products of shorter integers, handled by the same method; this recursion produces the extra $\log\log n$ factor. Their proof is in Schönhage and Strassen's paper.

Later algorithms keep this scheme and change the ring. Fürer's 2007 bound replaces the factor $\log\log n$ by $2^{O(\log^* n)}$. Later improvements reduced the exponential factor to $8^{\log^* n}$ and then $4^{\log^* n}$. Harvey and van der Hoeven removed it, obtaining an unconditional algorithm with running time $O(n\log n)$ <cite data-source="paper">reached the unconditional $O(n\log n)$ upper bound</cite>.

In the ring modulo $y^r+1$, $y$ is a root of unity of order $2r$, since $y^r=-1$, and multiplying by a power of $y$ is a cyclic shift with sign changes. This is why the later stages use such rings.

The $O(n\log n)$ bound matches the order Schönhage and Strassen proposed, but as an upper bound it does not show that $n\log n$ is optimal. The chain's cost is measured against the [The n log n optimality conjecture](nlogn-conjecture.md).

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
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
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
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

Write the body to `exegenius/tasks/0109-write-ss-hh-background.answer.md` and the JSON to `exegenius/tasks/0109-write-ss-hh-background.answer.json`, then run `exegenius submit 0109-write-ss-hh-background` in the project directory. If submit rejects the answer, fix the answer and submit again.
