# exegenius task 0347-grade-g2

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

The background only partly covers this. The reader knows big-O, polynomials, complex numbers and basic Turing machines with tapes, but has not been taught the DFT or FFT, the butterfly structure of a transform, or the tape-machine cost accounting the question relies on. So the claim that only address movement and butterfly arithmetic can be made cheaper cannot be verified from the background, and the reader cannot say what the other possible tweaks are.

What the background does support: a divide-and-conquer recurrence of the form T(n) = 2T(n/2) + O(n), of the kind solved in an algorithms course, gives O(n log n). The log n factor is the number of recursion levels, and the n factor is the linear work done on each level. Applied to a transform, this reading would put the log n factor on the number of stages, with about n work per stage. On a tape machine, the work per stage includes moving the head to the addresses whose entries are combined, so movement cost is charged on every stage as well. This is consistent with the idea that cheaper movement and cheaper per-stage arithmetic are the places where the n log n total can be reduced.

What the background does not establish: why changing constants, or the base case of the recursion, cannot remove the log n factor (these change the constant in front of n log n, but whether any other restructuring could drop a level depends on the transform's structure, which the reader has not learned), and what the specific accounting of a standard transform on a tape machine is. Those points are not covered by the background.

### Answer B

Accounting: on this machine each head moves one cell per step, so one linear pass over an array costs time proportional to its stored bits. The main result's input has V = Theta(n) stored bits, so one pass costs Theta(n). The layered transform (Butterflies and the fast transform) has Theta(log n) layers. If each layer is one full pass over the data, the total is Theta(n) times Theta(log n), which is Theta(n log n), the bound to be beaten. To beat it, the work per layer must fall below one full pass. The wiki's route does this for both parts of a layer. Moving address bits so that paired entries sit together is a chunk interchange, which costs O(V u^tau) with tau < 1 (Fast address-chunk interchange). The butterfly arithmetic of several axes at once costs O(V d^lambda') with lambda' < 1, and runs as one Simultaneous butterfly layer instead of one pass per axis (Simultaneous butterfly layer, Tape layout for synthetic transforms). The Cost accounting and the exponent κ page then sums these cost terms, each a power of the width below one, and gets O(n (lg n)^(1-kappa)).

Why only these two: the Power-saving integer multiplication page states that beating the bound needs cheaper address movement and cheaper butterfly arithmetic. None of the pages I opened argues that other changes, such as fewer layers or a different radix, cannot also reduce the cost per layer. I accept the 'only' clause on the wiki's word, so that part of the answer is not established by the pages.

### Answer C

Accounting: the model is a Turing machine whose head moves one cell per step, so one pass over the stored bits costs time proportional to their number. The data has V = Theta(n) stored bits, so one pass costs Theta(n). The transform has Theta(log n) butterfly layers, and each layer scans the whole array, so a standard transform costs Theta(n) times Theta(log n) = Theta(n log n). To beat the log factor, each layer's rearrangement and butterfly work must cost less than one full pass. Two tape procedures do this with a power of their width below one: an interchange of two address chunks of u digits costs O(V u^tau) with tau < 1, and the Simultaneous butterfly layer does the butterfly rounds of D axes in O(V d^lambda') with lambda' < 1 instead of D passes. The tape layout makes each transform round a single Simultaneous butterfly layer. The widths are small powers of p, and p = 6b with b = ceil(log2 n), so the per-layer savings multiply out to a saving of a power of log n. Why other tweaks do not help: constant factors are free in this model, and the pages I opened do not argue that a different radix or a reordering trick changes the number of layers or the per-layer scan. That step is my inference. The 'only' in the front page is therefore not argued in the pages I read; the accounting and the mechanism are supported.

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

Write the answer to `exegenius/tasks/0347-grade-g2.answer.json`, then run `exegenius submit 0347-grade-g2` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0347-grade-g2`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
