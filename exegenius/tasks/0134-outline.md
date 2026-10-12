# exegenius task 0134-outline

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

Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

## Pages, in reading order

- `gaussian-dyadics`: [Gaussian dyadics](gaussian-dyadics.md) — Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer. (205 words, used by 3)
- `linear-network-frames`: [Linear networks and frames](linear-network-frames.md) — A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame. (312 words, used by 3)
- `fixed-tape-model`: [Fixed-tape machine model](fixed-tape-model.md) — A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input. (329 words, used by 3)
- `exact-integer-multiplication`: [Exact integer multiplication](exact-integer-multiplication.md) — Given binary strings x and y of length n, output the 2n-bit binary representation of their product. Needs: fixed-tape-model. (227 words, used by 3)
- `n-log-n-conjecture`: [The n log n optimality conjecture](n-log-n-conjecture.md) — The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers. Needs: exact-integer-multiplication. (219 words, used by 1)
- `address-interchange`: [Address-field interchange](address-interchange.md) — A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly. Needs: fixed-tape-model, linear-network-frames. (305 words, used by 5)
- `address-shear`: [Address shear](address-shear.md) — The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges. Needs: address-interchange, linear-network-frames. (223 words, used by 1)
- `established-multiplier`: [Established O(n log n) multiplier](established-multiplier.md) — The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine. Needs: exact-integer-multiplication. (126 words, used by 1)
- `signed-packing`: [Signed coefficient packing](signed-packing.md) — Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication. Needs: established-multiplier. (292 words, used by 1)
- `bilinear-form`: [Bilinear form](bilinear-form.md) — A function of two vectors that is linear in each argument; a form is nondegenerate when no nonzero vector is orthogonal to every vector of the space. (246 words, used by 2)
- `subspace-labels`: [Subspace labels](subspace-labels.md) — Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs. Needs: bilinear-form. (272 words, used by 2)
- `subset-intersection-network`: [Subset-intersection network](subset-intersection-network.md) — A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values. Needs: subspace-labels, linear-network-frames. (324 words, used by 2)
- `rank-saving-recursion`: [Rank-saving recursion](rank-saving-recursion.md) — The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level. Needs: subset-intersection-network, address-interchange. (321 words, used by 1)
- `tensor-product`: [Tensor product](tensor-product.md) — The product of vector spaces, whose basis is formed by pairing basis vectors of the factors, so that a tensor power of a space collects several copies of it. Needs: bilinear-form. (246 words, used by 2)
- `complex-phase-network`: [Complex phase network](complex-phase-network.md) — A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values. Needs: subset-intersection-network, gaussian-dyadics, subspace-labels, tensor-product. (222 words, used by 1)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two sequences in which indices wrap around modulo the sequence length. (248 words, used by 6)
- `discrete-fourier-transform`: [Discrete Fourier transform](discrete-fourier-transform.md) — The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q. Needs: cyclic-convolution. (351 words, used by 5)
- `radix-digit-convolution`: [Radix-digit convolution](radix-digit-convolution.md) — Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients. Needs: exact-integer-multiplication, discrete-fourier-transform. (363 words, used by 4)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. Needs: discrete-fourier-transform, radix-digit-convolution. (204 words, used by 2)
- `synthetic-transforms`: [Synthetic polynomial transforms](synthetic-transforms.md) — Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients. Needs: discrete-fourier-transform, cyclic-convolution. (324 words, used by 3)
- `polynomial-ring-mod-yr-plus-1`: [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md) — The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign. Needs: synthetic-transforms. (288 words, used by 2)
- `chinese-remainder-map`: [Chinese-remainder map](chinese-remainder-map.md) — A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution. Needs: cyclic-convolution, radix-digit-convolution. (371 words, used by 2)
- `bluestein-chirp-identity`: [Bluestein's chirp identity](bluestein-chirp-identity.md) — An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution. Needs: discrete-fourier-transform, cyclic-convolution. (272 words, used by 1)
- `phase-twist`: [Phase twist](phase-twist.md) — A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring. Needs: bluestein-chirp-identity, polynomial-ring-mod-yr-plus-1. (254 words, used by 2)
- `polynomial-ring-convolution`: [Convolution over the polynomial ring](polynomial-ring-convolution.md) — The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform. Needs: polynomial-ring-mod-yr-plus-1, synthetic-transforms, signed-packing, cyclic-convolution. (471 words, used by 2)
- `simultaneous-butterfly-layer`: [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) — The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time. Needs: complex-phase-network, gaussian-dyadics, address-interchange, discrete-fourier-transform, tensor-product. (482 words, used by 3)
- `guard-width-bound`: [Guard-width bound](guard-width-bound.md) — An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices. Needs: simultaneous-butterfly-layer, gaussian-dyadics. (418 words, used by 1)
- `transform-layout`: [Transform layout](transform-layout.md) — A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round. Needs: address-interchange, simultaneous-butterfly-layer, synthetic-transforms. (259 words, used by 1)
- `recovery-and-error`: [Exact coefficient recovery](recovery-and-error.md) — The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly. Needs: polynomial-ring-convolution, guard-width-bound, phase-twist. (227 words, used by 1)
- `packed-bit-addition`: [Packed selected-bit addition](packed-bit-addition.md) — An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses. Needs: simultaneous-butterfly-layer, address-interchange, address-shear. (551 words, used by 1)
- `transform-identity`: [Transform identity with retained permutations](transform-identity.md) — The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts. Needs: gaussian-resampling, cyclic-convolution. (158 words, used by 1)
- `prime-source-lengths`: [Prime source lengths](prime-source-lengths.md) — Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box. Needs: chinese-remainder-map, gaussian-resampling. (298 words, used by 1)
- `carry-propagation`: [Carry propagation](carry-propagation.md) — Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position. Needs: radix-digit-convolution. (349 words, used by 1)
- `main-theorem`: [Integer multiplication below n log n](main-theorem.md) — A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model. Needs: n-log-n-conjecture, fixed-tape-model, radix-digit-convolution, chinese-remainder-map, rank-saving-recursion, transform-layout, transform-identity, prime-source-lengths, phase-twist, polynomial-ring-convolution, packed-bit-addition, recovery-and-error, carry-propagation. (380 words, used by 0)

## The argument's main steps

- A simultaneous normalized butterfly layer on $d$ selected chunks of stored volume $V$ costs $O(V d^{\lambda'})$. Pages: `simultaneous-butterfly-layer`, `transform-layout`, `complex-phase-network`.
- Two disjoint equal address fields of $u$ bits in an array of stored volume $V$ can be interchanged in $O(V u^{\tau})$ time. Pages: `address-interchange`, `subset-intersection-network`, `rank-saving-recursion`.
- The exact product of two $n$-bit integers is obtained from the convolution of their radix-digit coefficients, computed by transforms on a fixed tape layout and then recovered and carried. Pages: `radix-digit-convolution`, `chinese-remainder-map`, `gaussian-resampling`, `transform-identity`, `bluestein-chirp-identity`, `phase-twist`, `polynomial-ring-convolution`, `signed-packing`, `recovery-and-error`, `carry-propagation`.
- A compatible choice of rational parameters makes every term of the cost table fit the bound of Theorem 1.
- The total cost is $O(n(\lg n)^{1-\kappa})$ for every large input, with $\kappa=2^{-182}$.

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

Write the answer to `exegenius/tasks/0134-outline.answer.json`, then run `exegenius submit 0134-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
