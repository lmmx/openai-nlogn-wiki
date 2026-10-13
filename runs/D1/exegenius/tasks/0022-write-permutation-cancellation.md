# exegenius task 0022-write-permutation-cancellation

Project directory: `/home/user/openai-nlogn-wiki/runs/D1` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic analysis, basic algorithm design (divide and conquer, recurrences, the idea of FFT-style multiplication at the level of knowing it exists), discrete math (modular arithmetic, primes, gcd, binary representation), and linear algebra (vectors, matrices, subspaces, rank, dimension, invertibility). They know complex numbers and polynomials, and basic multitape Turing machines. They have not studied the specialist material of the paper: Harvey-van der Hoeven machinery, Gaussian resampling, Bluestein, Chinese-remainder multidimensional reindexing, Bruhat factorization, or precise fixed-point error analysis.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution and cyclic convolution
- Discrete Fourier transform and roots of unity
- Two-point butterfly and fast transform levels
- Integer product as radix-digit convolution
- Known O(n log n) multiplier and the n log n conjecture
- Address fields, streams and scans on tape
- Fixed-point Gaussian dyadic records
- Polynomial ring modulo y^r+1
  - $y$ (ring variable): The formal variable of the polynomial ring, whose powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Signed packing (Kronecker substitution)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity and phase twist
- Linear exchange networks with roles and frames
- Three-element-subset subspace construction
- Recursive rank saving gives a power saving
- Address shear and triangular factorization
- Fast address-field interchange costing O(V u^τ)
  - $V$ (bit volume): The number of stored bits of the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (time exponent): A fixed constant strictly less than one in the cost exponent.
- Linear algebra over a field (also: vector space, subspace, dimension, rank, linear map, invertible matrix, matrix product)
- Modular arithmetic (also: residues, congruence, mod, bmod, integers modulo m, residue ring)
- Primes, gcd and coprimality (also: greatest common divisor, gcd, distinct primes, relatively prime, prime factorization)
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, bit position, lg n, base-2 logarithm)
- Logarithms, floor and ceiling (also: log, lg, floor, ceiling, iterated logarithm)
- Permutations (also: bijection, sorting a permutation, permutation of indices, inverse permutation)
- Mixed-radix and positional digit expansion (also: digits in base b, radix representation, index as digit tuple, lexicographic order, multi-index)
- Multidimensional arrays and tensors (also: multi-dimensional array, tensor product of transforms, axes, separable transform)
- Elementary Gaussian integers and dyadic rationals (also: dyadic rational, power-of-two denominators, Gaussian integer, fixed-point number)
- Norms, error bounds and rounding (also: triangle inequality, absolute value bound, operator norm, contraction, rounding to nearest integer, truncation error)
- Schoolbook carry addition (also: carry propagation, long multiplication, grade-school multiplication, linear-time addition)
- Geometric series and recurrences (also: recursion tree, divide and conquer recurrence, master theorem, summing powers)
- Roots of unity and Euler's formula (also: e^{2 pi i/n}, primitive n-th root, unit circle)
- Basic finite-set combinatorics (also: subsets of size three, counting subsets, binomial coefficient, intersection counting, inclusion-exclusion)
- Deterministic algorithms and tape scans (also: linear scan, copying between tapes, sorting on tape, merging)

## This page

Concept: Retaining permutations in the transform
Gloss: The source permutation from resampling cancels across the two forward transforms, the pointwise product and the inverse transform, avoiding separate full sorts.

## This page in the argument

The step: In the chirp identity the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two fast tape procedures (address interchange and simultaneous butterfly layers) with power savings, use them in synthetic transforms, and place those in the reduction of multiplication to convolution (on [Integer multiplication in O(n (lg n)^(1-κ))](main-result.md))
- Fourier transforms of pairwise coprime lengths reduce to power-of-two tensor transforms with the permutations retained in the transform formula.; how: Gaussian resampling with the source and target permutations kept inside the formula (on [Gaussian resampling](gaussian-resampling.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Gaussian resampling](gaussian-resampling.md): Harvey-van der Hoeven technique expressing a Fourier transform of prime length through a power-of-two tensor transform, with source and target permutations.
  Shown as: Retaining permutations in the transform *<predicate>* Gaussian resampling
- [Bluestein chirp identity and phase twist](bluestein-chirp.md): Rewriting a transform as a cyclic convolution via chirps; a phase twist turns the last cyclic axis into a negacyclic polynomial modulo y^r+1.
  Shown as: Retaining permutations in the transform *<predicate>* Bluestein chirp identity and phase twist
- [Synthetic polynomial transforms](synthetic-transform.md): Fourier transforms over the ring modulo y^r+1 using powers of y as roots, computed by signed shifts and butterflies and retaining one stored frequency order for the inverse.
  Shown as: Retaining permutations in the transform *<predicate>* Synthetic polynomial transforms

## Pages that build on this one

- Precision, rounding and carry recovery: Tracking contractive error bounds through all transforms so the recovered convolution coefficients err by less than 1/2, then rounding and propagating carries.
- Integer multiplication in O(n (lg n)^(1-κ)): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^(1-κ)) time with κ=2^-182, disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Known O(n log n) multiplier and the n log n conjecture](nlogn-multiplier.md)
- [Convolution and cyclic convolution](convolution.md)
- [Integer product as radix-digit convolution](radix-digit-reduction.md)
- [Address fields, streams and scans on tape](tape-layout-streams.md)
- [Fixed-point Gaussian dyadic records](fixed-point-dyadic.md)
- [Linear exchange networks with roles and frames](linear-network-frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Three-element-subset subspace construction](subset-intersection-network.md)
- [Recursive rank saving gives a power saving](recursive-power-saving.md)
- [Fast address-field interchange costing O(V u^τ)](address-interchange.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Discrete Fourier transform and roots of unity](dft.md)
- [Polynomial ring modulo y^r+1](negacyclic-ring.md)
- [Two-point butterfly and fast transform levels](butterfly.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Precision, rounding and carry recovery](precision-exact-recovery.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Simultaneous butterfly layer on selected bits](simultaneous-butterfly-layer.md)
- [Parameter choice and total cost accounting](parameter-cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1-κ))](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "the source permutation retained during resampling cancels
across the two forward source transforms, their pointwise product,
and the opposite-sign transform" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "=\frac{u*v}{S^2}." (paper)

  > \begin{lemma}[Chirp and permutation cancellation] \label{lem:chirp-permutation} With $R,Q,s_i,t_i$ as in Lemma~\ref{lem:tensor-resampling}, assume every $t_i$ is even. For $\boldsymbol j\in\mathbb Z^d$, define \[ a_{\boldsymbol j} =\exp\left(-\pi i\sum_{i=1}^d\frac{s_i j_i^2}{t_i}\right). \] Then $a$ has period $t_i$ in coordinate $i$, and \begin{equation} QF_{\boldsymbol t}u =\overline a\mathbin{\cdot} \frac{a*(\overline a\mathbin{\cdot}u)}{T}. \label{eq:permuted-chirp} \end{equation} If $S=\prod_i s_i$, then \begin{equation} (RF_{\boldsymbol s}^+) \bigl[(RF_{\boldsymbol s}u)\mathbin{\cdot} (RF_{\boldsymbol s}v)\bigr] =\frac{u*v}{S^2}. \label{eq:source-permutation-cancel} \end{equation} Complex conjugation of the input and output of an algorithm for $RF_{\boldsymbol s}$ gives an algorithm for $RF_{\boldsymbol s}^+$. \end{lemma}

- "P_sF_s=2^{2\alpha^2}B_0P_tF_tA." (paper)

  > \begin{lemma}[Resampling without executing the two permutations] \label{lem:no-sort-resampling} Fix $0<\delta<1/8$. Let $p>100$, $2\leq s<t<2^p$ and $2\leq\alpha<\sqrt p$ be integers, with $\gcd(s,t)=1$ and \[ \theta:=t/s-1>p/\alpha^4. \] Define coordinate permutations by \[ (P_su)_j=u_{tj},\qquad (P_tv)_k=v_{-sk}. \] There are linear contractions $A:\mathbb C^s\to\mathbb C^t$ and $B_0:\mathbb C^t\to\mathbb C^s$ satisfying \begin{equation} P_sF_s=2^{2\alpha^2}B_0P_tF_tA. \label{eq:no-sort-one-dimensional} \end{equation} There are fixed multitape algorithms for approximations $\widetilde A:\mathbb D_p^s\to\mathbb D_p^t$ and $\widetilde B_0:\mathbb D_p^t\to\mathbb D_p^s$, each with error less than $p^2$ and time \[ O(tp^{3/2+\delta}\alpha). \] The constant is uniform in $p,s,t,\alpha$. Inputs and outputs use the scalar component format above and occur in increasing coordinate order. \end{lemma}


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

Write the body to `exegenius/tasks/0022-write-permutation-cancellation.answer.md` and the JSON to `exegenius/tasks/0022-write-permutation-cancellation.answer.json`, then run `exegenius submit 0022-write-permutation-cancellation` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0022-write-permutation-cancellation`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
