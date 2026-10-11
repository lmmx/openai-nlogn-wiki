# exegenius task 0254-write-destination-rank

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
- Exact integer multiplication (also: exact multiplication)
- Convolution
- Running time cost (also: cost, linear-cost update, bit-complexity bound)
- Stable radix sort (also: label-and-sort operations)
- Payload (also: record)
- Schoolbook multiplication (also: the paper's construction)
- Truncation
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Bijection
- Permutation
- Mathematical induction (also: induction)
- Integer
- Prime number (also: prime)
- Ring
- Pointwise product
- Root of unity (also: roots of unity)
- Stream (also: fixed track, scan, role stream, stream position)
- Schönhage–Strassen multiplication (also: Schönhage and Strassen, Schönhage–Strassen bound)

## This page

Concept: Destination rank
Gloss: The position a record takes in the final order after a move, given by its rank among the records in that order.
Also called: prefix-slot move, move, extracted records, rectangular routine, hole, destination key

## Where the argument relies on this page

- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform, with the source and target coordinate permutations kept in the transform identity. (on [Transform identity with retained permutations](transform-identity.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first input, a binary string of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second input, a binary string of length n.
- $\mathrm{val}$ (binary value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed length k.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than $2^k$, which is written in binary by the padded representation.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol that marks where the first input ends and the second begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first input sequence, of length n.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second input sequence, of length n.
- $n$ (sequence length), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $k$ (output position), bound on [Convolution](convolution.md): The position of an entry of the output sequence c.
- $i$ (input position in a), bound on [Convolution](convolution.md): The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on [Convolution](convolution.md): The position of an entry of b in a product a_i b_j.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of a and b, a sequence of length 2n-1.
- $p$ (fractional precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $Q_p$ (truncation to precision p), bound on [Truncation](truncation.md): The operator that truncates each real and imaginary coefficient part of an array toward zero to the grid $2^{-p}\mathbb{Z}$.
- $z$ (input array), bound on [Truncation](truncation.md): An array of complex coefficients that is truncated by $Q_p$.
- $w$ (key width), bound on [Stable radix sort](stable-radix-sort.md): The number of bits in each key.
- $M$ (record count), bound on [Stable radix sort](stable-radix-sort.md): The number of records being sorted.
- $k$ (key), bound on [Stable radix sort](stable-radix-sort.md): The key of a record, written as a string of $w$ bits.
- $i$ (bit index), bound on [Stable radix sort](stable-radix-sort.md): The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Stable radix sort](stable-radix-sort.md): Sorting by successive passes over key digits from least to most significant, each pass stable so that equal keys keep their earlier order.
  Shown as: Destination rank *<predicate>* Stable radix sort
- [Stream](stream.md): A sequence of records that a procedure reads or writes in order, one position at a time, on a tape.
  Shown as: Destination rank *<predicate>* Stream

## Pages that build on this one

- Cost table: The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time.
- Packed selected-bit addition: An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.

## Other pages you may link to

- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Integer](integer.md)
- [Ring](ring.md)
- [Root of unity](root-of-unity.md)
- [Prime number](prime-number.md)
- [Pointwise product](pointwise-product.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Convolution](convolution.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Mathematical induction](mathematical-induction.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Little-o notation](little-o-notation.md)
- [Coprime](coprime.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Address](address.md)
- [Address field](address-field.md)
- [Cyclic shift](cyclic-shift.md)
- [Array](array.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Eigenvalue](eigenvalue.md)
- [Indicator vector](indicator-vector.md)
- [Matrix rank](matrix-rank.md)
- [Phase factor](phase-factor.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Gaussian integer](gaussian-integer.md)
- [Two-point kernel](two-point-kernel.md)
- [Tensor product](tensor-product.md)
- [Bilinear map](bilinear-map.md)
- [Ceiling function](ceiling-function.md)
- [Carry propagation](carry-propagation.md)
- [Grid numerator](grid-numerator.md)
- [Congruence](congruence-modulo.md)
- [Binary field](binary-field.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Centered residue](centered-residue.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bézout's identity](bezout-identity.md)
- [Big-Theta notation](big-theta-notation.md)
- [Cyclic group](cyclic-group.md)
- [Modular inverse](modular-inverse.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Extended real numbers](extended-reals.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Family parameter](family-parameter.md)
- [Frequency domain](frequency-domain.md)
- [Opposite transform](opposite-transform.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Padded transform box](padded-transform-box.md)
- [Logical bit volume](logical-bit-volume.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Normalization scales](normalization-scales.md)
- [Independence of events](independence.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Bit construction](bit-construction.md)
- [Complex phase network](complex-phase-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Tape procedure](tape-procedure.md)
- [Exclusive or](xor.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Complex construction](complex-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Supremum](supremum.md)
- [Linear contraction](linear-contraction.md)
- [Guard-width bound](guard-width-bound.md)
- [Union bound](union-bound.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "Attach this destination rank, padded to" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The destination rank follows from the current rank by a signed sum over the chunks:" (The reader cannot check that the rank changes additively, by sigma_h per unit change in chunk h, from what the page gives; the page only asserts the sum.)
- The reader cannot follow this step: "as for chunks with 4 and 3 values" (The page does not explain how the strides 1, 4 and 12 follow from the chunk sizes 4 and 3, so the example values cannot be checked.)
- The reader cannot follow this step: "the destination ranks are distinct and are exactly the ranks of the marked holes" (The claim depends on the move permuting the exceptional addresses and on how holes are marked, neither of which the page explains, so the reader cannot check it.)
- The reader cannot follow this step: "Sorting the records by destination rank therefore puts each record into its own hole." (This follows only from the unexplained distinctness and marking claims, so the reader cannot check it from the page.)
- The reader cannot follow this step: "The sort runs one pass per bit of the key" (The page asserts the number of passes and their link to the width of the rank without showing how the cost bound follows.)
- Say what $a_1$ denotes where it is first used (for a size or count, what it counts): "the rank of $(a_1, a_2, a_3)$" (The example uses a_1 as a coordinate of a generic address, but nothing on the page or in the known concepts says what a_1 denotes.)
- Say what $a_2$ denotes where it is first used (for a size or count, what it counts): "the rank of $(a_1, a_2, a_3)$" (The example uses a_2 as a coordinate of a generic address, but nothing on the page or in the known concepts says what a_2 denotes.)
- Say what $a_3$ denotes where it is first used (for a size or count, what it counts): "the rank of $(a_1, a_2, a_3)$" (The example uses a_3 as a coordinate of a generic address, but nothing on the page or in the known concepts says what a_3 denotes.)
- "stream" is the concept [Stream](stream.md), now a prerequisite: link it where the term is used.
- Explain "exceptional addresses" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

It has 443 words. Fix the problems by restructuring rather than appending: keep the rewrite within 553 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A destination rank is the position a record takes in the final order after a move, given by its rank among the records in that order. It is the key that lets displaced records return to their places in one pass over the stream.

Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md).

Each record is stored at an address made of three chunks, named $1$, $2$ and $3$ on this page. Let $q$ be the address of a record before the move, and let $q'$ be its address after the move.

The position of the record at $q$ among the records in stream order is its rank, written $\operatorname{rank}(q)$. A counter that moves through the stream computes it: <cite data-source="paper">scan the stream with a record-rank counter</cite>.

For chunk $h \in \{1,2,3\}$, let $q_h$ and $q'_h$ be the current and destination values of chunk $h$, and let $\sigma_h$ be the record stride of chunk $h$, the amount by which the rank changes when chunk $h$ rises by one with the other chunks fixed.

The destination rank follows from the current rank by a signed sum over the chunks: <cite data-source="paper">the fixed spectator coordinates give</cite>

$$\operatorname{rank}(q') = \operatorname{rank}(q) + \sum_{h=1}^{3} (q'_h - q_h)\,\sigma_h.$$

<cite data-source="paper">The differences are signed.</cite> A chunk can therefore lower the rank as well as raise it.

For example, take strides $\sigma_1 = 1$, $\sigma_2 = 4$ and $\sigma_3 = 12$, as for chunks with 4 and 3 values. In this example the rank of $(a_1, a_2, a_3)$ is $a_1 \cdot 1 + a_2 \cdot 4 + a_3 \cdot 12$. The record at $q = (1, 2, 0)$ has rank $1 \cdot 1 + 2 \cdot 4 = 9$, and its destination is $q' = (3, 0, 1)$. The formula gives $\operatorname{rank}(q') = 9 + (3-1)\cdot 1 + (0-2)\cdot 4 + (1-0)\cdot 12 = 15$, which agrees with the direct count $3 \cdot 1 + 0 \cdot 4 + 1 \cdot 12 = 15$.

Here $M$ is the number of records in the stream, and $A_{\mathrm{rect}}$ is a bit-size bound for the integers the rectangular routine handles. <cite data-source="paper">All involved integers have O(Arect ) bits</cite>.

The algorithm attaches this destination rank, padded to $\lceil \log_2 M \rceil \le A_{\mathrm{rect}}$ bits, to each extracted record.

Each extracted record also marks its hole, the position it returns to, on a fixed track of the stream: <cite data-source="paper">mark its hole on a fixed track of the full stream</cite>. Since the move permutes the exceptional addresses, the destination ranks are distinct and are exactly the ranks of the marked holes: <cite data-source="paper">these keys are distinct and are exactly the ranks of the marked</cite>. Sorting the records by destination rank therefore puts each record into its own hole. <cite data-source="paper">One forward full-stream scan reinserts the sorted records.</cite>

The sort runs one pass per bit of the key, and <cite data-source="paper">the at most Arect radix passes</cite> bound how many passes there are, so the width of the rank sets the number of passes in the cost bound.

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

Write the body to `exegenius/tasks/0254-write-destination-rank.answer.md` and the JSON to `exegenius/tasks/0254-write-destination-rank.answer.json`, then run `exegenius submit 0254-write-destination-rank` in the project directory. If submit rejects the answer, fix the answer and submit again.
