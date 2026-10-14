# exegenius task 0032-write-chunk-swap

Project directory: `/home/user/openai-nlogn-wiki/runs/Q1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, binomial counting, permutations, induction, graphs, the union bound, and elementary number theory with gcd, primes, modular inverses and the Chinese remainder theorem), an algorithms course (asymptotic notation, recurrences and geometric sums, divide and conquer including Karatsuba, sorting including radix sort, stacks, amortized counters, the RAM model and worst-case running time), and an introductory theory course with Turing machines and multitape tapes. From computer organization they know binary and two's-complement encodings, bit order, XOR and binary arithmetic; from calculus and a first linear-algebra course they know logarithms, exponentials, Newton's method, simple inequalities, complex numbers with conjugates, polynomials, matrices, Gaussian elimination, rank, dot products, projections and eigenvalues over the real or rational numbers. They have not studied abstract algebra (rings, quotient rings, finite fields, tensor products, bilinear forms over 𝔽₂), Fourier analysis, numerical error analysis, or the research literature on fast integer multiplication, so the FFT machinery, resampling and all of the paper's constructions are new to them.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Modular arithmetic and finite fields (also: F_2, residue ring)
- Linear maps, matrices and rank (also: rational rank)
- Tensor products (also: tensor power)
- Nondegenerate bilinear forms and orthogonal complements (also: orthogonal complement, orthonormal basis)
- The n log n conjecture (also: Schönhage–Strassen conjecture, n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
- Lexicographic array layout and logical volume (also: address field, logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings (also: prefix-controlled cyclic shift, triangular update)
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Q_p truncation, Gaussian dyadics)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, R_r)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Normalized butterfly H₀ (also: butterfly, Hadamard butterfly)
  - $H_0$ (normalized butterfly): The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).
- Linear network with wire roles (also: role, wire, gate, scalar network)
- Restoring scratch values (also: transparent computation, scratch wires)
- Three-element subset construction (also: Frankl–Wilson construction, triple indicators)
- Three-stage bank exchange (also: gather, scatter, side injection, forward invocation)
- Frames and the common-frame identity (also: frame, endpoint operator)
- Nested subspace labels and orthogonal residuals (also: label, orthogonal residual, dimension loss)
- Rank deficit s < Wm (also: rank saving, relative rank deficit)
  - $s$ (number of smaller calls): The total number of smaller recursive calls the network's edges require, summed over all edges.
  - $W$ (wire count): The number of wires (roles) in the finite network, including scratch wires.
  - $m$ (label dimension): The dimension of the label space, which is the factor by which each smaller call shrinks the recursion parameter.
- Rational matrix interface of the bit network
- Address shear
- Lower triangular (Bruhat) factorization
- Matrix shear by rank-many interchanges
- Row splitting among wire roles
- Volume-normalized recursion and the power saving (also: recursive saving)
- Fixed-tape depth-first schedule (also: parking stack)
- Power-width interchange
- Signed Kronecker packing (also: Kronecker substitution)
- Binary representation of integers (also: base-2 representation, bin_k, val, positional notation, radix-2^b digits)
- Two's-complement representation (also: two's complement, signed w-bit word, sign extension)
- Bit order and endianness (also: most significant bit first, least significant bit first, MSB first, LSB first)
- Bitwise exclusive or (also: XOR, ⊕, bitwise operations)
- Hamming weight (also: wt, popcount, number of ones)
- Logarithms and exponent rules (also: log, log₂, lg, natural logarithm)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, nearest integer, truncation toward zero)
- Worst-case running time (also: time complexity, T_A(n), worst-case cost)
- RAM model of computation (also: unit-cost RAM, random-access machine, word RAM)
- Recurrences and recursion trees (also: recurrence relation, divide and conquer, master theorem, unrolling a recurrence)
- Geometric series (also: geometric sum, Σ a^j)
- Telescoping sums (also: telescoping)
- Karatsuba multiplication (also: Karatsuba–Ofman algorithm, n^{log₂ 3} multiplication)
- Stacks (also: LIFO, push and pop, call stack)
- Binary counter and amortized increment cost (also: binary counter, amortized analysis, ripple counting)
- Radix sort and stable sorting (also: stable sort, LSD radix sort, binary radix sort)
- Row-major order and matrix transposition (also: row-major layout, transpose)
- Directed graphs (also: vertices and edges, head and tail of an edge, path)
- Sets, Cartesian products and indicator vectors (also: [a] = {0,…,a−1}, Cartesian product, characteristic vector, indicator vector, subset intersection)
- Binomial coefficients (also: n choose k, C(n,k))
- Permutations and cycle notation (also: bijection, involution, cycle (a b c), inverse permutation)
- Union bound (also: Boole's inequality, counting bad cases)
- Greatest common divisor and Euclid's algorithm (also: gcd, coprime, relatively prime, extended Euclidean algorithm, modular inverse)
- Prime numbers and trial division (also: primes, primality testing by trial division, odd prime)
- Chinese remainder theorem (also: CRT)
- Matrix operations (also: identity matrix, diagonal matrix, permutation matrix, triangular matrix, lower triangular, block diagonal, direct sum of maps)
- Gaussian elimination (also: row reduction, elementary row operations, row addition, row swap, pivot)
- Dot product and orthogonality (also: inner product, x·y, orthogonal vectors)
- Projection onto a subspace (also: projection matrix, P_U)
- Eigenvalues of a matrix (also: eigenvalue, eigenvector)
- Complex conjugate (also: conjugation, z̄)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Bernoulli's inequality (also: (1 + x)^n ≥ 1 + nx)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Proof by induction (also: induction, inductive invariant, loop invariant)

## This page

Concept: Fast address-chunk interchange
Gloss: The tape procedure that interchanges two disjoint u-bit address fields of any array in O(V·u^τ) time with fixed τ = 1 − 2^{−50}, computing XOR combinations of data along the way.
Also called: chunk swap, address interchange, arbitrary-width interchange

## This page in the argument

The step: The fast address-chunk interchange: one fixed procedure interchanges two disjoint $u$-bit address fields of any array in $O(Vu^\tau)$ time with $\tau=1-2^{-50}$.
How: Prove the power-width case with enough rows first, then supply rows from the top digits of the chunks, split a general width into base-$m$ pieces, and pad binary chunks to radix-$q$ ranges.
Why: A few high digits of the chunks themselves supply the rows the power-width case needs, and moving them costs less than the final bound. (the sources say so: "Rows for a general array can be supplied by a few of its own high digits.
Their movement will cost less than the final bound." (paper))
Striking feature: A pure permutation of addresses is done faster than $u$ passes over the data, by computing XOR combinations of data that cancel out by the end. (explain why it holds, from the method)

Its sub-steps, in order:

- For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits, preceded by a row field whose length is divisible by $W^k$, can be interchanged in $O(Ve^\tau)$ time on fixed tapes. (on [Power-width interchange](power-width-interchange.md))
- After interchanging and joining the top $\rho$ digits of each chunk, those digits form a row field of range $q^{2\rho}\ge W^k$ before both remaining chunks, padded to a multiple of $W^k$ at less than twice the volume.
- Writing the remaining width in base $m$ and applying the power-width interchange to each piece costs $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$.
- Padding $[2^u]$ to $[q^e]$ changes the volume by a fixed factor and $e=O(u)$, so the bound is $O(Vu^\tau)$.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ conjecture in this model.; how: Reduce the product to radix-digit convolution, move it by a Chinese-remainder map, Gaussian resampling, chirps and a phase twist to convolution over $\mathbb C[y]/(y^r+1)$ computed by synthetic transforms; speed up the transforms' address movement and butterfly layers with two network-based tape procedures; then prove exact recovery and total the costs. (on [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md))
- Two tape procedures save over plain scanning: address chunks of width $u$ are interchanged in $O(Vu^\tau)$ time, and a simultaneous normalized butterfly layer on $D\le d$ chunks costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$.; how: Build each procedure from its own fixed linear network that exchanges two banks and restores scratch wires, apply the network pointwise to row-split role streams with frames chosen so every edge is a few smaller calls, and solve the volume-normalized recurrence.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2, S2.3, S2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: After interchanging and joining the top $\rho$ digits of each chunk, those digits form a row field of range $q^{2\rho}\ge W^k$ before both remaining chunks, padded to a multiple of $W^k$ at less than twice the volume.
Source: "In the two middle orders, the first two fields form a row field of range" (paper)
> Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.

**S2.3**: Writing the remaining width in base $m$ and applying the power-width interchange to each piece costs $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$.
Source: "The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a
geometric sum of the stated order." (paper)
> Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.

**S2.4**: Padding $[2^u]$ to $[q^e]$ changes the volume by a fixed factor and $e=O(u)$, so the bound is $O(Vu^\tau)$.
Source: "Since $e=O(u)$ for fixed $q$, the bound is
$O(Vu^\tau)$." (paper)
> Finally, for binary chunks let $e$ be the least integer with $q^e\ge2^u$. Pad each of the two chunk ranges numerically from $[2^u]$ to $[q^e]$, putting zero in an entry if either chunk coordinate is invalid. The increase in volume is less than $q^2$, a fixed factor. The padding is a nested scan through consecutive valid and invalid intervals, with their lengths prepared from the shape. It costs $O(V)$ with a constant depending on $q$. Lexicographic radix-$q$ order of $[q^e]$ is its numerical order, just as binary order of $[2^u]$ is its numerical order. Padding therefore preserves the order of the existing entries without converting the digits of every address. The completed interchange preserves the set on which both chunk coordinates lie below $2^u$. Scan away the other entries to recover the desired binary array. Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Power-width interchange](power-width-interchange.md)): For $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits, preceded by a row field whose length is divisible by $W^k$, can be interchanged in $O(Ve^\tau)$ time on fixed tapes.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Power-width interchange](power-width-interchange.md): Interchanging two address chunks of e = mᵏ radix-q digits in O(V·e^τ) time by running the bit network on row-split role streams with shear frames and recursive smaller interchanges.
  Shown as: Fast address-chunk interchange *<predicate>* Power-width interchange
- [Elementary stream operations](elementary-streams.md): Linear-time O(V) tape scans that permute or move single radix-q digits of addresses, apply fixed pointwise maps to split streams, and split or merge whole rows cyclically into a fixed number of streams.
  Shown as: Fast address-chunk interchange *<predicate>* Elementary stream operations

## Pages that build on this one

- Packed selected-bit addition: XORing the selected bits of one address chunk into the corresponding bits of another using eight packed cyclic shifts guarded by a third chunk, then deterministically repairing the small set of addresses where guards overflow.
- Chinese-remainder convolution map: The Agarwal–Cooley isomorphism ℂ[x]/(x^S − 1) → ⊗ᵢ ℂ[xᵢ]/(xᵢ^{sᵢ} − 1) for pairwise coprime sᵢ, placing the digit list on a product of prime cyclic axes and implemented on tape by triangular controlled shifts and axis moves.
- Transform layout and cost: Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.
- Tensor resampling interface: Applying the one-dimensional resampling maps line by line on every axis of a padded power-of-two box, moving axes into position with the fast chunk interchange.
- Cost table and the exponent κ: The accounting that bounds every stage's cost divided by Tp = Θ(n) by a power of p at most 1 − 2κ, so the whole algorithm runs in O(n·(log n)^{1−κ}).

## Other pages you may link to

- [The n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic fixed-point arithmetic](fixed-point.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Modular arithmetic and finite fields](modular-arithmetic.md)
- [Address shear](address-shear.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Linear maps, matrices and rank](linear-algebra.md)
- [Linear network with wire roles](linear-network.md)
- [Row splitting among wire roles](row-splitting.md)
- [Frames and the common-frame identity](frames.md)
- [Restoring scratch values](scratch-restoration.md)
- [Lower triangular (Bruhat) factorization](bruhat.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-forms.md)
- [Three-element subset construction](triple-construction.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Tensor products](tensor-product.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Volume-normalized recursion and the power saving](power-saving-recursion.md)
- [Rational matrix interface of the bit network](bit-interface.md)
- [Matrix shear by rank-many interchanges](matrix-shear.md)
- [Fixed-tape depth-first schedule](fixed-tape-schedule.md)
- [Two-point kernel C](kernel-c.md)
- [Binary phase interface of the complex network](phase-interface.md)
- [Packed selected-bit addition](packed-addition.md)
- [Recursive C-layer via phase frames](recursive-c-layer.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction](radix-reduction.md)
- [Chinese-remainder convolution map](crt-map.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein's chirp identity](bluestein.md)
- [Contractions and error accounting](contraction-errors.md)
- [Resampling with retained permutations](resampling-retained.md)
- [Source permutation cancellation](source-perm-cancel.md)
- [Transform layout and cost](transform-layout.md)
- [Ring convolution from the retained layout](synthetic-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Size parameters and prime source lengths](parameters.md)
- [Computed source transform](source-transform.md)
- [Precision analysis and exact recovery](precision-recovery.md)
- [Cost table and the exponent κ](cost-accounting.md)
- [Integer multiplication in O(n (lg n)^{1−κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data." (paper)

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

Write the body to `exegenius/tasks/0032-write-chunk-swap.answer.md` and the JSON to `exegenius/tasks/0032-write-chunk-swap.answer.json`, then run `exegenius submit 0032-write-chunk-swap` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-chunk-swap`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
