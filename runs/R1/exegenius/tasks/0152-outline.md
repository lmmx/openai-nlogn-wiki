# exegenius task 0152-outline

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

## Pages, in reading order

- `nlogn-conjecture`: [The n log n optimality conjecture](nlogn-conjecture.md) — Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers. (307 words, used by 2)
- `convolution`: [Convolution](convolution.md) — Product of polynomials / combination of coefficient lists where entries sum by index (cyclic if indices wrap). (254 words, used by 5)
- `radix-digit-reduction`: [Reduction of integer product to digit convolution](radix-digit-reduction.md) — Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation. Needs: convolution. (455 words, used by 2)
- `poly-ring-y-r`: [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md) — Complex-coefficient polynomials in y reduced by y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list and powers of y serve as roots of unity. (414 words, used by 2)
- `fixed-tape-model`: [Fixed-tape machine model and stream operations](fixed-tape-model.md) — Machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; each step touches one cell per tape, so data movement (scans, shifts, permutations) is the cost to minimize. (375 words, used by 3)
- `address-fields`: [Address fields and array layout on tapes](address-fields.md) — Arrays stored in tape order with addresses forming a Cartesian product of digit fields; rearranging fields costs time. Needs: fixed-tape-model. (368 words, used by 3)
- `dft-fft`: [Discrete Fourier transform and butterflies](dft-fft.md) — Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product. Needs: convolution, address-fields. (310 words, used by 5)
- `ss-hh-background`: [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md) — Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity. Needs: dft-fft, nlogn-conjecture. (398 words, used by 1)
- `synthetic-transforms`: [Synthetic polynomial transforms](synthetic-transforms.md) — Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies. Needs: dft-fft, poly-ring-y-r, fixed-tape-model. (319 words, used by 2)
- `linear-network-roles`: [Finite linear network with roles and frames](linear-network-roles.md) — Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator. Needs: address-fields. (506 words, used by 3)
- `scratch-restoration`: [Restoring auxiliary scratch values](scratch-restoration.md) — Subtract initial register value, compute, add result, reverse, so the permutation is exact for arbitrary initial auxiliary values. Needs: linear-network-roles. (230 words, used by 1)
- `address-shear-factorization`: [Address shear and lower-triangular factorization](address-shear-factorization.md) — Endpoint operator (H,D)->(H+D,D) over a residue ring, with rank reduction via a singular-matrix Bruhat factorization into lower-triangular factors. Needs: linear-network-roles. (569 words, used by 1)
- `crt-address-map`: [Chinese-remainder map to prime cyclic axes](crt-address-map.md) — Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves. Needs: convolution, radix-digit-reduction, fixed-tape-model. (424 words, used by 2)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths. Needs: dft-fft, crt-address-map. (516 words, used by 1)
- `bluestein-chirp`: [Bluestein's chirp identity](bluestein-chirp.md) — Rewrites a discrete Fourier transform as a cyclic convolution via chirp phases. Needs: dft-fft, convolution. (250 words, used by 1)
- `phase-twist-convolution`: [Last-coordinate phase twist](phase-twist-convolution.md) — Twisting the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap equals the original cyclic wrap after untwisting. Needs: poly-ring-y-r, convolution, bluestein-chirp. (389 words, used by 1)
- `fixed-point-precision`: [Fixed-point precision and exact recovery](fixed-point-precision.md) — Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product. Needs: radix-digit-reduction, dft-fft. (465 words, used by 2)
- `signed-packing`: [Signed coefficient packing (Kronecker substitution)](signed-packing.md) — Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier. Needs: ss-hh-background. (465 words, used by 1)
- `ring-convolution-retained-order`: [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md) — Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts. Needs: synthetic-transforms, signed-packing, gaussian-resampling, phase-twist-convolution. (509 words, used by 1)
- `tensor-product-of-vector-spaces`: [Tensor product of vector spaces](tensor-product-of-vector-spaces.md) — The space built from tuples of vectors whose dimension is the product of the factors' dimensions, so (Q^h)^{⊗3} has dimension h^3. (298 words, used by 1)
- `subset-intersection-construction`: [Three-element subset intersection construction](subset-intersection-construction.md) — Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls. Needs: linear-network-roles, tensor-product-of-vector-spaces. (505 words, used by 1)
- `recursive-power-saving`: [Recursive power saving from s<Wm](recursive-power-saving.md) — Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving. Needs: subset-intersection-construction. (385 words, used by 2)
- `fast-address-interchange`: [Fast interchange of address fields](fast-address-interchange.md) — Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation. Needs: address-shear-factorization, scratch-restoration, recursive-power-saving, address-fields. (510 words, used by 2)
- `fast-butterfly-layers`: [Fast simultaneous butterfly layers](fast-butterfly-layers.md) — Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end. Needs: recursive-power-saving, fast-address-interchange, synthetic-transforms, fixed-point-precision. (598 words, used by 1)
- `main-theorem`: [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md) — Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model. Needs: fast-address-interchange, fast-butterfly-layers, ring-convolution-retained-order, fixed-point-precision, nlogn-conjecture, crt-address-map. (615 words, used by 0)

## The argument's main steps

- Splitting the inputs into radix digits reduces the integer product to a convolution of short integer coefficients. Pages: `radix-digit-reduction`.
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume. Pages: `linear-network-roles`, `fast-address-interchange`, `address-shear-factorization`, `fast-butterfly-layers`, `subset-intersection-construction`, `recursive-power-saving`.
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map. Pages: `crt-address-map`.
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform. Pages: `gaussian-resampling`.
- Bluestein's chirp identity converts the middle transform into normalized cyclic convolution. Pages: `bluestein-chirp`.
- A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the original cyclic wrap after untwisting. Pages: `phase-twist-convolution`.
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products. Pages: `ring-convolution-retained-order`, `synthetic-transforms`, `signed-packing`.
- Known rescalings and rounding recover the coefficients since the error is below $1/2$, and carry propagation gives the exact product. Pages: `fixed-point-precision`.

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

Write the answer to `exegenius/tasks/0152-outline.answer.json`, then run `exegenius submit 0152-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
