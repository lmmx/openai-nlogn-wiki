# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7B` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model; the saving comes from faster address interchange and butterfly layers inside a Gaussian-resampling, Bluestein, synthetic-transform reduction.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, permutations, modular arithmetic, primes and gcd), calculus-level analysis (limits, sums, Newton's method), first-course linear algebra (matrices, inverses, Gaussian elimination, vectors) and complex numbers up to roots of unity, algorithm analysis (recursion, recurrences, big-O with its relatives Omega, Theta, little-o) and basic Turing machines. The reader knows binary representation and bitwise operations, and the textbook schoolbook multiplication. The reader has not studied abstract algebra beyond what the existing concepts introduce (rings and quotient rings, zero divisors, group characters), number-theory estimates on primes, numerical analysis of rounding errors, fast multiplication algorithms beyond the basics, or any coding-theory or quantum-computing notation, so those are explained in the wiki.

## Pages, in reading order

- `nlogn-history`: Multiplication complexity and the n log n conjecture: Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on multitape machines and conjectured that n log n is optimal; later work (Fürer, then Harvey–van der Hoeven) reached O(n log n), and the paper's theorem breaks the conjectured optimum.
- `fixed-tape-model`: Fixed finite-alphabet multitape model: The cost model of the paper: one machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where a step touches one cell per tape; extra tracks or work tapes change time only by a constant factor.
- `established-multiplier`: Established O(n log n) multiplier (subroutine): The Harvey–van der Hoeven O(N log N) integer multiplier, used as a black-box subroutine on short operands (never recursively on the improved algorithm).
- `stream-operations`: Array order and elementary stream operations: Arrays are stored in lexicographic address order on a tape; digit moves, digit swaps, pointwise maps on split streams and cyclic splitting of rows into W streams all take O(V) steps for volume V on fixed tapes.
- `controlled-shifts`: Controlled shifts: A target address field is cyclically shifted (or multiplied by a fixed unit modulo q^b) by an offset computed from control fields that precede it, in O(V) time by splitting each fibre in two pieces and merging them in reverse order.
- `linear-algebra-prelims`: Subspaces, orthogonality and rank: Vector subspaces over the rationals or over the two-element field, bilinear forms, orthogonal complements, nondegeneracy, projections, matrix rank and tensor products.
- `xor-linear-network`: Linear network exchanging two banks with restored scratch values: A fixed network of pointwise linear gates on wires (data banks X, Y, scratch and central wires) that in three stages maps (X,Y) to (−Y,X) and returns every scratch wire to its arbitrary initial value, as in transparent computation.
- `subset-labels`: Subspace labels from three-element subsets: Frankl–Wilson style construction: indicator vectors of three-element subsets of [100] give intersection-size inner products; tensor cubes of these lines label gates by nested nondegenerate subspaces so that edge changes are small orthogonal residuals.
- `frames`: Frames: changing the representation along a network: An invertible operator D_v on an array chosen at each source, gate and sink; every edge applies D_vD_u^{-1}, a common frame commutes with the pointwise linear gate, so the network implements D_out S D_in^{-1} and the endpoint frames fix the operator on every role.
- `rank-deficit`: Rank deficit s < W m: The sum s of ranks of all edge differences (the number of smaller calls) is strictly less than W·m, where W is the number of wires and m the label-space dimension; the deficit comes from the loss L on decreasing edges being below N/2.
- `power-saving-recurrence`: Recursive power saving from the rank deficit: A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.
- `bit-shear-interface`: Address shear from the bit network: Using the permutation frame Φ_M that moves the entry at (H,D) to (H+MD,D), the bit network's endpoint matrices differ by the identity, so it implements the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
- `lower-triangular-factorization`: Lower-triangular (Bruhat) factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear-cost`: Cost of a rational matrix shear: For a rational matrix A of rank a, the shear (H,D) ↦ (H+AD,D) over ℤ/q^bℤ is done with exactly a interchanges of b-digit fields and O(V) other work, using triangular updates as controlled shifts.
- `power-width-interchange`: Recursive power-width address interchange: Two address chunks of m^k digits are interchanged in O(V e^τ) by splitting rows into W role streams, running the bit network whose edges are shears (smaller interchanges), and finishing with D←D−H, H←H+D, D←H−D; a depth-first schedule on fixed tapes realizes the recursion.
- `arbitrary-width-interchange`: Address-chunk interchange in time O(V u^τ): Exchanging two disjoint contiguous address fields of u bits (any width, any gaps, even one-bit payload) in O(V u^τ) for a fixed τ = 1 − 2^{−50} < 1, by peeling off high digits to make rows, padding, and splitting the width in base m; the intermediate steps are XOR combinations though the result is an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: A binary row addition (XOR) of selected bits across many address chunks at once, done by a constant number of whole-chunk cyclic shifts using a third chunk of arbitrary contents as temporary storage, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with multiplication reduced by y^r = −1; multiplying by a power of y just rotates the coefficient list with sign changes, so powers of y act as roots of unity.
- `fixed-point-disk`: Fixed-point complex coefficients and truncation: Complex numbers stored as 2^{−p}(a+ib) with integer a, b inside the unit disk, written as signed two's-complement words; Q_p truncates real and imaginary parts toward zero to this grid, with error below √2·2^{−p} and no increase of norm.
- `signed-packing-product`: Signed packing of ring products: A signed form of Kronecker substitution evaluates polynomial records at 2^{4p}, multiplies the resulting integers with the established multiplier, extracts coefficients, wraps negacyclically and truncates, giving a ring product in O(rp log(rp)).
- `error-accounting`: Contractions and error accounting: Normalized transforms and averaged convolutions are contractions in the max-modulus norm, so errors of composed approximate steps add (bilinear steps add the two operand errors) and a final error below 1/2 permits rounding to integers.
- `dft`: Discrete Fourier transform: The map u ↦ (1/q)Σ_j u_j e^{−2πi jk/q} that evaluates a length-q sequence at the q-th roots of unity; it is a contraction in the max-modulus norm and has an inverse of the same shape with the opposite sign.
- `butterfly`: Two-point butterfly: The map H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the basic step of a radix-2 fast Fourier transform; applied to a coordinate bit it is a halving contraction.
- `phase-frame-network`: Complex phase network and two-point kernels: The same network over Gaussian dyadic values with binary labels and phase frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge change is a product of two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), and telescoping gives C^{⊗m} on every role with s_c < W_c·m kernel factors.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in time O(V d^λ′): Applying H₀ at once to the same bit position of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) for fixed λ' < 1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase network, packed bit moves, exact Gaussian dyadic arithmetic and one final truncation.
- `cyclic-convolution`: Cyclic convolution and the convolution theorem: The product of two polynomials modulo x^q − 1 (indices added mod q); the Fourier transform turns it into a pointwise product, so convolution = transform, multiply pointwise, inverse transform.
- `multidimensional-dft`: Multidimensional transforms and convolutions: A tensor product of one-dimensional transforms (or convolutions) along several axes of a box of size t₁×…×t_D, applied one axis at a time.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform can be written as a pointwise phase (chirp) multiplication, a cyclic convolution with a chirp array, and another chirp multiplication; here it also absorbs the frequency permutation Q.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring using roots ω_t = y^{2r/t} (signed shifts), computed by decimation-in-frequency rounds of butterflies and monomial twiddles y^E; it is a contraction and satisfies character cancellation despite zero divisors.
- `retained-frequency-order`: Retained (bit-reversed) frequency order: The recursion writes frequencies in bit-reversed slots; both forward transforms keep this order through the pointwise product and the opposite transform consumes it, so no sort is executed.
- `transform-layout`: Transform layout and cost: A positional layout permutation L places the selected bits of all axes at a common offset in consecutive K-bit chunks (prefix moves plus chunk exchanges), so each round is one simultaneous layer; the forward and opposite transforms cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2 ℓ 2^{−p}.
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms in layout order, a pointwise ring product divided by r, the opposite transform and an exact scaling by M compute the normalized convolution (f*g)/T over the negacyclic ring with error below √2 M(3ℓ+1)2^{−p}.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique that expresses a Fourier transform of coprime length s through a transform of the larger length t (a power of two) using Gaussian-weighted contractions A and B₀ and a Neumann-series inverse; the sorting permutations stay inside the transform identity.
- `padded-box-tensor-resampling`: Tensor resampling on the padded box: Resampling in d dimensions applies the one-dimensional maps line by line on a zero-padded box of T = Πt_i entries, exposing each axis with address-chunk interchanges, at total cost O(d T p^{3/2+δ} α) plus O(Tp d²(1+ℓ^τ)) for movement.
- `permutation-cancellation`: Retained permutations and their cancellation: The source permutation R left in the resampling identity cancels across two forward transforms, the pointwise product and the opposite-sign transform, giving R F_s⁺[(R F_s u)·(R F_s v)] = (u*v)/S².
- `radix-digit-convolution`: Integer multiplication as radix-digit convolution: Splitting each n-bit input into radix-2^b digits turns the product into a convolution of short digit polynomials, padded so that no cyclic wraparound occurs, followed by a left-to-right carry propagation that yields the 2n-bit product.
- `crt-map`: Chinese-remainder map to prime cyclic axes: For pairwise coprime lengths s_i with product S, the algebra isomorphism x ↦ Π x_i^{μ_i} turns one cyclic convolution of length S into a multidimensional cyclic convolution on prime axes; on tape it is a sequence of prefix-controlled cyclic shifts.
- `prime-axis-parameters`: Parameter choices and prime axis lengths: Fixed parameters b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^{⌈(log₂T)/d⌉}, axes of length r/2 or r, and distinct primes s_i just below t_i found by deterministic search, with ε = 2^{−75}, c = 2^{−56}, λ' = 1−2^{−54}, κ = 2^{−182}.
- `phase-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps ℂ[x]/(x^r − 1) isomorphically onto the negacyclic ring, turning the last cyclic axis into a polynomial ring; its negative wrap gives the cyclic wrap after untwisting.
- `source-transform`: Computed source transform: The source Fourier transform R F_s is computed as 2^γ B₀ Q F_t A: Gaussian expansion on each line, the chirp transform (a twisted synthetic convolution) and Gaussian compression, then a power-of-two scaling, all with tracked disk margins and errors.
- `exact-recovery`: Precision budget and exact recovery: Scale bookkeeping (the two factors S) and the error bound 448 b 2^{−b+γ} < 1/2 show that each recovered convolution coefficient rounds to the true integer, which is below 2^{3b}, so carries give the exact product.
- `multiplication-algorithm`: The multiplication algorithm: Digit extraction, the address map Φ to prime axes, two source transforms, a truncated pointwise product, the opposite-sign transform, rescaling by S and 2^{2b+4}, rounding, inverse address map and carry propagation, producing the 2n-bit product.
- `cost-accounting`: Complete time bound and power margins: Dividing costs by V = Tp gives seven dominant terms (butterfly rounds, chunk exchanges, simultaneous layers, CRT layouts, Gaussian lines, chirps, packed products) each at most p^{1−2κ}; the smallest margin is 2^{−181} = 2κ, which absorbs log factors and gives O(n(log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model; the saving comes from faster address interchange and butterfly layers inside a Gaussian-resampling, Bluestein, synthetic-transform reduction.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Multitape Turing machine
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `logarithms-exponentials-floor-and-ceiling`: Logarithms, exponentials, floor and ceiling
- `binary-representation-and-bitwise-operations`: Binary representation and bitwise operations
- `schoolbook-integer-arithmetic`: Schoolbook integer arithmetic
- `modular-arithmetic`: Modular arithmetic
- `primes-coprimality-and-gcd`: Primes, coprimality and gcd
- `sets-functions-cartesian-products-and-bijections`: Sets, functions, Cartesian products and bijections
- `permutations`: Permutations
- `matrices-and-linear-maps`: Matrices and linear maps
- `roots-of-unity`: Roots of unity
- `summation-geometric-series-and-products`: Summation, geometric series and products
- `recursion-and-divide-and-conquer-recurrences`: Recursion and divide-and-conquer recurrences
- `worst-case-running-time-and-subroutines`: Worst-case running time and subroutines
- `triangle-inequality-and-norms`: Triangle inequality and norms
- `rational-numbers-and-rounding`: Rational numbers and rounding
- `newton-s-method`: Newton's method
- `tapes-scanning-and-sorting-as-basic-machine-procedures`: Tapes, scanning and sorting as basic machine procedures

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
