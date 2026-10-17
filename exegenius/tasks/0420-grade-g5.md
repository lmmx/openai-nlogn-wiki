# exegenius task 0420-grade-g5

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Why does kappa equal 2^-182 and not some larger constant? Which part of the cost accounting fixes it, and why is the margin taken to be twice kappa?

## Key points

1. After dividing each cost by the volume V = Tp (which is of order n), seven operations dominate, each costing a power of p below 1 with some margin g_i.
2. The smallest margin is 2^-181, coming from the chunk-exchange row, where it is the product of three tiny fixed exponents: epsilon, c and 1 - tau (2^-75 * 2^-56 * 2^-50).
3. Leftover powers of log p must be absorbed, and any fixed power of log p is eventually below p raised to a small positive exponent, so a margin of 2*kappa leaves room for that.
4. Taking the margin 2^-181 as twice kappa gives kappa = 2^-182 and total time O(n (log n)^(1-kappa)); setup and prime search cost o(V) and do not affect it.

## Answers

### Answer A

kappa = 2^-182 is the largest power of two that the cost accounting allows with the fixed exponents, not a free choice. Dividing each cost by V = Tp = Theta(n), seven kinds of operation each cost a power p^(1-g_i) of p, with margin g_i > 0. With epsilon = 2^-75, c = 2^-56 and 1-tau = 2^-50, the smallest margin is the chunk exchange: g_2 = epsilon*c*(1-tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. The reason is that an exchange acts on chunks of only K = Theta(p^(epsilon*c)) bits, so it saves K^-(1-tau) = p^-(epsilon*c*(1-tau)) against a full pass. Since 2^-181 = 2*kappa, kappa = 2^-182 is the largest allowed value. The margin is taken to be twice kappa because the logarithmic factors must be absorbed: a fixed power of log p is at most p^kappa for large p, so the seven powers (each at most p^(1-2*kappa)) times the logs give at most p^(1-2*kappa) * p^kappa = p^(1-kappa), i.e. O(n (log n)^(1-kappa)). Half of the smallest margin pays for the logs and half remains as the saving. A larger kappa would make 2*kappa exceed the smallest margin, so the bound on the seven powers would fail. The exponents epsilon, c and 1-tau are themselves fixed constants that the page says were chosen conservatively, and other rows (for example epsilon*(2-tau) < 1-tau) keep them below 2^-50, so a larger kappa would need different exponents. I am fairly confident in the arithmetic; I did not verify the upstream claim that the rank deficit s < Wm gives the saving.

### Answer B

kappa = 2^-182 is half of the smallest margin in the cost table. After dividing every cost by V = Tp, the seven dominant normalized costs are powers p^(1-g_i) of p. The smallest margin is g_2 = eps*c*(1-tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. It belongs to the chunk exchanges: their normalized cost p*K^(tau-1), with K = Theta(p^(eps*c)), is a power 1 - eps*c*(1-tau) of p. So every dominant term is at most p^(1-2kappa). The margin is taken to be 2kappa because one kappa pays for the fixed powers of log p (any fixed power of log p is at most p^kappa for large p) and the other kappa is the saving: p^(1-2kappa) * p^kappa = p^(1-kappa), and Tp * p^(1-kappa) = O(n (lg n)^(1-kappa)). The Parameter and prime-length choice page says that 2kappa may not exceed the smallest margin, so 2^-182 is the largest power of two that fits. The Cost accounting and the exponent κ page says any kappa below 2^-181 would pass the same test, and I could not reconcile these two statements from the pages. The exponents eps = 2^-75, c = 2^-56 and 1-tau = 2^-50 are described as conservative fixed choices, and their product fixes the scale of kappa.

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

Write the answer to `exegenius/tasks/0420-grade-g5.answer.json`, then run `exegenius submit 0420-grade-g5` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0420-grade-g5`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
