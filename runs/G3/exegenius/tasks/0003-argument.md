# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/G3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: algorithm analysis with asymptotic notation and recurrences, discrete mathematics (induction, divisibility, gcd, primes, permutations, summations, modular arithmetic at the level of residues), the schoolbook and divide-and-conquer integer arithmetic algorithms, sorting, and the fast Fourier transform as an O(n log n) convolution algorithm. They have taken linear algebra (matrices, linear maps, rank, inverses, vector norms) and complex numbers, and know basic multitape Turing machines and bit-level data representation. They have not studied abstract algebra beyond what the existing concepts give, finite-field linear algebra, tensor products of vector spaces, analytic number theory, or the research literature on fast multiplication.

## Pages, in reading order

- `mult-history`: History of fast multiplication and the n log n conjecture: Schönhage–Strassen (1971) multiplied n-bit integers in O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Fürer and later work reduced the extra factor, and Harvey and van der Hoeven reached O(n log n).
- `radix-convolution`: Integer product as digit-polynomial convolution: Writing each n-bit input in radix 2^b gives digit polynomials whose ordinary product has coefficients below 2^{3b}, so the integer product is the convolution of the digit lists followed by carry propagation.
- `negacyclic-ring`: Negacyclic ring ℂ[y]/(yʳ + 1): The ring of complex polynomials of degree below r taken modulo yʳ + 1, in which multiplying by a power of y is a signed shift of the coefficient list.
- `signed-packing`: Signed packing of polynomial products: A Kronecker-substitution reduction that evaluates polynomials at 2^{4p}, multiplies the resulting integers with the established O(N log N) multiplier, and extracts signed coefficients to get exact products in the negacyclic ring.
- `stream-scans`: Elementary stream scans on tapes: Splitting, merging, digit moves and row-wise stream splitting on a lexicographically stored array cost O(V) steps for volume V on a fixed number of tapes, with counters and head returns included.
- `linear-spaces`: Subspaces, orthogonal complements and bilinear forms: Linear subspaces of a vector space with a nondegenerate bilinear form, their orthogonal complements, projections and dimensions, used to label network vertices.
- `common-frame`: Frames and pointwise gates: Giving every wire at a gate the same invertible linear operator on its address-indexed array lets the pointwise linear gate commute with it, so only endpoint frames determine the net operator and edges change frames cheaply.
- `scratch-network`: Scratch-restoring bank-exchange network: A fixed network of pointwise linear gates built from copy, gather, scatter and side wires over three-element subsets that exchanges two data banks in three stages and returns every auxiliary scratch wire to its arbitrary initial value.
- `subspace-labels`: Nested subspace labels and the rank saving: Subspaces of an m-dimensional space attached to gates and terminals, nested along edges, so that the sum of edge ranks s is strictly less than the wire count W times m.
- `phase-frames`: Phase frames and the two-point kernel C: Over binary labels the frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} turn each edge into a product of translation kernels aI + bX_v built from C = H S H, with H₀ = b S C S.
- `fixed-point-grid`: Fixed-point complex numbers on a disk grid: Complex values with real and imaginary parts that are integer multiples of 2^{−p} inside the unit disk, stored as two signed two's-complement words, with truncation toward zero to the grid.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The normalized length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q} turns cyclic convolution into pointwise multiplication, and its opposite-sign transform inverts it up to scale.
- `multidim-transform`: Multidimensional transforms on product axes: A transform on an array indexed by a product of axes, defined as the tensor product of one-dimensional transforms and computed one axis (coordinate line) at a time.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms F_t^± over the negacyclic ring using the roots ω_t = y^{2r/t}, so multiplication by a root is a free signed shift; their character sums cancel to give F⁺F⁻ = I/t.
- `chirp-identity`: Bluestein chirp identity: Multiplying by a quadratic-phase chirp before and after a cyclic convolution with the chirp reproduces the permuted Fourier transform Q F_t, so a transform becomes a convolution.
- `butterfly-order`: Radix-2 butterflies and stored frequency order: The decimation-in-frequency recursion applies the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle shift at each level, writing outputs in bit-reversed order that the opposite transform consumes directly.
- `contraction-error`: Contractions and error accumulation: A linear map that never increases the maximum coordinate modulus is a contraction, so approximation errors of composed steps add and every normalized transform keeps values inside the unit disk.
- `modular-crt`: Modular arithmetic and the Chinese remainder theorem: Residues modulo pairwise coprime moduli determine a number modulo their product, so a cyclic index of length s₁⋯s_d splits into independent coordinates modulo each sᵢ.
- `controlled-shifts`: Controlled cyclic shifts of an address field: Updating a target field y mod q^b by an offset computed from earlier control fields, or multiplying it by a unit, costs O(V) on tape by splitting each fiber at the offset and merging the pieces swapped.
- `crt-prime-axes`: Chinese-remainder address map to prime axes: A ring isomorphism sending x to ∏ xᵢ^{μᵢ} that places a length-S cyclic coefficient list on a product of cyclic axes of pairwise coprime (prime) lengths while preserving convolution; the induced address change is a sequence of triangular controlled shifts.
- `matrix-shear`: Matrix shears and triangular factorization: The address map (H,D) → (H+AD,D) for a rational matrix A of rank a is done with exactly a field interchanges plus linear-cost triangular updates, using the factorization A = E₁ΠE₂ with E₁,E₂ lower triangular.
- `rank-saving-recurrence`: Recursion with a strict rank saving: Each call at parameter mf makes s calls at parameter f on streams of volume V/W, so the normalized cost obeys F_k ≤ (s/W)F_{k−1} + O(1) and, because s/W < m, grows like m^{kτ} with τ < 1.
- `address-interchange`: Fast address chunk interchange: Two disjoint equal-width address chunks of u bits are exchanged in O(V u^τ) time for a fixed τ < 1 by computing XOR combinations of intermediate streams through the bit network, even though the net effect is an exact permutation.
- `packed-bit-addition`: Packed addition on selected address bits: A binary row addition y_j ← y_j ⊕ x_j on the same bit position of several address chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set.
- `butterfly-layer`: Fast simultaneous butterfly layer: The two-point butterfly H₀ applied at once to one bit position of each of up to d address chunks of polynomial records costs O(V d^λ′) with λ′ < 1, evaluated exactly in Gaussian dyadics and truncated once.
- `transform-layout`: Tape layout for synthetic transforms: A positional permutation of record addresses puts the selected bits of all participating axes at a common offset in consecutive K-bit chunks, so each transform round is one simultaneous butterfly layer.
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms keep their common stored frequency order, the ring records are multiplied pointwise by signed packing, and the opposite transform consumes that order to give normalized convolution over the negacyclic ring.
- `phase-twist`: Phase twist from cyclic to negacyclic wrap: Multiplying coefficient k of the last cyclic axis by e^{πik/r} makes a length-r cyclic coordinate a polynomial modulo yʳ + 1, and the negative wrap becomes the correct cyclic wrap after untwisting.
- `gaussian-resampling`: Gaussian resampling with permutations retained: An identity P_s F_s = 2^{2α²} B₀ P_t F_t A (tensored over axes) expressing a Fourier transform of prime-related length s through a transform of power-of-two length t using Gaussian-weighted contractions A and B₀, with the coordinate permutations kept inside the formula.
- `permutation-cancel`: Source permutation cancellation: The coordinate permutation R retained in the source transform cancels across the two forward transforms, their pointwise product and the opposite-sign transform, so the product is exactly u*v/S².
- `parameter-choice`: Parameter choices and prime source lengths: The padded box size T, precision p = 6b, number of axes d, chunk width K, ring size r and distinct odd primes sᵢ just below the power-of-two axis lengths tᵢ are chosen so the resampling and layer hypotheses hold.
- `exact-recovery`: Exact recovery by rounding and carries: Because the accumulated numerical error on every recovered coefficient is below 1/2, rounding gives the exact integer convolution coefficients, and radix-2^b carry propagation yields the 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: Convert inputs to radix-2^b digit lists, map them by the Chinese-remainder address map, apply the resampled chirp source transform to each, multiply pointwise, apply the opposite transform, rescale, round, undo the address map and propagate carries.
- `cost-table`: Cost accounting and the exponent κ: Dividing every step's cost by the volume Tp gives seven dominant powers of p, each at most 1 − 2κ, which with κ = 2^{−182} yields total time O(n (lg n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Multitape Turing machine
- `binary-representation-of-integers-and-radix-expansions`: Binary representation of integers and radix expansions
- `schoolbook-arithmetic-and-carries`: Schoolbook arithmetic and carries
- `fast-fourier-transform-and-the-convolution-theorem`: Fast Fourier transform and the convolution theorem
- `linear-maps-and-matrices`: Linear maps and matrices
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `permutations-of-indices`: Permutations of indices
- `divisibility-gcd-and-coprime-integers`: Divisibility, gcd and coprime integers
- `prime-numbers-and-primality-testing-by-trial-division`: Prime numbers and primality testing by trial division
- `floor-ceiling-rounding-and-logarithms`: Floor, ceiling, rounding and logarithms
- `bitwise-xor-and-hamming-weight`: Bitwise XOR and Hamming weight
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `recurrences-induction-and-geometric-series`: Recurrences, induction and geometric series
- `sorting-and-its-o-n-log-n-cost`: Sorting and its O(N log N) cost
- `summation-product-and-index-notation`: Summation, product and index notation
- `integers-rationals-and-gaussian-integers`: Integers, rationals and Gaussian integers
- `euler-s-formula-and-complex-exponentials`: Euler's formula and complex exponentials
- `time-and-bit-complexity-of-turing-machine-computation`: Time and bit complexity of Turing machine computation

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
