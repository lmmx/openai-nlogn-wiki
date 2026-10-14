from lib import *
from key import LN, CF, SL


def SH():
    return show(
        "A shear $(H,D)\\mapsto(H+AD,D)$ over $\\mathbb Z/q^{k}\\mathbb Z$ with a rational matrix $A$ of rank $a$ costs exactly $a$ interchanges of pairs of equal-width fields plus $O(V)$ work, and the three shears $D\\leftarrow D-H$, $H\\leftarrow H+D$, $D\\leftarrow H-D$ interchange $H$ and $D$.",
        "Factor $A=E_1\\Pi E_2$ with lower-triangular invertible $E_i$ and a partial permutation $\\Pi$ of $a$ ones, run the triangular factors as linear-time controlled shifts, and realize each one of $\\Pi$ by a single swap sandwiched between two controlled updates.",
        "Lower-triangular changes of coordinates update a later field from earlier ones, which is exactly the direction in which controlled shifts run in linear time; so only the $a$ pivot entries of $\\Pi$ need genuine field interchanges.",
        "explicit",
        mq=r"can be performed entirely in this direction.",
        page="address-shear",
        frm=["linear-algebra-basics", "controlled-shift", "elementary-stream-ops", "tape-address-model", "vectors-matrices-and-invertibility"],
        salient="The cost of a shear depends on the rank $a$ of the matrix, not on its size $m$: this is what makes edge changes of small rank cheap and lets the total be counted by ranks.",
        adds=[("a", "matrix rank", "The rational rank of the shear matrix $A$, equal to the number of ones of $\\Pi$ and to the number of field interchanges.", "count")],
        children=[
            infer("Every rational $m\\times m$ matrix of rank $a$ factors as $A=E_1\\Pi E_2$ with $E_1,E_2$ invertible lower triangular and $\\Pi$ having exactly $a$ ones, at most one per row and column.",
                  r"Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"),
            infer("The elimination takes the topmost nonzero row, clears with its rightmost nonzero entry as pivot by lower-triangular operations on both sides, deletes pivot row and column, and repeats, leaving $a$ pivots.",
                  r"nonzero row and its rightmost nonzero entry."),
            infer("A fixed odd prime $q$ avoiding all denominators lets the rational identities specialize to $\\mathbb Z/q^{k}\\mathbb Z$, and the shear then uses exactly $a$ interchanges of field pairs.",
                  r"can be performed with exactly $a$ interchanges of pairs of $b$-digit"),
            infer("A lower-triangular transformation of $H$ or of $D$ costs $O(V)$: update coordinates in descending physical order, each by a diagonal unit and a fixed combination of earlier coordinates.",
                  r"A lower triangular transformation of $H$, or of $D$, costs $O(V)$:"),
            infer("For $A=E_1\\Pi E_2$, transform $D$ by $E_2$ and $H$ by $E_1^{-1}$, add $\\Pi D$ to $H$, then transform $H$ by $E_1$ and $D$ by $E_2^{-1}$.",
                  r"For $A=E_1\Pi E_2$, first transform $D$ by $E_2$ and $H$ by $E_1^{-1}$,"),
            infer("Each one of $\\Pi$ calls for $H_i\\leftarrow H_i+D_j$, done by $D_j\\leftarrow D_j+H_i$, then swapping $(H_i,D_j)$, then $D_j\\leftarrow H_i-D_j$.",
                  r"D_j\leftarrow D_j+H_i,\qquad"),
            infer("On an initial pair $(h,d)$ this sequence yields $(h+d,d)$ and uses just one interchange, so $a$ ones cost $a$ interchanges.",
                  r"It uses just one interchange."),
        ])


def K4():
    swap = show(
        "For the bit network each node makes $s$ calls on role streams of volume $V/W$ with $O(V)$ own work, so $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$, which gives $F_k=O(e^\\tau)$ for $e=m^k$.",
        "Count the smaller calls, divide the cost by the volume, and sum the geometric series, splitting by whether the ratio $s/W$ exceeds one.",
        "A strict inequality $s/W<m^\\tau$ makes the ratio of successive terms $s/(Wm^{\\tau})<1$ compared with the width growth $m$, so the series is dominated by the leaf level of size $e^\\tau$ rather than $e$.",
        "recoverable",
        salient="The ratio $s/W$ is only just below $m$, yet being strictly below it gives an exponent $\\tau<1$ for the whole recursion; with $s/W=m$ the same recursion would cost the full $e$.",
        children=[
            infer("Each smaller call acts on one role stream of volume $V/W$, while splitting, merging, gates and triangular operations cost $O(V)$ in total.",
                  r"Each acts on one role stream of volume $V/W$, retaining all other", deferred=True),
            infer("If $F_k$ bounds time divided by logical volume at width $e=m^k$, then $F_0=O(1)$ and $F_k\\le(s/W)F_{k-1}+O(1)$.",
                  r"F_0=O(1),\qquad F_k\le(s/W)F_{k-1}+O(1).", deferred=True),
            infer("For $a=s/W<m^\\tau$ the geometric sum $\\sum_{j\\le k}a^j$ is $O(m^{k\\tau})$: at most $k+1=O(m^{k\\tau})$ if $a\\le1$ and $O(a^k)$ if $a>1$.",
                  r"For $a=s/W<m^\tau$ the geometric sum", deferred=True),
        ])
    layer = show(
        "For the complex network the recurrence $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ with $F(e)=O(e)$ below the cutoff $d^\\beta$ still sums to $O(e^{\\lambda})$ internal cost and $O(e^\\sigma d^{\\beta(1-\\sigma)})$ leaf cost.",
        "Add to the same call-count recurrence the cost of the binary basis changes at a node, bound the chunk width $K\\le e^{c/\\beta}$ above the cutoff, and sum internal and leaf contributions separately.",
        "The complex version differs from the bit version only by a larger node overhead, $O((eK)^\\tau+1)$ instead of $O(1)$, so the same series argument applies once that overhead is bounded by a power $e^\\lambda$ with $\\lambda<1$.",
        "recoverable",
        children=[
            infer("The recurrence is $F(e)\\le(s/W)F(e/m)+O((eK)^\\tau+1)$ and $F(e)=O(e)$ for $e<d^\\beta$, since the $s$ child calls run on streams of volume $V/W$.",
                  r"F(e)\le (s/W)F(e/m)+O((eK)^\tau+1),", deferred=True),
            infer("At an internal node $e\\ge d^\\beta$, so $K\\le d^c\\le e^{c/\\beta}$ and the overhead is $O(e^{\\tau(1+c/\\beta)}+1)=O(e^\\lambda)$.",
                  r"\(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\).", deferred=True),
            infer("With $a=s/W\\le m^\\sigma<m^\\lambda$ the internal costs sum to $Ce^\\lambda\\sum_j(a/m^\\lambda)^j=O(e^\\lambda)$.",
                  r"C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda).", deferred=True),
            infer("The leaves after $j$ levels, with $u=e/m^j<d^\\beta$ active chunks each, contribute at most $O(a^ju)\\le O(e^\\sigma u^{1-\\sigma})\\le O(e^\\sigma d^{\\beta(1-\\sigma)})$.",
                  r"O(a^ju)\le O(e^\sigma u^{1-\sigma})", deferred=True),
        ])
    return show(
        "Dividing the cost of the networked procedure by the volume gives a recurrence whose branching ratio is $s/W$, and since $s/W<m^\\tau$ it solves to a cost $O(e^{\\tau})$ in the parameter $e$ for the bit network and $O(e^{\\lambda})$ in the complex one.",
        "Solve the recurrence once for each network, the bit network for address interchange and the complex network for butterfly layers.",
        "Each network gives its own recurrence with its own node overhead, so each variant is solved separately.",
        "reconstructed",
        mq=None, children=[swap, layer],
        adds=[])


def KEY():
    return show(
        "A fixed linear network with $W$ wires that exchanges two banks of values and restores all scratch wires, with every edge change carried out by smaller calls on role streams of volume $V/W$, has total call count $s<Wm$, so the cost per volume obeys $F_k\\le(s/W)F_{k-1}+O(1)$ and grows only like $e^{\\tau}$ with $\\tau<1$.",
        "Build the network, show that frames let its edges cost only their frame changes, label its gates with nested subspaces so that the total rank of the edge changes is below $Wm$, price a shear by its rank, and solve the resulting recurrence.",
        "The recursion is only worth having if the smaller calls cost less in total than the parent, which holds exactly when the number $s$ of smaller calls, each on volume $V/W$, satisfies $s/W<m$; so the work is to construct a network with a strict rank deficit.",
        "explicit",
        mq=r"is the source of the power saving.",
        page="rank-saving-recurrence",
        frm=["tape-address-model", "elementary-stream-ops", "linear-algebra-basics", "recurrences-and-induction", "big-o"],
        salient="The rank deficit $Wm-s$ is tiny relative to $Wm$ (about $10^{-14}$ for the bit network), yet because it is strictly positive it forces an exponent $1-2^{-50}$ below one; the whole saving of a power of the logarithm rests on this strict inequality.",
        adds=[("h", "ground-set size", "The size $100$ of the ground set $[h]$ whose three-element subsets index the labels.", "count"),
              ("v", "triples per axis", "The number $\\binom h3=161700$ of three-element subsets of $[h]$.", "count"),
              ("N", "data wires per bank", "The number $v^3=4227952113000000$ of wires in each of the two data banks.", "count"),
              ("m", "label dimension", "The dimension $h^3=1000000$ of the label space, i.e. the length of the vectors $H,D$ of address fields.", "count"),
              ("W", "wire count", "The total number of wires of the network, scratch wires included.", "count"),
              ("s", "smaller calls", "The total rank of all edge changes, i.e. the number of smaller calls one invocation makes.", "count"),
              ("e", "width parameter", "The size of the call: the number $m^k$ of digits per chunk (bit network) or of selected axes (complex network); each smaller call has parameter $e/m$.", "count"),
              ("I", "invocation count", "The number $3v^2=78440670000$ of separate invocations of the exchange schedule, each with its own scratch wires.", "count")],
        children=[
            infer("Fix $h=100$, $v=\\binom h3=161700$, $N=v^3=4227952113000000$ and $m=h^3=1000000$; the banks have $N$ data wires each and the label space has dimension $m$.",
                  r"N=v^3=4227952113000000,\qquad m=h^3=1000000."),
            LN(),
            CF(),
            SL(),
            SH(),
            K4(),
        ])
