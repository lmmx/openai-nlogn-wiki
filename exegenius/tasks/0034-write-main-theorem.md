# exegenius task 0034-write-main-theorem

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Open with one or two sentences that say what the concept is and what it is for on the way to the target (the step of the argument it presents, and the pages that build on it, are listed below), so a reader arriving from a link knows at once why the page matters.
- If the page presents a step of the argument, explain how its method shows its claim. Give the reader every motivation the task marks as not stated by the sources: the sources will not.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, say in a sentence what this page uses it for, and give that sentence as a relation: the prerequisite's id, a predicate, and the sentence copied exactly. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject and the prerequisite as object: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". If the sentence says "the transforms are reduced by X", the predicate is "reduces its transforms by", not "are reduced to". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"); the sentence must link or name the prerequisite. Pick the predicate that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources: read the parts you need (search for the evidence quotes). State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Back each specific claim taken from a source (a result, a constant, a construction step) with the source text it rests on, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them. Submit rejects text not found in the named source. Do not cite common background.
- Be concrete and specific. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Chinese-remainder map (also: Agarwal–Cooley map)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Prime source lengths
- Transform identity with retained permutations
- Carry propagation
- Exact coefficient recovery

## This page

Concept: Integer multiplication below n log n
Gloss: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
Also called: Theorem 1

## This page in the argument

The step: Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one fixed fixed-tape machine, with $\kappa = 2^{-182}$.
How: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and check that the output is exact
Why: The fixed-tape bound needs cheap address rearrangements and transform layers, so the argument replaces the costly steps by linear combinations of intermediate data. (the sources say so: "The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers" (paper))
Striking feature: A strict power saving in the logarithmic factor, valid for every input length. (explain why it holds, from the method)

Its sub-steps, in order:

- Exact multiplication reduces to a convolution of short integer coefficients obtained by splitting each input into radix digits. (on [Radix-digit convolution](radix-digit-convolution.md))
- The Fourier transforms in the convolution are replaced by multidimensional transforms whose axis lengths are powers of two. (on [Gaussian resampling](gaussian-resampling.md))
- One coordinate of the array is stored as the coefficient list of a polynomial modulo $y^r + 1$. (on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md))
- The transforms are synthetic polynomial transforms whose roots of unity are powers of the polynomial variable. (on [Synthetic polynomial transforms](synthetic-transforms.md))
- Two disjoint address fields of $u$ bits can be interchanged in time that grows more slowly than linearly in $u$. (on [Address-field interchange](address-interchange.md))
- A butterfly layer on the selected bits of several axes is applied at once, in a single pass. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values. (on [Linear networks and frames](linear-network-frames.md))
- A linear network on three-element subsets exchanges two banks of values and restores its scratch wires. (on [Subset-intersection network](subset-intersection-network.md))
- The number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a power. (on [Rank-saving recursion](rank-saving-recursion.md))
- The radix-digit coefficients are placed on distinct prime cyclic axes by a map that preserves convolution. (on [Chinese-remainder map](chinese-remainder-map.md))
- The source and target coordinate permutations stay inside the transform identity and are not executed as sorts. (on [Transform identity with retained permutations](transform-identity.md))
- The middle transform, including its target permutation, becomes a normalized cyclic convolution. (on [Bluestein's chirp identity](bluestein-chirp-identity.md))
- A phase twist turns the last cyclic coordinate into a coordinate of a polynomial ring. (on [Phase twist](phase-twist.md))
- Convolution on the remaining axes over the polynomial ring is computed with synthetic transforms, a pointwise product, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))
- The recovered coefficient error is below one half, so rounding returns the exact integer coefficients. (on [Exact coefficient recovery](recovery-and-error.md))
- Carries across the radix digits turn the recovered coefficients into the exact binary product. (on [Carry propagation](carry-propagation.md))
- The parameters are chosen so that every term in the cost table fits the bound of the theorem.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture](n-log-n-conjecture.md): The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
  Shown as: Integer multiplication below n log n *<predicate>* The n log n optimality conjecture
- [Fixed-tape machine model](fixed-tape-model.md): A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
  Shown as: Integer multiplication below n log n *<predicate>* Fixed-tape machine model
- [Radix-digit convolution](radix-digit-convolution.md): Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
  Shown as: Integer multiplication below n log n *<predicate>* Radix-digit convolution
- [Chinese-remainder map](chinese-remainder-map.md): A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
  Shown as: Integer multiplication below n log n *<predicate>* Chinese-remainder map
- [Rank-saving recursion](rank-saving-recursion.md): The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
  Shown as: Integer multiplication below n log n *<predicate>* Rank-saving recursion
- [Transform layout](transform-layout.md): A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
  Shown as: Integer multiplication below n log n *<predicate>* Transform layout
- [Transform identity with retained permutations](transform-identity.md): The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
  Shown as: Integer multiplication below n log n *<predicate>* Transform identity with retained permutations
- [Prime source lengths](prime-source-lengths.md): Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
  Shown as: Integer multiplication below n log n *<predicate>* Prime source lengths
- [Phase twist](phase-twist.md): A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
  Shown as: Integer multiplication below n log n *<predicate>* Phase twist
- [Convolution over the polynomial ring](polynomial-ring-convolution.md): The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
  Shown as: Integer multiplication below n log n *<predicate>* Convolution over the polynomial ring
- [Packed selected-bit addition](packed-bit-addition.md): An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
  Shown as: Integer multiplication below n log n *<predicate>* Packed selected-bit addition
- [Exact coefficient recovery](recovery-and-error.md): The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
  Shown as: Integer multiplication below n log n *<predicate>* Exact coefficient recovery
- [Carry propagation](carry-propagation.md): Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
  Shown as: Integer multiplication below n log n *<predicate>* Carry propagation

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)

## Evidence from the sources

- "There is one deterministic Turing machine A" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
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

Write the body to `exegenius/tasks/0034-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0034-write-main-theorem.answer.json`, then run `exegenius submit 0034-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
