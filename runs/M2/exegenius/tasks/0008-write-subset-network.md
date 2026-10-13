# exegenius task 0008-write-subset-network

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
- Tape streams, array order and controlled shifts
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomial ring, whose powers act as roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange networks with frames and roles
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

Concept: Three-subset networks with rank saving
Gloss: Finite networks built from three-element subsets whose gates and terminals carry nested subspaces so that the total number s of smaller calls is less than W times m.

## This page in the argument

The step: Networks from three-element subsets with nested subspaces at gates and terminals have total number $s$ of smaller calls less than $Wm$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: speed up the tape operations of the transform-based multiplication by a power of the logarithm, then assemble the multiplication (on [Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine](main-theorem.md))
- Two tape procedures cost $O(Vu^\tau)$ for interchanging address fields of $u$ bits and $O(Vd^{\lambda'})$ for a butterfly layer on $d$ chunks, with $\tau,\lambda'<1$, on bit volume $V$.; how: build fixed linear exchange networks with frames and subspaces, then recurse so that the number of smaller calls gives a power saving

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear exchange networks with frames and roles](linear-network-frames.md): Fixed linear networks that exchange two banks of values and restore auxiliary values, applied pointwise to arrays whose representations are changed by invertible frame operators.
  Shown as: Three-subset networks with rank saving *<predicate>* Linear exchange networks with frames and roles

## Pages that build on this one

- Recursive power saving: Recursion with s calls at parameter f on volume V/W, with s/W < m, yields a power-of-parameter saving over naive passes.

## Other pages you may link to

- [Convolution and multiplication by radix digits](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring.md)
- [Tape streams, array order and controlled shifts](tape-streams.md)
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

- "The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "Let $\mathcal T$ be the set of three-element subsets of $[h]$." (paper)

  > Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.

- "For arbitrary initial values of its auxiliary wires, a forward" (paper)

  > \begin{lemma}\label{lem:scalar-motifs} For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged. Performing a forward invocation from $X$ to $Y$ at stage 1, the inverse forward schedule from $Y$ to $X$ at stage 2, and a forward invocation from $X$ to $Y$ at stage 3 sends \[ (X_a,Y_a)\longmapsto(-Y_a,X_a) \] and restores every auxiliary value. In the bit construction this is the permutation exchanging $X_a$ and $Y_a$. \end{lemma}


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

Write the body to `exegenius/tasks/0008-write-subset-network.answer.md` and the JSON to `exegenius/tasks/0008-write-subset-network.answer.json`, then run `exegenius submit 0008-write-subset-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0008-write-subset-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
