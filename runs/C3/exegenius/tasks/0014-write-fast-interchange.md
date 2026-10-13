# exegenius task 0014-write-fast-interchange

Project directory: `/home/user/openai-nlogn-wiki/runs/C3` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: algorithm analysis with big-O and recurrences, discrete mathematics (sets, modular arithmetic, primes, induction, permutations), and the linear algebra and complex numbers of the first years (matrices, rank, invertibility, subspaces, norms). They know basic Turing machines with tapes and binary and two's-complement number representation. They have not studied Fourier transforms over rings, FFT-based multiplication, algebraic complexity, or the history of fast multiplication, and have not seen finite-field linear algebra beyond XOR as a bitwise operation.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape machine model and tape streams
- The n log n conjecture and history of multiplication
- Convolution
- Fixed-point complex values and Gaussian dyadics
- Harvey–van der Hoeven O(n log n) multiplier as subroutine
- Array addresses, fields and chunks
- Linear exchange network with roles and frames
- Three-element-subset network with rank saving
- Recursive power saving from s < Wm
- Lower triangular factorization of address shears
- Linear algebra over the reals and complex numbers (also: matrices, matrix product, invertible matrix, linear map, vector space, subspace, rank, linear combination, basis, dimension)
- Linear algebra over GF(2) (also: F_2 vectors, XOR, bitwise exclusive or, binary vector space, mod 2 arithmetic)
- Triangular matrices and Gaussian elimination (also: lower triangular matrix, upper triangular matrix, row reduction, elementary matrices, unit diagonal)
- Modular arithmetic and prime numbers (also: congruence, residues mod m, coprime, gcd, distinct primes, cyclic group Z/m, divisibility)
- Binary and two's-complement representation (also: bit string, binary expansion, two's complement, signed integers, most significant bit, radix-b digits, padding)
- Floor, ceiling, rounding and logarithms (also: lg n, log base 2, floor, ceiling, nearest integer rounding, truncation toward zero)
- Permutations and sorting (also: bijection, reordering, transposition of data, permutation of indices)
- Cartesian products and mixed-radix indexing (also: multi-index, lexicographic order, multidimensional array, row-major order, tuples of indices)
- Vector norms and inequalities (also: sup norm, maximum norm, triangle inequality, modulus bound, contraction)
- Geometric series and recurrences (also: recurrence relation, summing a series, induction, master theorem, telescoping)
- Schoolbook multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication)
- Roots of unity and Euler's formula (also: e^{2 pi i/k}, primitive root of unity, unit circle, cyclic sums of roots of unity)
- Asymptotic conventions (also: Theta, Omega, little-o, for sufficiently large n, fixed constant)
- Finite-state and constant-size alphabets (also: fixed finite alphabet, finite control, encoding symbols as bit blocks)

## This page

Concept: Fast interchange of address chunks
Gloss: Interchanges two equal address chunks of u digits in time O(V u^τ) for a fixed τ < 1 via XOR-like linear combinations, ending in an exact permutation.

## This page in the argument

The step: Two equal address chunks of $u$ digits of an array of volume $V$ can be interchanged in time $O(Vu^\tau)$ for a fixed $\tau<1$.
How: Build a fixed linear exchange network whose endpoint operator is an address shear, show its total edge rank $s$ is below $Wm$, and recurse on smaller interchanges
Why: Plain sorting of address fields costs a pass per level; a recursion whose number of smaller calls is less than the number of roles times the dimension saves a power of the chunk width. (the sources say so: "Because the sum of these ranks is less than the number of wires times" (paper))
Striking feature: The final effect is an exact permutation, although the intermediate steps compute XOR combinations of data; and the saving is a power $u^\tau$ with $\tau<1$ uniformly in the shape. (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed linear exchange network with a common invertible frame at each gate lets arrays flow through pointwise, so only the endpoint frame operators remain on each of the $W$ roles. (on [Linear exchange network with roles and frames](linear-network.md))
- A finite three-subset network with nested subspaces on gates makes the total number $s$ of smaller calls satisfy $s<Wm$. (on [Three-element-subset network with rank saving](subset-network.md))
- A recursive call at parameter $mf$ uses $s$ calls on streams of volume $V/W$, so the cost per volume grows by a factor $s/W<m$ per factor $m$ in the parameter, a power saving. (on [Recursive power saving from s < Wm](recursive-power-saving.md))
- A rational matrix shear $(H,D)\mapsto(H+AD,D)$ of rank $a$ costs exactly $a$ smaller interchanges plus $O(V)$ work, via a lower triangular factorization. (on [Lower triangular factorization of address shears](shear-factorization.md))
- For power widths $e=m^k$ with enough rows, the recursion on the rank-saving network interchanges the two chunks in $O(Ve^\tau)$ time.
- Removing the power-width and row restrictions, two chunks of $u$ bits are interchanged in $O(Vu^\tau)$ steps for any width.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to digit convolution computed by Fourier transforms, and speed up the two bottlenecks, address rearrangement and butterfly layers, by a recursion with a strict rank saving (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.5, S2.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.5**: For power widths $e=m^k$ with enough rows, the recursion on the rank-saving network interchanges the two chunks in $O(Ve^\tau)$ time.
Source: "The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every" (paper)
> \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}

**S2.6**: Removing the power-width and row restrictions, two chunks of $u$ bits are interchanged in $O(Vu^\tau)$ steps for any width.
Source: "in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$." (paper)
> \begin{lemma}[Arbitrary-width interchange] \label{lem:chunk-swap} There exist fixed $0<\tau<1$ and one fixed finite-alphabet multitape procedure with the following property. For positive integers $P,G,B$ and $u\ge1$, it transforms an arbitrary bit array on \[ [P]\times[2^u]\times[G]\times[2^u]\times[B] \] by the address permutation \[ (p,h,g,d,z)\longmapsto(p,d,g,h,z) \] in $O(Vu^\tau)$ steps, where $V=PG B\,2^{2u}$. The integers specifying the shape are part of the input. The time includes their processing, all padding and unpadding, and fixed-tape workspace cleanup. In particular, $B=1$ is allowed. \end{lemma}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Linear exchange network with roles and frames](linear-network.md)): A fixed linear exchange network with a common invertible frame at each gate lets arrays flow through pointwise, so only the endpoint frame operators remain on each of the $W$ roles.
- S2.2 (on [Three-element-subset network with rank saving](subset-network.md)): A finite three-subset network with nested subspaces on gates makes the total number $s$ of smaller calls satisfy $s<Wm$.
- S2.3 (on [Recursive power saving from s < Wm](recursive-power-saving.md)): A recursive call at parameter $mf$ uses $s$ calls on streams of volume $V/W$, so the cost per volume grows by a factor $s/W<m$ per factor $m$ in the parameter, a power saving.
- S2.4 (on [Lower triangular factorization of address shears](shear-factorization.md)): A rational matrix shear $(H,D)\mapsto(H+AD,D)$ of rank $a$ costs exactly $a$ smaller interchanges plus $O(V)$ work, via a lower triangular factorization.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving from s < Wm](recursive-power-saving.md): A recursive call at parameter mf uses s calls on streams of volume V/W, so the cost per volume grows by s/W < m per factor m in the parameter, giving a power saving.
  Shown as: Fast interchange of address chunks *<predicate>* Recursive power saving from s < Wm
- [Lower triangular factorization of address shears](shear-factorization.md): Bruhat-type factorization into lower triangular matrices, letting a rational matrix shear (H,D)→(H+D,D) on address fields be done with linear-time scans and rank-many smaller interchanges.
  Shown as: Fast interchange of address chunks *<predicate>* Lower triangular factorization of address shears

## Pages that build on this one

- Chinese-remainder map to prime cyclic axes: The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution, implemented by controlled shifts and axis moves.
- Fast simultaneous butterfly layers: Applies H₀ on the same bit position in each of d address chunks of arrays of complex polynomial records in time O(V d^λ') with λ' < 1, evaluated exactly with one final truncation.
- Resampling with permutations left in the transform: The source and target coordinate permutations of resampling are kept inside the transform identity and cancel across the two forward transforms, product and inverse, so no separate sorts are run.

## Other pages you may link to

- [Convolution](convolution.md)
- [Fixed-tape machine model and tape streams](tape-streams.md)
- [The n log n conjecture and history of multiplication](nlogn-conjecture.md)
- [Array addresses, fields and chunks](address-fields.md)
- [Fixed-point complex values and Gaussian dyadics](fixed-point-dyadics.md)
- [Linear exchange network with roles and frames](linear-network.md)
- [Three-element-subset network with rank saving](subset-network.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hvdh-multiplier.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Phase twist to the negacyclic last coordinate](phase-twist.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Two-point butterfly H₀](butterfly.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Synthetic transform on a retained-order layout](transform-layout.md)
- [Normalized convolution over the polynomial ring](ring-convolution.md)
- [Resampling with permutations left in the transform](retained-permutations.md)
- [Reduction of integer multiplication to digit convolution](radix-digit-reduction.md)
- [Precision and exact recovery](precision-recovery.md)
- [The multiplication algorithm and its cost](multiplication-algorithm.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "The chunks can be interchanged in $O(Ve^\tau)$ time" (paper)

  > \begin{proposition}[Power-width interchange with rows] \label{prop:power-interchange} Assume the fixed circuit data satisfy \eqref{eq:finite-shear-contract}, and let $q$ be a prime as in Lemma~\ref{lem:matrix-shear} for its edge matrices, also avoiding the denominators of every assigned terminal and gate matrix $M$. Choose a rational number $\tau\in(0,1)$ with $s/W<m^\tau$. For every $e=m^k$, $k\ge0$, consider two disjoint contiguous address chunks of $e$ radix-$q$ digits each. Suppose a row field preceding both chunks has length divisible by $W^k$. There may be additional fields before and after the row field, between the chunks, and after them. The chunks can be interchanged in $O(Ve^\tau)$ time, preserving every other address field, on a fixed number of finite-alphabet tapes. The constant is independent of all field lengths and of the data. \end{proposition}


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

Write the body to `exegenius/tasks/0014-write-fast-interchange.answer.md` and the JSON to `exegenius/tasks/0014-write-fast-interchange.answer.json`, then run `exegenius submit 0014-write-fast-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0014-write-fast-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
