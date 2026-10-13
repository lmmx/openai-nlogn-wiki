# exegenius task 0024-write-fast-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/B1` (paths below are relative to it)

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

For these sources: The reader has done an undergraduate computer science degree: asymptotic analysis and recurrences, basic algorithms (including schoolbook and Karatsuba multiplication and the idea of the FFT), discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, permutations, bit operations), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know complex numbers, polynomials and basic Turing machines with tapes. They have not studied abstract algebra beyond rings as a name, tensor products, Nussbaumer or Schönhage–Strassen transforms, or any research-level multiplication algorithm.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Schönhage–Strassen n log n optimality conjecture
  - $n$ (input length): The number of bits in each input integer.
- Multiplication as convolution of digit lists
- Discrete Fourier transform
- Multidimensional transform
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The indeterminate of the polynomials.
  - $r$ (ring degree): The number of complex coefficients in a polynomial, a power of two.
- Synthetic polynomial transform
- Two-point butterfly H₀
  - $H_0$ (butterfly map): The map sending a pair of values to their half-sum and half-difference.
  - $u$ (first value): The first input value of the pair.
  - $v$ (second value): The second input value of the pair.
- Chinese-remainder address map onto prime axes
- Signed packing (Kronecker substitution)
- Established O(n log n) multiplier as subroutine
- Linear networks with roles and frames
- Three-element-subset finite networks
  - $s$ (number of calls): The number of smaller calls the network makes.
  - $W$ (number of roles): The number of wires (roles) of the network.
  - $m$ (space dimension): The dimension of the fixed space whose subspaces label the network.
- Scratch-restoring exchange network
- Recursive power saving
  - $s$ (number of calls): The number of smaller calls.
  - $W$ (number of roles): The number of roles of the network.
  - $m$ (parameter multiplier): The factor by which the recursive parameter grows.
- Elementary scans and controlled shifts
- Lower triangular factorization
  - $m$ (matrix size): The number of rows and columns of the matrix.
  - $a$ (matrix rank): The rank of the matrix.
- Rational matrix shear of address fields
- Fast address-field interchange
  - $V$ (bit volume): The number of stored bits.
  - $u$ (field width): The number of bits in each interchanged address field.
  - $\tau$ (saving exponent): A fixed constant below 1.
- Phase frames for the butterfly layer
- Logarithms and iterated logarithms (also: lg, log base 2, log n, lg n)
- Binary representation and bit operations (also: bits, XOR, bit position, binary expansion, radix representation)
- Schoolbook and Karatsuba multiplication (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, fast Fourier transform)
- Convolution (also: cyclic convolution, product of coefficient sequences, polynomial multiplication as convolution)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, cyclic group Z/n)
- Primes and coprimality (also: distinct primes, relatively prime, gcd, greatest common divisor, prime number theorem)
- Chinese remainder theorem (also: CRT)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, lower triangular matrix, matrix rank, identity matrix)
- Vector spaces and subspaces (also: change of basis, linear subspace, linear independence, basis)
- Permutations (also: permutation matrix, partial permutation, bijection of indices)
- Floor, ceiling and rounding (also: nearest integer, floor function, integer part)
- Recursion and recurrence relations (also: divide and conquer, recurrence, master theorem, recursive calls)
- Fixed-point and dyadic arithmetic (also: fixed-point numbers, dyadic rationals, truncation error, rounding error)
- Complex conjugate and modulus (also: conjugate, absolute value of complex number, Gaussian integers)
- Cartesian products and multi-indexing (also: multidimensional array, tuple indices, product of index sets)
- Linear-time scans and tape sorting (also: sorting on tapes, copying a tape, linear scan, tape reversal)
- Deterministic computation and time complexity classes (also: deterministic algorithm, running time, step count, worst-case time)
- Geometric and power-of-two parameter manipulation (also: powers of two, geometric series, exponent inequalities)

## This page

Concept: Simultaneous butterfly layers
Gloss: Applies H₀ at the same bit position of up to d address chunks at once on complex fixed-point records, in O(V d^λ′) with λ′<1.
Heading: Simultaneous butterfly layer in time $O(Vd^{\lambda'})$

The symbols in this page's heading denote (say so on the page):

- $V$ (bit volume): The number of stored bits.
- $d$ (chunk count): The number of address chunks whose selected bit is transformed.
- $\lambda'$ (saving exponent): A fixed constant below 1.

## This page in the argument

The step: The two-point butterfly $H_0$ is applied at the same bit of up to $d$ address chunks on complex fixed-point records in $O(Vd^{\lambda'})$ with $\lambda'<1$.
How: run the same linear network with phase frames in place of bit shears, so that the layer reduces to smaller groups of selected bits
Why: Separate butterfly factors would need $D$ whole-array passes; the network trades them for a recursion with the same strict rank saving. (the sources say so: "whereas separate butterfly" (paper))
Striking feature: The cost exponent $\lambda'$ is strictly below 1, although each butterfly alone needs a pass over the array. (explain why it holds, from the method)

Its sub-steps, in order:

- The complex network telescopes its phase frames to give the tensor product $C^{\otimes m}$ on every role, with total rank $s_{\rm c}<W_{\rm c}m$.
- With $C=HSH=aI+bX$, $C^2=X$ and $H_0=bSCS$, a tensor product of butterflies is expressed through smaller groups of selected bits separated by binary changes of basis. (on [Phase frames for the butterfly layer](phase-frames.md))
- Selected address bits of a rectangle are changed by packed whole-chunk moves and controlled shifts, with a deterministic repair of the exceptional addresses.
- The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits, giving a layer at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.

It serves these steps, from the main result down:

- Integer multiplication of $n$-bit integers takes $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$ on one fixed multitape machine.; how: reduce to digit convolution, build the fast tape and ring-transform tools bottom up, then assemble reductions, precision and cost (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- The two tape procedures, fast address interchange and simultaneous butterfly layers, exist with power savings.; how: construct each procedure from its own fixed linear network, after the elementary scans

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3.1, S2.3.3, S2.3.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3.1**: The complex network telescopes its phase frames to give the tensor product $C^{\otimes m}$ on every role, with total rank $s_{\rm c}<W_{\rm c}m$.
Source: "telescoping these phase frames gives $C^{\otimes m}$" (paper)
> \begin{proposition}\label{prop:complex-motif-interface} For each edge of the complex network, write $U,V$ for its tail and head labels. Its phase-frame difference $\mathcal C_V\mathcal C_U^{-1}$ is a product of one translation kernel $aI+bX_v$, or its inverse, per vector in an orthonormal basis of the edge residual. Here $(X_vf)(x)=f(x+v)$. The sum of these basis lengths is \[ s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c} =1873807244636671267308000000<W_{\rm c}m. \] After source and sink diagonal corrections, and undoing the signed bank exchange, telescoping these phase frames gives $C^{\otimes m}$ on every role, including auxiliary roles. The same assertion holds on any positive number of columns by taking tensor products over columns. \end{proposition}

**S2.3.3**: Selected address bits of a rectangle are changed by packed whole-chunk moves and controlled shifts, with a deterministic repair of the exceptional addresses.
Source: "\begin{lemma}[Packed selected-bit addition on one rectangle]" (paper)
> \begin{lemma}[Packed selected-bit addition on one rectangle] \label{lem:packed-selected-bit-rectangle} Let $R\ge1$, $K\ge6$, $f\ge1$, $L=fK$, and $0\le\rho<K$. Let $N_0,N_1,N_2,N_3$ be positive integers, and let $(\chi_1,\chi_2,\chi_3)$ be a permutation of $(x,y,z)$. Consider $R$-bit records in lexicographic order on \[ [N_0]\times[2^L]_{\chi_1}\times[N_1]\times[2^L]_{\chi_2} \times[N_2]\times[2^L]_{\chi_3}\times[N_3]. \] The subscript names the chunk at that position. The input supplies $N_0,\ldots,N_3,R,K,f,\rho$ as a fixed number of canonical binary integers, together with the finite permutation of the chunk names, as in Section~\ref{sec:streams}. Put \[ M=2^{3L}\prod_{h=0}^3N_h,\qquad V=MR,\qquad A_{\rm rect}=\lceil\log_2(2V)\rceil. \] At the selected positions

**S2.3.4**: The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits, giving a layer at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
Source: "The phase-frame construction reduces a group of $e$ selected bits to" (paper)
> \begin{proof} The procedure reads the current parameters and component width from $\mathcal E$. Parsing this header and forming the initial collapsed descriptors take polynomial time in $p$, already charged in the descriptor work above. The phase-frame construction reduces a group of $e$ selected bits to $s_{\rm c}$ children on $e/m$ selected bits. The row split gives each child $1/W_{\rm c}$ of the parent's logical volume. The packed selected-bit procedure supplies the binary basis changes. We verify that its cost is uniform over the displayed bands for $d,r$. Put $\Delta=\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, a common cutoff gives $\Delta\le p$. The guarded record width is then $R_{\rm g}=2r(p+2\Delta+3)\le12rp$; also $R_{\rm g}\ge2rp$. Padding at most doubles the original record count $M$, and row splitting only decreases it. Thus a packed child with $M_{\rm child}$ records has the following value $A_*$ of its rectangular width parameter: \[ \begin{split} A_* &=\lceil\log_2(2M_{\rm child}R_{\rm g})\rceil\\ &\le\lceil\log_2(4MR_{\rm g})\rceil\le C_Ap, \qquad C_A=C_M+b_r+7. \end{split} \] The last inequality uses $\log_2(2M)\le C_Mp$, $\log_2r\le b_rp/d\le b_rp$, and $\log_2p\le p$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.3.2 (on [Phase frames for the butterfly layer](phase-frames.md)): With $C=HSH=aI+bX$, $C^2=X$ and $H_0=bSCS$, a tensor product of butterflies is expressed through smaller groups of selected bits separated by binary changes of basis.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Linear networks with roles and frames](linear-network-frames.md)
- [Three-element-subset finite networks](subset-network.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Two-point butterfly H₀](butterfly.md): The map (u,v) → ((u+v)/2, (u−v)/2), the basic arithmetic step of a transform layer, applied coefficientwise.
  Shown as: Simultaneous butterfly layers *<predicate>* Two-point butterfly H₀
- [Phase frames for the butterfly layer](phase-frames.md): Using C=HSH=aI+bX with C²=X and H₀=bSCS, a tensor product of butterflies is expressed through smaller groups of selected bits separated by binary changes of basis.
  Shown as: Simultaneous butterfly layers *<predicate>* Phase frames for the butterfly layer
- [Recursive power saving](recursive-saving.md): Recursing at parameter mf with s calls of parameter f on volume V/W adds s/W<m per level, a strict inequality that gives a power saving.
  Shown as: Simultaneous butterfly layers *<predicate>* Recursive power saving
- [Fast address-field interchange](address-interchange.md): Interchanges two disjoint address fields of u bits via pointwise XOR combinations that end as an exact permutation, in O(V u^τ) with τ<1.
  Shown as: Simultaneous butterfly layers *<predicate>* Fast address-field interchange

## Pages that build on this one

- Fixed-point precision and exact recovery: Intermediate values are exact Gaussian dyadics truncated once; the recovered coefficient error is below 1/2 so rounding and carry propagation give the exact product.
- Retained frequency order and transform layout: Selected bits of the participating axes are placed at a common offset in K-bit chunks so the simultaneous layers apply, and the frequency order is retained through the pointwise product.
- Fixed rational parameter choice: The fixed exponents (τ=σ=1−2⁻⁵⁰, λ′=1−2⁻⁵⁴, ε=2⁻⁷⁵, κ=2⁻¹⁸²) and size parameters p=6b, d=⌊b^ε⌋ making all costs fit the theorem.
- Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1−κ)), κ=2^−182: digit convolution, CRT prime axes, Gaussian resampling and chirps, synthetic transforms over the y^r+1 ring, accelerated by fast address interchange and butterfly layers.

## Other pages you may link to

- [Multiplication as convolution of digit lists](convolution-reduction.md)
- [Polynomial ring modulo y^r + 1](polyring-mod.md)
- [Chinese-remainder address map onto prime axes](chinese-remainder-map.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Schönhage–Strassen n log n optimality conjecture](nlogn-conjecture.md)
- [Elementary scans and controlled shifts](controlled-shifts.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Three-element-subset finite networks](subset-network.md)
- [Scratch-restoring exchange network](scalar-motif-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational matrix shear of address fields](matrix-shear.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Established O(n log n) multiplier as subroutine](hvdh-subroutine.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Fixed-point precision and exact recovery](exact-recovery.md)
- [Synthetic character cancellation](synthetic-character-cancellation.md)
- [Retained frequency order and transform layout](transform-layout.md)
- [Normalized convolution over the ring](normalized-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Resampling without executing permutations](resampling-lemma.md)
- [Tensor interface for growing dimension](tensor-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Chirp and permutation cancellation](chirp-permutation-cancellation.md)
- [Fixed rational parameter choice](parameter-choice.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "the cost is $O(Vd^{\lambda'})$ for a
fixed $\lambda'<1$." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0024-write-fast-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0024-write-fast-butterfly-layer.answer.json`, then run `exegenius submit 0024-write-fast-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
