# exegenius task 0022-write-fast-address-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/B4` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, algorithms (including divide and conquer, sorting, and the basic idea of fast multiplication), basic Turing machines, and the supporting mathematics of linear algebra, discrete math, probability-free basics, and complex numbers. They have not studied the FFT in depth, algebraic complexity, polynomial rings modulo relations, number theory beyond modular arithmetic and CRT basics, or numerical error analysis, and they know nothing of the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n conjecture and history
- Discrete Fourier transform and convolution
- Multiplication as convolution of radix digits
- Established O(n log n) multiplier (subroutine)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Polynomial ring modulo y^r + 1
  - $r$ (ring size): A power of two giving the number of complex coefficients in a polynomial of the ring.
  - $y$ (ring variable): The indeterminate of the polynomials, satisfying y^r = -1.
- Coefficient twist from cyclic to negacyclic
- Synthetic polynomial transform
- Two-point butterfly H₀
- Tape streams, array order and elementary scans
- Linear network with roles and frames
- Subset-intersection subspace labels
- Recursive power saving from rank deficit
- Lower triangular (Bruhat-type) factorization and matrix shear
- Fixed-point dyadic precision and exact recovery
- Linear algebra basics (also: vectors, matrices, linear maps, rank, invertible matrix, tensor-free linear algebra)
- Modular arithmetic (also: congruences, mod n, residues, remainder)
- Prime numbers and coprimality (also: primes, gcd, coprime, relatively prime, prime number theorem)
- Binary representation and radix expansion (also: base 2, bits, radix 2^b, binary digits, positional notation)
- Schoolbook multiplication and carries (also: long multiplication, quadratic multiplication, carry propagation, O(n^2) multiplication)
- Divide and conquer and recurrences (also: recurrence relations, master theorem, recursion, Karatsuba)
- Sorting and its cost (also: sort, permuting data, comparison sort, O(n log n) sorting)
- Logarithms and exponentials (also: lg, log base 2, log log, iterated logarithm)
- Cartesian product and mixed-radix indexing (also: multi-dimensional array, tensor index, row-major order, axes of an array)
- Cyclic groups and roots of unity (also: Z/mZ, cyclic group, additive group of integers mod m)
- Euclidean norm and unit disk (also: modulus, absolute value of complex number, unit disk, norm, triangle inequality)
- Fixed-point and rounding arithmetic (also: truncation, rounding error, floor and ceiling, dyadic rationals)
- Proof by induction and summation (also: geometric series, induction, telescoping sums)
- Subsets, indicator vectors and set intersection (also: characteristic vector, binomial coefficient, k-element subsets)
- Permutation matrices (also: permutations, partial permutation, bijection)
- Euler's formula and trigonometry (also: e^{i theta}, cos and sin, pi)
- Gaussian function (also: Gaussian, bell curve, e^{-x^2})
- Big-endian bit strings and Boolean operations (also: XOR, bitwise exclusive or, bit position)
- Rational numbers and field arithmetic (also: Q, rational field, fractions)

## This page

Concept: Fast interchange of address chunks
Gloss: Interchanging two contiguous address fields of u bits in a Cartesian-product array, by XOR/shear combinations through the bit network, at cost O(V u^τ) for fixed τ < 1.
Heading: Fast address interchange at cost $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of stored bits in the array.
- $u$ (field width): The number of bits in each of the two address fields being interchanged.
- $\tau$ (saving exponent): A fixed constant below 1 giving the power of u in the cost.

## This page in the argument

The step: Two address fields of $u$ bits can be interchanged at cost $O(Vu^\tau)$.
How: express each edge matrix of the network by shears, factor them, and recurse on smaller interchanges
Why: An edge matrix of rank a requires only a smaller interchanges once it is factored, so the rank saving of the network turns into a recurrence saving a power of the chunk width. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Every rational matrix of rank $a$ factors as $E_1\Pi E_2$ with lower triangular $E_i$ so a shear costs $a$ interchanges plus linear-time updates. (on [Lower triangular (Bruhat-type) factorization and matrix shear](lower-triangular-factorization.md))
- Chunks of power-of-two width can be interchanged, with rows, in time $O(Vu^\tau)$.
- The restrictions on width and rows are removed for arbitrary chunk width.

It serves these steps, from the main result down:

- There is a deterministic fixed multitape Turing machine multiplying $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two fast tape procedures, use them for synthetic and resampled transforms, and assemble the exact product through convolution (on [Multiplication in O(n (lg n)^{1-κ}) time](main-theorem.md))
- Two tape procedures, an address interchange of cost $O(Vu^\tau)$ and a simultaneous butterfly layer of cost $O(Vd^{\lambda'})$, exist for volume $V$ with fixed $\tau,\lambda'<1$.; how: build both from fixed linear networks with a rank saving, applied recursively

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.5.2, S1.5.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.5.2**: Chunks of power-of-two width can be interchanged, with rows, in time $O(Vu^\tau)$.
Source: "\begin{proposition}[Power-width interchange with rows]" (paper)
> \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

**S1.5.3**: The restrictions on width and rows are removed for arbitrary chunk width.
Source: "\begin{lemma}[Arbitrary-width interchange]" (paper)
> \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.5.1 (on [Lower triangular (Bruhat-type) factorization and matrix shear](lower-triangular-factorization.md)): Every rational matrix of rank $a$ factors as $E_1\Pi E_2$ with lower triangular $E_i$ so a shear costs $a$ interchanges plus linear-time updates.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving from rank deficit](recursive-saving.md): A call at parameter m·f uses s < W·m calls at parameter f on volume V/W, so normalized cost grows by factor s/W < m per level, giving cost V·(parameter)^{τ} with τ < 1.
  Shown as: Fast interchange of address chunks *<predicate>* Recursive power saving from rank deficit
- [Lower triangular (Bruhat-type) factorization and matrix shear](lower-triangular-factorization.md): Every rational matrix of rank a factors as E₁ΠE₂ with E_i lower triangular and Π a partial permutation with a ones, so a shear costs only a smaller interchanges plus linear-time updates.
  Shown as: Fast interchange of address chunks *<predicate>* Lower triangular (Bruhat-type) factorization and matrix shear

## Pages that build on this one

- Simultaneous butterfly layer: Applying H₀ at the same bit position of up to d address chunks at once on records of complex fixed-point polynomials, using the complex phase network, at cost O(V d^λ′).
- Resampling with permutations left in the transform: Keeping the source and target coordinate permutations inside the transform identity so they cancel across the forward and inverse transforms instead of being executed as sorts.
- Fixed rational parameter choice: The conservative constants (τ, λ, λ′, ε, δ, κ = 2^{-182}) chosen compatibly so all terms in the cost table fit the main bound.

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Discrete Fourier transform and convolution](dft-convolution.md)
- [Multiplication as convolution of radix digits](radix-digit-reduction.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Two-point butterfly H₀](butterfly-h0.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Fixed-point dyadic precision and exact recovery](fixed-point-precision.md)
- [Chinese-remainder map to prime cyclic axes](cyclic-crt.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Coefficient twist from cyclic to negacyclic](coefficient-twist.md)
- [Established O(n log n) multiplier (subroutine)](hvdh-multiplier.md)
- [Tape streams, array order and elementary scans](stream-operations.md)
- [Linear network with roles and frames](linear-network-frames.md)
- [Subset-intersection subspace labels](subset-intersection-labels.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Resampling with permutations left in the transform](resampling-keep-permutations.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Exact normalized convolution over the polynomial ring](ring-convolution.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Complete multiplication algorithm and cost](multiplication-algorithm.md)
- [Multiplication in O(n (lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields
of $u$ bits" (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

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

Write the body to `exegenius/tasks/0022-write-fast-address-interchange.answer.md` and the JSON to `exegenius/tasks/0022-write-fast-address-interchange.answer.json`, then run `exegenius submit 0022-write-fast-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
