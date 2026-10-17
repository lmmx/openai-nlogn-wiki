# exegenius task 0215-outline

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Organise the finished pages of an explanatory wiki into parts, and write its front page. The wiki explains a target result to a specific reader, one concept per page.

- Group the pages into parts that the reader works through in order, each a coherent stage of the explanation (for example: background, the main construction, the analysis). Aim for 3 to 8 parts; a small wiki may need fewer.
- Put every page in exactly one part, or in the glossary. Each page's prerequisites (listed below) must be in the glossary, the same part or an earlier one; submit rejects an outline that breaks this. Pages within a part are shown in reading order automatically, so their order in your list does not matter.
- Glossary: minor pages that define a term in a few sentences rather than explain an idea, such as a short page on a piece of terminology that one or two other pages use. They move to a glossary page, out of the reading order; links to them still work. Keep every page that explains a method, construction, result or argument in a part. Never put the target in the glossary. The word count and the number of pages using each page are listed to help.
- If the argument's main steps are listed below, base the parts on them where the prerequisites allow: a part per main step, with the pages that present its sub-steps, and background parts for the concepts the steps rely on.
- Part titles: 2 to 5 words, plain text, no numbering.
- Part intros: 2 to 4 sentences on what the part covers and why the reader needs it for what comes next. Link pages as `[Name](id.md)`.
- Overview: the front page, 150 to 350 words, for the reader described below. Say what the target result is and why it matters, then the route the wiki takes to it, part by part, naming the key ideas and linking their pages as `[Name](id.md)`. No headings.
- Write for this reader: concrete and specific, with no filler and no rhetorical flourishes. Mathematics in LaTeX ($...$). Links to anything other than the pages listed are rejected; external URLs are allowed.

## Target

Power-saving integer multiplication: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## Pages, in reading order

- `ring-y`: [Polynomial ring modulo y^r + 1](ring-y.md) — Polynomials of degree below r over the complex numbers with y^r = −1, so multiplying by a power of y is a signed shift of the coefficient list. (466 words, used by 3)
- `machine-model`: [Fixed finite-tape machine model](machine-model.md) — The computation model of the main theorem: one fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step. (351 words, used by 4)
- `conjecture`: [Schönhage–Strassen optimality conjecture](conjecture.md) — The 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine. Needs: machine-model. (412 words, used by 1)
- `fixed-point`: [Fixed-point Gaussian dyadic records](fixed-point.md) — Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid. Needs: machine-model. (460 words, used by 4)
- `exchange-network`: [Linear exchange network with restored scratch wires](exchange-network.md) — A fixed network of linear gates on wires holding values that swaps two banks with a prescribed sign while undoing the effect of arbitrary initial scratch values, built from three-element subsets. Needs: fixed-point. (685 words, used by 1)
- `array-frames`: [Frames on wire arrays](array-frames.md) — Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter. Needs: exchange-network. (413 words, used by 1)
- `convolution`: [Cyclic convolution](convolution.md) — The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}. (549 words, used by 5)
- `radix-digit-reduction`: [Multiplication as radix-digit convolution](radix-digit-reduction.md) — Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number. Needs: convolution. (400 words, used by 2)
- `phase-twist`: [Phase twist](phase-twist.md) — Multiplying coefficient k by e^{πik/r}, which converts the cyclic coordinate modulo x^r − 1 into the negacyclic ring modulo y^r + 1 and is removed afterwards. Needs: ring-y, convolution. (517 words, used by 1)
- `dft`: [Discrete Fourier transform](dft.md) — The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns convolution into pointwise multiplication. Needs: convolution. (336 words, used by 6)
- `butterfly`: [Butterflies and the fast transform](butterfly.md) — A two-point averaging/differencing step H₀(u,v) = ((u+v)/2, (u−v)/2) whose repeated use over address bits, with twiddle multiplications, computes a transform in log t layers. Needs: dft. (405 words, used by 4)
- `synthetic-transform`: [Synthetic polynomial transform](synthetic-transform.md) — A transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so every twiddle multiplication is a signed shift of a coefficient list. Needs: ring-y, dft, butterfly. (466 words, used by 2)
- `stream-ops`: [Elementary stream operations](stream-ops.md) — Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back. Needs: machine-model, butterfly. (515 words, used by 2)
- `chirp`: [Bluestein chirp identity](chirp.md) — An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase. Needs: dft, convolution. (419 words, used by 2)
- `hvdh-multiplier`: [Established O(n log n) multiplier](hvdh-multiplier.md) — The earlier Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine. Needs: machine-model, dft. (384 words, used by 1)
- `signed-packing`: [Signed packing](signed-packing.md) — A signed Kronecker substitution that evaluates polynomials with signed coefficients at 2^{4p} to form large integers, multiplies them with the O(n log n) multiplier, and recovers the product coefficients. Needs: ring-y, hvdh-multiplier. (644 words, used by 1)
- `controlled-shifts`: [Controlled shifts and rational scalings](controlled-shifts.md) — Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume. Needs: stream-ops. (614 words, used by 3)
- `matrix-shear`: [Matrix shear by triangular factorization](matrix-shear.md) — Factoring a rational matrix as A = E₁ΠE₂ with lower triangular E₁, E₂ and partial permutation Π lets the shear (H,D)→(H+AD,D) be done with exactly rank(A) field interchanges. Needs: controlled-shifts. (612 words, used by 1)
- `phase-kernel`: [Two-point kernel C](phase-kernel.md) — The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i). Needs: butterfly. (350 words, used by 1)
- `contraction-maps`: [Contractions and bilinear contractions](contraction-maps.md) — A linear map that never increases the norm of a vector, and a bilinear map whose output norm is at most the product of the input norms, so errors in the inputs do not grow beyond a controlled bound. (413 words, used by 3)
- `multidim-transform`: [Multidimensional transforms](multidim-transform.md) — A transform over several axes at once, the tensor product of one-dimensional transforms, applied to an array one axis at a time. Needs: dft, butterfly, contraction-maps. (527 words, used by 2)
- `crt-map`: [Chinese-remainder address map](crt-map.md) — An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts. Needs: convolution, multidim-transform, controlled-shifts. (601 words, used by 2)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed. Needs: dft, multidim-transform. (576 words, used by 2)
- `retained-permutations`: [Retained permutation cancellation](retained-permutations.md) — Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort. Needs: gaussian-resampling, chirp. (537 words, used by 1)
- `frequency-order`: [Retained frequency order](frequency-order.md) — The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed. Needs: synthetic-transform, contraction-maps. (634 words, used by 2)
- `precision-recovery`: [Error tracking and exact recovery](precision-recovery.md) — Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers. Needs: fixed-point, radix-digit-reduction, contraction-maps, chirp. (687 words, used by 1)
- `parameter-choice`: [Parameter and prime-length choice](parameter-choice.md) — Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold. Needs: gaussian-resampling, crt-map, fixed-point. (624 words, used by 1)
- `tensor-product-of-spaces`: [Tensor products of subspaces](tensor-product-of-spaces.md) — The space built from two spaces whose dimension is the product of their dimensions, in which operators and bilinear forms act factorwise. (438 words, used by 1)
- `subspace-labels`: [Nested subspace labels and rank deficit](subspace-labels.md) — Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m. Needs: array-frames, tensor-product-of-spaces. (768 words, used by 2)
- `rank-recurrence`: [Recursive power saving](rank-recurrence.md) — Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving. Needs: subspace-labels. (606 words, used by 2)
- `address-interchange`: [Fast address-chunk interchange](address-interchange.md) — The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data. Needs: rank-recurrence, matrix-shear, stream-ops. (655 words, used by 3)
- `phase-frames`: [Binary phase frames](phase-frames.md) — Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis. Needs: subspace-labels, phase-kernel. (659 words, used by 1)
- `packed-bit-addition`: [Packed selected-bit addition](packed-bit-addition.md) — XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses. Needs: address-interchange, controlled-shifts. (687 words, used by 2)
- `simultaneous-layer`: [Simultaneous butterfly layer](simultaneous-layer.md) — The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes. Needs: phase-frames, rank-recurrence, packed-bit-addition, fixed-point. (693 words, used by 2)
- `transform-layout`: [Tape layout for synthetic transforms](transform-layout.md) — Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes. Needs: synthetic-transform, simultaneous-layer, address-interchange, frequency-order. (529 words, used by 1)
- `ring-convolution`: [Convolution from the retained transform layout](ring-convolution.md) — Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM). Needs: transform-layout, signed-packing, frequency-order. (546 words, used by 1)
- `multiplication-algorithm`: [The multiplication algorithm](multiplication-algorithm.md) — Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product. Needs: radix-digit-reduction, crt-map, retained-permutations, phase-twist, ring-convolution, parameter-choice, precision-recovery. (548 words, used by 2)
- `cost-accounting`: [Cost accounting and the exponent κ](cost-accounting.md) — Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}). Needs: multiplication-algorithm, address-interchange, simultaneous-layer, packed-bit-addition. (663 words, used by 1)
- `main-result`: [Power-saving integer multiplication](main-result.md) — A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model. Needs: cost-accounting, multiplication-algorithm, conjecture. (489 words, used by 0)

## The argument's main steps

- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter. Pages: `rank-recurrence`, `exchange-network`, `array-frames`, `subspace-labels`, `phase-frames`, `address-interchange`, `matrix-shear`, `simultaneous-layer`, `packed-bit-addition`.
- Synthetic transforms over $\mathcal R_r$ on $d-1$ axes of lengths $t_i\in\{2^{\ell-1},2^\ell\}$ with outputs kept in a retained layout $LB$ cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error less than $\sqrt2\ell\,2^{-p}$. Pages: `transform-layout`, `frequency-order`.
- Normalized cyclic convolution over the polynomial ring $\mathbb C[y]/(y^r+1)$ on the remaining $d-1$ axes is computed from two forward synthetic transforms in retained order, $M$ pointwise polynomial products and the opposite transform, in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$ time with error less than $\sqrt2\,M(3\ell+1)2^{-p}$. Pages: `ring-convolution`, `signed-packing`.
- The Fourier transforms of pairwise coprime prime lengths $s_i$ that the integer product needs are computed through power-of-two lengths $t_i$ by Gaussian resampling and Bluestein chirps, with the source and target coordinate permutations left inside the transform identities, so that none is executed as a sort. Pages: `retained-permutations`, `gaussian-resampling`, `chirp`.
- The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain: radix digits, Chinese-remainder address map to a product of prime cyclic axes, two forward source transforms (resampling and chirps), pointwise product, opposite transform, rescaling, rounding, and carry propagation, with total error below $1/2$. Pages: `multiplication-algorithm`, `parameter-choice`, `radix-digit-reduction`, `crt-map`, `phase-twist`, `precision-recovery`.
- The total time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$: after dividing each cost by $V=Tp=\Theta(n)$ the dominant terms are powers of $p$ below one, with minimum margin $2^{-181}=2\kappa$. Pages: `cost-accounting`.

The page bodies are in `exegenius/pages/<id>.md`; read them if the glosses are not enough to write the overview.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Part": {
      "additionalProperties": false,
      "properties": {
        "intro": {
          "description": "What the part covers and why the reader needs it, as markdown.",
          "type": "string"
        },
        "pages": {
          "description": "Ids of the pages in this part.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "title": {
          "description": "Short title, plain text, no numbering.",
          "type": "string"
        }
      },
      "required": [
        "title",
        "intro",
        "pages"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "glossary": {
      "default": [],
      "description": "Ids of minor pages to move to the glossary.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "overview": {
      "description": "The front page, as markdown, with no headings.",
      "type": "string"
    },
    "parts": {
      "description": "The parts, in reading order.",
      "items": {
        "$ref": "#/$defs/Part"
      },
      "type": "array"
    }
  },
  "required": [
    "overview",
    "parts"
  ],
  "title": "OutlineAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0215-outline.answer.json`, then run `exegenius submit 0215-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0215-outline`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
