# exegenius task 0052-write-parameter-choice

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Omega, Theta), divide-and-conquer recurrences and standard algorithms including Karatsuba multiplication and the radix-two FFT for polynomial multiplication, and basic models of computation including multitape Turing machines. From discrete mathematics they know induction, sets and binomial coefficients, binary and two's-complement representation, primes, gcd, modular arithmetic and the Chinese remainder theorem. From a first linear algebra course they know vector spaces, bases, subspaces, matrices, invertibility, Gaussian elimination, permutation and diagonal matrices and projections, and from calculus the exponential and logarithm, geometric series, Newton's method and elementary error bounds such as the triangle inequality. They have not studied Fourier analysis beyond the FFT, abstract algebra beyond modular arithmetic, numerical analysis of fixed-point transforms, or research-level integer multiplication techniques such as Schönhage–Strassen, Nussbaumer transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- Modular arithmetic
- Matrices, linear maps and rank
- The field F₂ and XOR
  - $\mathbb F_2$ (two-element field): The field with elements 0 and 1, where addition is XOR and multiplication is AND.
- Symmetric bilinear forms and orthogonal complements
- Tensor products
- Gaussian dyadic numbers
- Cyclic convolution
- Discrete Fourier transform (also: normalized Fourier transform, Fourier transform)
- Multidimensional Fourier transforms (also: tensor transform)
- Normalized butterfly H₀ (also: butterfly layer)
  - $H_0$ (normalized butterfly): The two-point map sending (u,v) to ((u+v)/2,(u−v)/2).
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Harvey–van der Hoeven O(n log n) multiplier
  - $n$ (input bit length): The number of bits in each integer multiplied by the subroutine.
- Integer multiplication as digit convolution
- Arrays as address-ordered tape streams (also: logical volume, address field, row)
- Elementary stream operations
- Controlled shifts and rational scalings
- Linear networks, wires and roles
- Restoring arbitrary scratch values (also: transparent computation)
- Three-element subset construction (also: gather, scatter, side injection)
- Three-stage bank exchange
- Frames and the common-frame identity
- Subspace labels and orthogonal residuals (also: label, edge residual)
- Rank deficit s < Wm
  - $s$ (smaller call count): The total number of smaller recursive calls, summed over all edges of the network.
  - $W$ (wire count): The number of wires (roles) in the network, including scratch wires.
  - $m$ (label dimension): The dimension of the ambient label space, equal to the number of digit fields or selected axes a call is split into.
- Volume-normalized recursion (also: recursive saving, power saving)
- Explicit exponents τ and σ
  - $\tau$ (interchange exponent): The exponent with s_b/W_b < m^τ, giving chunk interchange cost O(V u^τ).
  - $\sigma$ (butterfly exponent): The exponent with s_c/W_c < m^σ, bounding the recursive cost of the complex phase network.
- Address shear
- Rational matrix interface of the bit network
- Lower triangular factorization
- Cost of a rational matrix shear
- Power-width chunk interchange
- Fast address chunk interchange (also: chunk swap, address interchange)
- Two-point kernel C
  - $C$ (two-point kernel): The 2×2 matrix aI + bX with a = (1+i)/2 and b = (1−i)/2, where X swaps the two coordinates.
- Binary phase frames
- Binary phase interface of the complex network
- Packed selected-bit addition
- Batched recursion for a common layer
- Guard width for exact layer evaluation
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Disk grid values and truncation
- Polynomial ring modulo yʳ + 1
  - $\mathbb C$ (complex numbers): The field of complex coefficients of the polynomials.
  - $y$ (polynomial variable): The indeterminate whose powers serve as roots of unity.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Transform layout and stored frequency order
- Signed coefficient packing (also: Kronecker substitution)
- Normalized convolution over the polynomial ring
- Gaussian resampling
- Tensor resampling interface
- Bluestein chirp identity
- Source permutation cancellation
- Coefficient twist (also: phase twist)
- Big-Omega and Big-Theta notation (also: Ω, Θ, asymptotic lower bound, tight bound)
- Worst-case running time (also: time complexity, T_A(n), worst-case cost, linear time)
- Logarithms, floor and ceiling (also: log₂, lg, natural logarithm, ⌊x⌋, ⌈x⌉)
- Exponential function (also: exp, e^x, Gaussian function exp(−x²))
- Euler's formula and complex roots of unity (also: e^{iθ}, primitive root of unity, ω = e^{2πi/n}, unit circle)
- Binary representation of integers (also: bin_k, val, base-2 representation, radix representation, positional notation, most significant bit)
- Two's complement (also: two's-complement words, signed binary integers)
- Fixed-point numbers and rounding (also: fixed-point arithmetic, truncation, rounding to the nearest integer, precision p bits)
- Integer division with remainder (also: quotient and remainder, Euclidean division, divisibility)
- Prime numbers and trial division (also: primes, odd prime, primality test)
- Greatest common divisor and coprimality (also: gcd, pairwise coprime, relatively prime, prime to q, Euclidean algorithm)
- Modular inverses and units (also: unit mod q, invertible residue, multiplicative inverse modulo q)
- Chinese remainder theorem (also: CRT, Chinese remainder, simultaneous congruences)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-2 FFT, butterfly)
- Polynomial evaluation and interpolation (also: Lagrange interpolation, point-value representation)
- Karatsuba multiplication (also: Karatsuba–Ofman algorithm, O(n^{log₂3}) multiplication)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree)
- Geometric series (also: geometric sum)
- Mathematical induction (also: proof by induction, inductive step)
- Sets, Cartesian products and lexicographic order (also: Cartesian product, lexicographic order, row-major order, tuples)
- Subsets and binomial coefficients (also: binom(h,3), k-subsets, combinations, intersection size)
- Permutations (also: bijection, permutation matrix, inverse permutation, reordering)
- Hamming weight (also: wt(x), number of ones, population count)
- Vector spaces, subspaces, bases and dimension (also: subspace, basis, dimension, span, linear independence, coordinate space)
- Invertible matrices and the general linear group (also: invertible matrix, nonsingular matrix, GL(m, F), matrix inverse, identity matrix)
- Gaussian elimination (also: row reduction, elementary row operations, triangular matrices)
- Diagonal matrices and pointwise products (also: diagonal operator, diag, Hadamard (entrywise) product, pointwise multiplication)
- Linear projections (also: projection onto U, projector, complementary subspace)
- Matrix transpose (also: transpose, matrix transposition, Aᵀ)
- Maximum norm and triangle inequality (also: sup norm, ℓ∞ norm, ‖x‖∞, triangle inequality, absolute value)
- Newton's method (also: Newton iteration, Newton reductions, reciprocal approximation)
- Depth-first traversal (also: depth-first schedule, depth-first search, recursion order)

## This page

Concept: Fixed rational parameter choice
Gloss: The conservative constants τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, c = 2⁻⁵⁶, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², and sizes p = 6⌈log₂ n⌉, d = ⌊b^ε⌋, K = ⌊d^c⌋ that satisfy all layer and cost conditions.

## This page in the argument

The step: The fixed rational constants $\tau=\sigma=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, $\kappa=2^{-182}$ satisfy all layer and cost conditions.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: build two fast tape procedures (address interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, assemble them into the transform-based convolution algorithm, prove exact recovery and bound the total time (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- An explicit fixed-tape algorithm computes approximations to the radix-$2^b$ digit convolution of the inputs through the CRT map, two forward resampled source transforms, a pointwise product and the inverse transform.; how: fix the rational parameters, map digits to prime axes by the CRT, convert the power-of-two convolution to the polynomial ring by a twist, build the source-transform procedures, and run them on the digit arrays (on [The multiplication algorithm](multiplication-algorithm.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Explicit exponents τ and σ](motif-exponents.md): The fixed rational exponents τ = σ = 1 − 2⁻⁵⁰ for the address and butterfly recurrences, justified because both relative rank deficits exceed 20·2⁻⁵⁰.
  Shown as: Fixed rational parameter choice *<predicate>* Explicit exponents τ and σ
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ on the same bit position of up to d address chunks at once, exactly in Gaussian dyadics followed by one truncation, in O(V d^λ′) time with λ′ < 1 instead of d separate passes.
  Shown as: Fixed rational parameter choice *<predicate>* Simultaneous butterfly layer

## Pages that build on this one

- The multiplication algorithm: Split the inputs into radix-2ᵇ digits, map them by the CRT map, compute two forward resampled source transforms, multiply pointwise, apply the inverse transform, rescale, round and propagate carries.
- Complete time bound: The cost table, normalized by V = Tp = Θ(n), whose every dominant term is a power of p at most 1 − 2κ, giving total time O(n (log n)^{1−κ}).

## Other pages you may link to

- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](butterfly-h0.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [n log n optimality conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Arrays as address-ordered tape streams](tape-array-layout.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [The field F₂ and XOR](binary-field-xor.md)
- [Matrices, linear maps and rank](linear-algebra-rank.md)
- [Linear networks, wires and roles](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Address shear](address-shear.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-element subset construction](subset-construction.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Symmetric bilinear forms and orthogonal complements](bilinear-forms.md)
- [Tensor products](tensor-products.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Volume-normalized recursion](volume-normalized-recurrence.md)
- [Rational matrix interface of the bit network](bit-network-interface.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Fast address chunk interchange](chunk-interchange.md)
- [Two-point kernel C](phase-kernel-c.md)
- [Binary phase frames](phase-frames.md)
- [Binary phase interface of the complex network](binary-phase-interface.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Batched recursion for a common layer](layer-recursion.md)
- [Guard width for exact layer evaluation](guard-width.md)
- [Disk grid values and truncation](fixed-point-grid.md)
- [Signed coefficient packing](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](multiplication-as-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional Fourier transforms](multidimensional-dft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Transform layout and stored frequency order](transform-layout.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Complete time bound](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "These constants are deliberately conservative; no optimization is claimed." (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

- "The comparison constants can be fixed for every input length at once." (paper)

  > iently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\leq d\leq p^\epsilon, \qquad \frac{p}{12d}\leq\ell\leq\frac{p}{3d}. \] Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer and transform interfaces. Their pointwise bounds cover every computed pair $(d,r)$, including all choices arising at the same $p$. These bounds also give that $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$, and $\ell/K\to\infty$. There are eventually enough axes for the $O(\log d)$ reserved row axes and enough bits for all work blocks.


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

Write the body to `exegenius/tasks/0052-write-parameter-choice.answer.md` and the JSON to `exegenius/tasks/0052-write-parameter-choice.answer.json`, then run `exegenius submit 0052-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0052-write-parameter-choice`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
