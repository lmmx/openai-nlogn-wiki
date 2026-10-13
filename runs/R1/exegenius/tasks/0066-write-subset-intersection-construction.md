# exegenius task 0066-write-subset-intersection-construction

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers (also: Gaussian integer)
- Multitape Turing machine
- Fixed-tape machine model and stream operations (also: fixed-tape machine)
- Convolution
- Discrete Fourier transform and butterflies
- The n log n optimality conjecture
- Schönhage–Strassen to Harvey–van der Hoeven multiplication
- Reduction of integer product to digit convolution
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Synthetic polynomial transforms
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Finite linear network with roles and frames (also: scalar network)
- Address shear and lower-triangular factorization
- Restoring auxiliary scratch values
- Fixed-point precision and exact recovery
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Three-element subset intersection construction
Gloss: Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls.

## This page in the argument

The step: The network is built from three-element subsets with gather, scatter and cancelling auxiliary wires, so that the total number $s$ of smaller calls satisfies $s<Wm$.

It serves these steps, from the main result down:

- An $n$-bit integer product is computed by a fixed-tape machine in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication to ring convolution and speed up its address moves and butterfly layers (on [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md))
- Two fixed-tape procedures, an address interchange and a simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed exponents below 1, where $V$ is the stored bit volume.; how: build both procedures from one finite linear network and a recursion that saves a power

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $n$ (input bit length), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The bit length of each input, the number of bits in each of the two integers.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input.
- $x$ (first input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first $n$-bit input integer.
- $y$ (second input), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second $n$-bit input integer.
- $x_j$ (digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $x$.
- $y_j$ (digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix-$2^b$ digit of $y$.
- $c_k$ (product coefficient), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $k$th coefficient of the digit convolution of $x$ and $y$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ during carry propagation.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit of the product at position $k$.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $p$ (working precision), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of fractional bits in each fixed-point numerator, so values are stored over the denominator $2^p$.
- $S$ (cyclic convolution length), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of coefficients in the cyclic convolution whose transforms are computed.
- $c_j$ (product coefficient), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The exact integer coefficient of the product at index $j$.
- $b$ (digit width), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The number of bits in each radix digit, equal to the ceiling of the base-2 logarithm of the input length $n$.
- $d_j$ (output digit), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The radix-$2^b$ digit of the product at position $j$.
- $k_j$ (carry), bound on [Fixed-point precision and exact recovery](fixed-point-precision.md): The carry from the processed coefficients into position $j$.
- $u$ (address field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field, a count of bits.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds, a count of stored bits.
- $n$ (input size), bound on [Address fields and array layout on tapes](address-fields.md): The size of the input, so that the array holds $\Theta(n)$ bits.
- $n$ (list length), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The number of coefficients in the list $a$, a power of two.
- $a$ (coefficient list), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ complex coefficients $a_0,\dots,a_{n-1}$ being transformed.
- $\omega$ (root of unity), bound on [Discrete Fourier transform and butterflies](dft-fft.md): A primitive $n$-th root of unity, with $\omega^n=1$ and $\omega^m\neq 1$ for $0<m<n$.
- $A$ (transform of a), bound on [Discrete Fourier transform and butterflies](dft-fft.md): The list of $n$ values $A_0,\dots,A_{n-1}$ obtained by evaluating $a$ at the powers of $\omega$.
- $n$ (integer length), bound on [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md): The number of bits in each integer being multiplied.
- $W$ (role count), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of roles of the network, which counts the fixed places its wires occupy.
- $V$ (padded bit volume), bound on [Finite linear network with roles and frames](linear-network-roles.md): The number of bits stored in the array after padding, which counts the node volume the network handles.
- $D_v$ (frame), bound on [Finite linear network with roles and frames](linear-network-roles.md): The invertible linear operator assigned to a source, gate or sink $v$, acting on arrays indexed by the common address set.
- $\varepsilon_w$ (route sign), bound on [Finite linear network with roles and frames](linear-network-roles.md): The prescribed scalar sign carried by the route from input role $w$ through the network.
- $\rho$ (role permutation), bound on [Finite linear network with roles and frames](linear-network-roles.md): The permutation of roles that the scalar network applies, sending input role $w$ to output role $\rho(w)$.
- $a$ (initial auxiliary value), bound on [Restoring auxiliary scratch values](scratch-restoration.md): The initial content of an auxiliary register, which may be any value.
- $m$ (fields per vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of address fields in each of the vectors $H$ and $D$.
- $H$ (first address vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(H_1,\ldots,H_m)$ of $m$ address fields.
- $D$ (second address vector), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The vector $(D_1,\ldots,D_m)$ of $m$ address fields.
- $b$ (digits per field), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The number of radix-$q$ digits in one address field.
- $q$ (radix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A fixed odd prime, the radix of each digit.
- $A$ (shear matrix), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A rational $m\times m$ matrix defining the shear $(H,D)\mapsto(H+AD,D)$.
- $a$ (rank), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The rank of $A$ over $\mathbb Q$, the number of linearly independent rows of $A$.
- $E_1$ (left triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization of $A$.
- $E_2$ (right triangular factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): An invertible lower-triangular rational matrix in the factorization of $A$.
- $\Pi$ (partial permutation factor), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): A partial permutation matrix with $a$ ones, at most one in each row and column, in the factorization of $A$.
- $V$ (stored volume), bound on [Address shear and lower-triangular factorization](address-shear-factorization.md): The stored bit volume, the number of bits held in the array.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Finite linear network with roles and frames](linear-network-roles.md): Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator.
  Shown as: Three-element subset intersection construction *<predicate>* Finite linear network with roles and frames

## Pages that build on this one

- Recursive power saving from s<Wm: Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Address fields and array layout on tapes](address-fields.md)
- [Discrete Fourier transform and butterflies](dft-fft.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The construction uses" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "three-element subsets" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "create coefficients that depend on the size of the intersection of two such subsets" (The page asserts that gather and scatter operations produce coefficients depending on intersection size but never shows how the wiring does this, so the reader cannot check it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "cancel the coefficients that are not wanted" (The page does not say which coefficients are unwanted or how the auxiliary wires cancel them.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Orthogonality of these vectors permits the assignment of subspaces to the gates and terminals." (The page does not say which subspace goes to which gate or terminal, or why orthogonal indicator vectors make such an assignment possible.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "the rank of the difference between the matrices assigned to the two ends of each edge" (The page never says which matrix is assigned to each gate or terminal, so s cannot be computed from the page.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The network meets the count needed for the recursion." (The inequality the count must satisfy is never stated on this page, so the reader cannot check that s is small enough. The citation does not supply the content of the inequality as used here.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $A$ denotes where it is first used (for a size or count, what it counts): "The indicator vector of a subset $A$" (The page introduces A only as 'a subset' and never says which subset it denotes. The earlier bindings (transform of a on dft-fft, shear matrix on address-shear-factorization) do not match this use.)

## Previous version (revise it)

It has 265 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 331 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The three-element subset intersection construction is a fixed finite network, built from gather, scatter and auxiliary wires, whose number of smaller calls is small enough for the recursion to save a power.

The construction is built inside a [Finite linear network with roles and frames](linear-network-roles.md). It uses three-element subsets of a fixed finite set. Gather and scatter operations, which combine several wires into one or spread one wire over several, create coefficients that depend on the size of the intersection of two such subsets. Auxiliary wires, which hold temporary values, cancel the coefficients that are not wanted.

The subsets also determine where subspaces go. Index the positions by the elements of the set. The indicator vector of a subset $A$ has entry $1$ at each element of $A$ and entry $0$ elsewhere. The dot product of two indicator vectors is the size of the intersection of their subsets, so the vectors for disjoint subsets are orthogonal. For example, $\{1,2,3\}$ and $\{4,5,6\}$ give orthogonal vectors, while $\{1,2,3\}$ and $\{3,4,5\}$ do not, since they share one element. Orthogonality of these vectors permits the assignment of subspaces to the gates and terminals.

Let $s$ be the total number of smaller calls, found by adding, over the edges of the network, the rank of the difference between the matrices assigned to the two ends of each edge. Let $W$ be the number of wires of the network, and let $m$ be the dimension of the fixed space that the subspaces lie in.

The network meets the count needed for the recursion. <cite data-source="paper">The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.</cite> The recursion in [Recursive power saving from s<Wm](recursive-power-saving.md) uses this inequality to save a fixed power.

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

Write the body to `exegenius/tasks/0066-write-subset-intersection-construction.answer.md` and the JSON to `exegenius/tasks/0066-write-subset-intersection-construction.answer.json`, then run `exegenius submit 0066-write-subset-intersection-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
