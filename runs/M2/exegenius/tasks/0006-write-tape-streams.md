# exegenius task 0006-write-tape-streams

Project directory: `/home/user/openai-nlogn-wiki/runs/M2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, discrete mathematics with modular arithmetic and primes, introductory linear algebra and probability-free algorithm design (divide and conquer, sorting, recursion with recurrences), complex numbers and polynomials, and basic Turing machines with tapes. They have likely seen the idea of the FFT only in passing, if at all, and have not studied abstract algebra, harmonic analysis, numerical error analysis or the Harvey-van der Hoeven line of work.

The reader already understands these concepts:

- Big-O notation
- Multitape Turing machine
- Complex numbers and polynomials
- Convolution and multiplication by radix digits
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomial ring, whose powers act as roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial record, a power of two.
- Euler's formula and roots of unity (also: e^{iθ}=cos θ+i sin θ, primitive roots of unity, complex exponential)
- Modular arithmetic and divisibility (also: congruences, residues mod m, gcd, coprime integers)
- Chinese remainder theorem (also: CRT)
- Prime numbers (also: primes, distinct primes, prime factorization)
- Binary representation and bit operations (also: bits, XOR, bit strings, two's complement, binary expansion)
- Radix-b representation of integers (also: base-b digits, positional notation, digit expansion)
- Schoolbook carry addition and multiplication (also: grade-school multiplication, carry propagation, long multiplication)
- Divide and conquer recurrences (also: master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Logarithms and exponentials (also: lg, log base 2, powers of two, iterated logarithm)
- Sums, products and summation manipulation (also: geometric series, sigma notation, index sets)
- Vectors, matrices and linear maps (also: linear algebra, matrix product, invertible matrix, basis, linear operator, vector space)
- Subspaces, dimension and rank (also: linear subspace, span, orthogonal complement, linear independence)
- Vector norms and the max norm (also: sup norm, infinity norm, triangle inequality, absolute value of complex number, modulus)
- Permutations and bijections (also: rearrangement, index permutation, one-to-one correspondence)
- Multidimensional arrays and index tuples (also: tensor indexing, array of arrays, Cartesian product of index sets, lexicographic order)
- Floating and fixed-point approximation and rounding (also: rounding to nearest integer, truncation, approximation error)
- Floor, ceiling and rounding functions (also: floor, ceiling, integer part)
- Real analysis basics: inequalities and exponential decay (also: Gaussian function, e^{-x^2}, tail bounds, sums of series)
- Dyadic rationals (also: dyadic numbers, binary fractions, numbers of form a/2^k)
- Cyclic and negacyclic indexing (also: indices mod q, wraparound, cyclic shift)
- Time complexity of sorting and merging on tapes (also: merge sort, sorting by passes, external sorting)

## This page

Concept: Tape streams, array order and controlled shifts
Gloss: Elementary linear-time scans, array layouts in lexicographic address order, whole-chunk moves and controlled shifts on tapes.

## Where the argument relies on this page

- A fixed linear network exchanging two banks of values and restoring auxiliary values acts pointwise on arrays via invertible frame operators that cancel along routes. (on [Linear exchange networks with frames and roles](linear-network-frames.md))
- Interchanging two disjoint address fields of $u$ bits on volume $V$ takes time $O(Vu^\tau)$ with exact final permutation. (on [Address interchange in time O(V u^τ)](address-interchange.md))
- Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the same bit in up to $d$ address chunks takes time $O(Vd^{\lambda'})$ using exact Gaussian dyadics and one final truncation. (on [Simultaneous butterfly layer in time O(V d^λ′)](simultaneous-butterfly.md))
- Exact multiplication of $n$-bit integers reduces, by a chain of changes of representation with parameters chosen consistently, to ring convolution, and the total cost is $O(n(\lg n)^{1-\kappa})$. (on [Assembly of the multiplication algorithm](multiplication-assembly.md))
- Normalized convolution over $\mathbb C[y]/(y^r+1)$ is computed with two forward synthetic transforms, a pointwise product by packed integer products, and the opposite transform in the same frequency order. (on [Normalized convolution over the polynomial ring with retained frequency order](ring-convolution.md))
- Synthetic polynomial transforms over the ring are computed by simultaneous butterfly layers on a suitable tape layout, keeping frequency order. (on [Synthetic polynomial transforms](synthetic-transform.md))

## Pages that build on this one

- Linear exchange networks with frames and roles: Fixed linear networks that exchange two banks of values and restore auxiliary values, applied pointwise to arrays whose representations are changed by invertible frame operators.
- Address interchange in time O(V u^τ): Interchanging two disjoint address fields of u bits via XOR combinations of intermediate streams, with exact final permutation.
- Chinese-remainder map to prime cyclic axes: Places the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- Normalized convolution over the polynomial ring with retained frequency order: Convolution computed by two forward synthetic transforms, a pointwise product via packed products, and the opposite transform, keeping the same frequency order throughout.

## Other pages you may link to

- [Convolution and multiplication by radix digits](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Three-subset networks with rank saving](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Address interchange in time O(V u^τ)](address-interchange.md)
- [Chinese-remainder map to prime cyclic axes](crt-map.md)
- [Fixed-point precision and error control](fixed-point-precision.md)
- [Simultaneous butterfly layer in time O(V d^λ′)](simultaneous-butterfly.md)
- [Discrete Fourier transform](dft.md)
- [The n log n optimality conjecture and prior bounds](nlogn-conjecture.md)
- [Multidimensional transform on power-of-two axes](tensor-transform.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Bluestein chirp identity](bluestein.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Normalized convolution over the polynomial ring with retained frequency order](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Assembly of the multiplication algorithm](multiplication-assembly.md)
- [Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "whole-chunk moves and controlled shifts" (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

- "A machine has one fixed finite alphabet and one fixed finite number of" (paper)

  > A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. A step reads and writes at most one cell on each tape and moves each head by at most one cell. Fixed tracks and finitely many work tapes change time by a fixed factor. We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow. The latter permutation will be realized in Section~\ref{sec:tape-interchange} by computing XOR combinations of intermediate data streams. The present section supplies the elementary scans it uses. Every scan includes its counters and the return of its tape heads.

- "Every scan includes its counters and the" (paper)

  > A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. A step reads and writes at most one cell on each tape and moves each head by at most one cell. Fixed tracks and finitely many work tapes change time by a fixed factor. We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow. The latter permutation will be realized in Section~\ref{sec:tape-interchange} by computing XOR combinations of intermediate data streams. The present section supplies the elementary scans it uses. Every scan includes its counters and the return of its tape heads.


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

Write the body to `exegenius/tasks/0006-write-tape-streams.answer.md` and the JSON to `exegenius/tasks/0006-write-tape-streams.answer.json`, then run `exegenius submit 0006-write-tape-streams` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0006-write-tape-streams`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
