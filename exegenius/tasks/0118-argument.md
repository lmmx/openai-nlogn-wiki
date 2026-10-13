# exegenius task 0118-argument

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`fixed-tape-multiplication`: Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

## Pages, in reading order

- `fixed-tape-model`: Fixed-tape machine model: A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length.
- `schonhage-strassen-conjecture`: Schonhage-Strassen optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers on a multitape Turing machine.
- `power-saving`: Power saving in the logarithmic factor: A bound of the form n times (lg n) raised to the power 1 − κ for a fixed κ > 0, which is smaller than n log n by a polynomial factor in log n.
- `gaussian-dyadic`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are both dyadic rationals, that is, have power-of-two denominators.
- `linear-network`: Linear network: A fixed network of wires with gates that apply fixed linear maps to the values on their wires, used here to exchange two banks of values while restoring all auxiliary values.
- `role-streams`: Role streams from a cyclic row split: Splitting the rows of an array cyclically among the W fixed wire roles of a network, so that each role carries an equal share of the volume and gates act pointwise on matching addresses.
- `subset-network`: Subset-intersection finite network: A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].
- `multiplier-subroutine`: Established fast multiplier: The known deterministic O(n log n) multiplication algorithm of Harvey and van der Hoeven, used as a black-box subroutine on shorter integers.
- `network-terminal`: Source, sink and terminal of a network: A source or sink of a linear network is an end vertex of a wire, where data enter the network or leave it, and the terminals are the sources and sinks at which the network meets its banks of values.
- `frame`: Frame of a vertex: An invertible linear operator attached to a gate or terminal that sets how the array on each wire there is stored; changing frames along an edge cancels between the two ends of a route.
- `address-shear`: Address shear: The address permutation that replaces the first of two address fields H by H + D, leaving D fixed, which is the endpoint operator of the bit network on arrays.
- `subspace-labels`: Nested subspace labels: Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.
- `recursive-saving`: Rank-saving recursion: A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.
- `tape-interchange`: Fast interchange of address chunks: A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
- `radix-digit-convolution`: Radix-digit convolution: Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two.
- `fourier-transform`: Discrete Fourier transform: The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
- `tensor-product`: Tensor product: The tensor product V ⊗ W of vector spaces is the space spanned by pairs of basis vectors, and the tensor product of linear maps acts on each factor separately, so one-dimensional operations on several coordinates combine into one operation on the product space.
- `multidim-transform`: Multidimensional transform with power-of-two axes: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
- `butterfly-layer`: Simultaneous butterfly layer H₀: The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.
- `order-of-element`: Order of an element: The order of an element x of a multiplicative group is the least positive integer k with x^k equal to the identity, when such k exists.
- `roots-of-unity`: Root of unity: A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role.
- `polynomial-ring`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree less than r, with multiplication reduced modulo y^r + 1; multiplication by a power of y permutes and sign-changes the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A discrete Fourier transform whose roots of unity are powers of y in the polynomial ring, so that each twiddle multiplication is a signed shift and the transform is computed by simultaneous butterfly layers.
- `signed-packing`: Signed coefficient packing: Encoding a polynomial with signed integer coefficients as one integer by placing coefficients at fixed bit offsets, so that a polynomial product becomes an integer product.
- `exact-recovery`: Exact recovery by rounding and carries: Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.
- `operator-norm`: Operator norm of a linear map: The operator norm of a linear map T is the largest factor by which T stretches a vector, the supremum of ‖Tv‖ over all vectors v with ‖v‖ ≤ 1, for a chosen vector norm.
- `gaussian-resampling`: Gaussian resampling: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
- `bluestein`: Bluestein's chirp identity: An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).
- `quotient-ring`: Quotient ring by several relations: The quotient ring of a polynomial ring by several relations is the ring obtained by identifying two polynomials whenever their difference lies in the ideal generated by those relations.
- `crt-axis-map`: Chinese-remainder axis map: The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
- `fixed-tape-multiplication`: Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomial`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-number`: Prime number
- `binary-field-and-exclusive-or`: Binary field and exclusive or
- `hamming-weight`: Hamming weight
- `two-s-complement-representation`: Two's-complement representation
- `positional-notation-and-binary-representation`: Positional notation and binary representation
- `dyadic-rational`: Dyadic rational
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `binomial-coefficient`: Binomial coefficient
- `finite-sets-subsets-and-intersections`: Finite sets, subsets and intersections
- `bijection-and-permutation`: Bijection and permutation
- `cartesian-product`: Cartesian product
- `lexicographic-order`: Lexicographic order
- `logarithm-and-exponential-function`: Logarithm and exponential function
- `limits`: Limits
- `convergence-of-sequences-and-series`: Convergence of sequences and series
- `basic-integrals`: Basic integrals
- `geometric-series`: Geometric series
- `big-omega-big-theta-and-little-o-notation`: Big-Omega, big-Theta and little-o notation
- `worst-case-running-time-of-a-turing-machine`: Worst-case running time of a Turing machine
- `recurrence-relation`: Recurrence relation
- `schoolbook-multiplication`: Schoolbook multiplication
- `directed-graph`: Directed graph
- `vector-space-subspace-basis-and-dimension`: Vector space, subspace, basis and dimension
- `linear-map-and-matrix`: Linear map and matrix
- `matrix-rank`: Matrix rank
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices
- `dot-product-and-orthogonal-complement`: Dot product and orthogonal complement
- `vector-norm-and-maximum-norm`: Vector norm and maximum norm
- `complex-conjugate-modulus-and-polar-form`: Complex conjugate, modulus and polar form

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Previous plan (revise it: the pages have changed since)

```json
{
  "id": "S0",
  "intention": "show",
  "claim": "The integer product is computed exactly on one fixed-tape machine in $O(n(\\lg n)^{1-\\kappa})$ worst-case time.",
  "from": [
    "fixed-tape-model",
    "schonhage-strassen-conjecture",
    "power-saving"
  ],
  "method": "reduce exact multiplication to convolution of radix digits, compute the convolution by synthetic transforms on tape layouts, and bound the total tape cost with a power saving",
  "motivation": {
    "text": "Scanning the stored bits at each transform level already costs $\\Theta(n\\log n)$, so savings in both movement and arithmetic are needed.",
    "source": "explicit",
    "quote": {
      "source": "paper",
      "quote": "We therefore need savings in both movement and arithmetic."
    }
  },
  "page": "fixed-tape-multiplication",
  "children": [
    {
      "id": "S1",
      "intention": "infer",
      "claim": "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.",
      "from": [
        "positional-notation-and-binary-representation"
      ],
      "page": "radix-digit-convolution",
      "quote": {
        "source": "paper",
        "quote": "Splitting the inputs into radix digits reduces multiplication to\nconvolution of short integer coefficients."
      }
    },
    {
      "id": "S2",
      "intention": "infer",
      "claim": "The radix-digit coefficient list is placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.",
      "from": [
        "radix-digit-convolution",
        "cyclic-convolution",
        "prime-number",
        "greatest-common-divisor-and-coprimality"
      ],
      "page": "crt-axis-map",
      "quote": {
        "source": "paper",
        "quote": "First, the radix-digit coefficient list is placed on a product of\ndistinct prime cyclic axes by a Chinese-remainder map that preserves\nconvolution."
      }
    },
    {
      "id": "S3",
      "intention": "show",
      "claim": "Each prime-length Fourier transform is expressed through a tensor transform with power-of-two axis lengths, keeping the source and target permutations inside the identity.",
      "from": [
        "fourier-transform",
        "multidim-transform",
        "gaussian-dyadic"
      ],
      "method": "Gaussian resampling, computing the transform formula directly with both permutations retained",
      "motivation": {
        "text": "The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two; Gaussian resampling connects these two shapes.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "The transform lengths needed for the integer product are pairwise coprime,\nwhereas the synthetic transforms use powers of two. Gaussian resampling\nconnects these two shapes."
        }
      },
      "page": "gaussian-resampling",
      "children": [
        {
          "id": "S3.1",
          "intention": "infer",
          "claim": "Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform.",
          "from": [
            "fourier-transform",
            "multidim-transform",
            "gaussian-dyadic",
            "tensor-product"
          ],
          "quote": {
            "source": "paper",
            "quote": "resampling then expresses each source Fourier transform through a\npower-of-two tensor transform."
          }
        },
        {
          "id": "S3.2",
          "intention": "infer",
          "claim": "The source and target coordinate permutations stay inside the transform identity, so they need not be executed as separate sorts.",
          "from": [],
          "quote": {
            "source": "paper",
            "quote": "Section~\\ref{sec:resampling} retains the\nsource and target coordinate permutations in the transform identity,\nso they need not be executed as separate full sorts."
          }
        }
      ]
    },
    {
      "id": "S4",
      "intention": "infer",
      "claim": "Bluestein's chirp identity turns the middle transform, with its target permutation, into normalized cyclic convolution.",
      "from": [
        "fourier-transform",
        "cyclic-convolution",
        "gaussian-resampling"
      ],
      "page": "bluestein",
      "quote": {
        "source": "paper",
        "quote": "Next, Bluestein's chirp identity converts the middle transform,\nincluding its target permutation, into normalized cyclic convolution."
      }
    },
    {
      "id": "S5",
      "intention": "show",
      "claim": "Normalized cyclic convolution on the power-of-two axes is computed over the polynomial ring $\\mathbb C[y]/(y^r+1)$ by synthetic transforms and packed polynomial products.",
      "from": [
        "polynomial-ring",
        "roots-of-unity",
        "butterfly-layer",
        "signed-packing",
        "multiplier-subroutine",
        "cyclic-convolution"
      ],
      "method": "phase twist of the last coordinate into the polynomial ring, synthetic transforms on retained layouts, pointwise product, then signed packing with the established multiplier",
      "motivation": {
        "text": "Powers of $y$ act as roots of unity, and multiplying by such a root is a signed shift, so the transforms need only shifts and butterflies.",
        "source": "explicit",
        "quote": {
          "source": "paper",
          "quote": "serve as roots of unity in the remaining axes, and multiplication by\nsuch a root is a signed shift of the coefficient list."
        }
      },
      "page": "synthetic-transform",
      "children": [
        {
          "id": "S5.1",
          "intention": "infer",
          "claim": "A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$, and its negative wrap gives the original cyclic wrap.",
          "from": [
            "polynomial-ring",
            "roots-of-unity"
          ],
          "quote": {
            "source": "paper",
            "quote": "A phase twist changes the last cyclic coordinate into a polynomial\nmodulo $y^r+1$; its negative wrap gives precisely the original cyclic\nwrap after the twist is removed."
          }
        },
        {
          "id": "S5.2",
          "intention": "infer",
          "claim": "The two forward synthetic transforms keep the same frequency order through their pointwise product, which the opposite transform consumes.",
          "from": [
            "butterfly-layer"
          ],
          "quote": {
            "source": "paper",
            "quote": "The two forward synthetic transforms\nretain the same frequency order through their pointwise product, and\nthe opposite transform consumes that order."
          }
        },
        {
          "id": "S5.3",
          "intention": "infer",
          "claim": "Polynomial products are computed by signed packing and the established $O(n\\log n)$ multiplier used as a subroutine.",
          "from": [
            "signed-packing",
            "multiplier-subroutine"
          ],
          "quote": {
            "source": "paper",
            "quote": "Their polynomial products\nuse signed packing and the established $O(n\\log n)$ multiplier as an\nordinary subroutine."
          }
        }
      ]
    },
    {
      "id": "S6",
      "intention": "infer",
      "claim": "The recovered coefficient error is strictly below $1/2$, so rounding and carry propagation give the exact binary product.",
      "from": [
        "radix-digit-convolution",
        "crt-axis-map",
        "bluestein",
        "gaussian-resampling"
      ],
      "salient": "the recovered coefficient error is strictly below $1/2$",
      "page": "exact-recovery",
      "quote": {
        "source": "paper",
        "quote": "Section~\\ref{sec:assembly} removes\nthe known normalizations and digit scales, proves that the recovered\ncoefficient error is strictly below $1/2$, and propagates carries to\nobtain the exact binary product."
      }
    },
    {
      "id": "S7",
      "intention": "show",
      "claim": "The tape operations of the algorithm cost $O(V(\\lg n)^{1-\\kappa})$ in total, for stored volume $V=\\Theta(n)$.",
      "from": [],
      "method": "bound the cost of each tape procedure by a fixed power of its width below linear, then choose compatible fixed rational parameters",
      "motivation": {
        "text": "Each tape procedure costs a power of its width below linear, and one fixed choice of parameters must keep that saving through every layer.",
        "source": "recoverable"
      },
      "salient": "every term of the cost table has its power of the logarithm at most $1-\\kappa$, from one fixed choice of parameters",
      "adds": [
        {
          "symbol": "V",
          "name": "stored volume",
          "meaning": "the number of stored bits of the array",
          "relation": "count"
        },
        {
          "symbol": "d",
          "name": "chunk count",
          "meaning": "the number of equal-width address chunks in a butterfly layer",
          "relation": "count"
        },
        {
          "symbol": "\\lambda'",
          "name": "layer exponent",
          "meaning": "a fixed exponent below one bounding the butterfly layer cost",
          "relation": "direct"
        }
      ],
      "children": [
        {
          "id": "S7.1",
          "intention": "show",
          "claim": "Interchanging two equal address fields of width $u$ costs less than linear in $u$ per unit volume.",
          "from": [
            "linear-network",
            "role-streams",
            "frame",
            "address-shear",
            "subset-network",
            "subspace-labels",
            "recursive-saving"
          ],
          "method": "rank-saving recursion on a bit network whose smaller calls have total rank below the number of wires times the parameter",
          "motivation": {
            "text": "Because the sum of these ranks is less than the number of wires times $m$, the resulting recurrence saves a power of the chunk width.",
            "source": "explicit",
            "quote": {
              "source": "paper",
              "quote": "An edge matrix of rank $a$ will require $a$ smaller interchanges.\nBecause the sum of these ranks is less than the number of wires times\n$m$, the resulting recurrence saves a power of the chunk width."
            }
          },
          "adds": [
            {
              "symbol": "u",
              "name": "field width",
              "meaning": "the number of bits in each interchanged address field",
              "relation": "count"
            },
            {
              "symbol": "\\tau",
              "name": "interchange exponent",
              "meaning": "a fixed exponent below one bounding the interchange cost",
              "relation": "direct"
            }
          ],
          "page": "tape-interchange",
          "children": [
            {
              "id": "S7.1.1",
              "intention": "infer",
              "claim": "The address interchange costs $O(Vu^{\\tau})$ for a fixed $\\tau<1$.",
              "from": [],
              "quote": {
                "source": "paper",
                "quote": "Its cost is $O(Vu^\\tau)$ for a fixed $\\tau<1$."
              },
              "deferred": true
            }
          ]
        },
        {
          "id": "S7.2",
          "intention": "infer",
          "claim": "A simultaneous butterfly layer on $d$ equal-width chunks costs $O(Vd^{\\lambda'})$ for a fixed $\\lambda'<1$.",
          "from": [
            "gaussian-dyadic",
            "tape-interchange"
          ],
          "page": "butterfly-layer",
          "quote": {
            "source": "paper",
            "quote": "equal-width address chunks, and the cost is $O(Vd^{\\lambda'})$ for a"
          },
          "deferred": true
        },
        {
          "id": "S7.3",
          "intention": "infer",
          "claim": "Choosing compatible fixed rational parameters, with $\\kappa=2^{-182}$, makes every term of the cost table fit the bound $O(n(\\lg n)^{1-\\kappa})$.",
          "from": [
            "power-saving"
          ],
          "quote": {
            "source": "paper",
            "quote": "A compatible choice of rational\nparameters makes all terms in its cost table fit Theorem~\\ref{thm:main}."
          }
        }
      ]
    }
  ]
}
```

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Binding": {
      "additionalProperties": false,
      "description": "What a symbol in a concept's name denotes.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the title's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation"
      ],
      "type": "object"
    },
    "Evidence": {
      "additionalProperties": false,
      "properties": {
        "quote": {
          "description": "Text copied character for character from that source.",
          "type": "string"
        },
        "source": {
          "description": "Id of the source the quote comes from.",
          "type": "string"
        }
      },
      "required": [
        "source",
        "quote"
      ],
      "type": "object"
    },
    "Intention": {
      "oneOf": [
        {
          "const": "show",
          "description": "Show a claim by a method that splits it into sub-steps.",
          "type": "string"
        },
        {
          "const": "infer",
          "description": "Infer one claim in a single step the sources report.",
          "type": "string"
        }
      ]
    },
    "Motivation": {
      "additionalProperties": false,
      "description": "Why a method suits the claim it shows.",
      "properties": {
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an explicit motivation, the sources' words, copied exactly."
        },
        "source": {
          "$ref": "#/$defs/Provenance",
          "description": "Whether the sources state the reason, leave it to be worked out, or neither."
        },
        "text": {
          "description": "The reason, in one or two sentences.",
          "type": "string"
        }
      },
      "required": [
        "text",
        "source"
      ],
      "type": "object"
    },
    "Node": {
      "additionalProperties": false,
      "description": "One step of the argument.",
      "properties": {
        "adds": {
          "description": "Symbols the step introduces, in force in its sub-steps.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "children": {
          "description": "For a show step: its sub-steps, in the order the method takes them.",
          "items": {
            "$ref": "#/$defs/Node"
          },
          "type": "array"
        },
        "claim": {
          "description": "What the step shows or infers, in one sentence, with mathematics in LaTeX ($...$).",
          "type": "string"
        },
        "deferred": {
          "description": "For an infer step the sources report out of order, before or after the steps around\nit.",
          "type": "boolean"
        },
        "from": {
          "default": [],
          "description": "Ids of the concepts the step relies on: known concepts, or pages before the step's\npage.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "id": {
          "description": "A short label, unique in the tree, such as \"S0\" or \"S2.1\".",
          "type": "string"
        },
        "intention": {
          "$ref": "#/$defs/Intention"
        },
        "method": {
          "description": "For a show step: how the claim is shown, in a phrase (\"reduce to a cyclic\nconvolution and bound its cost\").",
          "type": [
            "string",
            "null"
          ]
        },
        "motivation": {
          "anyOf": [
            {
              "$ref": "#/$defs/Motivation"
            },
            {
              "type": "null"
            }
          ],
          "description": "For a show step: why that method suits the claim."
        },
        "page": {
          "description": "Id of the page that presents this step and its sub-steps, if one does.",
          "type": [
            "string",
            "null"
          ]
        },
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an infer step: the step as the sources report it, copied exactly."
        },
        "salient": {
          "description": "For a step whose claim has a feature a reader would find striking (a symmetry, a\nuniformity across cases, a surprising value or bound): that feature. The page should\nexplain why it holds, from a matching feature of the method.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "intention",
        "claim"
      ],
      "type": "object"
    },
    "Provenance": {
      "oneOf": [
        {
          "const": "explicit",
          "description": "The sources state the reason; quote them.",
          "type": "string"
        },
        {
          "const": "recoverable",
          "description": "The sources do not state it, but a reader can work it out from what they say.",
          "type": "string"
        },
        {
          "const": "reconstructed",
          "description": "The sources neither state it nor make it recoverable: you supply it.",
          "type": "string"
        }
      ]
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "properties": {
    "root": {
      "$ref": "#/$defs/Node",
      "description": "The main step: to show the target result."
    }
  },
  "required": [
    "root"
  ],
  "title": "ArgumentAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0118-argument.answer.json`, then run `exegenius submit 0118-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
