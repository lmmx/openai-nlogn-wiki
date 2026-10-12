# exegenius task 0036-write-subset-network

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
- Frame of a network vertex (also: frame, input role and output role)
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

Concept: Subset-intersection network
Gloss: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.
Also called: three-element subset construction, bit construction

## This page in the argument

The step: The subset-intersection network has a total number $s$ of smaller calls with $s<Wm$, where $W$ is its wire count and $m$ the dimension of its label space.
How: exchange the two banks with a scalar network whose gates carry subspace labels from triples, then bound the total dimension change of the labels by counting dimension losses
Why: Each edge's dimension change counts the smaller operations on that edge, so the total number of smaller calls is the sum of absolute label changes; a bound of that sum below $Wm$ gives the saving. (the sources leave this for the reader to work out: spell it out)
Striking feature: the strict inequality $s<Wm$ holds with a fixed rational deficit that does not depend on the input length (explain why it holds, from the method)

Its sub-steps, in order:

- A fixed linear network of three-element-subset gates exchanges the banks $X_a$ and $Y_a$ with signs and restores every scratch wire. (on [Linear network that restores auxiliary values](linear-network.md))
- On every route of the network the operator on each role is $D_{\mathrm{sink}}D_{\mathrm{source}}^{-1}$, so only the endpoint frames determine it. (on [Frame of a network vertex](frame.md))
- The subspace labels satisfy $L=Ich$ and the sum of absolute label changes equals $Wm-2N+2L$, with loss $L<N/2$.
- For the bit network the total rational rank $s$ of the edge differences satisfies $s<Wm$.
- For the complex network the total rank of the phase translation factors, $s_{\rm c}$, is strictly below $W_{\rm c}m$.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $F$ (scalar field), bound on [Linear algebra over a field](linear-algebra.md): The field of scalars, the set of numbers that vectors are multiplied by.
- $V$ (vector space), bound on [Linear algebra over a field](linear-algebra.md): A vector space over $F$: a set of vectors with addition and multiplication by scalars from $F$.
- $c$ (scalar), bound on [Linear algebra over a field](linear-algebra.md): An element of the scalar field $F$.
- $L$ (linear map), bound on [Linear algebra over a field](linear-algebra.md): A linear map from $V$ into itself, that is, a map with $L(u+v)=L(u)+L(v)$ and $L(cu)=cL(u)$.
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
- $D_r$ (frame at vertex r), bound on [Frame of a network vertex](frame.md): The invertible linear operator attached to the source, gate or sink b, which turns the logical array into the stored array.
- $g$ (logical array), bound on [Frame of a network vertex](frame.md): The array that the computation means at a vertex, before its frame is applied.
- $G$ (pointwise linear gate), bound on [Frame of a network vertex](frame.md): A gate that combines its input arrays with fixed scalar coefficients.
- $t$ (number of gate inputs), bound on [Frame of a network vertex](frame.md): The count of input arrays of a pointwise linear gate.
- $w$ (input role), bound on [Frame of a network vertex](frame.md): An input role of the network, whose array the scalar routing sends to an output role.
- $\rho$ (role map), bound on [Frame of a network vertex](frame.md): The map sending each input role to the output role assigned to it by the scalar routing.
- $\varepsilon_w$ (role sign), bound on [Frame of a network vertex](frame.md): The sign, plus or minus one, that the network multiplies onto the array of input role w.
- $s$ (edge end vertex), bound on [Frame of a network vertex](frame.md): The vertex at the end of an edge that starts at r.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear network that restores auxiliary values](linear-network.md): A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state.
  Shown as: Subset-intersection network *<predicate>* Linear network that restores auxiliary values
- [Linear algebra over a field](linear-algebra.md): The theory of vector spaces, linear maps, invertible operators, subspaces, and the rank of a linear map.
  Shown as: Subset-intersection network *<predicate>* Linear algebra over a field
- [Frame of a network vertex](frame.md): An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented.
  Shown as: Subset-intersection network *<predicate>* Frame of a network vertex

## Other pages you may link to

- [Fixed-tape machine model](fixed-tape-machine.md)

## Evidence from the sources, with the paragraph around each quote

- "The construction uses three-element subsets" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $s$ means smaller call total here, but edge end vertex on [Frame of a network vertex](frame.md), which this page builds on: On subset-network, rename the smaller-call total (for example to $c$ or $\sigma$) so it does not reuse $s$ for the edge end vertex of the Frame page, which subset-network builds on. The frame page's $s$ is a vertex, not a count.
- $L$ means dimension loss here, but linear map on [Linear algebra over a field](linear-algebra.md), which this page builds on: On subset-network, rename the dimension loss (for example to $\lambda$ or $D$) so it does not reuse $L$ for the linear map of Linear algebra over a field, which subset-network builds on and which binds $L$ on the page as a linear map. The linear map is the standard use, so the later page changes.

## Previous version (revise it)

It has 403 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 503 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The subset-intersection network is a linear network whose labels are subspaces chosen from intersection sizes of three-element subsets. It shows that its number of smaller calls is less than its number of wires times the label dimension, the saving the main theorem uses.

It is based on a [Linear network that restores auxiliary values](linear-network.md) of gates that exchange the banks $X_a$ and $Y_a$ with signs. Each gate and terminal carries a subspace label of one fixed space, so the network is built on [Linear algebra over a field](linear-algebra.md). Here $W$ is the number of wires, $m=h^3$ is the dimension of the label space, and $s$ is the total number of smaller calls.

For a three-element subset $T$, let $t_T\in\mathbb Q^h$ be its indicator vector, with entry 1 at each element of $T$ and 0 elsewhere. Take the form
$$\langle x,y\rangle=\sum_i x_iy_i-\tfrac19\Bigl(\sum_i x_i\Bigr)\Bigl(\sum_i y_i\Bigr)$$
on $\mathbb Q^h$. The first sum counts common elements, and each indicator sums to 3, so $\langle t_S,t_T\rangle=|S\cap T|-\tfrac19\cdot3\cdot3=|S\cap T|-1$ and $\langle t_T,t_T\rangle=2$. The bank label $U_a$ is the span of $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, a line.

Labels at the two ends of an edge are nested, so one contains the other. <cite data-source="paper">Every edge joins comparable nondegenerate labels</cite>. Changing a label's dimension by some amount costs that many smaller calls, since the projections onto the two labels differ by a matrix of that rank, and each unit of rational rank is one smaller interchange. So $s$ is the sum of the ranks of all edge differences.

Each gate's label enters and leaves it, so gate contributions cancel in the signed sum of changes, leaving sinks minus sources. The sources total $N$, the number of banks $X_a$, since each $U_a$ is a line. Every sink label is the whole space, except the $N$ sinks $U_a^\perp$ of the $Y_a$, which have one dimension less, so the sinks total $Wm-N$. The signed sum is $Wm-2N$. Let $L$ be the total dimension lost on decreasing edges. The sum of absolute changes is the signed sum plus $2L$, namely $Wm-2N+2L$.

The rational interface adds one rank per bank: the source matrix of $X_a$ is minus the projection onto $U_a$, of rank one, on an edge with no label change. The operator on each role is computed from the endpoint frames of the [Frame of a network vertex](frame.md), so only the two ends of a route matter. Hence $s=Wm-N+2L$, and $s<Wm$ exactly when $L<N/2$.

The only decreasing edges are central-wire returns, each losing $h$ dimensions. For the two constructions the paper gives $L/N=100/539$ and $101/539$; <cite data-source="paper">both are smaller than $1/2$</cite>. So the deficit is $Wm-s=N-2L=\tfrac{339}{539}N$ for the bit network, a fixed fraction of $N$ independent of the input length.

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

Write the body to `exegenius/tasks/0036-write-subset-network.answer.md` and the JSON to `exegenius/tasks/0036-write-subset-network.answer.json`, then run `exegenius submit 0036-write-subset-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
