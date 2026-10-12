# exegenius task 0153-write-n-log-n-conjecture

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
- Fixed-tape machine model (also: fixed finite-tape model, fixed-tape machine)
- Exact integer multiplication
- Linear networks and frames (also: roles, frames)
- Gaussian dyadics
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

Concept: The n log n optimality conjecture
Gloss: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
Also called: Schönhage–Strassen conjecture

## Where the argument relies on this page

- A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model. (on [Integer multiplication below n log n](main-theorem.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (real numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
- $b$ (imaginary numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The non-negative integer exponent that sets the common denominator $2^k$.
- $H_0$ (two-point map), bound on [Gaussian dyadics](gaussian-dyadics.md): The map that sends a pair of coefficients $u$, $v$ to their halved sum and halved difference.
- $u$ (first coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The first coefficient of a pair on which the two-point map $H_0$ acts.
- $v$ (second coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The second coefficient of a pair on which the two-point map $H_0$ acts.
- $u$ (field size), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of cells in each of two disjoint fields, which counts the cells of a field.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs, the common length of x and y.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary string input, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary string input, of length n.
- $\mathrm{val}$ (binary value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is, leftmost bit most significant.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than 2^{2n} whose binary representation is taken.
- $\mathrm{bin}$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed number of bits.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: The n log n optimality conjecture *<predicate>* Exact integer multiplication

## Pages that build on this one

- Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Tensor product](tensor-product.md)
- [Complex phase network](complex-phase-network.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "proposed n log n as the optimal order of growth" (paper)

  > Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine, and proposed n log n as the optimal order of growth [25, Section 1]. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional O(n log n) upper bound [15]. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers. For a binary string x of length n, let val(x) be its nonnegative integer value, with the leftmost bit most significant. For 0 ≤ z < 2k , let bink (z) denote its binary representation padded on the left to length k. We consider exact multiplication: on input x#y, with x, y ∈ {0, 1}n , the output must be bin2n (val(x) val(y)). Write lg n = max{⌈log2 n⌉, 1}. Theorem 1. There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs. Its worst-case running time satisfies 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The quotation does not support the claim it is attached to (unsupported): "Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and" cites "proposed n log n as the optimal order of growth": The quotation says n log n was proposed as the optimal order of growth; it says nothing about Schönhage and Strassen, their 1971 multitape Turing machine algorithm, or its O(n log n log log n) running time. Say only what the source supports, or cite the passage that supports the claim.

## Previous version (revise it)

It has 183 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 233 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The n log n optimality conjecture is the claim that exact integer multiplication cannot be done faster, in order of growth, than $n\log n$. It is also called the Schönhage–Strassen conjecture.

Let $n$ be the number of bits in each of the two input integers. The conjecture bounds the cost of [Exact integer multiplication](exact-integer-multiplication.md), where the input is two $n$-bit binary strings and the output is their $2n$-bit product.

Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and <cite data-source="paper">proposed n log n as the optimal order of growth</cite>.

Later, Harvey and van der Hoeven reached an unconditional $O(n\log n)$ upper bound, one that holds without any extra hypothesis <cite data-source="paper">Harvey and van der Hoeven reached the unconditional O(n log n) upper bound</cite>. The conjecture therefore asks whether the extra $\log\log n$ factor, and any other gap, can be closed.

Saying $n\log n$ is optimal means no algorithm can do asymptotically better than this order. A faster method in a restricted model, such as a [fixed-tape machine](fixed-tape-model.md) (a Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes), does not by itself settle the conjecture.

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

Write the body to `exegenius/tasks/0153-write-n-log-n-conjecture.answer.md` and the JSON to `exegenius/tasks/0153-write-n-log-n-conjecture.answer.json`, then run `exegenius submit 0153-write-n-log-n-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
