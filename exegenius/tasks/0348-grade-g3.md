# exegenius task 0348-grade-g3

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

The two tape primitives get a saving that is tiny yet strictly positive (an exponent just below 1). Explain why the recursive construction produces a genuine power saving, and why the whole thing hinges on one strict inequality between the number of smaller calls s and W times m.

## Key points

1. A call at parameter m times f is implemented by s calls at parameter f, each on a stream holding only 1/W of the data volume.
2. So per unit of data, going up by a factor m in the parameter multiplies the recursive cost by s/W, whereas a linear-cost operation would multiply it by m.
3. If s < W*m then s/W < m, so the recursion solves to a power of the parameter strictly below the first power; if s were equal to W*m there would be no saving.
4. The strict inequality comes from the network labels: the total dimension is fixed by telescoping and only a small number L of unavoidable decreases occur, with L/N < 1/2, leaving s a little under W*m.
5. Hence the exponent is only barely below 1 (about 1 - 2^-50), but it is still a power saving.

## Answers

### Answer A

The background does not cover this question. It does not define the two tape primitives, the recursive construction, or the quantities s, W and m, and it does not give the strict inequality between s and W times m that the question says the saving hinges on. The reader has only introductory Turing machine and tape knowledge and has not been taught the specific literature on fast integer multiplication, so the reader cannot explain why the construction gives a power saving with an exponent just below 1. The only related material the reader knows is the general divide-and-conquer pattern from the algorithms course: a recursion that makes s calls on subproblems each shrunk by a factor m, with linear work per level, has the recurrence T(n) = s*T(n/m) + O(n), which solves to about n^(log_m s) when s is greater than m, and Karatsuba multiplication (three half-size calls, giving n^(log_2 3)) is the standard example. Because W and m are not defined in the question or the background, the reader cannot tell how this pattern maps onto the question's inequality, so this is not offered as an answer to the question.

### Answer B

The saving comes from a per-level recurrence. A call at parameter mf splits its data into W streams of volume V/W and makes s smaller calls on them, where s is the total rank of the edge changes and each unit of rank is one smaller call. Writing C(f) for the time per unit volume at parameter f, the children cost s(V/W)C(f), so C(mf) <= (s/W)C(f) + O(1) with C(1) = O(1) (Recursive power saving). Unrolling over the log_m f levels gives C(f) = O(sum_j (s/W)^j). If s/W < m^tau with a fixed tau < 1, the sum is O(f^tau), so an interchange costs O(V f^tau) (Recursive power saving). For the bit network tau = 1 - 2^-50. The strict inequality s < Wm is what makes a tau < 1 available: the per-level factor s/W must be below the factor m by which the parameter shrinks. Nested subspace labels and rank deficit gives s_b = Wm - (N - 2L_b) with L_b/N = 100/539 < 1/2, so the deficit N - 2L_b is positive (Nested subspace labels and rank deficit). Recursive power saving turns that deficit into a margin: s/W = m(1 - eta) with eta = 339/(22587335 m), about 1.5e-11, and the exponential estimate m^(1-2^-50) > m(1 - 20*2^-50) > m(1 - eta) = s/W holds because ln m < 20 and eta exceeds 20*2^-50 (Recursive power saving). So the one strict inequality gives an exponent strictly below 1 by a small positive amount. Gap in the pages, which is my own reconstruction and not stated on any page: with s = Wm exactly, the unrolled sum is about sum_j m^j = O(f), i.e. linear, so no saving; the exponent of the last term is log_m(s/W), which is below 1 exactly when s/W < m.

### Answer C

A call at parameter mf (m = 10^6, the label-space dimension) splits each chunk into m slots of parameter f, deals its rows into W streams of volume V/W, and runs a fixed linear exchange network whose gates act pointwise. Each edge of that network costs one smaller call per unit of rank of its frame change, so the call makes s smaller calls at parameter f, each on volume V/W. Writing C(f) for the time per unit volume at parameter f, this gives C(mf) <= (s/W) C(f) + O(1). Unrolling over the recursion levels gives C(f) = O(sum_j (s/W)^j). If s/W < m^tau for a fixed tau < 1, this sum is O(f^tau), so one call costs O(V f^tau). The saving is a genuine power because the per-volume cost is multiplied by s/W, which is below m, for each factor m in the parameter. The hinge is the count of smaller calls: on the nested-label construction s = Wm - N + 2L for the bit network, where N is the bank size and L the dimension lost on shrinking edges. So s < Wm is equivalent to 2L < N, and the wiki computes L/N = 100/539 < 1/2. Then s/W = m(1 - eta) with eta > 0, and the wiki's margin argument gives s/W < m^tau with tau = 1 - 2^-50. My own inference, not stated on the pages: if s were equal to Wm, each level would multiply the cost by m and the recursion would give no power saving, which is why the inequality has to be strict.

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

Write the answer to `exegenius/tasks/0348-grade-g3.answer.json`, then run `exegenius submit 0348-grade-g3` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0348-grade-g3`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
