# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/G5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has a standard undergraduate computer science education: discrete mathematics (induction, sums, logarithms, floor and ceiling, functions and bijections, graphs and acyclic circuits), algorithms (divide and conquer, recurrences, sorting in O(n log n), grade-school multiplication and Karatsuba, Newton's method from calculus), and the basic theory of computation with Turing machines and tapes. They know complex numbers, roots of unity, polynomial arithmetic, modular arithmetic and elementary linear algebra, and have seen the FFT as an algorithm. They have not studied abstract algebra beyond modular arithmetic, number theory beyond gcd and inverses, numerical analysis of rounding errors, or any multiplication algorithm beyond the basic ones, so the wiki must explain the Fourier-transform machinery, the polynomial ring, the Harvey-van der Hoeven resampling and the linear-network constructions.

## Pages, in reading order

- `nlogn-conjecture`: Optimality conjecture for multiplication: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine, which the paper refutes.
- `convolution`: Cyclic convolution: The operation combining two coefficient arrays so that coefficient j of the result sums products of entries whose indices add to j modulo the length; it is polynomial multiplication with wraparound.
- `fixed-point-disk`: Disk-grid fixed-point arithmetic: Complex values in the unit disk stored as 2^{-p} times Gaussian-integer numerators in two's complement; layers are computed exactly in Gaussian dyadics with guard bits and then truncated toward zero by Q_p.
- `subset-gadgets`: Three-element subset gadgets: Copy, side-injection, gather and scatter maps on indicator vectors of three-element subsets whose net effect adds x_S to y_S, because central coefficients depend only on intersection sizes and side wires cancel the unwanted ones.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: The computation model: one fixed machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, whose steps move each head by at most one cell.
- `nlogn-multiplier`: Established n log n multiplier: The Harvey–van der Hoeven O(N log N) multiplication algorithm for N-bit integers, used here only as an ordinary subroutine on short inputs.
- `stream-scans`: Array order and linear-time stream scans: Arrays are stored in lexicographic address order on tape; splitting on a digit, moving a digit, applying a pointwise map and merging all cost O(V) for volume V.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A target address field can be rotated by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time.
- `bank-exchange-network`: Linear bank-exchange network with restored scratch wires: A fixed network of linear gates on wires that, using three stages of the subset gadgets, exchanges two data banks (X,Y)→(−Y,X) while restoring every auxiliary scratch wire to its arbitrary initial value.
- `frames`: Frames and the common-frame identity: An invertible linear operator D_v on each wire's address-indexed array at each vertex; because gates are pointwise and linear they commute with a common frame, so the network realizes D_out S D_in^{-1}.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Each gate and terminal carries a nondegenerate subspace of a fixed bilinear space, adjacent labels are nested, and the orthogonal residual of an edge has dimension equal to the label change, so the total rank cost is Wm − 2N + 2L.
- `bit-network-interface`: Bit network and its rational matrix interface: Using XOR gates and projections P_U as frame matrices, the bit network permutes its roles and the endpoint matrices differ by the identity, so the net effect on arrays is the shear H ← H + D.
- `rank-saving`: Rank saving of the finite networks: The sum s of edge ranks is strictly less than the wire count W times the dimension m, so a recursive call on width m·f uses s calls on volume V/W each and the cost per volume grows by s/W < m, which gives the power saving.
- `matrix-factorization`: Lower-triangular factorization of a matrix: Every rational m×m matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Rank-bounded matrix shear on address fields: The permutation (H,D) ↦ (H + AD, D) of address fields over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus linear work, since triangular parts are controlled shifts.
- `power-width-interchange`: Recursive power-width interchange: For width e = m^k, a shear circuit built from the bit network turns one interchange of two e-digit chunks into s interchanges of width e/m on role streams of volume V/W, giving cost O(V e^τ).
- `address-interchange`: Fast address-chunk interchange: Exchanging two disjoint contiguous address fields of u bits in an array with product address set costs O(V u^τ) for a fixed τ < 1, although intermediate steps form XOR combinations of data.
- `packed-selected-bit-addition`: Packed selected-bit addition with repair: XORing one selected bit position of f chunks into another chunk is done by a few cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small set of addresses where guard values fail.
- `polynomial-ring`: Polynomial ring modulo yʳ + 1: Complex polynomials of degree below r with y^r = −1, so that multiplying by a power of y is a signed shift of the coefficient list; powers of y serve as roots of unity.
- `coefficient-twist`: Phase twist to a negacyclic wrap: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns convolution modulo x^r − 1 into convolution modulo y^r + 1 on the last axis, and untwisting restores the cyclic wrap.
- `signed-packing`: Signed Kronecker packing of polynomial products: Ring elements are evaluated at B₀ = 2^{4p} as signed integers, multiplied with the established multiplier, and unpacked by centered residues and carries, giving exact polynomial products.
- `dft`: Discrete Fourier transform and convolution theorem: The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns cyclic convolution into pointwise multiplication.
- `fft-butterfly`: Radix-2 FFT butterflies: A length-t transform is computed in log t levels, each pairing entries k and k+t/2 with the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle multiplication.
- `multidimensional-transform`: Multidimensional transforms on power-of-two axes: A transform over several axes is the tensor product of one-dimensional transforms, applied axis by axis to an array indexed by a product of axis lengths.
- `chirp-identity`: Bluestein chirp identity: A phase-weighted identity that rewrites a Fourier transform, including its frequency permutation, as a cyclic convolution with a chirp array a_j = exp(−πi Σ s_i j_i²/t_i) between pointwise phase multiplications.
- `two-point-kernel`: Two-point phase kernel C: The 2×2 kernel C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X and C⁴ = I and related to the butterfly by H₀ = b S C S.
- `phase-interface`: Binary phase interface of the complex network: With Gaussian-dyadic scalars and binary labels, each edge's frame change is a product of translation kernels aI + bX_v, one per residual basis vector, and telescoping the frames yields C^{⊗m} on every role.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ'}) instead of d passes.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform whose roots of unity are powers ω_t = y^{2r/t} of the ring variable, so twiddle multiplications are exact signed shifts and only butterflies cost arithmetic.
- `stored-frequency-order`: Retained frequency order of the transforms: The forward transform writes frequency j into slot rev(j), and the opposite transform consumes exactly that bit-reversed order, so no reordering sort is needed between the two.
- `transform-layout`: Transform layout for parallel butterfly rounds: A positional address permutation moves the selected bits of all axes into common-offset consecutive K-bit chunks so each transform round is one simultaneous butterfly layer; it costs O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- `ring-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, all in one retained order, give the normalized convolution (f*g)/(rM) over the polynomial ring with explicit error.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven technique expressing a Fourier transform of prime-like length s through one of a larger power-of-two length t, using Gaussian-weighted contractions A and B₀ and two coordinate permutations.
- `retained-permutations`: Resampling with retained permutations: Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform formula R F_s = 2^γ B₀ Q F_t A; the source permutation then cancels across the two forward transforms and the opposite one.
- `radix-digit-reduction`: Reducing integer multiplication to digit convolution: Writing each integer as a polynomial in 2^b with b-bit digits turns the product into a convolution of digit lists; padding avoids wraparound, and rounding plus carry propagation recover the bits.
- `precision-recovery`: Error analysis and exact recovery of the product: Every call returns disk-grid values with bounded error and norm margins; after removing the known scales the coefficient error is below 1/2, so rounding gives the exact integer coefficients and carries give the product.
- `crt-prime-axes`: Chinese-remainder map onto distinct prime axes: A ring isomorphism sends a length-S cyclic convolution to a multidimensional cyclic convolution on pairwise coprime axes s_i; on tape it is a sequence of triangular controlled shifts.
- `parameter-regime`: Parameter regime for input length n: All sizes are tied to b = ⌈log₂ n⌉: precision p = 6b, d = ⌊b^ε⌋ axes, K = ⌊d^c⌋, padded size T about n/b, record length r = 2^{⌈log₂T/d⌉} so that Tp = Θ(n) and r grows faster than any power of p.
- `prime-lengths`: Prime source lengths near powers of two: Distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by deterministic search, so S = ∏s_i lies in (T/2, T) and each ratio t_i/s_i leaves enough separation for Gaussian resampling.
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by resampling, chirp and polynomial-ring convolution, multiplied pointwise, transformed back with the opposite sign, rescaled, rounded and carry-propagated to give the 2n-bit product.
- `time-bound`: Complete time bound and the power saving: Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.

## Concepts the reader knows

- `big-o`: Big-O notation
- `multitape-tm`: Turing machines with tapes
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `roots-of-unity`: Roots of unity
- `modular-arithmetic`: Modular arithmetic
- `binary-arithmetic`: Binary integers and XOR
- `linear-algebra`: Basic linear algebra
- `logarithms-floors-and-ceilings`: Logarithms, floors and ceilings
- `mathematical-induction-and-recurrences`: Mathematical induction and recurrences
- `sorting-and-permutation-of-arrays`: Sorting and permutation of arrays
- `schoolbook-multiplication-and-karatsuba`: Schoolbook multiplication and Karatsuba
- `fast-fourier-transform-as-an-algorithm`: Fast Fourier transform as an algorithm
- `graphs-directed-acyclic-graphs-and-circuits`: Graphs, directed acyclic graphs and circuits
- `calculus-and-newton-s-method`: Calculus and Newton's method
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `primes-and-trial-division`: Primes and trial division
- `rounding-rational-numbers-and-fixed-point-numbers`: Rounding, rational numbers and fixed-point numbers
- `worst-case-time-analysis-of-deterministic-algorithms`: Worst-case time analysis of deterministic algorithms
- `sets-cartesian-products-and-indexed-arrays`: Sets, Cartesian products and indexed arrays

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
