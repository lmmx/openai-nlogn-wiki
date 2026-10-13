# exegenius task 0022-write-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/B2` (paths below are relative to it)

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

For these sources: The reader has finished undergraduate computer science: asymptotic analysis, discrete mathematics, linear algebra over the reals and complex numbers, basic algebra (modular arithmetic, primes, finite fields of two elements at an introductory level), recurrences and divide-and-conquer algorithms such as Karatsuba and the FFT in outline. They have seen Turing machines and tapes but not tape-level complexity theory, and have not studied Fourier analysis on groups, coding theory, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen n log n conjecture
- Convolution and discrete Fourier transform
- Harvey–van der Hoeven O(n log n) multiplication
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable whose powers act as roots of unity.
  - $r$ (ring length): The number of coefficients in a polynomial of the ring, a power of two.
- Synthetic polynomial transforms
- Gaussian resampling
- Chinese-remainder address map
- Bluestein chirp conversion
- Last-coordinate phase twist
- Signed coefficient packing
- Array order and tape scans
- Elementary stream operations and controlled shifts
- Linear networks with roles and frames
- Finite networks with a rank saving
- Address shear and triangular factorization
- Fast address-field interchange
- Exact Gaussian dyadics and precision
- Recursive power saving
- Integer multiplication algorithms (also: schoolbook multiplication, Karatsuba, Karatsuba multiplication, long multiplication)
- Binary representation and bit strings (also: binary expansion, base-2 digits, bits, radix representation)
- Modular arithmetic (also: congruence, residues mod m, mod operation, cyclic group Z/mZ)
- Prime numbers and coprimality (also: distinct primes, pairwise coprime, gcd, relatively prime)
- Chinese remainder theorem (also: CRT)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 FFT, butterfly)
- Roots of unity (also: primitive root of unity, N-th roots of unity, e^{2 pi i/N})
- Linear algebra over a field (also: vector spaces, linear maps, matrices, invertible matrix, rank, subspace, dimension)
- The field F_2 and binary vector spaces (also: GF(2), F_2^h, XOR, bit vectors, mod 2 arithmetic)
- Triangular matrices and factorization (also: lower triangular matrix, LU factorization, unitriangular matrix, elementary row operations)
- Permutations (also: bijection, rearrangement, permutation matrix, bit-reversal)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree)
- Logarithms and iterated logarithms (also: lg, log base 2, log n, logarithm)
- Little-o, Omega and liminf asymptotics (also: little-o, Theta, Omega, limit inferior, liminf)
- Convolution of sequences (also: cyclic convolution, polynomial multiplication as convolution, linear convolution)
- Norms and error bounds (also: operator norm, contraction, triangle inequality, rounding error, Euclidean norm)
- Dyadic rationals and fixed-point numbers (also: fixed-point arithmetic, binary fractions, truncation, rounding)
- Gaussian function (also: Gaussian, bell curve, normal density, e^{-x^2})
- Direct sum and tensor product of vector spaces (also: Kronecker product, tensor product, multidimensional array indexing)
- Polynomial evaluation and interpolation (also: Lagrange interpolation, evaluating at roots of unity, degree of a polynomial)
- Asymptotic definition of algorithm cost and time complexity (also: running time, worst-case time, deterministic algorithm, linear time, pointer-free sequential scan)

## This page

Concept: Fast simultaneous butterfly layers
Gloss: Applies H0(u,v)=((u+v)/2,(u-v)/2) simultaneously on selected bits of several address chunks at cost O(V d^λ'), λ'<1, using phase frames and dyadic scaling.

## This page in the argument

The step: Simultaneous butterfly layers $H_0(u,v)=((u+v)/2,(u-v)/2)$ on selected bits of up to $d$ address chunks cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
How: apply the complex network with phase frames, exact dyadic values and one final truncation
Why: Separate butterfly factors would need D whole-array passes; one network call with phase frames does the layer at once, and exactness of dyadic values allows a single truncation. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The layer is obtained at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
- The intermediate dyadic values are bounded; they are exact Gaussian dyadics. (on [Exact Gaussian dyadics and precision](fixed-point-dyadics.md))
- The entire layer is evaluated exactly before one final truncation.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce multiplication to convolution, accelerate the tape procedures by a power saving, then chain the reductions to an exact product (on [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md))
- Two tape procedures save both movement and arithmetic: address interchange at cost $O(Vu^\tau)$ and simultaneous butterfly layers at cost $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.; how: supply two tape procedures, each from its own linear network with a recursive power saving

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.4.1, S2.4.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.4.1**: The layer is obtained at cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
Source: "We will obtain cost $O(Vd^{\lambda'})$, with" (paper)
> The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.

**S2.4.3**: The entire layer is evaluated exactly before one final truncation.
Source: "evaluated exactly before one final truncation." (paper)
> We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.4.2 (on [Exact Gaussian dyadics and precision](fixed-point-dyadics.md)): The intermediate dyadic values are bounded; they are exact Gaussian dyadics.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Recursive power saving](recursive-power-saving.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Finite networks with a rank saving](finite-subspace-network.md): Network construction using three-element subsets and nested subspaces, so that the sum s of edge ranks satisfies s<Wm.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Finite networks with a rank saving
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms over the polynomial ring using powers of y as roots, built from address rearrangements, signed shifts and two-point butterflies.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Synthetic polynomial transforms
- [Exact Gaussian dyadics and precision](fixed-point-dyadics.md): Values are exact Gaussian dyadics with power-of-two denominators; truncation after contractive layers adds bounded error, tracked so the final error is below 1/2.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Exact Gaussian dyadics and precision
- [Fast address-field interchange](address-interchange.md): Interchanges two disjoint address fields of u bits in V stored bits at cost O(V u^τ), τ<1, via XOR combinations ending in an exact permutation.
  Shown as: Fast simultaneous butterfly layers *<predicate>* Fast address-field interchange

## Pages that build on this one

- Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1-κ)), κ=2^-182, refuting the n log n conjecture; it chains digit convolution, CRT axes, resampling, chirps, phase twist and synthetic transforms, accelerated by fast address interchange and butterfly layers.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Convolution and discrete Fourier transform](convolution-dft.md)
- [Harvey–van der Hoeven O(n log n) multiplication](nlogn-multiplier.md)
- [Polynomial ring modulo y^r + 1](ring-mod-yr1.md)
- [Array order and tape scans](tape-scans.md)
- [Linear networks with roles and frames](linear-network-frames.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Elementary stream operations and controlled shifts](stream-operations.md)
- [Recursive power saving](recursive-power-saving.md)
- [Address shear and triangular factorization](address-shear.md)
- [Signed coefficient packing](signed-packing.md)
- [Tensor resampling with retained permutations](tensor-resampling-chirps.md)
- [Rounding and carry propagation](exact-recovery.md)
- [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "\begin{proposition}[Simultaneous normalized butterfly layer]" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice

- "\begin{lemma}[Transform layout and cost]" (paper)

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

Write the body to `exegenius/tasks/0022-write-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0022-write-butterfly-layer.answer.json`, then run `exegenius submit 0022-write-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
