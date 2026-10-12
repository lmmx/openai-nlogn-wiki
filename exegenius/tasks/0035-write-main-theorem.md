# exegenius task 0035-write-main-theorem

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

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Chinese-remainder map (also: Agarwal–Cooley map)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Prime source lengths
- Transform identity with retained permutations
- Carry propagation
- Exact coefficient recovery
- Mathematical induction (also: induction, proof by induction, inductive proof)
- Logarithms and floor and ceiling functions (also: floor function, ceiling function, integer part, log base 2, lg)
- Binary representation of integers (also: binary string, bit string, base-2 representation, binary digits, bits)
- Dyadic rationals (also: binary fractions, dyadic numbers)
- Modular arithmetic (also: congruence modulo m, residues modulo m, integers modulo m, remainder arithmetic)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclidean algorithm)
- Prime numbers (also: primes, primality, prime factorization)
- Roots of unity (also: n-th roots of unity, primitive root of unity, unit roots, powers of a root of unity)
- Binary field F2 and XOR arithmetic (also: GF(2), field of two elements, mod-2 arithmetic, exclusive or, XOR, Boolean addition)
- Hamming weight (also: popcount, number of ones, weight of a binary vector, wt(x))
- Vector spaces and subspaces (also: linear subspace, span, basis, linear independence, dimension)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, transpose, identity matrix, linear transformation)
- Matrix rank (also: rank, rank of a linear map, column rank, row rank)
- Projection onto a subspace (also: projection matrix, idempotent linear map, orthogonal projection)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors, orthogonal complement)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum, characteristic polynomial)

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
Also called: Theorem 1

## This page in the argument

The step: A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model.
How: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits
Why: Each transform level scans $\Theta(n)$ stored bits, so the transform layers alone cost $\Theta(n\log n)$; the savings must come from both address movement and arithmetic. (the sources say so: "Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n). We therefore need savings in both movement and arithmetic." (paper))
Striking feature: the logarithmic factor is reduced by a power, $(\lg n)^{1-\kappa}$, so the bound is strictly below $n\lg n$ through all input lengths (explain why it holds, from the method)

Its sub-steps, in order:

- A simultaneous normalized butterfly layer on $d$ selected chunks of stored volume $V$ costs $O(V d^{\lambda'})$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Two disjoint equal address fields of $u$ bits in an array of stored volume $V$ can be interchanged in $O(V u^{\tau})$ time. (on [Address-field interchange](address-interchange.md))
- The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried. (on [Radix-digit convolution](radix-digit-convolution.md))
- A compatible choice of rational parameters makes every term of the cost table fit the bound of Theorem 1.
- The total cost is $O(n(\lg n)^{1-\kappa})$ for every large input, with $\kappa=2^{-182}$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture](n-log-n-conjecture.md): The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
  Shown as: Integer multiplication below n log n *<predicate>* The n log n optimality conjecture
- [Fixed-tape machine model](fixed-tape-model.md): A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
  Shown as: Integer multiplication below n log n *<predicate>* Fixed-tape machine model
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Integer multiplication below n log n *<predicate>* Radix-digit convolution
- [Chinese-remainder map](chinese-remainder-map.md): A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
  Shown as: Integer multiplication below n log n *<predicate>* Chinese-remainder map
- [Rank-saving recursion](rank-saving-recursion.md): The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
  Shown as: Integer multiplication below n log n *<predicate>* Rank-saving recursion
- [Transform layout](transform-layout.md): A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
  Shown as: Integer multiplication below n log n *<predicate>* Transform layout
- [Transform identity with retained permutations](transform-identity.md): The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
  Shown as: Integer multiplication below n log n *<predicate>* Transform identity with retained permutations
- [Prime source lengths](prime-source-lengths.md): Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
  Shown as: Integer multiplication below n log n *<predicate>* Prime source lengths
- [Phase twist](phase-twist.md): A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
  Shown as: Integer multiplication below n log n *<predicate>* Phase twist
- [Convolution over the polynomial ring](polynomial-ring-convolution.md): The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
  Shown as: Integer multiplication below n log n *<predicate>* Convolution over the polynomial ring
- [Packed selected-bit addition](packed-bit-addition.md): An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
  Shown as: Integer multiplication below n log n *<predicate>* Packed selected-bit addition
- [Exact coefficient recovery](recovery-and-error.md): The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
  Shown as: Integer multiplication below n log n *<predicate>* Exact coefficient recovery
- [Carry propagation](carry-propagation.md): Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
  Shown as: Integer multiplication below n log n *<predicate>* Carry propagation

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine A" (paper)

  > Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine, and proposed n log n as the optimal order of growth [25, Section 1]. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional O(n log n) upper bound [15]. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers. For a binary string x of length n, let val(x) be its nonnegative integer value, with the leftmost bit most significant. For 0 ≤ z < 2k , let bink (z) denote its binary representation padded on the left to length k. We consider exact multiplication: on input x#y, with x, y ∈ {0, 1}n , the output must be bin2n (val(x) val(y)). Write lg n = max{⌈log2 n⌉, 1}. Theorem 1. There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs. Its worst-case running time satisfies 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

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

Write the body to `exegenius/tasks/0035-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0035-write-main-theorem.answer.json`, then run `exegenius submit 0035-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
