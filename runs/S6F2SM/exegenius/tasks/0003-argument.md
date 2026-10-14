# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/S6F2SM` (paths below are relative to it)

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

`main-theorem`: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, using fast address-chunk interchange and simultaneous butterfly layers to speed synthetic transforms inside a Gaussian-resampling multiplication.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

## Pages, in reading order

- `n-log-n-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's conjecture that n log n is the optimal order of growth for the time to multiply two n-bit integers on a multitape Turing machine.
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each integer as a polynomial in a power of two 2^b, the product's digit-coefficient list is the convolution of the two digit lists, followed by carry propagation.
- `triple-gadget`: Three-element subset intersection gadget: Gather, scatter and side-injection updates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size; side wires cancel the unwanted intersection-one (or intersection-zero/two) contributions.
- `bank-exchange-network`: Linear network that exchanges two banks and restores scratch values: A fixed network of linear gates with three stages whose net effect is (X, Y) ↦ (−Y, X) on two banks, restoring every auxiliary scratch value whatever its initial contents.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: One machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads and writes one cell per tape and moves each head by at most one cell, and cost is the number of steps.
- `nlogn-subroutine`: Established n log n multiplier as a subroutine: The Harvey–van der Hoeven O(N log N) integer multiplier is used as an ordinary subroutine on short inputs and does not invoke the improved theorem recursively.
- `stream-arrays`: Arrays, address fields and elementary scans: Arrays with a product address set are stored in lexicographic order on tape, with addresses implicit in position; fixed permutations of digits, digit moves, pointwise maps and cyclic row splits cost O(V) for V stored bits.
- `frames`: Frames and the common-frame identity: An invertible operator D_v on each wire's address-indexed array at every network vertex; since gates are pointwise and linear they commute with a shared frame, so the whole network implements D_out S D_in⁻¹ and only edge changes D_v D_u⁻¹ cost anything.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A linear-time tape operation that adds an offset computed from earlier control fields to a later target field modulo q^b, or multiplies it by a fixed unit, by splitting and re-merging blocks.
- `bilinear-orthogonal`: Orthogonal complements and projections in a bilinear space: In a vector space with a nondegenerate symmetric bilinear form, a subspace U has an orthogonal complement U⊥ and a projection P_U along it; the residual of nested subspaces has dimension equal to the difference of their dimensions.
- `subspace-labels`: Nested subspace labels and the rank saving: Subspaces of an m-dimensional space attached to gates and terminals so adjacent labels are nested; edge dimension changes count the smaller operations needed, and their total s is strictly below W·m.
- `triangular-factorization`: Lower-triangular rank factorization: Every rational square matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones (a Bruhat factorization with coordinate order reversed).
- `matrix-shear`: Cost of a rational matrix shear: The address update (H, D) ↦ (H + AD, D) over Z/q^b is performed with exactly rank(A) interchanges of pairs of b-digit fields plus linear extra work, using triangular factors and controlled shifts.
- `power-width-interchange`: Power-width chunk interchange in O(Ve^τ) time: Recursively interchanges two chunks of e = m^k digits by running the bank-exchange network on W role streams of volume V/W, each edge costing rank-many smaller interchanges; since s/W < m^τ the cost per volume is O(e^τ).
- `chunk-swap`: Chunk interchange in O(Vu^τ) time: Interchanges two disjoint address chunks of u bits in any bit array in O(V u^τ) steps for a fixed τ < 1, by padding rows and splitting the width in base m into power-width pieces; intermediate steps are XOR combinations but the final effect is an exact permutation.
- `packed-selected-bits`: Packed XOR of selected bits across address chunks: A binary row addition y ← y ⊕ x on the selected bit of each of f chunks at once, done by a constant number of cyclic shifts of whole chunk ranges followed by deterministic repair of a small explicit set of bad addresses, using a third chunk as restored temporary space.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed shift of the coefficient list.
- `signed-kronecker-packing`: Signed Kronecker packing of polynomial products: Multiplying two polynomial records exactly by evaluating their integer-coefficient parts at a large power of two, multiplying the resulting integers with the established multiplier, and recovering signed coefficients by centered carries.
- `fixed-point-disk-grid`: Fixed-point disk-grid arithmetic and contractions: Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.
- `dft-cyclic-convolution`: Normalized DFT and cyclic convolution: The length-q discrete Fourier transform with 1/q normalization turns cyclic convolution into pointwise multiplication; its inverse uses the opposite sign of the exponent.
- `multidim-transform`: Multidimensional (tensor) Fourier transform: The tensor product of one-dimensional transforms along several axes; a transform on an array with axis lengths t_1,…,t_d is applied axis by axis.
- `crt-axis-map`: Chinese-remainder map to prime cyclic axes: An algebra isomorphism sending one cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on a product of d cyclic axes, implemented by triangular controlled cyclic shifts.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through a Fourier transform of a larger power-of-two length t, using Gaussian-weighted interpolation maps A and B₀.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another pointwise phase multiplication.
- `coefficient-twist`: Twist from cyclic to negacyclic convolution: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} is a ring isomorphism from the cyclic ring (x^r = 1) to the ring modulo y^r + 1, so its negative wrap yields the cyclic wrap after untwisting.
- `synthetic-transform`: Synthetic Fourier transform modulo y^r + 1: A Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddle multiplications are signed coefficient shifts; it satisfies a character-cancellation identity despite zero divisors.
- `butterfly-layers`: Radix-2 butterfly layers and stored frequency order: Decimation in frequency: each level combines entries k and k+t/2 by the two-point butterfly H₀ and a twiddle monomial, leaving frequencies stored in bit-reversed order, which the opposite transform consumes directly.
- `phase-kernel-network`: Two-point kernel C and the complex phase network: The Gaussian-dyadic two-point kernel C = H S H = aI + bX (a = (1+i)/2, b = (1−i)/2) satisfies H₀ = b S C S; the complex bank-exchange network with binary labels makes C^{⊗m} on every role from products of translation kernels, one per residual basis vector.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in O(Vd^λ') time: Applies the normalized butterfly H₀ to one bit position in each of d address chunks of polynomial records in one pass, exactly in Gaussian dyadics followed by a single truncation, in O(V d^λ') for a fixed λ' < 1 instead of d whole-array passes.
- `transform-layout`: Layout and cost of the synthetic transform: A positional layout permutation puts the selected bits of all axes at a common offset in K-bit chunks so each transform round is one simultaneous layer; the forward transform keeps its output order for the pointwise product and the opposite transform.
- `ring-convolution`: Convolution over the polynomial ring from the retained layout: Normalized convolution of arrays over the ring modulo y^r + 1: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform consuming the same frequency order, with error O(M ℓ 2^{-p}).
- `resampling-no-sort`: Resampling with the permutations left in the transform: The tensor form of Gaussian resampling in which the source and target coordinate permutations R and Q stay inside the transform identity, so they need not be executed as separate sorts.
- `chirp-permutation-cancel`: Chirp identity and source-permutation cancellation: A chirp-convolution formula for Q·F_t that leaves the target permutation unexecuted, together with the fact that the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform.
- `parameter-choice`: Choice of sizes, precision and prime axis lengths: Fixing b = ⌈log₂ n⌉, precision p = 6b, axis count d = ⌊b^ε⌋, padded size T ≈ n/b, record length r, power-of-two axis lengths t_i, and distinct odd prime lengths s_i just below t_i, so that Tp = Θ(n) and all hypotheses of the interfaces hold.
- `source-transform`: Source transform via resampling, chirp and ring convolution: The computed procedure for a source Fourier transform of prime lengths: Gaussian maps A, then a chirp transform evaluated by a twisted ring convolution, then B₀ and an exact power-of-two scale, with exact counterpart R F_s.
- `exact-recovery`: Exact recovery: scaling, rounding and carries: Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2 so rounding gives exact convolution coefficients, then propagating radix-2^b carries to the 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: Split into radix digits, map by Φ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with the two scalings by S, round, undo Φ, and propagate carries to output the 2n-bit product.
- `cost-accounting`: Cost accounting and the saving exponent κ: A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.
- `main-theorem`: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, using fast address-chunk interchange and simultaneous butterfly layers to speed synthetic transforms inside a Gaussian-resampling multiplication.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Turing machines and tapes
- `modular-arithmetic-and-residues`: Modular arithmetic and residues
- `primes-divisibility-gcd-and-coprimality`: Primes, divisibility, gcd and coprimality
- `binary-representation-of-integers`: Binary representation of integers
- `bitwise-xor`: Bitwise XOR
- `logarithms-floors-ceilings-and-powers-of-two`: Logarithms, floors, ceilings and powers of two
- `matrices-invertibility-and-rank`: Matrices, invertibility and rank
- `vector-spaces-basis-and-dimension`: Vector spaces, basis and dimension
- `permutations-and-permutation-matrices`: Permutations and permutation matrices
- `lexicographic-order-and-index-tuples`: Lexicographic order and index tuples
- `euler-s-formula-and-roots-of-unity-as-points-on-the-unit-circle`: Euler's formula and roots of unity as points on the unit circle
- `geometric-series-and-orthogonality-of-sums-of-roots-of-unity`: Geometric series and orthogonality of sums of roots of unity
- `norms-and-the-triangle-inequality`: Norms and the triangle inequality
- `rational-numbers-dyadic-rationals-and-exact-arithmetic`: Rational numbers, dyadic rationals and exact arithmetic
- `algebraic-structures-groups-rings-and-isomorphisms`: Algebraic structures: groups, rings and isomorphisms
- `discrete-math-proof-techniques`: Discrete-math proof techniques
- `schoolbook-multiplication-and-divide-and-conquer-multiplication`: Schoolbook multiplication and divide-and-conquer multiplication
- `multitape-machine-cost-model-and-linear-time-scans`: Multitape machine cost model and linear-time scans
- `complex-polynomial-evaluation-and-interpolation`: Complex polynomial evaluation and interpolation
- `gaussian-function`: Gaussian function
- `convolution-as-polynomial-multiplication`: Convolution as polynomial multiplication
- `quantifiers-sets-and-basic-asymptotic-notation-beyond-big-o`: Quantifiers, sets and basic asymptotic notation beyond big-O

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
