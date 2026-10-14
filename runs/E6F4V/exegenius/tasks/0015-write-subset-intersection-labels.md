# exegenius task 0015-write-subset-intersection-labels

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4V` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (modular arithmetic, primes and coprimality, the Chinese remainder theorem, permutations, induction, recurrences), calculus-level analysis (logarithms, floor and ceiling, norms and rounding errors), linear algebra (vectors, matrices, invertibility, rank, over the reals, complex numbers and F2), and algorithms (asymptotic notation, schoolbook multiplication, divide and conquer, sorting) with a first look at the FFT. They know basic multitape Turing machines and tapes, polynomials and complex numbers including roots of unity. They have not met Schoenhage-Strassen or Karatsuba-level multiplication algorithms in depth, ring and group-algebra language beyond polynomials, tensor products, numerical error analysis of fixed-point transforms, or any research literature on integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n conjecture for integer multiplication (also: n log n optimality conjecture, Schönhage–Strassen conjecture)
- Established n log n multiplier
- Arrays, addresses and volume on tapes (also: address field, logical volume)
- Elementary stream operations (also: split and merge, row splitting)
- Controlled cyclic shifts (also: controlled shifts, ordered affine streams)
- Rank, subspaces and orthogonal complements (also: nondegenerate subspace, orthogonal residual)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring, R_r)
  - $y$ (ring variable): The formal polynomial variable, whose powers y^a act as roots of unity of order 2r.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Linear exchange network with restored scratch wires (also: bank exchange, finite network, role)
- Frames on wire arrays (also: frame, common-frame identity)
- Address shear and lower-triangular factorization (also: Bruhat factorization, matrix shear)
- Fixed-point disk-grid arithmetic (also: disk grid, Gaussian dyadics, truncation Q_p)
- Logarithms and iterated logarithm notation (also: log, lg, log base 2, log2, powers of the logarithm, (lg n)^c)
- Big-Omega, Theta and little-o notation (also: Omega, Theta, Ω, Θ, little-o, asymptotic lower bound, tight bound)
- Binary representation and bit operations (also: binary strings, bits, XOR, exclusive or, bitwise operations, two's complement, Hamming weight, bit length)
- Modular arithmetic (also: congruence, residues mod m, Z/mZ, integers modulo m, centered residue, mod, wraparound)
- Primes, coprimality and gcd (also: prime numbers, pairwise coprime, relatively prime, greatest common divisor, gcd, Euclidean algorithm, prime number theorem, primes just below a number)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, Euler's formula, twiddle factor, ω)
- Vectors, matrices and invertibility (also: matrix multiplication, matrix inverse, invertible matrix, linear map, linear combination, lower-triangular matrix, permutation matrix, identity matrix, transpose, linear operator)
- Finite field F2 arithmetic (also: GF(2), binary field, mod 2 arithmetic, Z/2Z, F_2)
- Permutations and Cartesian products (also: bijection, permutation of indices, index set, product set, multi-index, coordinate permutation, lexicographic order, mixed-radix indexing, row-major order)
- Floor, ceiling and summation notation (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, sigma notation, geometric series, indicator vector)
- Recurrences and induction (also: recurrence relation, solving recurrences, unrolling a recurrence, proof by induction, master theorem, divide and conquer recurrence)
- Norms, absolute values and error bounds (also: max norm, sup norm, infinity norm, triangle inequality, modulus bound, rounding error, truncation error, round to nearest integer, unit disk)
- Fast Fourier transform and divide and conquer (also: FFT, Cooley-Tukey, fast Fourier transform, O(n log n) transform, convolution theorem, multiplying polynomials by FFT)
- Sorting and data movement on tapes (also: sorting, merge, scan, linear scan, stream, sequential access)
- Finite alphabet encodings and constant-factor simulation (also: alphabet, constant overhead, constant factor slowdown, encoding data as tape symbols, fixed finite state control, Turing machine simulation)
- Ring and group notions for polynomials (also: commutative ring, ring with identity, quotient ring, isomorphism, ring homomorphism, unit of a ring)

## This page

Concept: Subspace labels from three-element subsets
Gloss: Attaching nested nondegenerate subspaces of F^{⊗3} (spanned by indicator vectors of 3-element subsets, with ⟨t_S,t_T⟩ = |S∩T|−1) to gates and terminals so that gather/scatter coefficients depend on intersection size and unwanted ones are cancelled by side wires; the total rank change of all edges is less than Wm.
Also called: rank saving construction, orthogonal residual labels

## This page in the argument

The step: Nested nondegenerate subspaces of $F^{\otimes 3}$ can be attached to the gates and terminals so that the total rank change over all edges is less than $W m$.
How: label gates by tensor products of three-element-subset indicator lines, use their intersection-size inner products to make adjacent labels nested, and count dimension changes by telescoping
Why: The cost of an edge is the rank of its frame change, which equals the dimension gained or lost by its label; so the whole saving reduces to a counting problem on dimensions, which orthogonality of the subset indicators lets one solve with only the $I$ central-wire return edges decreasing. (the sources do not say this: give the reader the reason)
Striking feature: The total rank change is strictly less than the trivial count $W m$ for both networks, because the loss on decreasing edges is below half the number of data wires ($L/N=100/539$ and $101/539$). (explain why it holds, from the method)

Its sub-steps, in order:

- For indicator vectors $t_S,t_T$ of three-element subsets the form gives $\langle t_S,t_T\rangle=|S\cap T|-1$, so neighboring triples are orthogonal and unwanted gather/scatter coefficients can be cancelled by side wires.
- Source labels have total dimension $N$ and sink labels $Wm-N$, so the signed dimension changes over all edges sum to $Wm-2N$.
- The only decreasing edges are the central-wire edges between times 3 and 4, each losing dimension $h$, so the loss is $L=Ich$.
- The loss ratios $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are both below $1/2$.
- With the extra $N$ source ranks, the bit network has total edge rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$, and its matrices differ by $I_m$ between sink and source of every role.

It serves these steps, from the main result down:

- A single deterministic multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture.; how: reduce integer multiplication to convolution over a polynomial ring, and speed up the data movement and the butterfly layers of its transforms with two new tape procedures that each save a power of the logarithm (on [Integer multiplication below n log n](main-theorem.md))
- Two disjoint contiguous address fields of $u$ bits can be interchanged, $(p,h,g,d,z)\mapsto(p,d,g,h,z)$, in $O(V u^{\tau})$ time for a fixed $\tau<1$.; how: use the bit network, whose edges are address shears, to swap power-of-$m$ widths recursively, then remove the width and row-count restrictions (on [Fast address-chunk interchange](address-chunk-interchange.md))
- A fixed linear network whose total number $s$ of smaller calls is less than $W m$ gives a cost-per-volume recurrence with ratio $s/W<m$, hence a power-saving exponent $\tau<1$.; how: build a bank-exchanging network whose edge changes can be done by smaller instances of the same task, and bound the recursion by the total rank $s$ of the edge changes (on [Recursive rank saving](rank-saving-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (K3.1, K3.2, K3.3, K3.4, K3.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**K3.1**: For indicator vectors $t_S,t_T$ of three-element subsets the form gives $\langle t_S,t_T\rangle=|S\cap T|-1$, so neighboring triples are orthogonal and unwanted gather/scatter coefficients can be cancelled by side wires.
Source: "\langle t_S,t_T\rangle=|S\cap T|-1," (paper)
> For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.

**K3.2**: Source labels have total dimension $N$ and sink labels $Wm-N$, so the signed dimension changes over all edges sum to $Wm-2N$.
Source: "Thus the signed dimension changes will sum to $Wm-2N$, because the" (paper)
> The ambient label space is $\mathcal F=F^{\otimes3}$ with its tensor bilinear form. It has dimension $m$ and is nondegenerate. Write \[ u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3},\qquad U_a=\langle u_a\rangle. \] The prescribed terminal labels are \[ \begin{array}{c|cc} \text{role}&\text{source label}&\text{sink label}\\ \hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{each scratch role}&0&\mathcal F. \end{array} \] Write $W$ for the wire count in the construction under consideration. The source dimensions sum to $N$ and the sink dimensions to $Wm-N$. Thus the signed dimension changes will sum to $Wm-2N$, because the contributions at gates cancel. If decreasing edges lose a total dimension $L$, the sum of absolute changes is $Wm-2N+2L$. We will obtain $L<N/2$. The rational interface below will require an additional $N$ source ranks, so this inequality will leave a strict saving in both constructions.

**K3.3**: The only decreasing edges are the central-wire edges between times 3 and 4, each losing dimension $h$, so the loss is $L=Ich$.
Source: "edges are the central-wire edges from time 3 to time 4; their dimension" (paper)
> \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

**K3.4**: The loss ratios $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are both below $1/2$.
Source: "In particular, both are smaller than $1/2$." (paper)
> The loss ratios have the exact values \[ \frac{L_{\rm b}}{N}=\frac{100}{539},\qquad \frac{L_{\rm c}}{N}=\frac{101}{539}. \] In particular, both are smaller than $1/2$. We now turn the dimension count into the two interfaces needed later.

**K3.5**: With the extra $N$ source ranks, the bit network has total edge rank $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}<W_{\rm b}m$, and its matrices differ by $I_m$ between sink and source of every role.
Source: "=177176569088785861287000000<W_{\rm b}m." (paper)
> \begin{proposition}\label{prop:bit-motif-interface} The bit network has $W_{\rm b}$ wires, uses only pointwise XOR gates, and sends its input vector to the permutation $\rho$ of that vector. Its rational matrices are common to all incidences of a gate and obey \[ M_{\mathrm{sink}(\rho(w))}-M_{\mathrm{source}(w)}=I_m \quad\text{for every input role }w. \] The sum of the rational ranks of all edge differences is \begin{align} s_{\rm b} &=\sum_{e}\operatorname{rank}_{\mathbb Q} (M_{\mathrm{head}(e)}-M_{\mathrm{tail}(e)})\\ &=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m. \end{align} \end{proposition}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear exchange network with restored scratch wires](linear-network.md): A fixed network of linear gates on wires (each with a role) that, for arbitrary initial scratch values, exchanges two banks of values with prescribed signs and restores every scratch wire; run in eight rows of copy, gather, scatter and side-injection steps.
  Shown as: Subspace labels from three-element subsets *<predicate>* Linear exchange network with restored scratch wires
- [Frames on wire arrays](common-frame-principle.md): Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.
  Shown as: Subspace labels from three-element subsets *<predicate>* Frames on wire arrays
- [Rank, subspaces and orthogonal complements](linear-algebra-basics.md): Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.
  Shown as: Subspace labels from three-element subsets *<predicate>* Rank, subspaces and orthogonal complements

## Pages that build on this one

- Recursive rank saving: Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.
- Phase frames and the two-point kernel C: The complex version of the network uses frames built from Hamming-weight phases i^{wt(x) mod 4}; each edge change factors into two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), so a simultaneous C-layer on e=mf axes needs s smaller layers on f axes, and H₀^{⊗D} = b^D S_D C^{⊗D} S_D.

## Other pages you may link to

- [The n log n conjecture for integer multiplication](integer-multiplication-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod.md)
- [Fixed-point disk-grid arithmetic](fixed-point-truncation.md)
- [Established n log n multiplier](established-multiplier.md)
- [Arrays, addresses and volume on tapes](tape-address-model.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled cyclic shifts](controlled-shift.md)
- [Address shear and lower-triangular factorization](address-shear.md)
- [Recursive rank saving](rank-saving-recurrence.md)
- [Fast address-chunk interchange](address-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Signed packing of polynomial products](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Integer product as digit convolution](radix-digit-convolution.md)
- [Coefficient (phase) twist](phase-twist.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Multidimensional (tensor) transform](multidimensional-dft.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Phase frames and the two-point kernel C](phase-frame-kernel.md)
- [Fast simultaneous butterfly layer](fast-butterfly-layer.md)
- [Convolution over the polynomial ring](ring-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutations and their cancellation](permutation-cancellation.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choices and prime source lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving κ](time-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "three-element subsets: gather and scatter create coefficients depending" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "A label is a nondegenerate subspace of a fixed bilinear space." (paper)

  > The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive. A label is a nondegenerate subspace of a fixed bilinear space. On every edge one label will contain the other. For such an edge, the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one; its dimension is the absolute change in label dimension. The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.

- "\langle t_S,t_T\rangle=|S\cap T|-1," (paper)

  > For the bit network, let $F=\mathbb Q^h$ with bilinear form \[ \langle x,y\rangle=x^{\mathsf T}(I-J/9)y, \] where $J$ is the all-one matrix. This form has eigenvalues $1$ and $1-h/9=-91/9$, so it is nondegenerate. For a triple $T$ let $t_T$ be its indicator vector. Then \[ \langle t_S,t_T\rangle=|S\cap T|-1, \qquad \langle t_T,t_T\rangle=2. \] For the complex network, take instead $F=\mathbb F_2^h$ with the ordinary dot product; here $t_T\cdot t_T=1$. Thus every triple line is nondegenerate, and neighboring triple lines are orthogonal, in the label field belonging to either construction. The scalar domain need not equal the label field. These degree-one intersection formulas specialize the construction described by Alon~\cite[Section~3, remark after Theorem~1.1]{Alon1998} to the prime $2$, with the ground-set size changed to $h=100$.


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

Write the body to `exegenius/tasks/0015-write-subset-intersection-labels.answer.md` and the JSON to `exegenius/tasks/0015-write-subset-intersection-labels.answer.json`, then run `exegenius submit 0015-write-subset-intersection-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0015-write-subset-intersection-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
