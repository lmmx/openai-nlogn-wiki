# exegenius task 0429-attribute-g5

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

kappa = 2^-182 is the largest power of two that the cost accounting allows with the fixed exponents, not a free choice. Dividing each cost by V = Tp = Theta(n), seven kinds of operation each cost a power p^(1-g_i) of p, with margin g_i > 0. With epsilon = 2^-75, c = 2^-56 and 1-tau = 2^-50, the smallest margin is the chunk exchange: g_2 = epsilon*c*(1-tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. The reason is that an exchange acts on chunks of only K = Theta(p^(epsilon*c)) bits, so it saves K^-(1-tau) = p^-(epsilon*c*(1-tau)) against a full pass. Since 2^-181 = 2*kappa, kappa = 2^-182 is the largest allowed value. The margin is taken to be twice kappa because the logarithmic factors must be absorbed: a fixed power of log p is at most p^kappa for large p, so the seven powers (each at most p^(1-2*kappa)) times the logs give at most p^(1-2*kappa) * p^kappa = p^(1-kappa), i.e. O(n (log n)^(1-kappa)). Half of the smallest margin pays for the logs and half remains as the saving. A larger kappa would make 2*kappa exceed the smallest margin, so the bound on the seven powers would fail. The exponents epsilon, c and 1-tau are themselves fixed constants that the page says were chosen conservatively, and other rows (for example epsilon*(2-tau) < 1-tau) keep them below 2^-50, so a larger kappa would need different exponents. I am fairly confident in the arithmetic; I did not verify the upstream claim that the rank deficit s < Wm gives the saving.

Covers key points: 1, 2, 3, 4

Quotations:

1. "so the smallest margin is $2^{-181}=2\kappa$"
2. "In $g_2$ there is a further factor $c$: an exchange acts on chunks of only $K=\Theta(p^{\epsilon c})$ bits and saves a factor $K^{-(1-\tau)}=p^{-\epsilon c(1-\tau)}$ against a full pass."
3. "Each of the seven powers is at most $p^{1-2\kappa}$"
4. "Half the smallest margin pays for logarithms and half remains as the saving."
5. "So the smallest margin is $2^{-181}=2\kappa$, and $2^{-182}$ is the largest power of two allowed."
6. "The constants are conservative: no optimization is claimed. They only need to give some fixed $\kappa>0$, and $\kappa$ is then forced by the cost accounting."
7. "Hence $2\kappa$ may not exceed the smallest margin below one."
8. "The value $\tau=1-2^{-50}$ is chosen, not derived as the best exponent"

### Answer 2

kappa = 2^-182 is half of the smallest margin in the cost table. After dividing every cost by V = Tp, the seven dominant normalized costs are powers p^(1-g_i) of p. The smallest margin is g_2 = eps*c*(1-tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. It belongs to the chunk exchanges: their normalized cost p*K^(tau-1), with K = Theta(p^(eps*c)), is a power 1 - eps*c*(1-tau) of p. So every dominant term is at most p^(1-2kappa). The margin is taken to be 2kappa because one kappa pays for the fixed powers of log p (any fixed power of log p is at most p^kappa for large p) and the other kappa is the saving: p^(1-2kappa) * p^kappa = p^(1-kappa), and Tp * p^(1-kappa) = O(n (lg n)^(1-kappa)). The Parameter and prime-length choice page says that 2kappa may not exceed the smallest margin, so 2^-182 is the largest power of two that fits. The Cost accounting and the exponent κ page says any kappa below 2^-181 would pass the same test, and I could not reconcile these two statements from the pages. The exponents eps = 2^-75, c = 2^-56 and 1-tau = 2^-50 are described as conservative fixed choices, and their product fixes the scale of kappa.

Covers key points: 1, 2, 3, 4

Quotations:

1. "$\kappa=2^{-182}$, the exponent saved from the power of $\lg n$"
2. "Divided by $V=Tp$, the cost of each of seven kinds of operation is a power of $p$, and each of these exponents is at most $1-2\kappa$."
3. "The smallest margin belongs to the chunk exchanges, whose normalized cost $pK^{\tau-1}$ is a power $1-\epsilon c(1-\tau)$ of $p$ because $K=\Theta(p^{\epsilon c})$."
4. "Its margin is $\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}$."
5. "So the total is, up to a constant, $Tp\cdot p^{1-2\kappa}p^{\kappa}=Tp\cdot p^{1-\kappa}$, which is"
6. "one $\kappa$ of the margin absorbs the logarithmic factors and the other is the saving."
7. "Hence $2\kappa$ may not exceed the smallest margin below one."
8. "and $2^{-182}$ is the largest power of two allowed."
9. "Half the smallest margin pays for logarithms and half remains as the saving."
10. "Any positive $\kappa$ below $2^{-181}$ would pass the same test; $g_2$ sets the scale of $\kappa$."
11. "The constants are conservative: no optimization is claimed."
12. "a relative deficit of $\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$"
13. "For the actual network $\eta$ exceeds $20\cdot2^{-50}$"

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

Write the answer to `exegenius/tasks/0429-attribute-g5.answer.json`, then run `exegenius submit 0429-attribute-g5` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0429-attribute-g5`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
