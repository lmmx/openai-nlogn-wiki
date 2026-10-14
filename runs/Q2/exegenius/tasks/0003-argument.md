# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/Q2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education. In discrete mathematics they have sets, counting and binomial coefficients, induction, graphs, modular arithmetic, gcd and the extended Euclidean algorithm, primes and the Chinese remainder theorem. In algorithms and theory they have worst-case analysis, recurrences, sorting, stacks, binary counters, schoolbook and Karatsuba multiplication, Boolean circuits and the multitape Turing machine with its constant-factor simulations, and in computer arithmetic they have binary, two's-complement and fixed-point numbers with carries. They have also taken a first course in linear algebra over the reals (vector spaces, matrices, Gaussian elimination, triangular matrices, eigenvalues, dot products, projections) and calculus (limits, series, exponentials, Newton's method), plus complex numbers with Euler's formula. They have not studied bilinear forms over finite fields, tensor products, ring theory beyond the integers mod n, Fourier analysis or FFT internals, numerical error analysis, or the integer-multiplication literature after Karatsuba.

## Pages, in reading order

- `exact-multiplication-problem`: Exact binary multiplication problem: The task of reading x#y for two n-bit binary strings and writing the exact 2n-bit binary product val(x)·val(y), with lg n = max{⌈log₂ n⌉, 1}.
- `optimality-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 conjecture that n log n is the optimal order of integer multiplication cost, i.e. that every fixed multitape multiplication machine eventually needs time Ω(n lg n).
- `poly-ring`: Polynomial ring modulo yʳ + 1: The ring ℂ[y]/(yʳ+1) of complex polynomials of degree below r, r a power of two, in which yʳ = −1 so that multiplication wraps negacyclically.
- `synthetic-roots`: Synthetic roots of unity: Powers of y in ℂ[y]/(yʳ+1), such as ω_t = y^{2r/t}, which serve as roots of unity and act on a record by a signed cyclic shift of its coefficient list instead of a multiplication.
- `fft-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), the basic arithmetic step of a radix-two fast Fourier transform.
- `binary-field`: The binary field F₂ and XOR: The two-element field of bits in which addition is XOR; the bit network, binary labels and address basis changes all compute over it.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are integers divided by powers of two (the ring ℤ[i, 1/2]), which allow exact evaluation of halvings and fourth-root phases.
- `linear-network`: Linear network with wire roles: A fixed circuit of wires carrying scalars and gates applying fixed linear maps to some wires; each wire's fixed place is its role, and auxiliary scratch wires may start with arbitrary values.
- `subset-intersection-gadget`: Three-element subset intersection gadget: The construction indexing data by 3-element subsets of a 100-element set, where gather and scatter through central wires create coefficients depending on intersection size and side wires between neighboring triples cancel the unwanted ones, giving y_S ← y_S + x_S.
- `hvdh-multiplier`: Harvey–van der Hoeven multiplier: The previously established O(n log n) multitape integer multiplication algorithm, used here only as an ordinary subroutine on short records.
- `kronecker-packing`: Signed Kronecker substitution: Multiplying polynomials with signed integer coefficients by evaluating them at a large power of two, multiplying the resulting integers with an established multiplier, and reading coefficients back by centered residues.
- `scratch-restoration`: Scratch restoration schedule: An eight-row gate schedule that subtracts the effect of old scratch values, adds the source contribution, and restores the scratch wires, so the net effect is independent of their arbitrary initial contents (a linear form of transparent computation).
- `bank-exchange`: Three-stage bank exchange: The fixed network that, in three stages over the three tensor coordinates, maps two data banks (X, Y) to (−Y, X) (a plain swap over F₂) while restoring every auxiliary wire.
- `lexicographic-array-layout`: Lexicographic array layout and logical volume: Storing an array over a product of address fields as one tape stream in lexicographic order, so addresses are implicit in position, with V denoting the number of stored data bits.
- `frames`: Frames and the common-frame identity: An invertible operator D_v attached to each network vertex so the stored array is D_v applied to the logical array; because all wires at a gate share a frame, pointwise gates commute with it and the network applies only endpoint frame changes.
- `elementary-streams`: Elementary stream operations: Linear-time tape scans that permute or move a single fixed-radix digit of the address, split and merge streams on a digit, and split whole rows cyclically into a fixed number of streams.
- `row-splitting`: Row splitting among wire roles: Distributing whole rows of an array cyclically among the W network roles (padding the row count), so every role stream has the same address set and volume V/W and gates act pointwise on matching addresses.
- `controlled-shifts`: Controlled cyclic shifts: Linear-time updates y ↦ y + a(controls) mod Q (and fixed rational scalings) of an address field whose offset depends only on earlier address fields.
- `matrix-rank`: Matrix rank: The dimension of the image of a matrix (here over the rationals), which counts how many independent directions a linear map actually changes.
- `bruhat-factorization`: Lower-triangular Bruhat factorization: Writing any rational matrix of rank a as E₁ΠE₂ with invertible lower-triangular E₁, E₂ and a partial permutation Π with exactly a ones.
- `bilinear-forms`: Nondegenerate bilinear spaces and orthogonal complements: A vector space with a symmetric bilinear form ⟨·,·⟩ such that no nonzero vector is orthogonal to everything; each nondegenerate subspace U then splits the space as U ⊥ U^⊥.
- `tensor-product`: Tensor product of linear maps: The operator A ⊗ B acting on multi-indexed arrays by applying A along one coordinate and B along another, used for multidimensional transforms and for butterflies on many address bits at once.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nondegenerate subspaces of a fixed m-dimensional bilinear space attached to the gates and terminals so labels on each edge are nested; the orthogonal residual's dimension counts the smaller operations that edge needs.
- `rank-saving`: Rank saving s < Wm: The decisive inequality that the total number s of smaller recursive calls (summed residual dimensions or ranks) in the network is less than the number of wires W times the label dimension m, which yields the power saving.
- `address-shear`: Address shear: The address permutation (H, D) ↦ (H + MD, D) on two groups of address fields; the bit network's endpoint frames make it implement the shear H ← H + D on every role, which three such updates turn into an interchange.
- `matrix-shear-cost`: Matrix shear by interchanges: Performing an address shear by a rank-a matrix with exactly a smaller field interchanges plus linear work, using the triangular factors as controlled shifts.
- `depth-first-schedule`: Fixed-tape depth-first recursion schedule: Running the recursive calls one at a time while parking the inactive role streams on a stack tape, so a fixed number of tapes serves every depth and each node's overhead is linear in its own volume.
- `power-width-interchange`: Recursive power-width interchange: Interchanging two address chunks of m^k digits by running the bit network on row-split streams, each edge implemented by smaller interchanges, giving the volume-normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1).
- `chunk-swap`: Fast address-chunk interchange: A fixed multitape procedure that exchanges two disjoint contiguous address fields of u bits in O(V u^τ) time for a fixed τ < 1, using XOR combinations of data although its final effect is a permutation.
- `phase-kernel`: Phase kernel C: The 2×2 matrix C = H·diag(1, i)·H = aI + bX with a = (1+i)/2, b = (1−i)/2, from which the butterfly is recovered as H₀ = b·S·C·S with S = diag(1, i).
- `phase-frames`: Binary phase frames: Frames 𝒞_U = H^{⊗m}·diag(i^{wt(P_U x) mod 4})·H^{⊗m} attached to binary labels U, whose edge changes factor into one translation kernel per orthonormal residual vector and whose endpoints give C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: Performing XORs of one selected bit position across many K-bit address chunks at once by eight packed cyclic shifts of whole chunk ranges plus a deterministic sort-based repair of a small set of exceptional addresses.
- `disk-grid-truncation`: Disk grid and truncation: Fixed-point storage of complex values in the unit disk on the grid 2^{−p}ℤ[i], with Q_p truncating real and imaginary parts toward zero, an error below √2·2^{−p} that never increases the norm.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A procedure applying H₀ on the same bit position of up to d address chunks of an array of polynomial records at once, in O(V d^{λ′}) time for a fixed λ′ < 1, evaluated exactly and truncated once.
- `cyclic-convolution`: Cyclic convolution: The product of two arrays indexed modulo their lengths, (u∗v)_k = Σ_j u_j v_{k−j}, equivalently multiplication of polynomials modulo x^S − 1 (or modulo xᵢ^{sᵢ} − 1 on several axes).
- `radix-digit-convolution`: Radix-digit reduction to convolution: Splitting each input into radix-2^b digits turns the integer product into a convolution of short nonnegative coefficients, from which the binary product is recovered by carry propagation.
- `phase-twist`: Coefficient phase twist: Multiplying the k-th coefficient of the last cyclic axis by ζ^k with ζ = e^{πi/r}, which turns cyclic convolution of length r into multiplication modulo yʳ + 1 and is undone afterwards.
- `dft`: Normalized discrete Fourier transform: The maps (F_q u)_k = (1/q) Σ_j u_j e^{∓2πijk/q} and their tensor products over several axes, which are contractions and turn cyclic convolution into pointwise multiplication.
- `decimation-in-frequency`: Decimation-in-frequency FFT and bit-reversed order: The radix-two recursion that pairs z_k with z_{k+t/2} by a butterfly, multiplies one branch by a twiddle root, and recurses, leaving frequency j stored at the bit-reversed slot rev(j).
- `synthetic-transform`: Synthetic polynomial transform: The Nussbaumer–Quandalle Fourier transform over ℂ[y]/(yʳ+1) using synthetic roots, computed by radix-two butterflies and signed shifts, with a forward version and an opposite version that consumes its bit-reversed output order.
- `transform-layout`: Synthetic transform tape layout: A layout permutation that places the bits of all transform axes at common offsets in consecutive K-bit chunks so each round of the synthetic transform is one simultaneous butterfly layer plus a recordwise twiddle shift.
- `contraction-error`: Contractions and error accounting: Bookkeeping in which every exact step is a norm-nonincreasing linear (or bilinear) map, so computed approximations compose by simply adding their errors.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of power-of-two length t > s, sandwiched between contractions built from Gaussian kernels, with a scale factor 2^{2α²}.
- `synthetic-convolution`: Convolution over the polynomial ring: Normalized cyclic convolution of arrays of ℂ[y]/(yʳ+1) records computed by two forward synthetic transforms kept in their stored order, packed pointwise polynomial products, and one opposite transform.
- `retained-permutations`: Retained source and target permutations: Keeping the coordinate permutations of Gaussian resampling inside the transform identity instead of sorting, since the target permutation is absorbed by the chirp step and the source permutation cancels in the convolution.
- `bluestein-chirp`: Bluestein chirp identity: The identity writing a Fourier transform (here including its frequency permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `exact-recovery`: Exact coefficient recovery: Undoing the known scalings, showing the computed convolution coefficients are within 1/2 of the true integers, rounding them, and propagating carries to obtain the exact binary product.
- `prime-axis-lengths`: Distinct prime axis lengths: Choosing distinct odd primes sᵢ slightly below the power-of-two axis lengths tᵢ, so the source axes are pairwise coprime and each ratio tᵢ/sᵢ leaves room for resampling.
- `crt-address-map`: Chinese-remainder address map: The isomorphism x ↦ ∏ xᵢ^{μᵢ} from one cyclic convolution of length S = ∏ sᵢ to a multidimensional cyclic convolution on the prime axes, implemented on tape by triangular controlled shifts and axis moves.
- `parameter-cost-table`: Parameter choice and cost table: The fixed rational exponents and size parameters (b, p, d, K, r, ℓ) for which every normalized cost term is at most p^{1−2κ}, so the total time is O(n (lg n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `logarithms`: Logarithms
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `two-s-complement`: Two's complement
- `fixed-point-binary-numbers`: Fixed-point binary numbers
- `schoolbook-binary-arithmetic-and-carry-propagation`: Schoolbook binary arithmetic and carry propagation
- `integer-division-with-remainder`: Integer division with remainder
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-the-extended-euclidean-algorithm`: Greatest common divisor and the extended Euclidean algorithm
- `prime-numbers`: Prime numbers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `sets-cartesian-products-and-indicator-vectors`: Sets, Cartesian products and indicator vectors
- `binomial-coefficients`: Binomial coefficients
- `permutations-and-bijections`: Permutations and bijections
- `mathematical-induction`: Mathematical induction
- `directed-graphs`: Directed graphs
- `worst-case-running-time`: Worst-case running time
- `ram-model-of-computation`: RAM model of computation
- `recurrence-relations-and-divide-and-conquer`: Recurrence relations and divide and conquer
- `geometric-series`: Geometric series
- `karatsuba-multiplication`: Karatsuba multiplication
- `polynomial-evaluation-and-interpolation`: Polynomial evaluation and interpolation
- `sorting`: Sorting
- `stacks`: Stacks
- `binary-counters`: Binary counters
- `matrix-transposition-and-row-major-order`: Matrix transposition and row-major order
- `vector-spaces-subspaces-and-dimension`: Vector spaces, subspaces and dimension
- `matrices-and-linear-maps`: Matrices and linear maps
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices
- `eigenvalues`: Eigenvalues
- `dot-product-and-orthonormal-bases`: Dot product and orthonormal bases
- `projections-onto-subspaces`: Projections onto subspaces
- `direct-sums`: Direct sums
- `hamming-weight`: Hamming weight
- `euler-s-formula-and-the-complex-exponential`: Euler's formula and the complex exponential
- `exponential-function-and-gaussian-function`: Exponential function and Gaussian function
- `limits-and-convergent-series`: Limits and convergent series
- `triangle-inequality`: Triangle inequality
- `newton-s-method`: Newton's method

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
