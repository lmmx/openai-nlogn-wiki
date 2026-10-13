# exegenius task 0027-write-packed-bit-addition

Project directory: `/home/user/openai-nlogn-wiki/runs/G3` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: algorithm analysis with asymptotic notation and recurrences, discrete mathematics (induction, divisibility, gcd, primes, permutations, summations, modular arithmetic at the level of residues), the schoolbook and divide-and-conquer integer arithmetic algorithms, sorting, and the fast Fourier transform as an O(n log n) convolution algorithm. They have taken linear algebra (matrices, linear maps, rank, inverses, vector norms) and complex numbers, and know basic multitape Turing machines and bit-level data representation. They have not studied abstract algebra beyond what the existing concepts give, finite-field linear algebra, tensor products of vector spaces, analytic number theory, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- History of fast multiplication and the n log n conjecture
- Integer product as digit-polynomial convolution
- Discrete Fourier transform and cyclic convolution
- Multidimensional transforms on product axes
- Modular arithmetic and the Chinese remainder theorem
- Chinese-remainder address map to prime axes
- Fixed-point complex numbers on a disk grid
- Contractions and error accumulation
- Bluestein chirp identity
- Negacyclic ring ℂ[y]/(yʳ + 1)
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the polynomial coefficients are taken.
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a ring element, which is a power of two.
- Synthetic polynomial transforms
- Radix-2 butterflies and stored frequency order
- Elementary stream scans on tapes
- Controlled cyclic shifts of an address field
- Signed packing of polynomial products
- Subspaces, orthogonal complements and bilinear forms
- Matrix shears and triangular factorization
- Frames and pointwise gates
- Scratch-restoring bank-exchange network
- Nested subspace labels and the rank saving
- Recursion with a strict rank saving
- Fast address chunk interchange
- Phase frames and the two-point kernel C
- Binary representation of integers and radix expansions (also: binary numbers, base-b representation, radix-b digits, bit string value, most significant bit, padding with leading zeros)
- Schoolbook arithmetic and carries (also: long multiplication, grade-school multiplication, carry propagation, long division, linear-time integer addition)
- Fast Fourier transform and the convolution theorem (also: FFT, Cooley-Tukey algorithm, FFT-based multiplication, convolution theorem)
- Linear maps and matrices (also: matrix-vector product, matrix inverse, matrix rank, linear operator, diagonal matrix, identity matrix, invertible matrix, rational matrix)
- Vector norms and the triangle inequality (also: max norm, sup norm, infinity norm, operator norm, norm of a linear map, triangle inequality)
- Permutations of indices (also: coordinate permutation, bijection on indices, rearrangement of a list, permutation matrix, bit reversal permutation)
- Divisibility, gcd and coprime integers (also: greatest common divisor, relatively prime, Euclidean algorithm, division with remainder, quotient and remainder, modular inverse, units modulo n)
- Prime numbers and primality testing by trial division (also: primes, odd primes, trial division, prime search, finding primes in an interval)
- Floor, ceiling, rounding and logarithms (also: floor function, ceiling function, round to nearest integer, binary logarithm, lg, natural logarithm, integer part)
- Bitwise XOR and Hamming weight (also: exclusive or, XOR, addition modulo 2, parity, Hamming weight, population count, bit flip)
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, big-Theta, big-Omega, tight bound, lower bound)
- Recurrences, induction and geometric series (also: recurrence relation, proof by induction, geometric series, master theorem, unrolling a recurrence, telescoping sum)
- Sorting and its O(N log N) cost (also: merge sort, sorting on tapes, label and sort, comparison sorting)
- Summation, product and index notation (also: sigma notation, indicator function, Kronecker delta, Cartesian product of index sets, subscripts modulo q, ordered tuples)
- Integers, rationals and Gaussian integers (also: Z[i], dyadic rationals, Gaussian dyadics, integers modulo, rational numbers, real and imaginary parts)
- Euler's formula and complex exponentials (also: e^{i theta}, unit circle, modulus of a complex number, complex conjugate, polar form)
- Time and bit complexity of Turing machine computation (also: bit complexity, worst-case running time, sequential tape scan, head movement cost, finite-state control, unit-cost versus bit cost)

## This page

Concept: Packed addition on selected address bits
Gloss: A binary row addition y_j ← y_j ⊕ x_j on the same bit position of several address chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set.

## This page in the argument

The step: A binary row addition $y_j\leftarrow y_j\oplus x_j$ on the same bit position of several address chunks is done by a constant number of whole-chunk cyclic shifts plus a deterministic repair of a small exceptional address set, in $O(V(L^\tau+1))$ time.
How: Simulate the XORs of all chunks at once by eight packed cyclic shifts that are correct away from a small bad set of addresses, then repair exactly that set.
Why: The repair set depends only on addresses, so the bound is a worst-case bound over all payloads. (the sources say so: "The correction depends only on addresses, so the time bound is" (paper))
Striking feature: Cyclic shifts of packed fields reproduce XOR on all but a fraction $O(f2^{-K})$ of addresses, and that fraction does not depend on the data at all. (explain why it holds, from the method)

Its sub-steps, in order:

- Eight conditional additions of a control bit to two integers act on every square of parities as two three-cycles, which together flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.
- The addresses where a guard value leaves its safe interval form a set $\mathcal B$ with $|\mathcal B|\le\delta_{\rm bad}M$, independently of the record payload, and off $\mathcal B$ the packed shifts agree with the ideal XORs.
- Each shift is a chunk interchange costing $O(VL^\tau)$, and the permutation that repairs the small set $\mathcal B$ is applied by sorting only the exceptional records, so the total time is $O(V(L^\tau+1))$.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Reduce the product to a cyclic convolution of radix digits, evaluate it with Fourier-type transforms whose data movement and butterfly layers are accelerated by two power-saving tape procedures, recover the exact integers by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The two-point butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit position of each of $D\le d$ address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with exact intermediate values and a single truncation.; how: Express the layer through the kernel $C$, evaluate the $C$ layer by the complex network with phase frames so that each edge is a smaller layer on $e/m$ axes, implement the binary basis changes by packed additions, and convert back to $H_0$. (on [Fast simultaneous butterfly layer](butterfly-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2.1, S2.2.2, S2.2.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2.1**: Eight conditional additions of a control bit to two integers act on every square of parities as two three-cycles, which together flip the parity of $u$ exactly when $c=1$ and restore the auxiliary integer $w$.
Source: "If $c=0$, these operations do nothing. If $c=1$, the first four operations" (paper)
> from a small set of addresses. We then correct exactly that set. For a Boolean control $c$ and arbitrary integers $u,w$, perform the following eight operations in the displayed chronological order. Every predicate uses the current values of the integers. \begin{equation} \label{eq:eight-packed-additions} \begin{array}{rcl@{\qquad}l} u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\ w&\leftarrow&w-c[\,u\equiv0\pmod2\,],&(2)\\ u&\leftarrow&u+c[\,w\equiv0\pmod2\,],&(3)\\ w&\leftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If $c=0$, these operations do nothing. If $c=1$, the first four operations induce the cycle $(00\ 01\ 10)$ in every square \[ \{2a,2a+1\}\times\{2b,2b+1\},\qquad a,b\in\mathbb Z, \] where the corner labels record the parities of $(u,w)$. The last four induce $(01\ 10\ 11)$. Applying the first cycle and then the second gives $(00\ 10)(01\ 11)$. These facts follow by substituting the four parity pairs into the displayed operations; translation by $(2a,2b)$ does not change any predicate. Consequently the complete output is \begin{equation} \label{eq:eight-packed-result} (u',w')= \bigl(u+c(1-2(u\bmod2)),\ w\bigr). \end{equation} Here $u\bmod2\in\{0,1\}$, also for negative $u$. Thus the parity of $u$ is flipped precisely when $c=1$, both quotients under division by two are prese

**S2.2.2**: The addresses where a guard value leaves its safe interval form a set $\mathcal B$ with $|\mathcal B|\le\delta_{\rm bad}M$, independently of the record payload, and off $\mathcal B$ the packed shifts agree with the ideal XORs.
Source: "|\mathcal B|\le\delta_{\rm bad}M." (paper)
> There are exactly twenty excluded values for each guard in \eqref{eq:packed-guard-interval}. Since its complete range has $2^{K-1}$ values, the union bound over the $2(f-1)$ guards gives \begin{equation} \label{eq:packed-bad-fraction} |\mathcal B|\le\delta_{\rm bad}M. \end{equation} Indeed, the complete $y,z$ ranges give the same guard distribution at each choice of spectator coordinates. No record value enters this count.

**S2.2.3**: Each shift is a chunk interchange costing $O(VL^\tau)$, and the permutation that repairs the small set $\mathcal B$ is applied by sorting only the exceptional records, so the total time is $O(V(L^\tau+1))$.
Source: "descriptor has $O(A_{\rm rect})$ bits. The swap costs $O(VL^\tau)$, including" (paper)
> For one rotation, move its target to the rightmost of the three chunk positions if necessary. Let $P^{\rm sw}$ be the product of the record field lengths before the earlier exchanged chunk, let $G^{\rm sw}$ be the product between the exchanged chunks, and let $B^{\rm sw}$ be $R$ times the product after the later one. Empty products are one. The bit array has exactly the shape \[ [P^{\rm sw}]\times[2^L]\times[G^{\rm sw}] \times[2^L]\times[B^{\rm sw}]. \] The third chunk lies inside one collapsed spectator interval. Pass only $L$ and these three positive canonical lengths to Lemma~\ref{lem:chunk-swap}. Each length is at most $V$, so the local descriptor has $O(A_{\rm rect})$ bits. The swap costs $O(VL^\tau)$, including its own padding and cleanup.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast address chunk interchange](address-interchange.md): Two disjoint equal-width address chunks of u bits are exchanged in O(V u^τ) time for a fixed τ < 1 by computing XOR combinations of intermediate streams through the bit network, even though the net effect is an exact permutation.
  Shown as: Packed addition on selected address bits *<predicate>* Fast address chunk interchange
- [Controlled cyclic shifts of an address field](controlled-shifts.md): Updating a target field y mod q^b by an offset computed from earlier control fields, or multiplying it by a unit, costs O(V) on tape by splitting each fiber at the offset and merging the pieces swapped.
  Shown as: Packed addition on selected address bits *<predicate>* Controlled cyclic shifts of an address field

## Pages that build on this one

- Fast simultaneous butterfly layer: The two-point butterfly H₀ applied at once to one bit position of each of up to d address chunks of polynomial records costs O(V d^λ′) with λ′ < 1, evaluated exactly in Gaussian dyadics and truncated once.

## Other pages you may link to

- [History of fast multiplication and the n log n conjecture](mult-history.md)
- [Integer product as digit-polynomial convolution](radix-convolution.md)
- [Negacyclic ring ℂ[y]/(yʳ + 1)](negacyclic-ring.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Elementary stream scans on tapes](stream-scans.md)
- [Subspaces, orthogonal complements and bilinear forms](linear-spaces.md)
- [Frames and pointwise gates](common-frame.md)
- [Scratch-restoring bank-exchange network](scratch-network.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Phase frames and the two-point kernel C](phase-frames.md)
- [Fixed-point complex numbers on a disk grid](fixed-point-grid.md)
- [Discrete Fourier transform and cyclic convolution](dft-convolution.md)
- [Multidimensional transforms on product axes](multidim-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Radix-2 butterflies and stored frequency order](butterfly-order.md)
- [Contractions and error accumulation](contraction-error.md)
- [Modular arithmetic and the Chinese remainder theorem](modular-crt.md)
- [Chinese-remainder address map to prime axes](crt-prime-axes.md)
- [Matrix shears and triangular factorization](matrix-shear.md)
- [Recursion with a strict rank saving](rank-saving-recurrence.md)
- [Fast simultaneous butterfly layer](butterfly-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Phase twist from cyclic to negacyclic wrap](phase-twist.md)
- [Gaussian resampling with permutations retained](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancel.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We implement a binary row addition on corresponding selected bits in two address chunks." (paper)

  > We implement a binary row addition on corresponding selected bits in two address chunks. A third chunk supplies temporary address bits; its arbitrary initial value must be restored. The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses. The correction depends only on addresses, so the time bound is worst-case over all payloads.


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

Write the body to `exegenius/tasks/0027-write-packed-bit-addition.answer.md` and the JSON to `exegenius/tasks/0027-write-packed-bit-addition.answer.json`, then run `exegenius submit 0027-write-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0027-write-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
