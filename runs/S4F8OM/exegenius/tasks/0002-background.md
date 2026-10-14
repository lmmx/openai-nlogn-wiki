# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8` (paths below are relative to it)

Say what a specific reader already knows, for these sources. The reader profile describes the reader in a few words, and its examples do not list everything it covers: it stands for a level of study. Make it concrete for the sources.

The sources were written for readers of their own, and use without explanation what those readers know. Read the sources and find that background: the notions, notation and standard results they use without defining. For each, decide whether a reader at the profile's level has been taught it, in the profile's subject or in the subjects that subject rests on (an undergraduate degree in physics teaches linear algebra, Fourier series and probability as well as mechanics, whether or not a profile names them).

- The reader knows what their level of study teaches to everyone at that level. Do not withhold it because the profile does not name it.
- The reader does not know what is taught only in some courses, or in later or specialist study, nor what the sources introduce, define or prove: that is what the wiki explains. When unsure, count it as not known.
- The existing concepts were planned by an earlier task and stay as they are: this answer only adds background they lack.
- `summary`: the subjects and how far into each this reader has gone, as they bear on the sources. Everyone who writes or checks the wiki is shown it with the profile.
- `known`: each concept from that background that the reader knows and no existing concept covers, with the aliases a writer might use for it. Include what the sources use and what an explanation of them would naturally use. Known concepts get no page.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Existing concepts

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper bounds on running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1, with modulus and unit-modulus phases.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.
- `n-log-n-barrier`: The n log n barrier: The Schönhage–Strassen conjecture that n log n is the optimal multiplication cost on multitape Turing machines, and the Harvey–van der Hoeven O(n log n) multiplier, which is used here only as a subroutine on short inputs.
- `convolution`: Convolution: The cyclic convolution of two coefficient lists, equal to the product of the corresponding polynomials modulo x^S − 1.
- `radix-digit-reduction`: Radix-digit convolution: Writing each n-bit integer as a polynomial in 2^b with b-bit digits, so the integer product is the digit convolution followed by carry propagation.
- `discrete-fourier-transform`: Discrete Fourier transform: The normalized transform F_q that averages inputs weighted by roots of unity; it turns convolution into pointwise multiplication.
- `fft-butterflies`: Fast Fourier transform with butterflies: Computing a length-2^a transform in a levels, each pairing entries by a two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) followed by a twiddle multiplication.
- `fixed-point-complex-arithmetic`: Fixed-point complex grid and truncation: Complex numbers stored as signed two's-complement numerators over 2^p, in the unit disk, with truncation toward zero to the grid after exact dyadic arithmetic.
- `contraction-error-propagation`: Contractions and error accounting: Linear maps that do not increase the maximum-modulus norm; composing approximations adds their errors, which is how the accumulated numerical error is bounded.
- `rank-and-orthogonal-subspaces`: Subspaces, rank and orthogonal complements: Matrix rank, subspaces with a bilinear form, nondegenerate subspaces, orthogonal complements and orthonormal bases, as used to label a network.
- `tape-address-model`: Arrays as address fields on tape: An array indexed by a product of ranges is stored in lexicographic order; its logical volume V is the number of data bits, and elementary field moves, digit permutations and row splits cost O(V).
- `controlled-cyclic-shift`: Controlled cyclic shift: Adding to a target address field an offset computed from earlier control fields, modulo a range, in O(V) time by splitting and re-merging blocks.
- `scratch-restoring-exchange`: Scratch-restoring bank exchange: A fixed linear network of copy, gather, scatter and side-injection gates that swaps two banks of values in three stages while returning every auxiliary (scratch) wire to its arbitrary initial value.
- `array-frames`: Frames: changing representation along a network: Replacing each scalar wire by an array and storing it as D_v g for an invertible operator D_v (a frame), so that a pointwise linear gate commutes with the frame and only the endpoint operator remains.
- `subset-intersection-labels`: Triple-subset labels and the rank budget: Subspaces of a fixed space attached to gates and terminals, built from indicator vectors of three-element subsets so that adjacent labels are nested and the total edge rank s is strictly less than the wire count W times the dimension m.
- `address-shear-factorization`: Address shear and triangular factorization: The address map (H,D)↦(H+AD,D) for a rational matrix A of rank a, performed with exactly a interchanges of smaller field pairs after factoring A=E₁ΠE₂ into lower-triangular factors and a partial permutation.
- `rank-saving-recurrence`: Recursive rank saving: Splitting rows among the W network roles makes each recursive call a 1/W-volume stream, so the cost per volume grows by s/W<m when the parameter is multiplied by m, giving a power saving.
- `power-width-interchange`: Power-width chunk interchange: Interchanging two chunks of e=m^k digits in time O(V e^τ) by running the bit network on W role streams, with each edge shear implemented recursively by smaller interchanges.
- `address-chunk-interchange`: Address chunk interchange: Interchanging two disjoint contiguous address fields of u bits of an array in O(V u^τ) time for a fixed τ<1, using XOR combinations of intermediate data although the final effect is an exact permutation.
- `phase-frame-network`: Complex phase network: The second network over Gaussian dyadics with binary labels, whose frames are built from the two-point kernel C=HSH=aI+bX, so each edge is a product of translation kernels and the endpoint operator is C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of many chunks at once by a constant number of whole-chunk cyclic shifts that are correct away from a small set of guard-violating addresses, which are then repaired deterministically by sorting.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree less than r with y^r=−1, in which powers of y are roots of unity and multiplication by y^a is a signed shift of the coefficient list.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A Fourier-type transform over the negacyclic ring whose roots of unity ω_t=y^{2r/t} are signed coefficient shifts, so each twiddle multiplication is free of real arithmetic.
- `stored-frequency-order`: Retained frequency order: The forward transform writes outputs in bit-reversed order; the pointwise product and the opposite transform both use this order, so no permutation is ever executed.
- `transform-tape-layout`: Transform layout on tape: Placing the selected bit of each participating axis at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so that each transform round is one simultaneous butterfly layer.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying two polynomials with small signed integer coefficients by evaluating them at a large power of two, multiplying the resulting integers with the O(n log n) multiplier, and extracting coefficients with centered carries.
- `normalized-ring-convolution`: Normalized convolution over the polynomial ring: Convolving arrays of ring elements by two forward synthetic transforms, a pointwise polynomial product divided by r, and the opposite transform, giving (f*g)/T with a bounded error.
- `coefficient-twist`: Cyclic-to-negacyclic coefficient twist: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution on the last axis to convolution modulo y^r+1; untwisting recovers the cyclic result.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a Fourier transform, including a frequency permutation, as pointwise chirp phases around a cyclic convolution with the chirp.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's way to compute a Fourier transform of prime length s from one of power-of-two length t>s using Gaussian-weighted linear maps A and B₀ that are contractions.
- `permutation-cancellation`: Retained permutation cancellation: The coordinate permutations of resampling are kept in the transform formula; the source permutation cancels between the two forward transforms, the pointwise product and the opposite-sign transform, so no full sorts are executed.
- `crt-axis-map`: Chinese-remainder address map: An algebra isomorphism sending the radix-digit coefficient list onto a product of pairwise coprime cyclic axes while preserving convolution, implemented by triangular controlled shifts and axis reorderings.
- `tensor-source-transform`: Source transform on the padded box: The approximate source Fourier transform formed by linewise Gaussian maps A, the chirp convolution of length T on the padded power-of-two box, linewise B₀ and an exact 2^γ scale, equal to R F_s on the prime-length source.
- `parameter-regime`: Parameter regime for the multiplier: The choice of precision p=6b, dimension d≈p^ε, record length r=2^Θ(p^(1−ε)), power-of-two axis lengths t_i and distinct prime source lengths s_i just below them, so that Tp=Θ(n) and all hypotheses hold.
- `precision-exact-recovery`: Precision and exact recovery: Disk-margin and error bounds showing the recovered convolution coefficients are within error below 1/2 of integers below 2^{3b}, so rounding and carry propagation give the exact product.
- `multiplication-algorithm`: The multiplication algorithm: Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.
- `cost-accounting`: Cost accounting and the exponent κ: Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).
- `main-theorem`: Integer multiplication below n log n: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, disproving the n log n optimality conjecture in this model.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "KnownConcept": {
      "additionalProperties": false,
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations for it, in the sources or in standard texts.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what it is.",
          "type": "string"
        },
        "name": {
          "description": "Display name in plain text, e.g. \"Fourier series\".",
          "type": "string"
        }
      },
      "required": [
        "name",
        "aliases",
        "gloss"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "known": {
      "description": "Concepts the reader knows that the sources rely on and no existing concept covers.",
      "items": {
        "$ref": "#/$defs/KnownConcept"
      },
      "type": "array"
    },
    "summary": {
      "description": "Two to four sentences: the subjects this reader has studied that bear on the sources,\nand how far into each.",
      "type": "string"
    }
  },
  "required": [
    "summary",
    "known"
  ],
  "title": "BackgroundAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0002-background.answer.json`, then run `exegenius submit 0002-background` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
