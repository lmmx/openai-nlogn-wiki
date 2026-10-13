# exegenius task 0035-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n optimality conjecture
  - $n$ (input length): The number of bits in each input integer.
- Multiplication as convolution of digit lists
- Discrete Fourier transform
- Multidimensional transform
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial, a power of two.
- Synthetic polynomial transform
- Two-point butterfly H₀
  - $H_0$ (butterfly map): The map sending a pair of values to their half-sum and half-difference.
  - $u$ (first value): The first input value of the pair.
  - $v$ (second value): The second input value of the pair.
- Chinese-remainder address map onto prime axes
- Gaussian resampling
- Bluestein chirp identity
- Signed packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Linear networks with roles and frames
- Three-element-subset finite networks
  - $s$ (number of calls): The number of smaller calls the network makes.
  - $W$ (number of roles): The number of wires (roles) of the network.
  - $m$ (space dimension): The dimension of the fixed space whose subspaces label the network.
- Scratch-restoring exchange network
- Recursive power saving
  - $s$ (number of calls): The number of smaller calls.
  - $W$ (number of roles): The number of roles of the network.
  - $m$ (parameter multiplier): The factor by which the recursive parameter grows.
- Elementary scans and controlled shifts
- Lower triangular factorization
  - $m$ (matrix size): The number of rows and columns of the matrix.
  - $a$ (matrix rank): The rank of the matrix.
- Rational matrix shear of address fields
- Fast address-field interchange
  - $V$ (bit volume): The number of stored bits.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant below 1.
- Phase frames for the butterfly layer
- Simultaneous butterfly layers
  - $V$ (bit volume): The number of stored bits.
  - $d$ (chunk count): The number of address chunks whose selected bit is transformed.
  - $\lambda'$ (saving exponent): A fixed constant below 1.
- Synthetic character cancellation
- Retained frequency order and transform layout
- Normalized convolution over the ring
- Resampling without executing permutations
- Tensor interface for growing dimension
- Chirp and permutation cancellation
- Fixed-point precision and exact recovery
- Fixed rational parameter choice
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg n)
- Binary representation and bit operations (also: bits, XOR, bit position, binary expansion, radix representation)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, fast Fourier transform)
- Convolution (also: cyclic convolution, product of coefficient sequences, polynomial multiplication as convolution)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/n)
- Primes and coprimality (also: distinct primes, relatively prime, gcd, greatest common divisor, prime number theorem)
- Chinese remainder theorem (also: CRT)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, lower triangular matrix, matrix rank, identity matrix)
- Vector spaces and subspaces (also: change of basis, linear subspace, linear independence, basis)
- Permutations (also: permutation matrix, partial permutation, bijection of indices)
- Floor, ceiling and rounding (also: nearest integer, floor function, integer part)
- Recursion and recurrence relations (also: divide and conquer, recurrence, master theorem, recursive calls)
- Fixed-point and dyadic arithmetic (also: fixed-point numbers, dyadic rationals, truncation error, rounding error)
- Complex conjugate and modulus (also: conjugate, absolute value of complex number, Gaussian integers)
- Cartesian products and multi-indexing (also: multidimensional array, tuple indices, product of index sets)
- Linear-time scans and tape sorting (also: sorting on tapes, copying a tape, linear scan, tape reversal)
- Deterministic computation and time complexity classes (also: deterministic algorithm, running time, step count, worst-case time)
- Geometric and power-of-two parameter manipulation (also: powers of two, geometric series, exponent inequalities)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.
Heading: Multiplication in time $O(n(\lg n)^{1-\kappa})$

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each input integer.
- $\kappa$ (saving exponent): The fixed constant 2^-182 giving the power saving in the log factor.

## This page in the argument

The step: Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on one fixed multitape machine.
How: reduce to digit convolution, build the fast tape and ring-transform tools bottom up, then assemble reductions, precision and cost
Why: The fast address and butterfly procedures give the savings; the reductions place them inside multiplication. (the sources say so: "The remaining proof places these procedures inside the multiplication" (paper))
Striking feature: The saving is a strict power of the logarithm, $\kappa=2^{-182}$, tiny because every constant was chosen conservatively. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the $n$-bit inputs into radix digits reduces integer multiplication to convolution of short integer coefficient lists, with carries propagated afterwards. (on [Multiplication as convolution of digit lists](convolution-reduction.md))
- The two tape procedures, fast address interchange and simultaneous butterfly layers, exist with power savings.
- Convolution over $\mathbb C[y]/(y^r+1)$ is computed exactly by fast synthetic transforms, where $r$ is a power of two. (on [Synthetic polynomial transform](synthetic-transform.md))
- Each prime-length source transform is expressed through a power-of-two tensor transform and a chirp convolution, with the permutations cancelling. (on [Gaussian resampling](gaussian-resampling.md))
- The reductions and parameters assemble into an exact product with the stated cost.
- Every cost row has power of $p$ at most $1-2\kappa$, giving total time $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S5, S6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: The two tape procedures, fast address interchange and simultaneous butterfly layers, exist with power savings.
How: construct each procedure from its own fixed linear network, after the elementary scans

**S5**: The reductions and parameters assemble into an exact product with the stated cost.
How: place the tools inside the multiplication reduction, choose parameters, and account for every change of representation
- S5.3: A coefficient twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, with the negative wrap giving the cyclic wrap.
  Source: "obtained from the synthetic convolution by a coefficient twist." (paper)
  > The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwistin
- S5.4: The algorithm runs the three source transforms around a pointwise product, undoes the normalizations, rounds and propagates carries.
  Source: "The source-transform procedures now supply the three transforms needed" (paper)
  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

**S6**: Every cost row has power of $p$ at most $1-2\kappa$, giving total time $O(n(\lg n)^{1-\kappa})$.
Source: "The complete large-input bound is consequently" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Multiplication as convolution of digit lists](convolution-reduction.md)): Splitting the $n$-bit inputs into radix digits reduces integer multiplication to convolution of short integer coefficient lists, with carries propagated afterwards.
- S3 (on [Synthetic polynomial transform](synthetic-transform.md)): Convolution over $\mathbb C[y]/(y^r+1)$ is computed exactly by fast synthetic transforms, where $r$ is a power of two.
- S4 (on [Gaussian resampling](gaussian-resampling.md)): Each prime-length source transform is expressed through a power-of-two tensor transform and a chirp convolution, with the permutations cancelling.
- S2.1 (on [Elementary scans and controlled shifts](controlled-shifts.md)): Elementary scans and controlled shifts (updating a field by an offset from earlier control fields) take $O(V)$ steps on a fixed number of tapes.
- S2.2 (on [Fast address-field interchange](address-interchange.md)): Two disjoint address fields of $u$ bits are interchanged in $O(Vu^\tau)$ steps for a fixed $\tau<1$ (fast address interchange).
- S2.3 (on [Simultaneous butterfly layers](fast-butterfly-layer.md)): The two-point butterfly $H_0$ is applied at the same bit of up to $d$ address chunks on complex fixed-point records in $O(Vd^{\lambda'})$ with $\lambda'<1$.
- S5.1 (on [Fixed rational parameter choice](parameter-choice.md)): Fixed rational exponents and sizes $p=6b$, $d=\lfloor b^\epsilon\rfloor$ make all costs fit the theorem.
- S5.2 (on [Chinese-remainder address map onto prime axes](chinese-remainder-map.md)): The digit coefficient list is placed on a product of pairwise coprime cyclic axes by a Chinese-remainder map that preserves convolution.
- S5.5 (on [Fixed-point precision and exact recovery](exact-recovery.md)): The recovered coefficient error is below $1/2$, so rounding and carry propagation give the exact product.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Schönhage–Strassen n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen proposed n log n as optimal growth for multiplying n-bit integers on multitape machines; Harvey–van der Hoeven reached O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Schönhage–Strassen n log n optimality conjecture
- [Multiplication as convolution of digit lists](convolution-reduction.md): Splitting inputs into radix digits turns integer multiplication into convolution of short integer coefficient lists, with carries propagated afterwards.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Multiplication as convolution of digit lists
- [Chinese-remainder address map onto prime axes](chinese-remainder-map.md): Places the digit coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder address map onto prime axes
- [Tensor interface for growing dimension](tensor-resampling.md): Applies the one-dimensional resampling maps line by line along d axes, using chunk swaps to move axes, giving R F_s = 2^γ B₀ Q F_t A.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Tensor interface for growing dimension
- [Chirp and permutation cancellation](chirp-permutation-cancellation.md): Chirp identity Q F_t u = ā·(a*(ā·u))/T computes the permuted middle transform as a convolution, and the source permutation R cancels across forward transforms, product and opposite transform.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chirp and permutation cancellation
- [Normalized convolution over the ring](normalized-convolution.md): Convolution over the polynomial ring computed as two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, normalized by 1/(rM).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Normalized convolution over the ring
- [Fast address-field interchange](address-interchange.md): Interchanges two disjoint address fields of u bits via pointwise XOR combinations that end as an exact permutation, in O(V u^τ) with τ<1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast address-field interchange
- [Simultaneous butterfly layers](fast-butterfly-layer.md): Applies H₀ at the same bit position of up to d address chunks at once on complex fixed-point records, in O(V d^λ′) with λ′<1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Simultaneous butterfly layers
- [Fixed-point precision and exact recovery](exact-recovery.md): Intermediate values are exact Gaussian dyadics truncated once; the recovered coefficient error is below 1/2 so rounding and carry propagation give the exact product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed-point precision and exact recovery
- [Fixed rational parameter choice](parameter-choice.md): The fixed exponents (τ=σ=1−2⁻⁵⁰, λ′=1−2⁻⁵⁴, ε=2⁻⁷⁵, κ=2⁻¹⁸²) and size parameters p=6b, d=⌊b^ε⌋ making all costs fit the theorem.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed rational parameter choice
- [Elementary scans and controlled shifts](controlled-shifts.md): Linear-time tape operations: digit moves, splitting rows cyclically into streams, and updating a target field by an offset computed from earlier control fields.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Elementary scans and controlled shifts

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](polyring-mod.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Three-element-subset finite networks](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Scratch-restoring exchange network](scalar-motif-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational matrix shear of address fields](matrix-shear.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hvdh-subroutine.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase frames for the butterfly layer](phase-frames.md)
- [Synthetic character cancellation](synthetic-character-cancellation.md)
- [Retained frequency order and transform layout](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling without executing permutations](resampling-lemma.md)
- [Bluestein chirp identity](bluestein-chirp.md)

## Evidence from the sources, with the paragraph around each quote

- "We obtain a strict power saving in the
logarithmic factor" (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.

- "We now use the preceding algorithms to multiply two $n$-bit integers." (paper)

  > We now use the preceding algorithms to multiply two $n$-bit integers. An equal-width address swap on logical bit volume $V$ costs $O(Vu^\tau)$ for width $u$. A completed parallel normalized butterfly layer costs $O(Vd^{\lambda'})$ and has coefficient error less than $\sqrt2\,2^{-p}$. The ordered Gaussian resampling maps are contractions; their disk-grid approximations have error less than $p^2 2^{-p}$ and cost $O(tp^{3/2+\delta}\alpha)$ on a line of length $t$. Address permutations and intermediate dyadic arithmetic are exact. We choose compatible parameters for these procedures, recover the integer coefficients from their approximations, and account for the remaining tape operations.


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

Write the body to `exegenius/tasks/0035-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0035-write-main-theorem.answer.json`, then run `exegenius submit 0035-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
