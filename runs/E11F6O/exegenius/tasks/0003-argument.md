# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E11F6O` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- The key step: the step the target result turns on, the construction or estimate that gives the result its strength (where a saving, a bound or a surprise comes from). A reader who follows only one derivation should follow this one. Develop it with `show` steps down to the reasoning the sources give for it, each sub-step quoting where the sources carry it out, rather than stopping at an `infer` step that quotes its result. Where a sub-step concludes from a count, a bound or an equality, state the identity, lemma or definition that makes it hold, and every case the sources treat as an exception to it. Where the sources carry out a construction or estimate in more than one variant, develop each variant the target result uses; where a sub-step concludes a bound on an error, a size or a depth, state the recurrence or chain of estimates that produces the bound. Define each parameter and constant the target result's statement or derivation fixes (a size, a count, a threshold) with the value the sources give it, at the step that first uses it; where the sources establish a sub-step case by case or by a table, give every case and what it contributes.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`multiplication-below-nlogn`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture, by combining fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis and recurrences, discrete mathematics (induction, sets, functions, permutations, logarithms, floor and ceiling, modular arithmetic, primes, gcd and the Euclidean algorithm), introductory linear algebra (matrices, invertibility, rank, Gaussian elimination, vectors and inner products), basic algorithms (grade-school multiplication, divide and conquer, number representations in binary, bitwise XOR) and the basics of Turing machines with several tapes. They have met complex numbers and polynomials, but not the FFT in depth, abstract algebra beyond basic rings or quotient constructions, number-theoretic results such as prime density, numerical error analysis, or any research on fast integer multiplication.

## Pages, in reading order

- `convolution-multiplication`: Integer multiplication as convolution of radix digits: Writing each integer as a polynomial in 2^b with small digit coefficients turns the product into a convolution of digit lists, with carries propagated afterwards.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = −1, so multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y serve as roots of unity.
- `hvdh-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short inputs.
- `multitape-streams`: Fixed-tape model and elementary stream scans: The fixed-alphabet, fixed-number-of-tapes machine model in which arrays are streams in lexicographic order, and splitting, merging, digit moves and row splits cost O(V) for volume V.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: Updating a target address field by an offset computed from earlier control fields (a cyclic rotation of blocks), or multiplying it by a unit modulo q^b, in O(V) time.
- `bank-exchange-network`: Linear network exchanging two banks with restored scratch wires: A fixed network of linear gates on wires (roles) that, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange X and Y up to sign while restoring all scratch wires whatever their initial values.
- `linear-algebra-spaces`: Subspaces, orthogonal complements and projections: Vector subspaces of a space with a nondegenerate bilinear form, orthogonal complements, orthogonal projections P_U and tensor products of such spaces.
- `frames-on-arrays`: Frames and the common-frame identity: Replacing scalars by arrays, each vertex of the network gets an invertible operator (frame) on its array; since pointwise linear gates commute with a common frame, the network implements D_out S D_in^(−1) and each edge only changes frame.
- `subspace-labels`: Nested subspace labels with a rank deficit: Nondegenerate subspaces built from three-element subsets are attached to gates and terminals so adjacent labels are nested; the orthogonal residual dimensions total fewer than W·m, which bounds the number of smaller calls.
- `recursive-power-saving`: Recursive power saving from s < Wm: A call at parameter m·f makes s calls at parameter f on streams of volume V/W, so normalized cost satisfies F_k ≤ (s/W)F_(k−1)+O(1) with s/W < m^τ, giving cost O(V e^τ) with τ < 1.
- `bit-shear-interface`: Rational matrix interface and address shear: Using frames Φ_M that move the entry at (H,D) to (H+MD,D), the bit network turns the exchange into the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
- `lower-triangular-factorization`: Lower-triangular (Bruhat) factorization: Every m×m rational matrix A of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones.
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) → (H+AD,D) over Z/q^b with A of rank a costs exactly a interchanges of b-digit fields plus O(V) work, by factoring A and using one swap per pivot.
- `power-width-interchange`: Power-width chunk interchange with rows: Interchanging two chunks of e = m^k digits by splitting rows into W role streams, running the bit network with shear edges implemented by smaller interchanges, then applying D←D−H, H←H+D, D←H−D; cost O(V e^τ).
- `chunk-interchange`: Fast interchange of address chunks: Interchanging two disjoint address fields of u bits in an array in O(V u^τ) time for a fixed τ < 1, although the intermediate steps XOR data together; arbitrary widths are handled by padding and a base-m decomposition.
- `phase-frames`: Phase frames and the two-point kernel C: With C = H S H = aI+bX (a=(1+i)/2, b=(1−i)/2) one has H₀^(⊗D) = b^D S_D C^(⊗D) S_D, and phase frames of binary labels make each network edge a product of translation kernels, one per residual basis vector.
- `packed-selected-bit-addition`: Packed changes of selected address bits: Adding (XOR) selected bits of one address chunk into another using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.
- `fixed-point-precision`: Fixed-point disk-grid arrays and truncation: Complex coefficients of modulus at most 1 stored with p fractional bits per component; truncation Q_p toward zero costs error below √2·2^(−p) and never increases the norm.
- `guard-bits`: Exact Gaussian dyadics and guard width: Intermediate values in a butterfly layer are exact Gaussian dyadics whose denominators and magnitudes grow by at most a bounded number of guard bits, so one truncation follows the completed layer.
- `signed-kronecker-packing`: Signed packing of polynomial products: Computing products of ring polynomials exactly by evaluating each at a large power of two (signed Kronecker substitution), multiplying the resulting integers with the established multiplier and unpacking the coefficients.
- `discrete-fourier-transform`: Normalized discrete Fourier transform and convolution theorem: The transform F_q averaging inputs times roots of unity e^(−2πijk/q) (with inverse-sign version F_q⁺), which turns cyclic convolution into pointwise products up to a normalization.
- `radix-two-fft`: Radix-two FFT butterflies: The decimation-in-frequency recursion that pairs entries k and k+t/2, applies the two-point butterfly H₀ = ½[[1,1],[1,−1]] and a twiddle multiplication, then recurses on both halves, leaving outputs in bit-reversed order.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring modulo y^r + 1 using ω_t = y^(2r/t) as root of unity, so twiddle multiplications are signed coefficient shifts; their forward and opposite versions invert each other up to 1/t.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀(u,v) = ((u+v)/2,(u−v)/2) to the same bit position in d address chunks at once, on polynomial records, in O(V d^λ') time with λ' < 1 instead of d whole-array passes.
- `synthetic-transform-layout`: Synthetic transform layout on tape: A positional address permutation placing the selected bits of all participating axes at a common offset in consecutive K-bit chunks so that each FFT round is one simultaneous layer; total cost O(Tp[dK + pK^(τ−1) + ℓ d^λ']).
- `synthetic-convolution`: Convolution over the polynomial ring from retained frequency order: Convolving arrays over the ring by transforming both operands, multiplying pointwise in the retained stored frequency order, and applying the opposite transform, with error below √2·M(3ℓ+1)·2^(−p).
- `coefficient-twist`: Cyclic-to-negacyclic coefficient twist: Multiplying coefficient k of the last cyclic coordinate by ζ^k with ζ = e^(πi/r) maps cyclic convolution of length r to the ring modulo y^r + 1, so the ring convolution computes complex cyclic convolution.
- `gaussian-resampling`: Gaussian resampling without sorting: Rewrites the prime-length transform P_s F_s as 2^(2α²) B₀ P_t F_t A with contractions A, B₀ and power-of-two length t, keeping the two coordinate permutations inside the transform identity instead of sorting.
- `bluestein-chirp`: Bluestein chirp identity: Writes the permuted transform Q F_t as chirp multiplication, a cyclic convolution with the chirp array a, and chirp multiplication again, so the frequency permutation is never executed.
- `permutation-cancellation`: Cancellation of the retained source permutation: Because a coordinate permutation R commutes with pointwise products, applying R F_s to both operands and R F_s⁺ to their pointwise product yields (u*v)/S², so the source permutation never has to be undone.
- `tensor-resampling`: Tensor resampling on the padded box: Applying the one-dimensional resampling maps line by line along each of d axes of the zero-padded power-of-two box, exposing each axis with chunk interchanges, for error below d·p² and total line cost O(dTp^(3/2+δ)α).
- `crt-cyclic-convolution`: Chinese-remainder map to distinct prime cyclic axes: An algebra isomorphism sending x to the product of x_i^(μ_i) turns one cyclic convolution of length S = s₁…s_d into a d-dimensional cyclic convolution over pairwise coprime axes, implemented by triangular controlled shifts.
- `parameter-choice`: Size parameters and prime axis lengths: For input length n choose b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, a power-of-two T near 4n/b split into d axis lengths r/2 or r, and distinct odd primes s_i just below the t_i with T/2 < S < T.
- `multiplication-algorithm`: The multiplication algorithm: Split into radix digits, map by the CRT address map, apply the source transform (resampling, chirp convolution via ring convolution) to both operands, multiply pointwise, apply the opposite transform, undo scales, round and propagate carries.
- `exact-recovery`: Precision, rounding and carry recovery: Disk margins keep every intermediate array in the unit disk, accumulated approximation errors stay below 1/2 per coefficient so rounding returns exact integer product coefficients, and carry propagation gives the 2n-bit product.
- `time-bound-accounting`: Cost table and exponent margins: Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).
- `multiplication-below-nlogn`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture, by combining fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machines`: Turing machines and tapes
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-coprimality-and-gcd`: Primes, coprimality and gcd
- `euclidean-algorithm-and-modular-inverses`: Euclidean algorithm and modular inverses
- `trial-division-and-primality-search`: Trial division and primality search
- `binary-representation-bit-strings-and-xor`: Binary representation, bit strings and XOR
- `radix-representation-and-carry-propagation`: Radix representation and carry propagation
- `logarithms-floor-and-ceiling`: Logarithms, floor and ceiling
- `recurrences-and-induction`: Recurrences and induction
- `divide-and-conquer-multiplication`: Divide-and-conquer multiplication
- `permutations-and-bijections`: Permutations and bijections
- `matrices-invertibility-and-rank`: Matrices, invertibility and rank
- `gaussian-elimination`: Gaussian elimination
- `vector-spaces-bases-and-dimension`: Vector spaces, bases and dimension
- `cartesian-products-and-lexicographic-order`: Cartesian products and lexicographic order
- `rational-numbers-and-dyadic-fractions`: Rational numbers and dyadic fractions
- `norms-absolute-value-and-triangle-inequality`: Norms, absolute value and triangle inequality
- `euler-s-formula-and-roots-of-unity`: Euler's formula and roots of unity
- `rounding-and-square-roots`: Rounding and square roots
- `polynomial-time-and-computational-cost-on-tapes`: Polynomial time and computational cost on tapes
- `fast-fourier-transform-as-a-known-algorithm`: Fast Fourier transform as a known algorithm

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Binding": {
      "additionalProperties": false,
      "description": "What a symbol in a concept's name denotes.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the title's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation"
      ],
      "type": "object"
    },
    "Evidence": {
      "additionalProperties": false,
      "properties": {
        "quote": {
          "description": "Text copied character for character from that source.",
          "type": "string"
        },
        "source": {
          "description": "Id of the source the quote comes from.",
          "type": "string"
        }
      },
      "required": [
        "source",
        "quote"
      ],
      "type": "object"
    },
    "Intention": {
      "oneOf": [
        {
          "const": "show",
          "description": "Show a claim by a method that splits it into sub-steps.",
          "type": "string"
        },
        {
          "const": "infer",
          "description": "Infer one claim in a single step the sources report.",
          "type": "string"
        }
      ]
    },
    "Motivation": {
      "additionalProperties": false,
      "description": "Why a method suits the claim it shows.",
      "properties": {
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an explicit motivation, the sources' words, copied exactly."
        },
        "source": {
          "$ref": "#/$defs/Provenance",
          "description": "Whether the sources state the reason, leave it to be worked out, or neither."
        },
        "text": {
          "description": "The reason, in one or two sentences.",
          "type": "string"
        }
      },
      "required": [
        "text",
        "source"
      ],
      "type": "object"
    },
    "Node": {
      "additionalProperties": false,
      "description": "One step of the argument.",
      "properties": {
        "adds": {
          "description": "Symbols the step introduces, in force in its sub-steps.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "children": {
          "description": "For a show step: its sub-steps, in the order the method takes them.",
          "items": {
            "$ref": "#/$defs/Node"
          },
          "type": "array"
        },
        "claim": {
          "description": "What the step shows or infers, in one sentence, with mathematics in LaTeX ($...$).",
          "type": "string"
        },
        "deferred": {
          "description": "For an infer step the sources report out of order, before or after the steps around\nit.",
          "type": "boolean"
        },
        "from": {
          "default": [],
          "description": "Ids of the concepts the step relies on: known concepts, or pages before the step's\npage.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "id": {
          "description": "A short label, unique in the tree, such as \"S0\" or \"S2.1\".",
          "type": "string"
        },
        "intention": {
          "$ref": "#/$defs/Intention"
        },
        "method": {
          "description": "For a show step: how the claim is shown, in a phrase (\"reduce to a cyclic\nconvolution and bound its cost\").",
          "type": [
            "string",
            "null"
          ]
        },
        "motivation": {
          "anyOf": [
            {
              "$ref": "#/$defs/Motivation"
            },
            {
              "type": "null"
            }
          ],
          "description": "For a show step: why that method suits the claim."
        },
        "page": {
          "description": "Id of the page that presents this step and its sub-steps, if one does.",
          "type": [
            "string",
            "null"
          ]
        },
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an infer step: the step as the sources report it, copied exactly."
        },
        "salient": {
          "description": "For a step whose claim has a feature a reader would find striking (a symmetry, a\nuniformity across cases, a surprising value or bound): that feature. The page should\nexplain why it holds, from a matching feature of the method.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "intention",
        "claim"
      ],
      "type": "object"
    },
    "Provenance": {
      "oneOf": [
        {
          "const": "explicit",
          "description": "The sources state the reason; quote them.",
          "type": "string"
        },
        {
          "const": "recoverable",
          "description": "The sources do not state it, but a reader can work it out from what they say.",
          "type": "string"
        },
        {
          "const": "reconstructed",
          "description": "The sources neither state it nor make it recoverable: you supply it.",
          "type": "string"
        }
      ]
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
  "properties": {
    "root": {
      "$ref": "#/$defs/Node",
      "description": "The main step: to show the target result."
    }
  },
  "required": [
    "root"
  ],
  "title": "ArgumentAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0003-argument.answer.json`, then run `exegenius submit 0003-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0003-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
