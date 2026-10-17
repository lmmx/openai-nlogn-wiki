# exegenius task 0426-attribute-g2

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Why can the log n factor in n log n only be beaten here by making address movement and butterfly arithmetic cheaper, rather than by some other tweak of a standard FFT-style multiplier? What accounting of a standard transform on a tape machine leads to this?

## Key points

1. A transform on Theta(n) stored bits has about log n levels, and a tape machine must scan the whole array to do each level.
2. Each full scan costs time linear in the data, so scanning per level adds up to n log n for the whole transform.
3. So to get below n log n, many levels must be handled in one pass: moving data between address positions and doing butterfly arithmetic on several address bits together must cost less than one pass each.
4. This is why the proof builds the chunk-interchange and simultaneous-layer primitives with sub-linear cost per unit of data per level.

## Answers

### Answer 1

The log n factor is the number of levels times the cost of one level. A standard FFT-style transform on a tape is a sequence of Theta(log n) levels of two-point (butterfly) steps, each acting on one address bit. Each level needs the paired entries brought together (movement) and then the butterfly arithmetic. Done naively, every level is one linear pass over the Theta(n) stored bits, so the total is Theta(n log n). The number of levels is fixed by the two-point structure, so the only remaining lever is the cost of a level. Movement is expensive on a tape because a head crosses one cell per step, so a pair that is far apart on the tape costs its distance to meet. The arithmetic is t/2 butterflies and t/2 twiddle multiplications per layer. The later tape procedures (chunk interchange and Simultaneous butterfly layer) make the movement and the layer work cheaper, each costing the volume times a power below one of its width, and this is what saves a power of log n. Caveat: the pages do not show that no other tweak of the transform could help. The 'only' claim rests on a sentence attributed to an unnamed 'same source', and the pages never discuss whether a larger (higher-radix) butterfly could reduce the number of levels.

Covers key points: 1, 2, 3, 4

Quotations:

1. "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ Butterflies and the fast transform already costs $\Theta(n\log n)$, so the logarithmic factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic."
2. "A transform built from [Butterflies and the fast transform](bog) applies two-point steps, each on one address bit, so it has $\Theta(\log n)$ levels, and each level needs the data rearranged for the paired entries to meet, then the arithmetic."
3. "Done naively, that is one pass per level, and scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ Butterflies and the fast transform already costs $\Theta(n\log n)$, the bound to be beaten."
4. "The number of levels is fixed by the two-point structure, so what must shrink is the cost of a level"
5. "A head crosses one cell per step, so reaching a distant cell costs the distance."
6. "One layer of $t/2$ butterflies and $t/2$ twiddle multiplications reduces a length-$t$ transform to two independent length-$t/2$ transforms."
7. "cost the volume times a power below one of their width"

### Answer 2

On a tape machine a standard FFT-style transform on n bits has a fixed number of two-point levels, Theta(log n) of them. Each level has to bring the two partners of every butterfly together (address movement) and then apply the butterfly arithmetic. On a tape machine that costs one full pass over the stored volume of Theta(n) bits per level, so the levels together cost Theta(n log n). The page says the level count is fixed by the two-point structure, so the number of levels cannot be reduced; only the cost of a level can shrink. A level's cost is movement plus arithmetic, so only cheaper movement and cheaper arithmetic can beat n log n. The construction then lets one pass do the work of several levels: interchanging two address chunks of u bits costs O(V u^tau) with tau = 1 - 2^-50, and the Simultaneous butterfly layer performs one round of butterflies on up to d axes at once in time O(V d^lambda') with lambda' < 1, instead of d separate passes. The total saving is a power of log n with exponent kappa = 2^-182, so the time is O(n (lg n)^(1-kappa)). Other tweaks to the multiplier are not addressed on these pages; the argument that they cannot help depends on the claim that the level count is fixed, which the pages state without proof.

Covers key points: 1, 2, 3, 4

Quotations:

1. "each level must bring the partners of every butterfly together and then combine them."
2. "On a tape machine that is one pass over the whole stored volume of"
3. "Done naively, that is one pass per level"
4. "The number of levels is fixed by the two-point structure, so what must shrink is the cost of a level"
5. "the same source concludes that savings are needed in both movement and arithmetic, and that two tape procedures supply them."
6. "This is why movement and butterfly arithmetic must both be made cheaper"
7. "The remedy is to let one pass do the work of many levels, which needs cheaper movement and cheaper arithmetic together"
8. "A tape machine performs one butterfly factor per whole-array pass"

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

Write the answer to `exegenius/tasks/0426-attribute-g2.answer.json`, then run `exegenius submit 0426-attribute-g2` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0426-attribute-g2`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
