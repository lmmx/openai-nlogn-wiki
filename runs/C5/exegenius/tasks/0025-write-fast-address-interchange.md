# exegenius task 0025-write-fast-address-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/C5` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis, algorithm design basics (divide and conquer, recurrences, schoolbook and Karatsuba multiplication), discrete mathematics (modular arithmetic, primes, induction, permutations), and linear algebra and calculus at the usual first-course level. They know polynomials, complex numbers with roots of unity, and simple Turing machines with tapes. They have not studied the FFT in depth, Fourier analysis on groups, tensor products, numerical analysis, or fast integer multiplication research.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- The n log n conjecture and history
  - $n$ (input length): The number of bits of each multiplicand.
- Established O(n log n) multiplier
  - $n$ (input length): The number of bits of each multiplicand in the subroutine call.
- Discrete Fourier transform and roots of unity
- Convolution and the convolution theorem
- Multidimensional transforms
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial; a power of two.
- Synthetic polynomial transforms
- Phase twist to the negative-wrap ring
- Signed packing (Kronecker substitution)
- Fixed-point complex coefficients and exact recovery
- Array addresses, fields and tape layout
- Linear networks with restored auxiliary values
- Frames of a linear network
- Subset-intersection subspace labels
- Recursive power saving from s<Wm
- Address shear and triangular factorization
- Two-point butterfly H₀
  - $H_0$ (butterfly map): The map sending a pair to its half-sum and half-difference.
  - $u$ (first input): The first value of the pair.
  - $v$ (second input): The second value of the pair.
- Logarithms and iterated logarithm notation (also: lg, log base 2, log n, lg n)
- Floor, ceiling and rounding (also: floor, ceiling, nearest integer)
- Binary representation and bit operations (also: bits, binary expansion, XOR, bitwise exclusive or, bit fields)
- Radix (base-b) expansion (also: digits in base b, positional notation, radix digits)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, carry propagation)
- Divide and conquer recurrences (also: recurrence relations, master theorem, Karatsuba)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/NZ)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd, coprime)
- Permutations and bijections (also: rearrangement, one-to-one correspondence, bijective map)
- Vectors, matrices and linear maps (also: linear operator, invertible matrix, matrix inverse, linear combination, linear algebra)
- Subspaces, dimension and rank (also: linear subspace, span, rank of a matrix, basis)
- Vector spaces over GF(2) (also: binary vectors, F_2, bit vectors, mod 2 linear algebra)
- Triangular matrices and elimination (also: lower-triangular matrix, Gaussian elimination, LU factorization)
- Norms and triangle inequality (also: absolute value of complex number, modulus, magnitude, vector norm, error bound)
- Exponential function and Euler's formula (also: e^{i theta}, complex exponential, exp, Gaussian function)
- Fixed-point and finite-precision numbers (also: dyadic rationals, truncation, rounding error, binary fractions)
- Direct sum and product of index sets (also: Cartesian product, multi-index, array indexing, row-major order)
- Deterministic algorithms and upper/lower bounds (also: deterministic, worst-case time, upper bound, optimality)
- Induction and proofs by recursion (also: mathematical induction, recursive argument, inductive proof)
- Constants, exponents and power-of-two sizes (also: power of two, 2^k, padding to a power of two)

## This page

Concept: Fast interchange of address fields
Gloss: Swaps two disjoint contiguous u-bit address fields of an array of stored volume V in cost O(V u^τ), τ<1, using XOR combinations whose final effect is an exact permutation.
Heading: Fast interchange of address fields in cost $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of stored bits in the array.
- $u$ (field width): The number of bits in each interchanged address field.
- $\tau$ (savings exponent): A fixed constant below 1 controlling the cost.

## This page in the argument

The step: Two disjoint contiguous $u$-bit address fields of an array of volume $V$ can be swapped in cost $O(Vu^\tau)$ with $\tau<1$.
How: Apply the bit network whose endpoint operator is an address shear, completed by a triangular factorization, recursing on smaller interchanges
Why: Plain permutation of fields costs more than scanning; XOR combinations through the network permit recursion that saves a power of the width. (the sources leave this for the reader to work out: spell it out)
Striking feature: The final effect is an exact permutation although intermediate steps form XOR combinations of data. (explain why it holds, from the method)

Its sub-steps, in order:

- The endpoint operator $(H,D)\mapsto(H+D,D)$ is a shear, and a lower-triangular factorization lets two further linear updates complete the interchange. (on [Address shear and triangular factorization](address-shear.md))
- For power widths the recursion gives interchange cost $O(Vu^\tau)$.
- Padding removes the width and row restrictions.

It serves these steps, from the main result down:

- One fixed-tape Turing machine multiplies n-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Beat the $n\log n$ cost of transform-based multiplication by making the two tape operations (address rearrangement and butterfly layers) cost a power of their width less than a full scan, then plug them into the Harvey-van der Hoeven resampling reduction (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2, S3.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2**: For power widths the recursion gives interchange cost $O(Vu^\tau)$.
Source: "\begin{proposition}[Power-width interchange with rows]" (paper)
> \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

**S3.3**: Padding removes the width and row restrictions.
Source: "\begin{lemma}[Arbitrary-width interchange]" (paper)
> \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Address shear and triangular factorization](address-shear.md)): The endpoint operator $(H,D)\mapsto(H+D,D)$ is a shear, and a lower-triangular factorization lets two further linear updates complete the interchange.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving from s<Wm](recursive-saving.md): A call at parameter mf makes s<Wm calls at parameter f on volume V/W streams, so per-volume cost grows by a factor below m, giving a power saving.
  Shown as: Fast interchange of address fields *<predicate>* Recursive power saving from s<Wm
- [Address shear and triangular factorization](address-shear.md): The endpoint operator (H,D)↦(H+D,D) on address fields; a rank-reducing lower-triangular factorization lets two further linear updates complete an interchange.
  Shown as: Fast interchange of address fields *<predicate>* Address shear and triangular factorization

## Pages that build on this one

- Fast simultaneous butterfly layers: Applies H₀ simultaneously on the same selected bit of at most d address chunks in cost O(V d^λ′), via the linear network with phase frames and a single final truncation.
- Resampling with permutations left in the transform: The source and target coordinate permutations stay inside the transform identity and cancel across forward, product and inverse transforms instead of being sorted separately.
- Synthetic transforms with retained frequency order: Forward synthetic transforms keep the same frequency order through their pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y-r-plus-1.md)
- [Discrete Fourier transform and roots of unity](dft-roots-of-unity.md)
- [Convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transforms](multidimensional-transform.md)
- [Two-point butterfly H₀](butterfly-layer.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase twist to the negative-wrap ring](phase-twist.md)
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [The n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier](hh-multiplier.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Array addresses, fields and tape layout](address-fields-layout.md)
- [Linear networks with restored auxiliary values](linear-network.md)
- [Frames of a linear network](frames.md)
- [Subset-intersection subspace labels](subset-subspace-labels.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Resampling with permutations left in the transform](retained-permutations.md)
- [Synthetic transforms with retained frequency order](fast-synthetic-transform.md)
- [Assembling the exact product](multiplication-assembly.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

- "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}


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

Write the body to `exegenius/tasks/0025-write-fast-address-interchange.answer.md` and the JSON to `exegenius/tasks/0025-write-fast-address-interchange.answer.json`, then run `exegenius submit 0025-write-fast-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-fast-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
