# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N2` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Omega, Theta), divide-and-conquer recurrences and standard algorithms including Karatsuba multiplication and the radix-two FFT for polynomial multiplication, and basic models of computation including multitape Turing machines. From discrete mathematics they know induction, sets and binomial coefficients, binary and two's-complement representation, primes, gcd, modular arithmetic and the Chinese remainder theorem. From a first linear algebra course they know vector spaces, bases, subspaces, matrices, invertibility, Gaussian elimination, permutation and diagonal matrices and projections, and from calculus the exponential and logarithm, geometric series, Newton's method and elementary error bounds such as the triangle inequality. They have not studied Fourier analysis beyond the FFT, abstract algebra beyond modular arithmetic, numerical analysis of fixed-point transforms, or research-level integer multiplication techniques such as Schönhage–Strassen, Nussbaumer transforms or Gaussian resampling.

## Pages, in reading order

- `negacyclic-ring`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree below r modulo yʳ + 1, in which powers of y are roots of unity and multiplying by one is a signed shift of the coefficient list.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the basic step of radix-two transforms, applied coefficientwise to polynomial records.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are fractions with power-of-two denominators, i.e. the ring ℤ[i,1/2], on which the networks compute exactly.
- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, here read as an eventual Ω(n lg n) lower bound for every fixed multitape machine.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The previously established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine and as the source of the Gaussian-resampling method.
- `tape-array-layout`: Arrays as address-ordered tape streams: An array over a product of address fields is stored on tape in lexicographic order with addresses implicit, and its logical volume V is its number of stored data bits.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape procedures that permute or move single radix digits of addresses, split and merge streams by a digit, and split whole rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts and rational scalings: In linear time a tape machine can add to an address field an offset computed from earlier fields, modulo its range, or multiply that field by a fixed rational unit.
- `binary-field-xor`: The field F₂ and XOR: The two-element field F₂, in which addition is XOR of bits, so that vectors of bits form spaces over F₂.
- `linear-algebra-rank`: Matrices, linear maps and rank: A matrix represents a linear map between coordinate spaces, and its rank is the dimension of its image.
- `linear-network`: Linear networks, wires and roles: A fixed finite network of wires carrying scalars, acted on by pointwise linear gates; a wire's fixed place in the network is its role.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible operator (its frame) describing how the stored array represents the logical one; since a common frame commutes with a pointwise gate, the whole network implements D_out·S·D_in⁻¹ and intermediate frames cancel.
- `address-shear`: Address shear: The array permutation Φ_M moving the entry at address (H,D) to (H+MD,D) for two vectors H, D of address fields and a matrix M; shears compose additively.
- `scratch-restoration`: Restoring arbitrary scratch values: A schedule that subtracts the effect of the old auxiliary values, adds the source effect, and undoes the auxiliary updates, so the net effect is independent of arbitrary initial scratch contents.
- `subset-construction`: Three-element subset construction: Gates indexed by 3-subsets of a 100-element set: gather and scatter through central wires give coefficients depending on intersection size, and side wires between neighbouring subsets cancel the unwanted ones, so a forward invocation adds x to y.
- `bank-exchange`: Three-stage bank exchange: Applying forward, inverse and forward invocations along the three tensor coordinates sends the two data banks (X,Y) to (−Y,X) while restoring every auxiliary wire.
- `bilinear-forms`: Symmetric bilinear forms and orthogonal complements: A symmetric bilinear form pairs vectors to scalars; it defines orthogonality, orthogonal complements and nondegenerate subspaces.
- `tensor-products`: Tensor products: The tensor product combines vector spaces or operators so that an operator on several coordinates acts factorwise on each.
- `subspace-labels`: Subspace labels and orthogonal residuals: Each gate and terminal is labelled by a nondegenerate subspace of a fixed m-dimensional bilinear space, adjacent labels are nested, and the dimension of the orthogonal residual on an edge counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit s < Wm: The decisive property of each finite network: the total number s of smaller calls needed on its edges is strictly less than the number of wires W times the label dimension m.
- `volume-normalized-recurrence`: Volume-normalized recursion: Dividing cost by data volume, a call at parameter mf makes s calls at parameter f each on volume V/W, so the normalized cost grows by s/W < m per factor m, giving cost O(V·f^τ) with τ < 1.
- `bit-network-interface`: Rational matrix interface of the bit network: Assigning projection matrices onto the labels as shear frames makes the XOR bit network apply the shear H ← H + D on every role, with total edge rank s_b < W_b·m.
- `motif-exponents`: Explicit exponents τ and σ: The fixed rational exponents τ = σ = 1 − 2⁻⁵⁰ for the address and butterfly recurrences, justified because both relative rank deficits exceed 20·2⁻⁵⁰.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H,D) ↦ (H+AD,D) by a fixed rational matrix of rank a costs exactly a interchanges of smaller field pairs plus linear work, using the triangular factorization and controlled shifts.
- `power-width-interchange`: Power-width chunk interchange: For chunks of e = mᵏ digits with enough rows, splitting rows among the W roles and running the bit network with recursive shears interchanges the chunks in O(V e^τ) time on fixed tapes via a depth-first schedule.
- `chunk-interchange`: Fast address chunk interchange: A fixed tape procedure interchanging two disjoint u-bit address chunks of an array in O(V u^τ) time with τ < 1, by forming XOR combinations of data rather than moving it directly.
- `phase-kernel-c`: Two-point kernel C: The Gaussian dyadic kernel C = H·diag(1,i)·H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying H₀ = b·S·C·S, so layers of C convert into normalized butterfly layers.
- `phase-frames`: Binary phase frames: For a binary label U, the frame C_U = H^⊗m · diag(i^{q_U(x)}) · H^⊗m with q_U(x) the Hamming weight of the projection of x mod 4; between nested labels it changes by one translation kernel aI + bX_v per orthonormal residual vector.
- `binary-phase-interface`: Binary phase interface of the complex network: With phase frames on the complex network, s_c translation kernels in total suffice, and after endpoint diagonal corrections and undoing the bank exchange the network applies C^⊗m on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing bit x into bit y at regularly spaced positions of two address chunks via eight cyclic shifts using a third guard chunk, then deterministically repairing the small explicitly identified set of exceptional addresses.
- `layer-recursion`: Batched recursion for a common layer: Applying C on e = mf selected axes by splitting them into m slots, changing basis with packed row additions, splitting rows among the W roles and recursing s times on volume V/W each.
- `guard-width`: Guard width for exact layer evaluation: An explicit bound on denominator and magnitude growth inside one accelerated layer, giving a coefficient width of O(p) bits so all intermediate Gaussian dyadic values are exact.
- `fixed-point-grid`: Disk grid values and truncation: Complex values in the unit disk with coordinates in 2⁻ᵖℤ, stored as fixed-width two's-complement words, with truncation Q_p and an error notion that adds along compositions of contractions.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position of up to d address chunks at once, exactly in Gaussian dyadics followed by one truncation, in O(V d^λ′) time with λ′ < 1 instead of d separate passes.
- `signed-packing`: Signed coefficient packing: A signed Kronecker substitution packing polynomial coefficients into one integer so the O(n log n) multiplier computes exact products in ℂ[y]/(yʳ+1).
- `cyclic-convolution`: Cyclic convolution: The convolution of two sequences indexed modulo a length, equivalently the product of polynomials modulo xᴸ − 1, possibly over several axes.
- `multiplication-as-convolution`: Integer multiplication as digit convolution: Writing each integer in radix 2ᵇ makes its product the convolution of the digit sequences, followed by carry propagation.
- `coefficient-twist`: Coefficient twist: The map x ↦ ζy with ζ = e^{πi/r}, which turns a length-r cyclic coordinate into the negacyclic ring ℂ[y]/(yʳ+1) by scaling coefficient k by ζᵏ, preserving convolution.
- `dft`: Discrete Fourier transform: The linear map taking a length-q vector to its averages against the powers of a q-th root of unity; it turns cyclic convolution into pointwise multiplication.
- `multidimensional-dft`: Multidimensional Fourier transforms: The tensor product of one-dimensional discrete Fourier transforms along each axis of a multidimensional array.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer's normalized Fourier transforms over ℂ[y]/(yʳ+1) using ω_t = y^{2r/t} as root of unity, so they need only signed shifts and butterflies.
- `bluestein-chirp`: Bluestein chirp identity: Writing a Fourier transform, including its target permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `transform-layout`: Transform layout and stored frequency order: A tape layout placing the selected bits of participating axes at a common offset in consecutive K-bit chunks so simultaneous layers apply, with the frequency order retained for the opposite transform.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing the normalized cyclic convolution of arrays over ℂ[y]/(yʳ+1) by two forward synthetic transforms, pointwise packed products, and the opposite transform reading the retained frequency order.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of length s through one of a nearby length t via Gaussian-weighted contractions, here with the source and target coordinate permutations kept in the formula instead of sorted.
- `tensor-resampling`: Tensor resampling interface: The tensor product of the one-dimensional resampling identities, RF_s = 2^γ B₀ Q F_t A, applied one coordinate line at a time with chunk interchanges moving axis fields.
- `permutation-cancellation`: Source permutation cancellation: The retained source permutation R cancels across the two forward transforms, their pointwise product and the opposite-sign transform, giving (u∗v)/S² without a separate sort.
- `parameter-choice`: Fixed rational parameter choice: The conservative constants τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, c = 2⁻⁵⁶, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², and sizes p = 6⌈log₂ n⌉, d = ⌊b^ε⌋, K = ⌊d^c⌋ that satisfy all layer and cost conditions.
- `crt-map`: Chinese-remainder address map: The Agarwal–Cooley isomorphism turning a cyclic convolution of length S = ∏sᵢ into a multidimensional cyclic convolution on pairwise coprime axes, implemented on tape by triangular controlled shifts.
- `multiplication-algorithm`: The multiplication algorithm: Split the inputs into radix-2ᵇ digits, map them by the CRT map, compute two forward resampled source transforms, multiply pointwise, apply the inverse transform, rescale, round and propagate carries.
- `exact-recovery`: Precision and exact recovery: Error bookkeeping showing every call stays in the disk and the recovered coefficients have error below 1/2, so rounding gives the exact integer convolution.
- `time-bound`: Complete time bound: The cost table, normalized by V = Tp = Θ(n), whose every dominant term is a power of p at most 1 − 2κ, giving total time O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machines`: Multitape Turing machines
- `modular-arithmetic`: Modular arithmetic
- `big-omega-and-big-theta-notation`: Big-Omega and Big-Theta notation
- `worst-case-running-time`: Worst-case running time
- `logarithms-floor-and-ceiling`: Logarithms, floor and ceiling
- `exponential-function`: Exponential function
- `euler-s-formula-and-complex-roots-of-unity`: Euler's formula and complex roots of unity
- `binary-representation-of-integers`: Binary representation of integers
- `two-s-complement`: Two's complement
- `fixed-point-numbers-and-rounding`: Fixed-point numbers and rounding
- `integer-division-with-remainder`: Integer division with remainder
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `modular-inverses-and-units`: Modular inverses and units
- `chinese-remainder-theorem`: Chinese remainder theorem
- `fast-fourier-transform`: Fast Fourier transform
- `polynomial-evaluation-and-interpolation`: Polynomial evaluation and interpolation
- `karatsuba-multiplication`: Karatsuba multiplication
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `geometric-series`: Geometric series
- `mathematical-induction`: Mathematical induction
- `sets-cartesian-products-and-lexicographic-order`: Sets, Cartesian products and lexicographic order
- `subsets-and-binomial-coefficients`: Subsets and binomial coefficients
- `permutations`: Permutations
- `hamming-weight`: Hamming weight
- `vector-spaces-subspaces-bases-and-dimension`: Vector spaces, subspaces, bases and dimension
- `invertible-matrices-and-the-general-linear-group`: Invertible matrices and the general linear group
- `gaussian-elimination`: Gaussian elimination
- `diagonal-matrices-and-pointwise-products`: Diagonal matrices and pointwise products
- `linear-projections`: Linear projections
- `matrix-transpose`: Matrix transpose
- `maximum-norm-and-triangle-inequality`: Maximum norm and triangle inequality
- `newton-s-method`: Newton's method
- `depth-first-traversal`: Depth-first traversal

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
