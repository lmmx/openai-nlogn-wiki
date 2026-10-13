# exegenius task 0020-write-main-theorem

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
- Elementary tape streams and scans
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers serve as roots of unity.
  - $r$ (coefficient count): The number of complex coefficients in a polynomial of the ring, a power of two.
- Synthetic polynomial transforms
- Gaussian resampling
- Chinese-remainder address map
- Bluestein chirp identity
- Signed packing (Kronecker substitution)
- Fixed-point precision and exact recovery
- Linear networks with frames and roles
- Finite networks with rank saving
- Recursive power saving
- Fast interchange of address chunks
- Simultaneous butterfly layers
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

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits of each integer factor.
- $\kappa$ (power saving): The constant 2^{-182} giving the exponent saving in the logarithmic factor.

## This page in the argument

The step: A fixed deterministic multitape Turing machine multiplies $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce the product to convolution over a polynomial ring, speed up its transforms with two tape procedures having a recursive power saving, then recover the exact product by rounding
Why: Plain transforms cost n log n by scanning n bits at each of log n levels, so the logarithmic factor itself must shrink; this needs a faster tape procedure for data movement and arithmetic, plus a reduction placing multiplication where those procedures apply. (the sources say so: "Scanning an array of $\Theta(n)$ stored bits at each of" (paper))
Striking feature: The saving is a genuine power of the logarithm, but with the astronomically small exponent kappa=2^-182. (explain why it holds, from the method)

Its sub-steps, in order:

- Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients. (on [Multiplication as digit convolution](radix-digit-convolution.md))
- The address rearrangements and butterfly layers of the synthetic transforms cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for stored bit volume $V$, a power saving below the linear-per-level cost.
- One coordinate is stored as a polynomial modulo $y^r+1$, so powers of $y$ are roots of unity. (on [Polynomial ring modulo y^r + 1](poly-ring-y-r-1.md))
- Multiplication by a root of unity in the remaining axes is a signed shift, so synthetic transforms consist of shifts, butterflies and rearrangements. (on [Synthetic polynomial transforms](synthetic-transforms.md))
- The convolution of the digit list is computed by convolution over the polynomial ring using the transforms of S4.
- Known normalizations are removed, the coefficient error is below $1/2$, and rounding with carry propagation gives the exact binary product. (on [Fixed-point precision and exact recovery](fixed-point-precision.md))
- A compatible choice of rational parameters makes every term of the cost table fit $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S4, S5, S7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4**: The address rearrangements and butterfly layers of the synthetic transforms cost $O(Vu^\tau)$ and $O(Vd^{\lambda'})$ for stored bit volume $V$, a power saving below the linear-per-level cost.
How: build each procedure from a fixed linear network whose smaller calls number $s<Wm$ and recurse

**S5**: The convolution of the digit list is computed by convolution over the polynomial ring using the transforms of S4.
How: chain of reductions taken from the ring end: ring products, resampling and chirps, then the prime-axis address map

**S7**: A compatible choice of rational parameters makes every term of the cost table fit $O(n(\lg n)^{1-\kappa})$.
Source: "For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient" (paper)
> For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Multiplication as digit convolution](radix-digit-convolution.md)): Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.
- S2 (on [Polynomial ring modulo y^r + 1](poly-ring-y-r-1.md)): One coordinate is stored as a polynomial modulo $y^r+1$, so powers of $y$ are roots of unity.
- S3 (on [Synthetic polynomial transforms](synthetic-transforms.md)): Multiplication by a root of unity in the remaining axes is a signed shift, so synthetic transforms consist of shifts, butterflies and rearrangements.
- S6 (on [Fixed-point precision and exact recovery](fixed-point-precision.md)): Known normalizations are removed, the coefficient error is below $1/2$, and rounding with carry propagation gives the exact binary product.
- S4.1 (on [Elementary tape streams and scans](tape-streams.md)): Elementary scans, controlled shifts and fixed scalings on tape streams each cost linear time in the stored volume $V$.
- S4.2 (on [Linear networks with frames and roles](gate-frames.md)): A fixed linear network exchanging banks of values, with an invertible frame per gate, restores all auxiliary values and leaves only the endpoint operator on every role array.
- S4.3 (on [Finite networks with rank saving](finite-network-subspaces.md)): Networks built from three-element subsets with nested subspaces of an $m$-dimensional space need only $s<Wm$ smaller calls.
- S4.4 (on [Recursive power saving](recursive-power-saving.md)): A recursive call at parameter $mf$ uses $s$ calls at parameter $f$ on volume $V/W$ each, so cost per volume grows with an exponent below 1.
- S4.5 (on [Fast interchange of address chunks](address-interchange.md)): Two address fields of $u$ bits are interchanged in cost $O(Vu^\tau)$ with $\tau<1$, by XOR combinations whose final effect is an exact permutation.
- S4.6 (on [Simultaneous butterfly layers](fast-butterfly-layers.md)): The layer $H_0(u,v)=((u+v)/2,(u-v)/2)$ is applied simultaneously on selected address bits of $d$ chunks in cost $O(Vd^{\lambda'})$ with $\lambda'<1$.
- S5.4 (on [Signed packing (Kronecker substitution)](signed-packing.md)): Polynomial products in the ring are computed by signed packing and the $O(n\log n)$ multiplier as a subroutine.
- S5.2 (on [Gaussian resampling](gaussian-resampling.md)): Gaussian resampling expresses each source Fourier transform through a transform with power-of-two axis lengths.
- S5.3 (on [Bluestein chirp identity](bluestein-chirp.md)): Bluestein's chirp identity turns the middle transform into a normalized cyclic convolution.
- S5.1 (on [Chinese-remainder address map](crt-address-map.md)): The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a convolution-preserving Chinese-remainder map.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md): The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Schönhage–Strassen n log n conjecture
- [Fast interchange of address chunks](address-interchange.md): Interchanges two address fields of u bits in cost O(V u^τ), τ<1, through XOR combinations whose final effect is an exact permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast interchange of address chunks
- [Simultaneous butterfly layers](fast-butterfly-layers.md): Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected address bits of d chunks at cost O(V d^λ'), λ'<1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Simultaneous butterfly layers
- [Gaussian resampling](gaussian-resampling.md): The Harvey–van der Hoeven identity expressing a transform of arbitrary axis length through a transform with power-of-two axis lengths.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Chinese-remainder address map](crt-address-map.md): A map placing the coefficient list on a product of distinct prime cyclic axes that preserves convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder address map
- [Bluestein chirp identity](bluestein-chirp.md): Rewrites a transform as a normalized cyclic convolution via chirp phase factors.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp identity
- [Signed packing (Kronecker substitution)](signed-packing.md): Packing polynomial coefficients into one long integer with signs so ring products are computed by an ordinary O(n log n) integer multiplier.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Signed packing (Kronecker substitution)
- [Fixed-point precision and exact recovery](fixed-point-precision.md): Complex fixed-point coefficients with dyadic intermediates, one truncation, and an error bound below 1/2 that allows exact rounding and carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fixed-point precision and exact recovery
- [Synthetic polynomial transforms](synthetic-transforms.md): Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplications are signed shifts and the work is butterflies, shifts and address rearrangements.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Synthetic polynomial transforms

## Other pages you may link to

- [Convolution and discrete Fourier transform](dft-convolution.md)
- [Multiplication as digit convolution](radix-digit-convolution.md)
- [Polynomial ring modulo y^r + 1](poly-ring-y-r-1.md)
- [Elementary tape streams and scans](tape-streams.md)
- [Linear networks with frames and roles](gate-frames.md)
- [Finite networks with rank saving](finite-network-subspaces.md)
- [Recursive power saving](recursive-power-saving.md)

## Evidence from the sources, with the paragraph around each quote

- "Its worst-case running time satisfies" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "For the cost calculation put $V=Tp=\Theta(n)$." (paper)

  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}


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

Write the body to `exegenius/tasks/0020-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0020-write-main-theorem.answer.json`, then run `exegenius submit 0020-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0020-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
