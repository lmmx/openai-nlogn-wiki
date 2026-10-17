# exegenius task 0359-attribute-g5

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?

## Key points

1. After dividing each cost by the volume V = Tp (which is of order n), seven operations dominate, each costing a power of p below 1 with some margin g_i.
2. The smallest margin is 2^-181, coming from the chunk-exchange row, where it is the product of three tiny fixed exponents: epsilon, c and 1 - tau (2^-75 * 2^-56 * 2^-50).
3. Leftover powers of log p must be absorbed, and any fixed power of log p is eventually below p raised to a small positive exponent, so a margin of 2*kappa leaves room for that.
4. Taking the margin 2^-181 as twice kappa gives kappa = 2^-182 and total time O(n (log n)^(1-kappa)); setup and prime search cost o(V) and do not affect it.

## Answers

### Answer 1

kappa is set by the smallest of the seven dominant margins in the cost accounting. Every dominant cost, divided by V = Tp = Theta(n), is a power p^(1-g_i) of p with margin g_i. The smallest margin is g_2 for chunk exchanges, whose cost per unit volume is p K^(tau-1) with K = Theta(p^(epsilon c)), so g_2 = epsilon c (1 - tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. Because K^(tau-1) = p^(-epsilon c (1-tau)), the margin is fixed by the axis-count exponent epsilon, the chunk-width exponent c and the interchange saving 1 - tau. The margin is taken to be twice kappa because every dominant term is at most p^(1-2 kappa), and the leftover fixed powers of log p are at most p^kappa for large p, so the total is p^(1-kappa), i.e. O(n (lg n)^(1-kappa)). With margin kappa alone the bound would be p^1 and there would be no saving. Since g_2 = 2^-181 = 2 kappa, kappa = 2^-182 is the largest power-of-two value the margin allows. The wiki states kappa = 2^-182 as a fixed choice; it does not derive that value.

Covers key points: 1, 2, 3, 4

Quotations:

1. "The total is $O(p/K)K^\tau=O(pK^{\tau-1})$"
2. "Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$"
3. "so the smallest margin is $2^{-181}=2\kappa$"
4. "Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, which the margin $2\kappa$ leaves room for."
5. "Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$. These are conservative."
6. "two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time"
7. "The exponent is only $2^{-182}$ below one because $g_2$ multiplies three small numbers"
8. "The margin $g_i$ of the $i$-th term is one minus its exponent."

### Answer 2

kappa = 2^-182 is half of the smallest margin in the cost accounting; it is not a free choice. After dividing every cost by V = Theta(n), each of the seven dominant costs is a power p^(1-g_i), where the margin g_i is one minus the exponent. The smallest margin is g_2 = eps*c*(1-tau), which belongs to the chunk exchanges (the p K^(tau-1) term): 2^-75 * 2^-56 * 2^-50 = 2^-181 = 2*kappa. So every dominant term is at most p^(1-2*kappa). Any fixed power of log p is at most p^kappa eventually, so the normalized total is O(p^(1-kappa)) and the time is O(n (lg n)^(1-kappa)). The margin is 2*kappa because one kappa of it is spent absorbing the log factors and the remaining kappa is the saving. The pages do not argue why exactly half is taken; the constants eps, c, tau and lambda' are called conservative without justification.

Covers key points: 1, 2, 3, 4

Quotations:

1. "g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}=2\kappa"
2. "so the smallest margin is $2^{-181}=2\kappa$"
3. "So every dominant term is at most $p^{1-2\kappa}$."
4. "Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, which the margin $2\kappa$ leaves room for."
5. "so the normalized total is $O(p^{1-\kappa})$ and the time is $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$."
6. "The exponent is only $2^{-182}$ below one because $g_2$ multiplies three small numbers: $\epsilon$ (few axes), $c$ (narrow chunks) and $1-\tau$ (an exchange saves only $K^{-(1-\tau)}$)."
7. "The margin $g_i$ of the $i$-th term is one minus its exponent."
8. "two disjoint address chunks of $u$ bits can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time, $\tau=1-2^{-50}$"
9. "Take $C_1=20$, $\epsilon=2^{-75}$ and $\kappa=2^{-182}$. These are conservative."

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

Write the answer to `exegenius/tasks/0359-attribute-g5.answer.json`, then run `exegenius submit 0359-attribute-g5` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0359-attribute-g5`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
