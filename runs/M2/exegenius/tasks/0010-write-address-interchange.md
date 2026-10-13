# exegenius task 0010-write-address-interchange

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
- Three-subset networks with rank saving
- Recursive power saving
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

Concept: Address interchange in time O(V u^τ)
Gloss: Interchanging two disjoint address fields of u bits via XOR combinations of intermediate streams, with exact final permutation.
Heading: Address interchange in time $O(Vu^\tau)$

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): The number of stored bits in the array.
- $u$ (field width): The number of bits in each of the two interchanged address fields.
- $\tau$ (interchange exponent): A fixed constant less than 1 giving the power saving.

## This page in the argument

The step: Interchanging two disjoint address fields of $u$ bits on volume $V$ takes time $O(Vu^\tau)$ with exact final permutation.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: speed up the tape operations of the transform-based multiplication by a power of the logarithm, then assemble the multiplication (on [Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine](main-theorem.md))
- Two tape procedures cost $O(Vu^\tau)$ for interchanging address fields of $u$ bits and $O(Vd^{\lambda'})$ for a butterfly layer on $d$ chunks, with $\tau,\lambda'<1$, on bit volume $V$.; how: build fixed linear exchange networks with frames and subspaces, then recurse so that the number of smaller calls gives a power saving

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving](recursive-saving.md): Recursion with s calls at parameter f on volume V/W, with s/W < m, yields a power-of-parameter saving over naive passes.
  Shown as: Address interchange in time O(V u^τ) *<predicate>* Recursive power saving
- [Tape streams, array order and controlled shifts](tape-streams.md): Elementary linear-time scans, array layouts in lexicographic address order, whole-chunk moves and controlled shifts on tapes.
  Shown as: Address interchange in time O(V u^τ) *<predicate>* Tape streams, array order and controlled shifts

## Pages that build on this one

- Simultaneous butterfly layer in time O(V d^λ′): Applies H0(u,v)=((u+v)/2,(u-v)/2) coefficientwise on the same bit in up to d address chunks, using exact Gaussian dyadics and one final truncation.
- Assembly of the multiplication algorithm: Chains digit convolution, CRT, Gaussian resampling, chirps, twist to the polynomial ring, rescaling, rounding and carry propagation, with parameters chosen so the cost table fits the theorem.

## Other pages you may link to

- [Convolution and multiplication by radix digits](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Three-subset networks with rank saving](subset-network.md)
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

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "an address shear" (paper)

  > For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$. Two further linear-cost address updates complete their interchange. For the numerical procedure, the endpoint operator becomes the simultaneous $H_0$ layer after diagonal phase operations and a dyadic scale. The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure.

- "Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization" (paper)

  > \begin{lemma}[Lower triangular factorization] \label{lem:lower-lower} Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization \[ A=E_1\Pi E_2, \] where $E_1,E_2$ are invertible lower triangular rational matrices and $\Pi$ has exactly $a$ entries equal to one, with at most one in each row and column, and all remaining entries zero. \end{lemma}

- "can be performed with exactly $a$ interchanges of pairs of $b$-digit" (paper)

  > \begin{lemma}[The cost of a rational matrix shear] \label{lem:matrix-shear} Let $\mathcal A$ be a fixed finite collection of rational $m\times m$ matrices. There is a fixed odd prime $q$ such that the following holds. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two ordered groups of fields, every field ranging over $[q^b]$, with every $H_i$ before every $D_j$. For $A\in\mathcal A$ of rational rank $a$, the permutation \[ (H,D)\longmapsto(H+AD,D) \quad\text{over }\mathbb Z/q^b\mathbb Z \] can be performed with exactly $a$ interchanges of pairs of $b$-digit fields and $O(V)$ further work. Every interchange is between an $H$ field and a $D$ field. Spectators between any of the formal fields are allowed. \end{lemma}

- "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)

  > \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}


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

Write the body to `exegenius/tasks/0010-write-address-interchange.answer.md` and the JSON to `exegenius/tasks/0010-write-address-interchange.answer.json`, then run `exegenius submit 0010-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0010-write-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
