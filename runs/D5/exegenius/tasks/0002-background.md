# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/D5` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time.
- `polynomials`: Polynomials (known to the reader): Polynomials, their coefficients, multiplication and reduction modulo a polynomial.
- `complex-numbers`: Complex numbers (known to the reader): Complex arithmetic, roots of unity and the unit circle.
- `basic-turing-machines`: Turing machines and tapes (known to the reader): Basic Turing machines with tapes, heads and steps.
- `multitape-model`: Fixed multitape Turing machine model: The computation model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading/writing one cell per tape and moving each head by at most one cell; time is the number of steps.
- `nlogn-conjecture`: Multiplication history and the n log n conjecture: Schönhage–Strassen's O(n log n log log n) multiplier, their conjecture that n log n is optimal, and the Harvey–van der Hoeven O(n log n) algorithm that the paper beats by a power of log n.
- `convolution-dft`: Convolution and the discrete Fourier transform: Cyclic convolution of coefficient lists, and the DFT that turns it into pointwise multiplication; the inverse transform uses the opposite-sign root and a 1/size normalization.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Splitting each n-bit operand into short radix-2^b digits turns integer multiplication into a convolution of small integer coefficient lists, followed by rounding and carry propagation to get the exact binary product.
- `fft-butterfly`: FFT butterflies: A two-point butterfly combines two values u,v into (u+v)/2 and (u-v)/2; an FFT is built from layers of these acting on address bits, one layer per level, so scanning the array at each level costs n log n.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with multiplication reduced by y^r = −1; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style Fourier transforms over the negacyclic ring in which roots of unity are powers of y, so multiplications by roots are signed shifts and only butterflies and shifts remain; forward transforms keep the same frequency order and the opposite transform consumes it.
- `multidimensional-transform`: Multidimensional transforms with tensor structure: A transform on an array indexed by several axes is the tensor product of one-dimensional transforms along each axis; the paper uses d axes of power-of-two length.
- `crt-address-map`: Chinese-remainder coefficient address map: Map Φ placing the radix-digit coefficient list on a product of pairwise-coprime cyclic axes by the Chinese remainder theorem so that convolution is preserved, implemented by triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime-ish length s through a transform of power-of-two-axis length t via contractive Gaussian maps A and B; the paper keeps the source and target coordinate permutations inside the identity instead of sorting.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a Fourier transform (with its permutation) as a pointwise chirp multiplication around a cyclic convolution, and permutations cancel across the two forward transforms and the inverse.
- `coefficient-twist`: Phase twist from cyclic to negacyclic: Twisting coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution of length r to the ring modulo y^r+1, whose negative wrap restores the cyclic wrap.
- `signed-packing-products`: Signed packing of polynomial products: Kronecker-substitution style packing of ring elements with Gaussian-integer coefficients into long integers, multiplied by the established O(n log n) multiplier used as an ordinary subroutine.
- `fixed-point-precision`: Dyadic fixed-point arithmetic and rounding: Complex coefficients stored as fixed-point Gaussian dyadics with p fractional bits; exact intermediate values, a single truncation after contractive layers, and error tracking so the final coefficient error is below 1/2.
- `stream-scans`: Array order and elementary stream operations: Arrays are stored in lexicographic order with implicit addresses; splitting by digits, moving a digit, and splitting rows among roles are linear-time scans.
- `controlled-shifts`: Controlled shifts and rational scalings: Updating a later address field by an offset computed from earlier control fields, or multiplying it by a rational unit mod q^b, in linear time using whole-block splits and merges.
- `linear-network-frames`: Linear networks with frames: A fixed network of pointwise linear gates on wires (roles); giving each vertex an invertible frame operator D_v acting on address-indexed arrays lets gates stay pointwise while edges apply D_v D_u^{-1}, leaving an endpoint operator on every role.
- `subset-subspace-networks`: Finite networks from three-element subsets: Two fixed networks (a bit network over Q and a complex Gaussian-dyadic one over F_2) with nested subspace labels built from triples of [h], whose edge rank changes sum to s < Wm; this strict deficit is the source of the power saving.
- `recursive-saving`: Recursive power saving: A call at parameter mf uses s < Wm calls at parameter f on streams of volume V/W, so the per-volume cost grows by a factor s/W < m when the parameter is multiplied by m, giving cost V·e^τ with τ<1.
- `lower-triangular-shear`: Lower triangular factorization and matrix shear: Every rational matrix factors as E1·Π·E2 with E1,E2 lower triangular, so a coordinate change on address fields is a sequence of controlled shifts in tape order and costs O(V) times a rank-dependent number of smaller operations.
- `address-interchange`: Fast address-field interchange: Interchange of two disjoint contiguous address fields of u digits in time O(V u^τ) with a fixed τ<1, via XOR combinations of intermediate streams that finally give an exact permutation for arbitrary auxiliary values.
- `simultaneous-butterfly-layer`: Fast simultaneous butterfly layer: Applying the H_0 butterfly on the same bit position of d address chunks at once, using phase frames, binary changes of basis by chunk moves and the recursive saving, in time O(V d^λ') instead of d whole-array passes.
- `transform-layout-cost`: Synthetic transform layout and convolution cost: Arranging the array so the simultaneous layers apply with frequency order retained, giving a convolution over the ring from two forward transforms, a pointwise product (via signed packing) and an opposite transform at cost O(Tp[dK+pK^{τ-1}+ℓd^{λ'}+log(rp)]).
- `resampling-no-sort`: Resampling without executing the permutations: Lemma stating P_sF_s = 2^{2α²} B_0 P_tF_t A with coordinate permutations kept in the identity and tensored over d axes, so no full sorts are needed.
- `parameter-choice-cost`: Parameter choice and total cost accounting: Choosing b=⌈log n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log T/d⌉} and fixed rational exponents with κ=2^{-182}, then summing the normalized cost table, every row of which is a power of p below 1.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it chains CRT map, Gaussian resampling, chirps, twist and synthetic transforms accelerated by the fast interchange and butterfly layers.
- `scalar-motif-schedule`: Gather–scatter schedule with restored scratch: Eight-row schedule of pointwise gates (subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy) that adds a source into a target for arbitrary initial scratch values and restores them; three such invocations exchange banks X,Y up to sign.
- `rank-budget-labels`: Subspace labels and rank budget: Assigning nested nondegenerate subspaces to gates so that only the central-wire edges from time 3 to 4 decrease dimension (by h), giving a total dimension change Wm-2N+2L below Wm.
- `bit-network-interface`: Bit network interface: The bit network (pointwise XOR gates, rational matrices) sends its input to a permutation with endpoint matrices differing by identity and total rational rank s_b < W_b m.
- `complex-network-interface`: Complex phase network interface: The complex network edges are products of translation kernels aI+bX_v, one per basis vector of the edge residual, with total length s_c < W_c m; telescoping gives C tensor m on every role.
- `phase-frames`: Phase frames for butterfly layers: With C = HSH = aI + bX (a=(1+i)/2, b=(1-i)/2) one has H_0 = b S C S, C^2 = X, C^4 = I, so a simultaneous butterfly layer is a scalar times S C^{⊗D} S, and C^{⊗D} is implemented by smaller groups via the complex network.
- `packed-selected-bit-addition`: Packed selected-bit addition: Linear-time XOR/addition of the bit at a common offset of several address chunks on rectangle or grouped-stream layouts, used to change selected address bits; exceptional addresses are repaired by sorting.
- `synthetic-character-cancellation`: Synthetic character cancellation and inversion: The sum of ω_t^{jk} over k is t if t divides j and 0 otherwise, hence F_t^+ F_t^- = t^{-1} I; the decimation-in-frequency recursion for the transform follows.

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
