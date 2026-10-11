# exegenius task 0042-write-coprime-integers

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
- Linear map

## This page

Concept: Coprime integers
Gloss: Two integers are coprime when their greatest common divisor is 1; a family of integers is pairwise coprime when every two of them are coprime.
Also called: coprime

## Where the argument relies on this page

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))
- $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$, so the source permutation cancels across the convolution.
- $F_s^+R=R^{-1}F_s^+$, hence $RF_s^+R=F_s^+$.

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

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Cyclic convolution](cyclic-convolution.md): The product of two sequences in which indices wrap around modulo the sequence length.
  Shown as: Coprime integers *<predicate>* Cyclic convolution

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Linear map](linear-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Tensor product](tensor-product.md)
- [Convolution theorem](convolution-theorem.md)
- [Gaussian function](gaussian-function.md)
- [Transform](transform.md)
- [Axis length](axis-length.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "pairwise coprime" (paper)

  > The transform lengths needed for the integer product are pairwise coprime, whereas the synthetic transforms use powers of two. Gaussian resampling connects these two shapes. Its usual implementation sorts twice on each coordinate. We retain both permutations in the transform formula and compute that formula directly. This section proves the resulting interface, including its tape cost when the number of coordinates grows. For an integer q ≥ 1, write q−1


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- [Cyclic convolution](cyclic-convolution.md) is now a prerequisite: link it where "cyclic convolution" is used: "lets one cyclic convolution be split into a multidimensional one over the same lengths"
- Explain "Chinese remainder theorem" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

It has 186 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 236 words. Pages that grow with every repair stop being self-contained explanations of one concept.

Coprime integers are integers with no common factor greater than 1. Two integers are coprime when their greatest common divisor, the largest integer that divides both, is 1. A family of integers is pairwise coprime when every two members of the family are coprime. The argument needs this notion because the transform lengths for an exact integer product must be pairwise coprime, which the synthetic transforms, using powers of two, do not need to be <cite data-source="paper">pairwise coprime, whereas the synthetic transforms use powers of two</cite>. Coprimality is also the hypothesis of the Chinese remainder theorem, which lets one cyclic convolution be split into a multidimensional one over the same lengths.

For example, $\gcd(4,9)=1$, since $4=2^2$ and $9=3^2$ share no prime factor, so 4 and 9 are coprime. By contrast $\gcd(4,6)=2$, so 4 and 6 are not coprime. The family $4, 9, 25$ is pairwise coprime. The family $4, 6, 9$ is not, because 4 and 6 share the factor 2 and 6 and 9 share the factor 3.

Coprimality is a property of the whole family of lengths, not of any single length. A single length $q$ is trivially coprime to itself only when $q=1$, so the test always involves at least two distinct integers.

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

Write the body to `exegenius/tasks/0042-write-coprime-integers.answer.md` and the JSON to `exegenius/tasks/0042-write-coprime-integers.answer.json`, then run `exegenius submit 0042-write-coprime-integers` in the project directory. If submit rejects the answer, fix the answer and submit again.
