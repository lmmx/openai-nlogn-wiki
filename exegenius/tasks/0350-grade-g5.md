# exegenius task 0350-grade-g5

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

kappa = 2^-182 is half of the smallest margin in the cost accounting; it is not a free choice. After dividing every cost by V = Theta(n), each of the seven dominant costs is a power p^(1-g_i), where the margin g_i is one minus the exponent. The smallest margin is g_2 = eps*c*(1-tau), which belongs to the chunk exchanges (the p K^(tau-1) term): 2^-75 * 2^-56 * 2^-50 = 2^-181 = 2*kappa. So every dominant term is at most p^(1-2*kappa). Any fixed power of log p is at most p^kappa eventually, so the normalized total is O(p^(1-kappa)) and the time is O(n (lg n)^(1-kappa)). The margin is 2*kappa because one kappa of it is spent absorbing the log factors and the remaining kappa is the saving. The pages do not argue why exactly half is taken; the constants eps, c, tau and lambda' are called conservative without justification.

### Answer B

The background does not cover this question, so I cannot say why kappa equals 2^-182, which part of the cost accounting fixes it, or why the margin is taken to be twice kappa. The question depends on a specific construction and its cost accounting, and I have no information about what kappa stands for or how it is defined. My background covers big-O notation, polynomials, complex numbers, basic Turing machines with tapes, divide and conquer, schoolbook and Karatsuba multiplication, linear algebra, elementary number theory, and binary representation. It does not include the discrete Fourier transform or FFT, tensor products, numerical error analysis, or the literature on fast integer multiplication, which is what I would need to reason about where a constant like 2^-182 and a margin of 2*kappa come from. Any explanation I gave would be a guess, so I am not giving one.

### Answer C

kappa is set by the smallest of the seven dominant margins in the cost accounting. Every dominant cost, divided by V = Tp = Theta(n), is a power p^(1-g_i) of p with margin g_i. The smallest margin is g_2 for chunk exchanges, whose cost per unit volume is p K^(tau-1) with K = Theta(p^(epsilon c)), so g_2 = epsilon c (1 - tau) = 2^-75 * 2^-56 * 2^-50 = 2^-181. Because K^(tau-1) = p^(-epsilon c (1-tau)), the margin is fixed by the axis-count exponent epsilon, the chunk-width exponent c and the interchange saving 1 - tau. The margin is taken to be twice kappa because every dominant term is at most p^(1-2 kappa), and the leftover fixed powers of log p are at most p^kappa for large p, so the total is p^(1-kappa), i.e. O(n (lg n)^(1-kappa)). With margin kappa alone the bound would be p^1 and there would be no saving. Since g_2 = 2^-181 = 2 kappa, kappa = 2^-182 is the largest power-of-two value the margin allows. The wiki states kappa = 2^-182 as a fixed choice; it does not derive that value.

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

Write the answer to `exegenius/tasks/0350-grade-g5.answer.json`, then run `exegenius submit 0350-grade-g5` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0350-grade-g5`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
