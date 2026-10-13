# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/D2` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients, and their products.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with modulus, conjugates and roots of unity.
- `multitape-tm`: Turing machines and tapes (known to the reader): Basic Turing machines with tapes and heads.
- `roots-of-unity`: Roots of unity (known to the reader): Complex numbers whose powers return to 1, such as e^{2πi/q}.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's 1971 multiplication bound O(n log n log log n) and their conjecture that n log n is optimal; later work (Fürer, Harvey–van der Hoeven) reached O(n log n) unconditionally.
- `fixed-tape-model`: Fixed-tape machine model and cost of scans: One fixed finite alphabet and a fixed finite number of one-dimensional tapes; one step touches one cell per tape, so rearranging growing fields costs real time.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time tape scans: swapping or moving a digit, splitting into streams and merging, and updating a field by an offset computed from earlier fields.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q}; a contraction in the max norm.
- `convolution`: Cyclic convolution: Convolution of arrays on a product of cyclic groups; the transform turns it into a pointwise product, so convolutions are computed by transform, multiply, inverse transform.
- `butterfly`: Two-point butterfly H₀: The map H0(u,v)=((u+v)/2,(u−v)/2), the basic step of radix-2 fast transforms; a transform has about log n levels of butterfly layers.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Splitting each integer into radix-2^b digits turns the product into a convolution of short digit sequences, recovered into an integer by rounding and carry propagation.
- `harvey-hoeven-multiplier`: Established O(n log n) multiplier as a subroutine: The Harvey–van der Hoeven multitape integer multiplier with cost O(N log N), called as an ordinary subroutine on short inputs.
- `fixed-point-contraction`: Fixed-point grids, contractions and error: Values are complex numbers in the unit disk on a grid 2^-p Z[i]; maps that never grow the max norm (contractions) let truncation errors add rather than blow up.
- `ring-y-r-plus-1`: Polynomial ring modulo y^r + 1: Polynomials with complex coefficients of degree < r where y^r = −1 (negacyclic); multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring R_r using ω_t = y^{2r/t} as root of unity, so twiddle multiplications are signed shifts; its inverse pairs are exact up to a factor.
- `bluestein-chirp`: Chirp identity and permutation cancellation: Bluestein's identity rewrites the permuted transform Q F_t as a chirp multiplication, a cyclic convolution, and another chirp; the retained source permutation R cancels across two forward and one inverse transform.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of coprime (prime) length s through one of power-of-two length t via contractions A and B0, at cost O(t p^{3/2+δ} α) per line.
- `retained-permutations`: Resampling with the permutations left in the transform: Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform identity and cancel, so no separate full sorts are executed.
- `crt-prime-axes`: Chinese-remainder address map to prime cyclic axes: A convolution-preserving map Φ places the radix-digit list on a product of distinct prime cyclic axes, implemented by triangular controlled shifts and axis moves.
- `coefficient-twist`: Coefficient twist to the negacyclic ring: Scaling coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution in the last coordinate to polynomial multiplication modulo y^r+1, with the negative wrap undoing to the cyclic wrap.
- `signed-packing`: Signed packing of polynomial records: A signed Kronecker substitution packs a polynomial's coefficients into one big integer, multiplied by the O(N log N) multiplier and unpacked, giving ring multiplication in O(rp log(rp)).
- `linear-network`: Linear network with roles, frames and restored scratch: A fixed network of linear gates on wires (roles) exchanging two banks with signs, restoring every scratch value for arbitrary initial contents; applied to arrays, each wire gets an invertible frame whose change on an edge is what must be implemented.
- `transparent-restoration`: Restoring scratch values (transparent computation): The schedule subtracts old scratch contributions, performs the operation, and undoes it so arbitrary initial auxiliary values cancel.
- `triple-subspace-labels`: Three-element subsets and nested subspace labels: Indicator vectors of 3-subsets of [h] have intersection-count inner products; orthogonality gives nested nondegenerate subspaces whose dimension drops (orthogonal residuals) count the smaller operations on an edge.
- `rank-saving`: Total smaller calls below W m: In the finite network the edges need s<Wm smaller calls in total, so a recursive call at parameter m·f uses s calls at parameter f on volume V/W, whose per-volume cost grows by s/W<m, giving a power saving.
- `bruhat-shear`: Lower-triangular factorization and address shear: Every rational matrix factors as E1 Π E2 with lower triangular E1,E2 and a partial permutation of rank-many ones; so an edge matrix of rank a costs a smaller interchanges, and the shear (H,D)→(H+D,D) is done in tape order.
- `chunk-interchange`: Fast interchange of address chunks: Interchanging two equal-width address fields of u digits in an array of volume V in O(V u^τ), τ<1, via XOR-style combinations whose final effect is an exact permutation.
- `phase-frames`: Phase kernel C and complex network: The kernel C=H S H=aI+bX with C²=X and H₀=b S C S lets the complex network's frame changes be products of translation kernels on binary subspaces, over Gaussian dyadic numbers.
- `packed-bit-addition`: Packed selected-bit addition: Adding the selected bit across address chunks of many axes at once on packed records, with a small exceptional set of addresses repaired by sorting.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applies H₀ to the same bit position in d address chunks of complex fixed-point polynomial records in one pass, costing O(V d^λ') instead of d whole-array passes, with exact Gaussian dyadic intermediates and a single final truncation.
- `synthetic-convolution`: Convolution from the retained transform layout: Convolution over R_r on a multi-axis array: two forward synthetic transforms keep the same frequency order, multiply pointwise by signed packing, and the opposite transform consumes that order, using layers on a layout built from chunk swaps.
- `parameter-choice`: Parameter choice and cost table: With b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉}, every term of the normalized cost table is p^{1−margin}, so the total is O(Tp·p^{1−g}) = O(n (lg n)^{1−κ}).
- `exact-recovery`: Precision, rounding and carries: Rescaling by the known normalizations, showing the coefficient error is below 1/2, rounding to integers, and propagating radix carries yield the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm pipeline: Digits, Φ to prime axes, two source transforms via Gaussian resampling and chirp convolution, pointwise product, opposite transform, scale, round, Φ⁻¹, carry.
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^{1−κ}) with κ=2^{-182}, disproving the n log n optimality conjecture in that model.

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
