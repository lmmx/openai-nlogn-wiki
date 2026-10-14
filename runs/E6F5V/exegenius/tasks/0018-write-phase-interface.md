# exegenius task 0018-write-phase-interface

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
- Elementary stream operations
- Controlled cyclic shifts and rational scalings
- Established O(n log n) integer multiplier
- The n log n optimality conjecture
- Role networks and frames
- Restoring arbitrary scratch values
- Three-subset gather and scatter network
- Nondegenerate subspaces and orthogonal residuals
- Subspace labels and the rank budget
- Rank saving and the power-saving recurrence
- Bit network as an address shear
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

Concept: Binary phase frames
Gloss: For the complex network with binary labels, the frame C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} makes each edge change a product of one two-point kernel aI + bX_v per residual basis vector, and the whole network equals C^{⊗m} on every role.

## This page in the argument

The step: With binary labels and the phase frame $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)})H^{\otimes m}$, every edge changes by a product of two-point kernels $aI+bX_v$, one per residual basis vector, and the whole complex network equals $C^{\otimes m}$ on every role, with total edge rank $s<Wm$.
How: Use Hamming weight modulo 4 as a phase, which is additive over orthogonal pieces, so that each unit-norm residual vector contributes a Gaussian combination of the identity and a translation.
Why: Weight is additive modulo four over orthogonal binary vectors and each residual vector has odd weight, so its phase $i^{\pm[v\cdot x]}$ is exactly a combination $aI+bX_v$ of the identity and a translation, the kernel the butterfly needs. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- If $z\cdot w=0$ the weight of $z+w$ is additive modulo four, so the phase difference of an edge is a sum over an orthonormal basis of its residual.
- Each residual vector gives the kernel $aI+bX_v$ or its inverse, so an edge is a product of two-point kernels.
- The number of kernels over the network is $s=Wm-2N+2L<Wm$, since the deficit $2N-2L$ is positive.
- After source and sink diagonal corrections and undoing the bank exchange, every role, including every scratch role, carries the tensor product $C^{\otimes m}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.; how: Reduce the product to a convolution evaluated through Gaussian-resampled, chirped synthetic transforms, make the two costly tape operations (address movement and butterfly layers) cheaper by a power of the logarithm using networks with a rank saving, and then assemble the algorithm and add up its costs. (on [Integer multiplication below n log n](main-theorem.md))
- There are two fixed linear networks, a bit network over $\mathbb F_2$ and a complex network over $\mathbb Z[i,1/2]$, that exchange two banks of values with prescribed signs, restore every scratch wire, and have total edge rank $s<Wm$.; how: Build a scalar exchange network from subset-intersection gates, attach nested nondegenerate subspaces to its gates so that an edge costs only its dimension change, and count the dimension changes.

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.5.1, S3.5.2, S3.5.3, S3.5.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.5.1**: If $z\cdot w=0$ the weight of $z+w$ is additive modulo four, so the phase difference of an edge is a sum over an orthonormal basis of its residual.
Source: "If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four." (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S3.5.2**: Each residual vector gives the kernel $aI+bX_v$ or its inverse, so an edge is a product of two-point kernels.
Source: "The displayed phase therefore becomes $aI+bX_v$ or its inverse." (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S3.5.3**: The number of kernels over the network is $s=Wm-2N+2L<Wm$, since the deficit $2N-2L$ is positive.
Source: "The deficit is $2N-2L_{\rm c}>0$." (paper)
> \begin{proof} For binary vectors $z,w$, \[ \operatorname{wt}(z+w) =\operatorname{wt}(z)+\operatorname{wt}(w) -2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|. \] If $z\cdot w=0$, the intersection cardinality is even, so weight is additive modulo four. If $V=U\mathbin{\perp}E$ and $\mathcal B$ is an orthonormal basis of $E$, it follows that \[ q_V(x)-q_U(x)=\sum_{v\in\mathcal B} \operatorname{wt}(v)[v\cdot x]\pmod4. \] For a decreasing edge the right side is negated. Each $v$ has norm one, so $\operatorname{wt}(v)$ is odd. Its coefficient in the phase, including the sign for the edge direction, is therefore some $\varepsilon\in\{1,-1\}$ modulo four. The function $i^{\varepsilon[v\cdot x]}$ equals \[ \frac{1+i^\varepsilon}{2} +\frac{1-i^\varepsilon}{2}(-1)^{v\cdot x}. \] The identity $H\operatorname{diag}(1,-1)H=X$, tensored over the coordinates in $\operatorname{supp}(v)$, sends the diagonal character $(-1)^{v\cdot x}$ to translation $X_v$. The displayed phase therefore becomes $aI+bX_v$ or its inverse. The nonzero residuals have such bases by Lemma~\ref{lem:motif-residuals}; for a zero residual use the empty basis. The same lemma gives the count $s_{\rm c}$. The deficit is $2N-2L_{\rm c}>0$.

**S3.5.4**: After source and sink diagonal corrections and undoing the bank exchange, every role, including every scratch role, carries the tensor product $C^{\otimes m}$.
Source: "Every role, including every scratch role, now has the required forward tensor product." (paper)
> lsewhere. Put $Z=\operatorname{diag}(1,-1)$. Direct multiplication gives \[ C=iZC^{-1}Z,\qquad C^{-1}=-iZCZ. \] For $k$ columns, let $Z_{a,k}$ be the tensor product of $Z$ on those 27 coordinates in every column and the identity elsewhere. Apply $Z_{a,k}$ before the network at $X_a$, and apply $i^{27k}Z_{a,k}$ after the network at $Y_a$; the latter scalar is applied once to the whole role. There are $27k$ inverse factors, so the identity $C=iZC^{-1}Z$ turns each of them into $C$. The operator on this pair is therefore $C^{\otimes mk}$ as well. Only the physical $X$ outputs still carry the minus sign of the scalar exchange. Negate those outputs and send output role $\rho(w)$ back to role $w$. Every role, including every scratch role, now has the required forward tensor product. \end{proof}

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Two-point butterfly H₀ and the kernel C](two-point-butterfly.md): The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and its Gaussian dyadic relative C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, C² = X and H₀ = b S C S, which lets H₀ layers be computed from C layers.
  Shown as: Binary phase frames *<predicate>* Two-point butterfly H₀ and the kernel C
- [Subspace labels and the rank budget](subspace-labels.md): Each gate and terminal of the network gets a nested nondegenerate subspace of an m-dimensional space, so an edge costs its dimension change, and the only decreasing edges are central wires, keeping the total below the wire count times m.
  Shown as: Binary phase frames *<predicate>* Subspace labels and the rank budget
- [Role networks and frames](gate-network-frames.md): A fixed linear network of wires (roles) and pointwise gates is run on arrays; assigning each vertex an invertible frame D_v makes the implemented operator D_out S D_in⁻¹, so only changes of frame along edges cost work.
  Shown as: Binary phase frames *<predicate>* Role networks and frames
- [Three-subset gather and scatter network](subset-intersection-network.md): A fixed network on banks indexed by triples of 3-subsets whose gather, scatter, copy and side-injection gates have net coefficient depending on intersection size, cancelled by scratch wires, so three stages realize the signed exchange (X, Y) ↦ (−Y, X).
  Shown as: Binary phase frames *<predicate>* Three-subset gather and scatter network

## Pages that build on this one

- Simultaneous butterfly layer: One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [Established O(n log n) integer multiplier](nlogn-multiplier.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Arrays, address fields and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Nondegenerate subspaces and orthogonal residuals](nondegenerate-subspaces.md)
- [Rank saving and the power-saving recurrence](rank-saving-recurrence.md)
- [Bit network as an address shear](bit-network-interface.md)
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

- "is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual" (paper)

  > \begin{proposition}\label{prop:complex-motif-interface} For each edge of the complex network, write $U,V$ for its tail and head labels. Its phase-frame difference $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual. Here $(X_vf)(x)=f(x+v)$. The sum of these basis lengths is \[ s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c} =1873807244636671267308000000<W_{\rm c}m. \] After source and sink diagonal corrections, and undoing the signed bank exchange, telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles. The same assertion holds on any positive number of columns by taking tensor products over columns. \end{proposition}

- "q_U(x)=\operatorname{wt}(P_Ux)\pmod4." (paper)

  > Use the complex scalar network and binary labels. For a binary vector $x$, let $\operatorname{wt}(x)$ denote its integer Hamming weight, and write $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$. For a label $U$, let \[ q_U(x)=\operatorname{wt}(P_Ux)\pmod4. \] The projection here is over $\mathbb F_2$. Let \[ H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad C=H\begin{pmatrix}1&0\\0&i\end{pmatrix}H =aI+bX,\qquad a=\frac{1+i}{2},\quad b=\frac{1-i}{2}, \] where $X$ interchanges the two coordinates. On functions of $x\in\mathbb F_2^m$ define \[ \mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}. \] The use of $H$ in this definition is an identity of matrices. Each entry of $\mathcal C_U$ and its inverse is a Gaussian integer divided by $2^m$, so both preserve arrays over $\mathbb Z[i,1/2]$. The kernels implemented below have Gaussian dyadic coefficients.


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

Write the body to `exegenius/tasks/0018-write-phase-interface.answer.md` and the JSON to `exegenius/tasks/0018-write-phase-interface.answer.json`, then run `exegenius submit 0018-write-phase-interface` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0018-write-phase-interface`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
