# exegenius task 0017-write-linear-network-frames

Project directory: `/home/user/openai-nlogn-wiki/runs/A5` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who has studied algorithms and data structures (divide and conquer, recurrences, sorting, basic complexity), discrete mathematics (modular arithmetic, primes, binary representation, sets, permutations, induction), and linear algebra (vector spaces, subspaces, dimension, rank, invertible matrices, Gaussian elimination, triangular matrices) at an introductory level. They know the basics of Fourier analysis and probability/real analysis only as far as complex numbers and elementary calculus. They have not studied algebraic number theory, advanced finite-field theory, Lie groups or specialist FFT/multiplication literature.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Multiplication history and the n log n conjecture
- Convolution and multiplication
- Discrete Fourier transform
- FFT and two-point butterflies
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (ring size): The number of coefficients in a polynomial record, a power of two.
- Synthetic polynomial transforms
- Signed packing (Kronecker substitution)
- Prime cyclic axes and the Chinese remainder map
- Gaussian resampling
- Bluestein chirp identity
- Last-coordinate phase twist
- Fixed-point precision and exact recovery
- Tape arrays, scans and elementary streams
- Recurrences and divide and conquer (also: recursion, master theorem, recurrence relation)
- Modular arithmetic (also: congruences, mod n, remainders)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd)
- Chinese remainder theorem (also: CRT)
- Binary representation and bit operations (also: bits, base-2 expansion, bit fields, XOR, exclusive or, carries)
- Radix (base) expansion (also: digits in base B, positional notation, splitting into digits)
- Permutations (also: bijections of a finite set, reordering, sorting network)
- Vector spaces, subspaces and dimension (also: linear subspace, span, basis, linear independence)
- Finite field F_2 (also: GF(2), binary field, integers mod 2)
- Matrices, rank and invertibility (also: linear maps, matrix product, invertible matrix, rank of a matrix, identity matrix)
- Gaussian elimination (also: row reduction, triangular matrix, lower-triangular, upper-triangular)
- Cartesian product of sets (also: product set, multi-index, tuples, multidimensional array)
- Cyclic groups and roots of unity (also: Z/nZ, cyclic shift, primitive root of unity, n-th roots of unity, Euler's formula)
- Real and complex analysis basics (also: absolute value, modulus, norm, triangle inequality, Gaussian function, exponential)
- Rounding, floor and ceiling (also: floor, ceiling, nearest integer, truncation)
- Logarithms and exponents (also: lg, log base 2, binary logarithm, iterated logarithm, powers of two)
- Schoolbook multiplication and Karatsuba (also: long multiplication, quadratic multiplication, Karatsuba algorithm)
- Sorting and merging (also: sort, merge sort, sorting on tapes)
- Pigeonhole principle and counting arguments (also: union bound, counting subsets, binomial coefficients, combinatorics)
- Lower and upper bound asymptotics (also: Theta notation, little-o, Omega notation, asymptotic)
- Constants and parameters in complexity bounds (also: fixed constant, polylogarithmic, sub-logarithmic factor)

## This page

Concept: Linear networks, roles and frames
Gloss: A fixed linear network exchanges banks of values with signs and restores auxiliary values; rows are spread over roles and each vertex stores D_v g in an invertible linear frame so intermediate frames cancel.

## This page in the argument

The step: Both procedures arise from a fixed linear network on $W$ roles with frames, whose finite construction gives $s<Wm$ smaller calls, so recursion yields a power saving.
How: build each procedure from a fixed linear network with frames and recurse on smaller calls
Why: A single network design serves both bit and numerical procedures, and its call count drives the recurrence. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Each vertex stores $D_vg$ in an invertible linear frame, and intermediate frames cancel along any route.
- The bit network's endpoint operator is the address shear $(H,D)\mapsto(H+D,D)$ on address fields. (on [Address shear and triangular factorization](matrix-shear.md))
- Nested subspaces from three-element subset intersections give a network with $s<Wm$ smaller calls. (on [Finite networks from three-element subsets](finite-subset-networks.md))
- A call at parameter $mf$ made of $s$ calls at parameter $f$ on volume $V/W$ raises normalized cost by $s/W<m$ per factor $m$, giving a power saving. (on [Recursive power saving](recursive-saving.md))

It serves these steps, from the main result down:

- A deterministic fixed-tape machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time, $\kappa=2^{-182}$.; how: reduce multiplication through a chain of representation changes down to ring convolution, using the fast tape procedures, then recover the product (on [Integer multiplication in O(n (lg n)^(1−κ)) time](target.md))
- Two fast tape procedures, an address-field interchange and a simultaneous butterfly layer, cut the movement and arithmetic costs of the transform levels below $\Theta(n\log n)$ in stored volume $V$.; how: supply two tape procedures with sublinear overhead exponents and justify them from one network

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3.1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3.1**: Each vertex stores $D_vg$ in an invertible linear frame, and intermediate frames cancel along any route.
Source: "At a source, gate, or sink $v$, choose an invertible linear operator" (paper)
> The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.3.2 (on [Address shear and triangular factorization](matrix-shear.md)): The bit network's endpoint operator is the address shear $(H,D)\mapsto(H+D,D)$ on address fields.
- S2.3.3 (on [Finite networks from three-element subsets](finite-subset-networks.md)): Nested subspaces from three-element subset intersections give a network with $s<Wm$ smaller calls.
- S2.3.4 (on [Recursive power saving](recursive-saving.md)): A call at parameter $mf$ made of $s$ calls at parameter $f$ on volume $V/W$ raises normalized cost by $s/W<m$ per factor $m$, giving a power saving.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Tape arrays, scans and elementary streams](tape-streams.md): Arrays stored in address order on tapes with scans, controlled shifts and fixed rational scalings costing linear time.
  Shown as: Linear networks, roles and frames *<predicate>* Tape arrays, scans and elementary streams

## Pages that build on this one

- Simultaneous butterfly layer: Applying H0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on the same selected bit of up to d address chunks, in O(V d^λ') time with λ'<1.
- Fast interchange of address fields: Swapping two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) time, τ<1, using intermediate XOR combinations that end in an exact permutation.
- Finite networks from three-element subsets: Fixed networks with nested subspaces of an m-dimensional space built from three-element subset intersections, giving s<Wm smaller calls.

## Other pages you may link to

- [Multiplication history and the n log n conjecture](nlogn-conjecture.md)
- [Convolution and multiplication](convolution.md)
- [Discrete Fourier transform](dft.md)
- [Polynomial ring modulo y^r + 1](poly-ring-mod.md)
- [FFT and two-point butterflies](butterfly-fft.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Prime cyclic axes and the Chinese remainder map](multidim-crt.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Address shear and triangular factorization](matrix-shear.md)
- [Fast interchange of address fields](address-interchange.md)
- [Finite networks from three-element subsets](finite-subset-networks.md)
- [Recursive power saving](recursive-saving.md)
- [Resampling with permutations retained in the transform](retained-permutations.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](target.md)

## Evidence from the sources, with the paragraph around each quote

- "We call $D_v$ its frame" (paper)

  > The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.

- "A wire's fixed place in the network is called its role." (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.


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

Write the body to `exegenius/tasks/0017-write-linear-network-frames.answer.md` and the JSON to `exegenius/tasks/0017-write-linear-network-frames.answer.json`, then run `exegenius submit 0017-write-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.
