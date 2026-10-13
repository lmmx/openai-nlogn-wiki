# exegenius task 0016-write-rank-saving

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

Concept: Rank saving of the finite networks
Gloss: The sum s of edge ranks is strictly less than the wire count W times the dimension m, so a recursive call on width m·f uses s calls on volume V/W each and the cost per volume grows by s/W < m, which gives the power saving.
Also called: recursive saving

## This page in the argument

The step: Fixed linear networks exist that exchange two banks of values with prescribed signs, restore every auxiliary wire, and have total edge rank $s$ strictly less than the wire count times $m$, namely $s<Wm$.
How: Build the bank exchange from three-element-subset gadgets, track the representation of each wire by a common frame, attach nested subspace labels so that every edge costs only its label-dimension change, and add up the ranks
Why: The power saving rests on the number of smaller operations on edges being strictly below the number of wires times the dimension, so the construction must be organised so that this rank count can be read off edge by edge. (the sources say so: "The saving will come from keeping the total dimension lost on decreasing" (paper))
Striking feature: The inequality $s<Wm$ holds with a relative deficit of only about $10^{-11}$, yet any strict gap gives an exponent below 1. (explain why it holds, from the method)

Its sub-steps, in order:

- Three stages of the subset gadgets, each adding $x_S$ to $y_S$ whatever the scratch wires hold, send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every scratch wire. (on [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md))
- Because every gate is pointwise and linear it commutes with a common frame $D_v$ on all of its wires, so the network on arrays realizes $D_{\rm out}\mathsf S D_{\rm in}^{-1}$ and only the endpoint frames matter. (on [Frames and the common-frame identity](frames.md))
- Giving each gate and terminal a nondegenerate subspace label, nested along every edge, makes each edge cost its label-dimension change; the only decreasing edges are the central-wire returns, so the total rank cost is $Wm-2N+2L$. (on [Nested subspace labels and orthogonal residuals](subspace-labels.md))
- With XOR gates and projections $P_U$ as frame matrices, the bit network permutes its roles, the endpoint matrices differ by the identity (a shear $H\leftarrow H+D$), and the sum of edge ranks is $s<Wm$. (on [Bit network and its rational matrix interface](bit-network-interface.md))
- The rank deficit is large enough for an explicit exponent: $s/W<m^\tau$ with $\tau=1-2^{-50}$.

It serves these steps, from the main result down:

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Give the multiplication algorithm and show its output is exact, then total its cost stage by stage (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The algorithm, with digits placed on prime axes by the Chinese-remainder map, transformed by Gaussian resampling, chirp convolution and polynomial-ring convolution, multiplied pointwise, transformed back, rescaled, rounded and carry-propagated, outputs the exact $2n$-bit product.; how: Reduce the product to a cyclic convolution of digit lists and evaluate it with Fourier transforms, building from the fastest inner primitive (convolution over a polynomial ring) outward through the resampling, prime-axis and twist reductions, then bound the error so that rounding is exact (on [The multiplication algorithm](multiplication-algorithm.md))
- The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of disk-grid arrays over $\mathcal R_r$ is computed with error below $\sqrt2\,M(3\ell+1)2^{-p}$ in $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}+\log(rp)])$ time.; how: Take two forward synthetic transforms, multiply pointwise in the retained order using signed packing, apply the opposite transform to that same order, and rescale by $M$ (on [Convolution from the retained transform layout](ring-convolution.md))
- A forward synthetic transform of $M$ polynomial records, with error below $\sqrt2\,\ell 2^{-p}$, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda\prime}])$ and leaves its output in a retained layout order that the opposite transform consumes.; how: Use address interchanges to put the selected bits of all axes at a common offset in consecutive $K$-bit chunks so that each of the $\ell$ rounds is one simultaneous butterfly layer, and add the movement, exchange and layer costs (on [Transform layout for parallel butterfly rounds](transform-layout.md))
- Two disjoint contiguous address fields of $u$ bits in an array of volume $V$ with product address set can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$, although intermediate steps form XOR combinations of data.; how: Realize the interchange as a shear computed by a recursive XOR circuit whose edge ranks sum to less than the wire count, first for power widths with enough rows, then for arbitrary widths by splitting the width in base m (on [Fast address-chunk interchange](address-interchange.md))
- For width $e=m^k$, two disjoint chunks of $e$ radix-$q$ digits (with enough rows before them) are interchanged in $O(Ve^\tau)$ time.; how: Recursion on the width: perform the shear with the finite bit network on its role streams, each edge being a rank-bounded shear on fields $m$ times narrower, and solve the resulting recurrence (on [Recursive power-width interchange](power-width-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1.1.1.1.1.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1.1.1.1.1.5**: The rank deficit is large enough for an explicit exponent: $s/W<m^\tau$ with $\tau=1-2^{-50}$.
Source: "\frac{s_{\rm b}}{W_{\rm b}}<m^\tau," (paper)
> The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1.1.1.1.1.1 (on [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)): Three stages of the subset gadgets, each adding $x_S$ to $y_S$ whatever the scratch wires hold, send $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restore every scratch wire.
- S1.1.1.1.1.1.2 (on [Frames and the common-frame identity](frames.md)): Because every gate is pointwise and linear it commutes with a common frame $D_v$ on all of its wires, so the network on arrays realizes $D_{\rm out}\mathsf S D_{\rm in}^{-1}$ and only the endpoint frames matter.
- S1.1.1.1.1.1.3 (on [Nested subspace labels and orthogonal residuals](subspace-labels.md)): Giving each gate and terminal a nondegenerate subspace label, nested along every edge, makes each edge cost its label-dimension change; the only decreasing edges are the central-wire returns, so the total rank cost is $Wm-2N+2L$.
- S1.1.1.1.1.1.4 (on [Bit network and its rational matrix interface](bit-network-interface.md)): With XOR gates and projections $P_U$ as frame matrices, the bit network permutes its roles, the endpoint matrices differ by the identity (a shear $H\leftarrow H+D$), and the sum of edge ranks is $s<Wm$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Bit network and its rational matrix interface](bit-network-interface.md): Using XOR gates and projections P_U as frame matrices, the bit network permutes its roles and the endpoint matrices differ by the identity, so the net effect on arrays is the shear H ← H + D.
  Shown as: Rank saving of the finite networks *<predicate>* Bit network and its rational matrix interface

## Pages that build on this one

- Recursive power-width interchange: For width e = m^k, a shear circuit built from the bit network turns one interchange of two e-digit chunks into s interchanges of width e/m on role streams of volume V/W, giving cost O(V e^τ).
- Simultaneous butterfly layer: The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ'}) instead of d passes.

## Other pages you may link to

- [Optimality conjecture for multiplication](nlogn-conjecture.md)
- [Cyclic convolution](convolution.md)
- [Disk-grid fixed-point arithmetic](fixed-point-disk.md)
- [Three-element subset gadgets](subset-gadgets.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier](nlogn-multiplier.md)
- [Array order and linear-time stream scans](stream-scans.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear bank-exchange network with restored scratch wires](bank-exchange-network.md)
- [Frames and the common-frame identity](frames.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
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

- "This strict inequality is the source of the power saving." (paper)

  > A recursive call at parameter $mf$ therefore uses $s$ calls at parameter $f$, each on a stream of volume $V/W$. The parameter counts field digits for address interchange and selected axes for a numerical layer. After dividing cost by volume, multiplying the parameter by $m$ increases the recursive contribution by $s/W<m$. This strict inequality is the source of the power saving. The later tape and arithmetic estimates preserve it, including the work of changing numerical address coordinates. Those changes are implemented by whole-chunk moves and controlled shifts, followed by a deterministic correction of the explicitly identified exceptional addresses.

- "number $s$ of smaller calls satisfies $s<Wm$" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.


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

Write the body to `exegenius/tasks/0016-write-rank-saving.answer.md` and the JSON to `exegenius/tasks/0016-write-rank-saving.answer.json`, then run `exegenius submit 0016-write-rank-saving` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0016-write-rank-saving`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
