# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/B5` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of running time.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients, added and multiplied.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1, with modulus, conjugate and roots of unity.
- `multitape-tm`: Multitape Turing machine (known to the reader): A finite-alphabet machine with several one-dimensional tapes whose heads move one cell per step.
- `nlogn-conjecture`: The n log n conjecture and its history: Schönhage and Strassen conjectured n log n is the optimal multiplication cost on multitape Turing machines; Harvey and van der Hoeven reached O(n log n), which also serves here as an ordinary subroutine multiplier.
- `array-layout`: Arrays on tape, address fields and volume: An array indexed by a product of ranges is stored in lexicographic order on a tape, so address fields, chunks, rows and the bit volume V are positions in the tape stream.
- `stream-ops`: Elementary stream operations: Splitting an array into streams by a digit or by cyclic rows, applying a pointwise map, and merging, all in O(V) tape steps.
- `controlled-shifts`: Controlled shifts and rational scalings: A target field can be cyclically shifted or multiplied by a unit modulo q^b by an offset computed from earlier fields in linear time.
- `linear-algebra`: Rank, subspaces and orthogonal complements: Matrix rank, subspaces, a bilinear form, orthogonal complement and projection, over the rationals and over the two-element field F2.
- `convolution`: Cyclic convolution: The product of two coefficient lists as polynomials modulo x^S−1, so entries sum over index pairs adding to a fixed value modulo S; also done on products of several cyclic axes.
- `dft`: Discrete Fourier transform: The normalized transform F_q taking u to averages of u_j times roots of unity, which turns convolution into pointwise product.
- `butterfly`: Two-point butterfly: The basic fast-transform step replacing a pair (u,v) by their sum and difference, here H0(u,v)=((u+v)/2,(u−v)/2).
- `radix-digit-mult`: Integer product as digit convolution: Splitting each integer into radix-2^b digits turns multiplication into a convolution of short coefficients; carries are propagated afterwards.
- `scalar-network`: Bank-exchanging linear network with restored scratch: A fixed network of linear gates on scalar wires that swaps two banks X,Y (X→−Y, Y→X) using scratch wires with arbitrary initial values that are restored.
- `frames`: Frames and the common-frame invariant: Assigning an invertible operator on a wire's array at each gate lets pointwise gates commute with it, so intermediate frames cancel and only endpoint operators remain.
- `labels`: Subspace labels from triple indicator vectors: Nested nondegenerate subspaces built from three-element subsets of a fixed set, attached to gates so each edge's frame change costs its residual dimension.
- `rank-deficit`: Rank deficit and the recursive power saving: The edge residual dimensions sum to s<Wm, so a recursive call on m times more parameter uses s calls on 1/W of the volume, giving cost exponent below 1.
- `bit-interface`: Bit network and rational shear interface: The XOR network with rational matrices at gates whose endpoint difference is the identity, yielding the same shear H←H+D on every role.
- `phase-interface`: Phase frames and the kernel C=aI+bX: The Gaussian-dyadic network whose frame changes are products of translation kernels aI+bX_v, ending in C⊗m on every role.
- `bruhat`: Lower triangular factorization: Any rational matrix of rank a equals E1·Π·E2 with E1,E2 invertible lower triangular and Π a partial permutation with a ones.
- `matrix-shear`: Cost of a rational matrix shear: The map (H,D)→(H+AD,D) over Z/q^b needs exactly rank(A) interchanges of b-digit fields plus O(V) work.
- `power-interchange`: Power-width chunk interchange: Recursively interchanging two address chunks of m^k digits by running the bit network on W role streams, with cost recurrence F_k ≤ (s/W)F_{k−1}+O(1).
- `chunk-swap`: Fast interchange of address chunks: Swapping two disjoint address chunks of u bits in O(V u^τ) tape time for a fixed τ<1, by padding to power widths and base-m pieces.
- `packed-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks at once, using a third chunk as restored scratch, with exceptional addresses repaired by sorting.
- `synthetic-ring`: Polynomial ring modulo y^r+1: Complex polynomials of degree below r with y^r=−1, where multiplying by a power of y is a signed shift of coefficients and serves as a root of unity.
- `synthetic-transform`: Synthetic polynomial transform: The transform F_t with root ω_t=y^{2r/t} in the ring modulo y^r+1, a contraction whose root multiplications are signed shifts.
- `butterfly-layer`: Simultaneous butterfly layer: Applying H0 to the same bit of up to d address chunks at once, using the phase network and packed bit additions, at cost O(V d^λ′) with one final truncation.
- `transform-layout`: Transform layout and cost: Placing selected bits of all axes at a common offset in consecutive chunks so butterfly layers apply round by round, and bounding the whole synthetic transform.
- `signed-packing`: Signed packing for ring products: Kronecker substitution evaluating polynomial coefficients at a power of two to multiply ring elements with an ordinary O(N log N) integer multiplier.
- `synthetic-convolution`: Convolution from retained transform layout: Convolution over the ring: two forward synthetic transforms, pointwise ring products, and the opposite transform, keeping the same frequency order throughout.
- `crt-map`: Chinese-remainder address map: An isomorphism of cyclic convolution on S=∏s_i points onto a product of pairwise coprime cyclic axes, implemented by triangular controlled shifts.
- `fixed-point-errors`: Fixed-point error control: Complex values on a grid of spacing 2^{-p} in the unit disk, linear contractions that do not enlarge error, truncation, and additive error bookkeeping.
- `resampling`: Gaussian resampling: Gaussian-weighted contractions A and B0 that relate a Fourier transform of length s to one of length t slightly larger, with the two coordinate permutations kept inside the identity.
- `tensor-resampling`: Multidimensional resampling: The tensor product of the one-dimensional resampling identities over d axes, applied one line at a time, with axis movement done by chunk interchange.
- `chirp`: Bluestein chirp and permutation cancellation: A chirp identity turns the permuted middle transform into a cyclic convolution with pointwise phases, and the source permutation cancels between forward transforms and the opposite one.
- `coefficient-twist`: Coefficient phase twist: Mapping x_d to ζy, ζ=e^{πi/r}, turns cyclic wrap of the last axis into the negative wrap of the ring modulo y^r+1.
- `parameters-cost`: Parameter choices and cost table: Choice p=6b, d≈b^ε, K≈d^c and the rational exponents, with a cost table whose every normalized term is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)): A deterministic fixed-tape machine multiplies n-bit integers by digit convolution, CRT axes, resampling, chirps, twisting, synthetic convolution and rounding, disproving the n log n conjecture.

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
