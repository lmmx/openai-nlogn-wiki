# exegenius task 0487-write-array-norm

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
- Little-o notation (also: limit as lambda tends to infinity)
- Payload (also: record)
- Truncation
- Address (also: binary addresses, least significant end)
- Array (also: disk array, disk-grid ring array)
- Logarithm (also: logarithm lg)
- Base-2 logarithm (also: logarithm and ceiling)
- Mathematical induction (also: induction)
- Integer
- Root of unity (also: roots of unity, primitive root of unity)
- Real numbers (also: Real number)

## This page

Concept: Array norm
Gloss: The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one.
Also called: norm of an array, coefficient bound, norm of a vector

## Where the argument relies on this page

- Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products. (on [Convolution over the polynomial ring](polynomial-ring-convolution.md))
- The recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients. (on [Exact coefficient recovery](recovery-and-error.md))

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
- $\lambda$ (evaluation point), bound on [Little-o notation](little-o-notation.md): The real point at which the functions are evaluated, taken to infinity.
- $\varphi$ (bounded function), bound on [Little-o notation](little-o-notation.md): The function being bounded.
- $\psi$ (comparison function), bound on [Little-o notation](little-o-notation.md): The comparison function, positive for all large $\lambda$.
- $A$ (multiplication machine), bound on [Little-o notation](little-o-notation.md): The deterministic Turing machine with a fixed number of tapes that multiplies two n-bit integers exactly.
- $\kappa$ (saving exponent), bound on [Little-o notation](little-o-notation.md): The fixed positive constant 2^{-182} in the saving exponent $1-\kappa$.
- $T_A$ (running time), bound on [Little-o notation](little-o-notation.md): The running time of machine A on inputs of length n.
- $C$ (constant factor), bound on [Little-o notation](little-o-notation.md): A constant factor in the big-O bound on $T_A(n)$.
- $c_A$ (conjecture constant), bound on [Little-o notation](little-o-notation.md): A positive constant in the conjectured lower bound for machine A.
- $N$ (entry count), bound on [Address](address.md): The number of entries in an array, which counts every stored entry once.
- $d$ (address length), bound on [Address](address.md): The number of bits in each address of an array.
- $\alpha$ (address), bound on [Address](address.md): A string of d bits that labels one entry of the array.
- $p$ (precision), bound on [Truncation](truncation.md): The number of fractional binary places kept, which sets the grid spacing to $2^{-p}$.
- $z$ (coefficient list), bound on [Truncation](truncation.md): A finite list of complex numbers, called coefficients.
- $Q_p$ (truncation map), bound on [Truncation](truncation.md): The map that truncates each real and imaginary part of each coefficient of a list toward zero to the grid $2^{-p}\mathbb{Z}$.
- $\|\cdot\|_\infty$ (maximum norm), bound on [Truncation](truncation.md): The largest complex modulus of any coefficient of a list.
- $H$ (layer), bound on [Truncation](truncation.md): The operation that applies a two-point map to each pair of entries whose addresses differ in one of several selected bits, in one pass.
- $\alpha$ (first paired value), bound on [Truncation](truncation.md): The first of the two values that the layer combines in each pair.
- $\beta$ (second paired value), bound on [Truncation](truncation.md): The second of the two values that the layer combines in each pair.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Array](array.md): A finite collection of entries, each stored at an address and carrying a payload.
  Shown as: Array norm *<predicate>* Array

## Pages that build on this one

- Supremum: The least upper bound of a set of real numbers.
- Bilinear map: A map that is linear in each of two vector arguments separately, such as the product of two polynomials.
- Neumann series: The series of powers of an operator with alternating signs, which inverts I plus a small operator when that operator has norm below one.
- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
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
- [Little-o notation](little-o-notation.md)
- [Address](address.md)
- [Truncation](truncation.md)
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

- "has norm at most one." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- [Array](array.md) is now a prerequisite: link it where "array" is used: "Let $X$ be a finite array of complex values"
- The reader cannot follow this step: "The source states that a disk array" (The sentence ends before saying what the source states, so the reader cannot tell what claim is being made or check it.)

## Previous version (revise it)

It has 248 words. Fix the problems by restructuring rather than appending: keep the rewrite within 310 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

The norm of an array is the largest modulus among its entries, so it measures the size of the worst entry. The [convolution over the polynomial ring](polynomial-ring-convolution.md) and the error bound of [exact coefficient recovery](recovery-and-error.md) are stated in this size measure.

Let $X$ be a finite array of complex values, and let $u$ range over its entries. The modulus of $u$ is its distance from $0$ in the complex plane: $|u| = \sqrt{\operatorname{Re}(u)^2 + \operatorname{Im}(u)^2}$. The norm of $X$, written $\|X\|$, is the largest modulus $|u|$ over all entries $u$ of $X$.

For example, let $X$ have the entries $0.6+0.8i$, $-0.3$ and $0.5i$. Their moduli are $1$, $0.3$ and $0.5$, so $\|X\|=1$. Replacing $-0.3$ by $1.2$ gives norm $1.2$.

An array is a disk array when every entry has modulus at most one, that is, lies in the closed unit disk of the complex plane. Since $\|X\|$ is the largest modulus, this holds exactly when $\|X\| \le 1$. The source states that a disk array <cite data-source="paper">has norm at most one.</cite>

The norm is extended to arrays over the [polynomial ring](polynomial-ring-mod-yr-plus-1.md). Here $y$ is the polynomial variable, $r$ is the number of coefficients in each representative, and the ring is the polynomials modulo $y^r + 1$. Each element $g$ of this ring is represented by $g = \sum_{t=0}^{r-1} g_t y^t$, where the coefficient index $t$ runs from $0$ to $r-1$. <cite data-source="paper">We always use representatives of degree less than r.</cite> The norm of $g$ is $\max_t |g_t|$. For an array over the ring, the norm is the maximum over all coefficients in all entries: <cite data-source="paper">the same notation denotes the maximum over all coefficients in all entries.</cite>

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

Write the body to `exegenius/tasks/0487-write-array-norm.answer.md` and the JSON to `exegenius/tasks/0487-write-array-norm.answer.json`, then run `exegenius submit 0487-write-array-norm` in the project directory. If submit rejects the answer, fix the answer and submit again.
