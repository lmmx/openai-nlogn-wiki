# exegenius task 0041-write-multiplication-algorithm

Project directory: `/home/user/openai-nlogn-wiki/runs/P5` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic notation, recurrences and divide-and-conquer, binary and two's-complement arithmetic, integer division with remainder, modular arithmetic, primes and coprimality, sets, bijections and functions, basic vector and matrix algebra, polynomials and complex numbers (including roots of unity), and basic multitape Turing machines with linear scans. The reader has seen schoolbook and Karatsuba multiplication and probably an introductory FFT in an algorithms course, but has not studied abstract algebra (rings, groups, tensor products), finite fields beyond bit arithmetic, numerical analysis of rounding, or the specialist theory of fast integer multiplication, so the wiki must explain those.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed finite-tape Turing machine model
- The n log n conjecture and the history of multiplication
- Established O(n log n) multiplier as a subroutine
- Cyclic convolution
- Normalized discrete Fourier transform F_q
  - $F_q$ (normalized transform): The map sending a length-q complex vector u to the vector whose kth entry is (1/q) times the sum of u_j e^{-2πijk/q}.
  - $q$ (transform length): The number of complex entries in the vector being transformed.
- Two-point butterfly H₀ and the radix-two recursion
  - $H_0$ (butterfly map): The averaging map sending a pair (u,v) to ((u+v)/2,(u−v)/2).
- Polynomial ring modulo y^r+1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate with y^r = −1; its powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record; a power of two.
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Retained bit-reversed frequency order
- Fixed-point grid arrays with precision p
  - $p$ (precision): The number of fractional bits kept in each real or imaginary component.
- Exact Gaussian dyadic evaluation of a layer
- Array streams, address fields and elementary scans
- Controlled shifts and fixed rational scalings
- Subspaces, rank and orthogonal complements
- Triple indicator vectors and intersection pairings
- Scalar exchange network with restored scratch wires
- Frames and the common-frame identity
- Subspace labels and the rank saving s<Wm
  - $s$ (total edge rank): The number of smaller calls needed, equal to the sum of the ranks of all edge differences.
  - $W$ (wire count): The number of wires, including scratch wires, in the network.
  - $m$ (label dimension): The dimension of the ambient label space.
- Bit network and its shear interface
- Lower-triangular factorization of a matrix
- Address shear costing rank-many interchanges
- Power saving from a rank-deficit recursion
- Address-chunk interchange in O(Vu^τ) time
  - $V$ (stored volume): The number of stored data bits in the array.
  - $u$ (chunk width): The number of bits in each of the two address fields being interchanged.
  - $\tau$ (interchange exponent): A fixed constant below 1, namely 1−2^{-50}.
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Simultaneous butterfly layer in O(Vd^λ') time
  - $V$ (stored volume): The number of stored data bits in the array.
  - $d$ (axis count): The maximum number of address chunks (axes) whose selected bits are butterflied together.
  - $\lambda'$ (layer exponent): A fixed constant below 1, namely 1−2^{-54}.
- Synthetic transform layout and cost
- Signed packing of polynomial products
- Convolution from the retained transform layout
- Multiplication as radix-digit convolution
- Chinese-remainder map to prime cyclic axes (also: Agarwal–Cooley)
- Gaussian resampling
- Bluestein chirp identity
- Retaining resampling permutations in the transform
- Coefficient twist from cyclic to negacyclic
- Size parameters and prime source lengths
- Exact recovery by rounding and carry propagation
- Logarithms, floors and ceilings (also: log, lg, log base 2, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Binary representation and integer arithmetic (also: binary numerals, bit strings, radix representation, base-b digits, bits, carries)
- Division with remainder (also: quotient and remainder, Euclidean division, integer division)
- Modular arithmetic (also: congruences, residues, mod q, integers modulo q, Z/qZ, residue classes)
- Primes, divisibility and coprimality (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, coprime)
- Sets, functions and permutations (also: bijection, permutation of a set, subsets, intersection, cardinality, indicator vector, Cartesian product)
- Matrices and linear maps (also: matrix-vector product, identity matrix, permutation matrix, matrix inverse, linear transformation, vector spaces)
- XOR and arithmetic over F₂ (also: exclusive or, mod 2 addition, bitwise XOR, GF(2), parity, Hamming weight, popcount)
- Asymptotic notation beyond big-O (also: Θ, Ω, little-o, Theta notation, polylogarithmic factor, poly log)
- Recurrences and divide and conquer (also: recurrence relation, master theorem, recursion tree, geometric series, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, quadratic multiplication, Karatsuba, O(n^2) multiplication)
- Fast Fourier transform as an algorithm (also: FFT, Cooley–Tukey, Cooley-Tukey algorithm, fast polynomial multiplication by FFT, evaluation and interpolation)
- Inequalities for error bounds (also: triangle inequality, absolute value bounds, modulus bound, error accumulation, rounding error)
- Lexicographic order and mixed-radix indices (also: row-major order, multi-dimensional arrays, array indexing, mixed radix, lexicographic address order)
- Two's-complement and truncation (also: signed integers, round toward zero, truncate, fixed-point numbers)

## This page

Concept: The assembled multiplication algorithm
Gloss: Digits are placed on prime axes by the CRT map, two source transforms (Gaussian resampling with chirp convolution over the ring via twist, using synthetic convolution) and one opposite transform give the digit convolution, then rescale, round and carry.

## This page in the argument

The step: The assembled algorithm places the radix digits on prime axes by the Chinese-remainder map, applies two source transforms, a pointwise product and one opposite transform, then rescales, rounds and carries to give the exact product.
How: reduce the integer product to a convolution, move it step by step to the ring convolution of the earlier sections, and recover the integer by rounding
Why: Each reduction in the flow from digit convolution to prime axes to power-of-two axes to the ring changes only the problem's representation, so the faster transforms can be used at the end and the answer pulled back. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Writing both inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits, the product coefficients are a convolution modulo $x^S-1$ with capacity below $2^{3b}$ and no wraparound. (on [Multiplication as radix-digit convolution](digit-convolution.md))
- The map $x\mapsto\prod_ix_i^{\mu_i}$ is an isomorphism from cyclic convolution of length $S$ onto convolution on a product of prime cyclic axes, realized by triangular controlled shifts. (on [Chinese-remainder map to prime cyclic axes](crt-cyclic-axes.md))
- Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto $\mathbb C[y]/(y^r+1)$, so negative wrap becomes cyclic wrap. (on [Coefficient twist from cyclic to negacyclic](phase-twist.md))
- The source transform applies the Gaussian maps linewise, the chirp transform via complex convolution by twist, and a final exact scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
- Place the digits by $\Phi$, transform both operands, multiply pointwise, apply the opposite transform, and rescale by $S$ and $2^{2b+4}$ to obtain the integer coefficient convolution.
- Undoing the known scales shows every recovered coefficient has error below $1/2$, so rounding and radix-$2^b$ carry propagation give the exact $2n$-bit product. (on [Exact recovery by rounding and carry propagation](exact-recovery.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two tape procedures that save a power of the width, use them inside the Harvey and van der Hoeven Gaussian-resampling multiplication with polynomial transforms and retained permutations, then choose parameters, prove exactness and sum the costs (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))
- The sizes, the assembled algorithm with exact recovery, and the cost bound complete the multiplication.; how: choose parameters compatible with all earlier interfaces, run the pipeline, prove exactness, and sum the costs

## Steps this page derives

The argument gives this page these sub-steps of its step (D2.4, D2.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**D2.4**: The source transform applies the Gaussian maps linewise, the chirp transform via complex convolution by twist, and a final exact scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
Source: "For a source disk-grid tensor of norm at most $.5$, write" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**D2.5**: Place the digits by $\Phi$, transform both operands, multiply pointwise, apply the opposite transform, and rescale by $S$ and $2^{2b+4}$ to obtain the integer coefficient convolution.
Source: "The source-transform procedures now supply the three transforms needed" (paper)
> The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- D2.1 (on [Multiplication as radix-digit convolution](digit-convolution.md)): Writing both inputs in radix $2^b$ with $q=\lceil n/b\rceil$ digits, the product coefficients are a convolution modulo $x^S-1$ with capacity below $2^{3b}$ and no wraparound.
- D2.2 (on [Chinese-remainder map to prime cyclic axes](crt-cyclic-axes.md)): The map $x\mapsto\prod_ix_i^{\mu_i}$ is an isomorphism from cyclic convolution of length $S$ onto convolution on a product of prime cyclic axes, realized by triangular controlled shifts.
- D2.3 (on [Coefficient twist from cyclic to negacyclic](phase-twist.md)): Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps $\mathbb C[x]/(x^r-1)$ isomorphically onto $\mathbb C[y]/(y^r+1)$, so negative wrap becomes cyclic wrap.
- D2.6 (on [Exact recovery by rounding and carry propagation](exact-recovery.md)): Undoing the known scales shows every recovered coefficient has error below $1/2$, so rounding and radix-$2^b$ carry propagation give the exact $2n$-bit product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Multiplication as radix-digit convolution](digit-convolution.md): Writing both inputs in radix 2^b with q=⌈n/b⌉ digits, the product coefficients are a convolution with capacity below 2^{3b}, and padding to length S avoids wraparound.
  Shown as: The assembled multiplication algorithm *<predicate>* Multiplication as radix-digit convolution
- [Chinese-remainder map to prime cyclic axes](crt-cyclic-axes.md): Using pairwise coprime lengths s_i, a length-S cyclic convolution becomes convolution on a product of cyclic axes through the map x↦∏x_i^{μ_i}, realized by triangular controlled shifts.
  Shown as: The assembled multiplication algorithm *<predicate>* Chinese-remainder map to prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven's identity expressing a Fourier transform of prime-related length s through a power-of-two length t≥s transform via Gaussian-weighted contractions A and B₀, with a small error N−I.
  Shown as: The assembled multiplication algorithm *<predicate>* Gaussian resampling
- [Bluestein chirp identity](bluestein-chirp.md): A Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another phase multiplication.
  Shown as: The assembled multiplication algorithm *<predicate>* Bluestein chirp identity
- [Retaining resampling permutations in the transform](retained-permutations.md): The coordinate permutations of resampling stay inside the transform formula, so the chirp absorbs the target permutation and the source permutation cancels across two forward transforms, a pointwise product and the opposite transform.
  Shown as: The assembled multiplication algorithm *<predicate>* Retaining resampling permutations in the transform
- [Coefficient twist from cyclic to negacyclic](phase-twist.md): Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1) so negative wrap becomes cyclic wrap.
  Shown as: The assembled multiplication algorithm *<predicate>* Coefficient twist from cyclic to negacyclic
- [Convolution from the retained transform layout](synthetic-convolution.md): Two forward synthetic transforms, a pointwise ring product by signed packing, and the opposite transform give normalized convolution over C[y]/(y^r+1) with error about 3ℓ·M·2^{-p}.
  Shown as: The assembled multiplication algorithm *<predicate>* Convolution from the retained transform layout
- [Size parameters and prime source lengths](size-parameters.md): Choice b=⌈log₂n⌉, p=6b, d≈b^ε, K≈d^c, T≈n/b a power of two, axis lengths r/2 or r, and distinct odd primes s_i just below t_i, so that Tp=Θ(n) and r outgrows every power of p.
  Shown as: The assembled multiplication algorithm *<predicate>* Size parameters and prime source lengths
- [Exact recovery by rounding and carry propagation](exact-recovery.md): Undoing known scales S and 2^{2b+4}, showing the coefficient error is below 1/2, rounding to integers, and propagating radix-2^b carries to obtain the exact 2n-bit product.
  Shown as: The assembled multiplication algorithm *<predicate>* Exact recovery by rounding and carry propagation

## Pages that build on this one

- Cost accounting and the exponent κ: Dividing each term by Tp gives powers of p with margins g_i below one; the smallest margin is 2κ with κ=2^{-182}, absorbing any polylog factor.
- Integer multiplication in O(n (lg n)^{1−κ}) time: A deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Fixed-point grid arrays with precision p](fixed-point.md)
- [Exact Gaussian dyadic evaluation of a layer](dyadic-exact.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [The n log n conjecture and the history of multiplication](nlogn-conjecture.md)
- [Established O(n log n) multiplier as a subroutine](hvdh-multiplier.md)
- [Array streams, address fields and elementary scans](streams.md)
- [Controlled shifts and fixed rational scalings](controlled-shifts.md)
- [Subspaces, rank and orthogonal complements](linear-algebra.md)
- [Triple indicator vectors and intersection pairings](three-subset-pairing.md)
- [Scalar exchange network with restored scratch wires](scalar-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Subspace labels and the rank saving s<Wm](subspace-labels.md)
- [Power saving from a rank-deficit recursion](power-saving-recursion.md)
- [Bit network and its shear interface](bit-network.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Address shear costing rank-many interchanges](address-shear.md)
- [Address-chunk interchange in O(Vu^τ) time](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bits.md)
- [Polynomial ring modulo y^r+1](ring-mod-yr-plus-1.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](convolution.md)
- [Normalized discrete Fourier transform F_q](dft.md)
- [Two-point butterfly H₀ and the radix-two recursion](butterfly.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Retained bit-reversed frequency order](stored-order.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer in O(Vd^λ') time](simultaneous-layer.md)
- [Synthetic transform layout and cost](transform-layout.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The two occurrences of $S$ in this algorithm undo different" (paper)

  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

- "The multiplication algorithm" (paper)

  > \subsection{The multiplication algorithm}


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

Write the body to `exegenius/tasks/0041-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0041-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0041-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0041-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
