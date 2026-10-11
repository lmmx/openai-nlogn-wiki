# exegenius task 0048-write-radix-digit-convolution

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

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Discrete Fourier transform (also: normalized Fourier transform, Fourier transform)
- Cyclic convolution
- Axis length
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)
- Operator norm (also: norm of a linear map)
- Tensor product
- Convolution theorem
- Gaussian function (also: Gaussian weight, Gaussian (weight or function))
- Transform

## This page

Concept: Radix-digit convolution
Gloss: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## Where the argument relies on this page

- $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$, so the source permutation cancels across the convolution.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.
- $m$ (input length), bound on [Linear map](linear-map.md): The number of input coordinates of a linear map.
- $k$ (output length), bound on [Linear map](linear-map.md): The number of output coordinates of a linear map.
- $L$ (linear map), bound on [Linear map](linear-map.md): The rule sending a vector of m complex numbers to a vector of k complex numbers.
- $u$ (input vector), bound on [Linear map](linear-map.md): The vector of m complex numbers that a linear map takes as input.
- $v$ (output vector), bound on [Linear map](linear-map.md): The vector of k complex numbers that a linear map returns.
- $u_j$ (input coordinate), bound on [Linear map](linear-map.md): The j-th coordinate of the input vector.
- $v_i$ (output coordinate), bound on [Linear map](linear-map.md): The i-th coordinate of the output vector.
- $a_{ij}$ (weight), bound on [Linear map](linear-map.md): The fixed complex number by which output i multiplies input j.
- $q$ (vector length), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The number of values in each vector.
- $\omega$ (root of unity), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A primitive $q$-th root of unity, with $\omega^q=1$.
- $m$ (exponent), bound on [Discrete Fourier transform](discrete-fourier-transform.md): An integer exponent of $\omega$, with $0<m<q$.
- $j$ (input position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The position of an input value, running from $0$ to $q-1$.
- $k$ (output position), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The position of an output value, running from $0$ to $q-1$.
- $u$ (input vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A vector of $q$ values.
- $F_q$ (transform map), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of $q$ values to its normalized transform.
- $F_q^+$ (opposite transform), bound on [Discrete Fourier transform](discrete-fourier-transform.md): The transform with $\omega^{-1}$ in place of $\omega$.
- $v$ (second vector), bound on [Discrete Fourier transform](discrete-fourier-transform.md): A second vector of $q$ values, for forming a convolution.
- $L$ (linear map), bound on [Operator norm](operator-norm.md): The linear map whose stretching of vectors the operator norm measures.
- $u$ (test vector), bound on [Operator norm](operator-norm.md): A vector whose length matches the input length of the map, over which the supremum is taken.
- $L$ (first map), bound on [Tensor product](tensor-product.md): A linear map on vectors of length $s$.
- $M$ (second map), bound on [Tensor product](tensor-product.md): A linear map on vectors of length $t$.
- $\otimes$ (tensor product), bound on [Tensor product](tensor-product.md): The operator that combines $L$ and $M$ into a linear map on arrays with $s$ rows and $t$ columns.
- $u$ (array), bound on [Tensor product](tensor-product.md): An array with $s$ rows and $t$ columns, whose entries are $u_{hg}$.
- $i$ (output row index), bound on [Tensor product](tensor-product.md): The index of an output row, which is the first coordinate of an output position.
- $m$ (output column index), bound on [Tensor product](tensor-product.md): The index of an output column, which is the second coordinate of an output position.
- $h$ (input row index), bound on [Tensor product](tensor-product.md): The index of an input row of the array $u$.
- $g$ (input column index), bound on [Tensor product](tensor-product.md): The index of an input column of the array $u$.
- $\ell_1$ (first axis length), bound on [Axis length](axis-length.md): The number of positions along the first axis of a two-dimensional array, a count.
- $\ell_2$ (second axis length), bound on [Axis length](axis-length.md): The number of positions along the second axis of a two-dimensional array, a count.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication](exact-integer-multiplication.md): Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
  Shown as: Radix-digit convolution *<predicate>* Exact integer multiplication
- [Discrete Fourier transform](discrete-fourier-transform.md): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
  Shown as: Radix-digit convolution *<predicate>* Discrete Fourier transform
- [Axis length](axis-length.md): The number of positions along one coordinate axis of a multidimensional array; a multidimensional transform is applied along each axis in turn, with its own length.
  Shown as: Radix-digit convolution *<predicate>* Axis length

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.

## Other pages you may link to

- [Linear map](linear-map.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Coprime integers](coprime-integers.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Tensor product](tensor-product.md)
- [Convolution theorem](convolution-theorem.md)
- [Gaussian function](gaussian-function.md)
- [Transform](transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven [15]: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two. Powers of y then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer [21, 20]. In this representation, the transform calculation consists of address rearrangements,


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "transform $a$ and $b$, multiply pointwise, and invert" (The page presents transforming a and b, multiplying pointwise and inverting as computing the convolution when the transform length is at least 2d-1. Nothing given shows why a pointwise product of transforms yields the coefficient convolution (the convolution theorem) or why length 2d-1 suffices. That is not in the reader's profile or known concepts.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $k$ denotes where it is first used: the page uses it before saying so in "with $k$ the number of bits in each radix digit"
- Say what $m$ denotes where it is first used (for a size or count, what it counts): "with $c_m = \sum_{i+l=m} a_i b_l$" (The index of the convolution coefficient c_m and of the sum over m in the polynomial identity; the page never says what m denotes. The earlier-page bindings of m (input length, exponent of omega) are different quantities and do not apply here.)

## Previous version (revise it)

It has 241 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 301 words. Pages that grow with every repair stop being self-contained explanations of one concept.

A radix-digit convolution computes a product of two integers as a polynomial convolution. Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a polynomial product whose coefficients are short integers.

Let $B = 2^k$ be the radix, the base in which each integer is written, with $k$ the number of bits in each radix digit. Let $d$ be the number of radix digits of each input. Let $x$ and $y$ be the two inputs, nonnegative integers below $B^d$. Let $a = (a_0, \dots, a_{d-1})$ be the coefficient list of $x$, its radix digits, so that $x = \sum_{i=0}^{d-1} a_i B^i$ with $0 \le a_i < B$. Let $z$ be a formal variable, a placeholder for the powers of a polynomial. Then $x$ is the value at $z = B$ of the polynomial $a(z) = \sum_i a_i z^i$. The input $y$ has the coefficient list $b$ in the same way.

The convolution $c = a * b$ is the coefficient list of the product $a(z)b(z)$, with $c_m = \sum_{i+l=m} a_i b_l$. Since $a(B) = x$ and $b(B) = y$, we have $xy = \sum_m c_m B^m$, so carrying the $c_m$ in base $B$ gives the binary representation of $xy$. Each $c_m$ is a sum of at most $d$ products of digits, so $c_m < dB^2$: the coefficients are short integers even when $x$ and $y$ are long.

For example, take $B = 4$, $d = 2$, $x = 13$ and $y = 11$. Then $13 = 3\cdot 4 + 1$ and $11 = 2\cdot 4 + 3$, so $a = (1, 3)$ and $b = (3, 2)$. The convolution is $c = (3, 11, 6)$, since $c_0 = 1\cdot 3$, $c_1 = 1\cdot 2 + 3\cdot 3$ and $c_2 = 3\cdot 2$, and $3 + 11\cdot 4 + 6\cdot 16 = 143 = 13\cdot 11$.

Computing this convolution directly takes about $d^2$ multiplications of digits. Radix-digit convolution is computed by [Fourier transforms](discrete-fourier-transform.md) of length at least $2d-1$: transform $a$ and $b$, multiply pointwise, and invert.

The sources start from this reduction. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>. After [Gaussian resampling](gaussian-resampling.md), the convolution is computed with transforms of [axis lengths](axis-length.md) that are powers of two.

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

Write the body to `exegenius/tasks/0048-write-radix-digit-convolution.answer.md` and the JSON to `exegenius/tasks/0048-write-radix-digit-convolution.answer.json`, then run `exegenius submit 0048-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
