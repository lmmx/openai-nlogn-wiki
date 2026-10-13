# exegenius task 0030-write-synthetic-transform-layout

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- Elementary stream operations on tape arrays
- Controlled shifts and rational scalings
- Convolution
- Discrete Fourier transform
- Radix-2 butterflies and FFT
- Subspaces, rank and orthogonal complements
- Fixed-point disk arithmetic and truncation error
- Established O(n log n) integer multiplier
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable, which satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing of polynomial products
- Two-point kernel C and phase frames
- Frames on pointwise linear networks
- Subset-intersection exchange network
- Subspace labels and the rank budget
- Recursive power saving from a rank deficit
- Bit network shear interface
- Lower triangular (Bruhat-type) factorization
- Cost of a rational matrix shear
- Power-width address interchange
- Fast chunk interchange
- Complex phase network
- Packed selected-bit addition
- Simultaneous butterfly layer
- Bluestein chirp identity
- Modular arithmetic and residue rings (also: congruence, Z/qZ, integers mod q, residue classes, modular inverse)
- Primes, coprimality and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, extended Euclidean algorithm, coprime)
- Positional (radix) number representation (also: base-b expansion, binary representation, digits, binary integers, mixed radix)
- Signed binary numbers and rounding (also: two's complement, sign-magnitude, floor, ceiling, rounding to nearest integer, truncation toward zero)
- Dyadic rationals (also: binary fractions, fractions with power-of-two denominator, fixed-point binary fractions)
- Bitwise operations and Hamming weight (also: XOR, exclusive or, bit string, popcount, Hamming weight, parity)
- Permutations and bijections (also: permutation of indices, bijection, inverse permutation, bit-reversal permutation, transposition)
- Lexicographic order and multi-index addressing (also: row-major order, dictionary order, multidimensional array indexing, mixed-radix address, tuple indices)
- Matrix algebra (also: matrix multiplication, matrix inverse, identity matrix, transpose, invertible matrix, 2x2 matrices, diagonal matrix, matrix-vector product)
- Vector norms and the triangle inequality (also: sup norm, max norm, infinity norm, absolute value bound, modulus bound, triangle inequality)
- Logarithms, exponentials and floor/ceiling in analysis (also: log base 2, lg, powers of two, exponent laws, iterated logarithm, real exponent)
- Theta, Omega and little-o notation (also: big-Theta, big-Omega, little-o, liminf, asymptotic lower bound, tight bound)
- Summations and geometric series (also: geometric sum, telescoping sum, sum of powers, series bound)
- Recurrence relations and divide and conquer (also: recurrence, unrolling a recurrence, master theorem, recursion tree, recursive algorithm, divide-and-conquer)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, Karatsuba, quadratic multiplication)
- Stacks and call stacks (also: stack, recursion stack, call stack, program counter, subroutine call)
- Pointwise operations on lists and vectors (also: componentwise product, Hadamard product, elementwise map, coordinatewise operation)
- Sets, subsets and counting (also: subset, cardinality, intersection, binomial coefficient, ground set, indicator vector, power set)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, contradiction, proof techniques)
- Euler's formula and complex exponentials (also: e^{i theta}, Euler formula, unit circle, phase factor, twiddle factor, modulus of e^{i theta})

## This page

Concept: Synthetic transform layout and cost
Gloss: Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.

## This page in the argument

The step: A forward synthetic transform of $M$ ring records, after a positional layout permutation $L$ of the record addresses, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and leaves the frequencies in bit-reversed order $B$, which the opposite transform consumes.
How: Move the selected bit slots of every axis to a prefix and permute $K$-bit chunks so that the bits used in each round sit at a common offset, so each of the $\ell$ rounds is one simultaneous butterfly layer.
Why: The simultaneous layer needs the active bits of all participating axes at the same offset in consecutive $K$-bit chunks, so the layout has to be built by chunk interchanges first. (the sources say so: "we must place the selected bits of the participating axes at a common" (paper))

Its sub-steps, in order:

- The forward procedure writes frequency $j$ into slot $\operatorname{rev}(j)$; the reverse procedure consumes that order, implementing $B_tF_t^-$ and $F_t^+B_t^{-1}$.
- Moving at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.
- At most $Dq-1$ exchanges of width-$K$ chunks put the chunks in round order, costing $O(Tp\cdot pK^{\tau-1})$.
- Process the rounds at named positions $h=\ell-1,\ldots,0$, each a simultaneous layer on all participating axes.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.; how: Reduce the product to a cyclic convolution of radix digits evaluated by Fourier-type transforms, make the two costly ingredients of those transforms (address rearrangement and butterfly arithmetic) cost a power of the logarithm less than a full scan per level by two rank-saving tape procedures, then assemble the algorithm, prove exactness and total the cost. (on [Sub-n log n integer multiplication](sub-nlogn-multiplication.md))
- Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays of $M$ ring records over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ has error below $\sqrt2\,M(3\ell+1)2^{-p}$ and costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$, using two forward synthetic transforms, pointwise ring products and the opposite transform.; how: Apply the convolution theorem in the ring: transform both operands, multiply pointwise with signed packing, and transform back, keeping the same frequency order throughout so that no permutation is executed. (on [Convolution from the retained transform layout](synthetic-convolution.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1.1, S4.1.2, S4.1.3, S4.1.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1.1**: The forward procedure writes frequency $j$ into slot $\operatorname{rev}(j)$; the reverse procedure consumes that order, implementing $B_tF_t^-$ and $F_t^+B_t^{-1}$.
Source: "procedures implement" (paper)
> The procedure consuming this stored order traverses the recursion in reverse: first process the two smaller branches, then apply the inverse monomial to the second branch, and finally apply $H_0$. Each forward level is invertible, since both its butterfly and its monomial are invertible. As $H_0^2=I/2$, the reversed level is half the inverse of the corresponding forward level. There are $a=\log_2t$ levels, so the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$. Lemma~\ref{lem:synthetic-characters} gives the same composite for $F_t^+B_t^{-1}$ with $B_tF_t^-$. The forward procedure is invertible, so these two reverse operators agree. Thus the two exact procedures implement \begin{equation} B_tF_t^-,\qquad F_t^+B_t^{-1}, \label{eq:stored-opposite} \end{equation} respectively.

**S4.1.2**: Moving at most $D(b+1)=O(dK)$ listed bit slots to a prefix costs $O(TpdK)$.
Source: "listed slots, so the moves cost $O(TpdK)$." (paper)
> long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and within each $h$ in increasing $i$; this second list is empty if $b=0$. Move each listed slot immediately after the prefix already formed, leaving all other slots in their relative order. There are at most $D(b+1)=O(dK)$ listed slots, so the moves cost $O(TpdK)$. A descriptor records the physical position of every named slot. The part of each axis left outside the prefix now consists of $q$ consecutive $K$-bit chunks.

**S4.1.3**: At most $Dq-1$ exchanges of width-$K$ chunks put the chunks in round order, costing $O(Tp\cdot pK^{\tau-1})$.
Source: "exchanges of width-$K$ address chunks, even when the chunks are" (paper)
> Number the axes by $i$ and their chunks, from high to low, by $j$. The remaining physical order changes from \[ (1,1),(1,2),\ldots,(1,q),(2,1),\ldots,(D,q) \quad\hbox{to}\quad (1,1),(2,1),\ldots,(D,1),(1,2),\ldots,(D,q). \] To obtain this order, scan its target positions from left to right. At each position except the last, exchange the chunk currently there with the required chunk if they differ. This uses at most $Dq-1$ exchanges of width-$K$ address chunks, even when the chunks are nonadjacent. Each costs $O(TpK^\tau)$, so all these exchanges cost \[ O\bigl(Tp\,DqK^\tau\bigr) =O\bigl(Tp\,pK^{\tau-1}\bigr). \] These prefix moves and chunk exchanges define $L$. We use the same letter for its induced record permutation: a record at address $x$ moves to address $Lx$, while its polynomial suffix stays intact. Recording the inverse operations in reverse order gives $L^{-1}$ with the same cost.

**S4.1.4**: Process the rounds at named positions $h=\ell-1,\ldots,0$, each a simultaneous layer on all participating axes.
Source: "First process the round at named position $h=\ell-1$ on the long" (paper)
> First process the round at named position $h=\ell-1$ on the long axes, if there are any. Every axis then has current recursive length $2^{\ell-1}$. Next process $h=\ell-2,\ldots,b$ in the $qK$ rounds on the remaining chunks, and finally the bottom positions $h=b-1,\ldots,0$, if $b>0$. Thus all participating axes in a common round have current length $u_i=2^{h+1}$. The branch bit written at position $h$ is frequency bit $a_i-1-h$; its frequency significance can differ between long and short axes. The descriptor locates that named slot after $L$, so the physical move has not changed which pair the current butterfly uses. The opposite procedure executes this schedule in reverse order and, when present, ends with the extra leading round on the long axes.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): A Fourier transform whose roots of unity are ω_t = y^{2r/t} in the ring modulo y^r + 1, so twiddles are signed shifts, computed by butterfly rounds with outputs left in bit-reversed order.
  Shown as: Synthetic transform layout and cost *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.
  Shown as: Synthetic transform layout and cost *<predicate>* Simultaneous butterfly layer
- [Fast chunk interchange](chunk-interchange.md): Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
  Shown as: Synthetic transform layout and cost *<predicate>* Fast chunk interchange

## Pages that build on this one

- Convolution from the retained transform layout: Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.

## Other pages you may link to

- [Convolution](convolution.md)
- [Recursive power saving from a rank deficit](recursive-power-saving.md)
- [Fixed-tape Turing machine model](fixed-tape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [Elementary stream operations on tape arrays](elementary-stream-ops.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, rank and orthogonal complements](linear-subspaces.md)
- [Frames on pointwise linear networks](frames-on-arrays.md)
- [Subset-intersection exchange network](exchange-network.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Bit network shear interface](bit-network-interface.md)
- [Lower triangular (Bruhat-type) factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Power-width address interchange](power-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](synthetic-ring.md)
- [Fixed-point disk arithmetic and truncation error](fixed-point-precision.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Discrete Fourier transform](dft.md)
- [Radix-2 butterflies and FFT](fft-butterfly.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Two-point kernel C and phase frames](phase-kernel-c.md)
- [Complex phase network](complex-phase-network.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Multidimensional resampling on a padded box](tensor-resampling.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Exact recovery of the integer product](exact-recovery.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Parameter choices](parameter-choices.md)
- [Coefficient twist to the negacyclic ring](convolution-twist.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Complete time bound](cost-accounting.md)
- [Sub-n log n integer multiplication](sub-nlogn-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "The procedure constructs an explicit positional
layout permutation $L$ of record addresses" (paper)

  > The procedure constructs an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and th

- "Transform layout and cost" (paper)

  > \begin{lemma}[Transform layout and cost] \label{lem:synthetic-transform-cost} Fix the rational parameters and positive comparison constants $a_d\leq b_d$, $a_r\leq b_r$ of Proposition~\ref{prop:simultaneous-layer}. Fix constants $C_\ell>0$ and $C_w>1$, and choose the layer constants once as \[ C_M=C_\ell+1,\qquad C_{\rm desc}=32(C_\ell+C_w+1). \] Use these constants and $C_w$ in Proposition~\ref{prop:simultaneous-layer}. These fixed choices determine a cutoff $p_1$, one fixed-tape procedure, and an implicit time constant with the following guarantee. For every choice of positive integers $p,d,r$ with $p\geq p_1$ and \[ a_dp^\epsilon\leq d\leq b_dp^\epsilon,\qquad 2^{a_rp/d}\leq r\leq2^{b_rp/d}, \] suppose $d\geq2$ and $r=2^\ell$ with an integer $2\leq\ell<p$, and require \[ d\ell\leq C_\ell p,\qquad 1\leq K=\lfloor d^c\rfloor\leq\ell-1. \] Let $t_i\in\{2^{\ell-1},2^\ell\}$ for $1\leq i\leq d-1$, put $M=\prod_{i=1}^{d-1}t_i$ and $T=rM$, and let $w$ be an integer with $p+2\leq w\leq C_wp$. The cutoff and time constant are independent of $p,d,r$, these axis choices, the round headers constructed from them, and $w$ within the displayed bounds.


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

Write the body to `exegenius/tasks/0030-write-synthetic-transform-layout.answer.md` and the JSON to `exegenius/tasks/0030-write-synthetic-transform-layout.answer.json`, then run `exegenius submit 0030-write-synthetic-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0030-write-synthetic-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
