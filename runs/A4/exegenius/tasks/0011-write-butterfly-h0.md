# exegenius task 0011-write-butterfly-h0

Project directory: `/home/user/openai-nlogn-wiki/runs/A4` (paths below are relative to it)

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

For these sources: An undergraduate computer science reader who knows asymptotic notation, basic discrete mathematics, linear algebra over the reals and complex numbers, elementary algebra (groups, rings, modular arithmetic, polynomials), elementary number theory (primes, CRT) and basic probability/combinatorics. They know basic Turing machines and tapes and the schoolbook and Karatsuba multiplication, and probably the FFT as an algorithm. They have not studied multitape-machine algorithm engineering, Schönhage–Strassen or later multiplication algorithms, or specialist linear-algebra constructions such as Bruhat factorizations.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed multitape Turing machine model
- Array order and elementary tape scans
- Convolution and Fourier transforms
- Multiplication as convolution of radix digits
- Established O(n log n) multiplication and history
- Polynomial ring modulo y^r + 1
  - $y$ (polynomial variable): The formal indeterminate of the polynomials, whose powers serve as roots of unity.
  - $r$ (ring degree): The number of complex coefficients in a record, a power of two; y^r = -1 in the ring.
- Synthetic polynomial transforms
- Binary representation and bit operations (also: bit strings, binary expansion, XOR, bitwise exclusive or, Hamming weight)
- Modular arithmetic and congruences (also: residue ring, integers mod m, Z/mZ)
- Primes and divisibility (also: gcd, coprime, relatively prime, prime number theorem)
- Linear algebra over fields (also: vector space, subspace, rank, invertible matrix, linear map, GL, diagonal matrix)
- Permutations and bijections (also: permutation, index permutation, bit reversal, bijection)
- Groups and rings (basic algebra) (also: group, cyclic group, ring, abelian group, subgroup)
- Finite sets and elementary combinatorics (also: subsets, counting arguments, binomial coefficients, intersection sizes)
- Floating and fixed-point approximation and rounding (also: rounding error, error bounds, triangle inequality)
- Recurrences and divide-and-conquer analysis (also: recursion, master theorem, recursion tree, geometric series)
- Logarithms and exponentials (also: lg, log base 2, iterated logarithm, powers of two)
- Fast Fourier transform algorithm (also: FFT, Cooley-Tukey, DFT)
- Schoolbook and Karatsuba multiplication (also: long multiplication, Karatsuba)
- Floor, ceiling and big-omega notation (also: floor, ceiling, Omega, Theta, little-o)

## This page

Concept: Two-point butterfly H₀
Gloss: The map H0(u,v) = ((u+v)/2,(u−v)/2) applied coefficientwise; the basic arithmetic step of a transform layer.
Heading: Two-point butterfly $H_0(u,v)$

The symbols in this page's heading denote (say so on the page):

- $u$ (first operand): The first of the two input values (a polynomial record).
- $v$ (second operand): The second of the two input values.

## Where the argument relies on this page

- $H_0$ can be applied simultaneously on one bit in each of $d$ address chunks at cost $O(Vd^{\lambda'})$ with $\lambda'<1$. (on [Fast simultaneous butterfly layers](fast-butterfly-layers.md))
- Convolution on the remaining axes over the polynomial ring is computed by synthetic transforms and ring products. (on [Synthetic transforms on tape layouts](synthetic-layout.md))

## Pages that build on this one

- Multidimensional transform with power-of-two axes: Fourier transform on an array indexed by several axes, computed one axis at a time by butterflies; axis lengths are powers of two.
- Fast simultaneous butterfly layers: Tape procedure applying H0 simultaneously on one selected bit in each of d address chunks of numerical arrays at cost O(V d^λ'), using phase frames and one truncation after the contractive layer.

## Other pages you may link to

- [Fixed multitape Turing machine model](multitape-model.md)
- [Established O(n log n) multiplication and history](known-nlogn.md)
- [Convolution and Fourier transforms](convolution-dft.md)
- [Multiplication as convolution of radix digits](radix-digit-reduction.md)
- [Polynomial ring modulo y^r + 1](ring-mod-yr.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Array order and elementary tape scans](elementary-scans.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Linear networks, roles and frames](linear-network-frames.md)
- [Address shear and restoration of scratch values](address-shear.md)
- [Finite networks from three-element subsets](subset-finite-network.md)
- [Recursive power saving from s < Wm](recursive-saving.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Chinese-remainder map to distinct prime cyclic axes](crt-prime-axes.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Fixed-point complex coefficients and exact recovery](fixed-point-precision.md)
- [Fast simultaneous butterfly layers](fast-butterfly-layers.md)
- [Synthetic transforms on tape layouts](synthetic-layout.md)
- [Signed coefficient packing (Kronecker substitution)](kronecker-packing.md)
- [Exact polynomial-ring products](ring-products.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](fast-multiplication.md)

## Evidence from the sources, with the paragraph around each quote

- "H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr)" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
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
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
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

Write the body to `exegenius/tasks/0011-write-butterfly-h0.answer.md` and the JSON to `exegenius/tasks/0011-write-butterfly-h0.answer.json`, then run `exegenius submit 0011-write-butterfly-h0` in the project directory. If submit rejects the answer, fix the answer and submit again.
