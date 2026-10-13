# exegenius task 0022-write-multiplication-assembly

Project directory: `/home/user/openai-nlogn-wiki/runs/M2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, discrete mathematics with modular arithmetic and primes, introductory linear algebra and probability-free algorithm design (divide and conquer, sorting, recursion with recurrences), complex numbers and polynomials, and basic Turing machines with tapes. They have likely seen the idea of the FFT only in passing, if at all, and have not studied abstract algebra, harmonic analysis, numerical error analysis or the Harvey-van der Hoeven line of work.

The reader already understands these concepts:

- Big-O notation
- Multitape Turing machine
- Complex numbers and polynomials
- Convolution and multiplication by radix digits
- Discrete Fourier transform
- The n log n optimality conjecture and prior bounds
- Tape streams, array order and controlled shifts
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable of the polynomial ring, whose powers act as roots of unity.
  - $r$ (ring length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transforms
- Signed packing (Kronecker substitution)
- Normalized convolution over the polynomial ring with retained frequency order
- Bluestein chirp identity
- Gaussian resampling
- Multidimensional transform on power-of-two axes
- Chinese-remainder map to prime cyclic axes
- Linear exchange networks with frames and roles
- Three-subset networks with rank saving
- Recursive power saving
- Address interchange in time O(V u^τ)
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each of the two interchanged address fields.
  - $\tau$ (interchange exponent): A fixed constant less than 1 giving the power saving.
- Simultaneous butterfly layer in time O(V d^λ′)
  - $V$ (stored bit volume): The number of stored bits in the arrays.
  - $d$ (selected chunk count): The maximum number of equal-width address chunks whose selected bit is transformed together.
  - $\lambda'$ (layer exponent): A fixed constant less than 1 giving the power saving.
- Fixed-point precision and error control
- Euler's formula and roots of unity (also: e^{iθ}=cos θ+i sin θ, primitive roots of unity, complex exponential)
- Modular arithmetic and divisibility (also: congruences, residues mod m, gcd, coprime integers)
- Chinese remainder theorem (also: CRT)
- Prime numbers (also: primes, distinct primes, prime factorization)
- Binary representation and bit operations (also: bits, XOR, bit strings, two's complement, binary expansion)
- Radix-b representation of integers (also: base-b digits, positional notation, digit expansion)
- Schoolbook carry addition and multiplication (also: grade-school multiplication, carry propagation, long multiplication)
- Divide and conquer recurrences (also: master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Logarithms and exponentials (also: lg, log base 2, powers of two, iterated logarithm)
- Sums, products and summation manipulation (also: geometric series, sigma notation, index sets)
- Vectors, matrices and linear maps (also: linear algebra, matrix product, invertible matrix, basis, linear operator, vector space)
- Subspaces, dimension and rank (also: linear subspace, span, orthogonal complement, linear independence)
- Vector norms and the max norm (also: sup norm, infinity norm, triangle inequality, absolute value of complex number, modulus)
- Permutations and bijections (also: rearrangement, index permutation, one-to-one correspondence)
- Multidimensional arrays and index tuples (also: tensor indexing, array of arrays, Cartesian product of index sets, lexicographic order)
- Floating and fixed-point approximation and rounding (also: rounding to nearest integer, truncation, approximation error)
- Floor, ceiling and rounding functions (also: floor, ceiling, integer part)
- Real analysis basics: inequalities and exponential decay (also: Gaussian function, e^{-x^2}, tail bounds, sums of series)
- Dyadic rationals (also: dyadic numbers, binary fractions, numbers of form a/2^k)
- Cyclic and negacyclic indexing (also: indices mod q, wraparound, cyclic shift)
- Time complexity of sorting and merging on tapes (also: merge sort, sorting by passes, external sorting)

## This page

Concept: Assembly of the multiplication algorithm
Gloss: Chains digit convolution, CRT, Gaussian resampling, chirps, twist to the polynomial ring, rescaling, rounding and carry propagation, with parameters chosen so the cost table fits the theorem.

## This page in the argument

The step: Exact multiplication of $n$-bit integers reduces, by a chain of changes of representation with parameters chosen consistently, to ring convolution, and the total cost is $O(n(\lg n)^{1-\kappa})$.
How: chain reductions from the product to convolution over the polynomial ring, then recover the exact integer and sum the cost table
Why: Only the ring convolution can use the fast tape procedures, so the product must be turned into it exactly; each step changes the problem or representation and its error and cost must be accounted for. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficient lists. (on [Convolution and multiplication by radix digits](convolution.md))
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution. (on [Chinese-remainder map to prime cyclic axes](crt-map.md))
- Normalized convolution over $\mathbb C[y]/(y^r+1)$ is computed with two forward synthetic transforms, a pointwise product by packed integer products, and the opposite transform in the same frequency order. (on [Normalized convolution over the polynomial ring with retained frequency order](ring-convolution.md))
- Gaussian resampling expresses each prime-length Fourier transform through a power-of-two tensor transform, keeping the source and target permutations inside the formula. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity turns the middle transform into a cyclic convolution, which a twist moves to the polynomial ring. (on [Bluestein chirp identity](bluestein.md))
- Fixed-point errors accumulate through contractive maps and remain below $1/2$, so rounding recovers the integer coefficients. (on [Fixed-point precision and error control](fixed-point-precision.md))
- The cost table with the chosen rational parameters gives a total of $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: speed up the tape operations of the transform-based multiplication by a power of the logarithm, then assemble the multiplication (on [Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.7**: The cost table with the chosen rational parameters gives a total of $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.
Source: "The complete large-input bound is consequently" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Convolution and multiplication by radix digits](convolution.md)): Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficient lists.
- S2.2 (on [Chinese-remainder map to prime cyclic axes](crt-map.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- S2.3 (on [Normalized convolution over the polynomial ring with retained frequency order](ring-convolution.md)): Normalized convolution over $\mathbb C[y]/(y^r+1)$ is computed with two forward synthetic transforms, a pointwise product by packed integer products, and the opposite transform in the same frequency order.
- S2.4 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each prime-length Fourier transform through a power-of-two tensor transform, keeping the source and target permutations inside the formula.
- S2.5 (on [Bluestein chirp identity](bluestein.md)): Bluestein's chirp identity turns the middle transform into a cyclic convolution, which a twist moves to the polynomial ring.
- S2.6 (on [Fixed-point precision and error control](fixed-point-precision.md)): Fixed-point errors accumulate through contractive maps and remain below $1/2$, so rounding recovers the integer coefficients.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder map to prime cyclic axes](crt-map.md): Places the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
  Shown as: Assembly of the multiplication algorithm *<predicate>* Chinese-remainder map to prime cyclic axes
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven reduction expressing a Fourier transform on prime lengths via a power-of-two multidimensional transform, here keeping source and target permutations inside the transform formula.
  Shown as: Assembly of the multiplication algorithm *<predicate>* Gaussian resampling
- [Normalized convolution over the polynomial ring with retained frequency order](ring-convolution.md): Convolution computed by two forward synthetic transforms, a pointwise product via packed products, and the opposite transform, keeping the same frequency order throughout.
  Shown as: Assembly of the multiplication algorithm *<predicate>* Normalized convolution over the polynomial ring with retained frequency order
- [Fixed-point precision and error control](fixed-point-precision.md): Complex values stored on a 2^{-p} grid, with contractive maps, error accumulation and rounding so integer coefficients are recoverable.
  Shown as: Assembly of the multiplication algorithm *<predicate>* Fixed-point precision and error control
- [Address interchange in time O(V u^τ)](address-interchange.md): Interchanging two disjoint address fields of u bits via XOR combinations of intermediate streams, with exact final permutation.
  Shown as: Assembly of the multiplication algorithm *<predicate>* Address interchange in time O(V u^τ)

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine: A deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Other pages you may link to

- [Convolution and multiplication by radix digits](convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring.md)
- [Tape streams, array order and controlled shifts](tape-streams.md)
- [Linear exchange networks with frames and roles](linear-network-frames.md)
- [Three-subset networks with rank saving](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Simultaneous butterfly layer in time O(V d^λ′)](simultaneous-butterfly.md)
- [Discrete Fourier transform](dft.md)
- [The n log n optimality conjecture and prior bounds](nlogn-conjecture.md)
- [Multidimensional transform on power-of-two axes](tensor-transform.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Bluestein chirp identity](bluestein.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The remaining proof places these procedures inside the multiplication" (paper)

  > The remaining proof places these procedures inside the multiplication reduction and accounts for every change of representation. First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Section~\ref{sec:assembly} implements this map through triangular controlled shifts and charged axis moves. Gaussian resampling then expresses each source Fourier transform through a power-of-two tensor transform. Section~\ref{sec:resampling} retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.

- "Propagate radix-$2^b$ carries in increasing coefficient order." (paper)

  > exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}

- "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex


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

Write the body to `exegenius/tasks/0022-write-multiplication-assembly.answer.md` and the JSON to `exegenius/tasks/0022-write-multiplication-assembly.answer.json`, then run `exegenius submit 0022-write-multiplication-assembly` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0022-write-multiplication-assembly`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
