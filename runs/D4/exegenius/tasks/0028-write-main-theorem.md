# exegenius task 0028-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/D4` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, algorithms (divide and conquer, recurrences, FFT-style ideas at a basic level), discrete mathematics (sets, binomial coefficients, binary representation, modular arithmetic, primes), and linear algebra (vector spaces, subspaces, rank, matrix products, Gaussian elimination, orthogonal projections, over the rationals and basic finite fields). They know complex numbers and polynomials, and basic Turing machines. They have not studied advanced algebra (Bruhat decomposition, general rings and quotients in depth), number theory beyond basics, numerical error analysis of FFTs, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- Fixed-tape machine model and stream scans
- Convolution and the discrete Fourier transform
- Integer multiplication as digit convolution
- History and the n log n conjecture
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable whose powers serve as roots of unity.
  - $r$ (ring degree): The power-of-two number of coefficients of a ring element, with y^r equal to −1.
- Synthetic polynomial transforms
- Two-point butterfly
- Gaussian resampling
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp conversion
- Coefficient twist to the negative wrap
- Signed packing (Kronecker substitution)
- Exact normalized polynomial products
- Fixed-point complex coefficients and exact dyadics
- Linear networks with frames and restored auxiliaries
- Finite network from three-element subsets
- Recursive power saving
- Address shear and triangular factorization
- Fast interchange of address chunks
- Simultaneous fast butterfly layers
- Synthetic transform layout with retained frequency order
- Retained permutations cancelling
- Rounding, rescaling and carry propagation
- The assembled multiplication algorithm
- Binary representation of integers (also: bits, base-2 expansion, binary digits, bit string)
- Hamming weight (also: wt, popcount, number of ones)
- Bitwise XOR (also: exclusive or, addition mod 2, xor)
- Modular arithmetic (also: residues, congruence, integers mod m, residue ring)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd)
- Linear algebra over the rationals (also: vector spaces, subspaces, dimension, matrix rank, rational rank, linear maps, orthogonal projection, orthogonal complement)
- Gaussian elimination and the general linear group over F2 (also: row reduction, GL(m,F_2), invertible binary matrices, elementary row operations, triangular factorization)
- Binomial coefficients and basic counting (also: n choose k, subsets, combinations, inclusion-exclusion)
- Recurrences and divide and conquer (also: recursion, recursive calls, master theorem, recursion tree)
- Exponentials, logarithms and iterated logarithm bounds (also: lg, log base 2, exp, powers of logarithms)
- Matrix and block notation (also: diagonal matrix, block matrix, identity matrix, transpose, Kronecker product, tensor product)
- Roots of unity and Euler's formula (also: primitive root of unity, e^{2 pi i/N}, complex exponential)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, radix-2 FFT)
- Sorting and permutations (also: permutation of indices, bit reversal, rearranging records)
- Basic real error bounds (also: rounding, floor and ceiling, triangle inequality, absolute error, fixed-point arithmetic)
- Schoolbook integer multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication, radix)

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed-tape Turing machine multiplies n-bit integers in O(n (lg n)^(1−κ)) time with κ=2^(−182), disproving the n log n optimality conjecture in this model.

## This page in the argument

The step: A deterministic fixed-tape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in this model.
How: reduce multiplication to a ring convolution whose transforms are accelerated by two fast tape procedures, then account for the cost
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels costs $\Theta(n\log n)$, so beating it needs savings in both data movement and arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving is a genuine power $(\lg n)^{-\kappa}$ of the logarithm, with an astronomically small $\kappa=2^{-182}$, rather than a $\log\log$ or $\log^*$ factor. (explain why it holds, from the method)

Its sub-steps, in order:

- Schönhage and Strassen gave $O(n\log n\log\log n)$ and proposed $n\log n$ as optimal; Harvey and van der Hoeven reached $O(n\log n)$. (on [History and the n log n conjecture](nlogn-conjecture.md))
- The machine model has one fixed finite alphabet and a fixed finite number of one-dimensional tapes; moving one digit in a fixed radix takes a bounded number of scans, but interchanging fields with growing numbers of digits does not. (on [Fixed-tape machine model and stream scans](fixed-tape-model.md))
- Two tape procedures, fast address interchange and simultaneous fast butterfly layers, cut the cost of address rearrangement and of transform layers by a power of the logarithm.
- The product of two $n$-bit integers is computed exactly by the pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery. (on [The assembled multiplication algorithm](multiplication-algorithm.md))
- With a compatible choice of rational parameters every term of the cost table fits the bound $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Two tape procedures, fast address interchange and simultaneous fast butterfly layers, cut the cost of address rearrangement and of transform layers by a power of the logarithm.
How: derive both from a fixed linear network with a strict deficit in the number of smaller calls and recurse

**S3**: With a compatible choice of rational parameters every term of the cost table fits the bound $O(n(\lg n)^{1-\kappa})$.
Source: "$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely" (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S0.1 (on [History and the n log n conjecture](nlogn-conjecture.md)): Schönhage and Strassen gave $O(n\log n\log\log n)$ and proposed $n\log n$ as optimal; Harvey and van der Hoeven reached $O(n\log n)$.
- S0.2 (on [Fixed-tape machine model and stream scans](fixed-tape-model.md)): The machine model has one fixed finite alphabet and a fixed finite number of one-dimensional tapes; moving one digit in a fixed radix takes a bounded number of scans, but interchanging fields with growing numbers of digits does not.
- S2 (on [The assembled multiplication algorithm](multiplication-algorithm.md)): The product of two $n$-bit integers is computed exactly by the pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.
- S1.1 (on [Linear networks with frames and restored auxiliaries](linear-network-frames.md)): A fixed linear network exchanges two banks of values with signs, frames $D_v$ change representation along edges so that intermediate frames cancel, and auxiliary values are restored.
- S1.3 (on [Finite network from three-element subsets](subset-network.md)): A finite network with nested subspaces of an $m$-dimensional space attached to its gates, built from three-element subset intersection counts, has total number $s$ of smaller calls with $s<Wm$.
- S1.4 (on [Recursive power saving](recursive-saving.md)): Applying the network at parameter $mf$ uses $s$ calls at parameter $f$ on streams of volume $V/W$, and $s<Wm$ makes the cost per unit volume grow like a power of the parameter below 1.
- S1.2 (on [Address shear and triangular factorization](address-shear.md)): For the bit procedure the endpoint operator is the address shear $(H,D)\mapsto(H+D,D)$ over a residue ring, implemented through lower-triangular factorization.
- S1.5 (on [Fast interchange of address chunks](fast-address-interchange.md)): Two disjoint contiguous address fields of $u$ bits in an array with a complete Cartesian product of addresses can be interchanged in time $O(Vu^{\tau})$ for a fixed $\tau<1$, ending as an exact permutation.
- S1.6 (on [Simultaneous fast butterfly layers](fast-butterfly-layers.md)): The butterfly $H_0$ can be applied simultaneously on the same bit position in at most $d$ address chunks at cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-tape machine model and stream scans](fixed-tape-model.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The assembled multiplication algorithm](multiplication-algorithm.md): Pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.
  Shown as: Integer multiplication below n log n *<predicate>* The assembled multiplication algorithm
- [History and the n log n conjecture](nlogn-conjecture.md): Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
  Shown as: Integer multiplication below n log n *<predicate>* History and the n log n conjecture

## Other pages you may link to

- [Convolution and the discrete Fourier transform](convolution-dft.md)
- [Integer multiplication as digit convolution](mult-to-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Fixed-point complex coefficients and exact dyadics](fixed-point-dyadics.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Coefficient twist to the negative wrap](phase-twist.md)
- [Rounding, rescaling and carry propagation](exact-recovery.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Fixed-tape machine model and stream scans](fixed-tape-model.md)
- [Linear networks with frames and restored auxiliaries](linear-network-frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Finite network from three-element subsets](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Fast interchange of address chunks](fast-address-interchange.md)
- [Simultaneous fast butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Synthetic transform layout with retained frequency order](transform-layout.md)
- [Retained permutations cancelling](permutation-cancellation.md)
- [Exact normalized polynomial products](polynomial-products.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers
in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "\kappa=2^{-182}" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "Chunk exchanges for transform layout" (paper)

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

Write the body to `exegenius/tasks/0028-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0028-write-main-theorem.answer.json`, then run `exegenius submit 0028-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
