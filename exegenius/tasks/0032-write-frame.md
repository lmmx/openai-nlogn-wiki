# exegenius task 0032-write-frame

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education at introductory depth: discrete mathematics (integers, divisibility, modular arithmetic, gcd and primes, binomial coefficients, induction, the field of two elements with XOR), algorithms (the big-O family, divide-and-conquer recurrences, the RAM and multitape Turing models), calculus (limits, convergence of sequences and series, geometric series, basic integrals), elementary linear algebra over the reals and F_2 (vector spaces, linear maps, rank, dot products, matrix products), and complex numbers with modulus and polar form. The reader has not reached specialist algebra, tensor products, bilinear forms, eigen-theory beyond the basics, analysis (liminf and limsup), or numerical analysis, so the main theorem's proof and its network and transform machinery must be explained.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Complex numbers
- Polynomials
- Multitape Turing machine (also: Turing machine, tape)
- Linear algebra over a field (also: invertible linear operator, subspace, matrix rank)
- Fixed-tape machine model (also: fixed finite-tape model)
- Linear network that restores auxiliary values (also: exchange network, network, pointwise linear gate)
- Logarithms and exponentials (also: log, logarithm base 2, log_2, lg, binary logarithm, natural logarithm, exp, e^x, change of base)
- Floor and ceiling functions (also: floor, ceiling, integer part, round down, round up, lfloor x rfloor, lceil x rceil)
- Positional (radix) representation (also: binary representation, base-b expansion, radix representation, positional notation, digit string, bit string, padded binary, most significant bit)
- Field of two elements (also: F_2, GF(2), binary field, Z/2Z, field of order 2)
- Bitwise XOR (also: exclusive or, XOR, addition modulo 2 of bits, symmetric difference of bits)
- Modular arithmetic and congruences (also: congruence modulo m, residues modulo m, integers mod m, Z/mZ, mod m arithmetic, residue classes)
- Greatest common divisor and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, coprime, Euclidean algorithm, extended Euclidean algorithm)
- Prime numbers (also: primes, prime factorization, distinct primes, prime modulus, prime power)
- Binomial coefficients and counting subsets (also: n choose k, binom(n,k), choose function, number of k-element subsets, k-subsets)
- Mathematical induction (also: proof by induction, induction on n, strong induction, recursion on the number of ranges)
- Divide-and-conquer recurrence (also: recurrence relation, recursive cost recurrence, recursion tree, master theorem, unrolling a recurrence)
- Random-access machine model (also: RAM model, word RAM, unit-cost RAM, random access machine)
- Limits and convergence of sequences (also: limit of a sequence, convergent sequence, limit as n tends to infinity, tends to zero, epsilon-N definition)
- Convergence of series (also: convergent series, infinite series, sum of a series, absolute convergence, partial sums)
- Geometric series (also: geometric sum, sum of powers of a ratio, geometric progression sum)
- Big-Omega, big-Theta and little-o notation (also: big-Omega, Omega notation, big-Theta, Theta notation, little-o, small-o notation, asymptotically smaller)
- Dot product and orthogonal vectors (also: inner product, scalar product, orthogonality, perpendicular vectors, orthogonal vectors)
- Matrix product, transpose, and special matrices (also: matrix multiplication, transpose, diagonal matrix, upper triangular matrix, lower triangular matrix, permutation matrix, identity matrix)
- Complex modulus, conjugate and polar form (also: absolute value of a complex number, magnitude, complex conjugate, argument of a complex number, unit circle, Euler's formula, e^(i theta))
- Fixed-point arithmetic (also: fixed-point number, fixed-point representation, binary fixed-point, signed fixed-point, guard bits)

## This page

Concept: Frame of a network vertex
Gloss: An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented.
Also called: frame, input role and output role

## This page in the argument

The step: On every route of the network the operator on each role is $D_{\mathrm{sink}}D_{\mathrm{source}}^{-1}$, so only the endpoint frames determine it.
How: pass a common frame through each pointwise linear gate, so the intermediate frames cancel
Why: Once the scalar routing is fixed, the endpoint frames determine the array operator on each route, and the intermediate frames can be chosen to make each edge cheap. (the sources say so: "intermediate frames can then be chosen to make each edge change inexpensive" (paper))

Its sub-steps, in order:

- A common frame commutes with a pointwise linear gate.
- The implemented array operator is $D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}$.

It serves these steps, from the main result down:

- The subset-intersection network has a total number $s$ of smaller calls with $s<Wm$, where $W$ is its wire count and $m$ the dimension of its label space.; how: exchange the two banks with a scalar network whose gates carry subspace labels from triples, then bound the total dimension change of the labels by counting dimension losses (on [Subset-intersection network](subset-network.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $F$ (scalar field), bound on [Linear algebra over a field](linear-algebra.md): The field of scalars over which vector spaces are taken.
- $V$ (vector space), bound on [Linear algebra over a field](linear-algebra.md): The vector space of vectors under consideration, over the field F.
- $u$ (vector), bound on [Linear algebra over a field](linear-algebra.md): An arbitrary vector in V.
- $v$ (vector), bound on [Linear algebra over a field](linear-algebra.md): An arbitrary vector in V.
- $a$ (scalar), bound on [Linear algebra over a field](linear-algebra.md): An arbitrary scalar in F.
- $T$ (linear map), bound on [Linear algebra over a field](linear-algebra.md): A linear map of V into itself, the map whose rank and invertibility are discussed.
- $S$ (inverse map), bound on [Linear algebra over a field](linear-algebra.md): The linear map that inverts T, when T is invertible.
- $h$ (ground set size), bound on [Linear network that restores auxiliary values](linear-network.md): The number of elements of the ground set, from which the three-element subsets are taken.
- $\mathcal T$ (three-element subsets), bound on [Linear network that restores auxiliary values](linear-network.md): The set of all three-element subsets of $[h]$.
- $a$ (bank index), bound on [Linear network that restores auxiliary values](linear-network.md): A triple of subsets $a=(a_1,a_2,a_3)$ that indexes each value of the two banks.
- $X_a$ (data bank X), bound on [Linear network that restores auxiliary values](linear-network.md): The first data bank, holding one value for each index $a$.
- $Y_a$ (data bank Y), bound on [Linear network that restores auxiliary values](linear-network.md): The second data bank, holding one value for each index $a$.
- $T$ (subset T), bound on [Linear network that restores auxiliary values](linear-network.md): A three-element subset of $[h]$ used as a varying coordinate, not the linear map of the earlier page.
- $S$ (subset S), bound on [Linear network that restores auxiliary values](linear-network.md): A three-element subset of $[h]$ used as the varying target coordinate of an invocation.
- $x$ (control value), bound on [Linear network that restores auxiliary values](linear-network.md): The control value on the wires of subset $T$ in a forward invocation.
- $y$ (target value), bound on [Linear network that restores auxiliary values](linear-network.md): The target value on the wires of subset $S$ in a forward invocation.
- $A_{ST}$ (scratch wire), bound on [Linear network that restores auxiliary values](linear-network.md): The scratch wire for the ordered neighbor pair $(S,T)$.
- $C_i$ (central wire), bound on [Linear network that restores auxiliary values](linear-network.md): The central wire for the ground element $i$.
- $p$ (initial scratch values A), bound on [Linear network that restores auxiliary values](linear-network.md): The initial values of the scratch wires $A_{ST}$.
- $q$ (initial scratch values C), bound on [Linear network that restores auxiliary values](linear-network.md): The initial values of the central wires $C_i$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear network that restores auxiliary values](linear-network.md): A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state.
  Shown as: Frame of a network vertex *<predicate>* Linear network that restores auxiliary values

## Pages that build on this one

- Subset-intersection network: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.

## Other pages you may link to

- [Linear algebra over a field](linear-algebra.md)
- [Fixed-tape machine model](fixed-tape-machine.md)
- [Subset-intersection network](subset-network.md)

## Evidence from the sources, with the paragraph around each quote

- "We call $D_v$ its frame" (paper)

  > The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $v$ means vertex here, but vector on [Linear algebra over a field](linear-algebra.md), which this page builds on: Use vertex letters that are not vector letters from linear-algebra (for example p and q, so that the frame is D_p and edges run from p to q), since the frame page's v names a vertex and linear-algebra's v names a vector in V.
- $u$ means edge start vertex here, but vector on [Linear algebra over a field](linear-algebra.md), which this page builds on: Use another vertex letter for the edge start (for example p in place of u), because linear-algebra binds u as an arbitrary vector in V and the frame page's u names a vertex.

## Previous version (revise it)

It has 321 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 401 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A frame of a network vertex is an invertible linear operator attached to a vertex of a network that changes how the array on each wire is represented, without changing the logical array it encodes. Frames make the operator on each route through the network depend only on the route's two endpoints. Each frame acts on the wires of a [Linear network that restores auxiliary values](linear-network.md).

Let $D_v$ denote the frame at a source, gate or sink $v$: an invertible linear operator on the arrays indexed by the common address set, the addresses that every wire's array is indexed by. The stored array is $D_v g$ when the logical array is $g$, the array the computation means. Along an edge from $u$ to $v$, the operator $D_v D_u^{-1}$ turns the stored array $D_u g$ into $D_v g$.

A pointwise linear gate $G$ with $t$ inputs, where $t$ is the number of its input arrays, commutes with a common frame:

$$G(D_v g_1,\ldots,D_v g_t)=D_v\,G(g_1,\ldots,g_t).$$

This holds because $G$ combines its inputs with fixed scalar coefficients, and $D_v$ is linear, so $D_v$ moves across the combination.

The scalar network sends each input role $w$ to $\rho(w)$, the output role assigned to $w$, and multiplies the array by a sign $\varepsilon_w$, which is $+1$ or $-1$ and is fixed by the network. The route runs from the source of $w$ to the sink of $\rho(w)$. Each edge contributes a frame change and each gate passes its frame through, so the intermediate frames cancel and the route applies
$$\varepsilon_w\,D_{\mathrm{sink}(\rho(w))}\,D_{\mathrm{source}(w)}^{-1},$$
where $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ are the vertices where the route starts and ends.

So the intermediate frames do not affect the route operator and may be chosen freely. The paper uses this freedom to make each edge change cheap, which this page does not need to explain. <cite data-source="paper">intermediate frames can then be chosen to make each edge change inexpensive</cite>.

Undoing the role exchange and the signs gives the endpoint operator on every role array. Undoing the exchange reads the output role $\rho(w)$ as the role $w$ again, and since $\varepsilon_w=\pm 1$, undoing the sign multiplies by $\varepsilon_w$ once more. The route identity holds for every input role, <cite data-source="paper">including the roles that carried auxiliary scalar values</cite>.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
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

Write the body to `exegenius/tasks/0032-write-frame.answer.md` and the JSON to `exegenius/tasks/0032-write-frame.answer.json`, then run `exegenius submit 0032-write-frame` in the project directory. If submit rejects the answer, fix the answer and submit again.
