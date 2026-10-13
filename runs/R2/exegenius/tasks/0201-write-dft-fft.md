# exegenius task 0201-write-dft-fft

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
- The n log n optimality conjecture
- Reduction of integer product to digit convolution
- Polynomial ring modulo $y^r+1$
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring degree): The power of two giving the number of coefficients in each polynomial.
- Address fields and array layout on tapes (also: fields, address rearrangements and signed shifts)
- Binary representation and bit operations (also: bits, XOR, bitwise operations, base 2)
- Modular arithmetic (also: congruence, residues mod m, remainder arithmetic)
- Prime numbers and coprimality (also: primes, relatively prime, gcd, distinct primes)
- Logarithms and floor/ceiling (also: lg, log base 2, floor, ceiling, iterated logarithm)
- Vectors, matrices and inverses (also: linear algebra, matrix multiplication, invertible matrix, dot product, orthogonality, linear map, norm)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Limits, series and convergence (also: geometric series, summation, converging sum, epsilon bounds)
- Cartesian product and tuples (also: product of sets, index tuples, mixed radix, multi-index)
- Permutations (also: bijection, rearrangement, reordering, inverse permutation)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n})
- Rings and basic algebraic structures (also: ring, commutative ring, group, quotient ring, residue ring)
- Fixed-point and rounding arithmetic (also: rounding error, truncation, fixed-point numbers, absolute error)

## This page

Concept: Discrete Fourier transform and butterflies
Gloss: Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
Also called: transform (the DFT/FFT the layout is for), twiddle factor, bit-reversed input, forward transform of length S

## Where the argument relies on this page

- A simultaneous layer of $H_0(u,v)=((u+v)/2,(u-v)/2)$ on selected address bits of polynomial-valued arrays costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with a single truncation at the end. (on [Fast simultaneous butterfly layers](fast-butterfly-layers.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity converts the middle transform into normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein-chirp.md))
- Convolution over $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by synthetic transforms and packed polynomial products. (on [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md))
- Synthetic transforms over the polynomial ring need only signed shifts, address rearrangements and butterflies. (on [Synthetic polynomial transforms](synthetic-transforms.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (integer length), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The number of bits in each of the two integers being multiplied.
- $A$ (fixed-tape machine), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The paper's deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.
- $T_A$ (running time of A), bound on [The n log n optimality conjecture](nlogn-conjecture.md): The worst-case running time of machine A on pairs of n-bit inputs.
- $\kappa$ (logarithm exponent gap), bound on [The n log n optimality conjecture](nlogn-conjecture.md): A fixed positive constant, equal to 2^{-182}.
- $n$ (list length), bound on [Convolution](convolution.md): The number of entries in each input and output coefficient list.
- $a$ (input list a), bound on [Convolution](convolution.md): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
- $b$ (input list b), bound on [Convolution](convolution.md): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
- $c$ (output list), bound on [Convolution](convolution.md): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
- $i$ (index i), bound on [Convolution](convolution.md): An index into the entries of the input list $a$.
- $j$ (index j), bound on [Convolution](convolution.md): An index into the entries of the input list $b$.
- $k$ (output index), bound on [Convolution](convolution.md): An index into the entries of the output list $c$.
- $y$ (indeterminate), bound on [Convolution](convolution.md): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
- $x$ (first integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The first of the two integers being multiplied.
- $y$ (second integer), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The second of the two integers being multiplied.
- $b$ (digit width), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of bits in each radix digit.
- $q$ (digit count), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The number of radix digits of each input.
- $x_j$ (radix digit of x), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $x$, a value below $2^b$.
- $y_j$ (radix digit of y), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The $j$th radix digit of $y$, a value below $2^b$.
- $h_k$ (carry), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The carry into position $k$ in the radix-$2^b$ carry propagation, with $h_0=0$.
- $d_k$ (output digit), bound on [Reduction of integer product to digit convolution](radix-digit-reduction.md): The radix-$2^b$ digit at position $k$ of the product.
- $y$ (ring variable), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The polynomial variable of the ring, whose powers act as roots of unity.
- $r$ (ring degree), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The number of complex coefficients in each element of the ring, a power of two.
- $j$ (rule exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent left after removing $y^r$ from $y^{r+j}$, with $0\le j<r$.
- $s$ (reduced exponent), bound on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): The exponent of the power $y^s$ that equals a given power of $y$, with $0\le s<2r$.
- $m$ (tape position), bound on [Address fields and array layout on tapes](address-fields.md): The position of an item in tape order, so the item sits in the m-th cell.
- $u$ (field width), bound on [Address fields and array layout on tapes](address-fields.md): The number of bits in one address field.
- $V$ (stored bit volume), bound on [Address fields and array layout on tapes](address-fields.md): The total number of bits the array holds.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Convolution](convolution.md): Product of polynomials / combination of coefficient lists where entries sum by index (cyclic if indices wrap).
  Shown as: Discrete Fourier transform and butterflies *<predicate>* Convolution
- [Address fields and array layout on tapes](address-fields.md): Arrays stored in tape order with addresses forming a Cartesian product of digit fields; rearranging fields costs time.
  Shown as: Discrete Fourier transform and butterflies *<predicate>* Address fields and array layout on tapes

## Pages that build on this one

- Schönhage–Strassen to Harvey–van der Hoeven multiplication: Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.
- Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies.
- Gaussian resampling: Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths.
- Bluestein's chirp identity: Rewrites a discrete Fourier transform as a cyclic convolution via chirp phases.
- Fixed-point precision and exact recovery: Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.

## Other pages you may link to

- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Reduction of integer product to digit convolution](radix-digit-reduction.md)
- [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md)
- [Fixed-tape machine model and stream operations](fixed-tape-model.md)
- [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Finite linear network with roles and frames](linear-network-roles.md)
- [Restoring auxiliary scratch values](scratch-restoration.md)
- [Address shear and lower-triangular factorization](address-shear-factorization.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist-convolution.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed coefficient packing (Kronecker substitution)](signed-packing.md)
- [Convolution with retained transform order and cancelled permutations](ring-convolution-retained-order.md)
- [Tensor product of vector spaces](tensor-product-of-vector-spaces.md)
- [Three-element subset intersection construction](subset-intersection-construction.md)
- [Recursive power saving from s<Wm](recursive-power-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n(lg n)^{1-κ}) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "two-point butterfly operations" (paper)

  > In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations. Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic. Two tape procedures supply them; in both bounds, $V$ denotes the stored bit volume.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $m$ means frequency index here, but tape position on [Address fields and array layout on tapes](address-fields.md), which this page builds on: Use another letter for the frequency index instead of m, since m is the tape position on the address-fields page.
- $u$ means first butterfly input here, but field width on [Address fields and array layout on tapes](address-fields.md), which this page builds on: Use another letter for the butterfly input instead of u, since u is the field width on the address-fields page.

## Previous version (revise it)

It has 269 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 336 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The discrete Fourier transform (DFT) evaluates a coefficient list at powers of a root of unity, reducing [Convolution](convolution.md) to a pointwise product.

Let $a=(a_0,\dots,a_{n-1})$ have $n$ entries, a power of two. For $0\le m<n$, the letter $m$ is the frequency index (the letter $m$ changes meaning here, from the tape position on the earlier address-fields page). Let $\omega$ be a primitive $n$-th root of unity: $\omega^n=1$ and $\omega^m\ne1$ for $0<m<n$. The transform of $a$ is the list $A=(A_0,\dots,A_{n-1})$ with

$$A_m=\sum_{i=0}^{n-1} a_i\,\omega^{im}.$$

Here the letter $A$ changes meaning from the machine $A$ of the earlier pages.

A butterfly is the two-point operation $(u,v)\mapsto(u+\omega^s v,\;u-\omega^s v)$, where $u$, $v$ are its inputs and $s$ its exponent (these letters change meaning here: on the earlier address-fields page, $u$ is a field width).

Since $\omega^{n/2}=-1$, splitting $a$ by the parity of $i$ gives $A_m=E_m+\omega^mO_m$ and $A_{m+n/2}=E_m-\omega^mO_m$ for $0\le m<n/2$, where $E$ and $O$ are the transforms with root $\omega^2$ of the even- and odd-indexed entries.

Let $h$ be the number of entries in a block, and $t$, $0\le t<h/2$, an offset in it. With bit-reversed input, a block of size $h$ computes a transform with root $\omega^{n/h}$ from two halves that are transforms with root $\omega^{2n/h}$. The split above, with $\omega^{n/h}$ in place of $\omega$, pairs offsets $t$ and $t+h/2$ into a butterfly with exponent $s=tn/h$. The levels $h=2,4,\dots,n$ leave $A_0,\dots,A_{n-1}$ in order.

On tapes, the transform is built from butterflies and the address rearrangements of [Address fields and array layout on tapes](address-fields.md). Each level is one rearrangement that makes partners $t$ and $t+h/2$ adjacent, then one scan of butterflies. The paper's tape-level transform uses the same kinds of operation <cite data-source="paper">address rearrangements, signed shifts, and two-point butterfly operations</cite>.

Let $c_k=\sum_i a_i\,b_{(k-i)\bmod n}$ be the convolution, with transforms $B$ of $b$ and $C$ of $c$. Let $l=(k-i)\bmod n$ be the index into $b$ paired with $i$ at output $k$. Since $\omega^{km}=\omega^{(i+l)m}$ and $l$ runs over all indices for fixed $i$, $C_m=\sum_i a_i\omega^{im}\sum_l b_l\omega^{lm}=A_mB_m$.

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

Write the body to `exegenius/tasks/0201-write-dft-fft.answer.md` and the JSON to `exegenius/tasks/0201-write-dft-fft.answer.json`, then run `exegenius submit 0201-write-dft-fft` in the project directory. If submit rejects the answer, fix the answer and submit again.
