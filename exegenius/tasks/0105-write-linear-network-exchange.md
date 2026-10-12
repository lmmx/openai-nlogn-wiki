# exegenius task 0105-write-linear-network-exchange

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

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Multitape Turing machine (also: fixed-tape model)
- Complex numbers
- Polynomials
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplication (also: Harvey and van der Hoeven multiplier)
- Matrix rank (also: rank)
- Discrete Fourier transform (also: Fourier transform, DFT, transform of length n)
- Primitive roots of unity (also: root of unity)
- Cyclic convolution (also: normalized cyclic convolution)
- Multiplication as convolution of digits (also: radix-digit convolution)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, signed shift)
  - $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
  - $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, synthetic transform)
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Butterfly operation (also: two-point butterfly, H_0)
- Modular arithmetic (also: congruence, congruence modulo c, residue class, mod c arithmetic, integers modulo n)
- Prime numbers and greatest common divisors (also: primes, prime, gcd, greatest common divisor, coprime, relatively prime)
- Arithmetic modulo 2 and XOR (also: F_2, GF(2), Z/2Z, binary field, two-element field, exclusive or, parity, bitwise XOR)
- Dyadic rationals (also: binary fractions, numbers with power-of-two denominators, dyadic numbers, fixed-point binary fractions)
- Vector spaces, subspaces, bases and dimension (also: linear space, subspace, span, linear independence, basis, dimension, ordered basis)
- Linear maps, matrix operations and invertibility (also: linear transformation, linear operator, matrix product, transpose, invertible matrix, nonsingular matrix, inverse matrix, kernel, null space)
- Gaussian elimination (also: row reduction, Gauss-Jordan elimination, elimination, pivot)
- Triangular matrices (also: lower-triangular matrix, upper-triangular matrix, unit triangular matrix)
- Dot product and orthogonality in R^n (also: inner product, scalar product, orthogonal vectors, orthonormal basis, orthogonal complement)
- Permutations of a finite set (also: permutation, rearrangement, bijection of an index set, permutation matrix)
- Finite sets, subsets and intersections (also: set intersection, cardinality, subset, k-subset, binomial coefficient, power set)
- Graphs (also: undirected graph, vertices and edges, adjacency, neighbours, intersection graph, source and sink vertices of the network)
- Mathematical induction (also: induction, inductive proof, strong induction, proof by induction on n)
- Recurrence relations and divide-and-conquer recursion (also: recurrence, recursion equation, divide and conquer, recursive algorithm, cost recurrence, T(n) recurrence)
- Floor and ceiling functions (also: integer part, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Logarithms base 2 (also: lg, log base 2, binary logarithm, log_2)
- Big-Omega and big-Theta notation (also: Omega notation, Theta notation, Ω, Θ, asymptotic lower bound, asymptotic tight bound)
- Limits and convergence of sequences and series (also: limit of a sequence, convergent sequence, convergent series, sum of a series, n tends to infinity)
- Geometric series (also: geometric sum, geometric progression sum, sum of powers of a ratio)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton reduction, Newton's root-finding iteration)
- Worst-case time complexity of a Turing machine (also: running time, worst-case running time, time bound, T_A(n), time on n-bit inputs)

## This page

Concept: Linear network with restored auxiliary values
Gloss: A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
Also called: linear network, frame

## This page in the argument

The step: Each tape procedure is a fixed linear network that exchanges two banks of values and restores every auxiliary value.

It serves these steps, from the main result down:

- Two $n$-bit integers can be multiplied exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time on a deterministic multitape Turing machine, for a fixed $\kappa=2^{-182}$.; how: reduce the product to a digit convolution, compute that convolution through transform layers whose tape cost saves a power, and recover the exact product by rounding (on [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md))
- Both tape procedures cost $O(V)$ times a power of their parameter whose exponent is strictly below one.; how: give each procedure a fixed linear network with fewer smaller calls than roles, and iterate the resulting recursion (on [Recursive power saving](recursive-power-saving.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input bit length), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The number of bits in each input integer.
- $\kappa$ (exponent gap), bound on [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): A fixed positive constant, $2^{-182}$, by which the logarithmic exponent of the target running time falls below 1.
- $\kappa$ (power-saving constant), bound on [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md): The fixed constant $\kappa>0$ in the target's bound $O(n(\lg n)^{1-\kappa})$, with value $2^{-182}$.
- $n$ (root order), bound on [Primitive roots of unity](roots-of-unity.md): The order of the root, a positive integer that counts the positions of the transform it labels.
- $\omega$ (primitive root), bound on [Primitive roots of unity](roots-of-unity.md): A primitive $n$-th root of unity, the complex number that labels the positions of a transform.
- $k$ (power exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, marking which power of $\omega$ is meant.
- $j$ (earlier exponent), bound on [Primitive roots of unity](roots-of-unity.md): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
- $n$ (input length), bound on [Discrete Fourier transform](fourier-transform.md): The length of the input sequence, the number of its entries, so the roots are the $n$-th roots of unity.
- $a$ (input sequence), bound on [Discrete Fourier transform](fourier-transform.md): The input sequence $a=(a_0,\dots,a_{n-1})$, a list of $n$ complex numbers.
- $j$ (input index), bound on [Discrete Fourier transform](fourier-transform.md): An index running from $0$ to $n-1$ over the input entries.
- $k$ (output index), bound on [Discrete Fourier transform](fourier-transform.md): An index running from $0$ to $n-1$ over the output entries.
- $\hat a$ (output sequence), bound on [Discrete Fourier transform](fourier-transform.md): The output sequence of $n$ complex numbers, whose entries are the transform of $a$.
- $x$ (formal variable), bound on [Discrete Fourier transform](fourier-transform.md): A formal variable, a placeholder for a number substituted into the polynomial $p$.
- $p$ (coefficient polynomial), bound on [Discrete Fourier transform](fourier-transform.md): The polynomial whose coefficient list is $a$, so that $a_j$ is the coefficient of $x^j$.
- $u$ (first input value), bound on [Butterfly operation](butterfly-operation.md): One of the two input values that the butterfly operation maps.
- $v$ (second input value), bound on [Butterfly operation](butterfly-operation.md): The other of the two input values that the butterfly operation maps.
- $H_0$ (butterfly operation), bound on [Butterfly operation](butterfly-operation.md): The two-point map sending $(u,v)$ to $\left(\frac{u+v}{2}, \frac{u-v}{2}\right)$.
- $r$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of complex coefficients in each input sequence, which is also the length of their cyclic convolution.
- $b$ (second input sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second input sequence, a list of r complex numbers.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The length-r sequence a convolved with b cyclically, whose k-th entry is the sum over j of a_j b_((k-j) mod r).
- $l$ (second-sequence index), bound on [Cyclic convolution](cyclic-convolution.md): An index of a term of b, running over the residues 0 to r-1 in the reduction argument.
- $x$ (formal variable), bound on [Cyclic convolution](cyclic-convolution.md): An indeterminate used to write sequences as polynomials; it is not evaluated at any number.
- $b$ (digit width), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of bits in one digit, so that digits are taken in radix $2^b$.
- $m$ (digits per input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The number of radix-$2^b$ digits in each input.
- $u$ (first input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The first of the two integers being multiplied.
- $v$ (second input), bound on [Multiplication as convolution of digits](convolution-reduction.md): The second of the two integers being multiplied.
- $y$ (ring variable), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The variable of the polynomial ring modulo $y^r+1$, whose powers serve as roots of unity in the remaining axes.
- $r$ (coefficient count), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): The number of complex coefficients in the coefficient list of one polynomial record, a power of two.
- $\theta$ (twist factor), bound on [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md): A complex $2r$-th root of unity with $\theta^r=-1$, whose powers multiply the entries of a coefficient list in the phase twist.
- $x$ (input sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): The sequence of ring elements $x_0$ through $x_{2r-1}$ to which the transform is applied.
- $t$ (input position), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an input entry, running from 0 to $2r-1$.
- $s$ (frequency index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an output frequency, running from 0 to $2r-1$.
- $i$ (half-transform index), bound on [Synthetic polynomial transform](synthetic-transform.md): The index, running from 0 to $r-1$, that labels the even outputs $\hat x_{2i}$ and the odd outputs $\hat x_{2i+1}$.
- $z$ (second sequence), bound on [Synthetic polynomial transform](synthetic-transform.md): A second sequence of ring elements, transformed by the same rule as $x$.
- $q$ (position in z), bound on [Synthetic polynomial transform](synthetic-transform.md): The index of an entry of $z$, summed over together with $t$.
- $h$ (convolution position), bound on [Synthetic polynomial transform](synthetic-transform.md): The output position of the cyclic convolution $x\ast z$, taken modulo $2r$.
- $j$ (coefficient index), bound on [Signed Kronecker packing](kronecker-packing.md): The index running over the $r$ coefficient positions of a polynomial in the ring, $0 \le j < r$.
- $f$ (packed polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): An element of the ring whose integer coefficients $f_j$ are packed into an integer.
- $g$ (second polynomial), bound on [Signed Kronecker packing](kronecker-packing.md): A second element of the ring with integer coefficients $g_j$, packed in the same way as $f$.
- $M$ (coefficient bound), bound on [Signed Kronecker packing](kronecker-packing.md): A bound on the absolute value of every coefficient of $f$ and $g$.
- $B$ (packing base), bound on [Signed Kronecker packing](kronecker-packing.md): The power of two at which polynomials are evaluated to pack them into integers.
- $F$ (packed integer of f), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $f$ at the packing base $B$.
- $G$ (packed integer of g), bound on [Signed Kronecker packing](kronecker-packing.md): The integer obtained by evaluating $g$ at the packing base $B$.
- $h$ (unreduced product), bound on [Signed Kronecker packing](kronecker-packing.md): The product $fg$ of $f$ and $g$ as polynomials, before reduction modulo $y^r+1$.
- $k$ (product power), bound on [Signed Kronecker packing](kronecker-packing.md): The power of $y$ indexing a coefficient $h_k$ of the unreduced product.
- $M$ (matrix), bound on [Matrix rank](matrix-rank.md): A real matrix, the matrix whose rank is taken.
- $p$ (pivot), bound on [Matrix rank](matrix-rank.md): The nonzero pivot entry, the top-left entry after reordering rows and columns.
- $S$ (smaller matrix), bound on [Matrix rank](matrix-rank.md): The matrix left after the pivot's row and column are deleted, which is smaller than the original.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Matrix rank](matrix-rank.md): The rank of a matrix is the maximum number of linearly independent rows or columns; the number of nonzero pivots in elimination.
  Shown as: Linear network with restored auxiliary values *<predicate>* Matrix rank

## Pages that build on this one

- Address shear: The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A.
- Fast address interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
- Simultaneous butterfly layer: A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
- Recursive power saving: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Evidence from the sources, with the paragraph around each quote

- "Each procedure arises from its own fixed linear network that exchanges two" (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Cite or cut this step: "Each procedure of the paper uses such a network, which exchanges two banks of values and (cited)." (The cited clause is cut off mid-sentence after "and", so the page does not say what the source states about the procedures or how the network is used in them. The reader cannot check this claim from the page.). It is inside reasoning added for an earlier step, so do not explain it further: cite the source for it, or remove the claim.
- Say what $u$ denotes where it is first used (for a size or count, what it counts): "An edge from $u$ to $v$ changes the stored array by $D_vD_u^{-1}$ and leaves the logical array fixed." (The page never says what u denotes; it is used as the tail vertex of an edge, which the reader can only infer to be a vertex.)
- Say what $D_u$ denotes where it is first used (for a size or count, what it counts): "An edge from $u$ to $v$ changes the stored array by $D_vD_u^{-1}$ and leaves the logical array fixed." (The page defines the frame D_v only for a generic vertex v; it never states that D_u is the frame of the vertex u.)

## Previous version (revise it)

It has 377 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 471 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A linear network with restored auxiliary values is a fixed network of linear gates that exchanges two banks of values, with prescribed signs, and returns every auxiliary (scratch) value to its starting content. Each tape procedure of the target is built from one such network.

Each wire has a fixed place in the network, its *role*. The values on a wire form an array indexed by a finite address set $\Omega$. A gate acts pointwise: at each address it takes a linear combination, with scalar coefficients, of the values on the wires it touches. An input role is written $w$, and the network carries it to an output role $\rho(w)$. Its prescribed sign is $\varepsilon_w$.

Each source, gate and sink $v$ carries an invertible linear operator $D_v$ on arrays indexed by $\Omega$, its *frame*. Each frame is invertible, so its matrix has full [matrix rank](matrix-rank.md) on $\Omega$. The stored array at $v$ is $D_v$ applied to the logical array the network computes with. An edge from $u$ to $v$ changes the stored array by $D_vD_u^{-1}$ and leaves the logical array fixed.

Gates commute with a common frame. If every input of a gate is stored in frame $D_v$, the gate's output is a combination of those inputs with scalar coefficients that are the same at every address. By linearity, applying $D_v$ to such a combination gives the same combination of its images, so the output is stored in frame $D_v$ too. The frame acts across addresses and the gate across wires, so the two commute and the frames on intermediate vertices cancel.

Here $\mathrm{source}(w)$ is the source vertex where role $w$ enters, and $\mathrm{sink}(\rho(w))$ is the sink vertex where output role $\rho(w)$ leaves; the wiring fixes both. So a route from input role $w$ to output role $\rho(w)$ with sign $\varepsilon_w$ applies $\varepsilon_w D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to the array.

Example. Let $a$ be one address, and let the two wires carry $x$ and $y$ at $a$; here $a$, $x$ and $y$ change meaning from earlier pages. Three gates act: add the first value to the second, subtract the second from the first, then add the first to the second. They take $(x,y)$ to $(x,\,x+y)$, then $(-y,\,x+y)$, then $(-y,\,x)$. Here $X_a$ and $Y_a$ are the values of the two banks at $a$. The schedule therefore sends $(X_a,Y_a)$ to $(-Y_a,X_a)$. Each procedure of the paper uses such a network, which exchanges two banks of values and <cite data-source="paper">restores every auxiliary value</cite>.

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

Write the body to `exegenius/tasks/0105-write-linear-network-exchange.answer.md` and the JSON to `exegenius/tasks/0105-write-linear-network-exchange.answer.json`, then run `exegenius submit 0105-write-linear-network-exchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
