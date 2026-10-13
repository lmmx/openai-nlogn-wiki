# exegenius task 0021-write-packed-selected-bit-addition

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
- Disk-grid fixed-point arithmetic (also: Gaussian dyadics, truncation Q_p)
- Three-element subset gadgets
- Linear bank-exchange network with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels and orthogonal residuals
- Bit network and its rational matrix interface
- Rank saving of the finite networks (also: recursive saving)
- Lower-triangular factorization of a matrix (also: Bruhat factorization)
- Rank-bounded matrix shear on address fields
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, arbitrary-width interchange)
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

Concept: Packed selected-bit addition with repair
Gloss: XORing one selected bit position of f chunks into another chunk is done by a few cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small set of addresses where guard values fail.

## This page in the argument

The step: XORing the selected bit of $f$ chunks of one range into another range, with a third chunk restored to its arbitrary initial value, costs $O(V(L^\tau+1))$ in the family of parameters used.
How: Use a constant number of cyclic shifts of whole chunk ranges that are correct away from an explicit small exceptional set, then repair that set by sorting
Why: The shifts are cheap whole-range moves but wrong on some addresses; since the wrong addresses depend only on the addresses, they can be listed and fixed in worst-case time whatever the payload. (the sources say so: "The correction depends only on addresses, so the time bound is" (paper))

Its sub-steps, in order:

- The selected-bit rotations by cyclic shifts of whole chunk ranges give the required XORs except at a small explicit set of addresses.
- The exceptional addresses are extracted, given destination keys, stably radix sorted and reinserted, which repairs them deterministically.
- The movement costs $O(V(L^\tau+1))$ and the repair adds only a small fraction because the bad fraction is at most $80(f-1)2^{-K}$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Give the multiplication algorithm and show its output is exact, then total its cost stage by stage (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.; how: Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact (on [The multiplication algorithm](multiplication-algorithm.md))
- The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time.; how: Take two forward synthetic transforms, multiply pointwise in the retained order using signed packing, apply the opposite transform to that same order, and rescale by $M$ (on [Convolution from the retained transform layout](ring-convolution.md))
- A forward synthetic transform of $M$ polynomial records, with error below $\sqrt2\,\ell 2^{-p}$, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}])$ and leaves its output in a retained layout order that the opposite transform consumes.; how: Use address interchanges to put the selected bits of all axes at a common offset in consecutive $K$-bit chunks so that each of the $\ell$ rounds is one simultaneous butterfly layer, and add the movement, exchange and layer costs (on [Transform layout for parallel butterfly rounds](transform-layout.md))
- The butterfly $H_0$ applied at once to the same bit position of $D\le d$ address chunks of polynomial-record arrays, followed by one truncation, costs $O(Vd^{\lambda\prime})$ for a fixed $\lambda\prime<1$ instead of $D$ passes.; how: Compute the equivalent tensor power of the two-point kernel with the complex phase network, by the same recursion as the address interchange, performing its binary changes of basis by packed XORs, then convert back to the normalized butterfly and truncate once (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.1.2.4.1, S1.1.1.2.4.2, S1.1.1.2.4.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.1.2.4.1**: The selected-bit rotations by cyclic shifts of whole chunk ranges give the required XORs except at a small explicit set of addresses.
Source: "We first construct eight rotations that have the required effect away" (paper)
> \begin{proof} We first construct eight rotations that have the required effect away from a small set of addresses. We then correct exactly that set. For a Boolean control $c$ and arbitrary integers $u,w$, perform the following eight operations in the displayed chronological order. Every predicate uses the current values of the integers. \begin{equation} \label{eq:eight-packed-additions} \begin{array}{rcl@{\qquad}l} u&\leftarrow&u-c[\,w\equiv0\pmod2\,],&(1)\\ w&\leftarrow&w-c[\,u\equiv0\pmod2\,],&(2)\\ u&\leftarrow&u+c[\,w\equiv0\pmod2\,],&(3)\\ w&\leftarrow&w+c[\,u\equiv0\pmod2\,],&(4)\\ w&\leftarrow&w+c[\,u\equiv1\pmod2\,],&(5)\\ u&\leftarrow&u+c[\,w\equiv1\pmod2\,],&(6)\\ w&\leftarrow&w-c[\,u\equiv1\pmod2\,],&(7)\\ u&\leftarrow&u-c[\,w\equiv1\pmod2\,].&(8) \end{array} \end{equation} If

**S1.1.1.2.4.2**: The exceptional addresses are extracted, given destination keys, stably radix sorted and reinserted, which repairs them deterministically.
Source: "To implement the correction, scan the stream with a record-rank counter." (paper)
> To implement the correction, scan the stream with a record-rank counter. All chunk names are back in their original positions. Dividing the current rank through the fixed seven field lengths recovers the three chunk values and their mixed-radix record strides. The strides exclude the $R$ payload bits. All involved integers have $O(A_{\rm rect})$ bits, so schoolbook arithmetic, descriptor copying, and resets take at most $O(A_{\rm rect}^3)$ per record. Test membership in $\mathcal B$ and extract just those records. For a current exceptional address $q$, compute $q'=T_0(S_0^{-1}(q))$ by reversing the eight modular additions with negated offsets, then applying the selected XORs directly. Each reversed mask uses the current controls of that reversed line. There are at most $f\le L\le A_{\rm rect}$ selected positions, so this calculation also fits $O(A_{\rm rect}^3)$ time.

**S1.1.1.2.4.3**: The movement costs $O(V(L^\tau+1))$ and the repair adds only a small fraction because the bad fraction is at most $80(f-1)2^{-K}$.
Source: "The movement costs $O(V(L^\tau+1))$." (paper)
> The movement costs $O(V(L^\tau+1))$. A fixed number of full record scans costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty. The initial descriptor has a fixed number of canonical integers of $O(A_{\rm rect})$ bits, so its preparation is covered by $O(MA_{\rm rect}^3)$. All counters, positioning, rewinds, and cleanup are included. Equation~\eqref{eq:packed-bad-fraction} proves \eqref{eq:packed-rectangle-time} on a fixed number of tapes. After division by $V=MR$, its additional terms are bounded by $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under the stated family bounds the first tends to zero, and the second is $O(p^2 2^{-K}(1+A_{\rm rect}/R))=o(1)$. This proves the final assertion. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Fast address-chunk interchange](address-interchange.md): Exchanging two disjoint contiguous address fields of u bits in an array with product address set costs O(V u^τ) for a fixed τ < 1, although intermediate steps form XOR combinations of data.
  Shown as: Packed selected-bit addition with repair *<predicate>* Fast address-chunk interchange
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md): A target address field can be rotated by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time.
  Shown as: Packed selected-bit addition with repair *<predicate>* Controlled cyclic shifts and rational scalings

## Pages that build on this one

- Simultaneous butterfly layer: The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ'}) instead of d passes.

## Other pages you may link to

- [Optimality conjecture for multiplication](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Disk-grid fixed-point arithmetic](fixed-point-disk.md)
- [Three-element subset gadgets](subset-gadgets.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier](nlogn-multiplier.md)
- [Array order and linear-time stream scans](stream-scans.md)
- [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Bit network and its rational matrix interface](bit-network-interface.md)
- [Rank saving of the finite networks](rank-saving.md)
- [Lower-triangular factorization of a matrix](matrix-factorization.md)
- [Rank-bounded matrix shear on address fields](matrix-shear.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Phase twist to a negacyclic wrap](coefficient-twist.md)
- [Signed Kronecker packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform and convolution theorem](dft.md)
- [Radix-2 FFT butterflies](fft-butterfly.md)
- [Multidimensional transforms on power-of-two axes](multidimensional-transform.md)
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
- [Reducing integer multiplication to digit convolution](radix-digit-reduction.md)
- [Error analysis and exact recovery of the product](precision-recovery.md)
- [Chinese-remainder map onto distinct prime axes](crt-prime-axes.md)
- [Parameter regime for input length n](parameter-regime.md)
- [Prime source lengths near powers of two](prime-lengths.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound and the power saving](time-bound.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We implement a binary row addition on corresponding selected bits in two address chunks." (paper)

  > We implement a binary row addition on corresponding selected bits in two address chunks. A third chunk supplies temporary address bits; its arbitrary initial value must be restored. The construction first uses a constant number of cyclic shifts of whole chunk ranges, then corrects an explicitly bounded set of addresses. The correction depends only on addresses, so the time bound is worst-case over all payloads.

- "y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i}" (paper)

  > <K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions $j_i=\rho+iK$, numbered from the least significant bit, one fixed multitape procedure performs \[ y_{j_i}\longleftarrow y_{j_i}\mathbin\oplus x_{j_i} \quad(0\le i<f). \] It preserves the spectator coordinates, all other chunk bits, and every record payload; in particular, it restores the entire chunk $z$ for every initial value. With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is \begin{equation} \label{eq:packed-rectangle-time} O\!\left(V(L^\tau+1)+MA_{\rm rect}^3+ \delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})\right). \end{equation} When $A_{\rm rect}=O(p)$, $R$ exceeds every fixed polynomial in $p$, $f\le d\le p$, and $K/\log p\to\infty$, this is $O(V(L^\tau+1))$, uniformly over the permitted lengths and payloads in the fixed family. \end{lemma}


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

Write the body to `exegenius/tasks/0021-write-packed-selected-bit-addition.answer.md` and the JSON to `exegenius/tasks/0021-write-packed-selected-bit-addition.answer.json`, then run `exegenius submit 0021-write-packed-selected-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0021-write-packed-selected-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
