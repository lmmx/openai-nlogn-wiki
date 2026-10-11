# exegenius task 0039-write-linear-map

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

## This page

Concept: Linear map
Gloss: A map between vectors of numbers that preserves addition and scalar multiplication, so that each output coordinate is a fixed weighted sum of the input coordinates.

## Where the argument relies on this page

- For coprime $s<t$ with $\theta=t/s-1$ large enough, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ with contractions $A$ and $B_0$. (on [Gaussian resampling](gaussian-resampling.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $n$ (input length), bound on [Exact integer multiplication](exact-integer-multiplication.md): The number of bits in each input string.
- $x$ (first input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The first binary input string, of length $n$.
- $y$ (second input), bound on [Exact integer multiplication](exact-integer-multiplication.md): The second binary input string, of length $n$.

## Pages that build on this one

- Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- Operator norm: For a linear map, the largest factor by which it stretches a vector measured in a fixed norm, taken over all vectors of norm at most one.
- Tensor product: The product of two linear maps or arrays acting on separate coordinates, so that applying the product acts on each coordinate in turn.
- Transform: A linear map from one array of values to another array of the same kind, each output being a fixed weighted sum of the inputs, such as a discrete Fourier transform.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Coprime integers](coprime-integers.md)
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

- "A gate is a fixed linear map on a specified set of" (paper)

  > Let T be the set of three-element subsets of [h]. There are two data banks Xa , Ya , indexed by a = (a1 , a2 , a3 ) ∈ T 3 . A wire carries one scalar. A gate is a fixed linear map on a specified set of wires; untouched wires retain their values. The vertices on a wire are its source, the gates that touch it in time order, and its sink; its edges join consecutive vertices. We call the name of a wire its role, so that we can distinguish a fixed place in the network from the value currently carried there.


## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $u_1$ denotes where it is first used (for a size or count, what it counts): "Then $L(u)=(u_1" (Only the general coordinate $u_j$ is defined; the page never says that $u_1$ is the first coordinate of $u$.)
- Say what $u_2$ denotes where it is first used (for a size or count, what it counts): "Then $L(u)=(u_1+2u_2" (Only the general coordinate $u_j$ is defined; the page never says that $u_2$ is the second coordinate of $u$.)
- Say what $a_{11}$ denotes where it is first used (for a size or count, what it counts): "with weights $a_{11}=1$" (Only the general weight $a_{ij}$ is defined; the page never says that $a_{11}$ is one of its instances.)
- Say what $a_{12}$ denotes where it is first used (for a size or count, what it counts): "$a_{12}=2$" (Only the general weight $a_{ij}$ is defined; the page never says that $a_{12}$ is one of its instances.)
- Say what $a_{21}$ denotes where it is first used (for a size or count, what it counts): "$a_{21}=3$" (Only the general weight $a_{ij}$ is defined; the page never says that $a_{21}$ is one of its instances.)
- Say what $a_{22}$ denotes where it is first used (for a size or count, what it counts): "$a_{22}=-1$" (Only the general weight $a_{ij}$ is defined; the page never says that $a_{22}$ is one of its instances.)
- Explain "matrix product" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

It has 166 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 216 words. Pages that grow with every repair stop being self-contained explanations of one concept.

Let $m$ be the number of input coordinates and $k$ the number of output coordinates. A linear map is a rule $L$ that takes a vector $u$ of $m$ complex numbers and returns a vector $v$ of $k$ complex numbers, written $L:\mathbb{C}^m\to\mathbb{C}^k$.

The rule is linear: for vectors $u, u'$ and a number $c$, $L(u+u')=L(u)+L(u')$ and $L(cu)=cL(u)$. Equivalently, each output coordinate is a fixed weighted sum of the input coordinates. Here $u_j$ is the $j$-th input coordinate, $v_i$ the $i$-th output coordinate, and $a_{ij}$ the weight that output $i$ gives to input $j$.

That is,

$$v_i=\sum_{j=1}^{m} a_{ij}\,u_j \qquad (i=1,\dots,k).$$

The weights do not depend on $u$. The table of all $a_{ij}$ is the matrix of $L$, and any choice of weights defines a linear map in this way.

For example, take $m=k=2$ with weights $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=-1$. Then $L(u)=(u_1+2u_2,\ 3u_1-u_2)$, and for $u=(1,1)$ the output is $v=(3,2)$.

Composing two linear maps gives another linear map, whose matrix is the matrix product of the two matrices. So a chain of linear maps can be replaced by a single one, which is how the argument below combines its steps.

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

Write the body to `exegenius/tasks/0039-write-linear-map.answer.md` and the JSON to `exegenius/tasks/0039-write-linear-map.answer.json`, then run `exegenius submit 0039-write-linear-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
