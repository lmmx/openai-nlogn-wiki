# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

## Pages, in reading order

- `nlogn-conjecture`: The n log n conjecture and prior bounds: Schönhage–Strassen's 1971 bound O(n log n log log n), their conjecture that n log n is optimal, and Harvey–van der Hoeven's O(n log n) upper bound for multitape machines.
- `linear-network`: Linear network with restored scratch wires: A fixed circuit of linear gates on wires that exchanges two banks of values with a sign while arbitrary initial values on auxiliary scratch wires are cancelled and restored.
- `frames`: Frames on wire arrays: Invertible linear operators D_v on each wire's address-indexed array so that stored array = D_v applied to the logical array, commuting with pointwise gates so only edge changes D_v D_u^{-1} cost anything.
- `tape-streams`: Arrays as tape streams and elementary scans: Arrays stored in lexicographic address order on tapes, with logical volume V (number of stored bits), whose splitting, merging and digit moves cost linear time.
- `fixed-point-dyadics`: Fixed-point and Gaussian dyadic arithmetic: Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.
- `controlled-shift`: Controlled shifts and rational scalings: A linear-time tape operation that adds an offset, computed from earlier control fields, to a later address field modulo a prime power, or multiplies it by a rational unit.
- `linear-algebra-orthogonality`: Subspaces, bilinear forms and orthogonal complements: A subspace of a vector space with a nondegenerate bilinear form, its orthogonal complement, the projection onto it, and the dimension (rank) of the difference of two nested subspaces.
- `triple-subset-gadgets`: Triple-subset intersection gadgets: Gather, scatter and side-injection gates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size and whose side wires cancel the unwanted terms.
- `rank-deficit-labels`: Nested subspace labels and the rank deficit: Subspaces attached to gates and terminals so that adjacent labels are nested and the total rank s of all edge changes is strictly below the wire count times dimension, s < Wm.
- `recursive-power-saving`: Recursive power saving from the rank deficit: A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume grows like m^τ rather than m, with τ<1 because s/W<m.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Matrix shear on address fields: The address permutation (H,D)→(H+AD,D) modulo a prime power, which costs exactly rank(A) interchanges of b-digit fields plus linear work.
- `fast-chunk-interchange`: Fast interchange of address chunks: Swapping two disjoint contiguous address fields of u bits in an array of volume V in time O(V u^τ) for fixed τ<1, via XOR combinations of intermediate streams that finally form an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding corresponding selected bits of two address chunks using a third temporary chunk, via cyclic whole-chunk shifts plus a deterministic correction of an explicit small set of exceptional addresses.
- `ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r in which y^r = −1, so powers of y are roots of unity and multiplying by y^a is a signed cyclic shift of coefficients.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πijk/q} on length-q vectors, a contraction in the max norm.
- `two-point-butterfly`: Two-point butterfly layer: The map H₀(u,v)=((u+v)/2,(u−v)/2) applied to pairs, whose repeated layers build a radix-2 fast Fourier transform.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient arrays indexed by ℤ/tℤ (or a product of such groups) as in multiplication of polynomials modulo x^t−1; the Fourier transform turns it into pointwise multiplication.
- `multiplication-as-convolution`: Multiplication as convolution of radix digits: Splitting both integers into radix-2^b digits makes the product a convolution of the digit coefficient lists, followed by carry propagation.
- `multidimensional-transform`: Multidimensional transform: The tensor product of one-dimensional Fourier transforms along several axes, computing convolution on a product of cyclic groups.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, so multiplications by roots are exact signed shifts and only butterflies remain.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven method that expresses a Fourier transform of length s (coprime lengths) through a transform whose axis lengths are powers of two, via contractive Gaussian maps.
- `error-and-exact-recovery`: Error bounds and exact recovery: Contraction-based accumulation of approximation errors through all steps, removal of known normalizations and scales, showing the coefficient error is below 1/2 so rounding gives exact integers.
- `phase-twist`: Last-coordinate phase twist: The isomorphism x_d→ζy, ζ=e^{πi/r}, from ℂ[x_d]/(x_d^r−1) to ℂ[y]/(y^r+1) that turns cyclic wrap into negacyclic wrap and back.
- `nlogn-multiplier`: The established O(N log N) multiplier: The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log 2N) on N-bit inputs, used only as an ordinary subroutine on short inputs.
- `phase-frames`: Binary phase frames and the two-point kernel C: Frames C_U=H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} over Gaussian dyadics, whose edge changes are products of translation kernels aI+bX, composing to C^{⊗m} on every role.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: One H₀ butterfly at the same bit offset in up to d address chunks applied to all polynomial records at cost O(V d^{λ'}) for fixed λ'<1, evaluated exactly in dyadics with one final truncation.
- `synthetic-transform-layout`: Synthetic transform tape layout: A tape layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that parallel layers apply, with the frequency order retained.
- `kronecker-packing`: Signed packing for ring products: Multiplying two polynomials in the ring by packing signed coefficients into big integers (Kronecker substitution) and calling an O(N log N) integer multiplier.
- `synthetic-convolution`: Normalized convolution over the ring: Convolution of arrays over ℂ[y]/(y^r+1) as inverse transform of the pointwise product of forward transforms in the same frequency order, scaled by 1/T, with polynomial products done by signed packing.
- `resampling-without-sorting`: Resampling with permutations left in the transform: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A (and its tensor form) keeping both coordinate permutations inside the formula instead of sorting twice on each coordinate.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform (with its permutation) rewritten as a pointwise chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication; the source permutation cancels across the product of two transforms.
- `parameter-choice`: Parameter choice and cost table: Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism Φ sending x to Π x_i^{μ_i} that turns cyclic convolution of length S=Πs_i (pairwise coprime) into convolution on the product of cyclic axes, implemented by triangular controlled shifts.
- `multiplication-algorithm`: The multiplication algorithm: Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `xor-bits`: Bit XOR
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `logarithms-and-binary-logarithm`: Logarithms and binary logarithm
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `binary-representation-of-integers`: Binary representation of integers
- `radix-representation-and-digits`: Radix representation and digits
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `divide-and-conquer-and-recurrences`: Divide-and-conquer and recurrences
- `fast-fourier-transform-and-fft-multiplication`: Fast Fourier transform and FFT multiplication
- `mathematical-induction-and-proof-by-cases`: Mathematical induction and proof by cases
- `sets-subsets-and-cartesian-products`: Sets, subsets and Cartesian products
- `functions-bijections-and-permutations`: Functions, bijections and permutations
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-divisibility-and-coprimality`: Primes, divisibility and coprimality
- `rational-numbers-and-exact-fractions`: Rational numbers and exact fractions
- `finite-fields-and-the-field-f-2`: Finite fields and the field F_2
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `rank-basis-and-dimension`: Rank, basis and dimension
- `gaussian-elimination`: Gaussian elimination
- `inner-product-norm-and-orthonormal-basis`: Inner product, norm and orthonormal basis
- `roots-of-unity-and-euler-s-formula`: Roots of unity and Euler's formula
- `summation-and-product-notation`: Summation and product notation
- `newton-s-method`: Newton's method
- `integer-division-with-remainder`: Integer division with remainder
- `lexicographic-order`: Lexicographic order
- `arrays-records-and-matrix-transposition`: Arrays, records and matrix transposition
- `turing-machine-running-time-and-model-conventions`: Turing machine running time and model conventions

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
