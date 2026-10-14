# exegenius task 0015-write-bit-network

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Theta, Omega), recursion and induction, discrete mathematics (sets, functions, permutations, graphs, modular arithmetic, primes and gcd, elementary combinatorics), and single-variable calculus. They have taken linear algebra at the level of vectors, matrices, bases, dimension and dot products, and have met complex numbers, polynomials, binary representation, Boolean gates and basic multitape Turing machines. They have not studied abstract algebra beyond residues and the two-element field, Fourier analysis, the FFT, fast integer multiplication, tensor products, or any research-level algorithms or complexity.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model
- The n log n optimality conjecture
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Arrays in lexicographic tape order with address fields
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Matrix rank, subspaces and orthogonal complements
- Linear exchange network with restored scratch wires
- Frames and the common-frame identity
- Three-element-subset subspace labels
- Rank deficit s < Wm
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Big-Theta, Big-Omega, Θ, Ω, o(1))
- Logarithms and exponentials (also: lg, log base 2, log n, log log n, powers of two, exponent laws)
- Floor, ceiling and rounding (also: floor function, ceiling function, round to nearest integer, truncation toward zero, integer part)
- Proof by induction and recursion (also: mathematical induction, recursive definition, recurrence relation, geometric series, divide and conquer)
- Sets, subsets and basic combinatorics (also: subset, intersection of sets, cardinality, binomial coefficient, counting, indicator vector, characteristic vector, pigeonhole)
- Functions, bijections and permutations (also: permutation, bijection, composition of functions, inverse function, permutation matrix, one-to-one correspondence)
- Graphs (also: vertices and edges, graph, neighbors, adjacency, directed edge, path in a graph)
- Modular arithmetic (also: residues, congruence, integers mod n, Z/nZ, mod q, remainder, cyclic group of residues)
- Primes, coprimality and gcd (also: prime number, relatively prime, coprime, greatest common divisor, Euclidean algorithm, modular inverse, Chinese remainder theorem, prime factorization)
- Binary field F2 and XOR (also: GF(2), F_2, exclusive or, XOR, mod 2 arithmetic, bitwise xor, parity)
- Positional number representation and carries (also: radix, base-b digits, binary representation, digit expansion, carry propagation, schoolbook multiplication, bit length, most significant digit)
- Dyadic rationals and binary fractions (also: dyadic numbers, binary fraction, fixed-point number, fixed-point arithmetic, scaling by a power of two, shift)
- Exponential function and Gaussian function (also: e^x, Euler's formula, Gaussian function, e^{-x^2}, bell curve, exponential decay, calculus bounds, Taylor series)
- Vectors, matrices and linear maps (also: matrix multiplication, invertible matrix, linear transformation, dot product, inner product, linear independence, basis, dimension, identity matrix, diagonal matrix, transpose, lower triangular matrix, linear combination)
- Vector norms and error bounds (also: norm, Euclidean norm, triangle inequality, operator norm, contraction, sup norm, absolute error, modulus of a complex number)
- Boolean gates and circuits (also: logic gate, wire, circuit, XOR gate, AND gate, fan-out, gate network)
- Determinism and exact versus approximate computation (also: deterministic algorithm, exact arithmetic, rational arithmetic, approximation error, worst-case running time, constant-factor overhead)

## This page

Concept: Bit exchange network with shear interface
Gloss: The F₂ network with rational labels whose frames are address shears: its endpoint operator is (H,D)→(H+D,D) on every role, using only XOR gates, with rank sum s_b < W_b m.

## This page in the argument

The step: A fixed network of $W_{\rm b}$ pointwise XOR gates exchanges two banks of values and restores every scratch wire, and nested rational labels give edge matrices whose ranks sum to $s_{\rm b}<W_{\rm b}m$ while the endpoint difference is $I_m$ on every role.
How: Attach nested rational subspaces (labels) to the gates and terminals of the scalar network, take their projections as address-shear frames, and count the rank of each edge difference.
Why: A frame change along an edge is cheap exactly when the labels at its ends are nested and differ in few dimensions, so the labels are chosen to make the dimension changes small. (the sources say so: "choose its intermediate labels to make the changes of frame inexpensive." (paper))
Striking feature: The endpoint operator is the same address shear $(H,D)\mapsto(H+D,D)$ on every one of the $W_{\rm b}$ roles, scratch roles included, although every edge applies a different frame change. (explain why it holds, from the method)

Its sub-steps, in order:

- For arbitrary initial scratch values, one forward invocation of the eight-row copy/gather/scatter/side-injection schedule changes $y_S$ to $y_S+x_S$ and nothing else; three stages then swap the two banks with signs and restore every scratch wire. (on [Linear exchange network with restored scratch wires](network.md))
- If every array on a wire is given an invertible frame at each vertex, with one common frame at all incidences of a gate, then the pointwise gate commutes with the frame and the network's overall effect is the endpoint frames applied to each role. (on [Frames and the common-frame identity](frames.md))
- Labels built from indicator vectors of three-element subsets, tensored three times, are nested along every edge of the network and the labels of neighboring gates are orthogonal. (on [Three-element-subset subspace labels](subset-labels.md))
- The labels' dimension changes along all edges sum to $Wm-2N+2L$ with total loss $L<N/2$, so the rational ranks of the edge differences sum to a total $s<Wm$. (on [Rank deficit s < Wm](rank-saving.md))
- The bit network's matrices obey $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$.
- The rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ falls short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$ (the $N$ negative source projections cost one extra rank each).

It serves these steps, from the main result down:

- There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a digit convolution computed with Fourier-type transforms on power-of-two axes, and accelerate the transforms' address rearrangements and butterfly layers by a power of the logarithm. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- There are two fixed-tape procedures whose cost beats a full scan per level by a power: an address-chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$.; how: Build each procedure from a fixed linear network that exchanges two banks of values and restores its scratch values, and apply it recursively with a strict rank deficit.
- Two disjoint address chunks of $u$ bits, with any prefix, gap and suffix, can be interchanged in $O(Vu^\tau)$ tape steps for a fixed $\tau<1$.; how: Move the top digits of both chunks into a row field, pad rows to a multiple of $W^k$, write the remaining width in base $m$ and apply the power-width interchange to each base-$m$ piece. (on [Fast interchange of address chunks](chunk-interchange.md))
- Two chunks of $e=m^k$ digits can be interchanged in $O(Ve^\tau)$ time by running a fixed exchange network of $W$ wires whose edges are smaller interchanges, with $s<Wm$ smaller calls in all.; how: Exchange the chunks with a shear $H\leftarrow H+D$ run through the bit network on $W$ role streams of volume $V/W$, implement each edge by smaller interchanges, and solve the recursion. (on [Power-width address interchange with rows](power-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (KEY.1.5, KEY.1.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**KEY.1.5**: The bit network's matrices obey $M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m$ for every input role $w$.
Source: "M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m" (paper)
> \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}

**KEY.1.6**: The rank sum $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$ falls short of $W_{\rm b}m$ by $N-2L_{\rm b}>0$ (the $N$ negative source projections cost one extra rank each).
Source: "Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$." (paper)
> \begin{proof} Lemma~\ref{lem:scalar-motifs} gives the scalar permutation, including all auxiliary roles. For $U\subset V$ nondegenerate, $P_V-P_U$ is the identity on $V\cap U^\perp$ and zero on its orthogonal complement. Its rank is $\dim V-\dim U$; reversing the edge negates the matrix without changing its rank. The only exceptions are the $N$ negative source projections. At stage 1, $B=0$, and the first gate on $X_a$ has label exactly $U_a$. Its first edge matrix is therefore $2P_{U_a}$, of rational rank one, where the corresponding dimension change was zero. Lemma~\ref{lem:motif-residuals} consequently gives the stated rank sum. Its deficit from $W_{\rm b}m$ is $N-2L_{\rm b}>0$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- KEY.1.1 (on [Linear exchange network with restored scratch wires](network.md)): For arbitrary initial scratch values, one forward invocation of the eight-row copy/gather/scatter/side-injection schedule changes $y_S$ to $y_S+x_S$ and nothing else; three stages then swap the two banks with signs and restore every scratch wire.
- KEY.1.2 (on [Frames and the common-frame identity](frames.md)): If every array on a wire is given an invertible frame at each vertex, with one common frame at all incidences of a gate, then the pointwise gate commutes with the frame and the network's overall effect is the endpoint frames applied to each role.
- KEY.1.3 (on [Three-element-subset subspace labels](subset-labels.md)): Labels built from indicator vectors of three-element subsets, tensored three times, are nested along every edge of the network and the labels of neighboring gates are orthogonal.
- KEY.1.4 (on [Rank deficit s < Wm](rank-saving.md)): The labels' dimension changes along all edges sum to $Wm-2N+2L$ with total loss $L<N/2$, so the rational ranks of the edge differences sum to a total $s<Wm$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Three-element-subset subspace labels](subset-labels.md): Subspaces of a tensor-cube bilinear space attached to gates, built from indicator vectors of three-element subsets with intersection-size pairings (Frankl–Wilson, Alon), so labels are nested along edges and neighbors are orthogonal.
  Shown as: Bit exchange network with shear interface *<predicate>* Three-element-subset subspace labels
- [Frames and the common-frame identity](frames.md): Giving each array on a wire an invertible address-space operator (a frame) at every vertex; because a common frame commutes with a pointwise linear gate, the network's overall effect is the endpoint frames applied to each role, and each edge only changes the frame.
  Shown as: Bit exchange network with shear interface *<predicate>* Frames and the common-frame identity
- [Rank deficit s < Wm](rank-saving.md): Summing the dimension changes (edge ranks) of all labels gives a total s of smaller calls strictly below W·m, where W is the number of wires and m the dimension, which is the source of the power saving.
  Shown as: Bit exchange network with shear interface *<predicate>* Rank deficit s < Wm

## Pages that build on this one

- Power-width address interchange with rows: Interchanges two chunks of m^k digits using the bit network: split rows among the W roles, apply a matrix shear on each edge via recursive smaller interchanges, merge, then compose three shears into a swap.

## Other pages you may link to

- [Fixed finite-tape machine model](fixed-tape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](nlogn-multiplier.md)
- [Arrays in lexicographic tape order with address fields](array-order.md)
- [Elementary stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrix rank, subspaces and orthogonal complements](matrix-basics.md)
- [Linear exchange network with restored scratch wires](network.md)
- [Lower-triangular factorization of matrices](lower-triangular.md)
- [Rational matrix shear as field interchanges](matrix-shear.md)
- [Power-saving recurrence](power-saving-recurrence.md)
- [Power-width address interchange with rows](power-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition with deterministic repair](packed-bit-addition.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Signed packing (Kronecker substitution)](kronecker-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](int-as-convolution.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 FFT order](butterfly-fft.md)
- [Complex phase network](phase-network.md)
- [Fixed-point disk grid and error propagation](fixed-point-disk-grid.md)
- [Coefficient twist to negacyclic ring](negacyclic-twist.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Convolution theorem for normalized transforms](convolution-theorem.md)
- [Multidimensional (tensor) transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Bluestein chirp identity](chirp-identity.md)
- [Source-permutation cancellation](permutation-cancellation.md)
- [Synthetic transform layout and stored frequency order](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Choice of prime source lengths](prime-lengths.md)
- [Complex cyclic convolution by coefficient twist](complex-convolution.md)
- [Source transform procedure](source-transform.md)
- [Rounding and carry propagation to the exact product](exact-recovery.md)
- [The multiplication algorithm](mult-algorithm.md)
- [Parameter choice and cost balance](parameter-balance.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates," (paper)

  > \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}


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

Write the body to `exegenius/tasks/0015-write-bit-network.answer.md` and the JSON to `exegenius/tasks/0015-write-bit-network.answer.json`, then run `exegenius submit 0015-write-bit-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-bit-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
