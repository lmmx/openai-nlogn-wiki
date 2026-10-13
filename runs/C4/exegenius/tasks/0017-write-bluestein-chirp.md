# exegenius task 0017-write-bluestein-chirp

Project directory: `/home/user/openai-nlogn-wiki/runs/C4` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science core: asymptotic analysis and recurrences, algorithms and data structures (divide and conquer, FFT-style ideas at the level of an algorithms course), discrete mathematics (modular arithmetic, binary representation, induction, basic combinatorics), and linear algebra (vectors, matrices, bases, invertible maps, subspaces over the reals and complex numbers). They know basic Turing machines with tapes, but not multitape time-complexity subtleties, the Schönhage–Strassen or Harvey–van der Hoeven methods, number-theoretic transforms in depth, or any research-level algebra or numerical analysis.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed multitape machine model and scans
- Schönhage–Strassen n log n conjecture and history
- Discrete Fourier transform and cyclic convolution
- Multiplication as convolution of radix digits
- Signed Kronecker packing
- Harvey–van der Hoeven O(n log n) multiplier as subroutine
- Chinese-remainder map to prime cyclic axes
- Polynomial ring modulo y^r + 1
  - $y$ (indeterminate): The formal variable of the polynomials.
  - $r$ (ring size): The number of complex coefficients in a record, a power of two.
- Linear exchange networks with frames and roles
- Three-element subset construction with rank saving
- Recursive power saving from s < Wm
- Address shear and lower triangular factorization
- Interchange of address chunks in time O(Vu^τ)
  - $V$ (bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant less than 1 in the cost exponent.
- Binary representation and bit operations (also: bits, XOR, binary expansion, bit strings)
- Modular arithmetic (also: congruences, mod, residues, integers modulo m)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, primes)
- Matrices and linear maps (also: linear algebra, invertible matrix, linear operator, change of basis, tensor product of vectors)
- Vector spaces over finite fields (also: F_2 vector space, subspace, dimension, rank, GF(2))
- Norms and triangle inequality (also: max norm, sup norm, operator norm, modulus bound)
- Floor, ceiling, rounding and logarithms (also: lg, log base 2, nearest integer, rounding)
- Recurrences and divide and conquer (also: recursion, recursive cost analysis, master theorem, recursion depth)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 butterfly)
- Euler's formula and exponentials of complex numbers (also: e^{2 pi i/q}, unit circle, phase, primitive roots of unity)
- Gaussian function and Gaussian sums (also: Gaussian, normal curve, exp(-x^2), Gaussian weight)
- Geometric series and exponential decay bounds (also: geometric sum, tail bound, exponential tail)
- Tuples, products of sets and mixed-radix indexing (also: Cartesian product, multi-index, coordinates, array indexing, tensor array)
- Permutations (also: bijection, reordering, coordinate permutation)
- Cyclic groups and direct products (also: Z/qZ, cyclic shift, cyclic axes, abelian group)
- Real and complex number approximation (also: rational approximation, dyadic rational, truncation error, error propagation)
- Big-O variants and constants (also: little-o, Theta, Omega, implied constant, sufficiently large)
- Induction and proof by recursion (also: mathematical induction, proof by induction)
- Diagonal matrices (also: diagonal operator, pointwise multiplication, entrywise scaling)

## This page

Concept: Bluestein chirp identity
Gloss: Rewrites a DFT of arbitrary length as a cyclic convolution sandwiched between pointwise phase (chirp) multiplications.

## This page in the argument

The step: Bluestein's chirp identity writes the middle transform as a cyclic convolution between pointwise phase multiplications, without applying the target permutation separately.

It serves these steps, from the main result down:

- Two $n$-bit integers are multiplied exactly by a deterministic fixed-tape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: Reduce the product to convolution through a chain of exact changes of representation, supply the movement and butterfly cost savings by two fast tape procedures, and assemble parameters, precision and cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- A Fourier transform of coprime length is expressed through a power-of-two tensor transform by Gaussian resampling, with the permutations retained and the middle transform turned into cyclic convolution.; how: Use Harvey--van der Hoeven resampling, keeping source and target permutations inside the transform formula, apply it line by line over many coordinates, and rewrite the middle transform by a chirp identity. (on [Gaussian resampling](gaussian-resampling.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform and cyclic convolution](dft-convolution.md): The length-q DFT (normalized by 1/q) turns cyclic convolution into pointwise multiplication; inverse transform has opposite sign in the exponent.
  Shown as: Bluestein chirp identity *<predicate>* Discrete Fourier transform and cyclic convolution

## Pages that build on this one

- Phase twist to the polynomial ring: A phase multiplication converting the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.
- Retained permutations cancelling in transforms: Keeping the source and target coordinate permutations of resampling inside the transform formula so that they cancel across the forward transforms, product and inverse instead of being sorted.

## Other pages you may link to

- [Fixed multitape machine model and scans](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](conjecture.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Address shear and lower triangular factorization](lower-triangular-shear.md)
- [Three-element subset construction with rank saving](subset-intersection-network.md)
- [Recursive power saving from s < Wm](recursive-power-saving.md)
- [Interchange of address chunks in time O(Vu^τ)](chunk-interchange.md)
- [Polynomial ring modulo y^r + 1](ring-y-r.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hvdh-multiplier.md)
- [Multiplication as convolution of radix digits](radix-digit-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist to the polynomial ring](phase-twist.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Exact Gaussian dyadic arithmetic with single truncation](gaussian-dyadics.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Simultaneous butterfly layer H₀](butterfly-h0.md)
- [Phase frames for simultaneous butterflies](phase-frames.md)
- [Fast simultaneous butterfly layer in time O(Vd^λ′)](fast-butterfly-layer.md)
- [Synthetic transform layout and convolution](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancelling in transforms](retained-permutations.md)
- [Tensor resampling over growing dimension](tensor-resampling.md)
- [Compatible parameter choice and cost accounting](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Next, Bluestein's chirp identity converts the middle transform," (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


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

Write the body to `exegenius/tasks/0017-write-bluestein-chirp.answer.md` and the JSON to `exegenius/tasks/0017-write-bluestein-chirp.answer.json`, then run `exegenius submit 0017-write-bluestein-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0017-write-bluestein-chirp`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
