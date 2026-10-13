# exegenius task 0009-write-recursive-power-saving

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
- Linear exchange networks with frames and roles
- Three-element subset construction with rank saving
- Address shear and lower triangular factorization
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

Concept: Recursive power saving from s < Wm
Gloss: A recursive call at parameter mf uses s calls at parameter f on volume V/W each, so the per-volume cost multiplies by s/W < m, giving cost V·(parameter)^θ with θ<1.

## This page in the argument

The step: Fixed linear exchange networks with $s<Wm$ give a recursion whose per-volume cost grows by a factor $s/W<m$ when the parameter is multiplied by $m$, hence cost $V\cdot(\text{parameter})^\theta$ with $\theta<1$.
How: Build a fixed network on $W$ roles with frames, label its gates by nested subspaces of an $m$-dimensional space so that the number $s$ of smaller calls is below $Wm$, then solve the recursion.
Why: The power saving comes only from a strict rank deficit across the edges of the network, so the argument must construct the network and its labels before the recursion can be analysed. (the sources say so: "is the source of the power saving. The later tape and arithmetic" (paper))
Striking feature: The saving is a power of the parameter, obtained from a strict inequality $s<Wm$ between two nearly equal quantities. (explain why it holds, from the method)

Its sub-steps, in order:

- With an invertible frame $D_v$ at each vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array. (on [Linear exchange networks with frames and roles](linear-network-frames.md))
- Labelling gates by subspaces of an $m$-dimensional space built from three-element subsets makes adjacent edge operators nested, so the total number $s$ of smaller calls is less than $Wm$. (on [Three-element subset construction with rank saving](subset-intersection-network.md))
- A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ with $W$ roles and label dimension $m$, so $s/W<m^\tau$ with $\tau<1$ and the cost is $V$ times a power of the parameter below $1$.

It serves these steps, from the main result down:

- Two $n$-bit integers are multiplied exactly by a deterministic fixed-tape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: Reduce the product to convolution through a chain of exact changes of representation, supply the movement and butterfly cost savings by two fast tape procedures, and assemble parameters, precision and cost. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3**: A call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ with $W$ roles and label dimension $m$, so $s/W<m^\tau$ with $\tau<1$ and the cost is $V$ times a power of the parameter below $1$.
Source: "\frac{s_{\rm b}}{W_{\rm b}}<m^\tau," (paper)
> The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Linear exchange networks with frames and roles](linear-network-frames.md)): With an invertible frame $D_v$ at each vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array.
- S2.2 (on [Three-element subset construction with rank saving](subset-intersection-network.md)): Labelling gates by subspaces of an $m$-dimensional space built from three-element subsets makes adjacent edge operators nested, so the total number $s$ of smaller calls is less than $Wm$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Three-element subset construction with rank saving](subset-intersection-network.md): Subspaces of an m-dimensional space labelled by three-element subsets, using gather/scatter and auxiliary wires, make adjacent edge operators nested so the total number s of smaller calls is less than W·m.
  Shown as: Recursive power saving from s < Wm *<predicate>* Three-element subset construction with rank saving

## Pages that build on this one

- Interchange of address chunks in time O(Vu^τ): Interchanging two disjoint contiguous u-bit address fields of an array by XOR combinations of intermediate data and the bit network, with exact final permutation for arbitrary auxiliary values.
- Fast simultaneous butterfly layer in time O(Vd^λ′): Applying H₀ to the same bit in d address chunks of the polynomial array in cost O(V d^λ′) instead of d full passes.

## Other pages you may link to

- [Fixed multitape machine model and scans](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](conjecture.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Address shear and lower triangular factorization](lower-triangular-shear.md)
- [Interchange of address chunks in time O(Vu^τ)](chunk-interchange.md)
- [Polynomial ring modulo y^r + 1](ring-y-r.md)
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
- [Phase frames for simultaneous butterflies](phase-frames.md)
- [Fast simultaneous butterfly layer in time O(Vd^λ′)](fast-butterfly-layer.md)
- [Synthetic transform layout and convolution](transform-layout.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations cancelling in transforms](retained-permutations.md)
- [Tensor resampling over growing dimension](tensor-resampling.md)
- [Compatible parameter choice and cost accounting](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "This strict inequality is the source of the power saving." (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.


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

Write the body to `exegenius/tasks/0009-write-recursive-power-saving.answer.md` and the JSON to `exegenius/tasks/0009-write-recursive-power-saving.answer.json`, then run `exegenius submit 0009-write-recursive-power-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0009-write-recursive-power-saving`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
