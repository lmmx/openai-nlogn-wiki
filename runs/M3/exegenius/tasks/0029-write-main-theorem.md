# exegenius task 0029-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/M3` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis and recurrences, algorithm design (divide and conquer, the classical FFT idea), basic Turing machine complexity, discrete mathematics (binary and positional number systems, modular arithmetic, prime numbers, subsets), and the linear algebra and calculus that such a degree includes (vector spaces, subspaces, rank, matrices, inverse, real exponentials and logarithms). The reader has not studied algebraic structures beyond the basics, number theory beyond elementary modular arithmetic, numerical error analysis, or the research literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Convolution and cyclic convolution
- Fourier transform and roots of unity
- The n log n conjecture and history of multiplication
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity.
  - $r$ (coefficient count): The number of coefficients of a polynomial in the ring, a power of two.
- Synthetic polynomial transforms
- Two-point butterfly H₀
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Last-coordinate phase twist
- Signed packing (Kronecker substitution)
- Elementary stream operations and controlled shifts
- Linear networks with roles and restored auxiliaries
- Frames and endpoint operators
- Finite networks with nested subspaces and rank saving
- Recursive power saving
- Fast interchange of address chunks
  - $V$ (stored bit volume): The number of stored bits in the array.
  - $u$ (field width): The number of bits in each address field being interchanged.
  - $\tau$ (savings exponent): A fixed constant strictly less than 1.
- Simultaneous fast butterfly layers
  - $V$ (stored bit volume): The number of stored bits in the arrays.
  - $d$ (chunk count): The number of equal-width address chunks in which one bit position is selected.
  - $\lambda'$ (savings exponent): A fixed constant strictly less than 1.
- Gaussian dyadics and fixed-point precision
- Synthetic transforms on the retained layout
- Normalized convolution over the polynomial ring
- Precision, rounding and carry propagation
- Lower triangular (Bruhat) factorization
- Binary representation of integers (also: binary expansion, bits, most significant bit, bit strings)
- Positional radix and digit expansion (also: base-b digits, radix digits, carries)
- Logarithms and floor/ceiling (also: lg, log base 2, ceiling, floor)
- Modular arithmetic and congruences (also: remainder, mod, residues, cyclic indices)
- Prime numbers and coprimality (also: distinct primes, pairwise coprime, gcd)
- Matrices and linear maps (also: linear operator, matrix inverse, invertible matrix, matrix product, diagonal matrix, GL)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, rank of a matrix, linear combination, direct sum)
- Permutations and permutation matrices (also: partial permutation, bijection of indices, rearrangement)
- Cartesian products and multidimensional arrays (also: tensor array, product of index sets, multi-index)
- Divide and conquer recurrences (also: recursion, recursive calls, master theorem)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, fast convolution)
- Absolute value, norms and error bounds (also: sup norm, max norm, rounding error, truncation, triangle inequality)
- Dyadic rationals and fixed-point numbers (also: binary fixed point, power-of-two denominators)
- XOR and bitwise operations (also: exclusive or, bit flip, bitwise sum mod 2)
- Finite sets and subset operations (also: intersection, union, support, indicator)
- Euler's formula and unit circle (also: e^{2 pi i/N}, primitive root of unity, complex conjugate, modulus)
- Worst-case running time and Turing machine step counting (also: time complexity, T(n), linear time, DTIME)
- Gaussian elimination and triangular matrices (also: lower triangular matrix, row operations, shear)

## This page

Concept: Integer multiplication in O(n (lg n)^(1-κ)) time
Gloss: Deterministic fixed-tape machine multiplying n-bit integers in O(n(lg n)^(1-κ)) with κ=2^-182, disproving the n log n optimality conjecture in this model.
Heading: Multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} giving the power saving.
- $\lg n$ (binary logarithm): The maximum of the ceiling of log base 2 of n and 1.

## This page in the argument

The step: A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, with $p$ bits of working precision, $d$ transform axes of length about $r$.
How: Reduce the product to a convolution through a chain of representation changes, evaluate it with the two fast tape procedures, then recover the exact product and sum the costs
Why: Multiplication is a convolution of digits, convolution is computed by transforms, and the cost of transforms is dominated by address movement and butterflies, so a power saving in those two procedures gives a power saving in the whole product. (the sources say so: "Scanning an array of $\Theta(n)$ stored bits at each of" (paper))

Its sub-steps, in order:

- Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. (on [Reduction of integer product to digit convolution](radix-reduction.md))
- Two tape procedures, the address interchange and the simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed $\tau,\lambda'<1$ on stored bit volume $V$.
- Convolution over the ring $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with cost small enough to be dominated by the fast layers and interchanges.
- Prime-length Fourier transforms on the source axes reduce to power-of-two $d$-axis transforms of precision $p$ followed by a normalized cyclic convolution.
- The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md))
- A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, and its negative wrap gives the original cyclic wrap after untwisting. (on [Last-coordinate phase twist](phase-twist.md))
- The multiplication algorithm reads digits, applies the address map, three transforms, exact scalings, rounding and carries.
- Removing known normalizations leaves coefficient error strictly below $1/2$, so rounding and carry propagation give the exact binary product. (on [Precision, rounding and carry propagation](exact-recovery.md))
- With the fixed rational parameters every cost-table term is at most $p^{1-2\kappa}$, and the total time is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S2, S3, S4, S7, S9). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2**: Two tape procedures, the address interchange and the simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed $\tau,\lambda'<1$ on stored bit volume $V$.
How: Obtain both procedures from fixed linear networks with a strict rank saving and recurse

**S3**: Convolution over the ring $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with cost small enough to be dominated by the fast layers and interchanges.
How: Use synthetic polynomial transforms on a retained layout, with pointwise ring products by signed packing

**S4**: Prime-length Fourier transforms on the source axes reduce to power-of-two $d$-axis transforms of precision $p$ followed by a normalized cyclic convolution.
How: Gaussian resampling with the source and target permutations kept inside the transform, then Bluestein's chirp identity on the middle transform

**S7**: The multiplication algorithm reads digits, applies the address map, three transforms, exact scalings, rounding and carries.
Source: "The source-transform procedures now supply the three transforms needed" (paper)
> The source-transform procedures now supply the three transforms needed for the radix-digit convolution. Read each stored operand backward from its least significant end in groups of $b$ bits. This produces the radix-$2^b$ digits $a_0,\ldots,a_{q-1}$ in increasing coefficient order. Buffer each group on a fixed work tape and read it back most significant bit first, reversing its least-significant-first input order; pad the final short group with leading zeroes. For digit $a_j$, write the exact grid numerator $a_j2^{p-b-2}$ in a signed $w_{\rm c}$-bit real word, followed by a zero $w_{\rm c}$-bit imaginary word. This exponent is nonnegative because $p=6b$, and the represented value is exactly $a_j2^{-b-2}$. Append $S-q$ zero coefficient records. Buffering and ordering the groups costs $O(n)$, including the one partial group's padding, and writing the $S$ records costs $O(Sp)$. Together with the initial count and copies, this input conversion costs $O(n+Sp)=O(Tp)$; all $n$ input bits, including leading zeroes, are retained before the final group is padded.

**S9**: With the fixed rational parameters every cost-table term is at most $p^{1-2\kappa}$, and the total time is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.
Source: "$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Reduction of integer product to digit convolution](radix-reduction.md)): Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.
- S5 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- S6 (on [Last-coordinate phase twist](phase-twist.md)): A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, and its negative wrap gives the original cyclic wrap after untwisting.
- S8 (on [Precision, rounding and carry propagation](exact-recovery.md)): Removing known normalizations leaves coefficient error strictly below $1/2$, so rounding and carry propagation give the exact binary product.
- S2.1 (on [Fast interchange of address chunks](address-interchange.md)): Two disjoint contiguous address fields of $u$ bits in a Cartesian-product array of volume $V$ can be interchanged in time $O(Vu^\tau)$ for a fixed $\tau<1$.
- S2.2 (on [Simultaneous fast butterfly layers](fast-butterfly-layer.md)): Simultaneous normalized butterfly layers applying $H_0$ at the same bit position in each of at most $d$ address chunks cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, with coefficient error less than $\sqrt2\,2^{-p}$.
- S3.1 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Synthetic characters cancel, so the forward and opposite synthetic transforms invert each other up to a scale, $F_t^+F_t^-=t^{-1}I$.
- S3.2 (on [Synthetic transforms on the retained layout](transform-layout.md)): On a retained layout parallel butterfly layers and address interchanges compute a $d$-axis synthetic transform at the stated cost and keep the frequency order through the pointwise product.
- S3.3 (on [Signed packing (Kronecker substitution)](signed-packing.md)): Polynomial products in the ring of $r$ complex coefficients are computed exactly by signed packing (Kronecker substitution) and the ordinary $O(n\log n)$ multiplier, in time $O(rp\log(rp))$.
- S3.4 (on [Normalized convolution over the polynomial ring](normalized-convolution.md)): Convolution on the remaining axes over the ring uses two forward transforms, pointwise polynomial products and the opposite transform on the retained layout.
- S4.1 (on [Gaussian resampling](gaussian-resampling.md)): Each prime-length transform is expressed through a power-of-two tensor transform by contractions, with source and target permutations retained in the transform identity.
- S4.2 (on [Bluestein chirp identity](bluestein-chirp.md)): Bluestein's chirp identity turns the middle transform, with its target permutation, into a normalized cyclic convolution.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fourier transform and roots of unity](dft-roots-of-unity.md)
- [Polynomial ring modulo y^r + 1](poly-ring-yr1.md)
- [Convolution and cyclic convolution](convolution.md)
- [Gaussian dyadics and fixed-point precision](complex-fixed-point.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Normalized convolution over the polynomial ring](normalized-convolution.md)
- [Reduction of integer product to digit convolution](radix-reduction.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Precision, rounding and carry propagation](exact-recovery.md): Remove known normalizations and digit scales, show coefficient error is below 1/2, round and propagate carries to the exact binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* Precision, rounding and carry propagation
- [The n log n conjecture and history of multiplication](nlogn-conjecture.md): Schönhage and Strassen's 1971 O(n log n log log n) bound and conjecture that n log n is optimal; Harvey and van der Hoeven reached O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^(1-κ)) time *<predicate>* The n log n conjecture and history of multiplication

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-reduction.md)
- [Polynomial ring modulo y^r + 1](poly-ring-yr1.md)
- [Gaussian dyadics and fixed-point precision](complex-fixed-point.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Fourier transform and roots of unity](dft-roots-of-unity.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Two-point butterfly H₀](butterfly.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Elementary stream operations and controlled shifts](stream-operations.md)
- [Linear networks with roles and restored auxiliaries](linear-network.md)
- [Frames and endpoint operators](frames.md)
- [Finite networks with nested subspaces and rank saving](finite-network-subspaces.md)
- [Recursive power saving](recursive-saving.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Simultaneous fast butterfly layers](fast-butterfly-layer.md)
- [Synthetic transforms on the retained layout](transform-layout.md)
- [Normalized convolution over the polynomial ring](normalized-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "computes this exact product for every $n\ge1$ and every pair of $n$-bit" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "Its worst-case running time satisfies" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "These constants are deliberately conservative; no optimization is claimed." (paper)

  > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

- "For the cost calculation put $V=Tp=\Theta(n)$." (paper)

  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}


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

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
