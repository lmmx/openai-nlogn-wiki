# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/P3` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on running time as input size grows.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1, including roots of unity e^{2πi/k}.
- `multitape-tm`: Multitape Turing machine (known to the reader): A finite-state machine with a fixed number of one-dimensional tapes, each head reading/writing one cell and moving at most one cell per step.
- `history`: Integer multiplication complexity and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n), which this paper's algorithm beats.
- `linear-algebra`: Subspaces, rank, orthogonal complements and bilinear forms: Basic linear algebra over Q or F₂: subspaces, rank of a matrix, a nondegenerate symmetric bilinear form, orthogonal complements and orthogonal direct sums.
- `stream-ops`: Arrays on tape and elementary stream operations: An array with a product address set is stored in lexicographic order on tape; splitting on a digit, merging, moving a digit and splitting whole rows cyclically into streams each cost O(V) for stored volume V.
- `controlled-shift`: Controlled cyclic shifts and fixed rational scalings: Updating a later address field y by y+a(controls) mod q^b, or multiplying it by a fixed rational unit, costs O(V) on tape by splitting each fibre in two pieces and merging them in swapped order.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q} of a length-q vector, with the opposite-sign inverse F⁺ satisfying F⁺F = I/q.
- `convolution`: Cyclic convolution and the convolution theorem: Cyclic convolution u*v multiplies polynomials modulo x^q − 1 and equals, up to normalization, the inverse transform of the pointwise product of the transforms.
- `integer-as-convolution`: Integer product as convolution of radix digits: Writing both inputs as polynomials in 2^b with b-bit digits, the product is a convolution of digit lists; padding so the degree is below the cyclic length S avoids wraparound, and coefficients stay below 2^{3b}.
- `butterfly-fft`: Butterfly (decimation-in-frequency) transform: A length-t transform is computed in log₂t levels, each pairing z_k with z_{k+t/2}, applying the two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2), a twiddle multiplication, and recursing on both halves.
- `multidim-transform`: Multidimensional transforms (tensor products): A transform on an array indexed by several axes is the tensor product of one-dimensional transforms, computed one axis at a time; convolution on the product group corresponds to pointwise product.
- `crt-map`: Chinese-remainder map to distinct prime axes: With pairwise coprime axis lengths s_i and product S, the map x ↦ ∏ x_i^{μ_i} is an isomorphism from C[x]/(x^S−1) to the multi-axis cyclic ring, converting one long cyclic convolution into a multidimensional one; on tape it is a sequence of triangular controlled shifts.
- `fixed-point`: Fixed-point complex grid and truncation: Complex numbers are stored as pairs of signed two's-complement integers scaled by 2^{-p}; the truncation Q_p rounds each part toward zero to this grid with error below √2·2^{-p}.
- `contraction-error`: Contractions and error accumulation: A linear map that does not increase the maximum coefficient norm is a contraction; errors of composed approximations add, and for a bilinear contraction the error is bounded by ‖Δf‖‖g′‖+‖f‖‖Δg‖.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s as a transform of larger power-of-two length t, sandwiched between two Gaussian-weighted contractions A and B₀ and two coordinate permutations.
- `bluestein`: Bluestein chirp identity: A transform with quadratic-phase (chirp) factors equals pointwise chirp multiplication, a cyclic convolution with the chirp array, and a second chirp multiplication.
- `retained-permutations`: Resampling with the permutations left in the transform: Instead of sorting twice per coordinate, the coordinate permutations of resampling are kept in the transform formula; the chirp absorbs the target permutation and the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.
- `ring-mod-yr`: Polynomial ring modulo yʳ + 1: The ring C[y]/(y^r+1) of polynomials of degree below a power of two r; multiplying by y^a permutes the coefficient list with sign changes, and the coefficient maximum norm is preserved.
- `synthetic-transform`: Synthetic polynomial transform: A butterfly transform over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} act as exact signed shifts of the coefficient list, so twiddle multiplications are cheap (Nussbaumer–Quandalle).
- `phase-twist`: Phase twist from cyclic to negacyclic wrap: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1), so the negative wrap of the ring gives exactly the cyclic wrap after the twist is removed.
- `signed-packing`: Signed packing (Kronecker substitution) of ring products: Polynomials with small signed coefficients are evaluated at a large power of two to give integers, multiplied by the established O(N log N) integer multiplier as a subroutine, and the product coefficients are recovered by centered residues, giving normalized ring products in O(rp log(rp)).
- `exact-recovery`: Exact recovery by rounding and carry propagation: After removing the known scales, each recovered digit-convolution coefficient has error below 1/2, so rounding gives the exact integer coefficients and radix-2^b carries give the 2n-bit product.
- `linear-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on W scalar wires that exchanges two banks of values with signs while returning every auxiliary (scratch) wire to its arbitrary initial value; each wire's fixed place is its role.
- `subset-gadget`: Three-element-subset gather/scatter gadget: Using triples of a ground set, gather and scatter create coefficients depending on intersection size, and side wires cancel the unwanted ones so that three stages realize (X,Y)↦(−Y,X) with arbitrary scratch values restored.
- `frames`: Frames: changing the representation along network edges: Each array on a wire is stored as D_v g for a vertex-dependent invertible operator D_v; since all wires at a gate share the frame and gates are pointwise linear, the whole network implements D_out S D_in^{-1}, with edge cost D_v D_u^{-1}.
- `rank-saving`: Subspace labels and the rank saving s < Wm: Attaching nested nondegenerate subspaces of an m-dimensional space to gates so that the sum s of edge-difference ranks stays strictly below W·m; this strict deficit is the source of the power saving.
- `bit-network-shear`: Bit network and the address shear: The XOR-only bit network with rational matrices M_v whose endpoint difference is the identity, so frames Φ_M (moving entry (H,D) to (H+MD,D)) make every role undergo the shear (H,D)↦(H+D,D).
- `triangular-factorization`: Lower-triangular (Bruhat) factorization: Every rational m×m matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones, matching the tape order of controlled shifts.
- `matrix-shear`: Cost of a rational matrix shear: The shear (H,D)↦(H+AD,D) for a rank-a rational matrix A is done with exactly a interchanges of b-digit fields plus O(V) work, using triangular factors and three controlled updates per pivot.
- `power-width-interchange`: Power-width chunk interchange and the recursive saving: For chunks of e=m^k digits, running the bit network on W row-split role streams, with each edge done by smaller interchanges, gives F_k ≤ (s/W)F_{k−1}+O(1); because s/W<m^τ this yields cost O(V e^τ).
- `chunk-interchange`: Chunk interchange in O(V uᵗ) time: Interchanging two disjoint u-bit address fields of an array in which all address combinations occur costs O(V u^τ) for a fixed τ<1, via XOR-style intermediate steps whose final effect is an exact permutation.
- `complex-phase-network`: Complex phase network and the C kernel: The complex version of the network with binary labels and phase frames C_U=H^{⊗m}diag(i^{wt(P_U x) mod 4})H^{⊗m}; each edge difference is a product of two-point kernels aI+bX_v, and telescoping gives C^{⊗m} on every role.
- `phase-frame-reduction`: Phase frames reduce a butterfly layer to C kernels: Since H₀=b·S·C·S with a diagonal phase S, a simultaneous layer H₀^{⊗D} equals b^D S_D C^{⊗D} S_D; the network turns C^{⊗e} on e axes into s calls on e/m axes plus binary basis changes of selected bits.
- `packed-bit-addition`: Packed addition of selected address bits: A binary row addition on corresponding selected bits of two address chunks, using a third chunk as restored scratch, is done by eight packed cyclic shifts plus deterministic repair of an exponentially small set of exceptional addresses.
- `simultaneous-layer`: Simultaneous butterfly layer in O(V d^λ′) time: Applying H₀ to the same bit position in d address chunks of polynomial records at once, exactly in Gaussian dyadics with guard bits and one final truncation, costs O(V d^{λ′}) with λ′<1 instead of d passes.
- `transform-layout`: Synthetic transform layout and retained frequency order: Selected bits of the participating axes are brought to a common offset in K-bit chunks by chunk interchanges; the forward transform leaves frequencies in bit-reversed order B_t and layout L, which the opposite transform consumes, at cost O(Tp[dK+pK^{τ−1}+ℓd^{λ′}]).
- `ring-convolution`: Normalized convolution over the ring from the retained layout: Forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform in the same stored order compute f*g/(rM) on the remaining axes over C[y]/(y^r+1) with error below √2·M(3ℓ+1)2^{-p}.
- `complex-convolution-twist`: Complex cyclic convolution via the coefficient twist: Normalized cyclic convolution on all d power-of-two axes is obtained by twisting the last coordinate into the ring, applying the ring convolution on the other axes, and untwisting.
- `source-transform`: Computed source transform: The procedure evaluating R F_s: Gaussian map A on each line, the chirp-based transform via complex convolution, Gaussian map B₀, then scaling by 2^γ, with the opposite sign obtained by complex conjugation.
- `parameters`: Parameter choices, padded box and prime source lengths: From n pick b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, a power of two T≈n/b split into d axes of length r/2 or r, and distinct primes s_i just below each t_i (found by deterministic search), with fixed rational exponents leaving positive margins.
- `multiplication-algorithm`: The multiplication algorithm: Form radix-2^b digits, apply the CRT map Φ, compute two forward source transforms, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}S, round, invert Φ, and propagate carries to output the 2n-bit product.
- `cost-accounting`: Cost table and the κ margin: Dividing costs by Tp=Θ(n), seven dominant terms have powers of p at most 1−2κ (smallest margin 2^{-181}), so every polylogarithmic loss is absorbed and the total is O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it works by fast address interchanges and fast simultaneous butterfly layers inside a Gaussian-resampling/Bluestein/synthetic-transform reduction.

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
