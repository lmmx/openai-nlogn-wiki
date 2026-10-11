# exegenius task 0017-write-discrete-fourier-transform

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
- Axis length
- Linear map

## This page

Concept: Discrete Fourier transform
Gloss: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
Also called: normalized Fourier transform, Fourier transform

## Where the argument relies on this page

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))
- $(RF_s^+)((RF_su)\cdot(RF_sv))=\frac{u*v}{(\prod_i s_i)^2}$, so the source permutation cancels across the convolution.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear map](linear-map.md): A map between vectors of numbers that preserves addition and scalar multiplication, so that each output coordinate is a fixed weighted sum of the input coordinates.
  Shown as: Discrete Fourier transform *<predicate>* Linear map

## Pages that build on this one

- Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Axis length](axis-length.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Coprime integers](coprime-integers.md)
- [Modular arithmetic](modular-arithmetic.md)
- [Operator norm](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Tensor product](tensor-product.md)
- [Transform identity with retained permutations](transform-identity.md)

## Evidence from the sources, with the paragraph around each quote

- "We now implement the normalized Fourier transforms needed for convolution" (paper)

  > We now implement the normalized Fourier transforms needed for convolution. Their entries will be short polynomials in a quotient where the required roots of unity act by exact signed permutations of coefficient lists. We also specify where each frequency entry is stored, because the opposite transform consumes that same order after a pointwise product. The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method of Nussbaumer and Quandalle [21, 20]; we use the form developed in [15, Section 2.4 and Lemma 3.2]. The work here is to apply the simultaneous layers on a suitable tape layout and retain the resulting frequency order through convolution. For an integer r ≥ 2 that is a power of two, put Rr = C[y]/(y r + 1),


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Transforming two vectors, multiplying the results entrywise, and applying the opposite transform gives their convolution up to a fixed scalar." (The page does not define the convolution of two vectors, does not say what the fixed scalar is, and gives no argument. The reader cannot check that this pipeline yields the convolution.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "an opposite transform brings the product back" (The page gives F_q^+ only as the transform with omega^{-1} in place of omega. It does not show that applying F_q^+ after F_q returns the original vector, so the reader cannot check this.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- The reader cannot follow this step: "The paper also fixes where each transformed entry is stored" (The page does not state the storage order, so the reader cannot check that the opposite transform reads entries in the same order. The claim rests on the paper, and it is not marked as cited.). Either give the reasoning, or attribute the step to the source with a citation; choose whichever needs fewer words.
- Say what $m$ denotes where it is first used (for a size or count, what it counts): "$\omega^m\neq 1$ for $0<m<q$" (Used only as an exponent over a range (0<m<q); nothing says what m denotes or counts.)
- "linear map" is the concept [Linear map](linear-map.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

It has 153 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 203 words. Pages that grow with every repair stop being self-contained explanations of one concept.

The discrete Fourier transform is a linear map that sends a vector of complex numbers to another vector of the same length. It is the tool that makes convolution cheap: the transform reduces [radix-digit convolution](radix-digit-convolution.md) to pointwise products of transformed vectors, and an opposite transform brings the product back.

Here $q$ is the number of values in the vector. Here $\omega$ is a primitive $q$-th root of unity: $\omega^q=1$, and $\omega^m\neq 1$ for $0<m<q$. The input position $j$ runs from $0$ to $q-1$. The output position $k$ runs from $0$ to $q-1$. We write $F_q$ for the transform map. For a vector $u=(u_0,\dots,u_{q-1})$,

$$(F_q u)_k=\frac{1}{q}\sum_{j=0}^{q-1}\omega^{jk}u_j.$$

The opposite transform $F_q^+$ uses $\omega^{-1}$ in place of $\omega$.

For $q=2$ we have $\omega=-1$, so $F_2(3,1)=\left(\tfrac{3+1}{2},\tfrac{3-1}{2}\right)=(2,1)$.

Transforming two vectors, multiplying the results entrywise, and applying the opposite transform gives their convolution up to a fixed scalar. The paper also fixes where each transformed entry is stored, because the opposite transform reads the entries in that same order after the pointwise product.

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

Write the body to `exegenius/tasks/0017-write-discrete-fourier-transform.answer.md` and the JSON to `exegenius/tasks/0017-write-discrete-fourier-transform.answer.json`, then run `exegenius submit 0017-write-discrete-fourier-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
