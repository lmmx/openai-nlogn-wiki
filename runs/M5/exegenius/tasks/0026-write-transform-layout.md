# exegenius task 0026-write-transform-layout

Project directory: `/home/user/openai-nlogn-wiki/runs/M5` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: discrete mathematics (induction, sets, modular arithmetic, primes, permutations, binary representation), algorithm analysis with recurrences, and a first course in linear algebra (vector spaces, subspaces, dimension, invertible and triangular matrices). They know big-O, polynomials, complex numbers including roots of unity, and basic Turing machines with tapes. They have not studied the FFT-based multiplication literature, Schönhage–Strassen, Nussbaumer transforms, multitape complexity theory in depth, or numerical error analysis beyond basics.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Multitape Turing machine multiplication model
- Schönhage–Strassen n log n conjecture and history
- Radix digits and convolution
- Discrete Fourier transform
- Multidimensional transforms with power-of-two axes
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $\mathbb C$ (complex numbers): The coefficient field of the polynomials.
  - $y$ (ring variable): The polynomial variable, whose powers act as roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial, a power of two.
- Phase twist to the polynomial ring
- Synthetic polynomial transforms
- Two-point butterfly
- Signed packing (Kronecker substitution)
- Tape array order and elementary stream operations
- Linear network with roles and frames
- Finite networks from three-element subsets
- Restoring auxiliary values
- Recursive power saving
- Address shear and triangular factorization
- Fast address-field interchange
- Simultaneous butterfly layer
- Fixed-point Gaussian dyadics and exact recovery
- Modular arithmetic and congruences (also: mod, residues, congruence mod m)
- Prime numbers and coprimality (also: distinct primes, gcd, relatively prime)
- Binary representation and bit operations (also: bits, XOR, binary expansion, most significant bit)
- Floors, ceilings and logarithms (also: lg, log base 2, ceil, floor)
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω)
- Vector spaces, subspaces and dimension (also: linear subspace, span, basis, linear independence)
- Matrices, invertibility and linear maps (also: invertible matrix, matrix product, triangular matrix, linear operator, identity matrix)
- Permutations and bijections (also: permutation of indices, one-to-one correspondence)
- Cartesian products and index tuples (also: multi-index, array indexed by tuples, product set)
- Mathematical induction and recurrences (also: recursion, recurrence relation, divide and conquer analysis, induction)
- Schoolbook multiplication and linear-time addition (also: grade-school multiplication, quadratic multiplication, long multiplication, carry addition)
- Cyclic and negacyclic indexing (also: wraparound indices, indices mod N, cyclic group Z/NZ)
- Dyadic rationals and fixed-point numbers (also: binary fractions, fixed point, power-of-two denominators)
- Sup norm and rounding error bounds (also: max norm, infinity norm, rounding to nearest integer, truncation error)
- Real and imaginary parts, complex conjugate and modulus (also: Re, Im, absolute value of a complex number, Gaussian integers)
- Summation, geometric series and inequalities (also: sum notation, geometric sums, triangle inequality)

## This page

Concept: Transform layout with retained frequency order
Gloss: Layout on tape in which forward synthetic transforms keep the same frequency order through pointwise product and the opposite transform consumes it.

## This page in the argument

The step: The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly by a deterministic multitape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce multiplication through a chain of convolution problems down to polynomial-ring convolution, evaluated with the fast tape procedures (on [Multiplying n-bit integers in O(n (lg n)^(1-κ)) time](target.md))
- Convolution over the polynomial ring on the remaining axes is computed with synthetic transforms in retained frequency order and packed polynomial products.; how: use synthetic transforms for the evaluation and signed packing for the pointwise products

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transforms](synthetic-transforms.md): Nussbaumer-style transforms using powers of y as roots of unity, so root multiplications are signed shifts of coefficient lists.
  Shown as: Transform layout with retained frequency order *<predicate>* Synthetic polynomial transforms
- [Simultaneous butterfly layer](fast-butterfly-layer.md): Applies H0 simultaneously on the same bit position in d address chunks of numerical arrays, cost O(V d^λ') with λ'<1, with a single truncation after the layer.
  Shown as: Transform layout with retained frequency order *<predicate>* Simultaneous butterfly layer
- [Fast address-field interchange](address-interchange.md): Interchanges two disjoint contiguous address fields of u bits in an array of stored bit volume V in time O(V u^τ) with τ<1, using XOR combinations of data.
  Shown as: Transform layout with retained frequency order *<predicate>* Fast address-field interchange
- [Signed packing (Kronecker substitution)](signed-packing.md): Packs polynomial coefficients into one integer so a polynomial product is computed by an ordinary integer multiplier.
  Shown as: Transform layout with retained frequency order *<predicate>* Signed packing (Kronecker substitution)

## Pages that build on this one

- Multiplying n-bit integers in O(n (lg n)^(1-κ)) time: Deterministic multitape algorithm combining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, synthetic transforms with fast tape procedures, and carries.

## Other pages you may link to

- [Multitape Turing machine multiplication model](multitape-model.md)
- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Radix digits and convolution](convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transforms with power-of-two axes](multidimensional-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Two-point butterfly](butterfly.md)
- [Fixed-point Gaussian dyadics and exact recovery](fixed-point-precision.md)
- [Tape array order and elementary stream operations](tape-streams.md)
- [Linear network with roles and frames](linear-network.md)
- [Restoring auxiliary values](restored-auxiliaries.md)
- [Address shear and triangular factorization](address-shear.md)
- [Finite networks from three-element subsets](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase twist to the polynomial ring](phase-twist.md)
- [Rescaling and carry propagation](carry-propagation.md)
- [Multiplying n-bit integers in O(n (lg n)^(1-κ)) time](target.md)

## Evidence from the sources, with the paragraph around each quote

- "retain the same frequency order through their pointwise product" (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.

- "Transform layout and cost" (paper)

  > \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.


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

Write the body to `exegenius/tasks/0026-write-transform-layout.answer.md` and the JSON to `exegenius/tasks/0026-write-transform-layout.answer.json`, then run `exegenius submit 0026-write-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0026-write-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
