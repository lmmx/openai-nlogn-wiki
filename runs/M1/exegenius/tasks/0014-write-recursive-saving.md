# exegenius task 0014-write-recursive-saving

Project directory: `/home/user/openai-nlogn-wiki/runs/M1` (paths below are relative to it)

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

For these sources: The reader has completed undergraduate computer science: asymptotic analysis, discrete mathematics (modular arithmetic, primes, basic number theory, finite sets, permutations), linear algebra over the reals and complex numbers (matrices, rank, invertibility, linear maps), and basic algorithm design including recursion, divide and conquer, recurrences, and the standard school and Karatsuba multiplication. They know Turing machines and tapes and probably the FFT as an algorithm, but not abstract algebra beyond basics, finite fields in depth, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture and prior multiplication algorithms
- O(n log n) multiplier as a subroutine
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal variable of the polynomials; its powers act as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly
  - $H_0$ (butterfly map): The map sending a pair (u,v) to ((u+v)/2,(u−v)/2).
- Signed packing (Kronecker substitution)
- Fixed-point precision, exact dyadics and error control
- Arrays on tape, address fields and volume
- Linear networks, roles and frames
- Finite networks from three-element subsets
- Lower triangular factorization and address shear
- Modular arithmetic and residue rings (also: congruences, Z/mZ, integers mod m, residues)
- Prime numbers and coprimality (also: coprime, relatively prime, gcd, distinct primes)
- Binary representation of integers (also: bits, base 2, radix representation, binary expansion)
- Matrices, linear maps and rank (also: linear transformation, invertible matrix, matrix rank, vector space)
- Permutations (also: bijections, reordering of indices, permutation matrix)
- Logarithms and exponents (also: lg, log base 2, powers of two)
- Recurrences and divide and conquer (also: recursion, recurrence relation, master theorem)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 FFT)
- Karatsuba and schoolbook multiplication (also: grade-school multiplication, O(n^2) multiplication, Karatsuba)
- Floating-point and rounding errors (also: rounding, truncation error, error bound, triangle inequality)
- Sets, products and tuples (also: Cartesian product, index sets, subsets, lexicographic order)
- Linear-time scanning of tapes (also: tape scan, sequential pass, copying on a tape)
- Asymptotic constants and small epsilon exponents (also: fixed constant, polylogarithmic factors, O(n^(1+eps)))

## This page

Concept: Recursive power saving s < Wm
Gloss: Using s calls at parameter f on volume V/W each, with s<Wm, makes the cost per volume grow by a factor below m when the parameter is multiplied by m, giving a power rather than linear growth.
Heading: Recursive saving $s<Wm$

The symbols in this page's heading denote (say so on the page):

- $s$ (smaller call count): The total number of smaller recursive calls used by the network.
- $W$ (role count): The number of wire roles among which rows are distributed.
- $m$ (parameter multiplier): The factor by which the recursion parameter grows in one level, the dimension of the fixed space.

## This page in the argument

The step: Since $s<Wm$, a recursion with $s$ calls on volume $V/W$ costs $O(V\cdot\text{parameter}^{\tau})$ with $\tau<1$ (explicitly $\tau=1-2^{-50}$).

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ evaluated by synthetic transforms, and speed up the two bottleneck tape operations (address interchange, butterfly layers) by a recursive power saving (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-result.md))
- Address interchange and simultaneous butterfly layers can be done with a power saving in the logarithmic factor.; how: Build fixed linear networks with frames whose total number of smaller calls satisfies $s<Wm$, then recurse

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Finite networks from three-element subsets](subset-networks.md): Construction using three-element subsets, gather, scatter and scratch wires, with nested subspaces at vertices so that the total number of smaller calls is below the number of roles times m.
  Shown as: Recursive power saving s < Wm *<predicate>* Finite networks from three-element subsets

## Pages that build on this one

- Fast address-chunk interchange: Interchanging two disjoint address fields of u bits in an array of volume V in time O(V u^τ) with τ<1, via XOR combinations of intermediate data that finally give an exact permutation.
- Fast simultaneous butterfly layers: Applying the butterfly on the same bit position of up to d address chunks at once, on complex polynomial records, in time O(V d^λ') with λ'<1, instead of d whole-array passes.

## Other pages you may link to

- [The n log n conjecture and prior multiplication algorithms](nlogn-conjecture.md)
- [Polynomial ring modulo y^r + 1](ring-ymr.md)
- [Two-point butterfly](butterfly.md)
- [Fixed-point precision, exact dyadics and error control](fixed-point-exactness.md)
- [O(n log n) multiplier as a subroutine](hh-multiplier.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays on tape, address fields and volume](array-streams.md)
- [Linear networks, roles and frames](linear-networks-frames.md)
- [Lower triangular factorization and address shear](lower-triangular-shear.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Discrete Fourier transform and cyclic convolution](dft-convolution.md)
- [Multiplication as convolution of radix digits](radix-convolution.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Assembly of the integer multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "The decisive property is that the total
number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "This strict inequality
is the source of the power saving." (paper)

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

Write the body to `exegenius/tasks/0014-write-recursive-saving.answer.md` and the JSON to `exegenius/tasks/0014-write-recursive-saving.answer.json`, then run `exegenius submit 0014-write-recursive-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-recursive-saving`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
