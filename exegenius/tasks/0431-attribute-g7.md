# exegenius task 0431-attribute-g7

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

The classical transform has Theta(log n) levels, and each level has to bring the partners of every butterfly together and then combine them. On a tape machine each level is one sequential pass over all Theta(n) stored bits, so the levels together cost Theta(n log n). That is why the classical approach alone suggests n log n. The new algorithm looks for savings in two places, and it needs both at once. First, movement: swapping two address chunks of u bits in one operation costs O(V u^tau) with a fixed tau < 1, so many address bits move at once instead of one level at a time. Second, arithmetic: one round of butterfly steps across up to d axes runs as a single pass in O(V d^lambda') with lambda' < 1, instead of d separate passes. A layout first gathers the bits of the axes so that many levels become one such round. The per-level cost then drops below a full pass because the recursion's branching ratio s/W is below m, which gives a power-saving exponent. The savings are all powers of the logarithm, so the single machine runs in O(n (lg n)^(1-kappa)) with kappa = 2^-182, which is o(n log n). Confidence is moderate to high on this outline. I followed the cited arguments but did not check the exponent margin arithmetic beyond the cited formulas, and I did not open the algebra pages behind the rank count s < Wm.

Covers key points: 1, 2, 3

Quotations:

1. "On a tape machine that is one pass over the whole stored volume of $\Theta(n)$ bits per level, so the levels cost $\Theta(n\log n)$."
2. "Interchanging two address chunks of $u$ bits moves $u$ address bits at once for $O(Vu^\tau)$ with fixed $\tau<1$"
3. "The [Simultaneous butterfly layer](tiz) does one round of butterflies on up to $d$ axes at once for $O(Vd^{\lambda'})$ with $\lambda'<1$, instead of $d$ separate passes."
4. "A tape machine performs one butterfly factor per whole-array pass, so $D$ separate factors would require $D$ whole-array passes"
5. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$, and an interchange costs $O(Vf^\tau)$."
6. "If $s=Wm$, depth $j$ contributes $m^j$, the sum is about $f$, and the cost is proportional to $Vf$: no saving."

### Answer 2

The classical transform on n-bit inputs runs Theta(log n) butterfly layers over Theta(n) stored bits. Each layer of t/2 butterflies and twiddle multiplications halves a length-t transform into two length-t/2 transforms, so the arithmetic per layer is small, but on a tape each layer needs at least one scan of all stored bits, and log n scans of n bits cost Theta(n log n). That is why the front page says the logarithmic factor can only be beaten by cheaper address movement or cheaper butterfly arithmetic. The new algorithm attacks both with two tape procedures. The first is a chunk interchange, which moves two address chunks of width u in O(V u^tau) time with tau = 1 - 2^-50. The second is the layer procedure (Simultaneous butterfly layer), which applies one bit of each of D selected chunks at once in O(V d^lambda') time with lambda' < 1, instead of one whole-array pass per bit. Both are recursive: a call at parameter mf makes s calls at parameter f on streams of volume V/W, with s < Wm, so each level of splitting multiplies the cost per unit volume by s/W < m, which gives a fixed power below linear in the parameter. The strict inequality s < Wm comes from a rank count on nested subspace labels that I could not verify in detail. The layer's two-point step is rewritten through a kernel C = aI + bX with C^2 = X. Summing all costs gives O(n (log n)^(1-kappa)) with kappa = 2^-182, which is the saving over n log n. I am confident of the mechanism and the scan argument. I am not confident of the exact rank count or of the constants, which the wiki states as choices.

Covers key points: 1, 2, 3

Quotations:

1. "so the logarithmic factor can only be beaten by cheaper address movement and cheaper butterfly arithmetic."
2. "even one scan of the stored bits per level over $\log n$ levels costs order $n\log n$"
3. "One layer of $t/2$ butterflies and $t/2$ twiddle multiplications reduces a length-$t$ transform to two independent length-$t/2$ transforms."
4. "and $F_k\le cF_{k-1}+O(1)$, where $c=s/W$ is the number of calls $s$ times the volume fraction $1/W$ of each."
5. "so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter"
6. "so the cost per unit volume grows as a power of the axis count below 1, not linearly."
7. "Since $a^2+b^2=\frac{i}{2}-\frac{i}{2}=0$ and $2ab=1$, we get $C^2=(a^2+b^2)I+2ab\,X=X$"
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

Write the answer to `exegenius/tasks/0431-attribute-g7.answer.json`, then run `exegenius submit 0431-attribute-g7` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0431-attribute-g7`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
