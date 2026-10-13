# exegenius task 0007-write-tape-layout-streams

Project directory: `/home/user/openai-nlogn-wiki/runs/D1` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic analysis, basic algorithm design (divide and conquer, recurrences, the idea of FFT-style multiplication at the level of knowing it exists), discrete math (modular arithmetic, primes, gcd, binary representation), and linear algebra (vectors, matrices, subspaces, rank, dimension, invertibility). They know complex numbers and polynomials, and basic multitape Turing machines. They have not studied the specialist material of the paper: Harvey-van der Hoeven machinery, Gaussian resampling, Bluestein, Chinese-remainder multidimensional reindexing, Bruhat factorization, or precise fixed-point error analysis.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Convolution and cyclic convolution
- Integer product as radix-digit convolution
- Known O(n log n) multiplier and the n log n conjecture
- Linear algebra over a field (also: vector space, subspace, dimension, rank, linear map, invertible matrix, matrix product)
- Modular arithmetic (also: residues, congruence, mod, bmod, integers modulo m, residue ring)
- Primes, gcd and coprimality (also: greatest common divisor, gcd, distinct primes, relatively prime, prime factorization)
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, bit position, lg n, base-2 logarithm)
- Logarithms, floor and ceiling (also: log, lg, floor, ceiling, iterated logarithm)
- Permutations (also: bijection, sorting a permutation, permutation of indices, inverse permutation)
- Mixed-radix and positional digit expansion (also: digits in base b, radix representation, index as digit tuple, lexicographic order, multi-index)
- Multidimensional arrays and tensors (also: multi-dimensional array, tensor product of transforms, axes, separable transform)
- Elementary Gaussian integers and dyadic rationals (also: dyadic rational, power-of-two denominators, Gaussian integer, fixed-point number)
- Norms, error bounds and rounding (also: triangle inequality, absolute value bound, operator norm, contraction, rounding to nearest integer, truncation error)
- Schoolbook carry addition (also: carry propagation, long multiplication, grade-school multiplication, linear-time addition)
- Geometric series and recurrences (also: recursion tree, divide and conquer recurrence, master theorem, summing powers)
- Roots of unity and Euler's formula (also: e^{2 pi i/n}, primitive n-th root, unit circle)
- Basic finite-set combinatorics (also: subsets of size three, counting subsets, binomial coefficient, intersection counting, inclusion-exclusion)
- Deterministic algorithms and tape scans (also: linear scan, copying between tapes, sorting on tape, merging)

## This page

Concept: Address fields, streams and scans on tape
Gloss: Arrays stored in lexicographic address order on tape, with fields of address digits, processed by linear scans, controlled shifts and cyclic splitting into role streams.

## This page in the argument

The step: A multitape machine with fixed alphabet and tapes can do elementary scans, permutations of digit pairs and controlled shifts on arrays in lexicographic order in time linear in the volume.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Build two fast tape procedures (address interchange and simultaneous butterfly layers) with power savings, use them in synthetic transforms, and place those in the reduction of multiplication to convolution (on [Integer multiplication in O(n (lg n)^(1-κ))](main-result.md))

## Pages that build on this one

- Linear exchange networks with roles and frames: A fixed linear network exchanging two banks of values and restoring auxiliary values; applied to arrays via rows distributed over wire roles, with an invertible frame per gate so intermediate frames cancel.
- Address shear and triangular factorization: The endpoint operator (H,D) -> (H+D,D) on address fields, with matrix shears implemented through lower-triangular (Bruhat-type) factorization in tape order.
- Chinese-remainder map to prime cyclic axes: A reindexing of the coefficient list onto a product of cyclic axes of distinct prime lengths that preserves convolution, giving a multidimensional convolution.
- Synthetic polynomial transforms: Fourier transforms over the ring modulo y^r+1 using powers of y as roots, computed by signed shifts and butterflies and retaining one stored frequency order for the inverse.
- Packed selected-bit addition: Adding (XOR) selected bit positions at positions rho+iK of grouped address chunks in one packed pass, the primitive behind changing address bits in the butterfly layer.

## Other pages you may link to

- [Known O(n log n) multiplier and the n log n conjecture](nlogn-multiplier.md)
- [Convolution and cyclic convolution](convolution.md)
- [Integer product as radix-digit convolution](radix-digit-reduction.md)
- [Fixed-point Gaussian dyadic records](fixed-point-dyadic.md)
- [Linear exchange networks with roles and frames](linear-network-frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Three-element-subset subspace construction](subset-intersection-network.md)
- [Recursive rank saving gives a power saving](recursive-power-saving.md)
- [Fast address-field interchange costing O(V u^τ)](address-interchange.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Discrete Fourier transform and roots of unity](dft.md)
- [Polynomial ring modulo y^r+1](negacyclic-ring.md)
- [Two-point butterfly and fast transform levels](butterfly.md)
- [Synthetic polynomial transforms](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity and phase twist](bluestein-chirp.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Retaining permutations in the transform](permutation-cancellation.md)
- [Precision, rounding and carry recovery](precision-exact-recovery.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Simultaneous butterfly layer on selected bits](simultaneous-butterfly-layer.md)
- [Parameter choice and total cost accounting](parameter-cost-accounting.md)
- [Integer multiplication in O(n (lg n)^(1-κ))](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "A step reads and writes at most one cell on each
tape and moves each head by at most one cell." (paper)

  > A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. A step reads and writes at most one cell on each tape and moves each head by at most one cell. Fixed tracks and finitely many work tapes change time by a fixed factor. We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow. The latter permutation will be realized in Section~\ref{sec:tape-interchange} by computing XOR combinations of intermediate data streams. The present section supplies the elementary scans it uses. Every scan includes its counters and the return of its tape heads.

- "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$." (paper)

  > The first procedure interchanges two disjoint contiguous address fields of $u$ bits in an array whose addresses form a complete Cartesian product. Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$. Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data. The final permutation is exact for arbitrary initial auxiliary values.

- "Each of the following operations on an array of
volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes:" (paper)

  > \begin{lemma}[Elementary stream operations] \label{lem:elementary-streams} Fix a radix $q\ge2$. Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes: \begin{enumerate} \item any fixed permutation of the pair of digit values at two specified radix-$q$ positions, whether or not the positions are adjacent; \item moving one specified radix-$q$ digit to another position, preserving the order of the intervening positions; \item splitting on a specified radix-$q$ digit, applying a fixed pointwise map to aligned streams, and merging them back; \item for positive integers $P,R,B$, within each prefix of an array on $[P]\times[R]\times[B]$, splitting whole rows cyclically into a fixed number $W$ of streams, and, when $W$ divides $R$, merging those streams in any fixed order of the row classes. \end{enumerate} The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes. Their constants may depend on the fixed radix, the fixed pointwise map, and the fixed number of row classes. \end{lemma}

- "An update
\[
 y\longmapsto y+a(\text{controls})\pmod Q
\]
costs $O(V)$" (paper)

  > \begin{lemma}[Controlled shifts and fixed rational scalings] \label{lem:ordered-affine-streams} Fix a prime $q$, a fixed number of control fields, and finitely many rational coefficients whose denominators are prime to $q$. Whenever a coefficient is used as a unit, also require its numerator to be prime to $q$. Put $Q=q^b$, $b\ge1$. Suppose a target field $y\in[Q]$ follows its control fields, each control used in an offset having $O(b)$ digits. An update \[ y\longmapsto y+a(\text{controls})\pmod Q \] costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values. In particular, this holds for a fixed rational linear combination of them, specialized modulo $Q$. Multiplication of $y$ by any of the specified rational units, and its inverse, also costs $O(V)$. Arbitrarily long intervening spectator fields and suffix records are permitted. \end{lemma}


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

Write the body to `exegenius/tasks/0007-write-tape-layout-streams.answer.md` and the JSON to `exegenius/tasks/0007-write-tape-layout-streams.answer.json`, then run `exegenius submit 0007-write-tape-layout-streams` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0007-write-tape-layout-streams`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
