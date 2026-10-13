# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/G3` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds such as O(n log n) on running time.
- `polynomials`: Polynomials (known to the reader): Expressions Σ aₖ yᵏ with coefficients, added and multiplied coefficientwise with exponent addition.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including roots of unity e^{2πik/q} of modulus one.
- `turing-machine`: Multitape Turing machine (known to the reader): A machine with a finite alphabet and several one-dimensional tapes, each step reading and writing one cell per tape and moving each head by at most one cell.
- `mult-history`: History of fast multiplication and the n log n conjecture: Schönhage–Strassen (1971) multiplied n-bit integers in O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Fürer and later work reduced the extra factor, and Harvey and van der Hoeven reached O(n log n).
- `radix-convolution`: Integer product as digit-polynomial convolution: Writing each n-bit input in radix 2^b gives digit polynomials whose ordinary product has coefficients below 2^{3b}, so the integer product is the convolution of the digit lists followed by carry propagation.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The normalized length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q} turns cyclic convolution into pointwise multiplication, and its opposite-sign transform inverts it up to scale.
- `multidim-transform`: Multidimensional transforms on product axes: A transform on an array indexed by a product of axes, defined as the tensor product of one-dimensional transforms and computed one axis (coordinate line) at a time.
- `modular-crt`: Modular arithmetic and the Chinese remainder theorem: Residues modulo pairwise coprime moduli determine a number modulo their product, so a cyclic index of length s₁⋯s_d splits into independent coordinates modulo each sᵢ.
- `crt-prime-axes`: Chinese-remainder address map to prime axes: A ring isomorphism sending x to ∏ xᵢ^{μᵢ} that places a length-S cyclic coefficient list on a product of cyclic axes of pairwise coprime (prime) lengths while preserving convolution; the induced address change is a sequence of triangular controlled shifts.
- `fixed-point-grid`: Fixed-point complex numbers on a disk grid: Complex values with real and imaginary parts that are integer multiples of 2^{−p} inside the unit disk, stored as two signed two's-complement words, with truncation toward zero to the grid.
- `contraction-error`: Contractions and error accumulation: A linear map that never increases the maximum coordinate modulus is a contraction, so approximation errors of composed steps add and every normalized transform keeps values inside the unit disk.
- `gaussian-resampling`: Gaussian resampling with permutations retained: An identity P_s F_s = 2^{2α²} B₀ P_t F_t A (tensored over axes) expressing a Fourier transform of prime-related length s through a transform of power-of-two length t using Gaussian-weighted contractions A and B₀, with the coordinate permutations kept inside the formula.
- `chirp-identity`: Bluestein chirp identity: Multiplying by a quadratic-phase chirp before and after a cyclic convolution with the chirp reproduces the permuted Fourier transform Q F_t, so a transform becomes a convolution.
- `permutation-cancel`: Source permutation cancellation: The coordinate permutation R retained in the source transform cancels across the two forward transforms, their pointwise product and the opposite-sign transform, so the product is exactly u*v/S².
- `negacyclic-ring`: Negacyclic ring ℂ[y]/(yʳ + 1): The ring of complex polynomials of degree below r taken modulo yʳ + 1, in which multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms F_t^± over the negacyclic ring using the roots ω_t = y^{2r/t}, so multiplication by a root is a free signed shift; their character sums cancel to give F⁺F⁻ = I/t.
- `butterfly-order`: Radix-2 butterflies and stored frequency order: The decimation-in-frequency recursion applies the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle shift at each level, writing outputs in bit-reversed order that the opposite transform consumes directly.
- `phase-twist`: Phase twist from cyclic to negacyclic wrap: Multiplying coefficient k of the last cyclic axis by e^{πik/r} makes a length-r cyclic coordinate a polynomial modulo yʳ + 1, and the negative wrap becomes the correct cyclic wrap after untwisting.
- `stream-scans`: Elementary stream scans on tapes: Splitting, merging, digit moves and row-wise stream splitting on a lexicographically stored array cost O(V) steps for volume V on a fixed number of tapes, with counters and head returns included.
- `controlled-shifts`: Controlled cyclic shifts of an address field: Updating a target field y mod q^b by an offset computed from earlier control fields, or multiplying it by a unit, costs O(V) on tape by splitting each fiber at the offset and merging the pieces swapped.
- `signed-packing`: Signed packing of polynomial products: A Kronecker-substitution reduction that evaluates polynomials at 2^{4p}, multiplies the resulting integers with the established O(N log N) multiplier, and extracts signed coefficients to get exact products in the negacyclic ring.
- `linear-spaces`: Subspaces, orthogonal complements and bilinear forms: Linear subspaces of a vector space with a nondegenerate bilinear form, their orthogonal complements, projections and dimensions, used to label network vertices.
- `matrix-shear`: Matrix shears and triangular factorization: The address map (H,D) → (H+AD,D) for a rational matrix A of rank a is done with exactly a field interchanges plus linear-cost triangular updates, using the factorization A = E₁ΠE₂ with E₁,E₂ lower triangular.
- `common-frame`: Frames and pointwise gates: Giving every wire at a gate the same invertible linear operator on its address-indexed array lets the pointwise linear gate commute with it, so only endpoint frames determine the net operator and edges change frames cheaply.
- `scratch-network`: Scratch-restoring bank-exchange network: A fixed network of pointwise linear gates built from copy, gather, scatter and side wires over three-element subsets that exchanges two data banks in three stages and returns every auxiliary scratch wire to its arbitrary initial value.
- `subspace-labels`: Nested subspace labels and the rank saving: Subspaces of an m-dimensional space attached to gates and terminals, nested along edges, so that the sum of edge ranks s is strictly less than the wire count W times m.
- `rank-saving-recurrence`: Recursion with a strict rank saving: Each call at parameter mf makes s calls at parameter f on streams of volume V/W, so the normalized cost obeys F_k ≤ (s/W)F_{k−1} + O(1) and, because s/W < m, grows like m^{kτ} with τ < 1.
- `address-interchange`: Fast address chunk interchange: Two disjoint equal-width address chunks of u bits are exchanged in O(V u^τ) time for a fixed τ < 1 by computing XOR combinations of intermediate streams through the bit network, even though the net effect is an exact permutation.
- `phase-frames`: Phase frames and the two-point kernel C: Over binary labels the frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} turn each edge into a product of translation kernels aI + bX_v built from C = H S H, with H₀ = b S C S.
- `packed-bit-addition`: Packed addition on selected address bits: A binary row addition y_j ← y_j ⊕ x_j on the same bit position of several address chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set.
- `butterfly-layer`: Fast simultaneous butterfly layer: The two-point butterfly H₀ applied at once to one bit position of each of up to d address chunks of polynomial records costs O(V d^λ′) with λ′ < 1, evaluated exactly in Gaussian dyadics and truncated once.
- `transform-layout`: Tape layout for synthetic transforms: A positional permutation of record addresses puts the selected bits of all participating axes at a common offset in consecutive K-bit chunks, so each transform round is one simultaneous butterfly layer.
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms keep their common stored frequency order, the ring records are multiplied pointwise by signed packing, and the opposite transform consumes that order to give normalized convolution over the negacyclic ring.
- `parameter-choice`: Parameter choices and prime source lengths: The padded box size T, precision p = 6b, number of axes d, chunk width K, ring size r and distinct odd primes sᵢ just below the power-of-two axis lengths tᵢ are chosen so the resampling and layer hypotheses hold.
- `exact-recovery`: Exact recovery by rounding and carries: Because the accumulated numerical error on every recovered coefficient is below 1/2, rounding gives the exact integer convolution coefficients, and radix-2^b carry propagation yields the 2n-bit product.
- `cost-table`: Cost accounting and the exponent κ: Dividing every step's cost by the volume Tp gives seven dominant powers of p, each at most 1 − 2κ, which with κ = 2^{−182} yields total time O(n (lg n)^{1−κ}).
- `multiplication-algorithm`: The multiplication algorithm: Convert inputs to radix-2^b digit lists, map them by the Chinese-remainder address map, apply the resampled chirp source transform to each, multiply pointwise, apply the opposite transform, rescale, round, undo the address map and propagate carries.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

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
