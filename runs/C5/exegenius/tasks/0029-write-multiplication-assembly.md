# exegenius task 0029-write-multiplication-assembly

Project directory: `/home/user/openai-nlogn-wiki/runs/C5` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis, algorithm design basics (divide and conquer, recurrences, schoolbook and Karatsuba multiplication), discrete mathematics (modular arithmetic, primes, induction, permutations), and linear algebra and calculus at the usual first-course level. They know polynomials, complex numbers with roots of unity, and simple Turing machines with tapes. They have not studied the FFT in depth, Fourier analysis on groups, tensor products, numerical analysis, or fast integer multiplication research.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- The n log n conjecture and history
  - $n$ (input length): The number of bits of each multiplicand.
- Established O(n log n) multiplier
  - $n$ (input length): The number of bits of each multiplicand in the subroutine call.
- Discrete Fourier transform and roots of unity
- Convolution and the convolution theorem
- Multidimensional transforms
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial; a power of two.
- Synthetic polynomial transforms
- Phase twist to the negative-wrap ring
- Signed packing (Kronecker substitution)
- Fixed-point complex coefficients and exact recovery
- Array addresses, fields and tape layout
- Linear networks with restored auxiliary values
- Frames of a linear network
- Subset-intersection subspace labels
- Recursive power saving from s<Wm
- Address shear and triangular factorization
- Fast interchange of address fields
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (savings exponent): A fixed constant below 1 controlling the cost.
- Two-point butterfly H₀
  - $H_0$ (butterfly map): The map sending a pair to its half-sum and half-difference.
  - $u$ (first input): The first value of the pair.
  - $v$ (second input): The second value of the pair.
- Fast simultaneous butterfly layers
  - $V$ (stored bit volume): The number of stored bits in the arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which the same bit is selected.
  - $\lambda'$ (savings exponent): A fixed constant below 1 controlling the cost.
- Synthetic transforms with retained frequency order
- Resampling with permutations left in the transform
- Logarithms and iterated logarithm notation (also: lg, log base 2, log n, lg n)
- Floor, ceiling and rounding (also: floor, ceiling, nearest integer)
- Binary representation and bit operations (also: bits, binary expansion, XOR, bitwise exclusive or, bit fields)
- Radix (base-b) expansion (also: digits in base b, positional notation, radix digits)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, carry propagation)
- Divide and conquer recurrences (also: recurrence relations, master theorem, Karatsuba)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/NZ)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd, coprime)
- Permutations and bijections (also: rearrangement, one-to-one correspondence, bijective map)
- Vectors, matrices and linear maps (also: linear operator, invertible matrix, matrix inverse, linear combination, linear algebra)
- Subspaces, dimension and rank (also: linear subspace, span, rank of a matrix, basis)
- Vector spaces over GF(2) (also: binary vectors, F_2, bit vectors, mod 2 linear algebra)
- Triangular matrices and elimination (also: lower-triangular matrix, Gaussian elimination, LU factorization)
- Norms and triangle inequality (also: absolute value of complex number, modulus, magnitude, vector norm, error bound)
- Exponential function and Euler's formula (also: e^{i theta}, complex exponential, exp, Gaussian function)
- Fixed-point and finite-precision numbers (also: dyadic rationals, truncation, rounding error, binary fractions)
- Direct sum and product of index sets (also: Cartesian product, multi-index, array indexing, row-major order)
- Deterministic algorithms and upper/lower bounds (also: deterministic, worst-case time, upper bound, optimality)
- Induction and proofs by recursion (also: mathematical induction, recursive argument, inductive proof)
- Constants, exponents and power-of-two sizes (also: power of two, 2^k, padding to a power of two)

## This page

Concept: Assembling the exact product
Gloss: Chain: radix digits, CRT prime axes, Gaussian resampling and chirps, phase twist, ring convolution; then rescale, round and propagate carries; cost table summed.

## This page in the argument

The step: The exact product is recovered by the chain of reductions and its cost is $O(n(\lg n)^{1-\kappa})$.
How: Chain radix digits, CRT prime axes, resampling and chirps, phase twist, ring convolution, then rescale, round, carry and sum the cost table
Why: Each reduction changes the problem into one the fast tape procedures serve; a cost table then shows every term fits the bound. (the sources leave this for the reader to work out: spell it out)
Striking feature: Every term of the cost table has a power of p strictly below one, so one fixed exponent works. (explain why it holds, from the method)

Its sub-steps, in order:

- A Chinese-remainder address map places the digit list on distinct prime cyclic axes preserving convolution. (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md))
- A phase twist turns the last cyclic axis into a polynomial modulo $y^r+1$. (on [Phase twist to the negative-wrap ring](phase-twist.md))
- Bluestein chirps turn the middle transform into a convolution.
- The algorithm applies the address map, transforms, pointwise product, inverse transform, rescale, round and carries.
- With fixed-point arrays the final coefficient error is below $1/2$, so rounding recovers exact integers. (on [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md))
- Summing the cost table, all terms are $O(n(\lg n)^{1-\kappa})$.

It serves these steps, from the main result down:

- One fixed-tape Turing machine multiplies n-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Beat the $n\log n$ cost of transform-based multiplication by making the two tape operations (address rearrangement and butterfly layers) cost a power of their width less than a full scan, then plug them into the Harvey-van der Hoeven resampling reduction (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S8.3, S8.4, S8.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S8.3**: Bluestein chirps turn the middle transform into a convolution.
Source: "We next use the complex convolution to evaluate the middle factor" (paper)
> We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps. For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator at tensor address $j$ is computed modulo $2r$ as \[ -\sum_i s_i j_i^2(r/t_i)\pmod{2r}. \] All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$. Scan the stored axis descriptors and compute the $d$ squares and products with the previously established integer multiplier. Additions, reductions modulo a power of two, and restarting local counters cost $O(p)$ per term; multiplication costs $O(p\log p)=O(p^{1+\delta})$. Exponential evaluation then has the same $O(p^{1+\delta})$ bound. Thus chirp construction costs $O(Td p^{1+\delta})$ in total. In particular, this cost includes the scan of the axis descriptors at every coefficient.

**S8.4**: The algorithm applies the address map, transforms, pointwise product, inverse transform, rescale, round and carries.
Source: "Apply the coefficient-address map $\Phi$, with its padded layout, to obtain" (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ ex

**S8.6**: Summing the cost table, all terms are $O(n(\lg n)^{1-\kappa})$.
Source: "For the cost calculation put $V=Tp=\Theta(n)$." (paper)
> For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S8.1 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): A Chinese-remainder address map places the digit list on distinct prime cyclic axes preserving convolution.
- S8.2 (on [Phase twist to the negative-wrap ring](phase-twist.md)): A phase twist turns the last cyclic axis into a polynomial modulo $y^r+1$.
- S8.5 (on [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)): With fixed-point arrays the final coefficient error is below $1/2$, so rounding recovers exact integers.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md): A Chinese-remainder address map placing a coefficient list onto a product of distinct prime cyclic axes while preserving convolution.
  Shown as: Assembling the exact product *<predicate>* Chinese-remainder map to prime cyclic axes
- [Resampling with permutations left in the transform](retained-permutations.md): The source and target coordinate permutations stay inside the transform identity and cancel across forward, product and inverse transforms instead of being sorted separately.
  Shown as: Assembling the exact product *<predicate>* Resampling with permutations left in the transform
- [Phase twist to the negative-wrap ring](phase-twist.md): A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.
  Shown as: Assembling the exact product *<predicate>* Phase twist to the negative-wrap ring
- [Signed packing (Kronecker substitution)](signed-packing.md): Packing polynomial coefficients into a single integer with signs so ring products reduce to integer products done by the established multiplier.
  Shown as: Assembling the exact product *<predicate>* Signed packing (Kronecker substitution)
- [Synthetic transforms with retained frequency order](fast-synthetic-transform.md): Forward synthetic transforms keep the same frequency order through their pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.
  Shown as: Assembling the exact product *<predicate>* Synthetic transforms with retained frequency order
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md): Numerical arrays hold complex fixed-point dyadic numbers; errors are bounded below 1/2 so rounding recovers exact integer coefficients.
  Shown as: Assembling the exact product *<predicate>* Fixed-point complex coefficients and exact recovery

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n conjecture in this model.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y-r-plus-1.md)
- [Discrete Fourier transform and roots of unity](dft-roots-of-unity.md)
- [Convolution and the convolution theorem](cyclic-convolution.md)
- [Multidimensional transforms](multidimensional-transform.md)
- [Two-point butterfly H₀](butterfly-layer.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [The n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier](hh-multiplier.md)
- [Array addresses, fields and tape layout](address-fields-layout.md)
- [Linear networks with restored auxiliary values](linear-network.md)
- [Frames of a linear network](frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Subset-intersection subspace labels](subset-subspace-labels.md)
- [Recursive power saving from s<Wm](recursive-saving.md)
- [Fast interchange of address fields](fast-address-interchange.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "propagates carries to" (paper)

  > Finally, the source permutation retained during resampling cancels across the two forward source transforms, their pointwise product, and the opposite-sign transform. Section~\ref{sec:assembly} removes the known normalizations and digit scales, proves that the recovered coefficient error is strictly below $1/2$, and propagates carries to obtain the exact binary product. A compatible choice of rational parameters makes all terms in its cost table fit Theorem~\ref{thm:main}. Figure~\ref{fig:multiplication-flow} summarizes these reductions.

- "The source-transform procedures now supply the three transforms needed" (paper)

  > The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

- "Propagate radix-$2^b$ carries in increasing coefficient order." (paper)

  > exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the represented dyadic array by $\widetilde w$. \item Multiply the grid numerators of $\widetilde w$ exactly by $2^{2b+4}S$, again retaining the denominator $2^p$, and write each component in signed width $w_{\rm c}+4b+4$. Round the represented real values to the nearest integers. At each valid address, write the rounded coefficient in one signed $(3b+1)$-bit word, most significant bit first; at every padded address, write a zero word of that width. Supply this local payload width to $\Phi^{-1}$ and apply it, including removal of the address padding, to restore the ordinary coefficient order. \item Propagate radix-$2^b$ carries in increasing coefficient order. Write the resulting bits from least to most significant on a work tape, then reverse that stream and output exactly $2n$ bits in most-significant-first order. \end{enumerate}


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

Write the body to `exegenius/tasks/0029-write-multiplication-assembly.answer.md` and the JSON to `exegenius/tasks/0029-write-multiplication-assembly.answer.json`, then run `exegenius submit 0029-write-multiplication-assembly` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-multiplication-assembly`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
