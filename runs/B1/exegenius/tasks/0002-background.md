# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1, including roots of unity.
- `turing-tapes`: Turing machines and tapes (known to the reader): Basic Turing machines with tapes, heads and finite alphabets.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; cost is the number of steps.
- `nlogn-conjecture`: Schönhage–Strassen n log n optimality conjecture: Schönhage and Strassen proposed n log n as optimal growth for multiplying n-bit integers on multitape machines; Harvey–van der Hoeven reached O(n log n).
- `convolution-reduction`: Multiplication as convolution of digit lists: Splitting inputs into radix digits turns integer multiplication into convolution of short integer coefficient lists, with carries propagated afterwards.
- `fourier-transform`: Discrete Fourier transform: Evaluation of a sequence at powers of a root of unity; it turns cyclic convolution into pointwise product.
- `multidim-transform`: Multidimensional transform: A Fourier transform on an array with several axes, applied along each axis in turn; here axis lengths are powers of two.
- `polyring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced modulo y^r+1, so y^r=-1; coefficients stored as a list, with r a power of two.
- `synthetic-transform`: Synthetic polynomial transform: Fourier transform over the polynomial ring where powers of y act as roots of unity, so multiplying by a root is a signed shift of the coefficient list (Nussbaumer).
- `butterfly`: Two-point butterfly H₀: The map (u,v) → ((u+v)/2, (u−v)/2), the basic arithmetic step of a transform layer, applied coefficientwise.
- `chinese-remainder-map`: Chinese-remainder address map onto prime axes: Places the digit coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing each prime-length Fourier transform through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform (with its permutation) into a normalized cyclic convolution via multiplication by chirp phases.
- `signed-packing`: Signed packing (Kronecker substitution): Encodes polynomial coefficients, with signs, into one long integer so ring products are computed by one integer multiplication.
- `hvdh-subroutine`: Established O(n log n) multiplier as subroutine: The Harvey–van der Hoeven O(n log n) multiplication used as an ordinary subroutine for polynomial products, not recursively invoking the new theorem.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network of gates exchanging banks of values with signs, restoring auxiliary values; each wire is a role and each gate has an invertible frame so intermediate frames cancel.
- `subset-network`: Three-element-subset finite networks: Finite networks built from three-element subsets with nested subspaces at gates; gather/scatter and auxiliary wires cancel unwanted coefficients, giving s<Wm smaller calls.
- `scalar-motif-network`: Scratch-restoring exchange network: Eight-row schedule of copy, gather, scatter and side-injection gates adding x_S to y_S for arbitrary initial scratch values; three stages give the exchange (X,Y) → (−Y,X).
- `recursive-saving`: Recursive power saving: Recursing at parameter mf with s calls of parameter f on volume V/W adds s/W<m per level, a strict inequality that gives a power saving.
- `controlled-shifts`: Elementary scans and controlled shifts: Linear-time tape operations: digit moves, splitting rows cyclically into streams, and updating a target field by an offset computed from earlier control fields.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones, so it can be applied in tape order.
- `matrix-shear`: Rational matrix shear of address fields: The frame Φ_M moving the entry at address (H,D) to (H+MD,D); a shear of rank a costs a smaller interchanges.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint address fields of u bits via pointwise XOR combinations that end as an exact permutation, in O(V u^τ) with τ<1.
- `phase-frames`: Phase frames for the butterfly layer: Using C=HSH=aI+bX with C²=X and H₀=bSCS, a tensor product of butterflies is expressed through smaller groups of selected bits separated by binary changes of basis.
- `fast-butterfly-layer`: Simultaneous butterfly layers: Applies H₀ at the same bit position of up to d address chunks at once on complex fixed-point records, in O(V d^λ′) with λ′<1.
- `synthetic-character-cancellation`: Synthetic character cancellation: In the ring modulo y^r+1, sums of powers of the root ω_t vanish unless t divides the exponent, so forward and opposite transforms invert each other up to 1/t.
- `transform-layout`: Retained frequency order and transform layout: Selected bits of the participating axes are placed at a common offset in K-bit chunks so the simultaneous layers apply, and the frequency order is retained through the pointwise product.
- `normalized-convolution`: Normalized convolution over the ring: Convolution over the polynomial ring computed as two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, normalized by 1/(rM).
- `resampling-lemma`: Resampling without executing permutations: Gaussian resampling identity P_sF_s = 2^{2α²}B₀P_tF_tA relating a length-s transform to a power-of-two-shape transform, with the two coordinate permutations kept inside the formula.
- `tensor-resampling`: Tensor interface for growing dimension: Applies the one-dimensional resampling maps line by line along d axes, using chunk swaps to move axes, giving R F_s = 2^γ B₀ Q F_t A.
- `chirp-permutation-cancellation`: Chirp and permutation cancellation: Chirp identity Q F_t u = ā·(a*(ā·u))/T computes the permuted middle transform as a convolution, and the source permutation R cancels across forward transforms, product and opposite transform.
- `exact-recovery`: Fixed-point precision and exact recovery: Intermediate values are exact Gaussian dyadics truncated once; the recovered coefficient error is below 1/2 so rounding and carry propagation give the exact product.
- `parameter-choice`: Fixed rational parameter choice: The fixed exponents (τ=σ=1−2⁻⁵⁰, λ′=1−2⁻⁵⁴, ε=2⁻⁷⁵, κ=2⁻¹⁸²) and size parameters p=6b, d=⌊b^ε⌋ making all costs fit the theorem.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.

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
