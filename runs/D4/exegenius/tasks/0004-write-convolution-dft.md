# exegenius task 0004-write-convolution-dft

Project directory: `/home/user/openai-nlogn-wiki/runs/D4` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, algorithms (divide and conquer, recurrences, FFT-style ideas at a basic level), discrete mathematics (sets, binomial coefficients, binary representation, modular arithmetic, primes), and linear algebra (vector spaces, subspaces, rank, matrix products, Gaussian elimination, orthogonal projections, over the rationals and basic finite fields). They know complex numbers and polynomials, and basic Turing machines. They have not studied advanced algebra (Bruhat decomposition, general rings and quotients in depth), number theory beyond basics, numerical error analysis of FFTs, or the research literature on fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machines
- Binary representation of integers (also: bits, base-2 expansion, binary digits, bit string)
- Hamming weight (also: wt, popcount, number of ones)
- Bitwise XOR (also: exclusive or, addition mod 2, xor)
- Modular arithmetic (also: residues, congruence, integers mod m, residue ring)
- Prime numbers and coprimality (also: distinct primes, relatively prime, gcd)
- Linear algebra over the rationals (also: vector spaces, subspaces, dimension, matrix rank, rational rank, linear maps, orthogonal projection, orthogonal complement)
- Gaussian elimination and the general linear group over F2 (also: row reduction, GL(m,F_2), invertible binary matrices, elementary row operations, triangular factorization)
- Binomial coefficients and basic counting (also: n choose k, subsets, combinations, inclusion-exclusion)
- Recurrences and divide and conquer (also: recursion, recursive calls, master theorem, recursion tree)
- Exponentials, logarithms and iterated logarithm bounds (also: lg, log base 2, exp, powers of logarithms)
- Matrix and block notation (also: diagonal matrix, block matrix, identity matrix, transpose, Kronecker product, tensor product)
- Roots of unity and Euler's formula (also: primitive root of unity, e^{2 pi i/N}, complex exponential)
- Fast Fourier transform idea (also: FFT, Cooley-Tukey, radix-2 FFT)
- Sorting and permutations (also: permutation of indices, bit reversal, rearranging records)
- Basic real error bounds (also: rounding, floor and ceiling, triangle inequality, absolute error, fixed-point arithmetic)
- Schoolbook integer multiplication and carries (also: long multiplication, carry propagation, grade-school multiplication, radix)

## This page

Concept: Convolution and the discrete Fourier transform
Gloss: Convolution multiplies coefficient lists as polynomials; a Fourier transform at roots of unity turns it into pointwise products.

## Where the argument relies on this page

- The product of two $n$-bit integers is computed exactly by the pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery. (on [The assembled multiplication algorithm](multiplication-algorithm.md))
- Splitting each $n$-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation. (on [Integer multiplication as digit convolution](mult-to-convolution.md))
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform. (on [Gaussian resampling](gaussian-resampling.md))
- Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. (on [Bluestein chirp conversion](bluestein-chirp.md))
- Convolution over the remaining axes is computed over $\mathbb{C}[y]/(y^r+1)$ by synthetic transforms. (on [Synthetic polynomial transforms](synthetic-transforms.md))

## Pages that build on this one

- Integer multiplication as digit convolution: Splitting each n-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation.
- Gaussian resampling: The Harvey–van der Hoeven reduction replacing arbitrary-length Fourier transforms by multidimensional transforms with power-of-two axis lengths.
- Synthetic polynomial transforms: Fourier-type transforms using powers of y in the ring as roots of unity, built from address rearrangements, signed shifts and butterflies.
- Bluestein chirp conversion: Bluestein's chirp identity rewrites a transform of arbitrary length as a cyclic convolution.

## Other pages you may link to

- [Integer multiplication as digit convolution](mult-to-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Two-point butterfly](butterfly.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Fixed-point complex coefficients and exact dyadics](fixed-point-dyadics.md)
- [Bluestein chirp conversion](bluestein-chirp.md)
- [Coefficient twist to the negative wrap](phase-twist.md)
- [Rounding, rescaling and carry propagation](exact-recovery.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Fixed-tape machine model and stream scans](fixed-tape-model.md)
- [History and the n log n conjecture](nlogn-conjecture.md)
- [Linear networks with frames and restored auxiliaries](linear-network-frames.md)
- [Address shear and triangular factorization](address-shear.md)
- [Finite network from three-element subsets](subset-network.md)
- [Recursive power saving](recursive-saving.md)
- [Fast interchange of address chunks](fast-address-interchange.md)
- [Simultaneous fast butterfly layers](fast-butterfly-layers.md)
- [Chinese-remainder map to prime cyclic axes](crt-prime-axes.md)
- [Synthetic transform layout with retained frequency order](transform-layout.md)
- [Retained permutations cancelling](permutation-cancellation.md)
- [Exact normalized polynomial products](polynomial-products.md)
- [The assembled multiplication algorithm](multiplication-algorithm.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients." (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "F_t^+F_t^-=t^{-1}I" (paper)

  > \begin{lemma}[Synthetic character cancellation] \label{lem:synthetic-characters} If $j$ is an integer, then \[ \sum_{k=0}^{t-1}\omega_t^{jk} =\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases} \qquad F_t^+F_t^-=t^{-1}I. \] \end{lemma} \begin{proof} Only the second case needs proof. Write $j=2^v j_0$ with $j_0$ odd and $0\leq v<\log_2t$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion. Expanding the composite transforms and applying this identity proves the final formula. \end{proof}


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

Write the body to `exegenius/tasks/0004-write-convolution-dft.answer.md` and the JSON to `exegenius/tasks/0004-write-convolution-dft.answer.json`, then run `exegenius submit 0004-write-convolution-dft` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0004-write-convolution-dft`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
