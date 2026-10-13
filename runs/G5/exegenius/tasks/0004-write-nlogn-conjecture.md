# exegenius task 0004-write-nlogn-conjecture

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

Concept: Optimality conjecture for multiplication
Gloss: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine, which the paper refutes.
Also called: n log n conjecture

## Where the argument relies on this page

- One deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Pages that build on this one

- Established n log n multiplier: The Harvey–van der Hoeven O(N log N) multiplication algorithm for N-bit integers, used here only as an ordinary subroutine on short inputs.
- Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.

## Other pages you may link to

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

- "proposed $n\log n$ as the optimal order of growth" (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.

- "disproves the $n\log n$ optimality conjecture" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0004-write-nlogn-conjecture.answer.md` and the JSON to `exegenius/tasks/0004-write-nlogn-conjecture.answer.json`, then run `exegenius submit 0004-write-nlogn-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0004-write-nlogn-conjecture`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
