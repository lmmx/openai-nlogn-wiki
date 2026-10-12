# exegenius task 0021-audit-linear-algebra

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education at introductory depth: discrete mathematics (integers, divisibility, modular arithmetic, gcd and primes, binomial coefficients, induction, the field of two elements with XOR), algorithms (the big-O family, divide-and-conquer recurrences, the RAM and multitape Turing models), calculus (limits, convergence of sequences and series, geometric series, basic integrals), elementary linear algebra over the reals and F_2 (vector spaces, linear maps, rank, dot products, matrix products), and complex numbers with modulus and polar form. The reader has not reached specialist algebra, tensor products, bilinear forms, eigen-theory beyond the basics, analysis (liminf and limsup), or numerical analysis, so the main theorem's proof and its network and transform machinery must be explained.

## Known concepts

- Big-O notation (also: O-notation)
- Complex numbers
- Polynomials
- Multitape Turing machine (also: Turing machine, tape)
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

## Symbols bound on earlier pages

None of this page's symbols is bound on an earlier page.

## Pages in the wiki

- [Linear algebra over a field](linear-algebra.md)
- [Fixed-tape machine model](fixed-tape-machine.md)
- [Linear network that restores auxiliary values](linear-network.md)
- [Frame of a network vertex](frame.md)
- [Subset-intersection network](subset-network.md)

## Page to audit (`linear-algebra`)

````markdown
# Linear algebra over a field

Linear algebra over a field is the theory of vector spaces, linear maps, invertible operators, subspaces and rank, with scalars taken from any field rather than only the reals. It is needed here because the main argument's network, a fixed wiring of gates in which each gate applies a linear rule to the arrays on its wires, changes how each array is stored from one gate to the next by invertible linear maps.

Let $F$ be a field, the set of scalars. The reader's cases are the real numbers and the field of two elements $F_2$.

A vector space over $F$ is a set $V$ of vectors with an addition and with multiplication by scalars from $F$, obeying the usual rules. For vectors $u,v$ in $V$ and a scalar $a$ in $F$, one such rule is $a(u+v)=au+av$. A subspace of $V$ is a subset that contains $0$ and is closed under addition and under multiplication by scalars; it is a vector space in its own right.

A linear map $T\colon V\to V$ is a map of $V$ into itself with $T(u+v)=T(u)+T(v)$ and $T(au)=aT(u)$. Its image $T(V)$ is a subspace. The rank of $T$ is the dimension of this image, the number of vectors in a basis of it; for a matrix, it is the largest number of linearly independent columns.

The map $T$ is invertible when some linear map $S\colon V\to V$ satisfies $ST=TS=\mathrm{id}$, the identity map; such an $S$ is the inverse, written $T^{-1}$. On a finite-dimensional space, $T$ is invertible exactly when its rank equals $\dim V$, the dimension of $V$. A composite of invertible maps is invertible, with $(ST)^{-1}=T^{-1}S^{-1}$.

Example: over $F_2$, the matrix $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ acts on $F_2^2$ with columns $(1,0)$ and $(1,1)$, which are linearly independent. So it has rank $2=\dim F_2^2$ and is invertible. Its square is the identity matrix over $F_2$, so it is its own inverse.

This gives the cancellation the network needs. A route through the network multiplies the operators met along it, and each intermediate operator is followed by its inverse, so only the operators at the two endpoints remain.
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0021-audit-linear-algebra.answer.json`, then run `exegenius submit 0021-audit-linear-algebra` in the project directory. If submit rejects the answer, fix the answer and submit again.
