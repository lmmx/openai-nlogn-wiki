# exegenius task 0006-write-poly-ring-yr1

Project directory: `/home/user/openai-nlogn-wiki/runs/M3` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis and recurrences, algorithm design (divide and conquer, the classical FFT idea), basic Turing machine complexity, discrete mathematics (binary and positional number systems, modular arithmetic, prime numbers, subsets), and the linear algebra and calculus that such a degree includes (vector spaces, subspaces, rank, matrices, inverse, real exponentials and logarithms). The reader has not studied algebraic structures beyond the basics, number theory beyond elementary modular arithmetic, numerical error analysis, or the research literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Convolution and cyclic convolution
- Reduction of integer product to digit convolution
- Binary representation of integers (also: binary expansion, bits, most significant bit, bit strings)
- Positional radix and digit expansion (also: base-b digits, radix digits, carries)
- Logarithms and floor/ceiling (also: lg, log base 2, ceiling, floor)
- Modular arithmetic and congruences (also: remainder, mod, residues, cyclic indices)
- Prime numbers and coprimality (also: distinct primes, pairwise coprime, gcd)
- Matrices and linear maps (also: linear operator, matrix inverse, invertible matrix, matrix product, diagonal matrix, GL)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, rank of a matrix, linear combination, direct sum)
- Permutations and permutation matrices (also: partial permutation, bijection of indices, rearrangement)
- Cartesian products and multidimensional arrays (also: tensor array, product of index sets, multi-index)
- Divide and conquer recurrences (also: recursion, recursive calls, master theorem)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, fast convolution)
- Absolute value, norms and error bounds (also: sup norm, max norm, rounding error, truncation, triangle inequality)
- Dyadic rationals and fixed-point numbers (also: binary fixed point, power-of-two denominators)
- XOR and bitwise operations (also: exclusive or, bit flip, bitwise sum mod 2)
- Finite sets and subset operations (also: intersection, union, support, indicator)
- Euler's formula and unit circle (also: e^{2 pi i/N}, primitive root of unity, complex conjugate, modulus)
- Worst-case running time and Turing machine step counting (also: time complexity, T(n), linear time, DTIME)
- Gaussian elimination and triangular matrices (also: lower triangular matrix, row operations, shear)

## This page

Concept: Polynomial ring modulo y^r + 1
Gloss: Polynomials in y with complex coefficients reduced using y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
Heading: Polynomial ring modulo $y^r + 1$

The symbols in this page's heading denote (say so on the page):

- $y$ (polynomial variable): The formal variable whose powers act as roots of unity.
- $r$ (coefficient count): The number of coefficients of a polynomial in the ring, a power of two.

## Where the argument relies on this page

- A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, with $p$ bits of working precision, $d$ transform axes of length about $r$. (on [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md))
- Simultaneous normalized butterfly layers applying $H_0$ at the same bit position in each of at most $d$ address chunks cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, with coefficient error less than $\sqrt2\,2^{-p}$. (on [Simultaneous fast butterfly layers](fast-butterfly-layer.md))
- Convolution over the ring $\mathbb C[y]/(y^r+1)$ on the remaining axes is computed with cost small enough to be dominated by the fast layers and interchanges.
- Synthetic characters cancel, so the forward and opposite synthetic transforms invert each other up to a scale, $F_t^+F_t^-=t^{-1}I$. (on [Synthetic polynomial transforms](synthetic-transforms.md))
- Polynomial products in the ring of $r$ complex coefficients are computed exactly by signed packing (Kronecker substitution) and the ordinary $O(n\log n)$ multiplier, in time $O(rp\log(rp))$. (on [Signed packing (Kronecker substitution)](signed-packing.md))
- A phase twist turns the last cyclic coordinate into a polynomial modulo $y^r+1$, and its negative wrap gives the original cyclic wrap after untwisting. (on [Last-coordinate phase twist](phase-twist.md))

## Pages that build on this one

- Last-coordinate phase twist: A phase twist turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
- Synthetic polynomial transforms: Nussbaumer-style transforms over the ring modulo y^r+1 where roots of unity are powers of y, so root multiplication is a signed shift; computed by address rearrangements, shifts and butterflies.
- Signed packing (Kronecker substitution): Packing polynomial coefficients into one integer so a polynomial product is computed with the ordinary O(n log n) multiplier as a subroutine.

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-reduction.md)
- [Gaussian dyadics and fixed-point precision](complex-fixed-point.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Fourier transform and roots of unity](dft-roots-of-unity.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Two-point butterfly H₀](butterfly.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Fixed multitape Turing machine model](multitape-model.md)
- [The n log n conjecture and history of multiplication](nlogn-conjecture.md)
- [Elementary stream operations and controlled shifts](stream-operations.md)
- [Linear networks with roles and restored auxiliaries](linear-network.md)
- [Frames and endpoint operators](frames.md)
- [Finite networks with nested subspaces and rank saving](finite-network-subspaces.md)
- [Recursive power saving](recursive-saving.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Lower triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Simultaneous fast butterfly layers](fast-butterfly-layer.md)
- [Synthetic transforms on the retained layout](transform-layout.md)
- [Normalized convolution over the polynomial ring](normalized-convolution.md)
- [Precision, rounding and carry propagation](exact-recovery.md)
- [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "one coordinate
is stored as the coefficient list of a polynomial modulo $y^r+1$" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "\mathcal R_r=\mathbb C[y]/(y^r+1)" (paper)

  > For an integer $r\geq 2$ that is a power of two, put \[ \mathcal R_r=\mathbb C[y]/(y^r+1),\qquad \left\|\sum_{k=0}^{r-1}z_k y^k\right\|_\infty =\max_{0\leq k<r}|z_k|. \] We always use representatives of degree less than $r$. Multiplication by $y^a$, for any integer $a$, permutes the coefficients and changes some signs; consequently it is an isometry for this norm. For arrays over $\mathcal R_r$, the same notation denotes the maximum over all coefficients in all entries. A disk array has norm at most one. A $p$-bit grid array has real and imaginary coefficient parts in $2^{-p}\mathbb Z$. For any array, let $Q_p$ truncate each real and imaginary coefficient part toward zero to this grid. Then \begin{equation} \|Q_p z-z\|_\infty<\sqrt2\,2^{-p},\qquad \|Q_p z\|_\infty\leq\|z\|_\infty. \label{eq:transform-truncate} \end{equation}


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

Write the body to `exegenius/tasks/0006-write-poly-ring-yr1.answer.md` and the JSON to `exegenius/tasks/0006-write-poly-ring-yr1.answer.json`, then run `exegenius submit 0006-write-poly-ring-yr1` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0006-write-poly-ring-yr1`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
