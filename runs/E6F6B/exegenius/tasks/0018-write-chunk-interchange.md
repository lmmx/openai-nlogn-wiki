# exegenius task 0018-write-chunk-interchange

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6B` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis and recurrences, discrete mathematics (induction, sets, functions, permutations, logarithms, floor and ceiling, modular arithmetic, primes, gcd and the Euclidean algorithm), introductory linear algebra (matrices, invertibility, rank, Gaussian elimination, vectors and inner products), basic algorithms (grade-school multiplication, divide and conquer, number representations in binary, bitwise XOR) and the basics of Turing machines with several tapes. They have met complex numbers and polynomials, but not the FFT in depth, abstract algebra beyond basic rings or quotient constructions, number-theoretic results such as prime density, numerical error analysis, or any research on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape model and elementary stream scans
- Controlled cyclic shifts and rational scalings
- Established O(n log n) integer multiplier
- Integer multiplication as convolution of radix digits
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, a power of two.
- Subspaces, orthogonal complements and projections
- Lower-triangular (Bruhat) factorization
- Linear network exchanging two banks with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels with a rank deficit
- Recursive power saving from s < Wm
- Rational matrix interface and address shear
- Cost of a rational matrix shear
- Power-width chunk interchange with rows
- Modular arithmetic and congruences (also: integers mod n, Z/nZ, residues, congruence, mod q^b)
- Primes, coprimality and gcd (also: prime numbers, relatively prime, coprime, prime to q, greatest common divisor, gcd)
- Euclidean algorithm and modular inverses (also: extended Euclidean algorithm, Euclid's algorithm, Bezout identity, inverse modulo q)
- Trial division and primality search (also: finding a prime by scanning, testing divisibility, trial division)
- Binary representation, bit strings and XOR (also: binary expansion, bit string, bits, exclusive or, XOR, addition mod 2, most significant bit)
- Radix representation and carry propagation (also: base-b digits, radix, carries, grade-school addition, schoolbook multiplication, digit expansion)
- Logarithms, floor and ceiling (also: lg, log base 2, natural logarithm, floor function, ceiling function, power of two)
- Recurrences and induction (also: proof by induction, recurrence relations, unrolling a recurrence, geometric series)
- Divide-and-conquer multiplication (also: Karatsuba, schoolbook algorithm, O(n^2) multiplication, Toom-Cook)
- Permutations and bijections (also: permutation of coordinates, permutation matrix, partial permutation, bit reversal, bijection)
- Matrices, invertibility and rank (also: matrix product, invertible matrix, rank of a matrix, linear map, diagonal matrix, identity matrix, matrix inverse, linear combination)
- Gaussian elimination (also: row reduction, elementary row operations, row echelon form)
- Vector spaces, bases and dimension (also: basis, span, linear independence, dimension, coordinates, standard basis)
- Cartesian products and lexicographic order (also: product of sets, tuples, lexicographic ordering, multi-index, d-dimensional array indexing, row-major order)
- Rational numbers and dyadic fractions (also: dyadic rationals, binary fractions, denominators, numerators, rational coefficients, lowest terms)
- Norms, absolute value and triangle inequality (also: modulus, sup norm, maximum norm, triangle inequality, unit disk, Euclidean norm, contraction, error bound)
- Euler's formula and roots of unity (also: e^(i theta), primitive root of unity, cis, complex exponential, unit circle)
- Rounding and square roots (also: nearest integer, rounding to integer, square root, truncation toward zero)
- Polynomial time and computational cost on tapes (also: polynomial in p, linear time, worst-case running time, single scan of a tape, fixed alphabet, finite control)
- Fast Fourier transform as a known algorithm (also: FFT, Cooley-Tukey, divide-and-conquer FFT, fast polynomial multiplication)

## This page

Concept: Fast interchange of address chunks
Gloss: Interchanging two disjoint address fields of u bits in an array in O(V u^τ) time for a fixed τ < 1, although the intermediate steps XOR data together; arbitrary widths are handled by padding and a base-m decomposition.

## This page in the argument

The step: Two disjoint address fields of $u$ bits in an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although the intermediate steps XOR data together.
How: Realize the exchange by a fixed network of XOR gates on $W$ wire roles whose edges are cheap changes of address frame, each costing smaller interchanges, so that the sum of edge ranks $s<Wm$ makes the recursion save a power of the chunk width; then handle arbitrary widths by padding and a base-$m$ decomposition.
Why: A strict rank deficit s<Wm makes the normalized cost recurrence grow like a power of the width below one, which no direct scan of the fields can do. (the sources say so: "is the source of the power saving." (paper))
Striking feature: The cost exponent $\tau$ is strictly less than one, so moving an arbitrary pair of address fields is cheaper than a linear number of passes in their width, even though the final effect is just a permutation. (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed network of linear gates on $W$ wires, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange $X$ and $Y$ up to sign and restores every scratch wire whatever its initial value. (on [Linear network exchanging two banks with restored scratch wires](bank-exchange-network.md))
- Replacing scalars by arrays and giving each vertex an invertible frame $D_v$, pointwise linear gates commute with a common frame, so the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$ and each edge only changes frame by $D_vD_u^{-1}$. (on [Frames and the common-frame identity](frames-on-arrays.md))
- Nondegenerate subspaces of an $m$-dimensional space, built from three-element subsets, can be attached to gates and terminals so that adjacent labels are nested and the orthogonal residual dimensions over all edges total $s<Wm$. (on [Nested subspace labels with a rank deficit](subspace-labels.md))
- With frames $\Phi_M$ moving the entry at $(H,D)$ to $(H+MD,D)$, the bit network turns the exchange into the shear $H\leftarrow H+D$ on every role, with total edge rank $s<Wm$. (on [Rational matrix interface and address shear](bit-shear-interface.md))
- A call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the normalized cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$, and because $s/W<m^\tau$ the cost is $O(Ve^\tau)$ with $\tau<1$. (on [Recursive power saving from s < Wm](recursive-power-saving.md))
- Every $m\times m$ rational matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones. (on [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md))
- The address map $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work, using one swap per pivot of the factorization. (on [Cost of a rational matrix shear](matrix-shear-cost.md))
- Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\tau)$ time by splitting rows into $W$ role streams, running the bit network with shear edges implemented by $s$ smaller interchanges, and then applying $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$. (on [Power-width chunk interchange with rows](power-width-interchange.md))
- For an arbitrary width $u$, padding the row count and the chunk ranges and writing the remaining width in base $m$ reduces to power-width interchanges, so the whole interchange costs $O(Vu^\tau)$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Provide two fast tape procedures, place them inside the Gaussian-resampling and synthetic-transform reduction of the integer product to a convolution, then check precision and exact recovery and add up the costs of all phases. (on [Integer multiplication below n log n](multiplication-below-nlogn.md))
- There are two fast tape procedures: an interchange of two address fields of $u$ bits in $O(Vu^\tau)$ time and a simultaneous butterfly layer over $d$ address chunks in $O(Vd^{\lambda'})$ time, with $\tau,\lambda'<1$ and $V$ the stored bit volume.; how: Set up the elementary stream and controlled-shift tools, then build each of the two procedures from its own rank-saving linear network that recurses on smaller calls of itself.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.9**: For an arbitrary width $u$, padding the row count and the chunk ranges and writing the remaining width in base $m$ reduces to power-width interchanges, so the whole interchange costs $O(Vu^\tau)$.
Source: "Write the remaining width in base $m$:" (paper)
> Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.3.1 (on [Linear network exchanging two banks with restored scratch wires](bank-exchange-network.md)): A fixed network of linear gates on $W$ wires, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange $X$ and $Y$ up to sign and restores every scratch wire whatever its initial value.
- S1.3.2 (on [Frames and the common-frame identity](frames-on-arrays.md)): Replacing scalars by arrays and giving each vertex an invertible frame $D_v$, pointwise linear gates commute with a common frame, so the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$ and each edge only changes frame by $D_vD_u^{-1}$.
- S1.3.3 (on [Nested subspace labels with a rank deficit](subspace-labels.md)): Nondegenerate subspaces of an $m$-dimensional space, built from three-element subsets, can be attached to gates and terminals so that adjacent labels are nested and the orthogonal residual dimensions over all edges total $s<Wm$.
- S1.3.4 (on [Rational matrix interface and address shear](bit-shear-interface.md)): With frames $\Phi_M$ moving the entry at $(H,D)$ to $(H+MD,D)$, the bit network turns the exchange into the shear $H\leftarrow H+D$ on every role, with total edge rank $s<Wm$.
- S1.3.5 (on [Recursive power saving from s < Wm](recursive-power-saving.md)): A call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$, so the normalized cost satisfies $F_k\le(s/W)F_{k-1}+O(1)$, and because $s/W<m^\tau$ the cost is $O(Ve^\tau)$ with $\tau<1$.
- S1.3.6 (on [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)): Every $m\times m$ rational matrix $A$ of rank $a$ factors as $E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ a partial permutation matrix with exactly $a$ ones.
- S1.3.7 (on [Cost of a rational matrix shear](matrix-shear-cost.md)): The address map $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ with $A$ of rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work, using one swap per pivot of the factorization.
- S1.3.8 (on [Power-width chunk interchange with rows](power-width-interchange.md)): Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\tau)$ time by splitting rows into $W$ role streams, running the bit network with shear edges implemented by $s$ smaller interchanges, and then applying $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-tape model and elementary stream scans](multitape-streams.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Power-width chunk interchange with rows](power-width-interchange.md): Interchanging two chunks of e = m^k digits by splitting rows into W role streams, running the bit network with shear edges implemented by smaller interchanges, then applying D←D−H, H←H+D, D←H−D; cost O(V e^τ).
  Shown as: Fast interchange of address chunks *<predicate>* Power-width chunk interchange with rows

## Pages that build on this one

- Packed changes of selected address bits: Adding (XOR) selected bits of one address chunk into another using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.
- Simultaneous butterfly layer: Applying H₀(u,v) = ((u+v)/2,(u−v)/2) to the same bit position in d address chunks at once, on polynomial records, in O(V d^λ') time with λ' < 1 instead of d whole-array passes.
- Synthetic transform layout on tape: A positional address permutation placing the selected bits of all participating axes at a common offset in consecutive K-bit chunks so that each FFT round is one simultaneous layer; total cost O(Tp[dK + pK^(τ−1) + ℓ d^λ']).
- Tensor resampling on the padded box: Applying the one-dimensional resampling maps line by line along each of d axes of the zero-padded power-of-two box, exposing each axis with chunk interchanges, for error below d·p² and total line cost O(dTp^(3/2+δ)α).
- Chinese-remainder map to distinct prime cyclic axes: An algebra isomorphism sending x to the product of x_i^(μ_i) turns one cyclic convolution of length S = s₁…s_d into a d-dimensional cyclic convolution over pairwise coprime axes, implemented by triangular controlled shifts.
- Cost table and exponent margins: Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).

## Other pages you may link to

- [Integer multiplication as convolution of radix digits](convolution-multiplication.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Established O(n log n) integer multiplier](hvdh-multiplier.md)
- [Fixed-tape model and elementary stream scans](multitape-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear network exchanging two banks with restored scratch wires](bank-exchange-network.md)
- [Subspaces, orthogonal complements and projections](linear-algebra-spaces.md)
- [Frames and the common-frame identity](frames-on-arrays.md)
- [Nested subspace labels with a rank deficit](subspace-labels.md)
- [Recursive power saving from s < Wm](recursive-power-saving.md)
- [Rational matrix interface and address shear](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Packed changes of selected address bits](packed-selected-bit-addition.md)
- [Fixed-point disk-grid arrays and truncation](fixed-point-precision.md)
- [Exact Gaussian dyadics and guard width](guard-bits.md)
- [Signed packing of polynomial products](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform and convolution theorem](discrete-fourier-transform.md)
- [Radix-two FFT butterflies](radix-two-fft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout on tape](synthetic-transform-layout.md)
- [Convolution over the polynomial ring from retained frequency order](synthetic-convolution.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Gaussian resampling without sorting](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on the padded box](tensor-resampling.md)
- [Chinese-remainder map to distinct prime cyclic axes](crt-cyclic-convolution.md)
- [Size parameters and prime axis lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision, rounding and carry recovery](exact-recovery.md)
- [Cost table and exponent margins](time-bound-accounting.md)
- [Integer multiplication below n log n](multiplication-below-nlogn.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product." (paper)

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

Write the body to `exegenius/tasks/0018-write-chunk-interchange.answer.md` and the JSON to `exegenius/tasks/0018-write-chunk-interchange.answer.json`, then run `exegenius submit 0018-write-chunk-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0018-write-chunk-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
