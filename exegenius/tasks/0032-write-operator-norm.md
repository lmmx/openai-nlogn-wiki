# exegenius task 0032-write-operator-norm

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
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree: discrete mathematics through modular arithmetic, primes, gcds and the Euclidean algorithm, and the binary (radix) representation of integers; a first course in linear algebra over the reals covering vector spaces, bases, dimension, matrices, rank and invertibility; and the basics of complex numbers and roots of unity. They have not studied finite fields beyond GF(2), bilinear forms, tensor products, rings beyond polynomials, or the fast Fourier transform as a specialist topic, so those are explained by the wiki.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution (also: convolution of two vectors)
- Positional (radix) representation of integers (also: binary representation, base-2 representation, radix-q digits, radix representation, binary string, bit string)
- Logarithm (also: base-2 logarithm, log2, lg)
- Modular arithmetic (also: congruence modulo m, residue arithmetic, integers modulo m, Z/mZ, mod m)
- Greatest common divisor and coprimality (also: gcd, highest common factor, coprime, relatively prime, pairwise coprime)
- Euclidean algorithm and modular inverses (also: extended Euclidean algorithm, Bezout coefficients, multiplicative inverse modulo m)
- Prime numbers (also: prime, distinct odd primes, prime factorization, primality)
- Roots of unity (also: q-th root of unity, primitive root of unity, root of unity, powers of a root of unity)
- Vector space, subspace, basis and dimension (also: linear subspace, span, linear independence, basis, dimension of a vector space, dim)
- Matrix, linear map, rank and invertibility (also: linear transformation, matrix of a linear map, rank of a matrix, invertible matrix, nonsingular matrix, inverse matrix, kernel, image)
- Dot product and orthogonality (also: inner product, standard inner product, orthogonal vectors, orthogonal complement, perpendicular)
- Field of two elements (also: GF(2), F_2, binary field, Z/2Z, mod 2 arithmetic, XOR as addition)

## This page

Concept: Operator norm
Gloss: The norm of a linear map L is the supremum of ‖Lu‖ over vectors u with ‖u‖ ≤ 1, where the vector norm of a complex vector is the largest modulus among its coordinates; a linear contraction is a linear map of norm at most one.
Also called: norm of a linear map, operator norm and maximum-modulus vector norm

## Where the argument relies on this page

- The maps $A=S'$ and $B_0=D'J'C$ are linear contractions, since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each of the two binary strings to be multiplied.
- $x$ (first input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first of the two binary strings to be multiplied, of length $n$.
- $y$ (second input string), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second of the two binary strings to be multiplied, of length $n$.
- $s$ (binary string), bound on [Exact integer multiplication](exact-integer-multiplication.md): A generic binary string whose integer value is taken by the function val.
- $\mathrm{val}$ (string value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $k$ (padded output length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
- $z$ (integer to represent), bound on [Exact integer multiplication](exact-integer-multiplication.md): A nonnegative integer less than $2^k$, whose binary representation is padded to length $k$.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer padded on the left with zeros to length $k$.
- $b$ (digit bit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of bits in one radix digit.
- $m$ (digit count), bound on [Radix-digit convolution](radix-digit-convolution.md): The number of digits in each integer.
- $u$ (first integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer whose i-th digit is u_i.
- $v$ (second integer), bound on [Radix-digit convolution](radix-digit-convolution.md): The integer whose i-th digit is v_i.
- $u_i$ (digit of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th digit of u, in the set $\{0,\dots,2^b-1\}$.
- $v_i$ (digit of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The i-th digit of v, in the set $\{0,\dots,2^b-1\}$.
- $i$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): An index of the digits of u and v, running from 0 to m-1.
- $l$ (digit index), bound on [Radix-digit convolution](radix-digit-convolution.md): A second index of the digits of u and v, running from 0 to m-1.
- $j$ (coefficient index), bound on [Radix-digit convolution](radix-digit-convolution.md): The index of a coefficient of W.
- $z$ (indeterminate), bound on [Radix-digit convolution](radix-digit-convolution.md): A formal symbol that is not a number, the variable of the polynomials U, V and W.
- $U$ (digit polynomial of u), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of u.
- $V$ (digit polynomial of v), bound on [Radix-digit convolution](radix-digit-convolution.md): The polynomial whose coefficient list is the digits of v.
- $W$ (product polynomial), bound on [Radix-digit convolution](radix-digit-convolution.md): The product UV, whose coefficient list is the convolution of the digit lists.
- $w_j$ (convolution coefficient), bound on [Radix-digit convolution](radix-digit-convolution.md): The j-th coefficient of W, the sum of the products u_i v_l with i+l=j.
- $a$ (first sequence), bound on [Cyclic convolution](cyclic-convolution.md): The first of the two input sequences, with entries $a_0, \dots, a_{q-1}$.
- $b$ (second sequence), bound on [Cyclic convolution](cyclic-convolution.md): The second of the two input sequences, with entries $b_0, \dots, b_{q-1}$.
- $q$ (sequence length), bound on [Cyclic convolution](cyclic-convolution.md): The number of entries in each of the two sequences.
- $c$ (cyclic convolution), bound on [Cyclic convolution](cyclic-convolution.md): The sequence $a \ast b$ of the same length, whose entries are given by the cyclic convolution sum.
- $i$ (summation index), bound on [Cyclic convolution](cyclic-convolution.md): The index of the terms in the sum that defines each output entry.
- $t$ (output index), bound on [Cyclic convolution](cyclic-convolution.md): The index of the output entry $c_t$.
- $q$ (entry count), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of complex entries in each input and output vector.
- $j$ (output index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an output entry, running from $0$ to $q-1$.
- $k$ (input index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an input entry, running from $0$ to $q-1$.
- $\omega$ (primitive root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, the weight base of the transform.
- $F_q$ (discrete Fourier transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The normalized transform on vectors of length $q$, with $y = F_q x$.
- $x$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ values on this page, not the integer inputs above.
- $y$ (output vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform of $x$ on this page, not the integer inputs above.
- $l$ (entry index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index of an entry of $x$, running from $0$ to $q-1$.
- $m$ (integer exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent in a sum of powers of $\omega$.
- $a$ (first vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The first vector of the convolution, of length $q$.
- $b$ (second vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The second vector of the convolution, of length $q$.
- $t$ (shifted index), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "All operator norms are induced by this norm" (paper)

  > All subscripts on a vector of length q are taken modulo q. The vector norm is the maximum modulus of its coordinates. All operator norms are induced by this norm: ∥L∥ = sup∥u∥≤1 ∥Lu∥. Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one. Coordinate permutations preserve the norm. For an integer precision p ≥ 1, put Dp = {2−p (a + ib) : a, b ∈ Z, a2 + b2 ≤ 22p }. For storage between completed scalar routines, put wc = p + 2. Represent 2−p (a + ib) ∈ Dp by a signed wc -bit two’s-complement word for a, followed by one for b, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since |a|, |b| ≤ 2p < 2wc −1 , this format includes both signs of every permitted numerator, e : Da →


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds" (The stated bounds are not on this page, and C, S', J', D' are never defined, so the reader cannot check that ||B_0|| <= 1 or that A and B_0 are contractions. The product bound itself is followable.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "A normalized Fourier transform is a contraction, since each output averages inputs multiplied by complex numbers of modulus one." (Calling each output an average needs the normalization factor (1/q), which this page never states. With the 1/sqrt(q) normalization the input (1,...,1) maps to (sqrt(q),0,...,0), which has norm sqrt(q), so the contraction claim depends on a definition the reader cannot see here.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $S'$ denotes where it is first used (for a size or count, what it counts): "for $A=S'$" (S' is never defined; the page only equates A with it, and no sentence says what S' is.)
- Say what $D'$ denotes where it is first used (for a size or count, what it counts): "$B_0=D'J'C$" (D' is never defined; the page only uses it in the product D'J'C, and no sentence says what it is.)
- Say what $J'$ denotes where it is first used (for a size or count, what it counts): "$B_0=D'J'C$" (J' is never defined; the page only uses it in the product D'J'C, and no sentence says what it is.)
- Say what $C$ denotes where it is first used (for a size or count, what it counts): "$B_0=D'J'C$" (C is never defined; the page only uses it in the product D'J'C and in the claim that its norm is one.)

## Previous version (revise it)

It has 231 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 288 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

The operator norm of a linear map is the largest factor by which the map can stretch a vector. It is what lets a bound on each map in a chain be multiplied into a bound on the whole chain.

Here $w$ denotes a complex vector of length $q$. Its vector norm $\|w\|$ is the largest modulus among its coordinates. <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite> For example, if $w=(1+i,\,-2,\,0.5i)$, the moduli of the coordinates are $\sqrt{2}$, $2$ and $0.5$, so $\|w\|=2$.

Here $L$ denotes a linear map from complex vectors to complex vectors. Its operator norm is

$$\|L\| = \sup_{\|w\|\le 1} \|Lw\|,$$

the supremum (least upper bound) of the values $\|Lw\|$ over all vectors $w$ with $\|w\|\le 1$. The operator norm is defined from the vector norm in this way. <cite data-source="paper">All operator norms are induced by this norm</cite>.

Scaling a nonzero vector $w$ to $w/\|w\|$, which has norm one, gives $\|Lw\|\le\|L\|\,\|w\|$ for every $w$. Applying this twice gives $\|LM\|\le\|L\|\,\|M\|$ for linear maps $L$ and $M$, so the norm of a composition is at most the product of the norms.

A linear map $L$ is a linear contraction when $\|L\|\le 1$, that is, when $\|Lw\|\le\|w\|$ for every $w$. Two examples follow from the definition. A coordinate permutation has norm one <cite data-source="paper">Coordinate permutations preserve the norm</cite>, since it only rearranges the moduli. A normalized Fourier transform is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.

The argument uses this for $A=S'$ and $B_0=D'J'C$. Since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds, the product bound gives $\|B_0\|\le\|D'\|\,\|J'\|\,\|C\|$, and this is what makes $A$ and $B_0$ linear contractions.

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

Write the body to `exegenius/tasks/0032-write-operator-norm.answer.md` and the JSON to `exegenius/tasks/0032-write-operator-norm.answer.json`, then run `exegenius submit 0032-write-operator-norm` in the project directory. If submit rejects the answer, fix the answer and submit again.
