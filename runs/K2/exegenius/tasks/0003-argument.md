# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/K2` (paths below are relative to it)

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

`main-theorem`: Deterministic integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape machine with a fixed finite alphabet and a fixed finite number of tapes that multiplies two n-bit integers exactly in worst-case time O(n (lg n)^(1−κ)) with κ = 2^(−182), which refutes the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, counting, induction, modular arithmetic, gcd and primes), calculus and a first linear algebra course (matrix rank and row reduction), an algorithms course (asymptotic notations, recurrences, sorting, schoolbook arithmetic), and a theory course on Turing machines and their running time. Complex numbers are known through polar form and roots of unity, and binary and two's-complement representation through computer organization. Each subject is taken only to first-course depth: no abstract algebra beyond the fields and rings that linear algebra uses, no Fourier analysis beyond the finite transform, no number theory beyond gcd, primes and modular inverses, and nothing from coding theory, circuit complexity or the specialist finite-network material.

## Pages, in reading order

- `polynomial-ring`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients of degree less than r, where r is a power of two and y^r is identified with −1, so that multiplication by a power of y is a signed cyclic shift of the coefficient list.
- `polynomial-roots-of-unity`: Polynomial roots of unity: The observation that powers of y in the polynomial ring are roots of unity whose multiplication is a signed shift, so a transform over the ring can use them as twiddle factors.
- `two-point-butterfly`: Normalized two-point butterfly: The map (u, v) to ((u + v)/2, (u − v)/2) applied to a pair of coefficients, the basic step of the synthetic transforms.
- `gaussian-dyadic`: Gaussian dyadic: A complex number whose real and imaginary parts are dyadic rationals, that is, have power-of-two denominators.
- `linear-algebra`: Linear algebra over a field: Vector spaces, linear maps and matrices, with subspaces, bilinear forms, orthogonal complements and tensor products, as used by the finite networks and their labels.
- `fixed-tape-machine`: Fixed-tape Turing machine model: A machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, in which each step moves each head by at most one cell and running time counts these steps.
- `schonhage-strassen-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 proposal that n log n is the optimal order of growth for multiplying integers on a multitape Turing machine; the main result refutes it in the fixed-tape model.
- `logical-volume`: Logical volume: The number V of stored data bits in an array, not counting work tapes or duplicate streams; every tape cost is measured against V.
- `address-fields`: Address fields and rows: An array is indexed by a complete lexicographic product of address fields and stored in that order, and a row is the complete block of entries at one fixed prefix and row index.
- `elementary-stream-operations`: Elementary stream operations: Linear-time scans on a fixed number of tapes that permute or move digits at chosen positions, apply fixed pointwise maps to aligned streams, and split whole rows cyclically into W streams of equal volume.
- `row-splitting`: Row splitting into role streams: Distributing the rows of an array cyclically among W role streams, so that each stream has the same shape and volume V/W and gates act pointwise on matching addresses.
- `controlled-shifts`: Controlled cyclic shifts: A cyclic shift of a target field by an offset computed from the preceding control fields, together with multiplication by fixed rational units, all done in linear time on tapes.
- `scratch-restoration`: Restoration of arbitrary scratch values: A linear computation whose auxiliary wires may start with arbitrary values and end with the same values, so that an exchange of two banks can be performed without knowing the scratch contents (the transparent-computation idea of Buhrman et al.).
- `triple-subset-exchange-network`: Triple-subset exchange network: A fixed linear network whose banks are indexed by triples of three-element subsets of a 100-element set, which exchanges two banks with a sign while restoring all scratch wires, using eight rows of copy, gather, scatter and side-injection operations.
- `frames`: Frames on network vertices: An invertible linear operator attached to each gate, source and sink of a network, which changes the stored representation of a wire's array so that every gate acts pointwise and the endpoint operators are the only net effect.
- `subspace-labels`: Subspace labels and orthogonal residuals: A nondegenerate subspace attached to each network vertex, with one label containing the other along every edge, so that the dimension of the orthogonal residual on an edge measures the cost of its frame change.
- `rank-saving`: Rank saving s < Wm: The inequality that the number s of smaller calls is less than W times m, where W is the number of wires and m the label dimension, which is the source of the power saving.
- `volume-normalized-recursion`: Volume-normalized recursion: A recursion in which cost per unit volume is multiplied by s/W at each level, with s/W below m to the power tau, so that the total cost is O(e^tau) per unit volume for chunks of e = m^k digits.
- `lower-triangular-factorization`: Lower-triangular factorization: Every rational matrix of rank a factors as an invertible lower-triangular matrix times a partial permutation matrix with exactly a ones, times another invertible lower-triangular matrix.
- `matrix-shear-interchange`: Matrix shear of address fields: The map (H, D) to (H + AD, D) on two groups of address fields for a fixed rational matrix A of rank a, performed with exactly a interchanges of field pairs and linear extra work.
- `circuit-to-address-permutation`: Finite circuit as address permutation: The transfer of a finite bit circuit with rational vertex matrices whose rank sum is below Wm into a permutation of address fields that applies the same shear to every wire role.
- `power-width-chunk-interchange`: Power-width chunk interchange: The interchange of two disjoint equal chunks of e = m^k digits in O(V e^tau) time, by splitting rows into W role streams, applying one shear per unit of rank on the streams, and recursing with the same fixed tapes.
- `arbitrary-width-chunk-interchange`: Arbitrary-width chunk interchange: The interchange of two equal bit chunks of arbitrary width u in O(V u^tau) time, by padding to a power of the radix, moving high digits into a row field, and handling the remaining width as a sum of power-width pieces in base m.
- `two-point-phase-kernel`: Two-point phase kernel: The 2 by 2 matrix C = aI + bX with a = (1 + i)/2 and b = (1 − i)/2, the Hadamard conjugate of the phase diag(1, i), which satisfies C² = X and C⁴ = I and is the one-bit kernel from which phase frames are built.
- `binary-phase-frames`: Binary phase frames: Frames indexed by binary subspace labels, built from the Hadamard transform and phases i raised to the Hamming weight of each label's projection, so that each edge change is a product of two-point phase kernels, one per residual basis vector.
- `packed-selected-bit-xor`: Packed selected-bit XOR: A linear-time operation that XORs the selected bits of one address chunk slot into the corresponding selected bits of another for all selected positions at once, using eight packed rotations of guarded segments followed by deterministic repair of the few addresses whose guards fail.
- `guard-bits`: Guard bits: Extra fractional and integer bits reserved in each coefficient so that every intermediate value of an exact butterfly layer is represented exactly, with a width bound that grows only as a fixed power of the number of selected axes.
- `disk-grid-arrays`: Disk-grid arrays: Arrays of coefficients lying in the complex unit disk and on the grid 2^(−p) times the Gaussian integers, which hold every approximate value in the algorithm.
- `grid-truncation`: Truncation to the precision grid: Rounding each real and imaginary part of a coefficient toward zero onto the grid of spacing 2^(−p), which keeps arrays in the disk and moves each entry by less than sqrt(2) times 2^(−p).
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The application of the normalized two-point butterfly to the same selected bit position in each of D address chunks at once, computed exactly through binary phase frames and truncated once, at cost O(V d^(λ')) with λ' below one instead of D separate passes.
- `transform-layout`: Positional layout of transform axes: A positional permutation of record addresses that places the selected bits of all participating axes at a common offset in consecutive K-bit chunks, realized by single-bit moves and chunk interchanges so that the simultaneous layer applies.
- `cyclic-convolution`: Cyclic convolution: The convolution of two arrays indexed by a product of cyclic groups, in which each output entry sums products of input entries whose indices are added modulo the axis lengths.
- `radix-digit-convolution`: Radix-digit convolution: The reduction of multiplying two n-bit integers to a cyclic convolution of their radix-2^b digit sequences, each with q = ceil(n/b) digits, whose coefficients are at most q(2^b − 1)^2, which is below 2^(3b).
- `crt-coefficient-map`: Chinese-remainder coefficient map: The algebra isomorphism x ↦ product of x_i^(μ_i) from C[x]/(x^S − 1) to a tensor product of cyclic rings for pairwise coprime lengths s_i, which preserves cyclic convolution and turns the ordinary coefficient order into a mixed-radix order reached by controlled cyclic shifts.
- `negacyclic-twist`: Phase twist of the last coordinate: The isomorphism from the cyclic group algebra of length r to the polynomial ring that sends x to ζy with ζ = e^(πi/r), implemented by multiplying coefficient k by ζ^k and undone by multiplying by ζ^(−k).
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map (F_q u)_k = (1/q) times the sum over j of u_j e^(−2πi jk/q) on vectors of length q, together with its opposite-sign partner F_q^+, which turns cyclic convolution into pointwise products up to a known factor.
- `synthetic-transform`: Synthetic polynomial transform: A normalized radix-two transform over the polynomial ring whose twiddle factors are powers of y, so each round is a parallel butterfly followed by a signed shift and the whole transform is a contraction.
- `bluestein-chirp`: Bluestein chirp identity: Bluestein's identity QF_t u = conj(a) · (a ∗ (conj(a) · u))/T, with chirp a_j = exp(−πi Σ s_i j_i²/t_i), which writes the middle transform, including its target permutation, as one cyclic convolution with pointwise phases.
- `synthetic-transform-on-tapes`: Synthetic transform on fixed tapes: The forward and opposite synthetic transforms implemented on fixed tapes as a sequence of simultaneous butterfly rounds on the transform layout, with error below sqrt(2) times l times 2^(−p) and time proportional to the logical volume times a power of p.
- `frequency-order-retention`: Retained frequency order: The stored record order produced by the forward synthetic transforms, which is preserved through a pointwise product so that the opposite transform consumes it without extra data movement.
- `hvdh-multiplier`: Established fixed-tape integer multiplier: Harvey and van der Hoeven's deterministic fixed-tape multiplication of N-bit integers in O(N log N) time, which the new algorithm calls as an ordinary subroutine on shorter records.
- `signed-coefficient-packing`: Signed coefficient packing: Evaluating two integer polynomials at a large base 2^(4p) so that one exact integer product yields all coefficient products, with signed carries recovered by centered residues; it is a signed form of Kronecker substitution.
- `ring-product`: Normalized polynomial-ring product: The normalized product f g / r of two disk-grid polynomials in the polynomial ring, computed exactly by signed packing into four integer products and returned truncated to the grid.
- `normalized-ring-convolution`: Normalized ring convolution: The bilinear contraction M_r(f, g) = (f ∗ g)/(rM) = (f ∗ g)/T on arrays over the polynomial ring, computed as two forward synthetic transforms, a pointwise ring product and an opposite transform.
- `approximate-roots-of-unity`: Approximate roots of unity: Disk-grid approximations of the roots of unity e^(2πi j/k) with error below 2^(−p), computable in time O(max(p, log k)^(1+δ)) and used for the phase twists.
- `contraction`: Contraction: A linear map that does not increase the maximum-modulus norm, so that an error in its input is not amplified when it is applied to an approximation.
- `gaussian-resampling`: Gaussian resampling: The identity P_s F_s = 2^(2α²) B_0 P_t F_t A, with contractions A and B_0 built from Gaussian weights, which expresses a length-s Fourier transform through a length-t transform when t/s is close to one, keeping the coordinate permutations inside the identity.
- `fixed-exponent-choices`: Fixed rational exponent choices: The fixed rational exponents τ = σ = 1 − 2^(−50), λ = 1 − 2^(−52), λ' = 1 − 2^(−54), c = 2^(−56), ε = 2^(−75) and κ = 2^(−182), chosen so that every cost term fits the target bound.
- `size-parameters`: Size parameters for the input length: The parameters derived from the input length n: b = ceil(log2 n), p = 6b, d = floor(b^ε), K = floor(d^c), a power of two T in [4n/b, 8n/b), and r = 2^(ceil(log2 T / d)), chosen so that T = r M and every axis length is r/2 or r.
- `prime-source-lengths`: Prime source lengths: The choice, for each axis, of a distinct odd prime s_i just below a power of two t_i with (1 − 2η) t_i < s_i ≤ (1 − η) t_i, so that the product S exceeds T/2 and each ratio t_i/s_i is large enough for the resampling lemma.
- `permutation-free-resampling`: Resampling with permutations left in the transform: Fixed-tape approximations to the Gaussian resampling maps A and B_0 for one length, with error below p^2 and time O(t p^(3/2+δ) α), in which both coordinate permutations stay in the transform identity instead of being executed as sorts.
- `tensor-resampling`: Multidimensional Gaussian resampling: The tensor product of the one-dimensional resampling identities over all d axes, R F_s = 2^γ B_0 Q F_t A with γ = 2dα², applied one coordinate line at a time on the padded power-of-two box.
- `source-permutation-cancellation`: Cancellation of the source permutation: The identity (R F_s^+)[(R F_s u)·(R F_s v)] = (u ∗ v)/S², which shows that the retained source permutation cancels across the two forward source transforms, their pointwise product and the opposite transform, leaving an ordinary convolution.
- `complex-convolution-by-twist`: Complex cyclic convolution by twist: The normalized complex cyclic convolution obtained from the normalized ring convolution by applying the phase twist to each operand and its inverse to the result, which is the convolution the chirp identity needs.
- `chirp-transform-procedure`: Computed chirp transform: The chirp identity evaluated with approximate phases, a computed complex convolution and final truncations, mapping a disk-grid array of norm at most 0.6 to an approximation of QF_t x with error below 8TL·2^(−p).
- `source-transform`: Source transform: The approximate forward transform of a source array, obtained by applying the linewise map A, then the computed chirp transform, then the linewise map B_0, and multiplying by 2^γ, which approximates R F_s.
- `digit-convolution-algorithm`: Multiplication algorithm by transforms: The integer multiplication procedure: split both inputs into radix digits, apply the coordinate map, compute both source transforms, multiply pointwise, apply the opposite transform, scale and round the coefficients, and propagate carries.
- `carry-propagation`: Carry propagation: The sweep that turns the recovered integer coefficients c_j into the binary digits of the product, using carries k_(j+1) = floor((c_j + k_j)/2^b) that stay below 2^(2b), processed from least to most significant.
- `precision-and-exact-recovery`: Precision and exact recovery: The error analysis showing that every intermediate array stays in the disk and that the recovered coefficients have total error below one half, so rounding each coefficient gives the exact product.
- `cost-exponent-accounting`: Cost accounting for the dominant terms: The accounting that writes every cost term as T p times a power of p, shows that each of the seven dominant exponents is at least 2κ below one, and so totals O(n (log n)^(1−κ)).
- `main-theorem`: Deterministic integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape machine with a fixed finite alphabet and a fixed finite number of tapes that multiplies two n-bit integers exactly in worst-case time O(n (lg n)^(1−κ)) with κ = 2^(−182), which refutes the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machines`: Basic Turing machines and tapes
- `arithmetic-modulo-n`: Arithmetic modulo n
- `the-field-with-two-elements`: The field with two elements
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `positional-radix-number-representation`: Positional (radix) number representation
- `two-s-complement-integers`: Two's-complement integers
- `bitwise-operations`: Bitwise operations
- `hamming-weight`: Hamming weight
- `floor-ceiling-logarithms-and-exponentials`: Floor, ceiling, logarithms and exponentials
- `theta-omega-and-little-o-notation`: Theta, Omega and little-o notation
- `geometric-series`: Geometric series
- `recurrence-relations`: Recurrence relations
- `mathematical-induction-and-proof-by-contradiction`: Mathematical induction and proof by contradiction
- `sets-cartesian-products-and-lexicographic-order`: Sets, Cartesian products and lexicographic order
- `permutations-and-permutation-matrices`: Permutations and permutation matrices
- `binomial-coefficients-and-counting-subsets`: Binomial coefficients and counting subsets
- `polar-form-euler-s-formula-and-roots-of-unity`: Polar form, Euler's formula and roots of unity
- `matrix-rank-and-gaussian-elimination`: Matrix rank and Gaussian elimination
- `directed-graphs`: Directed graphs
- `worst-case-time-complexity-of-turing-machines`: Worst-case time complexity of Turing machines
- `sorting-stability-and-radix-sort`: Sorting, stability and radix sort
- `schoolbook-multiplication-and-long-division`: Schoolbook multiplication and long division

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
