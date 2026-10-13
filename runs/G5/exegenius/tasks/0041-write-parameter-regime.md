# exegenius task 0041-write-parameter-regime

Project directory: `/home/user/openai-nlogn-wiki/runs/G5` (paths below are relative to it)

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

For these sources: The reader has a standard undergraduate computer science education: discrete mathematics (induction, sums, logarithms, floor and ceiling, functions and bijections, graphs and acyclic circuits), algorithms (divide and conquer, recurrences, sorting in O(n log n), grade-school multiplication and Karatsuba, Newton's method from calculus), and the basic theory of computation with Turing machines and tapes. They know complex numbers, roots of unity, polynomial arithmetic, modular arithmetic and elementary linear algebra, and have seen the FFT as an algorithm. They have not studied abstract algebra beyond modular arithmetic, number theory beyond gcd and inverses, numerical analysis of rounding errors, or any multiplication algorithm beyond the basic ones, so the wiki must explain the Fourier-transform machinery, the polynomial ring, the Harvey-van der Hoeven resampling and the linear-network constructions.

The reader already understands these concepts:

- Big-O notation
- Turing machines with tapes
- Polynomials
- Complex numbers
- Roots of unity
- Modular arithmetic
- Binary integers and XOR
- Basic linear algebra
- Fixed finite-tape Turing machine model
- Optimality conjecture for multiplication (also: n log n conjecture)
- Established n log n multiplier
- Array order and linear-time stream scans
- Controlled cyclic shifts and rational scalings
- Cyclic convolution
- Reducing integer multiplication to digit convolution
- Discrete Fourier transform and convolution theorem (also: Fourier transform, DFT)
- Radix-2 FFT butterflies (also: butterfly, decimation in frequency)
- Multidimensional transforms on power-of-two axes (also: tensor transform)
- Chinese-remainder map onto distinct prime axes (also: Chinese remainder address map)
- Gaussian resampling
- Bluestein chirp identity (also: Bluestein conversion, chirp)
- Resampling with retained permutations
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal variable of the polynomials, subject to the relation y^r = −1.
  - $r$ (record length): The number of complex coefficients in one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Retained frequency order of the transforms
- Phase twist to a negacyclic wrap
- Signed Kronecker packing of polynomial products
- Disk-grid fixed-point arithmetic (also: Gaussian dyadics, truncation Q_p)
- Three-element subset gadgets
- Linear bank-exchange network with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels and orthogonal residuals
- Bit network and its rational matrix interface
- Rank saving of the finite networks (also: recursive saving)
- Two-point phase kernel C
- Binary phase interface of the complex network
- Lower-triangular factorization of a matrix (also: Bruhat factorization)
- Rank-bounded matrix shear on address fields
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, arbitrary-width interchange)
- Packed selected-bit addition with repair
- Simultaneous butterfly layer (also: fast butterfly layer)
- Transform layout for parallel butterfly rounds
- Convolution from the retained transform layout
- Error analysis and exact recovery of the product
- Logarithms, floors and ceilings (also: lg n, log base 2, ceil, floor, rounding up, powers of two)
- Mathematical induction and recurrences (also: induction, recursion, recurrence relation, divide and conquer, recursive calls, master theorem)
- Sorting and permutation of arrays (also: merge sort, sorting in O(n log n), permutation, bijection, bit-reversal permutation)
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba algorithm, Karatsuba-Ofman, divide-and-conquer multiplication)
- Fast Fourier transform as an algorithm (also: FFT, Cooley-Tukey, fast polynomial multiplication, Schonhage-Strassen)
- Graphs, directed acyclic graphs and circuits (also: DAG, acyclic graph, network of gates, circuit, vertices and edges, wires and gates, graph)
- Calculus and Newton's method (also: Newton iteration, Newton's method, reciprocal and square root by iteration, geometric series, exponential and trigonometric functions, Euler's formula, e^{i theta})
- Vector norms and the triangle inequality (also: sup norm, maximum norm, infinity norm, triangle inequality, absolute value, error bound)
- Primes and trial division (also: prime number, primality testing, trial division, sieve of Eratosthenes, odd primes, coprime)
- Rounding, rational numbers and fixed-point numbers (also: round to nearest integer, truncation, dyadic rational, fixed point, finite precision, rounding error)
- Worst-case time analysis of deterministic algorithms (also: worst-case running time, deterministic algorithm, asymptotic through all input lengths, decision of constants and thresholds, finite lookup table)
- Sets, Cartesian products and indexed arrays (also: Cartesian product, product set, multi-index, tuple, array indexed by tuples, lexicographic order)

## This page

Concept: Parameter regime for input length n
Gloss: All sizes are tied to b = ⌈log₂ n⌉: precision p = 6b, d = ⌊b^ε⌋ axes, K = ⌊d^c⌋, padded size T about n/b, record length r = 2^{⌈log₂T/d⌉} so that Tp = Θ(n) and r grows faster than any power of p.

## This page in the argument

The step: All sizes are tied to $b=\lceil\log_2 n\rceil$: $p=6b$, $d=\lfloor b^\epsilon\rfloor$, $K=\lfloor d^c\rfloor$, a padded size $T$ in $[4n/b,8n/b)$ and $r=2^{\lceil\log_2 T/d\rceil}$, so that $Tp=\Theta(n)$ and $r$ exceeds every fixed power of $p$.
How: Fix the rational exponents, then derive every size from b and verify the comparison constants that the layer and transform interfaces need
Why: The interfaces proved earlier hold only inside bands of $d$ and $r$ relative to $p$, so one choice of sizes must put every pair $(d,r)$ inside them for all input lengths at once. (the sources do not say this: give the reader the reason)

Its sub-steps, in order:

- The exponents are fixed rationals, for example $\tau=1-2^{-50}$, $\lambda\prime=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, which satisfy every layer condition with room to spare.
- Put $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$, with $T$ and $r$ derived, so $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$ and $r=2^{\Theta(p^{1-\epsilon})}$.
- The band constants can be fixed for every input length at once, giving $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac{p}{12d}\le\ell\le\frac{p}{3d}$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Give the multiplication algorithm and show its output is exact, then total its cost stage by stage (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.; how: Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact (on [The multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.3.1, S1.3.2, S1.3.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.3.1**: The exponents are fixed rationals, for example $\tau=1-2^{-50}$, $\lambda\prime=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$, which satisfy every layer condition with room to spare.
Source: "Take the following fixed rational numbers:" (paper)
> The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.

**S1.3.2**: Put $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $K=\lfloor d^c\rfloor$, with $T$ and $r$ derived, so $Tp=\Theta(n)$, $d=\Theta(p^\epsilon)$ and $r=2^{\Theta(p^{1-\epsilon})}$.
Source: "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)
> After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

**S1.3.3**: The band constants can be fixed for every input length at once, giving $\frac1{12}p^\epsilon\le d\le p^\epsilon$ and $\frac{p}{12d}\le\ell\le\frac{p}{3d}$.
Source: "Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$" (paper)
> $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon\rfloor$ and $d\leq b$, they imply \[ \frac1{12}p^\epsilon\leq d\leq p^\epsilon, \qquad \frac{p}{12d}\leq\ell\leq\frac{p}{3d}. \] Thus we fix $a_d=a_r=1/12$, $b_d=1$, $b_r=1/3$, and $C_\ell=1$ in the layer and transform interfaces. Their pointwise bounds cover every computed pair $(d,r)$, including all choices arising at the same $p$. These bounds also give that $r$ exceeds every fixed power of $p$, $K/\log p\to\infty$, and $\ell/K\to\infty$. There are eventually enough axes for the $O(\log d)$ reserved row axes and enough bits for all work blocks.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Reducing integer multiplication to digit convolution](radix-digit-reduction.md): Writing each integer as a polynomial in 2^b with b-bit digits turns the product into a convolution of digit lists; padding avoids wraparound, and rounding plus carry propagation recover the bits.
  Shown as: Parameter regime for input length n *<predicate>* Reducing integer multiplication to digit convolution
- [Multidimensional transforms on power-of-two axes](multidimensional-transform.md): A transform over several axes is the tensor product of one-dimensional transforms, applied axis by axis to an array indexed by a product of axis lengths.
  Shown as: Parameter regime for input length n *<predicate>* Multidimensional transforms on power-of-two axes
- [Disk-grid fixed-point arithmetic](fixed-point-disk.md): Complex values in the unit disk stored as 2^{-p} times Gaussian-integer numerators in two's complement; layers are computed exactly in Gaussian dyadics with guard bits and then truncated toward zero by Q_p.
  Shown as: Parameter regime for input length n *<predicate>* Disk-grid fixed-point arithmetic

## Pages that build on this one

- Prime source lengths near powers of two: Distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by deterministic search, so S = ∏s_i lies in (T/2, T) and each ratio t_i/s_i leaves enough separation for Gaussian resampling.
- The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by resampling, chirp and polynomial-ring convolution, multiplied pointwise, transformed back with the opposite sign, rescaled, rounded and carry-propagated to give the 2n-bit product.
- Complete time bound and the power saving: Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).

## Other pages you may link to

- [Optimality conjecture for multiplication](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Three-element subset gadgets](subset-gadgets.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier](nlogn-multiplier.md)
- [Array order and linear-time stream scans](stream-scans.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Bit network and its rational matrix interface](bit-network-interface.md)
- [Rank saving of the finite networks](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Rank-bounded matrix shear on address fields](matrix-shear.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition with repair](packed-selected-bit-addition.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Phase twist to a negacyclic wrap](coefficient-twist.md)
- [Signed Kronecker packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform and convolution theorem](dft.md)
- [Radix-2 FFT butterflies](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point phase kernel C](two-point-kernel.md)
- [Binary phase interface of the complex network](phase-interface.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained frequency order of the transforms](stored-frequency-order.md)
- [Transform layout for parallel butterfly rounds](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Error analysis and exact recovery of the product](precision-recovery.md)
- [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md)
- [Prime source lengths near powers of two](prime-lengths.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and the power saving](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor," (paper)

  > After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $

- "Take the power of two $T$ in $[4n/b,8n/b)$" (paper)

  > After obtaining $n$, compute the size parameters below with the separate setup costs stated in this subsection. For sufficiently large $n$, put \[ b=\lceil\log_2n\rceil,\quad p=6b,\quad d=\lfloor b^\epsilon\rfloor, \quad K=\lfloor d^c\rfloor. \] Take the power of two $T$ in $[4n/b,8n/b)$, and let $r=2^{\lceil(\log_2T)/d\rceil}$ and $\ell=\log_2r$. Choose $d\ell-\log_2T$ of the $d$ axis lengths to be $r/2$ and the others to be $r$. This gives \[ t_i\in\{r/2,r\},\qquad \prod_i t_i=T,\qquad t_d=r. \] Indeed $d\ell-\log_2T$ is an integer in $[0,d)$, so at least one axis has length $r$; choose it as the last axis. These definitions give \begin{equation}\label{eq:sizes} Tp=\Theta(n),\quad d=\Theta(p^\epsilon),\quad K=\Theta(p^{\epsilon c}),\quad \ell=\Theta(p^{1-\epsilon}),\quad r=2^{\Theta(p^{1-\epsilon})}. \end{equation} The comparison constants can be fixed for every input length at once. For sufficiently large $b$, the bounds on $n,T$ give $b/2\leq\log_2T\leq b$. Since $p=6b$, $d=\lfloor b^\epsilon


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

Write the body to `exegenius/tasks/0041-write-parameter-regime.answer.md` and the JSON to `exegenius/tasks/0041-write-parameter-regime.answer.json`, then run `exegenius submit 0041-write-parameter-regime` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0041-write-parameter-regime`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
