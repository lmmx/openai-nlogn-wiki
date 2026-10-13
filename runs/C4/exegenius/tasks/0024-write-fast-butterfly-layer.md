# exegenius task 0024-write-fast-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/C4` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science core: asymptotic analysis and recurrences, algorithms and data structures (divide and conquer, FFT-style ideas at the level of an algorithms course), discrete mathematics (modular arithmetic, binary representation, induction, basic combinatorics), and linear algebra (vectors, matrices, bases, invertible maps, subspaces over the reals and complex numbers). They know basic Turing machines with tapes, but not multitape time-complexity subtleties, the Schönhage–Strassen or Harvey–van der Hoeven methods, number-theoretic transforms in depth, or any research-level algebra or numerical analysis.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed multitape machine model and scans
- Schönhage–Strassen n log n conjecture and history
- Discrete Fourier transform and cyclic convolution
- Multiplication as convolution of radix digits
- Signed Kronecker packing
- Harvey–van der Hoeven O(n log n) multiplier as subroutine
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $y$ (indeterminate): The formal variable of the polynomials.
  - $r$ (ring size): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Phase twist to the polynomial ring
- Fixed-point precision and exact recovery
- Exact Gaussian dyadic arithmetic with single truncation
- Simultaneous butterfly layer H₀
  - $H_0$ (butterfly map): The map sending a pair of values to their half-sum and half-difference.
  - $u$ (first value): The first input of the two-point butterfly.
  - $v$ (second value): The second input of the two-point butterfly.
- Linear exchange networks with frames and roles
- Three-element subset construction with rank saving
- Recursive power saving from s < Wm
- Address shear and lower triangular factorization
- Interchange of address chunks in time O(Vu^τ)
  - $V$ (bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant less than 1 in the cost exponent.
- Phase frames for simultaneous butterflies
- Binary representation and bit operations (also: bits, XOR, binary expansion, bit strings)
- Modular arithmetic (also: congruences, mod, residues, integers modulo m)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, primes)
- Matrices and linear maps (also: linear algebra, invertible matrix, linear operator, change of basis, tensor product of vectors)
- Vector spaces over finite fields (also: F_2 vector space, subspace, dimension, rank, GF(2))
- Norms and triangle inequality (also: max norm, sup norm, operator norm, modulus bound)
- Floor, ceiling, rounding and logarithms (also: lg, log base 2, nearest integer, rounding)
- Recurrences and divide and conquer (also: recursion, recursive cost analysis, master theorem, recursion depth)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 butterfly)
- Euler's formula and exponentials of complex numbers (also: e^{2 pi i/q}, unit circle, phase, primitive roots of unity)
- Gaussian function and Gaussian sums (also: Gaussian, normal curve, exp(-x^2), Gaussian weight)
- Geometric series and exponential decay bounds (also: geometric sum, tail bound, exponential tail)
- Tuples, products of sets and mixed-radix indexing (also: Cartesian product, multi-index, coordinates, array indexing, tensor array)
- Permutations (also: bijection, reordering, coordinate permutation)
- Cyclic groups and direct products (also: Z/qZ, cyclic shift, cyclic axes, abelian group)
- Real and complex number approximation (also: rational approximation, dyadic rational, truncation error, error propagation)
- Big-O variants and constants (also: little-o, Theta, Omega, implied constant, sufficiently large)
- Induction and proof by recursion (also: mathematical induction, proof by induction)
- Diagonal matrices (also: diagonal operator, pointwise multiplication, entrywise scaling)

## This page

Concept: Fast simultaneous butterfly layer in time O(Vd^λ′)
Gloss: Applying H₀ to the same bit in d address chunks of the polynomial array in cost O(V d^λ′) instead of d full passes.
Heading: Simultaneous butterfly layer in time $O(Vd^{\lambda'})$

The symbols in this page's heading denote (say so on the page):

- $V$ (bit volume): The logical number of stored bits in the array.
- $d$ (chunk count): The number of selected address chunks, at most the bound on active axes.
- $\lambda'$ (saving exponent): A fixed constant less than 1.

## This page in the argument

The step: A butterfly layer $H_0$ on the same bit of $d$ address chunks of a polynomial array of volume $V$ costs $O(Vd^{\lambda'})$ with $\lambda'<1$, instead of $d$ full passes.
How: Apply the complex network to a tensor product of an auxiliary kernel using phase frames, bound the exact dyadic intermediate values, then convert to $H_0$ with a single truncation.
Why: Separate butterfly factors would need $D$ whole-array passes; the same rank-saving recursion over selected bits gives a power saving in the number of chunks. (the sources say so: "whereas separate butterfly factors" (paper))
Striking feature: The cost exponent $\lambda'$ is below $1$ uniformly in the number of chunks, versus linear cost for separate factors. (explain why it holds, from the method)

Its sub-steps, in order:

- The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied coefficientwise to selected bits of many address chunks, as a tensor product over $d$ chunks. (on [Simultaneous butterfly layer H₀](butterfly-h0.md))
- Diagonal phase frames express a tensor product of the auxiliary kernel $C$ on many selected bits via smaller groups of bits separated by binary changes of basis done by moving whole chunks. (on [Phase frames for simultaneous butterflies](phase-frames.md))
- All intermediate values are exact Gaussian dyadics, and the layer is evaluated exactly before one truncation. (on [Exact Gaussian dyadic arithmetic with single truncation](gaussian-dyadics.md))
- The layer over $d$ chunks costs $O(Vd^{\lambda'})$ with $\lambda'<1$.

It serves these steps, from the main result down:

- Two $n$-bit integers are multiplied exactly by a deterministic fixed-tape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: Reduce the product to convolution through a chain of exact changes of representation, supply the movement and butterfly cost savings by two fast tape procedures, and assemble parameters, precision and cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.4**: The layer over $d$ chunks costs $O(Vd^{\lambda'})$ with $\lambda'<1$.
Source: "coefficient order, and component format in $O(Vd^{\lambda'})$ time," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.1 (on [Simultaneous butterfly layer H₀](butterfly-h0.md)): The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied coefficientwise to selected bits of many address chunks, as a tensor product over $d$ chunks.
- S4.2 (on [Phase frames for simultaneous butterflies](phase-frames.md)): Diagonal phase frames express a tensor product of the auxiliary kernel $C$ on many selected bits via smaller groups of bits separated by binary changes of basis done by moving whole chunks.
- S4.3 (on [Exact Gaussian dyadic arithmetic with single truncation](gaussian-dyadics.md)): All intermediate values are exact Gaussian dyadics, and the layer is evaluated exactly before one truncation.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Phase frames for simultaneous butterflies](phase-frames.md): Diagonal phase frames express a tensor product of the auxiliary kernel C on many selected bits via smaller groups of bits separated by binary changes of basis implemented as whole-chunk moves.
  Shown as: Fast simultaneous butterfly layer in time O(Vd^λ′) *<predicate>* Phase frames for simultaneous butterflies
- [Recursive power saving from s < Wm](recursive-power-saving.md): A recursive call at parameter mf uses s calls at parameter f on volume V/W each, so the per-volume cost multiplies by s/W < m, giving cost V·(parameter)^θ with θ<1.
  Shown as: Fast simultaneous butterfly layer in time O(Vd^λ′) *<predicate>* Recursive power saving from s < Wm
- [Polynomial ring modulo y^r + 1](ring-y-r.md): The ring of polynomials over ℂ modulo y^r+1, where powers of y are roots of unity and multiplication by y^a is a signed cyclic shift of coefficients; norm is the max coefficient modulus.
  Shown as: Fast simultaneous butterfly layer in time O(Vd^λ′) *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Synthetic transform layout and convolution: Layout on tape on which the parallel layers apply and the pointwise-multiplied transforms are inverted, with polynomial products by signed packing and the Harvey–van der Hoeven multiplier.

## Other pages you may link to

- [Fixed multitape machine model and scans](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](conjecture.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Address shear and lower triangular factorization](lower-triangular-shear.md)
- [Three-element subset construction with rank saving](subset-intersection-network.md)
- [Interchange of address chunks in time O(Vu^τ)](chunk-interchange.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hvdh-multiplier.md)
- [Discrete Fourier transform and cyclic convolution](dft-convolution.md)
- [Multiplication as convolution of radix digits](radix-digit-convolution.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase twist to the polynomial ring](phase-twist.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Exact Gaussian dyadic arithmetic with single truncation](gaussian-dyadics.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Simultaneous butterfly layer H₀](butterfly-h0.md)
- [Synthetic transform layout and convolution](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancelling in transforms](retained-permutations.md)
- [Tensor resampling over growing dimension](tensor-resampling.md)
- [Compatible parameter choice and cost accounting](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We will obtain cost $O(Vd^{\lambda'})$" (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.


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

Write the body to `exegenius/tasks/0024-write-fast-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0024-write-fast-butterfly-layer.answer.json`, then run `exegenius submit 0024-write-fast-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0024-write-fast-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
