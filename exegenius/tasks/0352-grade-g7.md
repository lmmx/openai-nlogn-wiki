# exegenius task 0352-grade-g7

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

Only part of this is answerable from the background. The first part can be reasoned from big-O and the introductory treatment of tapes, but with an unverified premise, since the reader has not been taught the discrete Fourier transform, FFT, or butterfly operations. The second part is not covered.

Why this suggests n log n on a tape machine: taking the question's description at face value, there are Theta(log n) levels, and each level does work over all Theta(n) stored bits. On a tape machine, a level that visits every bit means the head has to move along the whole tape, so one level costs on the order of n steps. Doing this for each of the Theta(log n) levels gives Theta(n) times Theta(log n), that is Theta(n log n) steps in total. The background does not explain why each level must be a full pass over the tape, and the reader cannot check what the butterfly work consists of.

Where the new algorithm looks for savings: the background does not say. The reader has no description of the new algorithm and has not studied the literature on fast integer multiplication, so the reader cannot identify where its savings come from without guessing. The only multiplication speedup the reader knows is Karatsuba's divide and conquer, which replaces four half-size products with three. That is not the algorithm the question asks about, and the background does not connect the two, so no answer is given for this part.

### Answer B

Why n log n alone: the Discrete Fourier transform is computed by log t layers of butterflies (called Butterflies and the fast transform on the wiki), and each layer touches all Theta(n) stored bits. Scanning n bits once per layer over Theta(log n) layers costs Theta(n log n) on a tape. The layer's partner pairs differ in a high address bit, so on a tape they are far apart and each layer is a rearrangement, not a linear pass (my inference from home, bog and tuf). Where the new algorithm saves: (1) cheaper address movement. The interchange of two address chunks of u bits costs O(V u^tau) with tau = 1 - 2^-50 (Fast address-chunk interchange), and the Simultaneous butterfly layer applies the butterfly step to D address chunks at once in O(V d^lambda') with lambda' < 1, instead of D passes (Simultaneous butterfly layer). The Recursive power saving recurrence gives both a power below one, because a call at parameter mf makes s < Wm calls at parameter f on volume V/W, so the cost per unit volume grows by s/W < m per level. (2) cheaper butterfly arithmetic. The synthetic transform over the ring modulo y^r+1 uses signed shifts as twiddle factors, and the tape layout (Tape layout for synthetic transforms) makes each round a single Simultaneous butterfly layer. Dividing the total cost by V = Theta(n), seven dominant terms are each a power of p below one, with minimum margin 2^-181 = 2 kappa, so the total is O(n (lg n)^(1-kappa)) with kappa = 2^-182 (Cost accounting and the exponent κ).

### Answer C

Why the classical route suggests n log n: the classical FFT-style multiplication runs Theta(log n) butterfly levels, and each level has to scan all Theta(n) stored bits. On a tape machine a scan of the stored data costs time linear in the volume (the wiki's tape procedures pay O(V) per push, pop or copy), so Theta(log n) levels of Theta(n) each give Theta(n log n) in total. Where the new algorithm looks for savings: it attacks the two costs named on the Power-saving integer multiplication page, address movement and butterfly arithmetic. (1) Address movement: swapping two disjoint address chunks of u bits on a fixed number of tapes costs O(V u^tau) with tau = 1 - 2^-50 < 1 (Fast address-chunk interchange page), so the movement is cheaper than a full linear pass by a power of the chunk width. (2) Butterfly arithmetic: one round that applies the two-point step on D axes at once is done as one Simultaneous butterfly layer pass costing O(V d^lambda') with lambda' < 1, instead of D passes (Simultaneous butterfly layer page; Tape layout for synthetic transforms page). Each saving is only a power below linear, and the margins add up on the Power-saving integer multiplication page to a total time O(n (lg n)^(1-kappa)) with kappa = 2^-182, so a power of log n is saved and n log n is beaten in this model.

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

Write the answer to `exegenius/tasks/0352-grade-g7.answer.json`, then run `exegenius submit 0352-grade-g7` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0352-grade-g7`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
