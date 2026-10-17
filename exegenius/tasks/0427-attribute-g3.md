# exegenius task 0427-attribute-g3

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

A call at parameter mf on a stream of volume V makes s smaller calls at parameter f, each on a stream of volume V/W (rut). Writing C(f) for the time per unit volume, the children cost (s/W)C(f) per unit of parent volume, so C(mf) is at most (s/W)C(f)+O(1) (rut). Unrolling this over the levels gives a geometric sum with ratio s/W whose deepest term is f^(log_m(s/W)) (rut). That exponent is below 1 exactly when s/W < m, i.e. s < Wm; at equality the cost is proportional to Vf and nothing is saved (rut). The number s is the total rank of the frame changes along the edges of a fixed linear exchange network (Linear exchange network with restored scratch wires, Frames on wire arrays), and a frame change of rank a costs a smaller calls because a shear of rank a takes exactly a interchanges of fields (Matrix shear by triangular factorization). The nested subspace labels (Nested subspace labels and rank deficit) give s = Wm - (N - 2L) in the bit network, with L/N = 100/539 below 1/2, so s is strictly less than Wm. The relative deficit is about 1.5e-11, so the exponent is only slightly below 1, and an explicit tau = 1 - 2^(-50) works (rut). The whole saving therefore hinges on the single strict inequality s < Wm: it makes the exponent of the recursion strictly below one.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "Both tape primitives (the interchange of two address chunks of $u$ digits and the Simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$"
2. "The children cost $s(V/W)\mathcal C(f)$, which per unit of the parent's volume is $(s/W)\mathcal C(f)$"
3. "The deepest term is $(s/W)^{\log_m f}=f^{\log_m(s/W)}$; for $s/W>1$ the geometric sum is a constant times it, and for $s/W\le1$ it is $O(\log f)$."
4. "If $s=Wm$, depth $j$ contributes $m^j$, the sum is about $f$, and the cost is proportional to $Vf$: no saving."
5. "The exponent $\log_m(s/W)=1+\log_m(1-\eta)$ is below $1$ exactly when $\eta>0$, and $\eta$ is fixed with the network."
6. "Summing over edges, the call makes $s$ calls at parameter $f$, each on volume $V/W$, where $s$ is the total rank of the edge changes."
7. "Hence $s_{\rm b}=W_{\rm b}m-(N-2L_{\rm b})$ and $s_{\rm c}=W_{\rm c}m-(2N-2L_{\rm c})$, both below $Wm$ because $L_{\rm b}/N=100/539$ and $L_{\rm c}/N=101/539$ are below $1/2$."
8. "The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive as $L_{\rm b}/N<1/2$, but tiny"
9. "For $A$ in a fixed finite set, it can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work."
10. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$, and an interchange costs $O(Vf^\tau)$."
11. "A linear exchange network is a fixed circuit of linear gates on wires, each carrying one scalar, that swaps two banks of values with a sign and restores every scratch wire to its initial value, whatever that was"

### Answer 2

Setup. Interchanging two address chunks of width e = m^k on a volume V uses a fixed linear exchange network with W wires, and the rows are dealt cyclically into W role streams, each of volume V/W. Each edge i of the network carries a Matrix shear by triangular factorization shear by a matrix A_i, and a shear of rank r costs exactly r interchanges of fields of width e/m, each of which is a recursive call at the smaller parameter e/m on the stream. So one call at width e makes s = sum of the edge ranks smaller calls, each on a stream of volume V/W.

Recurrence. Per unit volume, the cost F_k at width m^k satisfies F_k <= c F_{k-1} + O(1) with c = s/W, because the node's own splitting, gates and triangular work is O(V). Unrolling over k = log_m e levels gives a per-unit-volume cost of about c^k = e^{log_m c}. The exponent is log_m c = log_m(s/W), and this is a genuine power saving exactly when the exponent is below 1, i.e. when c < m, i.e. when s < Wm. Then any fixed tau with c < m^tau < m gives total cost O(V e^tau), with tau < 1.

Why the hinge is strict. If s = Wm, then c = m, the exponent is 1, and the total is proportional to V e, so there is no saving. Writing c = m(1 - eta), with eta the relative deficit (Wm - s)/(Wm), the exponent is 1 + log_m(1 - eta), which is below 1 exactly when eta > 0. The whole saving is therefore the gap between s and Wm.

Where the inequality comes from. Nested subspace labels and rank deficit attaches to each wire a nested subspace of an m-dimensional label space (m = h^3 = 10^6), so each edge's rank is its absolute change in label dimension. Summing over the wires, the absolute changes give Wm - 2N, plus 2L for the dimensions lost on decreasing edges (L the total loss), and the sign at each bit source adds N, so s_b = Wm - (N - 2L_b). The complex network gives s_c = Wm - (2N - 2L_c). Since L_b/N = 100/539 < 1/2 and L_c/N = 101/539 < 1/2, both deficits are positive and s < Wm strictly. The bit deficit relative to Wm is about 1.5 x 10^-11, which is tiny but positive, so there is a fixed tau < 1 above the exponent (the page picks tau = 1 - 2^-50).

Caveat. I checked the arithmetic of L/N, the deficit and the relative deficit, but I did not verify each label step of the Nested subspace labels and rank deficit dimension table; I took that bookkeeping and the complex count (stated on Binary phase frames) largely on the page's word.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$"
2. "a shear by an edge matrix costs as many interchanges of pairs of $b$-digit fields as its rank"
3. "The number of recursive calls is the sum of the edge ranks, exactly $s$."
4. "A linear exchange network is a fixed circuit of linear gates on wires, each carrying one scalar, that swaps two banks of values with a sign and restores every scratch wire to its initial value, whatever that was"
5. "Dealing whole rows cyclically into $W$ streams, where $W$ is the fixed number of streams"
6. "$F_k\le cF_{k-1}+O(1)$, where $c=s/W$ is the number of calls $s$ times the volume fraction $1/W$ of each."
7. "Each of the $k=\log_m e$ levels multiplies the cost by at most $c$"
8. "With $s=Wm$ calls the cost would be $e$, no saving; strictness of $s<Wm$ puts the exponent $\log_m c$ below $1$."
9. "The deepest term is $(s/W)^{\log_m f}=f^{\log_m(s/W)}$; for $s/W>1$ the geometric sum is a constant times it, and for $s/W\le1$ it is $O(\log f)$."
10. "If $s=Wm$, depth $j$ contributes $m^j$, the sum is about $f$, and the cost is proportional to $Vf$: no saving."
11. "So any fixed $\tau<1$ with $s/W<m^\tau$ gives $\mathcal C(f)=O(f^\tau)$"
12. "The exponent $\log_m(s/W)=1+\log_m(1-\eta)$ is below $1$ exactly when $\eta>0$"
13. "the fixed label-space dimension $m=h^3=10^6$"
14. "it uses nested subspaces as frames, so that an edge costs one smaller call per unit of rank change."
15. "So each edge's rank is its absolute dimension change, except the first edge of each $X_a$"
16. "Source dimensions sum to $N$, sink dimensions to $Nm+N(m-1)+(W-2N)m=Wm-N$."
17. "Against this, the $L$ dimensions lost on shrinking edges must be regained, costing $2L$"
18. "With $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$"
19. "The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive as $L_{\rm b}/N<1/2$, but tiny"

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

Write the answer to `exegenius/tasks/0427-attribute-g3.answer.json`, then run `exegenius submit 0427-attribute-g3` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0427-attribute-g3`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
