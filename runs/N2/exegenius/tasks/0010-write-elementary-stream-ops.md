# exegenius task 0010-write-elementary-stream-ops

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N2` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Omega, Theta), divide-and-conquer recurrences and standard algorithms including Karatsuba multiplication and the radix-two FFT for polynomial multiplication, and basic models of computation including multitape Turing machines. From discrete mathematics they know induction, sets and binomial coefficients, binary and two's-complement representation, primes, gcd, modular arithmetic and the Chinese remainder theorem. From a first linear algebra course they know vector spaces, bases, subspaces, matrices, invertibility, Gaussian elimination, permutation and diagonal matrices and projections, and from calculus the exponential and logarithm, geometric series, Newton's method and elementary error bounds such as the triangle inequality. They have not studied Fourier analysis beyond the FFT, abstract algebra beyond modular arithmetic, numerical analysis of fixed-point transforms, or research-level integer multiplication techniques such as Schönhage–Strassen, Nussbaumer transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- Modular arithmetic
- Gaussian dyadic numbers
- Normalized butterfly H₀ (also: butterfly layer)
  - $H_0$ (normalized butterfly): The two-point map sending (u,v) to ((u+v)/2,(u−v)/2).
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Harvey–van der Hoeven O(n log n) multiplier
  - $n$ (input bit length): The number of bits in each integer multiplied by the subroutine.
- Arrays as address-ordered tape streams (also: logical volume, address field, row)
- Polynomial ring modulo yʳ + 1
  - $\mathbb C$ (complex numbers): The field of complex coefficients of the polynomials.
  - $y$ (polynomial variable): The indeterminate whose powers serve as roots of unity.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Big-Omega and Big-Theta notation (also: Ω, Θ, asymptotic lower bound, tight bound)
- Worst-case running time (also: time complexity, T_A(n), worst-case cost, linear time)
- Logarithms, floor and ceiling (also: log₂, lg, natural logarithm, ⌊x⌋, ⌈x⌉)
- Exponential function (also: exp, e^x, Gaussian function exp(−x²))
- Euler's formula and complex roots of unity (also: e^{iθ}, primitive root of unity, ω = e^{2πi/n}, unit circle)
- Binary representation of integers (also: bin_k, val, base-2 representation, radix representation, positional notation, most significant bit)
- Two's complement (also: two's-complement words, signed binary integers)
- Fixed-point numbers and rounding (also: fixed-point arithmetic, truncation, rounding to the nearest integer, precision p bits)
- Integer division with remainder (also: quotient and remainder, Euclidean division, divisibility)
- Prime numbers and trial division (also: primes, odd prime, primality test)
- Greatest common divisor and coprimality (also: gcd, pairwise coprime, relatively prime, prime to q, Euclidean algorithm)
- Modular inverses and units (also: unit mod q, invertible residue, multiplicative inverse modulo q)
- Chinese remainder theorem (also: CRT, Chinese remainder, simultaneous congruences)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-2 FFT, butterfly)
- Polynomial evaluation and interpolation (also: Lagrange interpolation, point-value representation)
- Karatsuba multiplication (also: Karatsuba–Ofman algorithm, O(n^{log₂3}) multiplication)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree)
- Geometric series (also: geometric sum)
- Mathematical induction (also: proof by induction, inductive step)
- Sets, Cartesian products and lexicographic order (also: Cartesian product, lexicographic order, row-major order, tuples)
- Subsets and binomial coefficients (also: binom(h,3), k-subsets, combinations, intersection size)
- Permutations (also: bijection, permutation matrix, inverse permutation, reordering)
- Hamming weight (also: wt(x), number of ones, population count)
- Vector spaces, subspaces, bases and dimension (also: subspace, basis, dimension, span, linear independence, coordinate space)
- Invertible matrices and the general linear group (also: invertible matrix, nonsingular matrix, GL(m, F), matrix inverse, identity matrix)
- Gaussian elimination (also: row reduction, elementary row operations, triangular matrices)
- Diagonal matrices and pointwise products (also: diagonal operator, diag, Hadamard (entrywise) product, pointwise multiplication)
- Linear projections (also: projection onto U, projector, complementary subspace)
- Matrix transpose (also: transpose, matrix transposition, Aᵀ)
- Maximum norm and triangle inequality (also: sup norm, ℓ∞ norm, ‖x‖∞, triangle inequality, absolute value)
- Newton's method (also: Newton iteration, Newton reductions, reciprocal approximation)
- Depth-first traversal (also: depth-first schedule, depth-first search, recursion order)

## This page

Concept: Elementary stream operations
Gloss: Linear-time tape procedures that permute or move single radix digits of addresses, split and merge streams by a digit, and split whole rows cyclically into a fixed number of streams.

## Where the argument relies on this page

- For chunks of $e=m^k$ digits with enough rows, the bit network with recursive shears interchanges the chunks in $O(Ve^{\tau})$ time on fixed tapes. (on [Power-width chunk interchange](power-width-interchange.md))
- XORing selected bit $x$ into bit $y$ at regularly spaced positions of two chunks is done by cyclic shifts with a guard chunk plus deterministic repair of an explicitly bounded exceptional set. (on [Packed selected-bit addition](packed-selected-bit-addition.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Arrays as address-ordered tape streams](tape-array-layout.md): An array over a product of address fields is stored on tape in lexicographic order with addresses implicit, and its logical volume V is its number of stored data bits.
  Shown as: Elementary stream operations *<predicate>* Arrays as address-ordered tape streams

## Pages that build on this one

- Controlled shifts and rational scalings: In linear time a tape machine can add to an address field an offset computed from earlier fields, modulo its range, or multiply that field by a fixed rational unit.
- Power-width chunk interchange: For chunks of e = mᵏ digits with enough rows, splitting rows among the W roles and running the bit network with recursive shears interchanges the chunks in O(V e^τ) time on fixed tapes via a depth-first schedule.
- Packed selected-bit addition: XORing bit x into bit y at regularly spaced positions of two address chunks via eight cyclic shifts using a third guard chunk, then deterministically repairing the small explicitly identified set of exceptional addresses.

## Other pages you may link to

- [Polynomial ring modulo yʳ + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](butterfly-h0.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [n log n optimality conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [The field F₂ and XOR](binary-field-xor.md)
- [Matrices, linear maps and rank](linear-algebra-rank.md)
- [Linear networks, wires and roles](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Address shear](address-shear.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-element subset construction](subset-construction.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Symmetric bilinear forms and orthogonal complements](bilinear-forms.md)
- [Tensor products](tensor-products.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Volume-normalized recursion](volume-normalized-recurrence.md)
- [Rational matrix interface of the bit network](bit-network-interface.md)
- [Explicit exponents τ and σ](motif-exponents.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Fast address chunk interchange](chunk-interchange.md)
- [Two-point kernel C](phase-kernel-c.md)
- [Binary phase frames](phase-frames.md)
- [Binary phase interface of the complex network](binary-phase-interface.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Batched recursion for a common layer](layer-recursion.md)
- [Guard width for exact layer evaluation](guard-width.md)
- [Disk grid values and truncation](fixed-point-grid.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Signed coefficient packing](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](multiplication-as-convolution.md)
- [Coefficient twist](coefficient-twist.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional Fourier transforms](multidimensional-dft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Transform layout and stored frequency order](transform-layout.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor resampling interface](tensor-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Chinese-remainder address map](crt-map.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Complete time bound](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:" (paper)

  > \begin{lemma}[Elementary stream operations] \label{lem:elementary-streams} Fix a radix $q\ge2$. Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes: \begin{enumerate} \item any fixed permutation of the pair of digit values at two specified radix-$q$ positions, whether or not the positions are adjacent; \item moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions; \item splitting on a specified radix-$q$ digit, applying a fixed pointwise map to aligned streams, and merging them back; \item for positive integers $P,R,B$, within each prefix of an array on $[P]\times[R]\times[B]$, splitting whole rows cyclically into a fixed number $W$ of streams, and, when $W$ divides $R$, merging those streams in any fixed order of the row classes. \end{enumerate} The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes. Their constants may depend on the fixed radix, the fixed pointwise map, and the fixed number of row classes. \end{lemma}

- "For headers that concatenate a list of positive integer parameters, we use the self-delimiting code" (paper)

  > For headers that concatenate a list of positive integer parameters, we use the self-delimiting code \begin{equation} b_v=\lfloor\log_2v\rfloor+1,\qquad \Gamma(v)=0^{b_v-1}\operatorname{bin}_{b_v}(v),\qquad |\Gamma(v)|=2b_v-1\quad(v\ge1). \label{eq:integer-descriptor-code} \end{equation} The initial zeroes specify how many further bits follow the first one, so concatenated codes can be read in order. We use this code when an interface specifies a header; elementary calls still receive the fixed number of canonical binary lengths described above.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
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
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0010-write-elementary-stream-ops.answer.md` and the JSON to `exegenius/tasks/0010-write-elementary-stream-ops.answer.json`, then run `exegenius submit 0010-write-elementary-stream-ops` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0010-write-elementary-stream-ops`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
