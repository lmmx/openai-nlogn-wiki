# exegenius task 0140-outline

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

Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

## Pages, in reading order

- `nlogn-conjecture`: [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md) — The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the time to multiply two n-bit integers on a multitape Turing machine. (249 words, used by 1)
- `harvey-hoeven-multiplier`: [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md) — The unconditional O(n log n) multiplication algorithm on a multitape Turing machine, used in this result as an ordinary subroutine. (118 words, used by 1)
- `roots-of-unity`: [Primitive roots of unity](roots-of-unity.md) — A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1. (236 words, used by 2)
- `fourier-transform`: [Discrete Fourier transform](fourier-transform.md) — The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity. Needs: roots-of-unity. (295 words, used by 3)
- `butterfly-operation`: [Butterfly operation](butterfly-operation.md) — The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform. Needs: fourier-transform. (231 words, used by 1)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues. (371 words, used by 4)
- `convolution-reduction`: [Multiplication as convolution of digits](convolution-reduction.md) — Writing each integer in radix 2^b digits so that the integer product becomes a convolution of the digit sequences, which is then carried back to binary. Needs: cyclic-convolution. (368 words, used by 2)
- `polynomial-ring-y`: [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md) — The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list. Needs: cyclic-convolution. (346 words, used by 3)
- `synthetic-transform`: [Synthetic polynomial transform](synthetic-transform.md) — A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions. Needs: polynomial-ring-y, roots-of-unity, fourier-transform. (464 words, used by 2)
- `kronecker-packing`: [Signed Kronecker packing](kronecker-packing.md) — Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products. Needs: polynomial-ring-y, convolution-reduction. (476 words, used by 1)
- `matrix-rank`: [Matrix rank](matrix-rank.md) — The rank of a matrix is the maximum number of linearly independent rows or columns; the number of nonzero pivots in elimination. (230 words, used by 2)
- `linear-network-exchange`: [Linear network with restored auxiliary values](linear-network-exchange.md) — A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges. Needs: matrix-rank. (461 words, used by 4)
- `lower-triangular-factorization`: [Lower-triangular factorization](lower-triangular-factorization.md) — The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot. Needs: matrix-rank. (224 words, used by 1)
- `address-shear`: [Address shear](address-shear.md) — The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A. Needs: lower-triangular-factorization, linear-network-exchange. (388 words, used by 1)
- `address-interchange`: [Fast address interchange](address-interchange.md) — A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data. Needs: address-shear, linear-network-exchange. (393 words, used by 3)
- `chinese-remainder-address-map`: [Chinese-remainder address map](chinese-remainder-address-map.md) — A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges. Needs: cyclic-convolution, address-interchange. (300 words, used by 2)
- `tensor-product`: [Tensor product](tensor-product.md) — The tensor product V ⊗ W of two vector spaces, whose basis consists of all pairs of basis vectors of V and W, together with the tensor product A ⊗ B of linear maps, which acts on each coordinate separately. (284 words, used by 2)
- `simultaneous-butterfly-layer`: [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) — A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer. Needs: butterfly-operation, linear-network-exchange, tensor-product. (338 words, used by 3)
- `recursive-power-saving`: [Recursive power saving](recursive-power-saving.md) — The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter. Needs: linear-network-exchange, address-interchange, simultaneous-butterfly-layer. (394 words, used by 1)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity. Needs: fourier-transform, chinese-remainder-address-map, tensor-product. (363 words, used by 2)
- `bluestein-chirp`: [Bluestein's chirp identity](bluestein-chirp.md) — The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it. Needs: gaussian-resampling, cyclic-convolution. (322 words, used by 2)
- `rounding-recovery`: [Exact recovery by rounding](rounding-recovery.md) — The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product. Needs: synthetic-transform, simultaneous-butterfly-layer, kronecker-packing, bluestein-chirp. (458 words, used by 1)
- `integer-multiplication-target`: [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md) — A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model. Needs: nlogn-conjecture, harvey-hoeven-multiplier, recursive-power-saving, convolution-reduction, chinese-remainder-address-map, gaussian-resampling, bluestein-chirp, polynomial-ring-y, synthetic-transform, simultaneous-butterfly-layer, address-interchange, rounding-recovery. (396 words, used by 0)

## The argument's main steps

- The integer product is the carried convolution of the radix-$2^b$ digit sequences of the two inputs. Pages: `convolution-reduction`.
- Both tape procedures cost $O(V)$ times a power of their parameter whose exponent is strictly below one. Pages: `recursive-power-saving`, `address-interchange`, `simultaneous-butterfly-layer`, `linear-network-exchange`.
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes, preserving convolution. Pages: `chinese-remainder-address-map`.
- A Fourier transform of prime length is a multidimensional transform whose axis lengths are powers of two. Pages: `gaussian-resampling`.
- The middle transform, with its target permutation, becomes normalized cyclic convolution. Pages: `bluestein-chirp`.
- The last cyclic coordinate becomes a polynomial modulo $y^r+1$, so that its wrap is a signed shift. Pages: `polynomial-ring-y`.
- The two forward synthetic transforms keep the same frequency order through their pointwise product, and the opposite transform consumes that order. Pages: `synthetic-transform`.
- Polynomial products over the ring are computed by signed packing and the $O(n\log n)$ multiplier. Pages: `kronecker-packing`.
- The exact product is recovered: the source permutation cancels, and the coefficient error is below $1/2$, so rounding and carries give the binary product. Pages: `rounding-recovery`.

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

Write the answer to `exegenius/tasks/0140-outline.answer.json`, then run `exegenius submit 0140-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
