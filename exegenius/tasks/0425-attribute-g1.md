# exegenius task 0425-attribute-g1

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

The main theorem (Power-saving integer multiplication) says that one fixed deterministic Turing machine, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, multiplies two n-bit integers exactly in time O(n(lg n)^(1-kappa)) with kappa = 2^-182, which is o(n log n). The machine model is that deterministic tape machine, correct for every n >= 1. The theorem refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers in this model. The proof plan: (1) build two power-saving tape procedures, a chunk interchange and a Simultaneous butterfly layer (one pass doing a round of butterfly steps on up to d axes at once), from fixed finite linear networks; (2) use them to speed up the synthetic transforms and the ring convolution built on them; (3) use Gaussian resampling and chirps to turn prime-length transforms into power-of-two ones, cancelling permutations rather than sorting them; (4) assemble the exact 2n-bit product from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below 1/2; then total the cost, which shows that a power of lg n is saved.

Covers key points: 1, 2, 3, 4

Quotations:

1. "Power-saving integer multiplication is the main result: for $n$, the number of bits in each input, and $\kappa=2^{-182}$, the exponent saved from the power of $\lg n$, one fixed Turing machine multiplies two $n$-bit integers exactly in time $O(n(\lg n)^{1-\kappa})$, which is $o(n\log n)$, so it refutes the [Schönhage–Strassen optimality conjecture](kaf) in this model."
2. "The machine is deterministic, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$."
3. "The Schönhage–Strassen optimality conjecture is the claim that $n\log n$ is the best possible order of growth for the time to multiply two integers, where $n$ is the number of bits in each;"
4. "The remedy is to let one pass do the work of many levels, which needs cheaper movement and cheaper arithmetic together"
5. "Both primitives are built from fixed finite linear networks and are power-saving by [Recursive power saving](rut)."
6. "Recursive power saving is the recurrence that makes both tape procedures, the interchange of two address chunks and the Simultaneous butterfly layer, cost the stream volume times a power below one of their parameter."
7. "They speed up the synthetic transforms ([Tape layout for synthetic transforms](mov)) and the ring convolution built on them ([Convolution from the retained transform layout](tab))."
8. "with permutations cancelled rather than sorted ([Retained permutation cancellation](zom))."
9. "The exact $2n$-bit product is assembled by [The multiplication algorithm](siz) from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below $1/2$."
10. "The time is then $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$, with the finitely many small lengths handled by schoolbook multiplication."

### Answer 2

Main result: a single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^{1-kappa}) worst-case time with kappa = 2^{-182}. Its time divided by n lg n tends to zero, so it refutes the conjecture of Schonhage and Strassen that n log n is the best possible order of growth in this model. Plan: the integer product is turned into a Cyclic convolution of short digit coefficients, and the Discrete Fourier transform turns a Cyclic convolution into pointwise multiplication. On a tape machine each transform level costs a full pass, so two primitives (chunk interchange and Simultaneous butterfly layer) are made to cost volume times a power below one of their width: a call at parameter mf makes s < Wm smaller calls, using nested subspace labels on a fixed linear exchange network. These speed up the synthetic transforms and the ring convolution. Prime-length transforms are reduced to power-of-two ones by Gaussian resampling and Bluestein chirps, with permutations kept inside the identities rather than executed. The exact 2n-bit product is then assembled by two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carry propagation, with total error below 1/2. Cost accounting divides every cost by the volume and shows that a power of lg n is saved.

Covers key points: 1, 2, 3, 4

Quotations:

1. "The target is a deterministic Turing machine, with a fixed alphabet and a fixed number of tapes, that multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa = 2^{-182}$."
2. "that $n\log n$ is the best possible in the"
3. "A machine has a single finite alphabet and a finite number of one-dimensional tapes, both fixed independently of the input."
4. "In 1971 Schönhage and Strassen gave a multiplication algorithm running in $O(n\log n\log\log n)$ time, and proposed $n\log n$ as the optimal order of growth."
5. "The machine is deterministic, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$."
6. "The multiplication reduces to transforms on arrays of polynomials over $\mathbb C[y]/(y^r+1)$, whose calculation consists of address rearrangements, signed shifts and two-point butterflies."
7. "On a tape machine that is one pass over the whole stored volume of $\Theta(n)$ bits per level, so the levels cost $\Theta(n\log n)$."
8. "The remedy is to let one pass do the work of many levels, which needs cheaper movement and cheaper arithmetic together"
9. "The Simultaneous butterfly layer applies the two-point step $H_0(u,v)=((u+v)/2,(u-v)/2)$ to one bit of each of $D\le d$ selected address chunks"
10. "so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter."
11. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$, and an interchange costs $O(Vf^\tau)$."
12. "Source dimensions sum to $N$, sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$."
13. "The exact $2n$-bit product of the two inputs is obtained from the radix-digit convolution by the chain"
14. "The error on the recovered integer coefficients is below $1/2$, so rounding gives the exact integer coefficients, and carry propagation yields the exact binary product."
15. "Cyclic convolution is the product of two sequences whose indices wrap around"
16. "the transform of a convolution is a pointwise product of transforms."

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

Write the answer to `exegenius/tasks/0425-attribute-g1.answer.json`, then run `exegenius submit 0425-attribute-g1` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0425-attribute-g1`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
