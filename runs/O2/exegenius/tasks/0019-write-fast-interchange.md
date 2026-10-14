# exegenius task 0019-write-fast-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/O2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, binary representation and XOR), a first linear algebra course (vector spaces, matrices, rank, Gaussian elimination, eigenvalues, mostly over the reals but with arithmetic mod 2 seen in discrete math), single-variable calculus (limits, exponentials and logarithms, geometric series, simple inequalities, Newton's method), and an algorithms and theory sequence (asymptotic notation, recurrences, sorting, binary search, Turing machines and time complexity, schoolbook multiplication with carries). They have not studied fast Fourier transform based multiplication, the Schönhage–Strassen/Harvey–van der Hoeven line of work, polynomial transforms over quotient rings, tensor products, bilinear forms over finite fields, or the extremal set-theory constructions the paper borrows; those are what the wiki explains.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Polynomials
- Complex numbers
- Multitape Turing machine (also: multitape Turing model)
- Nondegenerate bilinear spaces (also: orthogonal complement, bilinear form)
- Tensor products
- Fixed finite-tape machine model and stream operations (also: logical volume, elementary streams, row split)
- Controlled shifts and rational scalings (also: controlled cyclic shift)
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input length): The number of bits in each integer being multiplied.
  - $\log$ (logarithm): The logarithm function, so n log n is the conjectured optimal growth of multiplication time.
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Z[i,1/2], fixed-point coefficients)
- Polynomial ring ℂ[y]/(y^r + 1) (also: R_r, synthetic roots of unity)
  - $\mathbb C$ (complex numbers): The field of complex numbers supplying the polynomial coefficients.
  - $y$ (indeterminate): The polynomial variable, whose powers serve as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Bank-exchange linear network (also: finite network, role, scratch wires, transparent computation)
- Three-element subset intersection construction (also: Frankl–Wilson construction, index-code decoding, gather and scatter)
- Frames and the common-frame identity (also: frame, endpoint operator, change of frame)
- Subspace labels and orthogonal residuals (also: labels, orthogonal residual, label space)
- Rank saving s < Wm (also: rank deficit, dimension deficit)
  - $s$ (smaller call count): The total number of smaller recursive calls needed over all edges of the network.
  - $W$ (wire count): The number of wires (roles) in the finite network, including scratch wires.
  - $m$ (label dimension): The dimension of the label space, equal to h³ = 1000000.
- Volume-normalized recursion (also: recursive saving)
- Address shears (H, D) ↦ (H + MD, D) (also: rational matrix interface, shear)
  - $H$ (earlier field vector): The vector of m earlier address fields being updated.
  - $D$ (later field vector): The vector of m later address fields used as the control of the update.
  - $M$ (rational matrix): A fixed rational m×m matrix, specialized modulo q^b, applied to D.
- Lower triangular (Bruhat) factorization (also: matrix shear, Grigor'ev factorization)
- Binary representation of integers (also: base-2 representation, bit string, most significant bit, leading zeroes, n-bit integer)
- Positional (radix) number systems (also: radix, base b digits, radix-2^b digits, mixed-radix representation, digit)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, carry propagation, quadratic multiplication)
- Two's complement and signed integers (also: signed binary integer, sign bit, sign-magnitude, signed word)
- Floor, ceiling and rounding (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, round to nearest integer, truncation toward zero)
- Integer division with remainder (also: division algorithm, quotient and remainder, a div b, a mod b)
- Logarithms and exponentials (also: log, log_2, lg, natural logarithm, exp, exponential function, powers of two)
- Theta, Omega and little-o notation (also: Θ, Ω, o(f), little-o, asymptotically tight bound, lower bound notation)
- Limits of sequences, lim inf (also: limit, liminf, limit inferior, tends to infinity, eventually, for sufficiently large n)
- Geometric series (also: geometric sum, sum of a geometric progression, geometrically increasing)
- Bernoulli's inequality (also: (1+x)^n ≥ 1+nx)
- Triangle inequality and absolute value (also: |a + b| ≤ |a| + |b|, modulus, absolute error)
- Gaussian function (also: Gaussian, bell curve, e^{-x^2}, Gaussian kernel)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Roots of unity (also: n-th root of unity, primitive root of unity, e^{2πi/n}, ω)
- Modular arithmetic (also: congruence, residues modulo q, mod, ≡ (mod q), Z/qZ, residue ring, reduction modulo q)
- Greatest common divisor and modular inverses (also: gcd, coprime, relatively prime, pairwise coprime, unit modulo q, modular inverse, extended Euclidean algorithm)
- Prime numbers and trial division (also: prime, odd prime, primality test by trial division)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- XOR and arithmetic modulo 2 (also: exclusive or, ⊕, bitwise XOR, parity, addition in F_2, the field with two elements, GF(2), F_2)
- Hamming weight (also: weight of a binary vector, wt(x), popcount, number of ones)
- Sets, subsets and Cartesian products (also: Cartesian product, [a] = {0, …, a−1}, 3-element subset, intersection size, |S ∩ T|, indicator vector, characteristic vector)
- Lexicographic order (also: row-major order, dictionary order, first coordinate most significant)
- Permutations (also: bijection, permutation of addresses, permutation matrix, rearrangement)
- Vector spaces, subspaces, basis and dimension (also: vector space, subspace, basis, dimension, span, linear independence, F_2^m)
- Linear maps and matrices (also: linear operator, linear transformation, matrix product, identity matrix, diagonal matrix, all-one matrix, transpose, kernel, image)
- Rank of a matrix (also: rank, rational rank, rank-one matrix, low-rank)
- Invertible matrices (also: nonsingular matrix, inverse matrix, GL(m, F), general linear group, singular matrix)
- Gaussian elimination (also: row reduction, elimination, row operations, pivoting)
- Triangular matrices (also: lower triangular matrix, upper triangular matrix, unit triangular)
- Eigenvalues (also: eigenvalue, eigenvector, spectrum)
- Max norm (also: infinity norm, ‖·‖_∞, sup norm, maximum absolute entry)
- Mathematical induction (also: induction, proof by induction, strong induction)
- Recurrence relations (also: recurrence, divide-and-conquer recurrence, unrolling a recurrence, recursion tree, master theorem)
- Binary search (also: bisection search)
- Stable sorting and radix sort (also: stable sort, radix sort, LSD radix sort, bucket sort, counting sort, sorting)
- Binary counter (also: incrementing a counter, ripple counting, ripple-carry increment)
- Deterministic worst-case time complexity (also: worst-case running time, deterministic algorithm, time complexity, T(n), lower bound)
- Cyclic shift (also: rotation, circular shift, cyclic rotation of a list)

## This page

Concept: Fast address-chunk interchange in O(V u^τ)
Gloss: The first tape procedure: exchanging two disjoint u-bit address fields of a stored array in O(V u^τ) time, τ = 1 − 2^−50, by recursively applying the bit network with XOR gates and row splits, rather than by data movement alone.
Also called: chunk swap, address interchange, power-width interchange
Heading: Fast address-chunk interchange in $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $O$ (big-O): Asymptotic upper bound up to a constant factor.
- $V$ (stored bit volume): The number of data bits stored in the array.
- $u$ (field width): The number of bits in each of the two interchanged address fields.
- $\tau$ (interchange exponent): A fixed rational exponent below one, here 1 − 2^−50.

## This page in the argument

The step: Two disjoint $u$-bit address fields of a stored array of volume $V$ can be interchanged in $O(Vu^\tau)$ time with $\tau=1-2^{-50}$.
How: factor each edge shear into rank-many smaller interchanges plus linear triangular updates, run the bit network on row-split role streams so its endpoint is the shear $H\gets H+D$, recurse on the field width, and remove the width and row restrictions by padding
Why: Each edge of rank $a$ costs $a$ smaller interchanges, so the strict rank saving turns into a recurrence that saves a power of the width. (the sources say so: "Because the sum of these ranks is less than the number of wires times
$m$, the resulting recurrence saves a power of the chunk width." (paper))
Striking feature: Its final effect is a pure permutation, yet it beats the cost of moving data field by field because its intermediate steps form XOR combinations of the data. (explain why it holds, from the method)

Its sub-steps, in order:

- Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones. (on [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md))
- A shear $(H,D)\mapsto(H+AD,D)$ with $A$ of rational rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.
- For widths $e=m^k$ with a row field of length divisible by $W^k$, chunk interchange costs $O(Ve^\tau)$, because time per bit obeys $F_k\le(s/W)F_{k-1}+O(1)$. (on [Volume-normalized recursion](power-saving-recursion.md))
- Borrowing high digits as a row field and padding binary chunks to radix $q$, any two $u$-bit chunks are interchanged in $O(Vu^\tau)$ time.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: build two linear-network tape procedures, fast address interchange and simultaneous butterfly layers, from fixed networks with a strict rank saving; use them in synthetic transforms; place these in the Harvey–van der Hoeven reduction through radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps and a phase twist; and bound every cost term (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2, S3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2**: A shear $(H,D)\mapsto(H+AD,D)$ with $A$ of rational rank $a$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ work.
Source: "can be performed with exactly $a$ interchanges of pairs of $b$-digit
fields and $O(V)$ further work." (paper)
> \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}

**S3.4**: Borrowing high digits as a row field and padding binary chunks to radix $q$, any two $u$-bit chunks are interchanged in $O(Vu^\tau)$ time.
Source: "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)
> \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md)): Every rational $m\times m$ matrix of rank $a$ factors as $E_1\Pi E_2$ with invertible lower triangular $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones.
- S3.3 (on [Volume-normalized recursion](power-saving-recursion.md)): For widths $e=m^k$ with a row field of length divisible by $W^k$, chunk interchange costs $O(Ve^\tau)$, because time per bit obeys $F_k\le(s/W)F_{k-1}+O(1)$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Controlled shifts and rational scalings](controlled-shifts.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Volume-normalized recursion](power-saving-recursion.md): Splitting rows cyclically among W roles makes each of s child calls act on volume V/W, so cost per bit obeys F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ yields a power saving e^τ in the parameter.
  Shown as: Fast address-chunk interchange in O(V u^τ) *<predicate>* Volume-normalized recursion
- [Address shears (H, D) ↦ (H + MD, D)](address-shears.md): Array permutations Φ_M that add a rational matrix M times one address-field vector D to another H modulo q^b; the bit network's rational matrix interface makes the endpoint operator the shear H ← H + D on every role.
  Shown as: Fast address-chunk interchange in O(V u^τ) *<predicate>* Address shears (H, D) ↦ (H + MD, D)
- [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md): Writing a rank-a rational matrix as E₁ Π E₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, so a matrix shear costs a field interchanges plus linear-time triangular updates.
  Shown as: Fast address-chunk interchange in O(V u^τ) *<predicate>* Lower triangular (Bruhat) factorization
- [Fixed finite-tape machine model and stream operations](fixed-tape-model.md): The model of one machine with a fixed alphabet and fixed number of tapes, where arrays are stored in lexicographic address order and elementary scans (digit moves, row splits, pointwise maps) cost time linear in the logical volume V of stored bits.
  Shown as: Fast address-chunk interchange in O(V u^τ) *<predicate>* Fixed finite-tape machine model and stream operations

## Pages that build on this one

- Packed selected-bit addition: A tape operation XORing the selected bits of one address chunk into the corresponding bits of another, using a temporary chunk, whole-chunk cyclic shifts and a sorted correction of a small explicit exceptional set.
- Chinese-remainder address map: The Agarwal–Cooley isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (distinct primes s_i near powers of two) into a multidimensional cyclic convolution, implemented on tape by triangular controlled shifts.
- Resampling with retained permutations: Keeping the source and target coordinate permutations R, Q inside the resampling identity R F_s = 2^γ B₀ Q F_t A rather than sorting, so the target permutation is absorbed by the chirp and the source permutation cancels across forward and inverse transforms in a convolution.
- Synthetic transform tape layout and cost: Arranging the axes of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in K-bit chunks, letting simultaneous butterfly layers and chunk interchanges compute every round.
- Parameter choice and cost table: The fixed rational exponents (τ = σ = 1 − 2^−50, λ′ = 1 − 2^−54, c = 2^−56, ε = 2^−75, …) and sizes (b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋) under which every per-bit cost term is at most p^{1−2κ}, giving κ = 2^−182.
- Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^−182, via radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps, a phase twist and synthetic transforms accelerated by fast interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Polynomial ring ℂ[y]/(y^r + 1)](ring-y-r-plus-1.md)
- [Gaussian dyadic fixed-point arithmetic](gaussian-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Nondegenerate bilinear spaces](linear-algebra-bilinear.md)
- [Bank-exchange linear network](bank-exchange-network.md)
- [Three-element subset intersection construction](triple-intersection-construction.md)
- [Tensor products](tensor-products.md)
- [Frames and the common-frame identity](frames.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Normalized butterfly H₀](butterfly-h0.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Binary phase frames](phase-frames.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication by radix-digit convolution](radix-digit-convolution.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Disk-grid approximation and error accounting](error-accounting.md)
- [Simultaneous butterfly layer in O(V d^λ′)](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Synthetic transform tape layout and cost](synthetic-transform-layout.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Parameter choice and cost table](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Although its final effect is an exact permutation, its intermediate
steps form pointwise XOR combinations of data." (paper)

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

Write the body to `exegenius/tasks/0019-write-fast-interchange.answer.md` and the JSON to `exegenius/tasks/0019-write-fast-interchange.answer.json`, then run `exegenius submit 0019-write-fast-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0019-write-fast-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
