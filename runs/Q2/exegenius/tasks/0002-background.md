# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/Q2` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic notation O(·), Ω(·), o(·) describing growth rates of running times up to constant factors.
- `polynomials`: Polynomials (known to the reader): Finite sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with real a, b and i² = −1, including modulus and roots of unity.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each read and written by a head moving at most one cell per step.
- `exact-multiplication-problem`: Exact binary multiplication problem: The task of reading x#y for two n-bit binary strings and writing the exact 2n-bit binary product val(x)·val(y), with lg n = max{⌈log₂ n⌉, 1}.
- `optimality-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 conjecture that n log n is the optimal order of integer multiplication cost, i.e. that every fixed multitape multiplication machine eventually needs time Ω(n lg n).
- `hvdh-multiplier`: Harvey–van der Hoeven multiplier: The previously established O(n log n) multitape integer multiplication algorithm, used here only as an ordinary subroutine on short records.
- `cyclic-convolution`: Cyclic convolution: The product of two arrays indexed modulo their lengths, (u∗v)_k = Σ_j u_j v_{k−j}, equivalently multiplication of polynomials modulo x^S − 1 (or modulo xᵢ^{sᵢ} − 1 on several axes).
- `radix-digit-convolution`: Radix-digit reduction to convolution: Splitting each input into radix-2^b digits turns the integer product into a convolution of short nonnegative coefficients, from which the binary product is recovered by carry propagation.
- `matrix-rank`: Matrix rank: The dimension of the image of a matrix (here over the rationals), which counts how many independent directions a linear map actually changes.
- `tensor-product`: Tensor product of linear maps: The operator A ⊗ B acting on multi-indexed arrays by applying A along one coordinate and B along another, used for multidimensional transforms and for butterflies on many address bits at once.
- `binary-field`: The binary field F₂ and XOR: The two-element field of bits in which addition is XOR; the bit network, binary labels and address basis changes all compute over it.
- `bilinear-forms`: Nondegenerate bilinear spaces and orthogonal complements: A vector space with a symmetric bilinear form ⟨·,·⟩ such that no nonzero vector is orthogonal to everything; each nondegenerate subspace U then splits the space as U ⊥ U^⊥.
- `dft`: Normalized discrete Fourier transform: The maps (F_q u)_k = (1/q) Σ_j u_j e^{∓2πijk/q} and their tensor products over several axes, which are contractions and turn cyclic convolution into pointwise multiplication.
- `fft-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), the basic arithmetic step of a radix-two fast Fourier transform.
- `decimation-in-frequency`: Decimation-in-frequency FFT and bit-reversed order: The radix-two recursion that pairs z_k with z_{k+t/2} by a butterfly, multiplies one branch by a twiddle root, and recurses, leaving frequency j stored at the bit-reversed slot rev(j).
- `poly-ring`: Polynomial ring modulo yʳ + 1: The ring ℂ[y]/(yʳ+1) of complex polynomials of degree below r, r a power of two, in which yʳ = −1 so that multiplication wraps negacyclically.
- `synthetic-roots`: Synthetic roots of unity: Powers of y in ℂ[y]/(yʳ+1), such as ω_t = y^{2r/t}, which serve as roots of unity and act on a record by a signed cyclic shift of its coefficient list instead of a multiplication.
- `synthetic-transform`: Synthetic polynomial transform: The Nussbaumer–Quandalle Fourier transform over ℂ[y]/(yʳ+1) using synthetic roots, computed by radix-two butterflies and signed shifts, with a forward version and an opposite version that consumes its bit-reversed output order.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are integers divided by powers of two (the ring ℤ[i, 1/2]), which allow exact evaluation of halvings and fourth-root phases.
- `disk-grid-truncation`: Disk grid and truncation: Fixed-point storage of complex values in the unit disk on the grid 2^{−p}ℤ[i], with Q_p truncating real and imaginary parts toward zero, an error below √2·2^{−p} that never increases the norm.
- `contraction-error`: Contractions and error accounting: Bookkeeping in which every exact step is a norm-nonincreasing linear (or bilinear) map, so computed approximations compose by simply adding their errors.
- `kronecker-packing`: Signed Kronecker substitution: Multiplying polynomials with signed integer coefficients by evaluating them at a large power of two, multiplying the resulting integers with an established multiplier, and reading coefficients back by centered residues.
- `lexicographic-array-layout`: Lexicographic array layout and logical volume: Storing an array over a product of address fields as one tape stream in lexicographic order, so addresses are implicit in position, with V denoting the number of stored data bits.
- `elementary-streams`: Elementary stream operations: Linear-time tape scans that permute or move a single fixed-radix digit of the address, split and merge streams on a digit, and split whole rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled cyclic shifts: Linear-time updates y ↦ y + a(controls) mod Q (and fixed rational scalings) of an address field whose offset depends only on earlier address fields.
- `linear-network`: Linear network with wire roles: A fixed circuit of wires carrying scalars and gates applying fixed linear maps to some wires; each wire's fixed place is its role, and auxiliary scratch wires may start with arbitrary values.
- `scratch-restoration`: Scratch restoration schedule: An eight-row gate schedule that subtracts the effect of old scratch values, adds the source contribution, and restores the scratch wires, so the net effect is independent of their arbitrary initial contents (a linear form of transparent computation).
- `subset-intersection-gadget`: Three-element subset intersection gadget: The construction indexing data by 3-element subsets of a 100-element set, where gather and scatter through central wires create coefficients depending on intersection size and side wires between neighboring triples cancel the unwanted ones, giving y_S ← y_S + x_S.
- `bank-exchange`: Three-stage bank exchange: The fixed network that, in three stages over the three tensor coordinates, maps two data banks (X, Y) to (−Y, X) (a plain swap over F₂) while restoring every auxiliary wire.
- `frames`: Frames and the common-frame identity: An invertible operator D_v attached to each network vertex so the stored array is D_v applied to the logical array; because all wires at a gate share a frame, pointwise gates commute with it and the network applies only endpoint frame changes.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nondegenerate subspaces of a fixed m-dimensional bilinear space attached to the gates and terminals so labels on each edge are nested; the orthogonal residual's dimension counts the smaller operations that edge needs.
- `rank-saving`: Rank saving s < Wm: The decisive inequality that the total number s of smaller recursive calls (summed residual dimensions or ranks) in the network is less than the number of wires W times the label dimension m, which yields the power saving.
- `row-splitting`: Row splitting among wire roles: Distributing whole rows of an array cyclically among the W network roles (padding the row count), so every role stream has the same address set and volume V/W and gates act pointwise on matching addresses.
- `depth-first-schedule`: Fixed-tape depth-first recursion schedule: Running the recursive calls one at a time while parking the inactive role streams on a stack tape, so a fixed number of tapes serves every depth and each node's overhead is linear in its own volume.
- `address-shear`: Address shear: The address permutation (H, D) ↦ (H + MD, D) on two groups of address fields; the bit network's endpoint frames make it implement the shear H ← H + D on every role, which three such updates turn into an interchange.
- `bruhat-factorization`: Lower-triangular Bruhat factorization: Writing any rational matrix of rank a as E₁ΠE₂ with invertible lower-triangular E₁, E₂ and a partial permutation Π with exactly a ones.
- `matrix-shear-cost`: Matrix shear by interchanges: Performing an address shear by a rank-a matrix with exactly a smaller field interchanges plus linear work, using the triangular factors as controlled shifts.
- `power-width-interchange`: Recursive power-width interchange: Interchanging two address chunks of m^k digits by running the bit network on row-split streams, each edge implemented by smaller interchanges, giving the volume-normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1).
- `chunk-swap`: Fast address-chunk interchange: A fixed multitape procedure that exchanges two disjoint contiguous address fields of u bits in O(V u^τ) time for a fixed τ < 1, using XOR combinations of data although its final effect is a permutation.
- `phase-kernel`: Phase kernel C: The 2×2 matrix C = H·diag(1, i)·H = aI + bX with a = (1+i)/2, b = (1−i)/2, from which the butterfly is recovered as H₀ = b·S·C·S with S = diag(1, i).
- `phase-frames`: Binary phase frames: Frames 𝒞_U = H^{⊗m}·diag(i^{wt(P_U x) mod 4})·H^{⊗m} attached to binary labels U, whose edge changes factor into one translation kernel per orthonormal residual vector and whose endpoints give C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: Performing XORs of one selected bit position across many K-bit address chunks at once by eight packed cyclic shifts of whole chunk ranges plus a deterministic sort-based repair of a small set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A procedure applying H₀ on the same bit position of up to d address chunks of an array of polynomial records at once, in O(V d^{λ′}) time for a fixed λ′ < 1, evaluated exactly and truncated once.
- `transform-layout`: Synthetic transform tape layout: A layout permutation that places the bits of all transform axes at common offsets in consecutive K-bit chunks so each round of the synthetic transform is one simultaneous butterfly layer plus a recordwise twiddle shift.
- `synthetic-convolution`: Convolution over the polynomial ring: Normalized cyclic convolution of arrays of ℂ[y]/(yʳ+1) records computed by two forward synthetic transforms kept in their stored order, packed pointwise polynomial products, and one opposite transform.
- `phase-twist`: Coefficient phase twist: Multiplying the k-th coefficient of the last cyclic axis by ζ^k with ζ = e^{πi/r}, which turns cyclic convolution of length r into multiplication modulo yʳ + 1 and is undone afterwards.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of power-of-two length t > s, sandwiched between contractions built from Gaussian kernels, with a scale factor 2^{2α²}.
- `retained-permutations`: Retained source and target permutations: Keeping the coordinate permutations of Gaussian resampling inside the transform identity instead of sorting, since the target permutation is absorbed by the chirp step and the source permutation cancels in the convolution.
- `bluestein-chirp`: Bluestein chirp identity: The identity writing a Fourier transform (here including its frequency permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `prime-axis-lengths`: Distinct prime axis lengths: Choosing distinct odd primes sᵢ slightly below the power-of-two axis lengths tᵢ, so the source axes are pairwise coprime and each ratio tᵢ/sᵢ leaves room for resampling.
- `crt-address-map`: Chinese-remainder address map: The isomorphism x ↦ ∏ xᵢ^{μᵢ} from one cyclic convolution of length S = ∏ sᵢ to a multidimensional cyclic convolution on the prime axes, implemented on tape by triangular controlled shifts and axis moves.
- `exact-recovery`: Exact coefficient recovery: Undoing the known scalings, showing the computed convolution coefficients are within 1/2 of the true integers, rounding them, and propagating carries to obtain the exact binary product.
- `parameter-cost-table`: Parameter choice and cost table: The fixed rational exponents and size parameters (b, p, d, K, r, ℓ) for which every normalized cost term is at most p^{1−2κ}, so the total time is O(n (lg n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.

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
