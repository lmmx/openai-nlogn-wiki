# exegenius task 0417-grade-g2

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?

## Key points

1. A transform on Theta(n) stored bits has about log n levels, and a tape machine must scan the whole array to do each level.
2. Each full scan costs time linear in the data, so scanning per level adds up to n log n for the whole transform.
3. So to get below n log n, many levels must be handled in one pass: moving data between address positions and doing butterfly arithmetic on several address bits together must cost less than one pass each.
4. This is why the proof builds the chunk-interchange and simultaneous-layer primitives with sub-linear cost per unit of data per level.

## Answers

### Answer A

On a tape machine a standard FFT-style transform on n bits has a fixed number of two-point levels, Theta(log n) of them. Each level has to bring the two partners of every butterfly together (address movement) and then apply the butterfly arithmetic. On a tape machine that costs one full pass over the stored volume of Theta(n) bits per level, so the levels together cost Theta(n log n). The page says the level count is fixed by the two-point structure, so the number of levels cannot be reduced; only the cost of a level can shrink. A level's cost is movement plus arithmetic, so only cheaper movement and cheaper arithmetic can beat n log n. The construction then lets one pass do the work of several levels: interchanging two address chunks of u bits costs O(V u^tau) with tau = 1 - 2^-50, and the Simultaneous butterfly layer performs one round of butterflies on up to d axes at once in time O(V d^lambda') with lambda' < 1, instead of d separate passes. The total saving is a power of log n with exponent kappa = 2^-182, so the time is O(n (lg n)^(1-kappa)). Other tweaks to the multiplier are not addressed on these pages; the argument that they cannot help depends on the claim that the level count is fixed, which the pages state without proof.

### Answer B

The log n factor is the number of levels times the cost of one level. A standard FFT-style transform on a tape is a sequence of Theta(log n) levels of two-point (butterfly) steps, each acting on one address bit. Each level needs the paired entries brought together (movement) and then the butterfly arithmetic. Done naively, every level is one linear pass over the Theta(n) stored bits, so the total is Theta(n log n). The number of levels is fixed by the two-point structure, so the only remaining lever is the cost of a level. Movement is expensive on a tape because a head crosses one cell per step, so a pair that is far apart on the tape costs its distance to meet. The arithmetic is t/2 butterflies and t/2 twiddle multiplications per layer. The later tape procedures (chunk interchange and Simultaneous butterfly layer) make the movement and the layer work cheaper, each costing the volume times a power below one of its width, and this is what saves a power of log n. Caveat: the pages do not show that no other tweak of the transform could help. The 'only' claim rests on a sentence attributed to an unnamed 'same source', and the pages never discuss whether a larger (higher-radix) butterfly could reduce the number of levels.

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

Write the answer to `exegenius/tasks/0417-grade-g2.answer.json`, then run `exegenius submit 0417-grade-g2` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0417-grade-g2`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
