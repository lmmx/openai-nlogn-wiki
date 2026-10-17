# exegenius task 0355-attribute-g1

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there.

## Key points

1. One deterministic machine with a fixed alphabet and a fixed number of one-dimensional tapes multiplies two n-bit numbers exactly in time O(n (log n)^(1-kappa)), with kappa = 2^-182 > 0.
2. This is asymptotically faster than n log n, so it refutes the 1971 Schoenhage-Strassen guess that n log n is optimal for multitape machines.
3. The plan is to build two cheaper tape primitives (swapping address chunks and a combined butterfly layer), use them to speed up Fourier-style transforms and ring convolution, and reduce the integer product to such convolutions.
4. The result is exact because the accumulated numerical error on the recovered coefficients is below 1/2, so rounding gives the true integers; the cost total then shows a power of log n is saved.

## Answers

### Answer 1

The main theorem says that one deterministic Turing machine, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, multiplies two n-bit integers exactly in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^-182. The wiki calls this model a Fixed finite-tape machine model. The result refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers on that model. The proof plan is: (1) build two power-saving tape procedures, an address-chunk interchange and a Simultaneous butterfly layer, from fixed linear networks; (2) use them to speed up the synthetic transforms and the ring convolution; (3) use Gaussian resampling and Bluestein chirps to turn prime-length transforms into power-of-two ones, leaving permutations inside the transform identities rather than executing them; (4) assemble the exact 2n-bit product from radix digits, with total error below 1/2 so rounding recovers the exact integers; (5) total the cost after dividing by the volume, and show that a power of log n is saved.

Covers key points: 1, 2, 3, 4

Quotations:

1. "The target is a deterministic Turing machine, with a fixed alphabet and a fixed number of tapes"
2. "A machine has a single finite alphabet and a finite number of one-dimensional tapes, both fixed independently of the input."
3. "best possible order of growth for the time to multiply two integers"
4. "so it refutes the [Schönhage–Strassen optimality conjecture](kaf) in this model."
5. "Build two power-saving tape procedures (chunk interchange and Simultaneous butterfly layer) from fixed finite linear networks"
6. "use Gaussian resampling with retained permutations and chirps to reduce the prime-length Cyclic convolution of the radix-digit coefficients to those power-of-two transforms"
7. "assemble the exact product with a proof that the error is below $1/2$"
8. "The multiplication algorithm chains the reductions of the earlier pages to turn two $n$-bit integers into their exact $2n$-bit product."
9. "so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$"

### Answer 2

Power-saving integer multiplication's main result: a single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1-kappa)) time, with kappa = 2^(-182). That is o(n log n), so it refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers on such a machine. The plan: (1) build two tape primitives, the interchange of address chunks and the Simultaneous butterfly layer, from fixed finite linear networks, each costing the data volume times a power below one of its width; (2) use them to speed up the synthetic transforms over C[y]/(y^r+1) and the ring convolution built on them; (3) use Gaussian resampling resampling with chirps to turn prime-length transforms into power-of-two ones, with permutations cancelled rather than executed; (4) assemble the exact 2n-bit product from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below 1/2; (5) total the cost per stored bit: the seven dominant terms are powers of p below one with minimum margin 2kappa, so the total is O(n(lg n)^(1-kappa)).

Covers key points: 1, 2, 3, 4

Quotations:

1. "Power-saving integer multiplication is the main result: for $n$, the number of bits in each input, and $\kappa=2^{-182}$, the exponent saved from the power of $\lg n$, a fixed Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$, which is $o(n\log n)$, so it refutes the [Schönhage–Strassen optimality conjecture](kaf) in this model."
2. "The machine is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$."
3. "The Schönhage–Strassen optimality conjecture is the claim that $n\log n$ is the best possible order of growth for the time to multiply two integers, where $n$ is the number of bits in each"
4. "for every multiplication machine there are a constant $c>0$ and a threshold such that the machine needs at least $c\,n\log n$ steps whenever $n$ exceeds the threshold."
5. "The conjecture is stated for the [Fixed finite-tape machine model](tuf): a Fixed finite-tape machine model with a fixed alphabet and a fixed number of one-dimensional tapes."
6. "Two tape primitives, the interchange of address chunks and the [Simultaneous butterfly layer](tiz), are built from fixed finite linear networks. Each costs the data volume times a power below one of its width, by [Recursive power saving](rut)."
7. "Recursive power saving is the recurrence that makes both tape procedures, the interchange of two address chunks and the Simultaneous butterfly layer, cost the volume times a power below one of their parameter."
8. "The children cost $s(V/W)\mathcal C(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$"
9. "The Simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\le d$ selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\lambda'}),$ $\lambda'<1,$ instead of $D$ passes"
10. "These speed up the synthetic transforms over $\mathbb C[y]/(y^r+1)$ ([Tape layout for synthetic transforms](mov)) and the ring convolution built on them ([Convolution from the retained transform layout](tab))."
11. "Convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by transforming both operands, multiplying records pointwise and transforming back."
12. "Gaussian resampling expresses a Discrete Fourier transform of length $s$, the source length, through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm."
13. "with permutations cancelled rather than sorted"
14. "The exact $2n$-bit product is assembled by [The multiplication algorithm](siz) from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below $1/2$."
15. "Exactness is shown by [Error tracking and exact recovery](mes): the error on these coefficients is below $1/2$, so rounding is exact."
16. "The transform diagonalizes [Cyclic convolution](fam): the transform of a convolution is a pointwise product of transforms."
17. "Repeated over the address bits of an array, with twiddle multiplications between layers, it computes the [Discrete Fourier transform](kur) of an array in $\log_2 t$ layers instead of $t^2$ operations."
18. "The total time of the machine is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$: after dividing each cost by $V=Tp=\Theta(n)$ the dominant terms are powers of $p$ below one, with minimum margin $2^{-181}=2\kappa$."

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Attribution": {
      "additionalProperties": false,
      "properties": {
        "answer": {
          "description": "Number of the answer, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "support": {
          "items": {
            "$ref": "#/$defs/Support"
          },
          "type": "array"
        }
      },
      "required": [
        "answer",
        "support"
      ],
      "type": "object"
    },
    "Support": {
      "additionalProperties": false,
      "description": "The quotation that supports one covered key point.",
      "properties": {
        "point": {
          "description": "Number of the key point.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "quotation": {
          "description": "Number of the quotation under the answer.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        }
      },
      "required": [
        "point",
        "quotation"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "answers": {
      "description": "One entry for every answer listed.",
      "items": {
        "$ref": "#/$defs/Attribution"
      },
      "type": "array"
    }
  },
  "required": [
    "answers"
  ],
  "title": "AttributeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0355-attribute-g1.answer.json`, then run `exegenius submit 0355-attribute-g1` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0355-attribute-g1`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
