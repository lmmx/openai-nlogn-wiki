# exegenius task 0029-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/D5` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis and recurrences, discrete mathematics (modular arithmetic, primes, gcd, permutations, binary representation), introductory linear algebra (matrices, rank, invertibility, vector spaces), and basic algebra with polynomials and complex numbers. They know algorithms such as schoolbook multiplication, divide and conquer and sorting, and basic Turing machines with tapes. They have not studied the FFT or Schönhage–Strassen in depth, rings and finite fields beyond basics, tensor products, or the specialist multitape-complexity and fast-multiplication literature.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Multiplication history and the n log n conjecture
- Convolution and the discrete Fourier transform
- Multiplication as convolution of radix digits
- FFT butterflies
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomial, whose powers play the role of roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial; a power of two and the degree bound of the ring elements.
- Synthetic polynomial transforms
- Multidimensional transforms with tensor structure
- Chinese-remainder coefficient address map
- Gaussian resampling
- Bluestein chirp conversion
- Phase twist from cyclic to negacyclic
- Signed packing of polynomial products
- Dyadic fixed-point arithmetic and rounding
- Array order and elementary stream operations
- Controlled shifts and rational scalings
- Linear networks with frames
- Finite networks from three-element subsets
- Recursive power saving
- Lower triangular factorization and matrix shear
- Fast address-field interchange
  - $V$ (stored bit volume): The number of stored data bits in the array.
  - $u$ (field width): The number of radix digits in each of the two interchanged address fields.
  - $\tau$ (interchange exponent): A fixed constant strictly less than one controlling the cost.
- Fast simultaneous butterfly layer
  - $V$ (stored bit volume): The number of stored data bits in the array.
  - $d$ (number of chunks): The number of equal-width address chunks (axes) whose selected bit gets a butterfly simultaneously.
  - $\lambda'$ (layer exponent): A fixed constant strictly less than one controlling the cost.
- Synthetic transform layout and convolution cost
- Resampling without executing the permutations
- Parameter choice and total cost accounting
- Schoolbook multiplication and divide and conquer (also: grade-school multiplication, quadratic multiplication, Karatsuba idea, recursion on halves)
- Recurrences and geometric sums (also: recurrence relations, master theorem, geometric series)
- Logarithms, floors and ceilings (also: lg n, log base 2, floor and ceiling, powers of two)
- Binary representation and bitwise operations (also: bits, XOR, exclusive or, binary digits, base-2 expansion, radix representation)
- Modular arithmetic (also: congruences, residues mod n, remainder, units mod q)
- Divisibility, primes and coprimality (also: gcd, greatest common divisor, relatively prime, pairwise coprime, prime numbers)
- Permutations and sorting (also: bijections of a finite set, sorting algorithms, reordering an array)
- Linear algebra over a field (also: matrices, matrix multiplication, invertible matrix, rank, vector space, subspace, dimension, linear map, basis)
- Triangular matrices and elementary operations (also: lower triangular matrix, row operations, Gaussian elimination, identity matrix)
- The field with two elements (also: F_2, GF(2), Z/2Z, binary field, mod 2 arithmetic)
- Rational numbers and dyadic fractions (also: rationals, Q, dyadic rationals, fixed-point numbers, binary fractions)
- Rounding and approximation error (also: truncation, nearest integer, absolute error, error bound, triangle inequality)
- Cyclic groups and powers of a generator (also: Z/nZ, cyclic group, additive group mod n, order of an element)
- Array indexing by tuples and mixed radix (also: multi-index, lexicographic order, row-major order, mixed-radix representation, multidimensional array)
- Sums, products and indicator notation (also: summation notation, Kronecker delta, indicator function, sigma notation)
- Basic complexity of tape computation (also: linear-time scan, one pass over a tape, copying a tape, deterministic algorithm)
- Euclidean norm and inequalities (also: absolute value of complex number, modulus, contraction, Cauchy–Schwarz, norm)
- Gaussian integers (also: Z[i], complex integers, integer complex numbers)

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it chains CRT map, Gaussian resampling, chirps, twist and synthetic transforms accelerated by the fast interchange and butterfly layers.

## This page in the argument

The step: A deterministic fixed multitape Turing machine multiplies two $n$-bit integers in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.
How: reduce multiplication to a convolution over $\mathbb C[y]/(y^r+1)$ via CRT, Gaussian resampling, chirps and a twist, and evaluate its transforms with fast interchange and butterfly layers
Why: Splitting into radix digits reduces multiplication to convolution; the transforms need power-of-two axes and polynomial roots of unity, and the two tape procedures supply the saving. The text builds the tape tools first and then the reductions. (the sources leave this for the reader to work out: spell it out)
Striking feature: The saving is a power of $\lg n$ (the exponent $\kappa=2^{-182}$ is tiny but positive), not a $\log\log$ factor. (explain why it holds, from the method)

Its sub-steps, in order:

- Two tape procedures, fast address interchange and fast simultaneous butterfly layers, make address movement and Fourier layers cost less than a full scan per level.
- Convolution over $\mathbb C[y]/(y^r+1)$ on $T$ entries is computed at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Synthetic transform layout and convolution cost](transform-layout-cost.md))
- The Fourier transform of pairwise coprime lengths $s_i$ is expressed through power-of-two transforms with the coordinate permutations kept in the identity. (on [Resampling without executing the permutations](resampling-no-sort.md))
- A chirp identity writes $QF_{\boldsymbol t}$ as a chirp multiplication around a cyclic convolution, and the source permutation $R$ cancels across the two forward transforms and the opposite transform. (on [Bluestein chirp conversion](bluestein-chirp.md))
- Chain the CRT map, twist and chirp procedures with the transforms, recover the integer coefficients exactly, and total the cost.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Two tape procedures, fast address interchange and fast simultaneous butterfly layers, make address movement and Fourier layers cost less than a full scan per level.
How: build the elementary scans, then the network-based recursive saving, then the two accelerated procedures
- S1.3: Two fixed linear networks exchange banks of values and restore auxiliary values, with strictly fewer than $Wm$ smaller calls in total.
  How: construct a linear network with frames, label it by subspaces, and read off a recurrence

**S5**: Chain the CRT map, twist and chirp procedures with the transforms, recover the integer coefficients exactly, and total the cost.
How: assemble the reductions of the pipeline and account for every representation change
- S5.3: The chirp phases and the middle transform are evaluated with the complex convolution and composed with the Gaussian maps.
  Source: "We next use the complex convolution to evaluate the middle factor" (paper)
  > We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps. For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator at tensor address $j$ is computed modulo $2r$ as \[ -\sum_i s_i j_i^2(r/t_i)\pmod{2r}. \] All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$. Scan the stored axis descriptors and compute the $d$ squares and products with the previously established integer multiplier. Additions, reductions modulo a power of two, and restarting local counters cost $O(p)$ per term; multiplication costs $O(p\log p)=O(p^{1+\delta})$. Exponential evaluation then has the same $O(p^{1+\delta})$ bound. Thus chirp construction costs $O(Td p^{1+\delta})$ in total. In particular, this cost includes the scan of the axis descriptors at every coefficient.
- S5.4: Digit extraction, $\Phi$, three transforms, a pointwise product, two rescalings, rounding and carry propagation produce the product.
  Source: "The source-transform procedures now supply the three transforms needed" (paper)
  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Synthetic transform layout and convolution cost](transform-layout-cost.md)): Convolution over $\mathbb C[y]/(y^r+1)$ on $T$ entries is computed at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- S3 (on [Resampling without executing the permutations](resampling-no-sort.md)): The Fourier transform of pairwise coprime lengths $s_i$ is expressed through power-of-two transforms with the coordinate permutations kept in the identity.
- S4 (on [Bluestein chirp conversion](bluestein-chirp.md)): A chirp identity writes $QF_{\boldsymbol t}$ as a chirp multiplication around a cyclic convolution, and the source permutation $R$ cancels across the two forward transforms and the opposite transform.
- S1.1 (on [Array order and elementary stream operations](stream-scans.md)): Splitting, digit moves and row splits on an array of volume $V$ are linear-time scans.
- S1.2 (on [Controlled shifts and rational scalings](controlled-shifts.md)): Updating a later address field by an offset computed from earlier control fields, or scaling it by a rational unit, costs $O(V)$.
- S1.3.1 (on [Linear networks with frames](linear-network-frames.md)): A network of pointwise linear gates with invertible frames $D_v$ leaves, along a route, only an endpoint operator on every role.
- S1.3.2 (on [Finite networks from three-element subsets](subset-subspace-networks.md)): Two fixed networks built from three-element subsets of $[h]$ have nested subspace labels whose edge rank changes sum to $s<Wm$.
- S1.3.3 (on [Recursive power saving](recursive-saving.md)): A call at parameter $mf$ makes $s<Wm$ calls at parameter $f$ on volume $V/W$, so the per-volume cost grows by $s/W<m^{\tau}$ per multiplication of the parameter by $m$, a power saving.
- S1.4 (on [Fast address-field interchange](address-interchange.md)): Two disjoint address fields of $u$ digits can be interchanged in time $O(Vu^{\tau})$ for a fixed $\tau<1$.
- S1.5 (on [Fast simultaneous butterfly layer](simultaneous-butterfly-layer.md)): A normalized butterfly layer on the same bit position of $d$ address chunks costs $O(Vd^{\lambda'})$ instead of $d$ whole-array passes.
- S5.1 (on [Chinese-remainder coefficient address map](crt-address-map.md)): The coefficient list is placed on pairwise coprime cyclic axes by the Chinese remainder map $\Phi$, preserving convolution, using controlled cyclic shifts.
- S5.2 (on [Phase twist from cyclic to negacyclic](coefficient-twist.md)): The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic convolution of length $r$ into the ring modulo $y^r+1$.
- S5.5 (on [Dyadic fixed-point arithmetic and rounding](fixed-point-precision.md)): The coefficient error is strictly below $1/2$, so rounding recovers the exact integer coefficients.
- S5.6 (on [Parameter choice and total cost accounting](parameter-choice-cost.md)): With $b=\lceil\log n\rceil$, $p=6b$, $d=\lfloor b^{\epsilon}\rfloor$ and fixed rational exponents, every row of the cost table is a power of $p$ at most $1-2\kappa$, giving $O(n(\lg n)^{1-\kappa})$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [FFT butterflies](fft-butterfly.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Synthetic transform layout and convolution cost](transform-layout-cost.md)
- [Resampling without executing the permutations](resampling-no-sort.md)
- [Chinese-remainder coefficient address map](crt-address-map.md)
- [Array order and elementary stream operations](stream-scans.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Parameter choice and total cost accounting](parameter-choice-cost.md): Choosing b=⌈log n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log T/d⌉} and fixed rational exponents with κ=2^{-182}, then summing the normalized cost table, every row of which is a power of p below 1.
  Shown as: Integer multiplication below n log n *<predicate>* Parameter choice and total cost accounting
- [Multiplication history and the n log n conjecture](nlogn-conjecture.md): Schönhage–Strassen's O(n log n log log n) multiplier, their conjecture that n log n is optimal, and the Harvey–van der Hoeven O(n log n) algorithm that the paper beats by a power of log n.
  Shown as: Integer multiplication below n log n *<predicate>* Multiplication history and the n log n conjecture
- [Multiplication as convolution of radix digits](radix-digit-convolution.md): Splitting each n-bit operand into short radix-2^b digits turns integer multiplication into a convolution of small integer coefficient lists, followed by rounding and carry propagation to get the exact binary product.
  Shown as: Integer multiplication below n log n *<predicate>* Multiplication as convolution of radix digits
- [Dyadic fixed-point arithmetic and rounding](fixed-point-precision.md): Complex coefficients stored as fixed-point Gaussian dyadics with p fractional bits; exact intermediate values, a single truncation after contractive layers, and error tracking so the final coefficient error is below 1/2.
  Shown as: Integer multiplication below n log n *<predicate>* Dyadic fixed-point arithmetic and rounding

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Multidimensional transforms with tensor structure](multidimensional-transform.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [FFT butterflies](fft-butterfly.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Signed packing of polynomial products](signed-packing-products.md)
- [Array order and elementary stream operations](stream-scans.md)
- [Linear networks with frames](linear-network-frames.md)
- [Finite networks from three-element subsets](subset-subspace-networks.md)
- [Recursive power saving](recursive-saving.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Lower triangular factorization and matrix shear](lower-triangular-shear.md)
- [Fast address-field interchange](address-interchange.md)
- [Fast simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform layout and convolution cost](transform-layout-cost.md)
- [Resampling without executing the permutations](resampling-no-sort.md)
- [Chinese-remainder coefficient address map](crt-address-map.md)

## Evidence from the sources, with the paragraph around each quote

- "computes this exact product for every $n\ge1$ and every pair of $n$-bit" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)," (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0029-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0029-write-main-theorem.answer.json`, then run `exegenius submit 0029-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
