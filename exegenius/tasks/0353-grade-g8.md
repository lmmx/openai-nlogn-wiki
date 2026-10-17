# exegenius task 0353-grade-g8

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Why does a recursive scheme where one call on parameter m*f makes s calls on parameter f, each working on 1/W of the data, give a cost per unit of data that is a power of the parameter strictly below the first power? What exactly must hold for the saving, and how large is it?

## Key points

1. Each call splits the data over W streams, so each of its s sub-calls handles only 1/W of the volume. Per unit of data, going from f to m*f therefore multiplies the cost by s/W.
2. A saving needs s/W to be strictly smaller than m, the factor by which the parameter grew, i.e. s < W*m. If s/W were m, cost would just be linear in the parameter and nothing would be gained.
3. Solving the recurrence gives cost per unit of data about (s/W)^k for parameter m^k, which is below the parameter raised to a fixed exponent smaller than 1.
4. The saving is tiny: s/W is only a relative 10^-11 or so below m, so the exponent is just under 1 (1 - 2^-50), but it is positive, and the whole power saving rests on that strict inequality.

## Answers

### Answer A

The background does not cover the source's exact normalization of the scheme, so this is a derivation from divide-and-conquer recurrences (the reader's algorithms background), with the assumptions stated. Let P be the parameter, D the amount of data, and u(P) the cost per unit of data, taken to be linear in data. A call at parameter m*f on data D makes s calls at parameter f, each on D/W of the data, so with per-level splitting and combining overhead negligible, cost(m*f, D) = s * cost(f, D/W), which gives u(m*f) = (s/W) * u(f). Unrolling this over k = log_m(P) levels: the parameter falls from P to a constant base case, there are s^k leaf calls, and the data is multiplied by (s/W)^k. Since (s/W)^k = P^(log_m(s/W)), the cost per unit of data is a power of P with exponent beta = log_m(s/W) = log(s/W) / log(m). This is the same shape as the master theorem for T(n) = a*T(n/b) with a = s and b = m, with an extra factor 1/W per level. For data proportional to P, the total cost is P^(1 + beta) = P^(log_m(m*s/W)).

What must hold for the saving: (1) beta < 1, which is exactly s/W < m, i.e. s < m*W. If s >= m*W, the per-unit cost is no better than the first power (or worse), so there is no saving. (2) The split must be exact: the s subcalls together handle exactly s/W of the data, and the data and parameter must be divisible by W and m at every level. (3) The per-level splitting, combining, and base-case costs must be of lower order, so that they do not change the exponent. (4) The cost must be linear in the data, so that cost per unit of data is well defined.

How large is the saving: compared with the schoolbook cost of the first power per unit of data (P^1), the saving factor per unit of data is P^(1 - beta) = P^(log_m(m*W/s)). It grows polynomially in P with that exponent. Check against Karatsuba multiplication (m = 2, s = 3, W = 2, and s < m*W since 3 < 4): beta = log_2(3/2), about 0.585; the saving per unit of data is P^(log_2(4/3)), about P^0.415; and the total cost is P^(log_2 3), about P^1.585, which is Karatsuba's known exponent. If the source measures the parameter in a different way (for example, as a logarithm of the size), the exponents above must be read in that measure.

### Answer B

The recurrence on the Recursive power saving page gives C(mf) <= (s/W) C(f) + O(1), where C(f) is the time per unit of volume at parameter f. Unrolling it over the recursion depth j gives C(f) = O(sum over j from 0 to log_m f of (s/W)^j). If the ratio s/W is at most m^tau for a fixed tau below 1, every term is at most m^(tau j), so the sum is O(f^tau): the per-unit cost is a power of the parameter strictly below the first power. Two things must hold. First, the total rank s of the edge changes must be strictly less than W*m (so s/W < m); the page takes this strictness from the rank counts on the Nested subspace labels and rank deficit page, which are strict because L/N < 1/2. Second, the gap must be a fixed power: s/W < m^tau with tau < 1 fixed, not merely some strict gap. The size of the saving is set by the chosen exponent tau = sigma = 1 - 2^(-50) on the Parameter and prime-length choice page, so the per-unit cost is O(f^(1-2^(-50))), a saving of a factor f^(2^(-50)) relative to linear in f (this last step is my own arithmetic from tau). The actual relative gap is eta = 339/22587335000000 (about 1.5e-11) for the bit network and 73/19906842167500 (about 3.7e-12) for the complex network; both exceed 20*2^(-50), about 1.8e-14, which is what makes s/W < m^tau hold. I did not open the cost-accounting page, so I did not verify how this exponent yields kappa = 2^(-182).

### Answer C

The cost per unit volume C(f) at parameter f satisfies C(mf) <= (s/W) C(f) + O(1) with C(1) = O(1). Each call at parameter mf makes s child calls at parameter f, each on a stream of volume V/W, so the recursive cost per unit volume is multiplied by s/W per factor m of the parameter. Unrolling over the log_m f levels gives C(f) = O(sum_{j=0}^{log_m f} (s/W)^j). If s/W < m^tau for a fixed tau < 1, the last term (s/W)^{log_m f} = f^{log_m(s/W)} lies below f^tau and dominates, so C(f) = O(f^tau): one power of f, strictly below the first. What must hold: the total rank s of the edge changes must be strictly below W*m (so s/W < m); with s/W a fixed constant this gives a fixed tau = log_m(s/W) < 1. For the bit network s = Wm - (N - 2L), so the saving needs N > 2L, i.e. L/N < 1/2, which holds because L/N = 100/539. How large: the relative deficit eta = (Wm - s)/(Wm) is 339/22587335000000, about 1.5e-11. The pages take tau = 1 - 2^-50, and m^tau > m(1 - 2^-50 ln m) > m(1 - 20*2^-50) > m(1 - eta) since eta is about 1.5e-11, far above 20*2^-50 (about 1.8e-14). So the cost is f^(1 - 2^-50) rather than f: the exponent gap is 2^-50, a tiny but sufficient margin. I checked the recurrence, the unrolling, the counting s = Wm - (N - 2L), and the numeric margin; I accepted the label-level facts (projection ranks, nondegeneracy, the wire-label chains) from the pages without verifying them.

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

Write the answer to `exegenius/tasks/0353-grade-g8.answer.json`, then run `exegenius submit 0353-grade-g8` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0353-grade-g8`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
