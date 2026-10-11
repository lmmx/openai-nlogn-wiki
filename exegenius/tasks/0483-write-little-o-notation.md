# exegenius task 0483-write-little-o-notation

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
- Exact integer multiplication (also: exact multiplication, Binary product)
- Convolution
- Running time cost (also: cost, linear-cost update, bit-complexity bound, linear tape time)
- Payload (also: record)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Mathematical induction (also: induction)
- Integer
- Root of unity (also: roots of unity, primitive root of unity)
- Real numbers (also: Real number)

## This page

Concept: Little-o notation
Gloss: A function f is o(g) when the ratio f/g tends to zero, a stronger statement than being O(g).
Also called: limit as lambda tends to infinity

## Where the argument relies on this page

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$. (on [Integer multiplication below n log n](main-theorem.md))
- The parameters can be chosen so that every term in the cost table is $O(n(\lg n)^{1-\kappa})$ for $\kappa = 2^{-182}$, which gives the bound of the theorem.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $b$ (base), bound on [Logarithm](logarithm.md): The fixed number, greater than 1, to which the logarithm is taken.
- $y$ (positive number), bound on [Logarithm](logarithm.md): The positive number whose logarithm to base $b$ is taken.
- $n$ (integer argument), bound on [Logarithm](logarithm.md): The positive integer whose base-2 logarithm $\lg n$ is taken.
- $n$ (argument), bound on [Base-2 logarithm](base-two-logarithm.md): A positive integer whose base-2 logarithm is taken.
- $\lg$ (base-2 logarithm), bound on [Base-2 logarithm](base-two-logarithm.md): The base-2 logarithm of $n$, the least integer $k$ with $2^k \ge n$, but at least 1.
- $z$ (complex number), bound on [Root of unity](root-of-unity.md): A complex number that is tested for being a root of unity.
- $m$ (order), bound on [Root of unity](root-of-unity.md): The order of $z$, the least positive integer with $z^m = 1$, which also counts the distinct powers of $z$.
- $y$ (polynomial variable), bound on [Root of unity](root-of-unity.md): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, which is a root of unity in that ring.
- $n$ (input length), bound on [Running time cost](running-time-cost.md): The number of cells holding an input, that is, the length of the input string.
- $A$ (machine), bound on [Running time cost](running-time-cost.md): The single machine whose running time the main theorem bounds.
- $\kappa$ (fixed exponent constant), bound on [Running time cost](running-time-cost.md): A fixed constant, equal to $2^{-182}$, that sets the exponent $1-\kappa$ in the running time bound.
- $T_A$ (running time cost), bound on [Running time cost](running-time-cost.md): The running time cost of machine A as a function of the input length n: the largest number of steps A takes on any input of that length.
- $M$ (scanning machine), bound on [Running time cost](running-time-cost.md): The example machine that reads cells from left to right and halts at the first cell holding 1 or at the last cell.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs $x$ and $y$.
- $\mathrm{val}$ (value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{val}(x)$ is the nonnegative integer value of a binary string $x$, with the leftmost bit most significant.
- $k$ (padded length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
- $z$ (padded integer), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer with $z < 2^k$ that is written in binary.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): $\mathrm{bin}_k(z)$ is the binary representation of $z$ padded on the left with zeros to length $k$.
- $\#$ (separator), bound on [Exact integer multiplication](exact-integer-multiplication.md): A separator symbol placed between $x$ and $y$ in the input, marking where $x$ ends and $y$ begins.
- $a$ (first input sequence), bound on [Convolution](convolution.md): The first input sequence, of length n.
- $b$ (second input sequence), bound on [Convolution](convolution.md): The second input sequence, of length n.
- $n$ (sequence length), bound on [Convolution](convolution.md): The number of entries in each input sequence.
- $m$ (output position), bound on [Convolution](convolution.md): The position of an output entry of the convolution.
- $i$ (first input position), bound on [Convolution](convolution.md): The position in a of the input entry that combines to an output entry.
- $j$ (second input position), bound on [Convolution](convolution.md): The position in b of the input entry that combines to an output entry.
- $c$ (convolution), bound on [Convolution](convolution.md): The convolution of a and b, a sequence of length 2n-1.
- $t$ (step index), bound on [Mathematical induction](mathematical-induction.md): The number of recursion levels passed, a nonnegative integer.
- $q$ (level ratio), bound on [Mathematical induction](mathematical-induction.md): The fixed positive real ratio by which one level may multiply a bound.
- $g_t$ (level bound), bound on [Mathematical induction](mathematical-induction.md): A bound on the cost after t levels.

## Pages that build on this one

- Guard-width bound: An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.
- Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.

## Other pages you may link to

- [Integer](integer.md)
- [Logarithm](logarithm.md)
- [Base-2 logarithm](base-two-logarithm.md)
- [Root of unity](root-of-unity.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [Convolution](convolution.md)
- [Payload](payload.md)
- [Mathematical induction](mathematical-induction.md)
- [Address](address.md)
- [Truncation](truncation.md)
- [Array](array.md)
- [Array norm](array-norm.md)
- [Ceiling function](ceiling-function.md)
- [Big-Theta notation](big-theta-notation.md)
- [Extended real numbers](extended-reals.md)
- [Supremum](supremum.md)
- [Telescoping identity](telescoping-identity.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Fixed-width digit blocks](fixed-width-digit-blocks.md)
- [Exceptional set](exceptional-set.md)
- [Big-Omega notation](big-omega-notation.md)
- [Bit-reversed index order](bit-reversed-order.md)
- [Directed graph](directed-graph.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Transform axis](transform-axis.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Linear contraction](linear-contraction.md)
- [Bilinear map](bilinear-map.md)
- [Coprime](coprime.md)
- [Bézout's identity](bezout-identity.md)
- [Cyclic group](cyclic-group.md)
- [Order of an element](order-of-element.md)
- [Diagonal scaling](diagonal-scaling.md)
- [Frequency domain](frequency-domain.md)
- [Projection along a subspace](projection-along-subspace.md)
- [Closed disk in the complex plane](complex-disk.md)
- [Linear functional](linear-functional.md)
- [Dual space](dual-space.md)
- [Floor function](floor-function.md)
- [Bijection](bijection.md)
- [Permutation](permutation.md)
- [Address field](address-field.md)
- [Linear networks and frames](linear-network-frames.md)
- [Logical array](logical-array.md)
- [Cyclic shift](cyclic-shift.md)
- [Butterfly](butterfly.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Incidence](incidence.md)
- [Tensor product](tensor-product.md)
- [Carry propagation](carry-propagation.md)
- [Congruence](congruence-modulo.md)
- [Schönhage–Strassen multiplication](schonhage-strassen.md)
- [Ring](ring.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Limit inferior](limit-inferior.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Binary field](binary-field.md)
- [Modular inverse](modular-inverse.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Bit network](bit-network.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Two-point kernel](two-point-kernel.md)
- [Gaussian integer](gaussian-integer.md)
- [Polynomial ring](polynomial-ring.md)
- [Grid numerator](grid-numerator.md)
- [Chinese remainder theorem](chinese-remainder-theorem.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Forward transform](forward-transform.md)
- [Pointwise product](pointwise-product.md)
- [Opposite transform](opposite-transform.md)
- [Iverson bracket](iverson-bracket.md)
- [Axis line](axis-line.md)
- [Near-linear time](near-linear-time.md)
- [Negacyclic convolution](negacyclic-convolution.md)
- [Neumann series](neumann-series.md)
- [Probability](probability.md)
- [Independence of events](independence.md)
- [Radix-two factorization](radix-two-factorization.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Standard basis vector](standard-basis-vector.md)
- [Matrix rank](matrix-rank.md)
- [Symmetric matrix](symmetric-matrix.md)
- [Eigenvalue](eigenvalue.md)
- [Bilinear form](bilinear-form.md)
- [Orthogonal complement](orthogonal-complement.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Exclusive or](xor.md)
- [Gram matrix](gram-matrix.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Numerical layer](numerical-layer.md)
- [Union bound](union-bound.md)
- [Transform round](transform-round.md)
- [Tape procedure](tape-procedure.md)
- [Stream](stream.md)
- [Bit procedure](bit-procedure.md)
- [Endpoint operator](endpoint-operator.md)
- [Address shear](address-shear.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Transform layout](transform-layout.md)
- [Padded transform box](padded-transform-box.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Prime number](prime-number.md)
- [Logical bit volume](logical-bit-volume.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Centered residue](centered-residue.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Normalization scales](normalization-scales.md)
- [Middle transform](middle-transform.md)
- [Phase twist](phase-twist.md)
- [Prime source lengths](prime-source-lengths.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Schedule](schedule.md)
- [Bit construction](bit-construction.md)
- [Complex construction](complex-construction.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Family parameter](family-parameter.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "γ = o(b). For example b ≥ 224 implies γ ≤ b/4." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The main result says that $A$, so its time is $O(n(\lg n)^{1-\kappa})$." (The page never names or links the main result and the sentence does not finish saying what it states, so the reader cannot check the O-bound on the running time of A from the page.)
- The reader cannot follow this step: "The paper states the saving as a limit too:" (The page refers to a limit stated in the paper, gives no formula after the colon, and does not link the paper, so the reader cannot check the claim.)
- Say what $c_A$ denotes where it is first used: the page uses it before saying so in "for a positive constant $c_A$ depending on $A$"

## Previous version (revise it)

It has 409 words. Fix the problems by restructuring rather than appending: keep the rewrite within 511 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

Little-o notation says that one function is negligible next to another. It states the integer multiplication result below $n\lg n$ as a strict saving, and so turns that saving into a refutation of the optimality conjecture.

The variable $\lambda$ is the real point at which both functions are evaluated, and it is taken to infinity. The function $\varphi$ is the one being bounded, and $\psi$ is the comparison function, positive for all large $\lambda$; both map the positive reals to the positive reals.

We write $\varphi(\lambda) = o(\psi(\lambda))$ as $\lambda \to \infty$ when the ratio tends to zero:

$$\lim_{\lambda \to \infty} \frac{\varphi(\lambda)}{\psi(\lambda)} = 0.$$

That is, for every positive number the ratio is below it for all sufficiently large $\lambda$. Taking that number to be $1$ shows that every $o(\psi)$ function is also $O(\psi)$: the ratio is eventually at most $1$, and since $\psi(\lambda) > 0$, $\varphi(\lambda) \le \psi(\lambda)$ for large $\lambda$. The converse fails. For example $2\lambda$ is $O(\lambda)$, yet $2\lambda/\lambda = 2$ never drops below $1$, so $2\lambda$ is not $o(\lambda)$.
The machine $A$ is one deterministic Turing machine with a fixed number of tapes that multiplies two $n$-bit integers exactly, where $n$ is the number of bits in each input. Here $\kappa = 2^{-182}$ is a fixed positive constant, and $\lg n$ is the [logarithm](logarithm.md) to base 2. The main result says that $A$ <cite data-source="paper">multiplies two n-bit integers in O(n(lg n)1−κ ) worstcase time, with κ = 2−182</cite>, so its time is $O(n(\lg n)^{1-\kappa})$.

Let $T_A(n)$ be the running time of $A$ on inputs of length $n$. The big-O bound gives a constant factor $C$ with $T_A(n) \le C\,n(\lg n)^{1-\kappa}$ for all sufficiently large $n$. Dividing by $n\lg n$ gives

$$\frac{T_A(n)}{n\lg n} \le C\,(\lg n)^{-\kappa} \qquad \text{for all sufficiently large } n.$$

Little-o notation bounds the cost of the [exact integer multiplication](exact-integer-multiplication.md) machine $A$ strictly below $n\lg n$: its running time is $o(n\lg n)$, not merely $O(n\lg n)$. As $n$ grows, $\lg n$ grows without bound. Then $(\lg n)^{\kappa}$ also grows without bound, since $\kappa > 0$, so $(\lg n)^{-\kappa} = 1/(\lg n)^{\kappa}$ tends to zero, and so does the ratio.

The optimality conjecture asserts that every exact multiplication machine $A$ satisfies $T_A(n) \ge c_A\, n\lg n$ for all sufficiently large $n$, for a positive constant $c_A$ depending on $A$. Dividing by $n\lg n$ keeps the ratio $T_A(n)/(n\lg n)$ at least $c_A$, yet that ratio tends to zero and is eventually below $c_A/2$, a contradiction. The conjecture fails for machine $A$. The paper states the saving as a limit too: <cite data-source="paper">The power saving proved here gives a limit of zero through all input lengths</cite>.

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

Write the body to `exegenius/tasks/0483-write-little-o-notation.answer.md` and the JSON to `exegenius/tasks/0483-write-little-o-notation.answer.json`, then run `exegenius submit 0483-write-little-o-notation` in the project directory. If submit rejects the answer, fix the answer and submit again.
