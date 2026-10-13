# exegenius task 0020-write-finite-network-subspaces

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
- Fixed multitape Turing machine model
- Convolution and cyclic convolution
- Fourier transform and roots of unity
- The n log n conjecture and history of multiplication
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity.
  - $r$ (coefficient count): The number of coefficients of a polynomial in the ring, a power of two.
- Synthetic polynomial transforms
- Two-point butterfly H₀
- Reduction of integer product to digit convolution
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Bluestein chirp identity
- Last-coordinate phase twist
- Elementary stream operations and controlled shifts
- Linear networks with roles and restored auxiliaries
- Frames and endpoint operators
- Gaussian dyadics and fixed-point precision
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

Concept: Finite networks with nested subspaces and rank saving
Gloss: Network whose gates carry nested subspaces of an m-dimensional space built from three-element subset intersections, with total smaller calls s < W m.

## This page in the argument

The step: Nested subspaces of an $m$-dimensional space attached to the gates, built from three-element subset intersections, give a network with total number $s$ of smaller calls less than $Wm$.

It serves these steps, from the main result down:

- A deterministic fixed-tape Turing machine multiplies two $n$-bit integers in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, with $p$ bits of working precision, $d$ transform axes of length about $r$.; how: Reduce the product to a convolution through a chain of representation changes, evaluate it with the two fast tape procedures, then recover the exact product and sum the costs (on [Integer multiplication in O(n (lg n)^(1-κ)) time](main-theorem.md))
- Two tape procedures, the address interchange and the simultaneous butterfly layer, cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for fixed $\tau,\lambda'<1$ on stored bit volume $V$.; how: Obtain both procedures from fixed linear networks with a strict rank saving and recurse
- Two disjoint contiguous address fields of $u$ bits in a Cartesian-product array of volume $V$ can be interchanged in time $O(Vu^\tau)$ for a fixed $\tau<1$.; how: Build a fixed linear network with a rank saving, use it recursively on streams of volume $V/W$, and turn each edge into smaller interchanges (on [Fast interchange of address chunks](address-interchange.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Frames and endpoint operators](frames.md): Invertible linear operators D_v attached to gates; intermediate frames cancel so a route applies D_sink D_source^-1, leaving an endpoint operator such as an address shear or the H₀ layer.
  Shown as: Finite networks with nested subspaces and rank saving *<predicate>* Frames and endpoint operators

## Pages that build on this one

- Recursive power saving: A call at parameter m f uses s calls at f on volume V/W, raising the cost factor by s/W < m, giving a power of the logarithm.

## Other pages you may link to

- [Convolution and cyclic convolution](convolution.md)
- [Reduction of integer product to digit convolution](radix-reduction.md)
- [Polynomial ring modulo y^r + 1](poly-ring-yr1.md)
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

- "The decisive property is that the total" (paper)

  > The finite construction in Section~\ref{sec:finite-networks} attaches subspaces of a fixed $m$-dimensional space to its gates and terminals. The subspaces at adjacent vertices are nested. Their dimension changes count the smaller operations needed on an edge, with an additional source contribution in the bit construction. The construction uses three-element subsets: gather and scatter create coefficients depending on intersection size, and auxiliary wires cancel the unwanted coefficients. Orthogonality of the corresponding indicator vectors permits the subspace assignments. The decisive property is that the total number $s$ of smaller calls satisfies $s<Wm$.

- "A label is a nondegenerate subspace of a fixed bilinear space." (paper)

  > The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive. A label is a nondegenerate subspace of a fixed bilinear space. On every edge one label will contain the other. For such an edge, the \emph{orthogonal residual} is the orthogonal complement of the smaller label inside the larger one; its dimension is the absolute change in label dimension. The saving will come from keeping the total dimension lost on decreasing edges small relative to $N$.

- "The only decreasing
edges are the central-wire edges from time 3 to time 4" (paper)

  > \begin{lemma}\label{lem:motif-residuals} Every edge joins comparable nondegenerate labels. The only decreasing edges are the central-wire edges from time 3 to time 4; their dimension loss is $h$. Consequently, if $c$ is the number of central wires per invocation and $W$ the total number of wires, then \begin{equation} L=Ich,\qquad \sum_{e}\bigl|\dim U_{\mathrm{head}(e)}- \dim U_{\mathrm{tail}(e)}\bigr| =Wm-2N+2L. \label{eq:rank-budget-labels} \end{equation} For the binary label space, every nonzero orthogonal residual of an edge has an orthonormal basis. \end{lemma}

- "Let $\mathcal T$ be the set of three-element subsets of $[h]$." (paper)

  > Put \[ h=100,\qquad v=\binom h3=161700,\qquad N=v^3=4227952113000000,\qquad m=h^3=1000000. \] Let $\mathcal T$ be the set of three-element subsets of $[h]$. There are two data banks $X_a,Y_a$, indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its \emph{role}, so that we can distinguish a fixed place in the network from the value currently carried there.


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

Write the body to `exegenius/tasks/0020-write-finite-network-subspaces.answer.md` and the JSON to `exegenius/tasks/0020-write-finite-network-subspaces.answer.json`, then run `exegenius submit 0020-write-finite-network-subspaces` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0020-write-finite-network-subspaces`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
