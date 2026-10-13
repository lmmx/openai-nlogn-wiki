# exegenius task 0006-write-cyclic-convolution

Project directory: `/home/user/openai-nlogn-wiki/runs/C5` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis, algorithm design basics (divide and conquer, recurrences, schoolbook and Karatsuba multiplication), discrete mathematics (modular arithmetic, primes, induction, permutations), and linear algebra and calculus at the usual first-course level. They know polynomials, complex numbers with roots of unity, and simple Turing machines with tapes. They have not studied the FFT in depth, Fourier analysis on groups, tensor products, numerical analysis, or fast integer multiplication research.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Discrete Fourier transform and roots of unity
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial; a power of two.
- Logarithms and iterated logarithm notation (also: lg, log base 2, log n, lg n)
- Floor, ceiling and rounding (also: floor, ceiling, nearest integer)
- Binary representation and bit operations (also: bits, binary expansion, XOR, bitwise exclusive or, bit fields)
- Radix (base-b) expansion (also: digits in base b, positional notation, radix digits)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, carry propagation)
- Divide and conquer recurrences (also: recurrence relations, master theorem, Karatsuba)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/NZ)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd, coprime)
- Permutations and bijections (also: rearrangement, one-to-one correspondence, bijective map)
- Vectors, matrices and linear maps (also: linear operator, invertible matrix, matrix inverse, linear combination, linear algebra)
- Subspaces, dimension and rank (also: linear subspace, span, rank of a matrix, basis)
- Vector spaces over GF(2) (also: binary vectors, F_2, bit vectors, mod 2 linear algebra)
- Triangular matrices and elimination (also: lower-triangular matrix, Gaussian elimination, LU factorization)
- Norms and triangle inequality (also: absolute value of complex number, modulus, magnitude, vector norm, error bound)
- Exponential function and Euler's formula (also: e^{i theta}, complex exponential, exp, Gaussian function)
- Fixed-point and finite-precision numbers (also: dyadic rationals, truncation, rounding error, binary fractions)
- Direct sum and product of index sets (also: Cartesian product, multi-index, array indexing, row-major order)
- Deterministic algorithms and upper/lower bounds (also: deterministic, worst-case time, upper bound, optimality)
- Induction and proofs by recursion (also: mathematical induction, recursive argument, inductive proof)
- Constants, exponents and power-of-two sizes (also: power of two, 2^k, padding to a power of two)

## This page

Concept: Convolution and the convolution theorem
Gloss: Multiplying polynomials (mod x^N−1 for cyclic) by transforming, multiplying pointwise, and inverse transforming; integer multiplication reduces to it by splitting into radix digits.

## Where the argument relies on this page

- Forward synthetic transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, at the layer-based cost. (on [Synthetic transforms with retained frequency order](fast-synthetic-transform.md))
- The source and target permutations stay in the transform identity and cancel across forward, product and inverse transforms. (on [Resampling with permutations left in the transform](retained-permutations.md))
- The exact product is recovered by the chain of reductions and its cost is $O(n(\lg n)^{1-\kappa})$. (on [Assembling the exact product](multiplication-assembly.md))
- A Chinese-remainder address map places the digit list on distinct prime cyclic axes preserving convolution. (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Discrete Fourier transform and roots of unity](dft-roots-of-unity.md): Evaluating a polynomial at all powers of a root of unity; the fast version is the FFT, built from layers of two-point butterflies.
  Shown as: Convolution and the convolution theorem *<predicate>* Discrete Fourier transform and roots of unity

## Pages that build on this one

- Multidimensional transforms: A transform on an array with several axes, applied axis by axis; axis lengths such as primes or powers of two determine cost and layout.
- Bluestein chirp identity: Rewrites a transform as a cyclic convolution by multiplying by chirp phases.
- Phase twist to the negative-wrap ring: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y-r-plus-1.md)
- [Multidimensional transforms](multidimensional-transform.md)
- [Two-point butterfly H₀](butterfly-layer.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase twist to the negative-wrap ring](phase-twist.md)
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [The n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier](hh-multiplier.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Array addresses, fields and tape layout](address-fields-layout.md)
- [Linear networks with restored auxiliary values](linear-network.md)
- [Frames of a linear network](frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Subset-intersection subspace labels](subset-subspace-labels.md)
- [Recursive power saving from s<Wm](recursive-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Resampling with permutations left in the transform](retained-permutations.md)
- [Synthetic transforms with retained frequency order](fast-synthetic-transform.md)
- [Assembling the exact product](multiplication-assembly.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "\begin{proposition}[Convolution from the retained transform layout]" (paper)

  > \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.


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

Write the body to `exegenius/tasks/0006-write-cyclic-convolution.answer.md` and the JSON to `exegenius/tasks/0006-write-cyclic-convolution.answer.json`, then run `exegenius submit 0006-write-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0006-write-cyclic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
