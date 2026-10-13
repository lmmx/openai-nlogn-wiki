# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/D3` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of a function.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with roots of unity and arithmetic.
- `turing-tapes`: Turing machines and tapes (known to the reader): Basic Turing machines with tapes, heads and step cost.
- `multitape-model`: Fixed multitape Turing machine model: The cost model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading/writing one cell per tape and moving heads by at most one cell.
- `convolution`: Convolution and radix-digit reduction: Multiplying integers reduces, by splitting them into radix digits, to convolving short integer coefficient lists.
- `fourier-transform`: Discrete Fourier transform: Evaluating a coefficient list at roots of unity, turning convolution into pointwise product; computed in levels of two-point butterflies.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's O(n log n log log n) bound and conjecture that n log n is optimal, later met by Harvey–van der Hoeven's O(n log n).
- `polynomial-ring-y-r-1`: Polynomial ring modulo y^r + 1: Complex polynomials in y with y^r = −1, r a power of two; powers of y act as roots of unity and multiplying by one is a signed shift of coefficients.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier transforms over the ring where roots of unity are powers of y, so multiplications by roots are signed shifts (Nussbaumer).
- `tape-address-rearrangement`: Address rearrangement cost on tapes: Moving data between address fields on tapes costs a scan per level; naive scanning gives Θ(n log n) over Θ(log n) levels.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction replacing needed Fourier transforms by multidimensional transforms with power-of-two axis lengths.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Places the radix-digit coefficient list on a product of distinct prime cyclic axes by a convolution-preserving CRT address map.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform into a cyclic convolution via chirp factors.
- `phase-twist`: Coefficient twist to the polynomial ring: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap yields the cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Packs polynomial coefficients into one long integer so a polynomial product becomes an integer product by the established O(n log n) multiplier.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs, restoring auxiliary values; frames are invertible operators changing array representation along edges and cancelling at the ends.
- `finite-network-subspaces`: Finite network via three-element subsets and nested subspaces: Subspaces of an m-dimensional space attached to gates, using three-element subsets, give a network with fewer than Wm smaller calls.
- `recursive-power-saving`: Recursive saving from s < Wm: Calls at parameter mf use s calls at parameter f on volume V/W; s/W<m strictly gives a power-saving cost.
- `address-interchange`: Fast address-field interchange: Interchanges two address fields of u bits at cost O(V u^τ), τ<1, through XOR combinations of data, with the final result an exact permutation.
- `fast-butterfly-layer`: Simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected coordinate bits of complex fixed-point arrays at cost O(V d^λ′), λ′<1.
- `precision-exact-recovery`: Precision and exact recovery: Fixed-point errors are kept strictly below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape multiplication of n-bit integers in O(n(lg n)^{1−κ}), κ=2^{-182}, disproving the n log n conjecture in this model.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time scans on tapes: digit permutations, moves, and controlled shifts/fixed rational scalings of a field using earlier control fields; arrays stored in lexicographic order with a self-delimiting integer header code.
- `scalar-motifs`: Scalar gates with restored scratch wires: In the network, a forward invocation adds x_S to y_S for arbitrary scratch contents; three stages exchange the banks (X,Y) to (−Y,X) and restore all auxiliary values.
- `motif-residuals`: Rank budget of the network labels: Edges join comparable subspace labels; total dimension change over edges equals Wm−2N+2L, giving the strict rank deficit s<Wm.
- `motif-interfaces`: Bit and complex network interfaces: The bit network (XOR gates, rational matrices) realises an address permutation with rank sum small; the complex network realises phase frames made of translation kernels and yields the H0 layer.
- `matrix-shear`: Lower triangular factorization and matrix shear: Any rational matrix of rank a factors as E1·Π·E2 with lower triangular E1,E2, so the shear (H,D)↦(H+AD,D) needs exactly a field interchanges plus linear work.
- `chunk-swap`: Power-width and arbitrary-width chunk interchange: Recurrence on parameter e=m^k gives chunk interchange in O(V e^τ); then arbitrary width u by decomposition.
- `packed-selected-bit-addition`: Packed selected-bit addition on grouped rectangles: XORs selected bits at positions ρ+iK of several chunks simultaneously by packing, repairing a small exceptional set of addresses.
- `transform-layout-cost`: Synthetic transform layout and cost: Layout of the synthetic transform over R_r with truncation Q_p, contractions, and stored frequency order retained through pointwise product; cost via simultaneous layers.
- `tensor-resampling`: Tensor resampling with retained permutations: Gaussian resampling lines combined over d axes, keeping source and target permutations inside the transform identity.
- `parameter-choice`: Fixed rational parameter choice and cost table: Choice τ=σ=1−2^{−50}, c, λ′ etc. and a cost table whose rows each fit O(p^{1−ε′}) after dividing by volume.

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
