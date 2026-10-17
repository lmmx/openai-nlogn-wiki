# exegenius task 0356-attribute-g2

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

Accounting: the model is a Turing machine whose head moves one cell per step, so one pass over the stored bits costs time proportional to their number. The data has V = Theta(n) stored bits, so one pass costs Theta(n). The transform has Theta(log n) butterfly layers, and each layer scans the whole array, so a standard transform costs Theta(n) times Theta(log n) = Theta(n log n). To beat the log factor, each layer's rearrangement and butterfly work must cost less than one full pass. Two tape procedures do this with a power of their width below one: an interchange of two address chunks of u digits costs O(V u^tau) with tau < 1, and the Simultaneous butterfly layer does the butterfly rounds of D axes in O(V d^lambda') with lambda' < 1 instead of D passes. The tape layout makes each transform round a single Simultaneous butterfly layer. The widths are small powers of p, and p = 6b with b = ceil(log2 n), so the per-layer savings multiply out to a saving of a power of log n. Why other tweaks do not help: constant factors are free in this model, and the pages I opened do not argue that a different radix or a reordering trick changes the number of layers or the per-layer scan. That step is my inference. The 'only' in the front page is therefore not argued in the pages I read; the accounting and the mechanism are supported.

Covers key points: 1, 2, 3, 4

Quotations:

1. "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ Butterflies and the fast transform therefore already costs $\Theta(n)\cdot\Theta(\log n)=\Theta(n\log n)$, the bound to be beaten."
2. "So each rearrangement must cost one pass, not one pass per level."
3. "After $\log_2 t$ layers every transform has length one, the identity, for $O(t\log t)$ operations in all."
4. "Constant factors are free, structure is not."
5. "A linear pass over an array is cheap, but an arbitrary rearrangement of an array is not."
6. "$b=\lceil\log_2n\rceil$, $p=6b$"
7. "in $O(Vu^\tau)$ time on fixed tapes"
8. "So an interchange costs $O(Vf^\tau)$."
9. "cost the volume times a power below one of their width"
10. "rather than $D$ whole-array passes"
11. "instead of one pass per axis."

### Answer 2

Accounting: on this machine each head moves one cell per step, so one linear pass over an array costs time proportional to its stored bits. The main result's input has V = Theta(n) stored bits, so one pass costs Theta(n). The layered transform (Butterflies and the fast transform) has Theta(log n) layers. If each layer is one full pass over the data, the total is Theta(n) times Theta(log n), which is Theta(n log n), the bound to be beaten. To beat it, the work per layer must fall below one full pass. The wiki's route does this for both parts of a layer. Moving address bits so that paired entries sit together is a chunk interchange, which costs O(V u^tau) with tau < 1 (Fast address-chunk interchange). The butterfly arithmetic of several axes at once costs O(V d^lambda') with lambda' < 1, and runs as one Simultaneous butterfly layer instead of one pass per axis (Simultaneous butterfly layer, Tape layout for synthetic transforms). The Cost accounting and the exponent κ page then sums these cost terms, each a power of the width below one, and gets O(n (lg n)^(1-kappa)).

Why only these two: the Power-saving integer multiplication page states that beating the bound needs cheaper address movement and cheaper butterfly arithmetic. None of the pages I opened argues that other changes, such as fewer layers or a different radix, cannot also reduce the cost per layer. I accept the 'only' clause on the wiki's word, so that part of the answer is not established by the pages.

Covers key points: 1, 2, 3, 4

Quotations:

1. "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ Butterflies and the fast transform therefore already costs $\Theta(n)\cdot\Theta(\log n)=\Theta(n\log n)$, the bound to be beaten."
2. "The data of the $n$-bit inputs occupy $V=\Theta(n)$ stored bits, so one pass costs $\Theta(n)$."
3. "Repeated over the address bits of an array, with twiddle multiplications between layers, it computes the [Discrete Fourier transform](kur) of an array in $\log_2 t$ layers instead of $t^2$ operations."
4. "Beating that needs cheaper address movement and cheaper butterfly arithmetic"
5. "in $O(Vu^\tau)$ time on fixed tapes, where $\tau=1-2^{-50}$ is the saving exponent"
6. "instead of $D$ passes"
7. "The tape layout arranges the address bits so that each round of a [Synthetic polynomial transform](gip) runs as one [Simultaneous butterfly layer](tiz) instead of one pass per axis."

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

Write the answer to `exegenius/tasks/0356-attribute-g2.answer.json`, then run `exegenius submit 0356-attribute-g2` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0356-attribute-g2`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
