# exegenius task 0019-write-address-fields-layout

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

Concept: Array addresses, fields and tape layout
Gloss: Arrays are stored on tape in row-major address order; address bit-fields (chunks) are contiguous and permuting them costs more than scanning.

## This page in the argument

The step: In the fixed multitape model data movement costs time, so arrays are laid out in address order and fields of addresses are contiguous chunks.

It serves these steps, from the main result down:

- One fixed-tape Turing machine multiplies n-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Beat the $n\log n$ cost of transform-based multiplication by making the two tape operations (address rearrangement and butterfly layers) cost a power of their width less than a full scan, then plug them into the Harvey-van der Hoeven resampling reduction (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed multitape Turing machine model](multitape-model.md): One fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads/writes one cell per tape and moves each head at most one cell, so moving data costs time.
  Shown as: Array addresses, fields and tape layout *<predicate>* Fixed multitape Turing machine model

## Pages that build on this one

- Linear networks with restored auxiliary values: A fixed network of gates exchanging two banks of values with signs, with roles for each wire, whose auxiliary values are restored so the effect is exact for arbitrary initial auxiliary contents.
- Address shear and triangular factorization: The endpoint operator (H,D)↦(H+D,D) on address fields; a rank-reducing lower-triangular factorization lets two further linear updates complete an interchange.

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
- [The n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier](hh-multiplier.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Linear networks with restored auxiliary values](linear-network.md)
- [Frames of a linear network](frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Subset-intersection subspace labels](subset-subspace-labels.md)
- [Recursive power saving from s<Wm](recursive-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Resampling with permutations left in the transform](retained-permutations.md)
- [Synthetic transforms with retained frequency order](fast-synthetic-transform.md)
- [Assembling the exact product](multiplication-assembly.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "interchanging fields whose numbers of digits grow" (paper)

  > A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. A step reads and writes at most one cell on each tape and moves each head by at most one cell. Fixed tracks and finitely many work tapes change time by a fixed factor. We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow. The latter permutation will be realized in Section~\ref{sec:tape-interchange} by computing XOR combinations of intermediate data streams. The present section supplies the elementary scans it uses. Every scan includes its counters and the return of its tape heads.

- "The array has complete address set" (paper)

  > We now apply the complex network to a common butterfly layer on several axes. The array has complete address set \[ [P]\times[2^K]^D\times[S],\qquad 1\le D\le d, \] with $P,S\ge1$, in lexicographic order. Its $D$ consecutive $K$-bit chunks each select the bit at one common offset $0\le\rho<K$, counted from the least significant end. Each address carries a polynomial record with $r$ complex coefficients, initially in the unit disk on the grid $2^{-p}\mathbb Z[i]$, with $\Theta(p)$ bits per real or imaginary component. The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits, acting coefficientwise and preserving all other address fields.


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

Write the body to `exegenius/tasks/0019-write-address-fields-layout.answer.md` and the JSON to `exegenius/tasks/0019-write-address-fields-layout.answer.json`, then run `exegenius submit 0019-write-address-fields-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0019-write-address-fields-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
