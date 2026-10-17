# exegenius task 0346-grade-g1

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

The main theorem says that one deterministic Turing machine, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, multiplies two n-bit integers exactly in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^-182. The wiki calls this model a Fixed finite-tape machine model. The result refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers on that model. The proof plan is: (1) build two power-saving tape procedures, an address-chunk interchange and a Simultaneous butterfly layer, from fixed linear networks; (2) use them to speed up the synthetic transforms and the ring convolution; (3) use Gaussian resampling and Bluestein chirps to turn prime-length transforms into power-of-two ones, leaving permutations inside the transform identities rather than executing them; (4) assemble the exact 2n-bit product from radix digits, with total error below 1/2 so rounding recovers the exact integers; (5) total the cost after dividing by the volume, and show that a power of log n is saved.

### Answer B

The background does not cover this question, so the reader cannot answer it. The reader knows schoolbook multiplication (O(n^2)) and Karatsuba's divide-and-conquer multiplication, and understands big-O notation, Turing machines with tapes at an introductory level, and binary representation. The reader has not been taught the discrete Fourier transform or FFT, nor the literature on fast integer multiplication, so they cannot state the main theorem, the machine model it holds in, the earlier conjecture it refutes, or the proof plan. Any specific claim about those would be a guess.

### Answer C

Power-saving integer multiplication's main result: a single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1-kappa)) time, with kappa = 2^(-182). That is o(n log n), so it refutes the Schönhage–Strassen optimality conjecture, the claim that n log n is the best possible order of growth for multiplying two integers on such a machine. The plan: (1) build two tape primitives, the interchange of address chunks and the Simultaneous butterfly layer, from fixed finite linear networks, each costing the data volume times a power below one of its width; (2) use them to speed up the synthetic transforms over C[y]/(y^r+1) and the ring convolution built on them; (3) use Gaussian resampling resampling with chirps to turn prime-length transforms into power-of-two ones, with permutations cancelled rather than executed; (4) assemble the exact 2n-bit product from radix digits, two forward transforms, a pointwise product, the opposite transform, rescaling, rounding and carries, with total error below 1/2; (5) total the cost per stored bit: the seven dominant terms are powers of p below one with minimum margin 2kappa, so the total is O(n(lg n)^(1-kappa)).

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

Write the answer to `exegenius/tasks/0346-grade-g1.answer.json`, then run `exegenius submit 0346-grade-g1` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0346-grade-g1`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
