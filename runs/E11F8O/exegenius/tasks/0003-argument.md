# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E11F8O` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

## Pages, in reading order

- `n-log-n-barrier`: The n log n barrier: The Schönhage–Strassen conjecture that n log n is the optimal multiplication cost on multitape Turing machines, and the Harvey–van der Hoeven O(n log n) multiplier, which is used here only as a subroutine on short inputs.
- `convolution`: Convolution: The cyclic convolution of two coefficient lists, equal to the product of the corresponding polynomials modulo x^S − 1.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree less than r with y^r=−1, in which powers of y are roots of unity and multiplication by y^a is a signed shift of the coefficient list.
- `coefficient-twist`: Cyclic-to-negacyclic coefficient twist: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution on the last axis to convolution modulo y^r+1; untwisting recovers the cyclic result.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying two polynomials with small signed integer coefficients by evaluating them at a large power of two, multiplying the resulting integers with the O(n log n) multiplier, and extracting coefficients with centered carries.
- `tape-address-model`: Arrays as address fields on tape: An array indexed by a product of ranges is stored in lexicographic order; its logical volume V is the number of data bits, and elementary field moves, digit permutations and row splits cost O(V).
- `controlled-cyclic-shift`: Controlled cyclic shift: Adding to a target address field an offset computed from earlier control fields, modulo a range, in O(V) time by splitting and re-merging blocks.
- `scratch-restoring-exchange`: Scratch-restoring bank exchange: A fixed linear network of copy, gather, scatter and side-injection gates that swaps two banks of values in three stages while returning every auxiliary (scratch) wire to its arbitrary initial value.
- `array-frames`: Frames: changing representation along a network: Replacing each scalar wire by an array and storing it as D_v g for an invertible operator D_v (a frame), so that a pointwise linear gate commutes with the frame and only the endpoint operator remains.
- `rank-and-orthogonal-subspaces`: Subspaces, rank and orthogonal complements: Matrix rank, subspaces with a bilinear form, nondegenerate subspaces, orthogonal complements and orthonormal bases, as used to label a network.
- `subset-intersection-labels`: Triple-subset labels and the rank budget: Subspaces of a fixed space attached to gates and terminals, built from indicator vectors of three-element subsets so that adjacent labels are nested and the total edge rank s is strictly less than the wire count W times the dimension m.
- `address-shear-factorization`: Address shear and triangular factorization: The address map (H,D)↦(H+AD,D) for a rational matrix A of rank a, performed with exactly a interchanges of smaller field pairs after factoring A=E₁ΠE₂ into lower-triangular factors and a partial permutation.
- `rank-saving-recurrence`: Recursive rank saving: Splitting rows among the W network roles makes each recursive call a 1/W-volume stream, so the cost per volume grows by s/W<m when the parameter is multiplied by m, giving a power saving.
- `power-width-interchange`: Power-width chunk interchange: Interchanging two chunks of e=m^k digits in time O(V e^τ) by running the bit network on W role streams, with each edge shear implemented recursively by smaller interchanges.
- `address-chunk-interchange`: Address chunk interchange: Interchanging two disjoint contiguous address fields of u bits of an array in O(V u^τ) time for a fixed τ<1, using XOR combinations of intermediate data although the final effect is an exact permutation.
- `crt-axis-map`: Chinese-remainder address map: An algebra isomorphism sending the radix-digit coefficient list onto a product of pairwise coprime cyclic axes while preserving convolution, implemented by triangular controlled shifts and axis reorderings.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of many chunks at once by a constant number of whole-chunk cyclic shifts that are correct away from a small set of guard-violating addresses, which are then repaired deterministically by sorting.
- `fixed-point-complex-arithmetic`: Fixed-point complex grid and truncation: Complex numbers stored as signed two's-complement numerators over 2^p, in the unit disk, with truncation toward zero to the grid after exact dyadic arithmetic.
- `phase-frame-network`: Complex phase network: The second network over Gaussian dyadics with binary labels, whose frames are built from the two-point kernel C=HSH=aI+bX, so each edge is a product of translation kernels and the endpoint operator is C^{⊗m} on every role.
- `discrete-fourier-transform`: Discrete Fourier transform: The normalized transform F_q that averages inputs weighted by roots of unity; it turns convolution into pointwise multiplication.
- `fft-butterflies`: Fast Fourier transform with butterflies: Computing a length-2^a transform in a levels, each pairing entries by a two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) followed by a twiddle multiplication.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A Fourier-type transform over the negacyclic ring whose roots of unity ω_t=y^{2r/t} are signed coefficient shifts, so each twiddle multiplication is free of real arithmetic.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a Fourier transform, including a frequency permutation, as pointwise chirp phases around a cyclic convolution with the chirp.
- `stored-frequency-order`: Retained frequency order: The forward transform writes outputs in bit-reversed order; the pointwise product and the opposite transform both use this order, so no permutation is ever executed.
- `transform-tape-layout`: Transform layout on tape: Placing the selected bit of each participating axis at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so that each transform round is one simultaneous butterfly layer.
- `contraction-error-propagation`: Contractions and error accounting: Linear maps that do not increase the maximum-modulus norm; composing approximations adds their errors, which is how the accumulated numerical error is bounded.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's way to compute a Fourier transform of prime length s from one of power-of-two length t>s using Gaussian-weighted linear maps A and B₀ that are contractions.
- `permutation-cancellation`: Retained permutation cancellation: The coordinate permutations of resampling are kept in the transform formula; the source permutation cancels between the two forward transforms, the pointwise product and the opposite-sign transform, so no full sorts are executed.
- `normalized-ring-convolution`: Normalized convolution over the polynomial ring: Convolving arrays of ring elements by two forward synthetic transforms, a pointwise polynomial product divided by r, and the opposite transform, giving (f*g)/T with a bounded error.
- `parameter-regime`: Parameter regime for the multiplier: The choice of precision p=6b, dimension d≈p^ε, record length r=2^Θ(p^(1−ε)), power-of-two axis lengths t_i and distinct prime source lengths s_i just below them, so that Tp=Θ(n) and all hypotheses hold.
- `radix-digit-reduction`: Radix-digit convolution: Writing each n-bit integer as a polynomial in 2^b with b-bit digits, so the integer product is the digit convolution followed by carry propagation.
- `tensor-source-transform`: Source transform on the padded box: The approximate source Fourier transform formed by linewise Gaussian maps A, the chirp convolution of length T on the padded power-of-two box, linewise B₀ and an exact 2^γ scale, equal to R F_s on the prime-length source.
- `precision-exact-recovery`: Precision and exact recovery: Disk-margin and error bounds showing the recovered convolution coefficients are within error below 1/2 of integers below 2^{3b}, so rounding and carry propagation give the exact product.
- `multiplication-algorithm`: The multiplication algorithm: Digit conversion, the CRT map Φ, two forward source transforms, a pointwise product, one opposite transform, two scalings by S, rounding, inverse Φ and carry propagation to output the 2n-bit product.
- `cost-accounting`: Cost accounting and the exponent κ: Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).
- `main-theorem`: Integer multiplication below n log n: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `binary-numerals-and-bit-strings`: Binary numerals and bit strings
- `positional-notation-in-any-radix`: Positional notation in any radix
- `integer-division-with-remainder-floor-and-ceiling`: Integer division with remainder, floor and ceiling
- `modular-arithmetic`: Modular arithmetic
- `arithmetic-modulo-2-and-xor`: Arithmetic modulo 2 and XOR
- `primes-coprimality-and-gcd`: Primes, coprimality and gcd
- `roots-of-unity-and-euler-s-formula`: Roots of unity and Euler's formula
- `exponential-logarithm-and-gaussian-function`: Exponential, logarithm and Gaussian function
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `geometric-series-and-sums`: Geometric series and sums
- `divide-and-conquer-and-recurrences`: Divide and conquer and recurrences
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `sorting-and-its-cost`: Sorting and its cost
- `permutations-and-bijections`: Permutations and bijections
- `sets-subsets-and-cartesian-products`: Sets, subsets and Cartesian products
- `multidimensional-arrays-and-row-major-order`: Multidimensional arrays and row-major order
- `matrices-vectors-and-linear-maps`: Matrices, vectors and linear maps
- `triangular-and-permutation-matrices`: Triangular and permutation matrices
- `dot-product-inner-product-and-orthogonality`: Dot product, inner product and orthogonality
- `dyadic-rationals-and-fixed-width-numerators`: Dyadic rationals and fixed-width numerators
- `matrix-transposition`: Matrix transposition
- `triangle-inequality-and-norms`: Triangle inequality and norms
- `mathematical-induction-and-proof-by-contradiction`: Mathematical induction and proof by contradiction
- `cyclic-shifts-and-rotations-of-lists`: Cyclic shifts and rotations of lists
- `subroutines-and-composition-of-algorithms`: Subroutines and composition of algorithms

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
