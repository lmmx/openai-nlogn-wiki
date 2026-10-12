# exegenius task 0017-write-radix-digit-convolution

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

Concept: Radix-digit convolution
Gloss: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## Where the argument relies on this page

- The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts. (on [Transform identity with retained permutations](transform-identity.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary string to multiply, of length n.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary string to multiply, of length n.
- $n$ (input bit length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $\mathrm{val}$ (integer value), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the nonnegative integer value of a binary string, with the leftmost bit most significant.
- $\mathrm{bin}_k$ (padded binary representation), bound on [Exact integer multiplication](exact-integer-multiplication.md): The function giving the binary representation of an integer z, padded on the left with zeros to k bits.
- $k$ (padded output length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in the padded binary representation.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Radix-digit convolution *<predicate>* Exact integer multiplication

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.

## Other pages you may link to

- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements,


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $v_l$ denotes where it is first used (for a size or count, what it counts): "$w_j=\sum_{i+l=j} u_i v_l$" (Only the digit definition of v_i (the i-th digit of v) suggests v_l is the l-th digit of v by the same subscript convention; the page does not say so.)

## Previous version (revise it)

It has 234 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 292 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Radix-digit convolution is the rewriting of two integers as polynomials in a power of two whose coefficients are their digits, so that multiplying the integers becomes multiplying the polynomials. It is the first step of the argument, and the [Transform identity with retained permutations](transform-identity.md) acts on the coefficient lists it produces.

Splitting integers into radix digits reduces [Exact integer multiplication](exact-integer-multiplication.md) to convolution of short integer coefficients. The paper states this reduction at the start of its argument.<cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

Let $k$ be the number of bits in one radix digit, so the digit base is $2^k$, and let $m$ be the number of digits in each integer.

Take integers $u$ and $v$ below $2^{km}$, whose $i$-th digits are $u_i$ and $v_i$, each in $\{0,\dots,2^k-1\}$. Then
$$u = \sum_{i=0}^{m-1} u_i 2^{ki}, \qquad v = \sum_{i=0}^{m-1} v_i 2^{ki}.$$

Let $z$ be an indeterminate and let $U(z)=\sum_{i=0}^{m-1} u_i z^i$ and $V(z)=\sum_{i=0}^{m-1} v_i z^i$ be the polynomials whose coefficient lists are the digits of $u$ and $v$, so that $u=U(2^k)$ and $v=V(2^k)$.

Let $W=UV$ be their product, whose coefficient of $z^j$ is $w_j=\sum_{i+l=j} u_i v_l$; this convolution of the digit lists gives $uv=W(2^k)$.

Each $w_j$ is a sum of at most $m$ products of digits, so $w_j \le m(2^k-1)^2$ and $w_j$ has about $2k+\log_2 m$ bits. These are the short integer coefficients of the reduction.

Multiplying the integers is thus replaced by convolving short coefficient lists, followed by carry propagation, because $w_j$ can exceed $2^k-1$.

For $k=2$ and $m=2$, take $u=13$ and $v=6$. Then $U(z)=1+3z$ and $V(z)=2+z$, so $W=2+7z+3z^2$ and $W(4)=78=13\cdot 6$. The coefficient $7$ is larger than any radix-4 digit, so it is carried into the next position, giving the digits $2,3,0,1$ of $78$.

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

Write the body to `exegenius/tasks/0017-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0017-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0017-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
