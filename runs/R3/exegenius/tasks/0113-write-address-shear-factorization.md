# exegenius task 0113-write-address-shear-factorization

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
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers (also: Gaussian integer)
- Multitape Turing machine
- Fixed-tape machine model and stream operations (also: fixed-tape machine)
- Convolution
- Discrete Fourier transform and butterflies (also: transform (the DFT/FFT the layout is for), twiddle factor, bit-reversed input, forward transform of length S)
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms (also: fast transform and transform axes)
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network, source and sink nodes of a route)
- Restoring auxiliary scratch values (also: scratch (auxiliary) roles)
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map, norm)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Address shear and lower-triangular factorization
Gloss: Endpoint operator (H,D)->(H+D,D) over a residue ring, with rank reduction via a singular-matrix Bruhat factorization into lower-triangular factors.

## This page in the argument

The step: The endpoint operator of the bit network is the address shear $(H,D)\mapsto(H+D,D)$ over a residue ring, with rank reduced by a lower-triangular factorization.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.; how: build both procedures from one finite linear network and a recursion that saves a power
- Two disjoint contiguous $u$-bit address fields can be interchanged in $O(Vu^\tau)$ for a fixed $\tau<1$, although the intermediate steps are XOR combinations.; how: take the network's endpoint operator to be an address shear and finish with two linear-cost updates (on [Fast interchange of address fields](fast-address-interchange.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $A$ (fixed machine), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The paper's deterministic Turing machine that multiplies integers.
- $T_A$ (running time of A), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The worst-case running time of the machine A on pairs of n-bit inputs.
- $\kappa$ (savings exponent), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The fixed positive constant 2^{-182} that gives the exponent of the logarithm in the bound.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input, $\lceil n/b\rceil$.
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $x$, an integer with $0\le x_j<2^b$.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $y$, an integer with $0\le y_j<2^b$.
- $c_k$ (digit coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution, the sum of $x_i\,y_j$ over all $i+j=k$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation, a nonnegative integer.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$, with $0\le d_k<2^b$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element, a power of two.
- $j$ (rule index), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The index of the coefficient that the wrap rule $y^{r+j}=-y^j$ reduces to, ranging over $0\le j<r$.
- $k$ (shift exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of the power $y^k$ that acts as a signed shift, with $0\le k<r$.
- $L$ (axis length), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of entries along one of the remaining transform axes, a divisor of $2r$.
- $m$ (cell position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in the array, which is also its address written in binary.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits the array holds in total.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\ne1$ for $0<m<n$.
- $m$ (frequency index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The frequency index of an entry of a transform, $0\le m<n$; it is also the exponent in $\omega^m$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $a$: the list of $n$ entries $A_m$ defined by the sum.
- $u$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The first input of a butterfly.
- $v$ (butterfly input), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The second input of a butterfly.
- $s$ (butterfly exponent), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The exponent of the power $\omega^s$ that a butterfly applies to its second input.
- $E$ (even-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the even-indexed entries of $a$.
- $O$ (odd-index transform), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform, with root $\omega^2$, of the odd-indexed entries of $a$.
- $h$ (block length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of entries in a block at a level.
- $t$ (block offset), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The offset of an entry within a block.
- $B$ (transform of b), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of $b$.
- $C$ (transform of c), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The transform of the cyclic convolution $c$.
- $l$ (paired index), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The index into $b$ paired with $i$ at output $k$, $l=(k-i)\bmod n$.
- $d$ (index difference), bound on [Discrete Fourier transform and butterflies](dft-fft.md): An integer, the difference of two output indices in the inverse sum.
- $t$ (transform length), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The number of entries in the transformed list, a power of two dividing 2r.
- $z$ (input list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of t ring elements being transformed.
- $Z$ (transformed list), bound on [Synthetic polynomial transforms](synthetic-transforms.md): The list of t entries produced by the transform.
- $g$ (output index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A position in the transformed list, running from 0 to t-1.
- $s$ (input index), bound on [Synthetic polynomial transforms](synthetic-transforms.md): A position in the input list, running from 0 to t-1.
- $m$ (primitivity exponent), bound on [Synthetic polynomial transforms](synthetic-transforms.md): An exponent used to test that the root has order exactly t.
- $W$ (role count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of roles of the network, the fixed places a wire can occupy.
- $\ell$ (row index), bound on [Finite linear network with roles and frames](linear-network-roles.md): The index of a row among the rows at a fixed prefix.
- $V$ (stored bit volume), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of bits stored in the padded array.
- $v$ (node), bound on [Finite linear network with roles and frames](linear-network-roles.md): A source, gate or sink of the network.
- $D_v$ (frame), bound on [Finite linear network with roles and frames](linear-network-roles.md): The invertible linear operator on arrays carried by node $v$.
- $u$ (edge tail node), bound on [Finite linear network with roles and frames](linear-network-roles.md): The node at the start of an edge, a node rather than the address field width.
- $g$ (logical array), bound on [Finite linear network with roles and frames](linear-network-roles.md): The array the network computes on before the frame is applied.
- $G$ (pointwise gate), bound on [Finite linear network with roles and frames](linear-network-roles.md): The pointwise linear gate operation that combines input arrays at each address.
- $t$ (gate input count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of input arrays of a gate.
- $\rho$ (role permutation), bound on [Finite linear network with roles and frames](linear-network-roles.md): The permutation of roles that the scalar network applies.
- $w$ (input role), bound on [Finite linear network with roles and frames](linear-network-roles.md): An input role of the scalar network, whose route ends at output role rho(w).
- $\varepsilon_w$ (route sign), bound on [Finite linear network with roles and frames](linear-network-roles.md): The sign on the route from input role w.
- $\mathrm{sink}$ (sink of a route), bound on [Finite linear network with roles and frames](linear-network-roles.md): The function giving the sink node at the output end of a route.
- $\mathrm{source}$ (source of a route), bound on [Finite linear network with roles and frames](linear-network-roles.md): The function giving the source node at the input end of a route.
- $I$ (identity operator), bound on [Finite linear network with roles and frames](linear-network-roles.md): The identity operator, which leaves every array unchanged.
- $\alpha$ (initial register value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The initial value of an auxiliary register, which may be any value.
- $\gamma$ (computed scratch result), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The value left in the register by the intended computation of stage 2, which depends only on the data.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Finite linear network with roles and frames](linear-network-roles.md): Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator.
  Shown as: Address shear and lower-triangular factorization *<predicate>* Finite linear network with roles and frames

## Pages that build on this one

- Fast interchange of address fields: Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "that endpoint operator is an address shear" (paper)

  > For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$. Two further linear-cost address updates complete their interchange. For the numerical procedure, the endpoint operator becomes the simultaneous $H_0$ layer after diagonal phase operations and a dyadic scale. The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "That sum is less than the number of wires times $m$, so the recurrence saves a power of the chunk width" (The page does not say what the rank budget states, nor which recurrence is meant, so the reader cannot check the inequality or the saving it is said to give.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- The reader cannot follow this step: "Each pass is linear in the stored bits, and $m$ is fixed." (The page does not justify why multiplying a field by a coefficient u v^{-1} mod q^b costs time linear in the field's bits. That coefficient is itself a b-digit residue, and the reader's known schoolbook multiplication cost is superlinear, so the linear-cost claim cannot be checked from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step. It is inside reasoning added for an earlier step. If it is part of how this page's own step of the argument works (see "This page in the argument"), develop it here; if it concerns a result that step uses, say what the result states and cite it.
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "A rational entry $u/v$ acts on fields as $u\,v^{-1}$ modulo $q^b$" (The page writes a rational entry as u/v and uses u v^{-1}, but never says what u denotes (the numerator of the fraction, an integer). Earlier pages bind u to other meanings (field width, butterfly input), which do not fit here.)
- Say what $v$ denotes where it is first used (for a size or count, what it counts): "A rational entry $u/v$ acts on fields as $u\,v^{-1}$ modulo $q^b$" (The page writes a rational entry as u/v and uses v^{-1}, but never says what v denotes (the denominator of the fraction). Earlier pages bind v to a butterfly input, which does not fit here.)
- Say what $h$ denotes where it is first used (for a size or count, what it counts): "On a pair $(h,d)$ this gives $(h+d,d)$" (The page uses h as the first entry of a pair but never says what h denotes. Earlier pages bind h to a block length, which does not fit here.)
- Say what $d$ denotes where it is first used (for a size or count, what it counts): "On a pair $(h,d)$ this gives $(h+d,d)$" (The page uses d as the second entry of a pair but never says what d denotes. Earlier pages bind d to an index difference, which does not fit here.)
- Explain "rank budget of the network (motif-residual lemma)" in a sentence where it is first used.

## Previous version (revise it)

It has 409 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 511 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

An address shear is a linear update of two vectors of address fields, and a lower-triangular factorization reduces it to interchanges and linear-cost updates. The address shear is the endpoint operator of the bit network, a [Finite linear network with roles and frames](linear-network-roles.md).

Let $m$ be the number of fields in each vector, and let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two vectors of address fields. Here $q$ is a fixed odd prime and $b$ the digits per field; these letters change meaning from earlier pages. Each field is a block of $b$ radix-$q$ digits, so it holds a residue in $\mathbb Z/q^b\mathbb Z$.

For a rational $m\times m$ matrix $M$, the shear by $M$ is $(H,D)\mapsto(H+MD,D)$. A rational entry $u/v$ acts on fields as $u\,v^{-1}$ modulo $q^b$, which exists only if $q$ does not divide $v$. So $q$ is chosen not to divide any denominator or diagonal numerator of the finitely many factors used. Let $\operatorname{rank}_{\mathbb Q}M$ be the number of linearly independent rows of $M$.

Every rational $M$ factors as $M=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower-triangular rational matrices and $\Pi$ is a partial permutation matrix with $\operatorname{rank}_{\mathbb Q}M$ ones, at most one in each row and column. This is Grigor'ev's Bruhat factorization with coordinate order reversed. Elimination proves it: pivot on the topmost nonzero row's rightmost entry, clear its row and column by triangular operations, and repeat.

Example: for $m=2$ and $M=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $\operatorname{rank}_{\mathbb Q}M=1$, and $M=E_1\Pi E_2$ with $E_1=I$, $\Pi=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $E_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}$.

Let $s$ and $g$ be the row and column indices of $\Pi$. To apply the shear, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$. For each entry $\Pi_{sg}=1$, update $H_s\gets H_s+D_g$. Then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. The result is $H+E_1\Pi E_2D=H+MD$, and $D$ is unchanged.

A lower-triangular transformation costs $O(V)$, where $V$ is the stored bit volume. Update coordinates in descending order: at coordinate $i$, add a fixed combination of coordinates $j<i$. Each $j<i$ is reached only after $i$, so it still holds its original value. Each pass is linear in the stored bits, and $m$ is fixed.

Each update $H_s\gets H_s+D_g$ is one interchange, which swaps the contents of two equal fields, plus two additions: $D_g\gets D_g+H_s$, swap, then $D_g\gets H_s-D_g$. On a pair $(h,d)$ this gives $(h+d,d)$. So the shear needs $\operatorname{rank}_{\mathbb Q}M$ interchanges plus $O(V)$ further work.

Each edge of the bit network carries such a matrix, whose rank is its edge rank. The interchange count of the network is the sum of the edge ranks, which the paper bounds by a rank budget of the network (its motif-residual lemma). That sum is less than the number of wires times $m$, so the recurrence saves a power of the chunk width (the length of each interchanged address chunk). <cite data-source="paper">Because the sum of these ranks is less than the number of wires times</cite>.

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

Write the body to `exegenius/tasks/0113-write-address-shear-factorization.answer.md` and the JSON to `exegenius/tasks/0113-write-address-shear-factorization.answer.json`, then run `exegenius submit 0113-write-address-shear-factorization` in the project directory. If submit rejects the answer, fix the answer and submit again.
