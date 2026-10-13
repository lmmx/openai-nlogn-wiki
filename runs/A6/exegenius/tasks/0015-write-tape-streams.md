# exegenius task 0015-write-tape-streams

Project directory: `/home/user/openai-nlogn-wiki/runs/A6` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied discrete mathematics, algorithms (divide and conquer, fast multiplication such as Karatsuba, the FFT at a basic level), linear algebra, and elementary number theory and probability. They know asymptotic notation, binary and positional number representation, polynomials and complex numbers, and basic Turing machines. They have not studied multitape complexity details, advanced harmonic analysis, algebraic number theory, or the research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Basic Turing machines and tapes
- Fixed multitape Turing machine model
- Multiplication history and the n log n conjecture
- Multiplication as convolution of radix digits
- Fourier transforms and butterfly operations
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial indeterminate whose powers act as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transforms
- Gaussian resampling
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp conversion
- Phase twist to the polynomial ring
- Signed packing of polynomial products
- Binary representation and radix digits (also: base-b expansion, positional notation, bit strings, most significant bit)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, remainder)
- Prime numbers and coprimality (also: distinct primes, gcd, relatively prime, prime factorization)
- Logarithms and powers of two (also: lg, log base 2, ceiling and floor)
- Schoolbook multiplication and convolution of sequences (also: discrete convolution, polynomial multiplication, Cauchy product)
- Karatsuba and divide-and-conquer multiplication (also: Karatsuba, Toom-Cook, divide and conquer)
- Fast Fourier transform basics (also: FFT, Cooley-Tukey, roots of unity)
- Linear algebra over the reals and complex numbers (also: vector space, matrix, linear map, invertible matrix, subspace, dimension, linear combination)
- Direct product of sets and multidimensional arrays (also: Cartesian product, tensor array, index tuple, multi-index)
- Permutations and bijections (also: rearrangement, bijection, identity permutation, involution)
- Cyclic groups and Z/mZ (also: cyclic group, integers modulo m, cyclic index)
- Fixed-point and rounding arithmetic (also: fixed point, rounding error, truncation, dyadic rationals)
- Error bounds and the triangle inequality (also: sup norm, max norm, absolute value bound, norm)
- Binary XOR and bitwise operations (also: xor, exclusive or, bit shift, bit masks)
- Basic counting and combinatorics (also: binomial coefficient, subsets, inclusion-exclusion, pigeonhole)
- Induction and recurrences (also: recurrence relation, recursion, master theorem, mathematical induction)
- Real analysis basics: inequalities and exponentials (also: Taylor series, exponential function, Euler's formula, Gaussian function)
- Ring and group axioms (also: commutative ring, algebra, ring homomorphism, quotient ring)

## This page

Concept: Array order, streams and controlled shifts
Gloss: Elementary tape operations: scanning arrays in address order, stream operations and controlled shifts/rational scalings that cost linear time.

## This page in the argument

The step: Elementary tape operations (scans in address order, stream operations, controlled shifts) cost linear time.

It serves these steps, from the main result down:

- A multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: chain reductions from the integer product to a convolution over $\mathbb C[y]/(y^r+1)$, compute it with accelerated synthetic transforms, then recover the exact product (on [Integer multiplication in O(n (lg n)^{1-κ}) time](main-result.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed exactly and fast.; how: use synthetic transforms whose twiddles are signed shifts, accelerated by the fast tape procedures, with polynomial products by signed packing (on [Synthetic polynomial transforms](synthetic-transforms.md))
- The synthetic-transform address rearrangements and butterfly layers can be done faster than by scanning the whole array at each of $\Theta(\log n)$ levels.; how: build two tape procedures from linear networks and a recursive power saving

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fixed multitape Turing machine model](multitape-model.md): Deterministic Turing machine with fixed finite alphabet and fixed finite number of one-dimensional tapes; the cost model where time counts bit-level tape steps and scans of n stored bits cost Θ(n).
  Shown as: Array order, streams and controlled shifts *<predicate>* Fixed multitape Turing machine model

## Pages that build on this one

- Linear networks with roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliaries; wires are roles, rows are distributed among W roles, and invertible frames D_v change array representation so intermediate frames cancel.
- Fast interchange of address chunks: Interchanges two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) with τ<1, via XOR combinations and address shears, yielding an exact permutation.

## Other pages you may link to

- [Multiplication history and the n log n conjecture](nlogn-conjecture-history.md)
- [Multiplication as convolution of radix digits](convolution-reduction.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod.md)
- [Fourier transforms and butterfly operations](fourier-transform-butterflies.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Phase twist to the polynomial ring](phase-twist.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Finite networks from three-element subsets](subset-intersection-network.md)
- [Recursive power saving](recursive-power-saving.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Fast simultaneous butterfly layers](simultaneous-butterfly.md)
- [Precision, error bound and exact recovery](precision-exact-recovery.md)
- [Integer multiplication in O(n (lg n)^{1-κ}) time](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "\section{The machine model and elementary streams}" (paper)

  > Integer operations and random access on $O(\log(n+2))$-bit words have unit cost, with a fixed number of words for each address or integer. The model supplies one specified Fourier root $\zeta_{D_*}$ of explicitly computable order $D_*<1024n^3$. Scalar preparation, schedule construction, and index work are charged. This is a separate application of the finite network, with its own uniform array implementation. It is neither a bit-complexity consequence nor a stable floating-point FFT consequence of the fixed-tape multiplication theorem, Theorem~\ref{thm:main}. \section{The machine model and elementary streams} \label{sec:streams}

- "Controlled shifts and fixed rational scalings" (paper)

  > \begin{lemma}[Controlled shifts and fixed rational scalings] \label{lem:ordered-affine-streams} Fix a prime $q$, a fixed number of control fields, and finitely many rational coefficients whose denominators are prime to $q$. Whenever a coefficient is used as a unit, also require its numerator to be prime to $q$. Put $Q=q^b$, $b\ge1$. Suppose a target field $y\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits. An update \[ y\longmapsto y+a(\text{controls})\pmod Q \] costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values. In particular, this holds for a fixed rational linear combination of them, specialized modulo $Q$. Multiplication of $y$ by any of the specified rational units, and its inverse, also costs $O(V)$. Arbitrarily long intervening spectator fields and suffix records are permitted. \end{lemma}


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

Write the body to `exegenius/tasks/0015-write-tape-streams.answer.md` and the JSON to `exegenius/tasks/0015-write-tape-streams.answer.json`, then run `exegenius submit 0015-write-tape-streams` in the project directory. If submit rejects the answer, fix the answer and submit again.
