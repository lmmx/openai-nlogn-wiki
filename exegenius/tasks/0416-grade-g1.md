# exegenius task 0416-grade-g1

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Summarise in a few sentences what the main theorem says about multiplying two n-bit integers, in which machine model it holds, which earlier conjecture it refutes, and the overall plan the proof follows to get there.

## Key points

1. One deterministic machine with a fixed alphabet and a fixed number of one-dimensional tapes multiplies two n-bit numbers exactly in time O(n (log n)^(1-kappa)), with kappa = 2^-182 > 0.
2. This is asymptotically faster than n log n, so it refutes the 1971 Schoenhage-Strassen guess that n log n is optimal for multitape machines.
3. The plan is to build two cheaper tape primitives (swapping address chunks and a combined butterfly layer), use them to speed up Fourier-style transforms and ring convolution, and reduce the integer product to such convolutions.
4. The result is exact because the accumulated numerical error on the recovered coefficients is below 1/2, so rounding gives the true integers; the cost total then shows a power of log n is saved.

## Answers

### Answer A

The main theorem (Power-saving integer multiplication) says that one fixed deterministic Turing machine, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, multiplies two n-bit integers exactly in time O(n(lg n)^(1-kappa)) with kappa = 2^-182, which is o(n log n). The machine model is that deterministic tape machine, correct for every n >= 1. The theorem refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers in this model. The proof plan: (1) build two power-saving tape procedures, a chunk interchange and a Simultaneous butterfly layer (one pass doing a round of butterfly steps on up to d axes at once), from fixed finite linear networks; (2) use them to speed up the synthetic transforms and the ring convolution built on them; (3) use Gaussian resampling and chirps to turn prime-length transforms into power-of-two ones, cancelling permutations rather than sorting them; (4) assemble the exact 2n-bit product from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below 1/2; then total the cost, which shows that a power of lg n is saved.

### Answer B

Main result: a single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^{1-kappa}) worst-case time with kappa = 2^{-182}. Its time divided by n lg n tends to zero, so it refutes the conjecture of Schonhage and Strassen that n log n is the best possible order of growth in this model. Plan: the integer product is turned into a Cyclic convolution of short digit coefficients, and the Discrete Fourier transform turns a Cyclic convolution into pointwise multiplication. On a tape machine each transform level costs a full pass, so two primitives (chunk interchange and Simultaneous butterfly layer) are made to cost volume times a power below one of their width: a call at parameter mf makes s < Wm smaller calls, using nested subspace labels on a fixed linear exchange network. These speed up the synthetic transforms and the ring convolution. Prime-length transforms are reduced to power-of-two ones by Gaussian resampling and Bluestein chirps, with permutations kept inside the identities rather than executed. The exact 2n-bit product is then assembled by two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carry propagation, with total error below 1/2. Cost accounting divides every cost by the volume and shows that a power of lg n is saved.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Grade": {
      "additionalProperties": false,
      "properties": {
        "contradicted": {
          "description": "Numbers of the key points the answer contradicts.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "covered": {
          "description": "Numbers of the key points the answer makes.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "label": {
          "description": "The answer's letter.",
          "type": "string"
        },
        "wrong": {
          "description": "Wrong claims in the answer that contradict no key point.",
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "required": [
        "label",
        "covered",
        "contradicted",
        "wrong"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "grades": {
      "items": {
        "$ref": "#/$defs/Grade"
      },
      "type": "array"
    }
  },
  "required": [
    "grades"
  ],
  "title": "GradeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0416-grade-g1.answer.json`, then run `exegenius submit 0416-grade-g1` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0416-grade-g1`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
