# exegenius task 0043-write-operator-norm

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
- Coprime integers (also: coprime)
- Linear map
- Modular arithmetic (also: modular indices)

## This page

Concept: Operator norm
Gloss: For a linear map, the largest factor by which it stretches a vector measured in a fixed norm, taken over all vectors of norm at most one.
Also called: norm of a linear map

## Where the argument relies on this page

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))
- $\|N-I\|<1/2$, so the correction $N$ is invertible by a Neumann series.
- $A=S/2$ and $B_0=2^{-(2\alpha^2-2)}DN^{-1}C/2$ are set as contractions.

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

- [Linear map](linear-map.md): A map between vectors of numbers that preserves addition and scalar multiplication, so that each output coordinate is a fixed weighted sum of the input coordinates.
  Shown as: Operator norm *<predicate>* Linear map

## Pages that build on this one

- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Coprime integers](coprime-integers.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Tensor product](tensor-product.md)
- [Convolution theorem](convolution-theorem.md)
- [Gaussian function](gaussian-function.md)
- [Transform](transform.md)
- [Axis length](axis-length.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "All operator norms are induced by this norm" (paper)

  > All subscripts on a vector of length q are taken modulo q. The vector norm is the maximum modulus of its coordinates. All operator norms are induced by this norm: ∥L∥ = sup∥u∥≤1 ∥Lu∥. Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one. Coordinate permutations preserve the norm. For an integer precision p ≥ 1, put Dp = {2−p (a + ib) : a, b ∈ Z, a2 + b2 ≤ 22p }. For storage between completed scalar routines, put wc = p + 2. Represent 2−p (a + ib) ∈ Dp by a signed wc -bit two’s-complement word for a, followed by one for b, with each word written most significant bit first. A coordinate list is the concatenation of these fixed-length records in its stated order. Since |a|, |b| ≤ 2p < 2wc −1 , this format includes both signs of every permitted numerator, e : Da →


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Operator norms also bound compositions" (The page states the bound on products of maps without proof, and the reader cannot derive it from the given definition of the operator norm (it needs the scaling behaviour of the supremum applied twice). M is also unbound.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $\sup$ denotes where it is first used: the page uses it before saying so in "where $\sup$ is the supremum, the least upper bound"
- Say what $M$ denotes where it is first used (for a size or count, what it counts): "$\|LM\| \le \|L\|\,\|M\|$" (Nothing on this page or the earlier pages says what M denotes; the reader can only guess it is another linear map.)
- Say what $A$ denotes where it is first used (for a size or count, what it counts): "the factors $A$ and $B_0$ are contractions" (A is not bound on any earlier page, and the page only names it as a factor on the linked Gaussian resampling page.)
- Say what $B_0$ denotes where it is first used (for a size or count, what it counts): "the factors $A$ and $B_0$ are contractions" (B_0 is not bound on any earlier page, and the page only names it as a factor on the linked Gaussian resampling page.)
- Say what $u_0$ denotes where it is first used (for a size or count, what it counts): "let $L$ send $(u_0, u_1)$ to" (The example introduces u_0 as a coordinate of a two-coordinate input, but nothing says it is a coordinate of u or what index it takes.)
- Say what $u_1$ denotes where it is first used (for a size or count, what it counts): "let $L$ send $(u_0, u_1)$ to" (The example introduces u_1 as a coordinate of a two-coordinate input, but nothing says it is a coordinate of u or what index it takes.)

## Previous version (revise it)

It has 207 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 258 words. Pages that grow with every repair stop being self-contained explanations of one concept.

The operator norm measures how much a linear map can enlarge a vector. It gives each map a single number, which lets a bound on one step of a computation carry over to the next. Here $L$ denotes a [linear map](linear-map.md). The operator norm is defined for any [linear map](linear-map.md), and it is the largest factor by which $L$ stretches a vector.

The variable $u$ denotes a vector whose length matches the input length of $L$. The norm of $u$ is the largest modulus (absolute value) among its coordinates, and operator norms are taken with respect to this norm. <cite data-source="paper">All operator norms are induced by this norm</cite>. Then

$$\|L\| = \sup_{\|u\| \le 1} \|Lu\|,$$

where $\sup$ is the supremum, the least upper bound of the values $\|Lu\|$ over all $u$ with $\|u\| \le 1$.

For example, let $L$ send $(u_0, u_1)$ to $(u_0+u_1,\ u_0-u_1)$. If every coordinate of $u$ has modulus at most one, each output coordinate has modulus at most $2$, and $u=(1,1)$ gives $Lu=(2,0)$. Hence $\|L\|=2$.

A map with $\|L\| \le 1$ never increases the norm of a vector, and is called a contraction. The normalized Fourier transform $F_q$ is one, because <cite data-source="paper">each output averages inputs multiplied by complex numbers of modulus one</cite>.

Operator norms also bound compositions: $\|LM\| \le \|L\|\,\|M\|$, so the norm of a product of maps is at most the product of their norms. On the [Gaussian resampling](gaussian-resampling.md) page, the factors $A$ and $B_0$ are contractions, so they cannot increase the norm of what they are applied to.

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

Write the body to `exegenius/tasks/0043-write-operator-norm.answer.md` and the JSON to `exegenius/tasks/0043-write-operator-norm.answer.json`, then run `exegenius submit 0043-write-operator-norm` in the project directory. If submit rejects the answer, fix the answer and submit again.
