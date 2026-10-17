# exegenius task 0423-grade-g8

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

A call at parameter mf makes s smaller calls at parameter f, each on a stream of volume V/W, so the cost per unit of data C satisfies C(mf) <= (s/W) C(f) + O(1), with C(1) = O(1). Unrolling this over the log_m f levels gives a sum of powers (s/W)^j, and its largest term is (s/W)^(log_m f) = f^(log_m(s/W)) when s/W > 1. Since s/W < m, the exponent log_m(s/W) is strictly below 1, so C(f) = O(f^tau) for any fixed tau < 1 with s/W < m^tau. What must hold: the total rank s of the edge changes must be strictly below W*m, so that s/W = m(1 - eta) for a fixed eta > 0 set by the network; the Nested subspace labels and rank deficit page gets this strict inequality by counting ranks, s_b = W_b m - (N - 2 L_b) with L_b/N = 100/539 < 1/2. How large: the page fixes tau = 1 - 2^(-50), which works once eta > 20 * 2^(-50), and the actual bit-network deficit is eta = 339/22587335000000, about 1.5 * 10^(-11). So the exponent is 1 + log_m(1 - eta), a little below 1. (By my own arithmetic it is about 1 - 10^(-12); that number is not on any page.)

### Answer B

Each call at parameter mf makes s calls at parameter f, each on a stream of volume V/W, so the cost per unit of volume C satisfies C(mf) <= (s/W) C(f) + O(1). Unrolling this over log_m f levels, the deepest term is (s/W)^(log_m f) = f^(log_m(s/W)), so the cost per unit of data is a power of f with exponent log_m(s/W). That exponent is strictly below one exactly when s/W < m, that is s < Wm. Here s is the total rank of the frame changes over the edges of the linear exchange network, W is its wire count and m = h^3 is the dimension of the label space. The strict inequality is obtained from nested subspace labels: for the bit network s_b = W_b m - (N - 2L_b), which is below W_b m because L_b/N = 100/539 is below 1/2. For the saving to be a power, any fixed tau < 1 with s/W < m^tau works, and the wiki takes tau = 1 - 2^(-50). The relative deficit is tiny: eta_b = 339/22587335000000, about 1.5e-11, and eta_c is about 3.7e-12, but any positive deficit gives a power saving.

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

Write the answer to `exegenius/tasks/0423-grade-g8.answer.json`, then run `exegenius submit 0423-grade-g8` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0423-grade-g8`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
