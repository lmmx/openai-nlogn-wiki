# exegenius task 0027-write-simultaneous-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis of algorithms and solving simple cost recurrences, basic Turing machines and multitape simulation, binary representation of integers and machine arithmetic (carries, two's complement, XOR, fixed-point rounding), and the discrete mathematics taught to everyone (induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, permutations, binomial coefficients, lexicographic order). From the required mathematics they have a first course in linear algebra (vectors, matrices, rank, invertibility, triangular and diagonal matrices, linear maps over Q and C) and basic complex numbers and polynomials. They have not studied tensor products of operators, bilinear forms, Hadamard or Bruhat-type factorizations, FFT variants beyond a textbook mention, or research-level integer multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
  - $n$ (input bit length): The number of bits in each input of the subroutine multiplication.
  - $O$ (big-O bound): Asymptotic upper bound up to a constant factor.
- Array streams and logical volume (also: logical volume, address field, row)
- Elementary stream operations
- Controlled shifts (also: prefix-controlled cyclic shift)
- Normalized butterfly H₀ (also: H0)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).
- Gaussian dyadics and fixed-point truncation (also: disk grid, Q_p truncation, guard bits)
- Linear bank-exchange network (also: finite network, role, wire)
- Restoration of arbitrary scratch values (also: transparent computation)
- Three-element-subset gather and scatter (also: index-code decoding, Frankl–Wilson construction)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels (also: orthogonal residual, labels)
- Rank deficit of the network (also: s < Wm)
- Address shear (also: shear)
- Rational matrix interface (also: bit network)
- Lower triangular factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Row splitting among roles
- Volume-normalized recurrence (also: recursive saving)
- Fast address chunk interchange (also: chunk swap, address interchange)
- Binary phase frames (also: kernel C, phase kernel)
- Binary phase interface (also: complex network)
- Packed selected-bit addition (also: binary change of basis, deterministic repair)
- Binary representation of integers (also: n-bit integer, base-2 expansion, binary digits, bits)
- Carry propagation (also: carries, ripple carry, radix carries, positional addition)
- Two's complement (also: sign-extended two's complement, signed binary integers, sign extension)
- Exclusive or (also: XOR, addition modulo 2, bitwise XOR)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Floor and ceiling (also: floor function, ceiling function, integer part, ⌊x⌋, ⌈x⌉)
- Rounding to the nearest integer (also: rounding, truncation toward zero, round-off error)
- Fixed-point numbers (also: fixed-point arithmetic, binary fractions, dyadic fractions in a word)
- Binary logarithm (also: lg, log base 2, logarithm, log n)
- Modular arithmetic (also: congruence modulo m, residues, mod, a ≡ b (mod m), centered residue)
- Greatest common divisor (also: gcd, coprime, relatively prime)
- Prime numbers (also: primes, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Recurrence relations for running time (also: recurrence, divide-and-conquer recurrence, unrolling a recurrence)
- Geometric series (also: geometric sum, sum of a geometric progression)
- Permutations (also: permutation, bijection of a finite set, reordering, inverse permutation)
- Binomial coefficients (also: n choose k, binom, k-element subsets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Vectors and matrices (also: matrix, vector, matrix multiplication, identity matrix, transpose)
- Vector spaces, subspaces and dimension (also: linear subspace, basis, dimension, span, linear map)
- Matrix rank (also: rank, column rank, full rank)
- Invertible matrices (also: nonsingular matrix, inverse matrix, determinant nonzero)
- Triangular and diagonal matrices (also: lower triangular matrix, upper triangular, diagonal matrix, diag, unit triangular)
- Permutation matrices (also: permutation matrix, partial permutation matrix)
- Gaussian elimination (also: row reduction, elimination, LU decomposition)
- Rational numbers (also: Q, fractions, rational matrix)
- Maximum norm (also: infinity norm, sup norm, ‖·‖∞, max absolute entry)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Exponential function and Euler's formula (also: e^{iθ}, Euler's formula, Gaussian function e^{-x^2})

## This page

Concept: Simultaneous butterfly layer
Gloss: Applying H₀ on the same bit position in up to d address chunks at once in O(Vd^{λ'}) time, λ' < 1, by recursing through the complex network and evaluating the layer exactly before one truncation.
Also called: fast butterfly layer, parallel butterfly

## This page in the argument

The step: On arrays $[P]\times[2^K]^D\times[S]$ of polynomial records with $D\le d$, the tensor product of $H_0$ on one selected bit in each of the $D$ chunks, followed by one truncation $Q_p$, costs $O(Vd^{\lambda'})$ with $\lambda'<1$ and error below $\sqrt2\,2^{-p}$.
How: write $H_0^{\otimes D}$ through the kernel $C^{\otimes D}$, apply $C^{\otimes e}$ recursively by the complex network on groups of $e=mf$ axes with packed binary basis changes, and bound the exact dyadic growth before a single truncation
Why: Separate butterfly factors would need $D$ whole-array passes; the complex network replaces them by $s_{\rm c}$ calls on streams of volume $V/W_{\rm c}$, so the normalized recursive factor $s_{\rm c}/W_{\rm c}<m^\sigma$ saves a power of $d$. (the sources say so: "whereas separate butterfly
factors would require $D$ whole-array passes." (paper))

Its sub-steps, in order:

- In the complex network with binary labels each edge's phase-frame change is a product of one kernel $aI+bX_v$ or its inverse per residual basis vector, these number $s_{\rm c}<W_{\rm c}m$ in total, and after endpoint corrections the network applies $C^{\otimes m}$ on every role. (on [Binary phase interface](complex-motif-interface.md))
- Applying the network with column frames to $e=mf$ selected axes uses exactly $s_{\rm c}$ child calls, each on the $f$ axes of one slot, and yields $C^{\otimes e}$; inverse children cost one forward call.
- The normalized layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, so it differs from the $C$ layer only by diagonal phases and a dyadic scale.
- XORing selected bits of one address chunk into another, restoring a third chunk, costs $O(V(L^\tau+1))$ via eight packed cyclic shifts with guard bits and a deterministic repair of the bounded exceptional set. (on [Packed selected-bit addition](packed-selected-bit.md))
- Splitting rows among the $W$ roles gives each of the $s$ child calls volume $V/W$, so $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$.
- Every intermediate value is a Gaussian dyadic of depth at most $C_0d^{C_1}=o(p)$, so $O(p)$-bit words represent the whole layer exactly until the final truncation.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: build two tape procedures that beat a scan per level (fast chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, place them in the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, recover the product exactly, and total the costs (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2, S2.3, S2.5, S2.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: Applying the network with column frames to $e=mf$ selected axes uses exactly $s_{\rm c}$ child calls, each on the $f$ axes of one slot, and yields $C^{\otimes e}$; inverse children cost one forward call.
Source: "$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S2.3**: The normalized layer is $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, so it differs from the $C$ layer only by diagonal phases and a dyadic scale.
Source: " H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S2.5**: Splitting rows among the $W$ roles gives each of the $s$ child calls volume $V/W$, so $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$.
Source: "\(V/W\), so their total cost is \(s(V/W)F(e/m)\).  Dividing by" (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S2.6**: Every intermediate value is a Gaussian dyadic of depth at most $C_0d^{C_1}=o(p)$, so $O(p)$-bit words represent the whole layer exactly until the final truncation.
Source: "the same as \(t\) successive halvings.  Thus reserving \(p+\Delta\)" (paper)
> To see how this count controls numerical size, start with disk-valued coefficients in \(2^{-p}\mathbb Z[i]\). A value at depth \(\ell\) lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\). This follows by induction: addition or subtraction can at most double the maximum modulus of its operands; halving adds at most one denominator bit; and signs and multiplication by \(i\) preserve both bounds. The charge of \(t\) for the final shift is the same as \(t\) successive halvings. Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow. Shifts consume the reserved fractional zeros and discard no bits.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Binary phase interface](complex-motif-interface.md)): In the complex network with binary labels each edge's phase-frame change is a product of one kernel $aI+bX_v$ or its inverse per residual basis vector, these number $s_{\rm c}<W_{\rm c}m$ in total, and after endpoint corrections the network applies $C^{\otimes m}$ on every role.
- S2.4 (on [Packed selected-bit addition](packed-selected-bit.md)): XORing selected bits of one address chunk into another, restoring a third chunk, costs $O(V(L^\tau+1))$ via eight packed cyclic shifts with guard bits and a deterministic repair of the bounded exceptional set.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Binary phase frames](phase-frames.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase interface](complex-motif-interface.md): The complex network with binary labels: after endpoint corrections it applies the tensor power of the kernel C on every role using s_c < W_c·m smaller kernel calls.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase interface
- [Packed selected-bit addition](packed-selected-bit.md): XORing selected bits of one address chunk into another by eight packed cyclic shifts with guard bits, followed by deterministic repair of an explicitly bounded set of exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Volume-normalized recurrence](volume-recurrence.md): The recurrence F_k ≤ (s/W)F_{k−1} + O(1) for cost divided by volume, which yields a power saving because s/W < m.
  Shown as: Simultaneous butterfly layer *<predicate>* Volume-normalized recurrence
- [Normalized butterfly H₀](butterfly.md): The two-point map (u, v) ↦ ((u+v)/2, (u−v)/2), the basic step of radix-two Fourier transforms.
  Shown as: Simultaneous butterfly layer *<predicate>* Normalized butterfly H₀
- [Gaussian dyadics and fixed-point truncation](gaussian-dyadics.md): Complex numbers whose real and imaginary parts have power-of-two denominators, stored exactly in fixed-point words and truncated toward zero to the p-bit grid only at the end of a layer.
  Shown as: Simultaneous butterfly layer *<predicate>* Gaussian dyadics and fixed-point truncation
- [Row splitting among roles](row-splitting.md): Distributing rows of an array cyclically among the W wire roles so that each role stream has the same address shape and volume V/W.
  Shown as: Simultaneous butterfly layer *<predicate>* Row splitting among roles

## Pages that build on this one

- Transform layout: A positional permutation of address bits placing the bits used in each transform round at a common offset in consecutive K-bit chunks, so simultaneous layers apply and the frequency order is retained.
- Parameter choice and cost table: Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Linear bank-exchange network](linear-network.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Array streams and logical volume](stream-array-layout.md)
- [Frames and the common-frame identity](frame-invariant.md)
- [Address shear](address-shear.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled shifts](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Three-element-subset gather and scatter](triple-gadget.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank deficit of the network](rank-deficit.md)
- [Rational matrix interface](bit-motif-interface.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Fast address chunk interchange](chunk-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed coefficient packing](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-fft.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Transform layout](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choice and cost table](cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0027-write-simultaneous-layer.answer.md` and the JSON to `exegenius/tasks/0027-write-simultaneous-layer.answer.json`, then run `exegenius submit 0027-write-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0027-write-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
