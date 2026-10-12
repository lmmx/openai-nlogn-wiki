# exegenius task 0018-write-linear-network

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

For these sources: The reader has an undergraduate computer science education at introductory depth: discrete mathematics (integers, divisibility, modular arithmetic, gcd and primes, binomial coefficients, induction, the field of two elements with XOR), algorithms (the big-O family, divide-and-conquer recurrences, the RAM and multitape Turing models), calculus (limits, convergence of sequences and series, geometric series, basic integrals), elementary linear algebra over the reals and F_2 (vector spaces, linear maps, rank, dot products, matrix products), and complex numbers with modulus and polar form. The reader has not reached specialist algebra, tensor products, bilinear forms, eigen-theory beyond the basics, analysis (liminf and limsup), or numerical analysis, so the main theorem's proof and its network and transform machinery must be explained.

The reader already understands these concepts:

- Big-O notation (also: O-notation)
- Complex numbers
- Polynomials
- Multitape Turing machine (also: Turing machine, tape)
- Linear algebra over a field (also: invertible linear operator, subspace, matrix rank)
- Fixed-tape machine model (also: fixed finite-tape model)
- Logarithms and exponentials (also: log, logarithm base 2, log_2, lg, binary logarithm, natural logarithm, exp, e^x, change of base)
- Floor and ceiling functions (also: floor, ceiling, integer part, round down, round up, lfloor x rfloor, lceil x rceil)
- Positional (radix) representation (also: binary representation, base-b expansion, radix representation, positional notation, digit string, bit string, padded binary, most significant bit)
- Field of two elements (also: F_2, GF(2), binary field, Z/2Z, field of order 2)
- Bitwise XOR (also: exclusive or, XOR, addition modulo 2 of bits, symmetric difference of bits)
- Modular arithmetic and congruences (also: congruence modulo m, residues modulo m, integers mod m, Z/mZ, mod m arithmetic, residue classes)
- Greatest common divisor and the Euclidean algorithm (also: gcd, greatest common divisor, relatively prime, coprime, Euclidean algorithm, extended Euclidean algorithm)
- Prime numbers (also: primes, prime factorization, distinct primes, prime modulus, prime power)
- Binomial coefficients and counting subsets (also: n choose k, binom(n,k), choose function, number of k-element subsets, k-subsets)
- Mathematical induction (also: proof by induction, induction on n, strong induction, recursion on the number of ranges)
- Divide-and-conquer recurrence (also: recurrence relation, recursive cost recurrence, recursion tree, master theorem, unrolling a recurrence)
- Random-access machine model (also: RAM model, word RAM, unit-cost RAM, random access machine)
- Limits and convergence of sequences (also: limit of a sequence, convergent sequence, limit as n tends to infinity, tends to zero, epsilon-N definition)
- Convergence of series (also: convergent series, infinite series, sum of a series, absolute convergence, partial sums)
- Geometric series (also: geometric sum, sum of powers of a ratio, geometric progression sum)
- Big-Omega, big-Theta and little-o notation (also: big-Omega, Omega notation, big-Theta, Theta notation, little-o, small-o notation, asymptotically smaller)
- Dot product and orthogonal vectors (also: inner product, scalar product, orthogonality, perpendicular vectors, orthogonal vectors)
- Matrix product, transpose, and special matrices (also: matrix multiplication, transpose, diagonal matrix, upper triangular matrix, lower triangular matrix, permutation matrix, identity matrix)
- Complex modulus, conjugate and polar form (also: absolute value of a complex number, magnitude, complex conjugate, argument of a complex number, unit circle, Euler's formula, e^(i theta))
- Fixed-point arithmetic (also: fixed-point number, fixed-point representation, binary fixed-point, signed fixed-point, guard bits)

## This page

Concept: Linear network that restores auxiliary values
Gloss: A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state.
Also called: exchange network, network, pointwise linear gate

## This page in the argument

The step: A fixed linear network of three-element-subset gates exchanges the banks $X_a$ and $Y_a$ with signs and restores every scratch wire.
How: a three-stage bank exchange built from copy, gather, scatter and side-injection rows, with the inverse schedule at the middle stage
Why: A schedule that subtracts the old scratch contents, runs the computation, adds the result and then undoes the schedule cancels arbitrary initial scratch values. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- A forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged, for arbitrary initial scratch values.
- The three-stage composition exchanges $X_a$ and $Y_a$ with a sign and restores every auxiliary value.

It serves these steps, from the main result down:

- The subset-intersection network has a total number $s$ of smaller calls with $s<Wm$, where $W$ is its wire count and $m$ the dimension of its label space.; how: exchange the two banks with a scalar network whose gates carry subspace labels from triples, then bound the total dimension change of the labels by counting dimension losses (on [Subset-intersection network](subset-network.md))

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $F$ (scalar field), bound on [Linear algebra over a field](linear-algebra.md): The field of scalars over which vector spaces and linear maps are taken.
- $V$ (vector space), bound on [Linear algebra over a field](linear-algebra.md): A vector space over F, the set of vectors on which linear maps act.
- $T$ (linear map), bound on [Linear algebra over a field](linear-algebra.md): A linear map from V to itself, whose rank and invertibility are discussed.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear algebra over a field](linear-algebra.md): The theory of vector spaces, linear maps, invertible operators, subspaces, and the rank of a linear map.
  Shown as: Linear network that restores auxiliary values *<predicate>* Linear algebra over a field
- [Fixed-tape machine model](fixed-tape-machine.md): A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step moves each head by at most one cell.
  Shown as: Linear network that restores auxiliary values *<predicate>* Fixed-tape machine model

## Pages that build on this one

- Frame of a network vertex: An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented.
- Subset-intersection network: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.

## Other pages you may link to

- [Frame of a network vertex](frame.md)
- [Subset-intersection network](subset-network.md)

## Evidence from the sources, with the paragraph around each quote

- "Each procedure arises from its own fixed linear network that exchanges two banks of values" (paper)

  > Each procedure arises from its own fixed linear network that exchanges two banks of values, with prescribed signs, and restores every auxiliary value. A wire's fixed place in the network is called its role. To use the network on an array, regard a row as the complete ordered suffix, including all active address fields, at a fixed prefix and row index. Distribute rows cyclically among the $W$ roles, padding the row count for each prefix to a multiple of $W$. Let $V$ now denote the node volume after padding. All role streams have the same local address set and each contains $V/W$ bits. A scalar gate is then applied pointwise to matching addresses on the roles that it touches.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "Rows 0 and 1 subtract the side injection and scatter of $p$ and $q$, so old scratch contents do not survive in the targets." (The page refers to rows 0 to 7 of a schedule but never shows that schedule; the reader cannot see which gates each row applies, so cannot check that the rows cancel the initial scratch and central values.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "The net change is independent of $p$ and $q$." (This claim follows from the unshown row schedule and is not derived on the page; the reader cannot check it.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "the coefficient of $x_T$ in $y_S$ is $|S\cap T|\bmod 2$" (This is the net effect of a forward invocation, which is how the page's own construction works, and it is attributed to a source without the page deriving it from the four gates; the reader cannot check the coefficient from what the page gives.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "side injection cancels the cases $|S\cap T|=1$, leaving only $T=S$" (The page asserts that side injection removes the neighbor contributions and leaves only the diagonal term, but does not compute this from the gate definitions or the row schedule.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Stage 2 is the inverse schedule, with source $Y$ and target $X$" (The page never says which gates or row order make up the inverse schedule or why it reverses stage 1; its stated net effect X gets X minus Y is therefore not checkable.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- The reader cannot follow this step: "Starting from $X=x$ and $Y=y$, the stages give $(x,y+x)$, $(-y,y+x)$, then $(-y,x)$." (The stage values are computed for single values x and y, while the banks are indexed by a with three coordinates; the page does not show how each stage's effect on fibers combines into the stated net map, and it relies on the unchecked stage effects above.). Give the reasoning on this page. If the step rests on a result from prior work, say what the result states and why it applies here, and cite the source for its proof: a citation alone does not explain a step.
- Say what $T$ denotes where it is first used: the page uses it before saying so in "Let $S,T\in\mathcal T$ be the varying coordinates of a forward invocation"

## Previous version (revise it)

It has 344 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 430 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

A linear network that restores auxiliary values is a fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state. The [Subset-intersection network](subset-network.md) uses it.

Let $[h]=\{1,\dots,h\}$, where $h$ is the number of elements of the ground set. Let $\mathcal T$ be the set of three-element subsets of $[h]$, and write $v=\binom{h}{3}$ for the number of its elements. Two data banks $X_a$ and $Y_a$ are indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. The network is a linear operator in [Linear algebra over a field](linear-algebra.md). It has the fixed structure of a [Fixed-tape machine model](fixed-tape-machine.md): a fixed set of wires and a schedule that does not depend on the values it carries.

At stage $j$, fix the other two coordinates of $a$ and operate on the $v$ values obtained by varying coordinate $j$. Let $S,T\in\mathcal T$ be the varying coordinates of a forward invocation, which takes controls $x_T$ and targets $y_S$. In the bit construction, scalars lie in $\mathbb F_2$ and $S,T$ are neighbors when $|S\cap T|=1$. For each neighboring ordered pair $(S,T)$ there is a scratch wire $A_{ST}$, and for each $i\in[h]$ a central wire $C_i$. The gates are:

- copy, adding $x_T$ to $A_{ST}$;
- gather, adding $\sum_{T\ni i}x_T$ to $C_i$;
- scatter, adding $\sum_{i\in S}C_i$ to $y_S$;
- side injection, adding $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$.

Let $p$ and $q$ be the initial values of the $A_{ST}$ and $C_i$. Rows 0 and 1 subtract the side injection and scatter of $p$ and $q$, so old scratch contents do not survive in the targets. Rows 2 and 3 copy and gather the controls. Rows 4 and 5 add scatter and side injection of the updated scratch values, and rows 6 and 7 undo gather and copy. The net change is independent of $p$ and $q$. In the bit construction the coefficient of $x_T$ in $y_S$ is $|S\cap T|\bmod 2$, and side injection cancels the cases $|S\cap T|=1$, leaving only $T=S$. <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.</cite>

Stage 1 is a forward invocation from $X$ to $Y$. Stage 2 is the inverse schedule, with source $Y$ and target $X$, whose net effect is $X\gets X-Y$. Stage 3 repeats stage 1. Starting from $X=x$ and $Y=y$, the stages give $(x,y+x)$, $(-y,y+x)$, then $(-y,x)$. The composition therefore sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$, and every scratch wire is restored. <cite data-source="paper">In the bit construction this is the permutation exchanging $X_a$ and $Y_a$.</cite>

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

Write the body to `exegenius/tasks/0018-write-linear-network.answer.md` and the JSON to `exegenius/tasks/0018-write-linear-network.answer.json`, then run `exegenius submit 0018-write-linear-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
