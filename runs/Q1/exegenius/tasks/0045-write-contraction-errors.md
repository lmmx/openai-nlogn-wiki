# exegenius task 0045-write-contraction-errors

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
- Cyclic convolution
- Normalized discrete Fourier transform (also: DFT, normalized Fourier transform, multidimensional transform)
- Radix-digit reduction (also: radix-digit polynomials, carry propagation)
- Lexicographic array layout and logical volume (also: address field, logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings (also: prefix-controlled cyclic shift, triangular update)
- Gaussian dyadic fixed-point arithmetic (also: disk grid, Q_p truncation, Gaussian dyadics)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, R_r)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Normalized butterfly H₀ (also: butterfly, Hadamard butterfly)
  - $H_0$ (normalized butterfly): The 2×2 matrix ½[[1, 1], [1, −1]] sending a pair (u, v) to ((u + v)/2, (u − v)/2).
- Two-point kernel C (also: translation kernel, aI+bX)
  - $C$ (two-point kernel): The 2×2 complex matrix aI + bX with a = (1 + i)/2, b = (1 − i)/2 and X the coordinate swap.
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
- Binary phase interface of the complex network (also: phase frame, complex network)
- Address shear
- Lower triangular (Bruhat) factorization
- Matrix shear by rank-many interchanges
- Row splitting among wire roles
- Volume-normalized recursion and the power saving (also: recursive saving)
- Fixed-tape depth-first schedule (also: parking stack)
- Power-width interchange
- Fast address-chunk interchange (also: chunk swap, address interchange, arbitrary-width interchange)
- Packed selected-bit addition (also: binary change of basis, deterministic repair, guard values)
- Recursive C-layer via phase frames
- Simultaneous butterfly layer (also: parallel butterfly layer, normalized butterfly layer)
- Synthetic polynomial transform (also: Nussbaumer transform, decimation in frequency, bit-reversed order)
- Signed Kronecker packing (also: Kronecker substitution)
- Gaussian resampling
- Bluestein's chirp identity (also: chirp transform, chirp)
- Chinese-remainder convolution map (also: Agarwal–Cooley map, CRT map)
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

Concept: Contractions and error accounting
Gloss: Linear maps of operator norm at most one do not amplify errors, so errors of approximate algorithms for contractions (and bilinear contractions) simply add when composed.

## Where the argument relies on this page

- Normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ is approximated with error below $\sqrt2M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Ring convolution from the retained layout](synthetic-convolution.md))
- On $d-1$ power-of-two axes of length $2^{\ell}$ or $2^{\ell-1}$ over $\mathcal R_r$, the forward synthetic transform $LBF_{\boldsymbol t}^-$ and its opposite $F_{\boldsymbol t}^+B^{-1}L^{-1}$ are computed with error below $\sqrt2\ell\,2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$. (on [Transform layout and cost](transform-layout.md))
- Because truncation commutes with the signed coefficient permutation $J_E$, each round equals one truncation after an exact contraction, so errors add to below $\sqrt2\ell\,2^{-p}$.
- Two forward errors, the product truncation and the opposite error add through contractions, and the scale $M$ gives error below $\sqrt2M(3\ell+1)2^{-p}$.
- For coprime $s<t$ with enough separation, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ for linear contractions $A,B_0$ that have disk-grid approximations with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$, the coordinate permutations $P_s,P_t$ being kept inside the identity. (on [Resampling with retained permutations](resampling-retained.md))
- The ordered approximations $\widetilde A$ and $\widetilde B_0$ have errors $16p<p^2$ and $4+3p^2/4<p^2$.
- On $d$ axes, $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$; the linewise approximations of $\mathcal A,\mathcal B_0$ have error below $dp^2$, line work $O(dTp^{3/2+\delta}\alpha)$ and axis movement $O(Tp\,d^2(1+\ell^\tau))$ in the padded box. (on [Tensor resampling interface](tensor-resampling.md))
- Each axis map is a contraction with error below $p^2$, so the $d$ axis maps compose to error below $dp^2$.
- Every recovered convolution coefficient is within less than $1/2$ of the true integer, so rounding gives the exact coefficients and carry propagation gives exactly the $2n$-bit product. (on [Precision analysis and exact recovery](precision-recovery.md))
- The returned ring convolution has error below $E_{\rm ring}=M(3L+2)<5TL$ and keeps the disk margin $\|\cdot\|<.701$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian dyadic fixed-point arithmetic](fixed-point.md): Complex numbers whose real and imaginary parts have power-of-two denominators, stored as fixed-width two's-complement numerators on the p-bit disk grid, with truncation Q_p toward zero to 2^{−p}ℤ.
  Shown as: Contractions and error accounting *<predicate>* Gaussian dyadic fixed-point arithmetic
- [Linear maps, matrices and rank](linear-algebra.md): Vector spaces over a field, linear maps represented by matrices, invertibility, and the rank of a matrix as the dimension of its image.
  Shown as: Contractions and error accounting *<predicate>* Linear maps, matrices and rank

## Pages that build on this one

- Resampling with retained permutations: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A, in which the two coordinate permutations of Gaussian resampling are kept inside the transform identity instead of being executed as sorts.
- Transform layout and cost: Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.
- Precision analysis and exact recovery: The error bookkeeping showing that after undoing the normalizations S and the digit scales, every recovered convolution coefficient is within 1/2 of the true integer, so rounding and carry propagation give the exact product.

## Other pages you may link to

- [The n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Modular arithmetic and finite fields](modular-arithmetic.md)
- [Address shear](address-shear.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
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
- [Power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
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

- "Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error." (paper)

  > routines, put $w_{\rm c}=p+2$. Represent $2^{-p}(a+ib)\in\mathbb D_p$ by a signed $w_{\rm c}$-bit two's-complement word for $a$, followed by one for $b$, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since $|a|,|b|\leq2^p<2^{w_{\rm c}-1}$, this format includes both signs of every permitted numerator, including $-2^p$ and $2^p$. An approximation $\widetilde L:\mathbb D_p^a\to\mathbb D_p^b$ to a linear contraction $L:\mathbb C^a\to\mathbb C^b$ has error $E$ if $2^p\|\widetilde L u-Lu\|<E$ for every input in $\mathbb D_p^a$. The approximation itself need not be linear. Composing such algorithms adds their errors: at each step, insert the exact map at the computed input and use its contraction bound on the accumulated input error.

- "A linear contraction propagates an input error without increasing it." (paper)

  > Put $h_p=2^{-p}$, and use the coefficient sup norm throughout this subsection. An error of $a$ will mean absolute error less than $ah_p$. A linear contraction propagates an input error without increasing it. For a bilinear contraction $\mathcal M$, replacing its operands gives \[ \|\mathcal M(f',g')-\mathcal M(f,g)\| \le \|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|. \] When all four operands are in the disk, their two errors therefore add.


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

Write the body to `exegenius/tasks/0045-write-contraction-errors.answer.md` and the JSON to `exegenius/tasks/0045-write-contraction-errors.answer.json`, then run `exegenius submit 0045-write-contraction-errors` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0045-write-contraction-errors`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
