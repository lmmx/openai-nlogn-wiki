# exegenius task 0024-write-fast-butterfly-layers

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
- Discrete Fourier transform
- Fixed-point complex values and Gaussian dyadics
- Harvey–van der Hoeven O(n log n) multiplier as subroutine
- Polynomial ring modulo y^r + 1 (also: synthetic roots of unity)
  - $y$ (ring variable): The indeterminate of the polynomial ring, with y^r equal to -1.
  - $r$ (record length): The number of complex coefficients in a record, a power of two.
- Synthetic polynomial transform (also: polynomial transform)
- Two-point butterfly H₀
- Array addresses, fields and chunks
- Linear exchange network with roles and frames
- Three-element-subset network with rank saving
- Recursive power saving from s < Wm
- Lower triangular factorization of address shears
- Fast interchange of address chunks
- Signed packing (Kronecker substitution)
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein's chirp identity
- Phase twist to the negacyclic last coordinate
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

Concept: Fast simultaneous butterfly layers
Gloss: Applies H₀ on the same bit position in each of d address chunks of arrays of complex polynomial records in time O(V d^λ') with λ' < 1, evaluated exactly with one final truncation.

## This page in the argument

The step: The two-point butterfly $H_0$ can be applied at the same bit position in each of $d$ address chunks of an array of polynomial records of volume $V$ in time $O(Vd^{\lambda'})$ with $\lambda'<1$.
How: Apply the complex phase network with the same rank-saving recursion, using fast chunk interchanges for the changes of basis and exact dyadic arithmetic
Why: Doing the $d$ butterfly factors separately needs $d$ whole-array passes; the same rank-saving recursion that speeds interchange applies to a common layer and makes it cost a power $d^{\lambda'}$ of a pass. (the sources say so: "whereas separate butterfly factors would require $D$ whole-array passes." (paper))
Striking feature: The exponent $\lambda'<1$ is a power saving over $d$ separate passes, coming from the same strict inequality of the complex network. (explain why it holds, from the method)

Its sub-steps, in order:

- The butterfly layer is a tensor product of an auxiliary two-point kernel whose phase frames use smaller groups of selected bits separated by binary changes of basis.
- The changes of basis are implemented by whole address chunk moves, using the fast interchange, and splitting complete rows among the network's roles reduces the volume of each recursive call.
- The intermediate dyadic values are bounded and the completed layer is converted to the normalized $H_0$ layer, evaluated exactly before one truncation.
- The simultaneous normalized butterfly layer returns $Q_p(\mathcal H z)$ in time $O(Vd^{\lambda'})$ with error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to digit convolution computed by Fourier transforms, and speed up the two bottlenecks, address rearrangement and butterfly layers, by a recursion with a strict rank saving (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1, S3.2, S3.3, S3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1**: The butterfly layer is a tensor product of an auxiliary two-point kernel whose phase frames use smaller groups of selected bits separated by binary changes of basis.
Source: "We first construct tensor products of the auxiliary two-point kernel" (paper)
> We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.

**S3.2**: The changes of basis are implemented by whole address chunk moves, using the fast interchange, and splitting complete rows among the network's roles reduces the volume of each recursive call.
Source: "selected bits, separated by binary changes of basis. We implement those" (paper)
> We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.

**S3.3**: The intermediate dyadic values are bounded and the completed layer is converted to the normalized $H_0$ layer, evaluated exactly before one truncation.
Source: "call. Finally, we bound the intermediate dyadic values and convert the" (paper)
> We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.

**S3.4**: The simultaneous normalized butterfly layer returns $Q_p(\mathcal H z)$ in time $O(Vd^{\lambda'})$ with error below $\sqrt2\,2^{-p}$.
Source: "coefficient order, and component format in $O(Vd^{\lambda'})$ time," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Recursive power saving from s < Wm](recursive-power-saving.md): A recursive call at parameter mf uses s calls on streams of volume V/W, so the cost per volume grows by s/W < m per factor m in the parameter, giving a power saving.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Recursive power saving from s < Wm
- [Two-point butterfly H₀](butterfly.md): The map H_0(u,v) = ((u+v)/2, (u-v)/2) on a pair of values, the basic step of radix-two transforms.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Two-point butterfly H₀
- [Fixed-point complex values and Gaussian dyadics](fixed-point-dyadics.md): Complex numbers stored as pairs of two's-complement integers over a power-of-two denominator 2^p, truncated toward zero, with contractive (norm ≤ 1) linear maps and error accumulation.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Fixed-point complex values and Gaussian dyadics
- [Fast interchange of address chunks](fast-interchange.md): Interchanges two equal address chunks of u digits in time O(V u^τ) for a fixed τ < 1 via XOR-like linear combinations, ending in an exact permutation.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Fast interchange of address chunks
- [Polynomial ring modulo y^r + 1](polynomial-ring.md): Complex polynomials of degree less than r with y^r = -1, so multiplying by a power of y is a signed cyclic shift of the coefficient list; powers of y act as roots of unity.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Synthetic transform on a retained-order layout: Transforms on several axes are computed by simultaneous butterfly layers on a tape layout, with the frequency order kept through the pointwise product so the opposite transform consumes it.

## Other pages you may link to

- [Convolution](convolution.md)
- [Fixed-tape machine model and tape streams](tape-streams.md)
- [The n log n conjecture and history of multiplication](nlogn-conjecture.md)
- [Array addresses, fields and chunks](address-fields.md)
- [Linear exchange network with roles and frames](linear-network.md)
- [Three-element-subset network with rank saving](subset-network.md)
- [Harvey–van der Hoeven O(n log n) multiplier as subroutine](hvdh-multiplier.md)
- [Lower triangular factorization of address shears](shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Phase twist to the negacyclic last coordinate](phase-twist.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform on a retained-order layout](transform-layout.md)
- [Normalized convolution over the polynomial ring](ring-convolution.md)
- [Resampling with permutations left in the transform](retained-permutations.md)
- [Reduction of integer multiplication to digit convolution](radix-digit-reduction.md)
- [Precision and exact recovery](precision-recovery.md)
- [The multiplication algorithm and its cost](multiplication-algorithm.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "the cost is $O(Vd^{\lambda'})$ for a" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "We now apply the complex network to a common butterfly layer on several" (paper)

  > We now apply the complex network to a common butterfly layer on several axes. The array has complete address set \[ [P]\times[2^K]^D\times[S],\qquad 1\le D\le d, \] with $P,S\ge1$, in lexicographic order. Its $D$ consecutive $K$-bit chunks each select the bit at one common offset $0\le\rho<K$, counted from the least significant end. Each address carries a polynomial record with $r$ complex coefficients, initially in the unit disk on the grid $2^{-p}\mathbb Z[i]$, with $\Theta(p)$ bits per real or imaginary component. The intended operation is the tensor product of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on the $D$ selected bits, acting coefficientwise and preserving all other address fields.


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

Write the body to `exegenius/tasks/0024-write-fast-butterfly-layers.answer.md` and the JSON to `exegenius/tasks/0024-write-fast-butterfly-layers.answer.json`, then run `exegenius submit 0024-write-fast-butterfly-layers` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0024-write-fast-butterfly-layers`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
