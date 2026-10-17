# exegenius task 0145-audit-rank-recurrence

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file and the paper at `sources/paper.tex`: do not read other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Fidelity: also check that the page's mathematics is right, and report what is wrong even where this reader could follow it. For each claim that states a definition, a hypothesis, a step of a proof, a value or a conclusion, work out what it assumes and what it concludes, and check it against everything this task file gives: the page's definitions, its other claims and its quotations. Report as a `step` any claim that is false, inconsistent with another statement on the page, stated more strongly or more widely than what supports it, or missing a hypothesis it needs. Quote the claim, and say in the note what is wrong and what the correct statement is.

The source: the paper this page explains is at `sources/paper.tex` (LaTeX). For each such claim, also find the passage of the paper that states, defines or proves it (search the file for the claim's terms and symbols, then read the passage around each match) and compare: every hypothesis present, the same scope and quantifiers, the same constants, signs, exponents and inequality directions, a conclusion no stronger than the paper's, and the right result, lemma or author credited. Report any mismatch as a `step` in the same way, and give the paper's line number in the note.

What counts as an error: report a claim as wrong only if, as this page states it, it is false; inconsistent with the page; stated more strongly or more widely than what supports it; missing a hypothesis without which it is false; given a wrong value, sign, exponent, constant, quantifier or credit; or presented as following from something it does not follow from. Do not report a correct statement as wrong because it is informal, abbreviated or simplified, uses a word in the paper's own sense, or leaves a technical precondition to another page or to the paper. If the paper's own summary of the same step states it the same way, it is not an error.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
- Parameter and prime-length choice
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)
- Contractions and bilinear contractions (also: contraction, bilinear contraction)
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

## Symbols bound on earlier pages

- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $N$ (bank size), bound on `exchange-network`: The size of each data bank.
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used later.
- $\sigma$ (side scratch vector), bound on `exchange-network`: The initial values of the side scratch wires.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $N$ (factor bit length), bound on `hvdh-multiplier`: The number of bits in each of the two integers of one product given to the established multiplier (not the bank size).
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $c$ (multiplier), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit (invertible) modulo q.
- $L$ (log of padded size), bound on `precision-recovery`: The base-2 logarithm of T.
- $\tau$ (chunk-swap exponent), bound on `parameter-choice`: An exponent bounding the cost of an equal-width chunk interchange.
- $\sigma$ (recursion exponent), bound on `parameter-choice`: An exponent bounding the growth of the layer's recursion.
- $\beta$ (threshold exponent), bound on `parameter-choice`: The exponent of the threshold d^beta of active chunks handled singly.
- $\lambda$ (node overhead exponent), bound on `parameter-choice`: The exponent of the per-node overhead in the butterfly layer.
- $\lambda'$ (layer cost exponent), bound on `parameter-choice`: The exponent in the final layer cost O(V d^lambda').
- $c$ (chunk-width exponent), bound on `parameter-choice`: The exponent giving the chunk width K = floor(d^c).
- $V$ (bit volume), bound on `parameter-choice`: The logical bit volume of the data the layer acts on.
- $K$ (chunk width), bound on `parameter-choice`: The number of bits in an address chunk.
- $\eta$ (relative distance), bound on `parameter-choice`: The relative distance 1/(4d) of each prime s_i below t_i.
- $\eta$ (vector in G), bound on `tensor-product-of-spaces`: A vector of the second space G.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $L$ (total dimension loss), bound on `subspace-labels`: The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.

## Pages in the wiki

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Page to audit (`rank-recurrence`)

````markdown
# Recursive power saving

Recursive power saving is the recurrence making both tape procedures (chunk interchange, butterfly layer) cost volume times a power below one of their parameter.

A call has a parameter $f$, the number of digits per interchanged chunk or of selected axes, and a volume $V$. A call at parameter $mf$, with $m=10^6$ (the label-space dimension) slots of size $f$, deals its rows into $W$ streams of volume $V/W$, one per wire of a fixed bit or complex [exchange network](exchange-network.md). Crossing a network edge changes the stream's frame ([Frames on wire arrays](array-frames.md)), costing one call at parameter $f$ on that stream per unit of rank of the change. So the call makes $s$ calls at parameter $f$, each on volume $V/W$, where $s$ is the total edge rank. With $F(f)$ the time per unit volume at parameter $f$, these cost $s(V/W)F(f)$. Multiplying the parameter by $m$ thus multiplies recursive cost per unit volume by $s/W$, less than $m$ when $s<Wm$ (cited)

For interchange, other node work (splitting, gates, shears, stack parking) is $O(V)$, and one digit swaps in linear time:

$$F(mf)\le\frac{s}{W}F(f)+O(1),\qquad F(1)=O(1).$$

Unrolling through $\log_m f$ levels ($f$ a power of $m$), with depth $j$ (here counting levels) contributing $(s/W)^j$, gives $F(f)=O\big(\sum_{j=0}^{\log_m f}(s/W)^j\big)$. If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$: if $s/W\le1$ there are $1+\log_m f$ terms of at most $1$; otherwise the last term, below $m^{\tau\log_m f}=f^\tau$, dominates the geometric sum. So an interchange costs $O(Vf^\tau)$ (cited).

For the layer (complex network), node overhead grows: frame changes are row additions on slots of $(f/m)K$ address bits ($K$ bits per address chunk), each costing $O(V((fK)^\tau+1))$ through chunk interchanges ([Packed selected-bit addition](packed-bit-addition.md)). Recursion stops below $d^\beta$ axes, $\beta=1/2$, applying the $f$ two-point kernels singly:

$$F(f)\le\frac{s}{W}F(f/m)+O((fK)^\tau+1),\qquad F(f)=O(f)\quad(f<d^\beta).$$

Fix $\sigma<1$ with $s/W\le m^\sigma$, and $\lambda<1$ above $\sigma$ and $\tau(1+c/\beta)$, where $K\le d^c$, $c$ fixed. Internal nodes have $f\ge d^\beta$, so $K\le f^{c/\beta}$ and overhead $O(f^\lambda)$. At depth $j$, the $(s/W)^j$ normalized overheads $O((f/m^j)^\lambda)$ sum geometrically, with ratio $(s/W)/m^\lambda<1$, to $O(f^\lambda)$; leaves contribute $(s/W)^jf/m^j\le f^\sigma(f/m^j)^{1-\sigma}<f^\sigma d^{\beta(1-\sigma)}$. With $f\le d$, and a $\log d$ factor from splitting into powers of $m$, the layer costs $O(Vd^{\lambda'})$ for fixed $\lambda'$ between $\max\{\lambda,\sigma+\beta(1-\sigma)\}$ and $1$ (cited)

The recursion gets its strict inequality $s<Wm$ from [Nested subspace labels and rank deficit](subspace-labels.md): an edge costs the dimension change of its nested labels, so a wire climbing from $0$ to $m$ dimensions costs $m$. One data bank's $N$ wires start on a line and the other's stop one dimension short, saving $2N$; the bit network spends $N$ on extra source ranks, and shrinking edges cost back $2L<N$.

Write $s/W=m(1-\eta)$, with $\eta$ now the relative deficit $(Wm-s)/(Wm)$. It is $339/22587335000000$ (bit) and $73/19906842167500$ (complex) (cited). Both ($\approx1.5\cdot10^{-11}$, $3.7\cdot10^{-12}$) exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$ (cited) Since $m<2^{20}$, $\ln m<20\ln 2<20$; as the exponential lies above its tangent at $0$, $m^{1-2^{-50}}=m\exp(-2^{-50}\ln m)>m(1-2^{-50}\ln m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$ for either network. Hence $\tau=\sigma=1-2^{-50}$ gives $s/W<m^\tau$ (bit) and $s/W<m^\sigma$ (complex), exponents barely below $1$.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0145-audit-rank-recurrence.answer.json`, then run `exegenius submit 0145-audit-rank-recurrence` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0145-audit-rank-recurrence`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
