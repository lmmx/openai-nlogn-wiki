# exegenius task 0021-write-synthetic-transform

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n optimality conjecture
  - $n$ (input length): The number of bits in each input integer.
- Multiplication as convolution of digit lists
- Discrete Fourier transform
- Multidimensional transform
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial, a power of two.
- Chinese-remainder address map onto prime axes
- Signed packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Linear networks with roles and frames
- Three-element-subset finite networks
  - $s$ (number of calls): The number of smaller calls the network makes.
  - $W$ (number of roles): The number of wires (roles) of the network.
  - $m$ (space dimension): The dimension of the fixed space whose subspaces label the network.
- Scratch-restoring exchange network
- Recursive power saving
  - $s$ (number of calls): The number of smaller calls.
  - $W$ (number of roles): The number of roles of the network.
  - $m$ (parameter multiplier): The factor by which the recursive parameter grows.
- Elementary scans and controlled shifts
- Lower triangular factorization
  - $m$ (matrix size): The number of rows and columns of the matrix.
  - $a$ (matrix rank): The rank of the matrix.
- Rational matrix shear of address fields
- Fast address-field interchange
  - $V$ (bit volume): The number of stored bits.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant below 1.
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg n)
- Binary representation and bit operations (also: bits, XOR, bit position, binary expansion, radix representation)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, fast Fourier transform)
- Convolution (also: cyclic convolution, product of coefficient sequences, polynomial multiplication as convolution)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/n)
- Primes and coprimality (also: distinct primes, relatively prime, gcd, greatest common divisor, prime number theorem)
- Chinese remainder theorem (also: CRT)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, lower triangular matrix, matrix rank, identity matrix)
- Vector spaces and subspaces (also: change of basis, linear subspace, linear independence, basis)
- Permutations (also: permutation matrix, partial permutation, bijection of indices)
- Floor, ceiling and rounding (also: nearest integer, floor function, integer part)
- Recursion and recurrence relations (also: divide and conquer, recurrence, master theorem, recursive calls)
- Fixed-point and dyadic arithmetic (also: fixed-point numbers, dyadic rationals, truncation error, rounding error)
- Complex conjugate and modulus (also: conjugate, absolute value of complex number, Gaussian integers)
- Cartesian products and multi-indexing (also: multidimensional array, tuple indices, product of index sets)
- Linear-time scans and tape sorting (also: sorting on tapes, copying a tape, linear scan, tape reversal)
- Deterministic computation and time complexity classes (also: deterministic algorithm, running time, step count, worst-case time)
- Geometric and power-of-two parameter manipulation (also: powers of two, geometric series, exponent inequalities)

## This page

Concept: Synthetic polynomial transform
Gloss: Fourier transform over the polynomial ring where powers of y act as roots of unity, so multiplying by a root is a signed shift of the coefficient list (Nussbaumer).

## This page in the argument

The step: Convolution over $\mathbb C[y]/(y^r+1)$ is computed exactly by fast synthetic transforms, where $r$ is a power of two.
How: evaluate at powers of $y$ as roots of unity, where multiplication by a root is a signed shift, using the fast layers
Why: Multiplication by a root is a signed shift of the coefficient list, so transform layers cost only shifts and butterflies. (the sources say so: "such a root is a signed shift of the coefficient list." (paper))

Its sub-steps, in order:

- In the ring modulo $y^r+1$, sums of powers of $\omega_t$ vanish unless $t$ divides the exponent, so $F_t^+F_t^-=t^{-1}I$. (on [Synthetic character cancellation](synthetic-character-cancellation.md))
- Selected bits of the participating axes are placed at a common offset in $K$-bit chunks so the simultaneous layers apply, and the frequency order is retained. (on [Retained frequency order and transform layout](transform-layout.md))
- Convolution over the ring, normalized by $1/(rM)$, is computed from two forward synthetic transforms, pointwise products and the opposite transform. (on [Normalized convolution over the ring](normalized-convolution.md))

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on one fixed multitape machine.; how: reduce to digit convolution, build the fast tape and ring-transform tools bottom up, then assemble reductions, precision and cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform](fourier-transform.md): Evaluation of a sequence at powers of a root of unity; it turns cyclic convolution into pointwise product.
  Shown as: Synthetic polynomial transform *<predicate>* Discrete Fourier transform
- [Polynomial ring modulo y^r + 1](polyring-mod.md): Complex polynomials in y reduced modulo y^r+1, so y^r=-1; coefficients stored as a list, with r a power of two.
  Shown as: Synthetic polynomial transform *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Synthetic character cancellation: In the ring modulo y^r+1, sums of powers of the root ω_t vanish unless t divides the exponent, so forward and opposite transforms invert each other up to 1/t.
- Retained frequency order and transform layout: Selected bits of the participating axes are placed at a common offset in K-bit chunks so the simultaneous layers apply, and the frequency order is retained through the pointwise product.

## Other pages you may link to

- [Multiplication as convolution of digit lists](convolution-reduction.md)
- [Chinese-remainder address map onto prime axes](chinese-remainder-map.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary scans and controlled shifts](controlled-shifts.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Three-element-subset finite networks](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Scratch-restoring exchange network](scalar-motif-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational matrix shear of address fields](matrix-shear.md)
- [Fast address-field interchange](address-interchange.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hvdh-subroutine.md)
- [Multidimensional transform](multidim-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase frames for the butterfly layer](phase-frames.md)
- [Simultaneous butterfly layers](fast-butterfly-layer.md)
- [Fixed-point precision and exact recovery](exact-recovery.md)
- [Synthetic character cancellation](synthetic-character-cancellation.md)
- [Retained frequency order and transform layout](transform-layout.md)
- [Normalized convolution over the ring](normalized-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling without executing permutations](resampling-lemma.md)
- [Tensor interface for growing dimension](tensor-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Chirp and permutation cancellation](chirp-permutation-cancellation.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "multiplication by
such a root is a signed shift of the coefficient list." (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "The polynomial roots and radix-two butterflies belong to the fast
polynomial-transform method of Nussbaumer and
Quandalle" (paper)

  > The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method of Nussbaumer and Quandalle~\cite{NussbaumerQuandalle1978,Nussbaumer1980}; we use the form developed in~\cite[Section~2.4 and Lemma~3.2]{HarveyHoeven2021}. The work here is to apply the simultaneous layers on a suitable tape layout and retain the resulting frequency order through convolution.


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

Write the body to `exegenius/tasks/0021-write-synthetic-transform.answer.md` and the JSON to `exegenius/tasks/0021-write-synthetic-transform.answer.json`, then run `exegenius submit 0021-write-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
