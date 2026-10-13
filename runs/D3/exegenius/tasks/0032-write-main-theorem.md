# exegenius task 0032-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/D3` (paths below are relative to it)

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

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, algorithms and a theory-of-computation course, with linear algebra and basic probability or number theory. They know asymptotic analysis, divide-and-conquer recurrences, binary and positional number representations, modular arithmetic, and sets and functions, and have met the idea of a fast Fourier transform and the n log n multiplication story at most informally. They have not studied finite fields, abstract algebra beyond basics, numerical error analysis, or the specialist literature on multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Convolution and radix-digit reduction
- Discrete Fourier transform
- Schönhage–Strassen n log n conjecture and history
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The polynomial variable whose powers serve as roots of unity.
  - $r$ (ring degree): The number of coefficients in a polynomial, a power of two.
- Synthetic polynomial transforms
- Address rearrangement cost on tapes
- Gaussian resampling
- Chinese-remainder map to prime cyclic axes
- Bluestein chirp identity
- Coefficient twist to the polynomial ring
- Signed packing (Kronecker substitution)
- Linear networks, roles and frames
- Finite network via three-element subsets and nested subspaces
- Recursive saving from s < Wm
- Fast address-field interchange
- Simultaneous butterfly layers
- Precision and exact recovery
- Elementary stream operations and controlled shifts
- Scalar gates with restored scratch wires
- Rank budget of the network labels
- Bit and complex network interfaces
- Lower triangular factorization and matrix shear
- Power-width and arbitrary-width chunk interchange
- Packed selected-bit addition on grouped rectangles
- Synthetic transform layout and cost
- Tensor resampling with retained permutations
- Fixed rational parameter choice and cost table
- Linear algebra over the reals and rationals (also: matrices, vector spaces, subspaces, linear maps, invertible matrix, rank, dimension, linear combination)
- Modular arithmetic and congruences (also: mod, residues, congruence classes, Z/nZ)
- Primes, coprimality and gcd (also: prime numbers, relatively prime, greatest common divisor, distinct primes)
- Binary representation and bit operations (also: bits, XOR, binary expansion, two's complement, most significant bit, bitwise exclusive or)
- Radix (base-b) positional representation (also: digits in base b, radix digits, base expansion)
- Floor, ceiling and logarithms (also: lg, log base 2, floor function, ceiling function)
- Schoolbook multiplication (also: grade-school multiplication, quadratic multiplication)
- Divide-and-conquer recurrences (also: recursion, recurrence relations, master theorem)
- Fixed-point arithmetic and rounding error (also: fixed-point numbers, rounding, approximation error, absolute error, sup norm)
- Complex exponential and unit roots (also: Euler's formula, e^{2 pi i/N}, primitive root of unity, unit circle)
- Cyclic groups and cyclic indexing (also: indices mod n, cyclic wraparound, cyclic convolution, Z_n)
- Cartesian products and multidimensional arrays (also: tensor indexing, multi-index, array axes, lexicographic order)
- Permutations (also: bijections, rearrangement of indices)
- Gaussian elimination and triangular matrices (also: lower triangular matrix, LU factorization)
- Gaussian function (also: normal density, e^{-x^2})
- Time complexity and reductions (also: worst-case running time, reduction, linear-time scan, sorting cost)
- Basic induction and proof by contradiction (also: induction, proof technique)
- Basic set notation and counting (also: subsets, cardinality, binomial coefficients, pigeonhole)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, divide-and-conquer DFT)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: Deterministic fixed-tape multiplication of n-bit integers in O(n(lg n)^{1−κ}), κ=2^{-182}, disproving the n log n conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits of each integer.
- $\kappa$ (saving exponent): The constant 2^{-182} giving the power saving in the log factor.

## This page in the argument

The step: Two $n$-bit integers can be multiplied exactly on a fixed finite-tape machine in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.
How: reduce multiplication to convolution, build two fast tape procedures whose recursion has a strict rank saving, and assemble the transforms into an exact product
Why: Scanning costs a pass per transform level, giving $n\log n$; a power saving requires cheaper movement and arithmetic, then a full exact multiplication assembled around them. (the sources leave this for the reader to work out: spell it out)
Striking feature: A power saving $(\lg n)^{-\kappa}$ below $n\lg n$ with a tiny exponent, from the strict inequality $s<Wm$. (explain why it holds, from the method)

Its sub-steps, in order:

- Schönhage and Strassen conjectured that $n\log n$ is optimal, and Harvey and van der Hoeven reached $O(n\log n)$; the goal is to beat it. (on [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md))
- Splitting the inputs into radix digits reduces integer multiplication to convolution of short integer coefficient lists. (on [Convolution and radix-digit reduction](convolution.md))
- Two tape procedures, a fast address-field interchange and fast simultaneous butterfly layers, beat the $\Theta(n\log n)$ cost of scanning.
- The integer product is reduced to a convolution over $\mathbb C[y]/(y^r+1)$, computed with the fast procedures, with exact recovery of the result.

## Steps this page derives

The argument gives this page these sub-steps of its step (S3, S4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3**: Two tape procedures, a fast address-field interchange and fast simultaneous butterfly layers, beat the $\Theta(n\log n)$ cost of scanning.
How: show that scanning is too expensive, then build both procedures from one network

**S4**: The integer product is reduced to a convolution over $\mathbb C[y]/(y^r+1)$, computed with the fast procedures, with exact recovery of the result.
How: chain the reductions: convolution on the ring, Gaussian resampling, chirps, Chinese-remainder axes, phase twist, then precision and cost

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)): Schönhage and Strassen conjectured that $n\log n$ is optimal, and Harvey and van der Hoeven reached $O(n\log n)$; the goal is to beat it.
- S2 (on [Convolution and radix-digit reduction](convolution.md)): Splitting the inputs into radix digits reduces integer multiplication to convolution of short integer coefficient lists.
- S3.1 (on [Address rearrangement cost on tapes](tape-address-rearrangement.md)): Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so savings are needed in both movement and arithmetic.
- S3.2 (on [Linear networks, roles and frames](linear-network-frames.md)): Both tape procedures arise from one fixed linear network exchanging two banks of values with frames, and recursion on it saves a power.
- S3.3 (on [Fast address-field interchange](address-interchange.md)): Two address fields of $u$ bits are interchanged at cost $O(Vu^\tau)$ with $\tau<1$.
- S3.4 (on [Simultaneous butterfly layers](fast-butterfly-layer.md)): Simultaneous butterfly layers on selected coordinate bits cost $O(Vd^{\lambda'})$, $\lambda'<1$.
- S4.1 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Convolution over $\mathbb C[y]/(y^r+1)$ is computed with synthetic transforms and packed polynomial products.
- S4.2 (on [Gaussian resampling](gaussian-resampling.md)): Each source Fourier transform is expressed through a transform with power-of-two axis lengths.
- S4.3 (on [Bluestein chirp identity](bluestein-chirp.md)): Bluestein's chirp identity converts the middle transform, with its target permutation, into a normalized cyclic convolution; the permutation cancels.
- S4.4 (on [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)): The radix-digit coefficient list is placed on a product of pairwise coprime cyclic axes by a convolution-preserving Chinese-remainder address map.
- S4.5 (on [Coefficient twist to the polynomial ring](phase-twist.md)): A coefficient twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, whose negative wrap gives the cyclic wrap after untwisting.
- S4.6 (on [Precision and exact recovery](precision-exact-recovery.md)): Fixed-point errors stay strictly below $1/2$, so rounding, rescaling and carry propagation give the exact integer product.
- S4.7 (on [Fixed rational parameter choice and cost table](parameter-choice.md)): With fixed rational parameters such as $\tau=\sigma=1-2^{-50}$ every row of the cost table fits $O(p^{1-\epsilon'})$ after dividing by the volume.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md): Schönhage and Strassen's O(n log n log log n) bound and conjecture that n log n is optimal, later met by Harvey–van der Hoeven's O(n log n).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Schönhage–Strassen n log n conjecture and history
- [Gaussian resampling](gaussian-resampling.md): Harvey–van der Hoeven reduction replacing needed Fourier transforms by multidimensional transforms with power-of-two axis lengths.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md): Places the radix-digit coefficient list on a product of distinct prime cyclic axes by a convolution-preserving CRT address map.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder map to prime cyclic axes
- [Bluestein chirp identity](bluestein-chirp.md): Converts a Fourier transform into a cyclic convolution via chirp factors.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp identity
- [Coefficient twist to the polynomial ring](phase-twist.md): A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap yields the cyclic wrap after untwisting.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Coefficient twist to the polynomial ring
- [Signed packing (Kronecker substitution)](signed-packing.md): Packs polynomial coefficients into one long integer so a polynomial product becomes an integer product by the established O(n log n) multiplier.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Signed packing (Kronecker substitution)
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier transforms over the ring where roots of unity are powers of y, so multiplications by roots are signed shifts (Nussbaumer).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic polynomial transforms
- [Fast address-field interchange](address-interchange.md): Interchanges two address fields of u bits at cost O(V u^τ), τ<1, through XOR combinations of data, with the final result an exact permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast address-field interchange
- [Simultaneous butterfly layers](fast-butterfly-layer.md): Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected coordinate bits of complex fixed-point arrays at cost O(V d^λ′), λ′<1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Simultaneous butterfly layers
- [Precision and exact recovery](precision-exact-recovery.md): Fixed-point errors are kept strictly below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Precision and exact recovery
- [Tensor resampling with retained permutations](tensor-resampling.md): Gaussian resampling lines combined over d axes, keeping source and target permutations inside the transform identity.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Tensor resampling with retained permutations
- [Fixed rational parameter choice and cost table](parameter-choice.md): Choice τ=σ=1−2^{−50}, c, λ′ etc. and a cost table whose rows each fit O(p^{1−ε′}) after dividing by volume.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed rational parameter choice and cost table
- [Synthetic transform layout and cost](transform-layout-cost.md): Layout of the synthetic transform over R_r with truncation Q_p, contractions, and stored frequency order retained through pointwise product; cost via simultaneous layers.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic transform layout and cost
- [Elementary stream operations and controlled shifts](elementary-streams.md): Linear-time scans on tapes: digit permutations, moves, and controlled shifts/fixed rational scalings of a field using earlier control fields; arrays stored in lexicographic order with a self-delimiting integer header code.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Elementary stream operations and controlled shifts

## Other pages you may link to

- [Convolution and radix-digit reduction](convolution.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-y-r-1.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [Address rearrangement cost on tapes](tape-address-rearrangement.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Finite network via three-element subsets and nested subspaces](finite-network-subspaces.md)
- [Recursive saving from s < Wm](recursive-power-saving.md)
- [Scalar gates with restored scratch wires](scalar-motifs.md)
- [Rank budget of the network labels](motif-residuals.md)
- [Bit and complex network interfaces](motif-interfaces.md)
- [Lower triangular factorization and matrix shear](matrix-shear.md)
- [Power-width and arbitrary-width chunk interchange](chunk-swap.md)
- [Packed selected-bit addition on grouped rectangles](packed-selected-bit-addition.md)

## Evidence from the sources, with the paragraph around each quote

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "\subsection{The multiplication algorithm}" (paper)

  > \subsection{The multiplication algorithm}

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

Write the body to `exegenius/tasks/0032-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0032-write-main-theorem.answer.json`, then run `exegenius submit 0032-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
