# exegenius task 0362-attribute-g8

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

The recurrence on the Recursive power saving page gives C(mf) <= (s/W) C(f) + O(1), where C(f) is the time per unit of volume at parameter f. Unrolling it over the recursion depth j gives C(f) = O(sum over j from 0 to log_m f of (s/W)^j). If the ratio s/W is at most m^tau for a fixed tau below 1, every term is at most m^(tau j), so the sum is O(f^tau): the per-unit cost is a power of the parameter strictly below the first power. Two things must hold. First, the total rank s of the edge changes must be strictly less than W*m (so s/W < m); the page takes this strictness from the rank counts on the Nested subspace labels and rank deficit page, which are strict because L/N < 1/2. Second, the gap must be a fixed power: s/W < m^tau with tau < 1 fixed, not merely some strict gap. The size of the saving is set by the chosen exponent tau = sigma = 1 - 2^(-50) on the Parameter and prime-length choice page, so the per-unit cost is O(f^(1-2^(-50))), a saving of a factor f^(2^(-50)) relative to linear in f (this last step is my own arithmetic from tau). The actual relative gap is eta = 339/22587335000000 (about 1.5e-11) for the bit network and 73/19906842167500 (about 3.7e-12) for the complex network; both exceed 20*2^(-50), about 1.8e-14, which is what makes s/W < m^tau hold. I did not open the cost-accounting page, so I did not verify how this exponent yields kappa = 2^(-182).

Covers key points: 1, 2, 3, 4

Quotations:

1. "So the call makes $s$ calls at parameter $f$, each on volume $V/W$, where $s$ is the total rank of the edge changes."
2. "\mathcal C(mf)\le\frac{s}{W}\mathcal C(f)+O(1),\qquad \mathcal C(1)=O(1)"
3. "If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$"
4. "both strictly less than $Wm$, because $L/N<1/2$."
5. "if the circuit data satisfy the shear contract with $s<Wm$ and $s/W<m^\tau$"
6. "Take $\tau=\sigma=1-2^{-50}$, $\beta=1/2$ and $\delta=1/16$."
7. "Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$"

### Answer 2

The cost per unit volume C(f) at parameter f satisfies C(mf) <= (s/W) C(f) + O(1) with C(1) = O(1). Each call at parameter mf makes s child calls at parameter f, each on a stream of volume V/W, so the recursive cost per unit volume is multiplied by s/W per factor m of the parameter. Unrolling over the log_m f levels gives C(f) = O(sum_{j=0}^{log_m f} (s/W)^j). If s/W < m^tau for a fixed tau < 1, the last term (s/W)^{log_m f} = f^{log_m(s/W)} lies below f^tau and dominates, so C(f) = O(f^tau): one power of f, strictly below the first. What must hold: the total rank s of the edge changes must be strictly below W*m (so s/W < m); with s/W a fixed constant this gives a fixed tau = log_m(s/W) < 1. For the bit network s = Wm - (N - 2L), so the saving needs N > 2L, i.e. L/N < 1/2, which holds because L/N = 100/539. How large: the relative deficit eta = (Wm - s)/(Wm) is 339/22587335000000, about 1.5e-11. The pages take tau = 1 - 2^-50, and m^tau > m(1 - 2^-50 ln m) > m(1 - 20*2^-50) > m(1 - eta) since eta is about 1.5e-11, far above 20*2^-50 (about 1.8e-14). So the cost is f^(1 - 2^-50) rather than f: the exponent gap is 2^-50, a tiny but sufficient margin. I checked the recurrence, the unrolling, the counting s = Wm - (N - 2L), and the numeric margin; I accepted the label-level facts (projection ranks, nondegeneracy, the wire-label chains) from the pages without verifying them.

Covers key points: 1, 2, 3, 4

Quotations:

1. "The children cost $s(V/W)\mathcal C(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$"
2. "\mathcal C(mf)\le\frac{s}{W}\mathcal C(f)+O(1)"
3. "so $\mathcal C(f)=O\big(\sum_{j=0}^{\log_m f}(s/W)^j\big)$"
4. "If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$"
5. "Choose $\tau$ with $s/W<m^\tau$."
6. "So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$."
7. "As $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$"
8. "Write $s/W=m(1-\eta)$, with $\eta$ now the relative deficit $(Wm-s)/(Wm)$."
9. "namely $339/22587335000000$ and $73/19906842167500$"
10. "Hence $\tau=\sigma=1-2^{-50}$ gives $s/W<m^\tau$ (bit)"
11. "as the exponential lies above its tangent at $0$, $m^{1-2^{-50}}=m\exp(-2^{-50}\ln m)>m(1-2^{-50}\ln m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$ for either network."
12. "where $\tau=1-2^{-50}$ is the saving exponent"

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

Write the answer to `exegenius/tasks/0362-attribute-g8.answer.json`, then run `exegenius submit 0362-attribute-g8` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0362-attribute-g8`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
