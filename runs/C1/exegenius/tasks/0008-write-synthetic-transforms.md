# exegenius task 0008-write-synthetic-transforms

Project directory: `/home/user/openai-nlogn-wiki/runs/C1` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis including recurrences and logarithms, basic discrete mathematics (modular arithmetic, binary representation, divisibility and primes), linear algebra (vectors, matrices, tensor-like indexing of arrays), and elementary algorithms such as schoolbook multiplication. They know Turing machines and tapes, polynomials and complex numbers, but have not studied fast integer multiplication, the FFT in depth, number-theoretic transforms, finite fields, or abstract algebra beyond basics. Specialist material introduced by the paper is not assumed.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Schönhage–Strassen n log n conjecture
- Convolution and discrete Fourier transform
- Multiplication as digit convolution
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a polynomial of the ring, a power of two.
- Binary representation of integers (also: binary expansion, bit string, most significant bit, val(x), padded binary)
- Logarithms and floor/ceiling (also: lg, log base 2, ceiling, floor, iterated logarithm)
- Modular arithmetic (also: congruence, mod, remainder, residues)
- Primes and coprimality (also: distinct primes, coprime, relatively prime, gcd)
- Vectors, matrices and linear maps (also: linear transformation, invertible matrix, subspace, rank, linear combination, dimension)
- Tensor (Kronecker) product and multidimensional arrays (also: tensor product, Kronecker product, multi-index array, d-dimensional array)
- Roots of unity (also: primitive root of unity, e^{2 pi i/n}, nth roots of unity)
- Schoolbook multiplication and basic divide-and-conquer (also: grade-school multiplication, O(n^2) multiplication, Karatsuba)
- Recurrence relations and geometric sums (also: recursion analysis, master theorem, geometric series)
- Floating and fixed-point numbers and rounding (also: truncation, rounding error, approximation error, sup norm, max norm)
- Sorting and permutations (also: permutation, bit-reversal, XOR, bitwise exclusive or)
- Asymptotic notation variants (also: Theta, Omega, little-o, soft-O, worst-case running time)
- Finite sets, products and maps (also: Cartesian product, cyclic group Z/mZ, bijection, index set)

## This page

Concept: Synthetic polynomial transforms
Gloss: Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplications are signed shifts and the work is butterflies, shifts and address rearrangements.

## This page in the argument

The step: Multiplication by a root of unity in the remaining axes is a signed shift, so synthetic transforms consist of shifts, butterflies and rearrangements.

It serves these steps, from the main result down:

- A fixed deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce the product to convolution over a polynomial ring, speed up its transforms with two tape procedures having a recursive power saving, then recover the exact product by rounding (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Convolution and discrete Fourier transform](dft-convolution.md): Convolution of coefficient lists is computed by transforming, multiplying pointwise and inverting the transform, using roots of unity.
  Shown as: Synthetic polynomial transforms *<predicate>* Convolution and discrete Fourier transform
- [Polynomial ring modulo y^r + 1](poly-ring-y-r-1.md): Polynomials in y with complex coefficients modulo y^r+1, where powers of y act as roots of unity and multiplication by them is a signed shift.
  Shown as: Synthetic polynomial transforms *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected address bits of d chunks at cost O(V d^λ'), λ'<1.
- Integer multiplication in O(n (lg n)^(1−κ)) time: A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Multiplication as digit convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Fixed-point precision and exact recovery](fixed-point-precision.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Elementary tape streams and scans](tape-streams.md)
- [Linear networks with frames and roles](gate-frames.md)
- [Finite networks with rank saving](finite-network-subspaces.md)
- [Recursive power saving](recursive-power-saving.md)
- [Fast interchange of address chunks](address-interchange.md)
- [Simultaneous butterfly layers](fast-butterfly-layers.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "synthetic polynomial transforms of Nussbaumer and Quandalle" (paper)

  > Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. Our starting point is the Gaussian-resampling reduction of Harvey and van der Hoeven \cite{HarveyHoeven2021}: it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two. After a further conversion to convolution, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two. Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list. These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer~\cite{NussbaumerQuandalle1978,Nussbaumer1980}.

- "\begin{lemma}[Synthetic character cancellation]" (paper)

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

Write the body to `exegenius/tasks/0008-write-synthetic-transforms.answer.md` and the JSON to `exegenius/tasks/0008-write-synthetic-transforms.answer.json`, then run `exegenius submit 0008-write-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0008-write-synthetic-transforms`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
