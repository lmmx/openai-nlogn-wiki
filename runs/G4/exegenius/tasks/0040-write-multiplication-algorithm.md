# exegenius task 0040-write-multiplication-algorithm

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Integer multiplication as digit convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform layout and cost
- Convolution from the retained transform layout
- Coefficient twist to the negacyclic ring
- Gaussian resampling
- Multidimensional resampling on a padded box
- Bluestein chirp identity
- Source permutation cancellation
- Chinese-remainder axis map
- Parameter choices
- Exact recovery of the integer product
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: The multiplication algorithm
Gloss: Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.

## This page in the argument

The step: The algorithm maps the digit polynomials by the Chinese-remainder map to prime axes, transforms them by resampling plus chirp convolution, multiplies pointwise, applies the opposite transform, rescales, rounds and propagates carries.
How: Use the convolution theorem on the prime-axis tensor: the digit convolution equals $F^+(Fu\cdot Fv)$ up to known scales, with the middle transform $QF_{\boldsymbol t}$ computed as a chirp convolution through the twist and synthetic convolution.
Why: The source-transform procedures supply the three transforms needed for the radix-digit convolution. (the sources say so: "The source-transform procedures now supply the three transforms needed" (paper))

Its sub-steps, in order:

- With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, power-of-two axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and distinct primes $s_i$ just below $t_i$, we have $Tp=\Theta(n)$ and every hypothesis of the layer, transform and resampling lemmas holds. (on [Parameter choices](parameter-choices.md))
- The map $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ and $P_i=\prod_{j<i}s_j$ takes cyclic convolution of length $S=\prod_is_i$ to multidimensional cyclic convolution, and is implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time. (on [Chinese-remainder axis map](crt-axis-map.md))
- The map $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic convolution in the last coordinate into convolution modulo $y^r+1$, so the power-of-two complex cyclic convolution reduces to the synthetic one at cost $O(Tp^{1+\delta})$ for the twists. (on [Coefficient twist to the negacyclic ring](convolution-twist.md))
- The middle factor $QF_{\boldsymbol t}$ is evaluated by the chirp transform $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0))$ using the complex convolution.
- The source transform applies $\mathcal A$, the chirp transform, $\mathcal B_0$ and the exact scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
- Convert to digits, apply $\Phi$, transform both operands, multiply pointwise, apply the opposite transform, scale by $S$ and $2^{2b+4}S$, round, undo $\Phi$ and propagate carries.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S6.4, S6.5, S6.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S6.4**: The middle factor $QF_{\boldsymbol t}$ is evaluated by the chirp transform $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0))$ using the complex convolution.
Source: "We next use the complex convolution to evaluate the middle factor" (paper)
> We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps. For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator at tensor address $j$ is computed modulo $2r$ as \[ -\sum_i s_i j_i^2(r/t_i)\pmod{2r}. \] All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$. Scan the stored axis descriptors and compute the $d$ squares and products with the previously established integer multiplier. Additions, reductions modulo a power of two, and restarting local counters cost $O(p)$ per term; multiplication costs $O(p\log p)=O(p^{1+\delta})$. Exponential evaluation then has the same $O(p^{1+\delta})$ bound. Thus chirp construction costs $O(Td p^{1+\delta})$ in total. In particular, this cost includes the scan of the axis descriptors at every coefficient.

**S6.5**: The source transform applies $\mathcal A$, the chirp transform, $\mathcal B_0$ and the exact scale $2^\gamma$, with exact counterpart $RF_{\boldsymbol s}$.
Source: "For a source disk-grid tensor of norm at most $.5$, write" (paper)
> For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.

**S6.6**: Convert to digits, apply $\Phi$, transform both operands, multiply pointwise, apply the opposite transform, scale by $S$ and $2^{2b+4}S$, round, undo $\Phi$ and propagate carries.
Source: "With these streams prepared, perform the following operations." (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S6.1 (on [Parameter choices](parameter-choices.md)): With $b=\lceil\log_2n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, power-of-two axis lengths $t_i\in\{r/2,r\}$ with $\prod_it_i=T$ and distinct primes $s_i$ just below $t_i$, we have $Tp=\Theta(n)$ and every hypothesis of the layer, transform and resampling lemmas holds.
- S6.2 (on [Chinese-remainder axis map](crt-axis-map.md)): The map $x\mapsto\prod_ix_i^{\mu_i}$ with $\mu_i=P_i^{-1}\bmod s_i$ and $P_i=\prod_{j<i}s_j$ takes cyclic convolution of length $S=\prod_is_i$ to multidimensional cyclic convolution, and is implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time.
- S6.3 (on [Coefficient twist to the negacyclic ring](convolution-twist.md)): The map $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic convolution in the last coordinate into convolution modulo $y^r+1$, so the power-of-two complex cyclic convolution reduces to the synthetic one at cost $O(Tp^{1+\delta})$ for the twists.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder axis map](crt-axis-map.md): Mapping a cyclic convolution of length S = ∏ s_i with pairwise coprime s_i to a multidimensional cyclic convolution via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.
  Shown as: The multiplication algorithm *<predicate>* Chinese-remainder axis map
- [Multidimensional resampling on a padded box](tensor-resampling.md): Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.
  Shown as: The multiplication algorithm *<predicate>* Multidimensional resampling on a padded box
- [Bluestein chirp identity](chirp-identity.md): Writing a Fourier transform (with its target permutation) as a pointwise chirp phase, a cyclic convolution with the chirp, and another chirp phase.
  Shown as: The multiplication algorithm *<predicate>* Bluestein chirp identity
- [Source permutation cancellation](permutation-cancellation.md): The coordinate permutation retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
  Shown as: The multiplication algorithm *<predicate>* Source permutation cancellation
- [Coefficient twist to the negacyclic ring](convolution-twist.md): The map x_d ↦ ζy with ζ = e^{πi/r} that turns cyclic convolution in the last coordinate into convolution modulo y^r + 1, so complex cyclic convolution reduces to the synthetic one.
  Shown as: The multiplication algorithm *<predicate>* Coefficient twist to the negacyclic ring
- [Integer multiplication as digit convolution](radix-digit-convolution.md): Writing each n-bit integer as a polynomial in 2^b with digits of b bits, so the integer product is a convolution of digit lists followed by carry propagation.
  Shown as: The multiplication algorithm *<predicate>* Integer multiplication as digit convolution
- [Parameter choices](parameter-choices.md): Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.
  Shown as: The multiplication algorithm *<predicate>* Parameter choices
- [Exact recovery of the integer product](exact-recovery.md): Showing the accumulated numerical error on the recovered coefficients is below 1/2, rounding to integers, and propagating radix carries to the exact 2n-bit product.
  Shown as: The multiplication algorithm *<predicate>* Exact recovery of the integer product

## Pages that build on this one

- Complete time bound: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).
- Sub-n log n integer multiplication: A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.

## Other pages you may link to

- [Convolution](convolution.md)
- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Radix-2 butterflies and FFT](fft-butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout and cost](synthetic-transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex

- "The two occurrences of $S$ in this algorithm undo different
normalizations." (paper)

  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.


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

Write the body to `exegenius/tasks/0040-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0040-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0040-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0040-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
