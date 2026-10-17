# exegenius task 0422-grade-g7

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

The classical FFT-style approach to multiplying n-bit integers does Theta(log n) levels of butterfly work over Theta(n) stored bits. Why does that alone suggest n log n on a tape machine, and where does the new algorithm look for savings to get below it?

## Key points

1. On a tape machine every level of the transform must sweep through all the Theta(n) stored bits, so Theta(log n) levels cost Theta(n log n) in total.
2. So the log factor can only be beaten by making each level cost less than a full pass: cheaper movement of data between addresses on the tapes, and cheaper butterfly arithmetic that handles several address bits together.
3. The algorithm builds two such faster tape procedures (exchanging address chunks, and a combined butterfly layer over many axes) and plugs them into the transforms.
4. The machine has a fixed alphabet, a fixed number of tapes and heads that move one cell per step, so data cannot be reached at random and cost counts moves.

## Answers

### Answer A

The classical transform has Theta(log n) levels, and each level has to bring the partners of every butterfly together and then combine them. On a tape machine each level is one sequential pass over all Theta(n) stored bits, so the levels together cost Theta(n log n). That is why the classical approach alone suggests n log n. The new algorithm looks for savings in two places, and it needs both at once. First, movement: swapping two address chunks of u bits in one operation costs O(V u^tau) with a fixed tau < 1, so many address bits move at once instead of one level at a time. Second, arithmetic: one round of butterfly steps across up to d axes runs as a single pass in O(V d^lambda') with lambda' < 1, instead of d separate passes. A layout first gathers the bits of the axes so that many levels become one such round. The per-level cost then drops below a full pass because the recursion's branching ratio s/W is below m, which gives a power-saving exponent. The savings are all powers of the logarithm, so the single machine runs in O(n (lg n)^(1-kappa)) with kappa = 2^-182, which is o(n log n). Confidence is moderate to high on this outline. I followed the cited arguments but did not check the exponent margin arithmetic beyond the cited formulas, and I did not open the algebra pages behind the rank count s < Wm.

### Answer B

The classical transform on n-bit inputs runs Theta(log n) butterfly layers over Theta(n) stored bits. Each layer of t/2 butterflies and twiddle multiplications halves a length-t transform into two length-t/2 transforms, so the arithmetic per layer is small, but on a tape each layer needs at least one scan of all stored bits, and log n scans of n bits cost Theta(n log n). That is why the front page says the logarithmic factor can only be beaten by cheaper address movement or cheaper butterfly arithmetic. The new algorithm attacks both with two tape procedures. The first is a chunk interchange, which moves two address chunks of width u in O(V u^tau) time with tau = 1 - 2^-50. The second is the layer procedure (Simultaneous butterfly layer), which applies one bit of each of D selected chunks at once in O(V d^lambda') time with lambda' < 1, instead of one whole-array pass per bit. Both are recursive: a call at parameter mf makes s calls at parameter f on streams of volume V/W, with s < Wm, so each level of splitting multiplies the cost per unit volume by s/W < m, which gives a fixed power below linear in the parameter. The strict inequality s < Wm comes from a rank count on nested subspace labels that I could not verify in detail. The layer's two-point step is rewritten through a kernel C = aI + bX with C^2 = X. Summing all costs gives O(n (log n)^(1-kappa)) with kappa = 2^-182, which is the saving over n log n. I am confident of the mechanism and the scan argument. I am not confident of the exact rank count or of the constants, which the wiki states as choices.

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

Write the answer to `exegenius/tasks/0422-grade-g7.answer.json`, then run `exegenius submit 0422-grade-g7` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0422-grade-g7`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
