# exegenius task 0008-write-linear-network

Project directory: `/home/user/openai-nlogn-wiki/runs/D2` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithms (divide and conquer, sorting, recurrences, schoolbook integer arithmetic), discrete mathematics, and introductory linear algebra, abstract algebra (groups, rings, fields, modular arithmetic) and probability. They know Turing machines and tapes at a basic level, but not the multitape fixed-alphabet cost model in detail, nor Fourier-analytic multiplication, FFT variants, or specialist algebra such as bilinear forms over F_2 and matrix factorizations like Bruhat.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Roots of unity
- Schönhage–Strassen n log n conjecture and history
- Fixed-tape machine model and cost of scans
- Elementary stream operations and controlled shifts
- Established O(n log n) multiplier as a subroutine
- Matrices and linear maps (also: linear algebra, matrix multiplication, invertible matrix, lower triangular matrix, linear transformation, basis)
- Modular arithmetic (also: congruences, residues, Z/nZ, integers modulo n)
- Chinese remainder theorem (also: CRT, Chinese remainder)
- Prime numbers and coprimality (also: primes, gcd, coprime, relatively prime, prime number theorem)
- Groups, rings and fields (also: abstract algebra, ring, finite field, F_2, GF(2), cyclic group, group homomorphism, direct product)
- Binary representation and bit operations (also: bits, XOR, binary expansion, two's complement, radix representation, base-b digits)
- Schoolbook and divide-and-conquer multiplication (also: Karatsuba, long multiplication, grade-school multiplication, quadratic multiplication)
- Fast Fourier transform (also: FFT, Cooley-Tukey, radix-2 FFT)
- Floor, ceiling, logarithms and exponents (also: lg, log base 2, floor function, ceiling function, iterated logarithm)
- Recurrences and amortized cost accounting (also: recurrence relation, master theorem, summing cost over levels, geometric series)
- Sorting and permutations (also: permutation, comparison sort, merge sort, bit-reversal permutation)
- Norms and inequalities (also: max norm, triangle inequality, sup norm, absolute value bound, Euclidean norm)
- Rounding and floating or fixed point error (also: truncation error, round to nearest integer, fixed-point arithmetic, approximation error)
- Gaussian integers and dyadic rationals (also: Z[i], dyadic numbers, Gaussian dyadic)
- Multidimensional arrays and product index sets (also: tensor indexing, array of dimension d, product of cyclic groups)
- Sums and product notation, Euler's formula (also: summation, e^{i theta}, Euler formula, complex exponential)
- Graphs and networks (also: directed graph, vertices and edges, circuit, gates, bipartite graph)
- Subsets and counting (also: binomial coefficient, indicator vector, inclusion-exclusion, 3-subsets, combinatorics)
- Basic probability and combinatorial bounds (also: union bound, pigeonhole principle, counting argument)

## This page

Concept: Linear network with roles, frames and restored scratch
Gloss: A fixed network of linear gates on wires (roles) exchanging two banks with signs, restoring every scratch value for arbitrary initial contents; applied to arrays, each wire gets an invertible frame whose change on an edge is what must be implemented.

## This page in the argument

The step: A fixed linear network of gates on wires (roles), applied to arrays, can have each wire carry an invertible frame, so that only the change of frame on each edge has to be implemented.
How: attach a frame to every source, gate and sink and observe that frames commute with pointwise gates
Why: Pointwise gates act on matching addresses, so a common frame at a gate leaves the gate unchanged and intermediate frames cancel; only edges cost anything. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Each wire's stored array is $D_vg$ for the logical array $g$, with the frame $D_v$ invertible and shared by all incidences of a gate.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$.; how: reduce integer multiplication to a Fourier convolution evaluated with two fast tape procedures, then bound error and cost (on [Integer multiplication in O(n (lg n)^{1−κ})](main-theorem.md))
- Two equal-width address chunks of $u$ digits in an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.; how: build a fixed linear network that exchanges two banks with restored scratch, label its edges so that edge matrices have small total rank, and recurse on smaller interchanges (on [Fast interchange of address chunks](chunk-interchange.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.1a). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.1a**: Each wire's stored array is $D_vg$ for the logical array $g$, with the frame $D_v$ invertible and shared by all incidences of a gate.
Source: "We call $D_v$ its frame: the stored" (paper)
> The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Elementary stream operations and controlled shifts](elementary-streams.md): Linear-time tape scans: swapping or moving a digit, splitting into streams and merging, and updating a field by an offset computed from earlier fields.
  Shown as: Linear network with roles, frames and restored scratch *<predicate>* Elementary stream operations and controlled shifts

## Pages that build on this one

- Restoring scratch values (transparent computation): The schedule subtracts old scratch contributions, performs the operation, and undoes it so arbitrary initial auxiliary values cancel.
- Three-element subsets and nested subspace labels: Indicator vectors of 3-subsets of [h] have intersection-count inner products; orthogonality gives nested nondegenerate subspaces whose dimension drops (orthogonal residuals) count the smaller operations on an edge.
- Total smaller calls below W m: In the finite network the edges need s<Wm smaller calls in total, so a recursive call at parameter m·f uses s calls at parameter f on volume V/W, whose per-volume cost grows by s/W<m, giving a power saving.
- Lower-triangular factorization and address shear: Every rational matrix factors as E1 Π E2 with lower triangular E1,E2 and a partial permutation of rank-many ones; so an edge matrix of rank a costs a smaller interchanges, and the shear (H,D)→(H+D,D) is done in tape order.
- Phase kernel C and complex network: The kernel C=H S H=aI+bX with C²=X and H₀=b S C S lets the complex network's frame changes be products of translation kernels on binary subspaces, over Gaussian dyadic numbers.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture and history](nlogn-conjecture.md)
- [Established O(n log n) multiplier as a subroutine](harvey-hoeven-multiplier.md)
- [Fixed-tape machine model and cost of scans](fixed-tape-model.md)
- [Restoring scratch values (transparent computation)](transparent-restoration.md)
- [Three-element subsets and nested subspace labels](triple-subspace-labels.md)
- [Total smaller calls below W m](rank-saving.md)
- [Lower-triangular factorization and address shear](bruhat-shear.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly H₀](butterfly.md)
- [Phase kernel C and complex network](phase-frames.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as convolution of radix digits](radix-digit-convolution.md)
- [Chinese-remainder address map to prime cyclic axes](crt-prime-axes.md)
- [Chirp identity and permutation cancellation](bluestein-chirp.md)
- [Coefficient twist to the negacyclic ring](coefficient-twist.md)
- [Fixed-point grids, contractions and error](fixed-point-contraction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Precision, rounding and carries](exact-recovery.md)
- [Signed packing of polynomial records](signed-packing.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Resampling with the permutations left in the transform](retained-permutations.md)
- [Parameter choice and cost table](parameter-choice.md)
- [The multiplication algorithm pipeline](multiplication-algorithm.md)
- [Integer multiplication in O(n (lg n)^{1−κ})](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "A wire's fixed place in the network is called its role." (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.

- "We call $D_v$ its frame" (paper)

  > The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.


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

Write the body to `exegenius/tasks/0008-write-linear-network.answer.md` and the JSON to `exegenius/tasks/0008-write-linear-network.answer.json`, then run `exegenius submit 0008-write-linear-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0008-write-linear-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
