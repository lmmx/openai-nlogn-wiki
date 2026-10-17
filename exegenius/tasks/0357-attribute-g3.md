# exegenius task 0357-attribute-g3

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

The two tape primitives get a saving that is tiny yet strictly positive (an exponent just below 1). Explain why the recursive construction produces a genuine power saving, and why the whole thing hinges on one strict inequality between the number of smaller calls s and W times m.

## Key points

1. A call at parameter m times f is implemented by s calls at parameter f, each on a stream holding only 1/W of the data volume.
2. So per unit of data, going up by a factor m in the parameter multiplies the recursive cost by s/W, whereas a linear-cost operation would multiply it by m.
3. If s < W*m then s/W < m, so the recursion solves to a power of the parameter strictly below the first power; if s were equal to W*m there would be no saving.
4. The strict inequality comes from the network labels: the total dimension is fixed by telescoping and only a small number L of unavoidable decreases occur, with L/N < 1/2, leaving s a little under W*m.
5. Hence the exponent is only barely below 1 (about 1 - 2^-50), but it is still a power saving.

## Answers

### Answer 1

A call at parameter mf (m = 10^6, the label-space dimension) splits each chunk into m slots of parameter f, deals its rows into W streams of volume V/W, and runs a fixed linear exchange network whose gates act pointwise. Each edge of that network costs one smaller call per unit of rank of its frame change, so the call makes s smaller calls at parameter f, each on volume V/W. Writing C(f) for the time per unit volume at parameter f, this gives C(mf) <= (s/W) C(f) + O(1). Unrolling over the recursion levels gives C(f) = O(sum_j (s/W)^j). If s/W < m^tau for a fixed tau < 1, this sum is O(f^tau), so one call costs O(V f^tau). The saving is a genuine power because the per-volume cost is multiplied by s/W, which is below m, for each factor m in the parameter. The hinge is the count of smaller calls: on the nested-label construction s = Wm - N + 2L for the bit network, where N is the bank size and L the dimension lost on shrinking edges. So s < Wm is equivalent to 2L < N, and the wiki computes L/N = 100/539 < 1/2. Then s/W = m(1 - eta) with eta > 0, and the wiki's margin argument gives s/W < m^tau with tau = 1 - 2^-50. My own inference, not stated on the pages: if s were equal to Wm, each level would multiply the cost by m and the recursion would give no power saving, which is why the inequality has to be strict.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "A call at parameter $mf$, with $m=10^6$ the label-space dimension, splits each chunk into $m$ slots of parameter $f$."
2. "It deals its rows into $W$ streams of volume $V/W$"
3. "So the call makes $s$ calls at parameter $f$, each on volume $V/W$, where $s$ is the total rank of the edge changes."
4. "The children cost $s(V/W)\mathcal C(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$"
5. "If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$"
6. "The labelling chooses the frames of [Frames on wire arrays](ber) so that $W$ wires cost $s<Wm$ smaller calls, the saving the recursion needs."
7. "As $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$"
8. "So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$."
9. "Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$"
10. "The intermediate frames are therefore free, and can be chosen so that each edge change is cheap"

### Answer 2

The saving comes from a per-level recurrence. A call at parameter mf splits its data into W streams of volume V/W and makes s smaller calls on them, where s is the total rank of the edge changes and each unit of rank is one smaller call. Writing C(f) for the time per unit volume at parameter f, the children cost s(V/W)C(f), so C(mf) <= (s/W)C(f) + O(1) with C(1) = O(1) (Recursive power saving). Unrolling over the log_m f levels gives C(f) = O(sum_j (s/W)^j). If s/W < m^tau with a fixed tau < 1, the sum is O(f^tau), so an interchange costs O(V f^tau) (Recursive power saving). For the bit network tau = 1 - 2^-50. The strict inequality s < Wm is what makes a tau < 1 available: the per-level factor s/W must be below the factor m by which the parameter shrinks. Nested subspace labels and rank deficit gives s_b = Wm - (N - 2L_b) with L_b/N = 100/539 < 1/2, so the deficit N - 2L_b is positive (Nested subspace labels and rank deficit). Recursive power saving turns that deficit into a margin: s/W = m(1 - eta) with eta = 339/(22587335 m), about 1.5e-11, and the exponential estimate m^(1-2^-50) > m(1 - 20*2^-50) > m(1 - eta) = s/W holds because ln m < 20 and eta exceeds 20*2^-50 (Recursive power saving). So the one strict inequality gives an exponent strictly below 1 by a small positive amount. Gap in the pages, which is my own reconstruction and not stated on any page: with s = Wm exactly, the unrolled sum is about sum_j m^j = O(f), i.e. linear, so no saving; the exponent of the last term is log_m(s/W), which is below 1 exactly when s/W < m.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "The children cost $s(V/W)\mathcal C(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$"
2. "\mathcal C(mf)\le\frac{s}{W}\mathcal C(f)+O(1)"
3. "If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$"
4. "So an interchange costs $O(Vf^\tau)$"
5. "So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$"
6. "The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$"
7. "$L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$"
8. "Write $s/W=m(1-\eta)$, with $\eta$ now the relative deficit $(Wm-s)/(Wm)$"
9. "Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$"
10. "Hence $\tau=\sigma=1-2^{-50}$ gives $s/W<m^\tau$ (bit)"

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

Write the answer to `exegenius/tasks/0357-attribute-g3.answer.json`, then run `exegenius submit 0357-attribute-g3` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0357-attribute-g3`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
