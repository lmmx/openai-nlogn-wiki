# exegenius task 0154-write-subspace-labels

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model, fixed-tape machine)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange)
- Address shear
- Gaussian dyadics
- Mathematical induction (also: induction, proof by induction, inductive proof)
- Logarithms and floor and ceiling functions (also: floor function, ceiling function, integer part, log base 2, lg)
- Binary representation of integers (also: binary string, bit string, base-2 representation, binary digits, bits)
- Dyadic rationals (also: binary fractions, dyadic numbers)
- Modular arithmetic (also: congruence modulo m, residues modulo m, integers modulo m, remainder arithmetic)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclidean algorithm)
- Prime numbers (also: primes, primality, prime factorization)
- Roots of unity (also: n-th roots of unity, primitive root of unity, unit roots, powers of a root of unity)
- Binary field F2 and XOR arithmetic (also: GF(2), field of two elements, mod-2 arithmetic, exclusive or, XOR, Boolean addition)
- Hamming weight (also: popcount, number of ones, weight of a binary vector, wt(x))
- Vector spaces and subspaces (also: linear subspace, span, basis, linear independence, dimension)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, transpose, identity matrix, linear transformation)
- Matrix rank (also: rank, rank of a linear map, column rank, row rank)
- Projection onto a subspace (also: projection matrix, idempotent linear map, orthogonal projection)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors, orthogonal complement)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum, characteristic polynomial)
- Bilinear form (also: bilinear space, nondegenerate form)

## This page

Concept: Subspace labels
Gloss: Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.

## Where the argument relies on this page

- A fixed linear network on three-element subsets exchanges two banks of scalars and restores every scratch wire. (on [Subset-intersection network](subset-intersection-network.md))
- The total number $s$ of smaller calls satisfies $s<Wm$. (on [Rank-saving recursion](rank-saving-recursion.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $a$ (real numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
- $b$ (imaginary numerator part), bound on [Gaussian dyadics](gaussian-dyadics.md): The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
- $k$ (denominator exponent), bound on [Gaussian dyadics](gaussian-dyadics.md): The non-negative integer exponent that sets the common denominator $2^k$.
- $H_0$ (two-point map), bound on [Gaussian dyadics](gaussian-dyadics.md): The map that sends a pair of coefficients $u$, $v$ to their halved sum and halved difference.
- $u$ (first coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The first coefficient of a pair on which the two-point map $H_0$ acts.
- $v$ (second coefficient), bound on [Gaussian dyadics](gaussian-dyadics.md): The second coefficient of a pair on which the two-point map $H_0$ acts.
- $u$ (field size), bound on [Fixed-tape machine model](fixed-tape-model.md): The number of cells in each of two disjoint fields, which counts the cells of a field.
- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two inputs, the common length of x and y.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary string input, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary string input, of length n.
- $\mathrm{val}$ (binary value function), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function mapping a binary string to the nonnegative integer whose binary digits it is, leftmost bit most significant.
- $z$ (integer to encode), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than 2^{2n} whose binary representation is taken.
- $\mathrm{bin}$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to a fixed number of bits.
- $V$ (stored volume), bound on [Address-field interchange](address-interchange.md): The number of bits the array stores.
- $u$ (field width), bound on [Address-field interchange](address-interchange.md): The number of bits in each address field.
- $\tau$ (cost exponent), bound on [Address-field interchange](address-interchange.md): A fixed constant less than 1 in the cost bound $O(V u^{\tau})$.
- $H$ (first address field), bound on [Address shear](address-shear.md): One of the two address fields, a vector of residues that the shear updates.
- $D$ (second address field), bound on [Address shear](address-shear.md): The other address field, a vector of residues that the shear leaves unchanged.
- $n$ (input length), bound on [Established O(n log n) multiplier](established-multiplier.md): The number of bits in each of the two binary input strings.
- $w$ (block width), bound on [Signed coefficient packing](signed-packing.md): The number of bits given to each coefficient in a packed integer.
- $f$ (polynomial), bound on [Signed coefficient packing](signed-packing.md): A polynomial with integer coefficients, packed into the integer $F$.
- $F$ (packed integer of f), bound on [Signed coefficient packing](signed-packing.md): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $g$ (second polynomial), bound on [Signed coefficient packing](signed-packing.md): A second polynomial with integer coefficients, packed into the integer $G$.
- $G$ (packed integer of g), bound on [Signed coefficient packing](signed-packing.md): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $h$ (product polynomial), bound on [Signed coefficient packing](signed-packing.md): The product $fg$ of the two polynomials, whose coefficients are recovered from the product $FG$.
- $U$ (ambient vector space), bound on [Bilinear form](bilinear-form.md): The vector space over F2 on which the bilinear form is defined.
- $B$ (bilinear form), bound on [Bilinear form](bilinear-form.md): The function that takes two vectors of U and returns a scalar, linear in each argument.
- $u$ (first vector), bound on [Bilinear form](bilinear-form.md): A vector of U, the first argument of the form.
- $v$ (second vector), bound on [Bilinear form](bilinear-form.md): A vector of U, the second argument of the form.
- $W$ (subspace), bound on [Bilinear form](bilinear-form.md): A subspace of U whose restricted form is tested for nondegeneracy.
- $u_1$ (first coordinate of u), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector u in the example.
- $u_2$ (second coordinate of u), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector u in the example.
- $v_1$ (first coordinate of v), bound on [Bilinear form](bilinear-form.md): The first coordinate of the vector v in the example.
- $v_2$ (second coordinate of v), bound on [Bilinear form](bilinear-form.md): The second coordinate of the vector v in the example.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Bilinear form](bilinear-form.md): A function of two vectors that is linear in each argument; a form is nondegenerate when no nonzero vector is orthogonal to every vector of the space.
  Shown as: Subspace labels *<predicate>* Bilinear form

## Pages that build on this one

- Subset-intersection network: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
- Complex phase network: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.

## Other pages you may link to

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Tensor product](tensor-product.md)
- [Complex phase network](complex-phase-network.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "A label is a nondegenerate subspace of a fixed bilinear" (paper)

  > The scalar network already has the required signed exchange. We now choose its intermediate labels to make the changes of frame inexpensive. A label is a nondegenerate subspace of a fixed bilinear space. On every edge one label will contain the other. For such an edge, the orthogonal residual is 13


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $U$ means label here, but ambient vector space on [Bilinear form](bilinear-form.md), which this page builds on: Subspace-labels page: U names a label (a nondegenerate subspace), not the ambient space of the bilinear form. Use another letter for the label, or state here that U is a label.

## Previous version (revise it)

It has 226 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 282 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Subspace labels are the intermediate subspaces that a [linear network](linear-network-frames.md) attaches to its wires, chosen so that each change of representation along a wire is cheap. They make the signed exchange of the scalar network affordable.

Subspace labels are based on the fixed bilinear space $F$, whose [bilinear form](bilinear-form.md) $\langle x,y\rangle$ is linear in each argument, where $x$ and $y$ are vectors of $F$. We assume $F$ is nondegenerate: no nonzero vector is orthogonal to every vector of $F$.

A label $U$ is a nondegenerate subspace of $F$, meaning $U\cap U^{\perp}=\{0\}$, where $U^{\perp}$ is the set of vectors orthogonal to every vector of $U$. Each wire carries one label at each stage of the network.

On every edge one label contains the other. For an edge with $U \subseteq V$, the labels $U$ and $V$ are its smaller and larger label. Its orthogonal residual is $R = V\cap U^{\perp}$, the orthogonal complement of the smaller label inside the larger one.

The residual's dimension is the change in label dimension across the edge. Since $U$ is nondegenerate and $F$ is nondegenerate, $F$ splits as $U$ plus $U^{\perp}$, with $U\cap U^{\perp}=\{0\}$ and $\dim U^{\perp}=\dim F-\dim U$ (standard linear algebra). For $v\in V$, write $v=u+w$ with $u\in U$ and $w\in U^{\perp}$. Since $U\subseteq V$, $w=v-u$ lies in $V$, so $w\in R$. Hence $V=U+R$ with $U\cap R=\{0\}$, and $\dim R=\dim V-\dim U$.

Small residuals mean that few dimensions change on each edge, so a change of frame touches little data.

Example. Take $F=\mathbb{C}^3$ with $\langle x,y\rangle=x_1y_1+x_2y_2+x_3y_3$. This form is nondegenerate, since $e_i\cdot e_j=\delta_{ij}$. Let $U=\operatorname{span}(e_1)\subseteq V=\operatorname{span}(e_1,e_2)$. Then $U^{\perp}=\operatorname{span}(e_2,e_3)$, so $R=V\cap U^{\perp}=\operatorname{span}(e_2)$, and $\dim R=1=\dim V-\dim U$.

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

Write the body to `exegenius/tasks/0154-write-subspace-labels.answer.md` and the JSON to `exegenius/tasks/0154-write-subspace-labels.answer.json`, then run `exegenius submit 0154-write-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.
