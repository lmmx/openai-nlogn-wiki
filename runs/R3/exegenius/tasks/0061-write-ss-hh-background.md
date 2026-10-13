# exegenius task 0061-write-ss-hh-background

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
- Discrete Fourier transform and butterflies
- The n log n optimality conjecture
- Reduction of integer product to digit convolution
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Fixed-point precision and exact recovery
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map)
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

- $n$ (input length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $n$ (input bit length), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The bit length of each input, the number of bits in each of the two integers.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first $n$-bit input integer.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second $n$-bit input integer.
- $x_j$ (digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $x$.
- $y_j$ (digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $y$.
- $c_k$ (product coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution of $x$ and $y$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $p$ (working precision), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of fractional bits in each fixed-point numerator, so values are stored over the denominator $2^p$.
- $S$ (cyclic convolution length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of coefficients in the cyclic convolution whose transforms are computed.
- $c_j$ (product coefficient), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The exact integer coefficient of the product at index $j$.
- $b$ (digit width), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of bits in each radix digit, equal to the ceiling of the base-2 logarithm of the input length $n$.
- $d_j$ (output digit), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The radix-$2^b$ digit of the product at position $j$.
- $k_j$ (carry), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The carry from the processed coefficients into position $j$.
- $u$ (address field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field, a count of bits.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds, a count of stored bits.
- $n$ (input size), bound on [Address fields and array layout on tapes](address-fields.md): The size of the input, so that the array holds $\Theta(n)$ bits.
- $n$ (list length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of coefficients in the list $a$, a power of two.
- $a$ (coefficient list), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ complex coefficients $a_0,\dots,a_{n-1}$ being transformed.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\neq 1$ for $0<m<n$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ values $A_0,\dots,A_{n-1}$ obtained by evaluating $a$ at the powers of $\omega$.

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
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper" (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Schönhage and Strassen showed that two $n$-bit integers can be multiplied (cited)" (The cited result is stated only as 'can be multiplied'. The page never says what running time it achieves, so the reader cannot tell the chain's starting bound, which the page itself says the reader needs.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Each algorithm in the chain computes its transforms by the" (The page asserts that every algorithm in the chain uses the DFT, but it names and describes none of the intermediate algorithms ('After a sequence of improvements'). The reader cannot check this claim from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "so the digit convolution of an integer product is handled in the same way" (The page does not state which convolution the transform computes (cyclic or linear) or what transform length is needed so that the full digit product is recovered without wraparound. The reader cannot check that the pointwise-product method yields the integer product.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.

## Previous version (revise it)

It has 253 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 316 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The concept is a chain of multiplication algorithms, from Schönhage and Strassen (1971) to Harvey and van der Hoeven, that multiplies two integers on a multitape Turing machine and whose cost is measured in bits. The main theorem gives a power saving in the logarithmic factor, so the reader needs this chain's starting and ending bounds and the method they share.

Here $n$ is the number of bits in each integer being multiplied.

Schönhage and Strassen showed that two $n$-bit integers can be multiplied <cite data-source="paper">in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. They proposed $n\log n$ as the optimal order of growth.

Each algorithm in the chain computes its transforms by the [Discrete Fourier transform and butterflies](dft-fft.md), which evaluates a coefficient list at roots of unity using logarithmically many levels of two-point butterfly operations. Convolution then becomes a pointwise product of two transforms followed by an inverse transform, so the digit convolution of an integer product is handled in the same way.

The later steps of the chain work over rings in which roots of unity are cheap to multiply by. In the ring modulo $y^r+1$, the variable $y$ is a root of unity of order $2r$, and multiplying by a power of $y$ is a cyclic shift with sign changes.

After a sequence of improvements, Harvey and van der Hoeven reached an unconditional algorithm with running time $O(n\log n)$ <cite data-source="paper">reached the unconditional $O(n\log n)$ upper bound</cite>. This is an upper bound. It matches the order Schönhage and Strassen proposed, but it does not by itself show that $n\log n$ is optimal. Its cost is measured against the [The n log n optimality conjecture](nlogn-conjecture.md).

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

Write the body to `exegenius/tasks/0061-write-ss-hh-background.answer.md` and the JSON to `exegenius/tasks/0061-write-ss-hh-background.answer.json`, then run `exegenius submit 0061-write-ss-hh-background` in the project directory. If submit rejects the answer, fix the answer and submit again.
