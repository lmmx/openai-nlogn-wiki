# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/P5` (paths below are relative to it)

Say what a specific reader already knows, for these sources. The reader profile describes the reader in a few words, and its examples do not list everything it covers: it stands for a level of study. Make it concrete for the sources.

The sources were written for readers of their own, and use without explanation what those readers know. Read the sources and find that background: the notions, notation and standard results they use without defining. For each, decide whether a reader at the profile's level has been taught it, in the profile's subject or in the subjects that subject rests on (an undergraduate degree in physics teaches linear algebra, Fourier series and probability as well as mechanics, whether or not a profile names them).

- The reader knows what their level of study teaches to everyone at that level. Do not withhold it because the profile does not name it.
- The reader does not know what is taught only in some courses, or in later or specialist study, nor what the sources introduce, define or prove: that is what the wiki explains. When unsure, count it as not known.
- The existing concepts were planned by an earlier task and stay as they are: this answer only adds background they lack.
- `summary`: the subjects and how far into each this reader has gone, as they bear on the sources. Everyone who writes or checks the wiki is shown it with the profile.
- `known`: each concept from that background that the reader knows and no existing concept covers, with the aliases a writer might use for it. Include what the sources use and what an explanation of them would naturally use. Known concepts get no page.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on a running time as a function of input size.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of an indeterminate, added and multiplied coefficientwise.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1, including roots of unity e^{2πi/k} of modulus one.
- `tape-basics`: Basic Turing machines and tapes (known to the reader): A finite-control machine reading and writing symbols on tapes with moving heads.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: The cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step touching one cell per tape, and cost counted in bit operations on n-bit inputs x#y with output the 2n-bit product.
- `nlogn-conjecture`: The n log n conjecture and the history of multiplication: Schönhage and Strassen's 1971 O(n log n log log n) bound with the conjecture that n log n is optimal, followed by Fürer's and others' improvements up to Harvey–van der Hoeven's unconditional O(n log n).
- `hvdh-multiplier`: Established O(n log n) multiplier as a subroutine: The previously known O(N log N) fixed-tape integer multiplier, used as an ordinary black box on short inputs, never recursively invoking the new algorithm.
- `convolution`: Cyclic convolution: The product rule f*g on a cyclic group (or product of cyclic groups), equal to polynomial multiplication modulo x^S−1.
- `dft`: Normalized discrete Fourier transform F_q: Length-q transform with entries averaged over roots of unity; it turns convolution into pointwise multiplication (F(u*v)=S·Fu·Fv) and has inverse F⁺ up to normalization.
- `butterfly`: Two-point butterfly H₀ and the radix-two recursion: The map H₀(u,v)=((u+v)/2,(u−v)/2) and its use in the decimation-in-frequency recursion that splits a length-t transform into two half-length ones after a twiddle multiplication.
- `ring-mod-yr-plus-1`: Polynomial ring modulo y^r+1: Polynomials with complex coefficients of degree < r where y^r=−1, so multiplying by a power of y permutes coefficients with sign changes (a signed shift) and y supplies roots of unity.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} are powers of y, so twiddle multiplications are signed shifts; evaluated by radix-two butterfly rounds.
- `stored-order`: Retained bit-reversed frequency order: The forward synthetic transform writes outputs in bit-reversed slots; the pointwise product and the opposite-sign transform consume that same order, so no reordering is executed.
- `fixed-point`: Fixed-point grid arrays with precision p: Complex numbers of modulus at most 1 stored as signed two's-complement integers scaled by 2^{-p}, with truncation toward zero after each completed step and error tracked as multiples of 2^{-p}.
- `dyadic-exact`: Exact Gaussian dyadic evaluation of a layer: Intermediate values of a butterfly layer are Gaussian integers over powers of two, computed exactly with enough guard bits, with a single truncation at the end.
- `streams`: Array streams, address fields and elementary scans: Arrays are stored in lexicographic address order on tapes with logical volume V bits; splitting, merging, and fixed permutations of digits cost O(V) by linear scans.
- `controlled-shifts`: Controlled shifts and fixed rational scalings: Updating a later address field by an offset computed from earlier fields, or multiplying it by a fixed unit modulo q^b, in linear time using split and merge of consecutive blocks.
- `linear-algebra`: Subspaces, rank and orthogonal complements: Vector subspaces, matrix rank, bilinear forms, orthogonal complements, projections and tensor products, over the rationals or F₂.
- `three-subset-pairing`: Triple indicator vectors and intersection pairings: Indicator vectors of three-element subsets of a 100-element set, whose bilinear pairings give |S∩T| mod 2 over F₂ or |S∩T|−1 over Q, making neighboring triples orthogonal.
- `scalar-exchange-network`: Scalar exchange network with restored scratch wires: A fixed linear network of gates (copy, gather, scatter, side injection) acting on banks X,Y and scratch wires, which sends (X,Y) to (−Y,X) in three stages and restores arbitrary initial scratch values.
- `frames`: Frames and the common-frame identity: Assigning an invertible operator D_v to each vertex so that stored arrays are D_v applied to logical arrays; pointwise gates commute with the common frame, so the network implements D_out S D_in^{-1} with only edge changes D_v D_u^{-1} to pay for.
- `subspace-labels`: Subspace labels and the rank saving s<Wm: Nested nondegenerate subspaces of an m-dimensional space attached to gates and terminals so the total rank of edge changes satisfies s<Wm.
- `bit-network`: Bit network and its shear interface: The F₂ network with W_b wires and rational labels whose endpoint matrices differ by the identity on every input role, giving the address shear H←H+D with s_b<W_b·m.
- `lower-triangular-factorization`: Lower-triangular factorization of a matrix: Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ lower triangular and Π a partial permutation with a ones.
- `address-shear`: Address shear costing rank-many interchanges: The permutation (H,D)↦(H+AD,D) of address fields mod q^b is done with exactly rank(A) field interchanges plus linear work, using triangular factors and controlled shifts.
- `power-saving-recursion`: Power saving from a rank-deficit recursion: Because the network makes s<Wm calls on streams of volume V/W, the per-volume cost recurrence F_k ≤ (s/W)F_{k−1}+O(1) with s/W<m^τ gives cost O(e^τ) at width e=m^k, with depth-first scheduling on fixed tapes.
- `chunk-interchange`: Address-chunk interchange in O(Vu^τ) time: Exchanging two disjoint contiguous u-bit address fields of an array of volume V by XOR combinations of intermediate data, in time O(V u^τ) for a fixed τ<1; the final effect is an exact permutation.
- `phase-frames`: Binary phase frames and the two-point kernel C: The complex network with binary labels, frames given by Hadamard-conjugated phases i^{wt(P_U x)}, so each edge is a product of translation kernels aI+bX_v and the endpoints give C⊗…⊗C on every role, where C=H·diag(1,i)·H and H₀=b·S·C·S.
- `packed-selected-bits`: Packed selected-bit addition: Adding corresponding selected bits of address chunks (a binary row addition) via a constant number of whole-chunk cyclic shifts, then repairing an explicitly bounded exceptional set of addresses.
- `simultaneous-layer`: Simultaneous butterfly layer in O(Vd^λ') time: Applying H₀ to the same bit position of D≤d address chunks of a polynomial array at once, via the phase network and recursion on e=mf axes, in time O(V d^λ') instead of D passes.
- `transform-layout`: Synthetic transform layout and cost: Placing the selected bits of participating axes at a common offset in K-bit chunks so that each synthetic transform round uses the simultaneous layer, with total cost O(Tp[dK+pK^{τ−1}+ℓd^{λ'}]).
- `signed-packing`: Signed packing of polynomial products: Evaluating polynomials at 2^{4p} (a signed Kronecker substitution) so one product in the ring is four integer products by the established multiplier, then reading centered coefficients back.
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms, a pointwise ring product by signed packing, and the opposite transform give normalized convolution over C[y]/(y^r+1) with error about 3ℓ·M·2^{-p}.
- `digit-convolution`: Multiplication as radix-digit convolution: Writing both inputs in radix 2^b with q=⌈n/b⌉ digits, the product coefficients are a convolution with capacity below 2^{3b}, and padding to length S avoids wraparound.
- `crt-cyclic-axes`: Chinese-remainder map to prime cyclic axes: Using pairwise coprime lengths s_i, a length-S cyclic convolution becomes convolution on a product of cyclic axes through the map x↦∏x_i^{μ_i}, realized by triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of prime-related length s through a power-of-two length t≥s transform via Gaussian-weighted contractions A and B₀, with a small error N−I.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another phase multiplication.
- `retained-permutations`: Retaining resampling permutations in the transform: The coordinate permutations of resampling stay inside the transform formula, so the chirp absorbs the target permutation and the source permutation cancels across two forward transforms, a pointwise product and the opposite transform.
- `phase-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1) so negative wrap becomes cyclic wrap.
- `size-parameters`: Size parameters and prime source lengths: Choice b=⌈log₂n⌉, p=6b, d≈b^ε, K≈d^c, T≈n/b a power of two, axis lengths r/2 or r, and distinct odd primes s_i just below t_i, so that Tp=Θ(n) and r outgrows every power of p.
- `exact-recovery`: Exact recovery by rounding and carry propagation: Undoing known scales S and 2^{2b+4}, showing the coefficient error is below 1/2, rounding to integers, and propagating radix-2^b carries to obtain the exact 2n-bit product.
- `multiplication-algorithm`: The assembled multiplication algorithm: Digits are placed on prime axes by the CRT map, two source transforms (Gaussian resampling with chirp convolution over the ring via twist, using synthetic convolution) and one opposite transform give the digit convolution, then rescale, round and carry.
- `cost-accounting`: Cost accounting and the exponent κ: Dividing each term by Tp gives powers of p with margins g_i below one; the smallest margin is 2κ with κ=2^{-182}, absorbing any polylog factor.
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: A deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "KnownConcept": {
      "additionalProperties": false,
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations for it, in the sources or in standard texts.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what it is.",
          "type": "string"
        },
        "name": {
          "description": "Display name in plain text, e.g. \"Fourier series\".",
          "type": "string"
        }
      },
      "required": [
        "name",
        "aliases",
        "gloss"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "known": {
      "description": "Concepts the reader knows that the sources rely on and no existing concept covers.",
      "items": {
        "$ref": "#/$defs/KnownConcept"
      },
      "type": "array"
    },
    "summary": {
      "description": "Two to four sentences: the subjects this reader has studied that bear on the sources,\nand how far into each.",
      "type": "string"
    }
  },
  "required": [
    "summary",
    "known"
  ],
  "title": "BackgroundAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0002-background.answer.json`, then run `exegenius submit 0002-background` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
