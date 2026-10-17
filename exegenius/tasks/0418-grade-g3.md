# exegenius task 0418-grade-g3

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

A call at parameter mf on a stream of volume V makes s smaller calls at parameter f, each on a stream of volume V/W (rut). Writing C(f) for the time per unit volume, the children cost (s/W)C(f) per unit of parent volume, so C(mf) is at most (s/W)C(f)+O(1) (rut). Unrolling this over the levels gives a geometric sum with ratio s/W whose deepest term is f^(log_m(s/W)) (rut). That exponent is below 1 exactly when s/W < m, i.e. s < Wm; at equality the cost is proportional to Vf and nothing is saved (rut). The number s is the total rank of the frame changes along the edges of a fixed linear exchange network (Linear exchange network with restored scratch wires, Frames on wire arrays), and a frame change of rank a costs a smaller calls because a shear of rank a takes exactly a interchanges of fields (Matrix shear by triangular factorization). The nested subspace labels (Nested subspace labels and rank deficit) give s = Wm - (N - 2L) in the bit network, with L/N = 100/539 below 1/2, so s is strictly less than Wm. The relative deficit is about 1.5e-11, so the exponent is only slightly below 1, and an explicit tau = 1 - 2^(-50) works (rut). The whole saving therefore hinges on the single strict inequality s < Wm: it makes the exponent of the recursion strictly below one.

### Answer B

Setup. Interchanging two address chunks of width e = m^k on a volume V uses a fixed linear exchange network with W wires, and the rows are dealt cyclically into W role streams, each of volume V/W. Each edge i of the network carries a Matrix shear by triangular factorization shear by a matrix A_i, and a shear of rank r costs exactly r interchanges of fields of width e/m, each of which is a recursive call at the smaller parameter e/m on the stream. So one call at width e makes s = sum of the edge ranks smaller calls, each on a stream of volume V/W.

Recurrence. Per unit volume, the cost F_k at width m^k satisfies F_k <= c F_{k-1} + O(1) with c = s/W, because the node's own splitting, gates and triangular work is O(V). Unrolling over k = log_m e levels gives a per-unit-volume cost of about c^k = e^{log_m c}. The exponent is log_m c = log_m(s/W), and this is a genuine power saving exactly when the exponent is below 1, i.e. when c < m, i.e. when s < Wm. Then any fixed tau with c < m^tau < m gives total cost O(V e^tau), with tau < 1.

Why the hinge is strict. If s = Wm, then c = m, the exponent is 1, and the total is proportional to V e, so there is no saving. Writing c = m(1 - eta), with eta the relative deficit (Wm - s)/(Wm), the exponent is 1 + log_m(1 - eta), which is below 1 exactly when eta > 0. The whole saving is therefore the gap between s and Wm.

Where the inequality comes from. Nested subspace labels and rank deficit attaches to each wire a nested subspace of an m-dimensional label space (m = h^3 = 10^6), so each edge's rank is its absolute change in label dimension. Summing over the wires, the absolute changes give Wm - 2N, plus 2L for the dimensions lost on decreasing edges (L the total loss), and the sign at each bit source adds N, so s_b = Wm - (N - 2L_b). The complex network gives s_c = Wm - (2N - 2L_c). Since L_b/N = 100/539 < 1/2 and L_c/N = 101/539 < 1/2, both deficits are positive and s < Wm strictly. The bit deficit relative to Wm is about 1.5 x 10^-11, which is tiny but positive, so there is a fixed tau < 1 above the exponent (the page picks tau = 1 - 2^-50).

Caveat. I checked the arithmetic of L/N, the deficit and the relative deficit, but I did not verify each label step of the Nested subspace labels and rank deficit dimension table; I took that bookkeeping and the complex count (stated on Binary phase frames) largely on the page's word.

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

Write the answer to `exegenius/tasks/0418-grade-g3.answer.json`, then run `exegenius submit 0418-grade-g3` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0418-grade-g3`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
