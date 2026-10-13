# exegenius task 0182-outline

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

Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

## Pages, in reading order

- `fixed-tape-model`: [Fixed-tape machine model](fixed-tape-model.md) — A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length. (236 words, used by 4)
- `schonhage-strassen-conjecture`: [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md) — The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers on a multitape Turing machine. Needs: fixed-tape-model. (308 words, used by 1)
- `power-saving`: [Power saving in the logarithmic factor](power-saving.md) — A bound of the form n times (lg n) raised to the power 1 − κ for a fixed κ > 0, which is smaller than n log n by a polynomial factor in log n. Needs: schonhage-strassen-conjecture. (213 words, used by 1)
- `gaussian-dyadic`: [Gaussian dyadic numbers](gaussian-dyadic.md) — Complex numbers whose real and imaginary parts are both dyadic rationals, that is, have power-of-two denominators. (295 words, used by 3)
- `linear-network`: [Linear network](linear-network.md) — A fixed network of wires with gates that apply fixed linear maps to the values on their wires, used here to exchange two banks of values while restoring all auxiliary values. (319 words, used by 7)
- `role-streams`: [Role streams from a cyclic row split](role-streams.md) — Splitting the rows of an array cyclically among the W fixed wire roles of a network, so that each role carries an equal share of the volume and gates act pointwise on matching addresses. Needs: linear-network. (324 words, used by 2)
- `subset-network`: [Subset-intersection finite network](subset-network.md) — A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2]. Needs: linear-network, gaussian-dyadic. (525 words, used by 1)
- `multiplier-subroutine`: [Established fast multiplier](multiplier-subroutine.md) — The known deterministic O(n log n) multiplication algorithm of Harvey and van der Hoeven, used as a black-box subroutine on shorter integers. Needs: fixed-tape-model. (192 words, used by 1)
- `network-terminal`: [Source, sink and terminal of a network](network-terminal.md) — A source or sink of a linear network is an end vertex of a wire, where data enter the network or leave it, and the terminals are the sources and sinks at which the network meets its banks of values. Needs: linear-network. (203 words, used by 2)
- `frame`: [Frame of a vertex](frame.md) — An invertible linear operator attached to a gate or terminal that sets how the array on each wire there is stored; changing frames along an edge cancels between the two ends of a route. Needs: linear-network, network-terminal. (393 words, used by 4)
- `address-shear`: [Address shear](address-shear.md) — The address permutation that replaces the first of two address fields H by H + D, leaving D fixed, which is the endpoint operator of the bit network on arrays. Needs: linear-network, frame. (281 words, used by 1)
- `subspace-labels`: [Nested subspace labels](subspace-labels.md) — Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge. Needs: frame, subset-network, network-terminal. (479 words, used by 1)
- `recursive-saving`: [Rank-saving recursion](recursive-saving.md) — A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume. Needs: frame, role-streams, subspace-labels, linear-network. (308 words, used by 1)
- `tape-interchange`: [Fast interchange of address chunks](tape-interchange.md) — A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data. Needs: fixed-tape-model, address-shear, recursive-saving, linear-network, role-streams. (485 words, used by 1)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S. (223 words, used by 5)
- `radix-digit-convolution`: [Radix-digit convolution](radix-digit-convolution.md) — Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two. Needs: cyclic-convolution. (311 words, used by 2)
- `fourier-transform`: [Discrete Fourier transform](fourier-transform.md) — The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q). Needs: cyclic-convolution. (270 words, used by 5)
- `tensor-product`: [Tensor product](tensor-product.md) — The tensor product V ⊗ W of vector spaces is the space spanned by pairs of basis vectors, and the tensor product of linear maps acts on each factor separately, so one-dimensional operations on several coordinates combine into one operation on the product space. Needs: fourier-transform. (364 words, used by 2)
- `multidim-transform`: [Multidimensional transform with power-of-two axes](multidim-transform.md) — A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms. Needs: fourier-transform, tensor-product. (318 words, used by 1)
- `butterfly-layer`: [Simultaneous butterfly layer H₀](butterfly-layer.md) — The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records. Needs: gaussian-dyadic, frame, tensor-product. (429 words, used by 2)
- `order-of-element`: [Order of an element](order-of-element.md) — The order of an element x of a multiplicative group is the least positive integer k with x^k equal to the identity, when such k exists. (280 words, used by 1)
- `roots-of-unity`: [Root of unity](roots-of-unity.md) — A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role. Needs: fourier-transform, order-of-element. (334 words, used by 2)
- `polynomial-ring`: [Polynomial ring modulo yʳ + 1](polynomial-ring.md) — The ring of complex polynomials of degree less than r, with multiplication reduced modulo y^r + 1; multiplication by a power of y permutes and sign-changes the coefficient list. Needs: roots-of-unity. (349 words, used by 2)
- `synthetic-transform`: [Synthetic polynomial transform](synthetic-transform.md) — A discrete Fourier transform whose roots of unity are powers of y in the polynomial ring, so that each twiddle multiplication is a signed shift and the transform is computed by simultaneous butterfly layers. Needs: polynomial-ring, roots-of-unity, butterfly-layer, cyclic-convolution. (330 words, used by 2)
- `signed-packing`: [Signed coefficient packing](signed-packing.md) — Encoding a polynomial with signed integer coefficients as one integer by placing coefficients at fixed bit offsets, so that a polynomial product becomes an integer product. Needs: synthetic-transform. (310 words, used by 1)
- `exact-recovery`: [Exact recovery by rounding and carries](exact-recovery.md) — Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b. Needs: radix-digit-convolution, gaussian-dyadic. (421 words, used by 1)
- `operator-norm`: [Operator norm of a linear map](operator-norm.md) — The operator norm of a linear map T is the largest factor by which T stretches a vector, the supremum of ‖Tv‖ over all vectors v with ‖v‖ ≤ 1, for a chosen vector norm. (261 words, used by 1)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity. Needs: fourier-transform, multidim-transform, operator-norm. (439 words, used by 2)
- `bluestein`: [Bluestein's chirp identity](bluestein.md) — An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t). Needs: cyclic-convolution, fourier-transform, gaussian-resampling. (234 words, used by 1)
- `quotient-ring`: [Quotient ring by several relations](quotient-ring.md) — The quotient ring of a polynomial ring by several relations is the ring obtained by identifying two polynomials whenever their difference lies in the ideal generated by those relations. Needs: polynomial-ring. (268 words, used by 1)
- `crt-axis-map`: [Chinese-remainder axis map](crt-axis-map.md) — The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one. Needs: cyclic-convolution, quotient-ring. (496 words, used by 1)
- `fixed-tape-multiplication`: [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md) — A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model. Needs: fixed-tape-model, power-saving, tape-interchange, butterfly-layer, synthetic-transform, gaussian-resampling, bluestein, crt-axis-map, radix-digit-convolution, signed-packing, multiplier-subroutine, exact-recovery. (567 words, used by 0)

## The argument's main steps

- Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Pages: `radix-digit-convolution`.
- The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Pages: `crt-axis-map`.
- Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity. Pages: `gaussian-resampling`.
- Bluestein's chirp identity turns the middle transform, with its target permutation, into normalized cyclic convolution. Pages: `bluestein`.
- Normalized cyclic convolution on the power-of-two axes is computed over the polynomial ring $\mathbb C[y]/(y^r+1)$ by synthetic transforms and packed polynomial products. Pages: `synthetic-transform`, `signed-packing`.
- The recovered coefficient error is strictly below $1/2$, so rounding and carry propagation give the exact binary product. Pages: `exact-recovery`.
- The tape operations of the algorithm cost $O(V(\lg n)^{1-\kappa})$ in total, for stored volume $V=\Theta(n)$. Pages: `tape-interchange`, `butterfly-layer`.

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

Write the answer to `exegenius/tasks/0182-outline.answer.json`, then run `exegenius submit 0182-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
