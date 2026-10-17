import json
d=[("S2.2","Both cost $O(Tp[dK+pK^{\\tau-1}+\\ell d^{\\lambda'}])$.")]
S="The tape layout arranges the address bits so that each round of a [synthetic polynomial transform](synthetic-transform.md) runs as one [simultaneous butterfly layer](simultaneous-layer.md) instead of one pass per axis."
rel=[
("synthetic-transform","arranges the rounds of",S),
("simultaneous-layer","runs as one",S),
("address-interchange","exchanges made by","This needs at most $Dq-1$ exchanges, each made by the [fast address-chunk interchange](address-interchange.md) at cost $O(TpK^\\tau)$, even for nonadjacent chunks."),
("frequency-order","keeps the bit-reversed order of","Outputs keep the bit-reversed order of [retained frequency order](frequency-order.md), written $B$ along every axis (the bit-reversal permutation here, not the row length of [stream operations](stream-ops.md) or the suffix digit count of [controlled shifts](controlled-shifts.md))."),
]
q1x="Write $\\ell=\\log_2 r$, the address bits of a long axis (an address-bit count, not the depth of a value), and $D=d-1$, the number of transformed axes (not the second chunk value of [fast address-chunk interchange](address-interchange.md), the source group of [matrix shear](matrix-shear.md), or the selected chunk count of the layer)."
q2="$K$ is the chunk width in bits (not a tensor line or segment spacing); $\\tau,\\lambda'<1$ are the interchange and layer exponents."
q3="Put $b=(\\ell-1)\\bmod K$ and $q=\\lfloor(\\ell-1)/K\\rfloor$, so $\\ell-1=qK+b$."
q4x="Here $b$ counts leftover low bits of an axis, not the lowest output-index bit of [butterflies](butterfly.md), a digit count of [matrix shear](matrix-shear.md) or [controlled shifts](controlled-shifts.md), or a kernel coefficient of [the kernel C](phase-kernel.md); $q$ counts whole chunks of an axis, not a sequence length (as in [the DFT](dft.md) or [cyclic convolution](convolution.md)), a radix, or a prime."
qL="The prefix moves and exchanges define the record permutation $L$ (neither a linear map, as in [contractions](contraction-maps.md), nor a dimension loss, as in [subspace labels](subspace-labels.md)); reversing them gives $L^{-1}$."
qz="Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering a round (not an address suffix, nor a binary vector of [phase frames](phase-frames.md)) $J_EQ_p(\\mathcal Hz)=Q_p(J_E\\mathcal Hz)$: one truncation follows the exact round."
sy=[
("D","transformed axis count","The number of transformed axes, d-1.","count",q1),
("b","leftover low bits","The number of leftover low bits of an axis.","count",q4),
("q","whole chunks","The number of whole K-bit chunks of an axis.","count",q4),
("B","bit reversal","The bit-reversal permutation applied along every axis.","direct",rel[3][2]),
("L","layout permutation","The record permutation defined by the prefix moves and chunk exchanges.","direct",qL),
("z","round input","The array entering a round of the transform.","direct",qz),
("\\tau","interchange exponent","The fixed exponent below 1 in the chunk interchange cost.","direct",q2),
("\\lambda'","layer exponent","The fixed exponent below 1 in the simultaneous layer cost.","direct",q2),
]
out={"derivations":[{"step":a,"quote":b} for a,b in d],
"relations":[{"prerequisite":a,"predicate":b,"quote":c} for a,b,c in rel],
"symbols":[{"symbol":a,"name":b,"meaning":c,"relation":r,"quote":q} for a,b,c,r,q in sy]}
json.dump(out,open("0311-write-transform-layout.answer.json","w"),indent=1)

