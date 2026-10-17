# exegenius task 0432-attribute-g8

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Why does a recursive scheme where one call on parameter m*f makes s calls on parameter f, each working on 1/W of the data, give a cost per unit of data that is a power of the parameter strictly below the first power? What exactly must hold for the saving, and how large is it?

## Key points

1. Each call splits the data over W streams, so each of its s sub-calls handles only 1/W of the volume. Per unit of data, going from f to m*f therefore multiplies the cost by s/W.
2. A saving needs s/W to be strictly smaller than m, the factor by which the parameter grew, i.e. s < W*m. If s/W were m, cost would just be linear in the parameter and nothing would be gained.
3. Solving the recurrence gives cost per unit of data about (s/W)^k for parameter m^k, which is below the parameter raised to a fixed exponent smaller than 1.
4. The saving is tiny: s/W is only a relative 10^-11 or so below m, so the exponent is just under 1 (1 - 2^-50), but it is positive, and the whole power saving rests on that strict inequality.

## Answers

### Answer 1

Each call at parameter mf makes s calls at parameter f, each on a stream of volume V/W, so the cost per unit of volume C satisfies C(mf) <= (s/W) C(f) + O(1). Unrolling this over log_m f levels, the deepest term is (s/W)^(log_m f) = f^(log_m(s/W)), so the cost per unit of data is a power of f with exponent log_m(s/W). That exponent is strictly below one exactly when s/W < m, that is s < Wm. Here s is the total rank of the frame changes over the edges of the linear exchange network, W is its wire count and m = h^3 is the dimension of the label space. The strict inequality is obtained from nested subspace labels: for the bit network s_b = W_b m - (N - 2L_b), which is below W_b m because L_b/N = 100/539 is below 1/2. For the saving to be a power, any fixed tau < 1 with s/W < m^tau works, and the wiki takes tau = 1 - 2^(-50). The relative deficit is tiny: eta_b = 339/22587335000000, about 1.5e-11, and eta_c is about 3.7e-12, but any positive deficit gives a power saving.

Covers key points: 1, 2, 3, 4

Quotations:

1. "a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$"
2. "The deepest term is $(s/W)^{\log_m f}=f^{\log_m(s/W)}$; for $s/W>1$ the geometric sum is a constant times it"
3. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$"
4. "Source dimensions sum to $N$, sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$."
5. "A wire enters and leaves each gate with that gate's label, so its signed changes telescope to sink minus source dimension, summing to $Wm-2N$ over all wires."
6. "is $339/22587335000000\approx1.5\cdot10^{-11}$"
7. "Hence $\tau=\sigma=1-2^{-50}$ gives $s_{\rm b}/W_{\rm b}<m^\tau$"

### Answer 2

A call at parameter mf makes s smaller calls at parameter f, each on a stream of volume V/W, so the cost per unit of data C satisfies C(mf) <= (s/W) C(f) + O(1), with C(1) = O(1). Unrolling this over the log_m f levels gives a sum of powers (s/W)^j, and its largest term is (s/W)^(log_m f) = f^(log_m(s/W)) when s/W > 1. Since s/W < m, the exponent log_m(s/W) is strictly below 1, so C(f) = O(f^tau) for any fixed tau < 1 with s/W < m^tau. What must hold: the total rank s of the edge changes must be strictly below W*m, so that s/W = m(1 - eta) for a fixed eta > 0 set by the network; the Nested subspace labels and rank deficit page gets this strict inequality by counting ranks, s_b = W_b m - (N - 2 L_b) with L_b/N = 100/539 < 1/2. How large: the page fixes tau = 1 - 2^(-50), which works once eta > 20 * 2^(-50), and the actual bit-network deficit is eta = 339/22587335000000, about 1.5 * 10^(-11). So the exponent is 1 + log_m(1 - eta), a little below 1. (By my own arithmetic it is about 1 - 10^(-12); that number is not on any page.)

Covers key points: 1, 2, 3, 4

Quotations:

1. "Unrolling $\log_m f$ levels, depth $j$ (the number of levels below the top call, not a stage number) contributes $(s/W)^j$"
2. "The deepest term is $(s/W)^{\log_m f}=f^{\log_m(s/W)}$; for $s/W>1$ the geometric sum is a constant times it, and for $s/W\le1$ it is $O(\log f)$."
3. "If $s=Wm$, depth $j$ contributes $m^j$, the sum is about $f$, and the cost is proportional to $Vf$: no saving."
4. "The exponent $\log_m(s/W)=1+\log_m(1-\eta)$ is below $1$ exactly when $\eta>0$, and $\eta$ is fixed with the network."
5. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$, and an interchange costs $O(Vf^\tau)$."
6. "Source dimensions sum to $N$, sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$."
7. "Hence $s_{\rm b}=W_{\rm b}m-(N-2L_{\rm b})$ and $s_{\rm c}=W_{\rm c}m-(2N-2L_{\rm c})$, both below $Wm$ because $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are below $1/2$."
8. "For $A$ in a fixed finite set, it can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work."
9. "Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$, by a factor over $200$."
10. "is $339/22587335000000\approx1.5\cdot10^{-11}$"
11. "Hence $\tau=\sigma=1-2^{-50}$ gives $s_{\rm b}/W_{\rm b}<m^\tau$ and $s_{\rm c}/W_{\rm c}<m^\sigma$, with $0<\tau=\sigma<1$."

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

Write the answer to `exegenius/tasks/0432-attribute-g8.answer.json`, then run `exegenius submit 0432-attribute-g8` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0432-attribute-g8`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
