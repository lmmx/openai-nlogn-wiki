# exegenius task 0013-write-address-shear

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/W2WHP14` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Address shear and lower-triangular factorization
Gloss: The address permutation (H,D) ↦ (H+AD, D) on two vectors of fields; a rank-a matrix factors as E₁ΠE₂ with lower-triangular E₁,E₂ so that it costs a single-pair swaps plus linear-time updates, and three shears D←D−H, H←H+D, D←H−D interchange H and D.
Also called: Bruhat factorization, matrix shear

## This page in the argument

The step: A rational shear $(H,D)\mapsto(H+AD,D)$ over $\mathbb Z/q^b\mathbb Z$ by a rank-$a$ matrix $A$ costs exactly $a$ interchanges of $b$-digit fields plus $O(V)$ further work.
How: Factor $A=E_1\Pi E_2$ with lower-triangular invertible $E_1,E_2$ and a partial permutation $\Pi$ with $a$ ones; the triangular parts are controlled shifts in tape order, and each one in $\Pi$ is one field interchange.
Why: Lower triangular changes of coordinates update a later field from earlier ones, which is the direction in which a tape can do it in linear time. (the sources say so: "can be performed entirely in this direction." (paper))
Striking feature: The number of expensive operations is the rank $a$ of the matrix, not its size $m$: a rank-$a$ shear needs only $a$ field swaps. (explain why it holds, from the method)

Its sub-steps, in order:

- Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one per row and column (Bruhat factorization with reversed coordinate order).
- Elimination picks the topmost nonzero row and its rightmost nonzero entry, clears its column to the left by right multiplication and below by left multiplication with lower triangular elementary matrices, scales the pivot to one, deletes that row and column, and repeats; the number of pivots is the rank.
- A fixed odd prime $q$ avoiding all denominators and diagonal numerators in a finite table of factors lets all rational identities specialize to $\mathbb Z/q^b\mathbb Z$ with the triangular factors invertible.
- A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a diagonal unit and a fixed combination of earlier coordinates (controlled shifts).
- Each one at position $(i,j)$ of $\Pi$ calls for $H_i\gets H_i+D_j$, done by $D_j\gets D_j+H_i$, then interchanging $(H_i,D_j)$, then $D_j\gets H_i-D_j$; from $(h,d)$ this gives $(h+d,d)$ using just one interchange, so $a$ ones cost $a$ interchanges.
- Three shears $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ interchange $H$ and $D$; only the middle shear needs the network, the other two target the later group and have linear cost.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of short integer coefficients, evaluate the convolution through power-of-two transforms over $\mathbb C[y]/(y^r+1)$, and replace the two tape operations that each cost a factor $\log n$ (address rearrangement and butterfly layers) by procedures whose cost per bit is a power of their parameter below one; then total the costs. (on [Integer multiplication below n log n](main-theorem.md))
- Both tape procedures cost a power of their parameter below one, because each runs a fixed linear exchange network on $W$ wires whose edge changes are smaller calls on role streams of volume $V/W$, with total number of calls $s<Wm$, so that each level of recursion multiplies the cost per volume by $s/W<m^\tau$ while the parameter shrinks by $m$.; how: Build a finite linear exchange network that restores its scratch wires, give its vertices frames so that only endpoint operators matter, attach nested subspace labels so that the total rank $s$ of all edge changes is below $Wm$, and unroll the resulting recursion once with bit gates (address-chunk interchange) and once with Gaussian-dyadic phase gates (simultaneous butterfly layer). (on [Recursive rank saving](rank-saving-recurrence.md))
- Fast address-chunk interchange: swapping two disjoint contiguous address fields of $u$ bits, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, takes $O(Vu^\tau)$ time with $\tau=1-2^{-50}$.; how: Run the bit network with address-shear frames, so that an edge matrix of rank $a$ costs $a$ smaller interchanges on role streams of volume $V/W$; solve the resulting recurrence, then remove the power-width and row restrictions. (on [Fast address-chunk interchange](address-chunk-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.5.1.1, S4.5.1.2, S4.5.1.3, S4.5.1.4, S4.5.1.5, S4.5.1.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.5.1.1**: Every rational $m\times m$ matrix $A$ of rank $a$ factors as $A=E_1\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\Pi$ having exactly $a$ ones, at most one per row and column (Bruhat factorization with reversed coordinate order).
Source: "Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization" (paper)
> \begin{lemma}[Lower triangular factorization] \label{lem:lower-lower} Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization \[ A=E_1\Pi E_2, \] where $E_1,E_2$ are invertible lower triangular rational matrices and $\Pi$ has exactly $a$ entries equal to one, with at most one in each row and column, and all remaining entries zero. \end{lemma}

**S4.5.1.2**: Elimination picks the topmost nonzero row and its rightmost nonzero entry, clears its column to the left by right multiplication and below by left multiplication with lower triangular elementary matrices, scales the pivot to one, deletes that row and column, and repeats; the number of pivots is the rank.
Source: "nonzero row and its rightmost nonzero entry." (paper)
> \begin{proof} If $A=0$, take $E_1=E_2=I$ and $\Pi=0$. Otherwise choose the topmost nonzero row and its rightmost nonzero entry. Use that pivot column to clear entries to its left by right multiplication by lower triangular elementary matrices. There are no nonzero entries to its right in the pivot row. Clear entries below the pivot by left multiplication by lower triangular elementary matrices, and scale the pivot to one. All rows above the chosen row were zero in the still active columns.

**S4.5.1.3**: A fixed odd prime $q$ avoiding all denominators and diagonal numerators in a finite table of factors lets all rational identities specialize to $\mathbb Z/q^b\mathbb Z$ with the triangular factors invertible.
Source: "Choose an odd prime avoiding every denominator" (paper)
> \begin{proof} Choose the factorizations of Lemma~\ref{lem:lower-lower} for all matrices in $\mathcal A$ once and for all. Include their factors and inverses in a finite rational table. Choose an odd prime avoiding every denominator in the table and every numerator of a diagonal entry of an invertible factor. For example, a prime exceeding the absolute values of all its nonzero numerators and denominators suffices. Rational elimination and trial division construct this finite table and a suitable prime in a finite computation independent of $b$. They may therefore be compiled into one fixed machine description. All these rational identities then specialize to $\mathbb Z/q^b\mathbb Z$, and the triangular factors remain invertible there.

**S4.5.1.4**: A lower triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a diagonal unit and a fixed combination of earlier coordinates (controlled shifts).
Source: "A lower triangular transformation of $H$, or of $D$, costs $O(V)$:" (paper)
> A lower triangular transformation of $H$, or of $D$, costs $O(V)$: update coordinates in descending physical order. At coordinate $i$, multiply by its diagonal unit and add a fixed linear combination of earlier coordinates. These earlier coordinates still have their original values. Apply Lemma~\ref{lem:ordered-affine-streams}; the number of coordinates is the fixed number $m$. Inverses are also lower triangular.

**S4.5.1.5**: Each one at position $(i,j)$ of $\Pi$ calls for $H_i\gets H_i+D_j$, done by $D_j\gets D_j+H_i$, then interchanging $(H_i,D_j)$, then $D_j\gets H_i-D_j$; from $(h,d)$ this gives $(h+d,d)$ using just one interchange, so $a$ ones cost $a$ interchanges.
Source: "D_j\leftarrow D_j+H_i,\qquad" (paper)
> For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, then add $\Pi D$ to $H$, and finally transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Each one in position $(i,j)$ of $\Pi$ calls for $H_i\leftarrow H_i+D_j$. Implement it by \[ D_j\leftarrow D_j+H_i,\qquad (H_i,D_j)\leftarrow(D_j,H_i),\qquad D_j\leftarrow H_i-D_j. \] The first and last updates target a later field controlled by an earlier field. On an initial pair $(h,d)$ this sequence yields $(h+d,d)$. It uses just one interchange. There are $a$ ones, which proves the claim. In particular, the number of recursive calls is the rational rank $a$; temporary tapes used for the other operations do not multiply that count. \end{proof}

**S4.5.1.6**: Three shears $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ interchange $H$ and $D$; only the middle shear needs the network, the other two target the later group and have linear cost.
Source: "D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D," (paper)
> To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md): Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.
  Shown as: Address shear and lower-triangular factorization *<predicate>* Rank, subspaces and orthogonal complements
- [Controlled cyclic shifts](controlled-shift.md): An update y ↦ y + a(controls) mod Q of a target field that follows its control fields on tape, done in O(V) by splitting each fiber at the offset and merging the two pieces in the opposite order; also multiplication by a fixed unit and negation of the target.
  Shown as: Address shear and lower-triangular factorization *<predicate>* Controlled cyclic shifts
- [Elementary stream operations](elementary-stream-ops.md): Linear-time (O(V)) tape scans that permute two radix-q digits, move a digit, split an array into aligned streams on a digit, apply a pointwise map and merge, or deal whole rows cyclically to W streams.
  Shown as: Address shear and lower-triangular factorization *<predicate>* Elementary stream operations

## Pages that build on this one

- Fast address-chunk interchange: The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Linear exchange network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](common-frame-principle.md)
- [Subspace labels from three-element subsets](subset-intersection-labels.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "updated by $(H,D)\mapsto(H+D,D)$." (paper)

  > For the bit procedure, that endpoint operator is an address shear: two fields, written as vectors $H,D$ over a common residue ring, are updated by $(H,D)\mapsto(H+D,D)$. Two further linear-cost address updates complete their interchange. For the numerical procedure, the endpoint operator becomes the simultaneous $H_0$ layer after diagonal phase operations and a dyadic scale. The intermediate frames are chosen so that every edge can be implemented by smaller calls to the same procedure.

- "A=E_1\Pi E_2," (paper)

  > \begin{lemma}[Lower triangular factorization] \label{lem:lower-lower} Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization \[ A=E_1\Pi E_2, \] where $E_1,E_2$ are invertible lower triangular rational matrices and $\Pi$ has exactly $a$ entries equal to one, with at most one in each row and column, and all remaining entries zero. \end{lemma}

- "D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D," (paper)

  > To interchange the two full chunks, perform \[ D\leftarrow D-H,\qquad H\leftarrow H+D,\qquad D\leftarrow H-D, \] componentwise. Only the middle shear uses the circuit. The other two updates target the later group and have linear cost. The transformation sends $(H,D)$ to $(D,H)$.


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

Write the body to `exegenius/tasks/0013-write-address-shear.answer.md` and the JSON to `exegenius/tasks/0013-write-address-shear.answer.json`, then run `exegenius submit 0013-write-address-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0013-write-address-shear`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
