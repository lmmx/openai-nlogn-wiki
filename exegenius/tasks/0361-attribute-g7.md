# exegenius task 0361-attribute-g7

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

The classical FFT-style approach to multiplying n-bit integers does Theta(log n) levels of butterfly work over Theta(n) stored bits. Why does that alone suggest n log n on a tape machine, and where does the new algorithm look for savings to get below it?

## Key points

1. On a tape machine every level of the transform must sweep through all the Theta(n) stored bits, so Theta(log n) levels cost Theta(n log n) in total.
2. So the log factor can only be beaten by making each level cost less than a full pass: cheaper movement of data between addresses on the tapes, and cheaper butterfly arithmetic that handles several address bits together.
3. The algorithm builds two such faster tape procedures (exchanging address chunks, and a combined butterfly layer over many axes) and plugs them into the transforms.
4. The machine has a fixed alphabet, a fixed number of tapes and heads that move one cell per step, so data cannot be reached at random and cost counts moves.

## Answers

### Answer 1

Why the classical route suggests n log n: the classical FFT-style multiplication runs Theta(log n) butterfly levels, and each level has to scan all Theta(n) stored bits. On a tape machine a scan of the stored data costs time linear in the volume (the wiki's tape procedures pay O(V) per push, pop or copy), so Theta(log n) levels of Theta(n) each give Theta(n log n) in total. Where the new algorithm looks for savings: it attacks the two costs named on the Power-saving integer multiplication page, address movement and butterfly arithmetic. (1) Address movement: swapping two disjoint address chunks of u bits on a fixed number of tapes costs O(V u^tau) with tau = 1 - 2^-50 < 1 (Fast address-chunk interchange page), so the movement is cheaper than a full linear pass by a power of the chunk width. (2) Butterfly arithmetic: one round that applies the two-point step on D axes at once is done as one Simultaneous butterfly layer pass costing O(V d^lambda') with lambda' < 1, instead of D passes (Simultaneous butterfly layer page; Tape layout for synthetic transforms page). Each saving is only a power below linear, and the margins add up on the Power-saving integer multiplication page to a total time O(n (lg n)^(1-kappa)) with kappa = 2^-182, so a power of log n is saved and n log n is beaten in this model.

Covers key points: 1, 2, 3

Quotations:

1. "Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$"
2. "already costs $\Theta(n\log n)$"
3. "Each push, pop or copy scans $O(V)$ cells"
4. "Beating that needs cheaper address movement and cheaper butterfly arithmetic"
5. "two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$"
6. "in time $O(Vd^{\lambda'}),$ $\lambda'<1,$ instead of $D$ passes"
7. "A chunk round's selected bits share an offset in $D$ consecutive chunks, so one layer does it at cost $O(Tpd^{\lambda'})$"
8. "So every dominant term is at most $p^{1-2\kappa}$."

### Answer 2

Why n log n alone: the Discrete Fourier transform is computed by log t layers of butterflies (called Butterflies and the fast transform on the wiki), and each layer touches all Theta(n) stored bits. Scanning n bits once per layer over Theta(log n) layers costs Theta(n log n) on a tape. The layer's partner pairs differ in a high address bit, so on a tape they are far apart and each layer is a rearrangement, not a linear pass (my inference from home, bog and tuf). Where the new algorithm saves: (1) cheaper address movement. The interchange of two address chunks of u bits costs O(V u^tau) with tau = 1 - 2^-50 (Fast address-chunk interchange), and the Simultaneous butterfly layer applies the butterfly step to D address chunks at once in O(V d^lambda') with lambda' < 1, instead of D passes (Simultaneous butterfly layer). The Recursive power saving recurrence gives both a power below one, because a call at parameter mf makes s < Wm calls at parameter f on volume V/W, so the cost per unit volume grows by s/W < m per level. (2) cheaper butterfly arithmetic. The synthetic transform over the ring modulo y^r+1 uses signed shifts as twiddle factors, and the tape layout (Tape layout for synthetic transforms) makes each round a single Simultaneous butterfly layer. Dividing the total cost by V = Theta(n), seven dominant terms are each a power of p below one, with minimum margin 2^-181 = 2 kappa, so the total is O(n (lg n)^(1-kappa)) with kappa = 2^-182 (Cost accounting and the exponent κ).

Covers key points: 1, 2, 3

Quotations:

1. "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ Butterflies and the fast transform already costs $\Theta(n\log n)$, so the logarithmic factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic."
2. "Repeated over the address bits of an array, with twiddle multiplications between layers, it computes the [Discrete Fourier transform](kur) of an array in $\log_2 t$ layers instead of $t^2$ operations."
3. "A linear pass over an array is cheap, but an arbitrary rearrangement of an array is not."
4. "Recursive power saving is the recurrence that makes both tape procedures, the interchange of two address chunks and the Simultaneous butterfly layer, cost the volume times a power below one of their parameter."
5. "The saving is a power of $e$ since $s/W$ is a fixed constant below $m$ but near it, so $\tau\approx1$."
6. "The Simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\le d$ selected address chunks of $K$ bits, at a common offset"
7. "The tape layout arranges the address bits so that each round of a [Synthetic polynomial transform](gip) runs as one [Simultaneous butterfly layer](tiz) instead of one pass per axis."
8. "The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$"

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

Write the answer to `exegenius/tasks/0361-attribute-g7.answer.json`, then run `exegenius submit 0361-attribute-g7` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0361-attribute-g7`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
