# exegenius task 0015-write-chunk-interchange

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen optimality conjecture
- Harvey–van der Hoeven O(n log n) multiplier
- Arrays and elementary stream operations on tape
- Controlled shifts and rational scalings
- Bank-exchange network with restored scratch wires
- Frames on network wires
- Nested subspace labels and orthogonal residuals
- Strict rank saving
- Lower-triangular factorization of a matrix
- Cost of a matrix shear on address fields
- Power-width chunk interchange
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(...), Ω, Θ, asymptotically smaller, worst-case running time)
- Limits and limit inferior (also: liminf, limsup, limit of a ratio, lim inf, eventually, for all sufficiently large n)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, log_2, natural logarithm, floor function, ceiling function, powers of two, iterated logarithm, log star)
- Recurrences and geometric sums (also: recurrence relation, solving recurrences, geometric series, geometric sum, unrolling a recurrence, divide and conquer)
- Positional number systems and carries (also: binary representation, radix representation, base-b digits, bit string, most significant bit, carry propagation, schoolbook addition, padding with leading zeros)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, divide-and-conquer multiplication, Toom-Cook, quadratic multiplication)
- Bitwise operations and XOR (also: exclusive or, XOR, bitwise exclusive or, addition modulo 2, bit flip, parity, bit shift, bit mask)
- Modular arithmetic (also: integers modulo q, Z/qZ, congruence, residues, units modulo q, invertible residues, arithmetic mod q, Chinese remainder theorem for integers)
- Primes, coprimality and the extended Euclidean algorithm (also: prime numbers, relatively prime, pairwise coprime, gcd, greatest common divisor, Euclid's algorithm, Bezout identity, modular inverse, odd primes, primality testing by trial division)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit complex numbers, complex exponential, Euler's formula, twiddle factor, N-th root of unity)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear operator, linear transformation, identity matrix, diagonal matrix, unitary or involution matrix, matrix-vector product, linear combination)
- Vector spaces, subspaces, dimension and rank (also: subspace, span, basis, linear independence, dimension, rank of a matrix, rank-nullity, kernel, image, column space, direct sum, quotient space)
- Inner products, bilinear forms and orthogonal complements (also: bilinear form, dot product, orthogonality, orthogonal complement, orthogonal subspace, nondegenerate pairing, inner product space, pairing)
- Gaussian elimination and triangular matrices (also: row reduction, LU decomposition, lower triangular matrix, upper triangular matrix, elementary row operations, back substitution, unit triangular matrix, row echelon form)
- Permutations, bijections and permutation matrices (also: permutation, bijection, one-to-one correspondence, inverse permutation, partial permutation, reordering of an array, sorting network, transposition of indices, permutation matrix)
- Arithmetic modulo 2 and linear algebra over F_2 (also: F_2, GF(2), binary field, field with two elements, matrices over F_2, GL(m, F_2), mod 2 arithmetic, boolean linear algebra)
- Finite sets, subsets and counting (also: Cartesian product, subset intersection, set cardinality, binomial coefficient, inclusion-exclusion, product of index sets, power set, three-element subsets, pigeonhole)
- Circuits and directed acyclic graphs (also: arithmetic circuit, linear circuit, wires and gates, directed graph, DAG, network of gates, fan-in, source and sink nodes, layered network)
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, ‖·‖_∞, modulus bound, triangle inequality, operator norm, error bound, disk bound)
- Fixed-point numbers, dyadic rationals and rounding (also: fixed point arithmetic, dyadic rational, binary fraction, rounding to nearest integer, truncation, round-off error, precision in bits, numbers with p fractional bits, grid of spacing 2^{-p})
- Row-major order and matrix transposition (also: row-major layout, array layout, transposing a matrix, matrix transpose, k×k binary matrix, lexicographic address, two-dimensional array as a list)
- Subroutines and reductions between problems (also: black-box subroutine, reduction, calling a subroutine, oracle call, problem reduction, conditional lower bound, composition of algorithms, uniform algorithm)
- Convolution of sequences (also: linear convolution, polynomial multiplication as convolution, product of coefficient sequences, discrete convolution, convolution theorem)

## This page

Concept: Address chunk interchange
Gloss: Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.
Heading: Address chunk interchange in $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of data bits stored in the array being permuted.
- $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
- $\tau$ (interchange exponent): A fixed constant below one, 1 − 2^{−50}, bounding the power of the width in the cost.

## This page in the argument

The step: Two disjoint equal-width bit chunks of $u$ bits in an address array of volume $V$ can be interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$, by XOR combinations whose final effect is an exact permutation.
How: First interchange chunks whose width is a power of $m$ and which have enough rows (the key construction), then remove those restrictions by taking rows from a few high digits of the chunks, cutting the remaining width into base-$m$ pieces, and padding binary chunks to the working radix.
Why: The fast operation is proved only for power widths with enough rows; a few high digits of the array supply the rows and their movement is cheaper than the final bound. (the sources say so: "We have proved the fast operation for power widths with enough rows.
Rows for a general array can be supplied by a few of its own high digits.
Their movement will cost less than the final bound." (paper))
Striking feature: The cost per stored bit is only $u^\tau$ with $\tau=1-2^{-50}$, a power of the chunk width below the first power, although the exponent is barely under one. (explain why it holds, from the method)

Its sub-steps, in order:

- Two address chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time by running the bit network on $W$ cyclic role streams, with one smaller interchange per unit of edge rank. (on [Power-width chunk interchange](power-width-interchange.md))
- Supply the $W^k$ rows the power-width call needs by interchanging the top $\rho=O(\log e)$ digits of the two chunks one pair at a time, then padding to a multiple of $W^k$ rows.
- Writing the remaining width in base $m$, cut each chunk into corresponding pieces of widths $m^j$ and interchange each pair by the power-width procedure.
- The pieces cost $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ in total, using $a_j<m$ and $m^k<me$.
- For binary chunks of $u$ bits, pad each range to $[q^e]$ with $q^e\ge2^u$, interchange, and scan the padding away; since $e=O(u)$ the bound is $O(Vu^\tau)$.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a convolution of short digits evaluated by Fourier transforms, speed up the two costly ingredients (moving data between addresses, and butterfly arithmetic) by a power of a block size using one recursive saving, and total every cost term. (on [Sub-n-log-n integer multiplication](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2, S2.3, S2.4, S2.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: Supply the $W^k$ rows the power-width call needs by interchanging the top $\rho=O(\log e)$ digits of the two chunks one pair at a time, then padding to a multiple of $W^k$ rows.
Source: "Write each chunk as its top $\rho$ digits followed by its remaining
digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively.  Interchange
the corresponding high digits one pair at a time." (paper)
> Write each chunk as its top $\rho$ digits followed by its remaining digits, denoted $h^+,h^-$ and $d^+,d^-$, respectively. Interchange the corresponding high digits one pair at a time. The high positions now contain $d^+$ and $h^+$; move the digits of the latter, preserving their order, into consecutive positions immediately after $d^+$. Suppressing the prefix and suffix, the field orders during the construction are \[ \begin{aligned} &(h^+,h^-,g,d^+,d^-),\\ &(d^+,h^+,h^-,g,d^-) &&\text{after exchanging and joining the high parts},\\ &(d^+,h^+,d^-,g,h^-) &&\text{after interchanging the remaining parts},\\ &(d^+,d^-,g,h^+,h^-) &&\text{after separating the high parts again}. \end{aligned} \] In the two middle orders, the first two fields form a row field of range \[ R=q^{2\rho}\ge W^k \] before both remaining chunks. The joining moves preserve the order of the remaining digits and the gap field. Exchanging and joining the high parts costs $O(V\rho)$ by Lemma~\ref{lem:elementary-streams}. Append zero rows, separately within each preceding prefix, until the row count is \[ R'=W^k\left\lceil R/W^k\right\rceil<2R. \] This changes the row field's length; it need not remain a power of $q$ during the computation. The padded logical volume is less than $2V$.

**S2.3**: Writing the remaining width in base $m$, cut each chunk into corresponding pieces of widths $m^j$ and interchange each pair by the power-width procedure.
Source: "Partition each remaining chunk into corresponding consecutive pieces,
with $a_j$ pieces of width $m^j$.  Apply
Proposition~\ref{prop:power-interchange} to each corresponding pair." (paper)
> Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.

**S2.4**: The pieces cost $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$ in total, using $a_j<m$ and $m^k<me$.
Source: "The sum of the costs is bounded by
\[
 O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)." (paper)
> Write the remaining width in base $m$: \[ e-\rho=\sum_{j=0}^{k} a_jm^j,\qquad 0\le a_j<m. \] Partition each remaining chunk into corresponding consecutive pieces, with $a_j$ pieces of width $m^j$. Apply Proposition~\ref{prop:power-interchange} to each corresponding pair. All these calls use the same row field of length $R'$, which is divisible by each required $W^j$. At completion every call preserves its row address, so it neither mixes genuine rows with padded rows nor depends on the values used for padding. The padded zero rows remain zero at these completed-call boundaries. The sum of the costs is bounded by \[ O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau). \] The fixed bound $a_j<m$ and the inequality $m^k<me$ make this a geometric sum of the stated order. Scan away the padded rows, then reverse only the moves that joined the high parts. This is the last transition in the field-order display: $h^+$ returns to the later high position, while $d^+$ stays in the earlier one. The final order is therefore the required interchange of the two full chunks. The remaining movement cost $O(V\log(2e))$ is $O(Ve^\tau)$. Computing the piece list and every new shape is polynomial in $\log(2V)$ per piece. There are at most $(m-1)(k+1)=O(\log(2e))$ pieces; since $V\ge q^{2e}$, their total descriptor cost is a fixed power of $\log(2V)$ and hence $O(V)$. Each power-width call uses the fixed schedule proved above and leaves its work tapes clean.

**S2.5**: For binary chunks of $u$ bits, pad each range to $[q^e]$ with $q^e\ge2^u$, interchange, and scan the padding away; since $e=O(u)$ the bound is $O(Vu^\tau)$.
Source: "Finally, for binary chunks let $e$ be the least integer with
$q^e\ge2^u$.  Pad each of the two chunk ranges numerically from $[2^u]$
to $[q^e]$, putting zero in an entry if either chunk coordinate is
invalid.  The increase in volume is less than $q^2$, a fixed factor.
The padding is a nested scan through consecutive valid and invalid
intervals, with their lengths prepared from the shape.  It costs $O(V)$
with a constant depending on $q$.  Lexicographic radix-$q$ order of
$[q^e]$ is its numerical order, just as binary order of $[2^u]$ is its
numerical order.  Padding therefore preserves the order of the existing
entries without converting the digits of every address.
The completed interchange preserves the set on which both chunk
coordinates lie below $2^u$.  Scan away the other entries to recover the
desired binary array.  Since $e=O(u)$ for fixed $q$, the bound is
$O(Vu^\tau)$." (paper)
> Finally, for binary chunks let $e$ be the least integer with $q^e\ge2^u$. Pad each of the two chunk ranges numerically from $[2^u]$ to $[q^e]$, putting zero in an entry if either chunk coordinate is invalid. The increase in volume is less than $q^2$, a fixed factor. The padding is a nested scan through consecutive valid and invalid intervals, with their lengths prepared from the shape. It costs $O(V)$ with a constant depending on $q$. Lexicographic radix-$q$ order of $[q^e]$ is its numerical order, just as binary order of $[2^u]$ is its numerical order. Padding therefore preserves the order of the existing entries without converting the digits of every address. The completed interchange preserves the set on which both chunk coordinates lie below $2^u$. Scan away the other entries to recover the desired binary array. Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$. \end{proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- K.0 (on [Power-width chunk interchange](power-width-interchange.md)): Two address chunks of $e=m^k$ radix-$q$ digits can be interchanged in $O(Ve^\tau)$ time by running the bit network on $W$ cyclic role streams, with one smaller interchange per unit of edge rank.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Arrays and elementary stream operations on tape](tape-stream-operations.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Power-width chunk interchange](power-width-interchange.md): Interchanging two address chunks of m^k digits by running the bit network on W cyclic role streams, with one smaller interchange per unit of edge rank, giving the recurrence F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ).
  Shown as: Address chunk interchange *<predicate>* Power-width chunk interchange

## Pages that build on this one

- Packed selected-bit addition: XORing corresponding selected bits of two address chunks by constantly many cyclic shifts of whole chunk ranges plus a deterministic repair of an explicitly small set of exceptional addresses, using a third chunk as restored scratch.
- Simultaneous butterfly layer: Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.
- Transform layout and cost: Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.
- Complete time bound: Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.

## Other pages you may link to

- [Schönhage–Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hh-multiplier.md)
- [Arrays and elementary stream operations on tape](tape-stream-operations.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Bank-exchange network with restored scratch wires](exchange-network.md)
- [Frames on network wires](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Strict rank saving](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Cost of a matrix shear on address fields](matrix-shear.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Contractions and error accumulation](contraction-error.md)
- [Exact dyadic intermediates with one truncation](guard-bits.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-two recursion](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Stored bit-reversed frequency order](bit-reversed-order.md)
- [Transform layout and cost](transform-layout.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancel in a convolution](permutation-cancellation.md)
- [Chinese-remainder map to prime axes](crt-axis-map.md)
- [Prime axis lengths near powers of two](prime-axis-lengths.md)
- [Parameter choice for the multiplier](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](time-bound.md)
- [Sub-n-log-n integer multiplication](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "(p,h,g,d,z)\longmapsto(p,d,g,h,z)" (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

- "The first procedure interchanges two disjoint contiguous address" (paper)

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

Write the body to `exegenius/tasks/0015-write-chunk-interchange.answer.md` and the JSON to `exegenius/tasks/0015-write-chunk-interchange.answer.json`, then run `exegenius submit 0015-write-chunk-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-chunk-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
