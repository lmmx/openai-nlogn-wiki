# exegenius task 0074-write-linear-network-frames

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
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Convolution
- Exclusive or (also: XOR)

## This page

Concept: Linear networks and frames
Gloss: A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
Also called: roles, frames

## This page in the argument

The step: Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values.
How: realise each procedure as a fixed linear network with frames on its wires
Why: Frames on the wires let a pointwise gate act on arrays without disturbing their representation. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- Each procedure arises from its own fixed linear network that exchanges two banks of values.

It serves these steps, from the main result down:

- Exact multiplication of two $n$-bit integers runs in $O(n(\lg n)^{1-\kappa})$ time on one deterministic fixed-tape machine, with $\kappa = 2^{-182}$.; how: reduce exact multiplication to radix-digit convolution, compute that convolution with fast tape transforms, and check that the output is exact (on [Integer multiplication below n log n](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear algebra basics](linear-algebra-basics.md): Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator.
  Shown as: Linear networks and frames *<predicate>* Linear algebra basics
- [Address field](address-field.md): A contiguous block of address bits of an array, which an address interchange exchanges with another block of the same width.
  Shown as: Linear networks and frames *<predicate>* Address field

## Pages that build on this one

- Endpoint operator: The operator that a network realises on each role's array once all intermediate frames have cancelled, so that it depends only on the endpoint frames.
- Gate and terminal of a network: A gate combines the values on the wires it touches by a fixed linear map, and a terminal is an input or output end of a wire where the network's values enter or leave.
- Address-field interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
- Subset-intersection network: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
- Address shear: The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.

## Other pages you may link to

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Exclusive or](xor.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources

- "Each procedure arises from its own fixed linear network that exchanges two banks of values" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t)." (D_v acts on whole arrays across addresses while G acts separately at each address. The page gives no argument that the identity holds for every invertible D_v, so the reader cannot check it.)
- The reader cannot follow this step: "The claim this page supports is that each tape procedure is such a network:" (The page states this claim but gives no construction or argument on this page that each tape procedure can be realised as such a network.)
- The reader cannot follow this step: "A route from an input wire $w$ to an output role $\rho(w)$ therefore applies" ('therefore' is not backed by a derivation here. The sentence before it, about the logical interpretation of the output being defined by the inverse input frame, has no clear antecedent for 'its', so the reader cannot check why the route applies D_sink(rho(w)) D_source(w)^{-1}.)
- Say what $t$ denotes where it is first used (for a size or count, what it counts): "G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t)." (The formula uses t as the number of gate inputs, but no sentence says what t denotes; the only sentence giving it a value is the example 'Take t = 2', which is an example use.)
- Say what $a$ denotes where it is first used (for a size or count, what it counts): "the gate $G(a, b) = a + b$ on arrays with two addresses" (a and b are the formal arguments of the example gate; the only sentence using them is an example, and nothing says what they denote.)
- Say what $b$ denotes where it is first used (for a size or count, what it counts): "the gate $G(a, b) = a + b$ on arrays with two addresses" (a and b are the formal arguments of the example gate; the only sentence using them is an example, and nothing says what they denote.)
- Say what $D_u$ denotes where it is first used (for a size or count, what it counts): "$D_v D_u^{-1}$ changes the stored array from $D_u g$ to $D_v g$" (D_u is an instance of the family D_v chosen at each vertex, but u is never introduced as a vertex or otherwise bound.)
- Say what $\rho$ denotes where it is first used (for a size or count, what it counts): "A route from an input wire $w$ to an output role $\rho(w)$" (The page never says what rho is: it is used as a map from input wires to output roles, but no sentence defines it.)
- Say what $\mathrm{source}$ denotes where it is first used (for a size or count, what it counts): "therefore applies $D_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to the array" (The prose says each wire runs from its source to its sink, but no sentence defines source(w) as a function of a wire, and the first mathematical use is here.)
- Say what $\mathrm{sink}$ denotes where it is first used (for a size or count, what it counts): "therefore applies $D_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to the array" (The prose says each wire runs from its source to its sink, but no sentence defines sink(.) as a function of a role, and the first mathematical use is here.)
- "linear algebra: invertible linear operator, matrix, inverse" is the concept [Linear algebra basics](linear-algebra-basics.md), now a prerequisite: link it where the term is used.
- Explain "scalar sign of a route" inline: its concept depends on this page, so it cannot be a prerequisite.
- Explain "bit procedure" inline: its concept depends on this page, so it cannot be a prerequisite.
- "address field" is the concept [Address field](address-field.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 569 words. Fix the problems by restructuring rather than appending: keep the rewrite within 711 words, a quarter more, unless a problem cannot be fixed without more. Pages that grow with every repair stop being self-contained explanations of one concept.

A linear network is a fixed wiring of linear gates that exchanges two banks of values and restores its scratch values. A frame is an invertible operator attached to a vertex of such a network, saying how the array on a wire is stored. Each tape procedure in the argument is realised as one such network acting on arrays, and frames are what let its gates act on those arrays without changing their representation.

Here a tape procedure is an operation that rearranges the contents of the tapes of a Turing machine. A scratch (auxiliary) wire is a wire that carries no input or output and whose value must be restored at the end.

The network is built from wires, gates and roles. A gate is a fixed linear map on a specified set of wires; untouched wires keep their values. <cite data-source="paper">A gate is a fixed linear map on a specified set of wires; untouched wires retain their values.</cite> Each wire runs from its source through the gates that touch it, in time order, to its sink. <cite data-source="paper">A wire’s fixed place in the network is called its role.</cite> A role names a position in the network, not the value currently sitting there.

The claim this page supports is that each tape procedure is such a network: <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value.</cite>

To run the network on arrays, replace each scalar by an array indexed by a common set of addresses, and apply each gate pointwise, meaning separately at each address. <cite data-source="paper">A scalar gate is then applied pointwise to matching addresses on the roles that it touches.</cite> Then, at each source, gate and sink $v$, choose an invertible linear operator $D_v$ on these arrays. Here $g$ is the logical array, the array a wire is meant to represent before any frame is applied. <cite data-source="paper">We call Dv its frame: the stored array is Dv g when the logical array is g.</cite> The stored array on a wire is therefore $D_v g$ at vertex $v$, and <cite data-source="paper">All incidences of one gate have the same frame.</cite>

A wire’s stored representation can change from one vertex to the next. <cite data-source="paper">Along an edge from u to v, the operator</cite> $D_v D_u^{-1}$ changes the stored array from $D_u g$ to $D_v g$, while the logical array $g$ stays the same.

Frames are what make the gates cheap. Write $G$ for a pointwise linear gate, which combines the entries of several wires at each address. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

So a gate that receives stored arrays in the common frame $D_v$ returns a stored array still in frame $D_v$. The gate never converts representations; changes of representation happen on edges.

Worked example. Take $t = 2$, the gate $G(a, b) = a + b$ on arrays with two addresses, and let $D_v$ be the matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ acting on column vectors. For logical arrays $g_1 = (1, 0)$ and $g_2 = (0, 1)$, the stored inputs are $D_v g_1 = (1, 0)$ and $D_v g_2 = (1, 1)$. The gate applied to the stored arrays gives $(2, 1)$. The logical sum is $g_1 + g_2 = (1, 1)$, and $D_v (1, 1) = (2, 1)$. The two computations agree, so the gate can run directly on the stored arrays.

Frames also fix the endpoints. <cite data-source="paper">The supplied input needs no preliminary change of frame</cite>: its logical interpretation is defined by applying the inverse input frame. A route from an input wire $w$ to an output role $\rho(w)$ therefore applies $D_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to the array, together with the scalar sign of that route. <cite data-source="paper">Thus the intermediate frames cancel</cite>, so only the endpoint frames remain. The scalar network carries the exchange of the two banks; the endpoint frames turn it into a fixed operator on the stored arrays.

For the bit procedure, the endpoint operator is a shear of two address fields, <cite data-source="paper">For the bit procedure, that endpoint operator is an address shear</cite>, which is the operation of the address shear page that builds on this one.

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

Write the body to `exegenius/tasks/0074-write-linear-network-frames.answer.md` and the JSON to `exegenius/tasks/0074-write-linear-network-frames.answer.json`, then run `exegenius submit 0074-write-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.
