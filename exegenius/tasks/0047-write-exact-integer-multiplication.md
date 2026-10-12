# exegenius task 0047-write-exact-integer-multiplication

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

Concept: Exact integer multiplication
Gloss: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.

## Where the argument relies on this page

- The transform identity $P_s F_s = 2^{2\alpha^2} B_0 P_t F_t A$ holds with linear contractions $A$ and $B_0$, so the source permutation $P_s$ and target permutation $P_t$ stay in the formula instead of being executed as sorts. (on [Transform identity with retained permutations](transform-identity.md))

## Pages that build on this one

- Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.

## Other pages you may link to

- [Radix-digit convolution](radix-digit-convolution.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "We consider exact multiplication" (paper)

  > Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine, and proposed n log n as the optimal order of growth [25, Section 1]. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional O(n log n) upper bound [15]. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers. For a binary string x of length n, let val(x) be its nonnegative integer value, with the leftmost bit most significant. For 0 ≤ z < 2k , let bink (z) denote its binary representation padded on the left to length k. We consider exact multiplication: on input x#y, with x, y ∈ {0, 1}n , the output must be bin2n (val(x) val(y)). Write lg n = max{⌈log2 n⌉, 1}. Theorem 1. There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs. Its worst-case running time satisfies 


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- $s$ means binary string here, but source length on [Gaussian resampling](gaussian-resampling.md), which builds on this page: Use another letter for the binary string (for example w), since s on gaussian-resampling is the length of the source vectors.
- $k$ means padded output length here, but target entry index on [Gaussian resampling](gaussian-resampling.md), which builds on this page: Use another letter for the padded output length (for example L), since k on gaussian-resampling is a target entry index.

## Previous version (revise it)

It has 331 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 413 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Exact integer multiplication is the problem of computing the complete binary product of two integers of equal bit length, with no rounding and no truncation. It is the problem whose cost the target result bounds, so its input and output format must be fixed first.

Let $n$ be the number of bits in each of the two binary strings to multiply, and let $x$ and $y$ be those strings. For a binary string $s$, let $\mathrm{val}(s)$ be its nonnegative integer value, with the leftmost bit most significant. Let $k$ be the length of a padded output, and for an integer $z$ with $0 \le z < 2^k$, let $\mathrm{bin}_k(z)$ be its binary representation padded on the left with zeros to length $k$.

The input is the string $x\#y$, where $\#$ is a separator symbol, and the output must be $\mathrm{bin}_{2n}(\mathrm{val}(x)\cdot\mathrm{val}(y))$. The output length $2n$ is always enough: $\mathrm{val}(x)$ and $\mathrm{val}(y)$ are at most $2^n-1$, so their product is at most $(2^n-1)^2<2^{2n}$. For example, with $n=3$, $x=101$ and $y=011$ have values 5 and 3, and the output is $\mathrm{bin}_6(15)=001111$.

A deterministic Turing machine computes exact multiplication if, on every input $x\#y$ with $x$ and $y$ of length $n$, it halts with this output. Its running time, as a function of $n$, is the worst case over all such inputs of length $n$. The target result uses a fixed finite alphabet and a fixed finite number of one-dimensional tapes, so neither grows with $n$. This is the fixed finite-tape model.

Schönhage and Strassen gave a multitape Turing machine that multiplies two $n$-bit integers in $O(n\log n\log\log n)$ time <cite data-source="paper">two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine</cite>, and they proposed $n\log n$ as the optimal order of growth. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound for this problem <cite data-source="paper">reached the unconditional O(n log n) upper bound</cite>. This is the bound that applies here: it is for the same problem, multiplying two $n$-bit integers on a multitape Turing machine, so the target result's saving is measured against it.

A strict power saving in the logarithmic factor means a running time smaller than $O(n\log n)$ by a fixed positive power of $\log n$. The target result gives such a saving in the same fixed finite-tape model.

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

Write the body to `exegenius/tasks/0047-write-exact-integer-multiplication.answer.md` and the JSON to `exegenius/tasks/0047-write-exact-integer-multiplication.answer.json`, then run `exegenius submit 0047-write-exact-integer-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
