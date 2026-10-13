# exegenius task 0130-write-subspace-labels

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

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

The reader already understands these concepts:

- Big-O notation (also: O(n))
- Polynomials
- Complex numbers (also: Gaussian integers)
- Multitape Turing machine
- Fixed-tape machine model (also: fixed finite-tape model)
- Schonhage-Strassen optimality conjecture (also: n log n optimality conjecture)
- Power saving in the logarithmic factor (also: (lg n)^(1-kappa) saving)
- Linear network (also: fixed linear network, network, pointwise linear gate, wires, bank and forward invocation)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles, wire streams)
- Subset-intersection finite network (also: three-element subset network, gather and scatter wires)
- Address shear (also: H + D shear, endpoint operator)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
- Established fast multiplier (also: Harvey-van der Hoeven multiplier)
- Modular arithmetic (also: congruence, residue classes, integers modulo m, Z/mZ, modular inverse, division with remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, Euclidean algorithm)
- Prime number (also: prime, primality, prime factorization)
- Binary field and exclusive or (also: F_2, GF(2), Z/2Z, XOR, exclusive or, bitwise XOR)
- Hamming weight (also: weight, popcount, number of ones)
- Two's-complement representation (also: two's complement, signed binary integer, signed fixed-width integer)
- Positional notation and binary representation (also: radix representation, base-b digits, binary representation, binary expansion, carries)
- Dyadic rational (also: dyadic fraction, binary fraction, finite binary expansion, power-of-two denominator)
- Floor and ceiling functions (also: integer part, round down, round up, floor, ceiling)
- Binomial coefficient (also: n choose k, binomial, binom(n,k))
- Finite sets, subsets and intersections (also: subset, intersection, intersection size, indicator vector, characteristic vector, k-element subset)
- Bijection and permutation (also: one-to-one correspondence, bijective function, permutation map, permutation of a set)
- Cartesian product (also: product set, direct product, product of index sets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Logarithm and exponential function (also: lg, log base 2, natural logarithm, ln, exp, e^x)
- Limits (also: limit of a sequence, limit of a function, lim, tends to, approaches)
- Convergence of sequences and series (also: convergent sequence, convergent series, divergence, partial sums, sum of an infinite series, convergence)
- Basic integrals (also: definite integral, indefinite integral, antiderivative, Riemann integral, fundamental theorem of calculus, integration by substitution)
- Geometric series (also: geometric sum, sum of powers)
- Big-Omega, big-Theta and little-o notation (also: Omega notation, Theta notation, o-notation, asymptotic lower bound, tight bound, asymptotic equivalence)
- Worst-case running time of a Turing machine (also: time complexity, step count, worst-case time, running time)
- Recurrence relation (also: recurrence, divide-and-conquer recurrence, unrolling, T(n) recurrence)
- Schoolbook multiplication (also: grade-school multiplication, long multiplication, naive multiplication)
- Directed graph (also: digraph, vertex, edge, head and tail, directed acyclic graph, DAG, node)
- Vector space, subspace, basis and dimension (also: linear space, subspace, span, linearly independent, basis, direct sum, dimension)
- Linear map and matrix (also: linear transformation, matrix, invertible matrix, nonsingular matrix, transpose, identity matrix, diagonal matrix)
- Matrix rank (also: column rank, row rank, rational rank, rank over a field)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, echelon form, lower triangular matrix, upper triangular matrix)
- Dot product and orthogonal complement (also: standard inner product, scalar product, orthogonal complement, perpendicular space, U perp)
- Vector norm and maximum norm (also: norm, maximum norm, sup norm, infinity norm, max norm, triangle inequality)
- Complex conjugate, modulus and polar form (also: conjugate, modulus, absolute value of a complex number, argument, unit circle, Euler's formula, polar form)
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## This page

Concept: Nested subspace labels
Gloss: Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.

## Where the argument relies on this page

- Interchanging two equal address fields of width $u$ costs less than linear in $u$ per unit volume. (on [Fast interchange of address chunks](tape-interchange.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of bits in each input; the worst-case time is measured as a function of it.
- $\kappa$ (power-saving constant), bound on [Fixed-tape machine model](fixed-tape-model.md): A fixed constant equal to $2^{-182}$ that does not depend on $n$.
- $n$ (integer length), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (power-saving exponent gap), bound on [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md): A fixed constant with κ > 0, so that the target's time bound has exponent 1 − κ on lg n.
- $\kappa$ (saving parameter), bound on [Power saving in the logarithmic factor](power-saving.md): A fixed number greater than 0 that sets the size of the saving in the bound.
- $z$ (Gaussian dyadic number), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A complex number whose real and imaginary parts are both dyadic rationals.
- $a$ (real part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The real part of the Gaussian dyadic number $z$, a dyadic rational.
- $b$ (imaginary part), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The imaginary part of the Gaussian dyadic number $z$, a dyadic rational.
- $m$ (numerator), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The integer numerator of a dyadic rational $m/2^k$.
- $k$ (denominator exponent), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The non-negative integer exponent such that $2^k$ is the denominator of a dyadic rational $m/2^k$.
- $\mathcal{G}$ (Gaussian dyadic set), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The set of all Gaussian dyadic numbers.
- $u$ (first input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number used as the first input of the butterfly $H_0$.
- $v$ (second input), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): A Gaussian dyadic number used as the second input of the butterfly $H_0$.
- $p$ (fractional bit count), bound on [Gaussian dyadic numbers](gaussian-dyadic.md): The number of fractional bits in the fixed-point grid, counting the binary digits after the binary point of each stored part.
- $x$ (first bank value), bound on [Linear network](linear-network.md): The value of the first bank, held on one wire in the example.
- $y$ (second bank value), bound on [Linear network](linear-network.md): The value of the second bank, held on one wire in the example.
- $i$ (row index), bound on [Role streams from a cyclic row split](role-streams.md): The position of a row among the rows that share its prefix, counted from 0.
- $W$ (number of roles), bound on [Role streams from a cyclic row split](role-streams.md): The number of roles, which is the number of fixed wire places in the network.
- $V$ (padded node volume), bound on [Role streams from a cyclic row split](role-streams.md): The number of bits the node holds once its rows are padded.
- $R$ (padded row count), bound on [Role streams from a cyclic row split](role-streams.md): The number of rows of one prefix after padding, a multiple of W.
- $h$ (ground-set size), bound on [Subset-intersection finite network](subset-network.md): The number of elements of the ground set $[h]$, which counts the elements the triples are drawn from.
- $\mathcal{T}$ (triple family), bound on [Subset-intersection finite network](subset-network.md): The set of all three-element subsets of $[h]$.
- $T$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$ in the family $\mathcal T$, used as an index of scalars.
- $S$ (triple), bound on [Subset-intersection finite network](subset-network.md): A three-element subset of $[h]$ in $\mathcal T$, which indexes one bank-X scalar and one bank-Y scalar.
- $X$ (bank X), bound on [Subset-intersection finite network](subset-network.md): The bank holding the bank-X scalars $x_S$, one for each triple $S$.
- $Y$ (bank Y), bound on [Subset-intersection finite network](subset-network.md): The bank holding the bank-Y scalars $y_S$, one for each triple $S$.
- $x_S$ (bank-X scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-X scalar held at triple $S$, on one wire.
- $y_S$ (bank-Y scalar), bound on [Subset-intersection finite network](subset-network.md): The bank-Y scalar held at triple $S$, on one wire.
- $A_{ST}$ (side wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire for an ordered neighbouring pair $(S,T)$, which receives a copy of $x_T$.
- $C_i$ (central wire), bound on [Subset-intersection finite network](subset-network.md): The scratch wire for element $i$ of $[h]$, which gathers the $x_T$ over triples $T$ containing $i$.
- $C_\ast$ (total central wire), bound on [Subset-intersection finite network](subset-network.md): The extra scratch wire of the complex version, which gathers the sum of all $x_T$.
- $D_v$ (vertex frame), bound on [Frame of a vertex](frame.md): The frame of a vertex v, an invertible linear operator on arrays indexed by the common address set; D_u is the frame of u.
- $u$ (edge tail vertex), bound on [Frame of a vertex](frame.md): A vertex at the tail of an edge, where the edge goes from u to v.
- $v$ (edge head vertex), bound on [Frame of a vertex](frame.md): A vertex at the head of an edge, where the edge goes from u to v.
- $g$ (logical array), bound on [Frame of a vertex](frame.md): The array a wire carries in its logical interpretation, before the frame is applied.
- $t$ (gate input count), bound on [Frame of a vertex](frame.md): The number of input arrays of a pointwise linear gate.
- $c_i$ (gate coefficient), bound on [Frame of a vertex](frame.md): The fixed scalar by which a pointwise linear gate multiplies its i-th input array.
- $i$ (input index), bound on [Frame of a vertex](frame.md): The index of an input array of a pointwise linear gate, running from 1 to t.
- $H$ (first address field), bound on [Address shear](address-shear.md): The first of the two address fields, a vector of residues, which the shear replaces by H + D.
- $D$ (second address field), bound on [Address shear](address-shear.md): The second of the two address fields, a vector of residues, which the shear adds to H and leaves fixed.
- $q$ (modulus), bound on [Address shear](address-shear.md): The fixed modulus q of the residue ring Z/qZ in which the entries of H and D lie.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Frame of a vertex](frame.md): An invertible linear operator attached to a gate or terminal that sets how the array on each wire there is stored; changing frames along an edge cancels between the two ends of a route.
  Shown as: Nested subspace labels *<predicate>* Frame of a vertex
- [Subset-intersection finite network](subset-network.md): A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].
  Shown as: Nested subspace labels *<predicate>* Subset-intersection finite network
- [Source, sink and terminal of a network](network-terminal.md): A source or sink of a linear network is an end vertex of a wire, where data enter the network or leave it, and the terminals are the sources and sinks at which the network meets its banks of values.
  Shown as: Nested subspace labels *<predicate>* Source, sink and terminal of a network

## Pages that build on this one

- Rank-saving recursion: A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.

## Other pages you may link to

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Address shear](address-shear.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Tensor product](tensor-product.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Order of an element](order-of-element.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed coefficient packing](signed-packing.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Operator norm of a linear map](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The subspaces at adjacent vertices are nested." (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Cite or cut this step: "The labels are chosen to make changes of" (The page says the labels are chosen to make frame changes inexpensive, but never states how they are chosen or why the chosen nested subspaces have that effect.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Cite or cut this step: "The drop counts the operations an edge needs because the edge's change is the difference of two projections." (No cost model is given, so the reader cannot check why the number of operations an edge needs equals the rank, and hence the dimension drop.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- The reader cannot follow this step: "A smaller operation is the same interchange on a narrower address field, a recursive call. (cited)" (The cited result is not stated: the page does not say what the source proves about the recursive call or why it applies to this network.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Cite or cut this step: "This gives the claim." (The page does not state the claim here, and does not show how the telescoping of frames and the drop count combine into the cost bound.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- The reader cannot follow this step: "Let $s$ be the total number of smaller calls, the sum of the drops over all edges. (cited)" (The cited statement that the number of smaller calls equals the sum of drops, and what it contributes to the bound, is not stated by the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Cite or cut this step: "turns this bound into a cost below linear in $q$ per unit volume" (The page claims the linked recursion yields a cost below linear in q, but does not show how the sum s feeds into that cost; the reader cannot check the conclusion from what the page gives.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Say what $y$ denotes where it is first used (for a size or count, what it counts): "Along an edge from $x$ to $y$ the labels are nested" (The page never says what y denotes; it is presumably a vertex at the other end of an edge, but this is only implied. The earlier page linear-network binds y as a bank value, which is a different sense and does not fit here.)
- Say what $D_x$ denotes where it is first used (for a size or count, what it counts): "the change along an edge from $x$ to $y$ is $D_y D_x^{-1}$" (The page defines D_v only for a generic vertex v; it never says D_x or D_y is the frame of x or y, though the reader may infer it from that definition.)
- Say what $D_y$ denotes where it is first used (for a size or count, what it counts): "the change along an edge from $x$ to $y$ is $D_y D_x^{-1}$" (The page defines D_v only for a generic vertex v; it never says D_x or D_y is the frame of x or y, though the reader may infer it from that definition.)
- Say what $D$ denotes where it is first used: the page uses it before saying so in "each intermediate frame appears once as $D$ and once as $D^{-1}$"
- "terminal" is the concept [Source, sink and terminal of a network](network-terminal.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 319 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 398 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Nested subspace labels are subspaces of one fixed space, attached to the gates and terminals of a network, whose dimension drops measure what each edge costs. They give the cost bound for interchanging two equal address fields, blocks of bits in an address, below linear in the field width.

Fix a space $E$ of dimension $m$; here $m$ is that dimension, not the numerator of a dyadic rational. The labels are attached to the gates and terminals of a [Subset-intersection finite network](subset-network.md) on three-element subsets. A vertex $x$ is one such gate or terminal, and its label $L(x)$ is a subspace of $E$. Along an edge from $x$ to $y$ the labels are nested, say $L(y) \subseteq L(x)$, and the dimension drop across the edge is $\dim L(x) - \dim L(y)$. For example, a plane $L(x)$ of dimension 2 containing a line $L(y)$ has drop $2-1=1$.

The drop counts the operations an edge needs because the edge's change is the difference of two projections. Let $P_U$ be the orthogonal projection onto a subspace $U$. For nested labels, $P_{L(x)} - P_{L(y)}$ projects onto the orthogonal residual, the part of $L(x)$ orthogonal to $L(y)$, so its rank is the drop. A smaller operation is the same interchange on a narrower address field, a recursive call. <cite data-source="paper">Their dimension changes count the smaller operations needed on an edge</cite>.

The labels are chosen to make changes of [Frame of a vertex](frame.md) inexpensive along each edge. A frame $D_v$ is an invertible operator at a vertex, and the change along an edge from $x$ to $y$ is $D_y D_x^{-1}$. Along a route, a chain of edges, each intermediate frame appears once as $D$ and once as $D^{-1}$. These cancel, so the two end frames alone fix the operator on the route.

This gives the claim. Let $q$ be the width in bits of each address field, and let the volume be the number of bits the network holds. Let $s$ be the total number of smaller calls, the sum of the drops over all edges. <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite> The recursion in [Rank-saving recursion](recursive-saving.md) turns this bound into a cost below linear in $q$ per unit volume.

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

Write the body to `exegenius/tasks/0130-write-subspace-labels.answer.md` and the JSON to `exegenius/tasks/0130-write-subspace-labels.answer.json`, then run `exegenius submit 0130-write-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.
