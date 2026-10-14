# exegenius task 0009-write-gate-network-frames

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Binary integers
- Modular arithmetic
- Matrices, rank and linear maps
- Fixed-tape Turing machine model
- Arrays, address fields and logical volume
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Two-point butterfly H₀ and the kernel C
- Big-Theta, big-Omega and little-o notation (also: Theta, Omega, Θ, Ω, little-o, o(1), asymptotic notation)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, solving recurrences)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba, Toom-Cook, grade-school multiplication)
- Positional notation in any radix and mixed radix (also: radix-q digits, base-q representation, mixed-radix expansion, digit string, most significant digit)
- Bitwise operations, XOR and Hamming weight (also: XOR, exclusive or, addition mod 2, bit parity, wt, popcount, Hamming weight)
- Floor, ceiling and rounding (also: ⌊x⌋, ⌈x⌉, round to nearest integer, integer part)
- Exponential and logarithm functions (also: log base 2, lg, natural logarithm, ln, exp, e^x, Gaussian function)
- Convergent series and the geometric series (also: absolutely convergent sum, infinite sum, geometric series, tail bound, series convergence)
- Prime numbers, coprimality and trial division (also: relatively prime, pairwise coprime, gcd, odd prime, primality by trial division, unique factorization)
- Extended Euclidean algorithm (also: Euclid's algorithm, Bezout identity, computing modular inverses)
- Counting subsets and binomial coefficients (also: n choose k, binomial coefficient, k-subsets, inclusion-exclusion, ground set)
- Permutations and permutation matrices (also: bijection of indices, reordering of coordinates, involution, permutation of positions, partial permutation)
- Lexicographic order and Cartesian products of index sets (also: lexicographic order, product of ranges, multi-index, tuple addressing, row-major order)
- Vector norms, inner products and orthogonality (also: maximum norm, sup norm, infinity norm, triangle inequality, dot product, orthonormal basis, orthogonal complement, isometry)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, echelon form)
- Dyadic rationals and binary fractions (also: dyadic numbers, numbers m/2^k, binary point, fixed-point numbers, Gaussian dyadics, Gaussian integers)
- Stable radix sort and counting sort (also: bit sorting, stable sorting, radix sorting, sorting by a key digit)
- Mathematical induction (also: induction on k, proof by induction, recursive construction)

## This page

Concept: Role networks and frames
Gloss: A fixed linear network of wires (roles) and pointwise gates is run on arrays; assigning each vertex an invertible frame D_v makes the implemented operator D_out S D_in⁻¹, so only changes of frame along edges cost work.

## This page in the argument

The step: If every vertex of the network carries an invertible frame $D_v$ on its wire arrays, the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so only the changes of frame $D_vD_u^{-1}$ along edges cost work.
How: Keep each wire's array in the frame of its current vertex and observe that a pointwise linear gate commutes with a common frame.
Why: The intermediate frames cancel along each route, so they can be chosen freely to make each edge change cheap. (the sources say so: "intermediate frames can then be chosen to make each edge change inexpensive." (paper))

Its sub-steps, in order:

- On an edge from $u$ to $v$ the stored array is changed from $D_ug$ to $D_vg$ by applying $D_vD_u^{-1}$.
- A pointwise linear gate commutes with the common frame of its incidences, so the frame invariant passes through every gate to the sinks.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.; how: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs. (on [Integer multiplication below n log n](main-theorem.md))
- There are two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, that exchange two banks of values with prescribed signs, restore every scratch wire, and have total edge rank $s<Wm$.; how: Build a scalar exchange network from subset-intersection gates, attach nested nondegenerate subspaces to its gates so that an edge costs only its dimension change, and count the dimension changes.

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.2.1, S3.2.2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.2.1**: On an edge from $u$ to $v$ the stored array is changed from $D_ug$ to $D_vg$ by applying $D_vD_u^{-1}$.
Source: "On an edge from $u$ to $v$, apply $D_vD_u^{-1}$ to that wire's array." (paper)
> At each source, gate and sink $v$, assign an invertible $R$-linear operator $D_v$ on $R^\Omega$, called its \emph{frame}. A frame acts on the values indexed by addresses within one wire's array and may mix them; a gate instead combines wire values at each fixed address. All incoming and outgoing incidences of one gate use the same $D_v$. On an edge from $u$ to $v$, apply $D_vD_u^{-1}$ to that wire's array. Define the operators on all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c

**S3.2.2**: A pointwise linear gate commutes with the common frame of its incidences, so the frame invariant passes through every gate to the sinks.
Source: "Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks." (paper)
> all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Arrays, address fields and logical volume](array-layout.md): Data is stored as a stream in lexicographic address order over a product of fields; the logical volume V counts stored bits and rows are consecutive blocks over a suffix field.
  Shown as: Role networks and frames *<predicate>* Arrays, address fields and logical volume

## Pages that build on this one

- Subspace labels and the rank budget: Each gate and terminal of the network gets a nested nondegenerate subspace of an m-dimensional space, so an edge costs its dimension change, and the only decreasing edges are central wires, keeping the total below the wire count times m.
- Bit network as an address shear: Using projection matrices of the labels as frames, the XOR network turns the role exchange into the shear H ← H + D on every role, with total rational edge rank s_b < W_b m.
- Binary phase frames: For the complex network with binary labels, the frame C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} makes each edge change a product of one two-point kernel aI + bX_v per residual basis vector, and the whole network equals C^{⊗m} on every role.

## Other pages you may link to

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md)
- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Three-subset gather and scatter network](subset-intersection-network.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Subspace labels and the rank budget](subspace-labels.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
- [Binary phase frames](phase-interface.md)
- [Lower-triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width address interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional transforms and convolution on several axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Decimation-in-frequency butterflies and bit-reversed frequency order](butterfly-recursion.md)
- [Fixed-point complex arithmetic and truncation error](fixed-point-numerics.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on a padded box](tensor-resampling-box.md)
- [Choosing prime source lengths](prime-lengths.md)
- [Size parameters of the multiplication](size-parameters.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Phase twist from cyclic to negacyclic](coefficient-twist.md)
- [Source Fourier transform procedure](source-transform.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision and exact recovery](exact-recovery.md)
- [Cost table and the saving exponent κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$." (paper)

  > The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.

- "D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}." (paper)

  > w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.


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

Write the body to `exegenius/tasks/0009-write-gate-network-frames.answer.md` and the JSON to `exegenius/tasks/0009-write-gate-network-frames.answer.json`, then run `exegenius submit 0009-write-gate-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0009-write-gate-network-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
