# exegenius task 0080-write-subset-intersection-network

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
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange)
- Address shear
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
- Bilinear form (also: bilinear space, nondegenerate form)

## This page

Concept: Subset-intersection network
Gloss: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
Also called: three-element subset network

## This page in the argument

The step: A fixed linear network on three-element subsets exchanges two banks of scalars and restores every scratch wire.
How: gather and scatter coefficients by intersection size, and cancel the unwanted coefficients with auxiliary wires carrying subspace labels
Why: Coefficients depending on intersection size, with auxiliary wires cancelling the rest, give an exchange whose subspace ranks can be controlled. (the sources say so: "The construction uses three-element subsets: gather and scatter" (paper))

Its sub-steps, in order:

- The total number $s$ of smaller calls satisfies $s<Wm$. (on [Rank-saving recursion](rank-saving-recursion.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time, with $\kappa=2^{-182}$, below the $n\lg n$ conjecture in this model.; how: bound the cost of an exact multiplication whose transform layers are made cheap by two tape procedures, then fix parameters so every cost term fits (on [Integer multiplication below n log n](main-theorem.md))
- Two disjoint equal address fields of $u$ bits in an array of stored volume $V$ can be interchanged in $O(V u^{\tau})$ time.; how: apply a fixed linear network that exchanges two banks while restoring scratch values, recursively on streams of $1/W$ of the volume, so each level costs a strictly smaller power (on [Address-field interchange](address-interchange.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (numerator real part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator a + bi of a Gaussian dyadic.
- $b$ (numerator imaginary part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator a + bi of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): A non-negative integer; the denominator of a Gaussian dyadic is the power of two 2^k.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The common length of the two input strings, counting the bits of each input.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length n.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is.
- $k$ (padded width), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation, counting leading zeros.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the k-bit binary representation of a number z, padded with leading zeros.
- $n$ (input length), bound on [The n log n optimality conjecture](n-log-n-conjecture.md): The number of bits in each of the two input integers.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of bits the array stores.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $\tau$ (cost exponent), bound on [Address-field interchange](address-interchange.md): A fixed exponent less than 1 in the cost bound.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields the shear updates, a vector of residues.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields the shear updates, a vector of residues, left unchanged by the shear.
- $n$ (input length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary input strings.
- $w$ (block width), bound on [Signed coefficient packing](signed-packing.md): The number of bits reserved for each coefficient in a packed integer.
- $f$ (packed polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial with integer coefficients that is packed into an integer.
- $F$ (packed integer of f), bound on [Signed coefficient packing](signed-packing.md): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, multiplied by $f$.
- $G$ (packed integer of g), bound on [Signed coefficient packing](signed-packing.md): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The product $fg$ of the two packed polynomials, whose coefficients the packed product recovers.
- $F$ (fixed bilinear space), bound on [Subspace labels](subspace-labels.md): The fixed vector space carrying the nondegenerate bilinear form, in which all labels are subspaces.
- $U$ (label), bound on [Subspace labels](subspace-labels.md): A nondegenerate subspace of $F$ attached to a wire or an edge of the network.
- $V$ (larger label), bound on [Subspace labels](subspace-labels.md): The label on the edge that contains the smaller label $U$.
- $R$ (orthogonal residual), bound on [Subspace labels](subspace-labels.md): The orthogonal complement of the smaller label inside the larger one, on an edge.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Subspace labels](subspace-labels.md): Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.
  Shown as: Subset-intersection network *<predicate>* Subspace labels
- [Linear networks and frames](linear-network-frames.md): A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
  Shown as: Subset-intersection network *<predicate>* Linear networks and frames

## Pages that build on this one

- Rank-saving recursion: The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
- Complex phase network: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
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

- "The construction uses three-element subsets: gather and scatter create coefficients" (paper)

  > written as vectors H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D). Two further linear-cost address updates complete their interchange. For the numerical procedure, the endpoint operator becomes the simultaneous H0 layer after diagonal phase operations and a dyadic scale. The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure. The finite construction in Section 3 attaches subspaces of a fixed m-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number s of smaller calls satisfies s < W m. A recursive call at parameter mf therefore uses s calls at parameter f , each on a stream of volume V /W . The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by m increases the recursive contribution by s/W < m. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Explain "Gather and scatter" in a sentence where it is first used.

## Previous version (revise it)

It has 247 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 308 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A subset-intersection network is a fixed linear network on the three-element subsets of a ground set. It exchanges two banks of scalars while restoring every scratch wire, that is, every auxiliary wire ends with the value it started with. It is the exchange step that the [address-field interchange](address-interchange.md) applies recursively.

The network is based on [linear networks and frames](linear-network-frames.md). Its wires carry scalars, and its gates combine them according to the size of the intersection of their subsets. Take the ground set $\{1,2,3,4\}$. Two distinct three-element subsets of it always meet in exactly two elements, so a gate that depends only on intersection size treats every pair of distinct subsets alike, and treats a subset paired with itself, which meets in three elements, differently.

Gates are the vertices that combine values, and terminals are the endpoints where the two banks attach. The network attaches [subspace labels](subspace-labels.md) to its gates and terminals. Here $m$ is the dimension of the fixed space from which the labels are drawn.

Gather and scatter create coefficients that depend on intersection size, and auxiliary wires cancel the unwanted ones. <cite data-source="paper">The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients.</cite> The point is that such coefficients, with the rest cancelled, give an exchange whose subspace ranks can be controlled.

Here $s$ is the total number of smaller calls made by one call. Here $W$ is the factor by which the stream volume shrinks, so each smaller call works on a stream of $1/W$ of the volume.

The inequality $s<Wm$ is the property the rest of the argument needs. <cite data-source="paper">The decisive property is that the total number s of smaller calls satisfies s < W m.</cite>

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

Write the body to `exegenius/tasks/0080-write-subset-intersection-network.answer.md` and the JSON to `exegenius/tasks/0080-write-subset-intersection-network.answer.json`, then run `exegenius submit 0080-write-subset-intersection-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
