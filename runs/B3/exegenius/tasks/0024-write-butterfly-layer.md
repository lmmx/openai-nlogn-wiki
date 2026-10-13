# exegenius task 0024-write-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/B3` (paths below are relative to it)

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

For these sources: An undergraduate computer scientist who has taken discrete mathematics, linear algebra, algorithms and introductory theory of computation. They know asymptotic notation, divide-and-conquer recurrences, basic number theory (divisibility, gcd, modular arithmetic, primes, Chinese remainder theorem statement), matrices and linear maps, complex numbers and roots of unity, and simple multitape Turing machines. They have not studied the FFT-based multiplication literature in depth, Nussbaumer or Bluestein transforms, fine tape-machine permutation tricks, or finite-ring and numerical-error analysis beyond basics.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen n log n conjecture and history
- Convolution and the discrete Fourier transform
- Multiplication as digit convolution
- Signed coefficient packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Elementary stream operations on tapes
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, with y^r = -1.
  - $r$ (number of coefficients): The number of coefficients in a polynomial, a power of two.
- Synthetic polynomial transforms
- Exact normalized polynomial products
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Coefficient twist to the polynomial ring
- Linear networks, roles and frames
- Finite networks from three-element subsets
- Recursive power saving s < Wm
  - $s$ (number of smaller calls): The total number of smaller calls the network makes.
  - $W$ (number of roles): The number of roles (wires) in the network, among which rows are distributed.
  - $m$ (parameter multiplier): The dimension of the fixed space and the factor by which the recursive parameter grows per level.
- Restoring auxiliary values
- Address shear and triangular factorization
- Fast interchange of address fields
  - $V$ (stored bit volume): The number of bits stored in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (exponent): A fixed constant strictly less than 1.
- Fixed-point precision and exact recovery
- Modular arithmetic (also: congruence, residues mod m, bmod, remainder)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime)
- Prime numbers (also: primes, distinct primes, prime factorization)
- Floor and ceiling functions (also: floor, ceiling, lceil, rounding)
- Binary logarithm (also: lg, log base 2, log n)
- Binary representation and bit strings (also: n-bit integers, bits, binary expansion, dyadic rationals)
- Exclusive or (also: XOR, oplus, bitwise xor)
- Matrices and linear maps (also: linear transformation, matrix product, invertible matrix, linear algebra)
- Permutations (also: bijection, permutation matrix, reordering)
- Subspaces, dimension and rank (also: rank, vector subspace, linear independence)
- Cyclic groups and rings (also: Z/mZ, integers mod m, cyclic group, ring, commutative ring)
- Cartesian products and tuples (also: product of sets, multi-index, coordinates, array indexing)
- Subsets and combinatorial counting (also: binomial coefficient, k-element subsets, triples)
- Recurrences and geometric series (also: recursion cost, telescoping sum, geometric sum)
- Inequalities and error bounds (also: triangle inequality, absolute value bound, norm, rounding error)
- Gaussian integers (also: Z[i], complex integers, integers a+bi)
- Exponents and powers (also: exponential, power of two, fractional exponent)
- Sorting and scanning arrays (also: linear scan, array order, merge sort)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey)

## This page

Concept: Simultaneous butterfly layer H₀
Gloss: Applying H_0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on selected address bits of arrays of complex fixed-point polynomial records via the recursive network, in O(V d^λ') time.
Heading: Simultaneous butterfly layer $H_0(u,v)$

The symbols in this page's heading denote (say so on the page):

- $H_0$ (butterfly map): The map sending (u,v) to ((u+v)/2,(u-v)/2).
- $u$ (first value): The first input value of the two-point butterfly.
- $v$ (second value): The second input value of the two-point butterfly.

## This page in the argument

The step: Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ simultaneously on selected bits of at most $d$ address chunks of arrays of complex fixed-point polynomial records costs $O(Vd^{\lambda'})$ with a fixed $\lambda'<1$.

It serves these steps, from the main result down:

- A fixed deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two fast tape procedures, use them in synthetic transforms for ring convolution, then chain the reductions from integer multiplication (on [Integer multiplication below n log n](main-result.md))
- Two tape procedures, an address interchange and a simultaneous butterfly layer, cost a power of their parameter below the first power times the volume.; how: build both from fixed linear networks that restore scratch values, and recurse on their rank saving

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving s < Wm](recursive-saving.md): Recursing at parameter m·f uses s calls at parameter f on volume V/W each; since s/W < m the volume-normalized cost grows by a factor below m per level, giving a power of the parameter below the first power.
  Shown as: Simultaneous butterfly layer H₀ *<predicate>* Recursive power saving s < Wm
- [Linear networks, roles and frames](linear-networks-frames.md): A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; roles are wire positions and invertible frames D_v change the stored representation so intermediate frames cancel and only an endpoint operator remains.
  Shown as: Simultaneous butterfly layer H₀ *<predicate>* Linear networks, roles and frames
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms over the polynomial ring where powers of y serve as roots of unity, built from address rearrangements, signed shifts and two-point butterflies (Nussbaumer).
  Shown as: Simultaneous butterfly layer H₀ *<predicate>* Synthetic polynomial transforms
- [Fixed-point precision and exact recovery](fixed-point-precision.md): Gaussian dyadic intermediates with one truncation after a contractive layer; accumulated error is kept below 1/2 so rounding and carries give the exact integer product.
  Shown as: Simultaneous butterfly layer H₀ *<predicate>* Fixed-point precision and exact recovery

## Pages that build on this one

- Transform layout with retained frequency order: Tape layout on which the parallel layers apply; permutations from resampling and chirps stay inside the transform and cancel across forward, pointwise-product and opposite transforms.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod-yr1.md)
- [Established O(n log n) multiplier as subroutine](hh-nlogn-multiplier.md)
- [Elementary stream operations on tapes](stream-operations.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Finite networks from three-element subsets](subset-network-construction.md)
- [Restoring auxiliary values](restoring-auxiliary.md)
- [Address shear and triangular factorization](address-shear.md)
- [Fast interchange of address fields](address-interchange.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist to the polynomial ring](phase-twist.md)
- [Multiplication as digit convolution](radix-digit-reduction.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Exact normalized polynomial products](exact-ring-products.md)
- [Transform layout with retained frequency order](transform-layout.md)
- [Multiplication algorithm and its cost](main-algorithm.md)
- [Integer multiplication below n log n](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "\begin{proposition}[Simultaneous normalized butterfly layer]" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice

- "The intended operation is the tensor product
of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits" (paper)

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

Write the body to `exegenius/tasks/0024-write-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0024-write-butterfly-layer.answer.json`, then run `exegenius submit 0024-write-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
