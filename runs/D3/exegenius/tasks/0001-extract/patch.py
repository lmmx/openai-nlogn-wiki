import json
f="0001-extract.answer.json"
d=json.load(open(f))
X={
"fourier-transform":["(F_t^+z)_j=\\frac1t\\sum_{k=0}^{t-1}\\omega_t^{jk}z_k"],
"polynomial-ring-y-r-1":["\\mathcal R_r=\\mathbb C[y]/(y^r+1)"],
"synthetic-transforms":["Multiplication\nby $y^a$, for any integer $a$, permutes the coefficients and changes\nsome signs; consequently it is an isometry for this norm.","\\begin{lemma}[Synthetic character cancellation]"],
"signed-packing":["The\nreduction is a signed form of Kronecker substitution"],
"gaussian-resampling":["\\begin{lemma}[Resampling without executing the two permutations]"],
"bluestein-chirp":["\\begin{lemma}[Chirp and permutation cancellation]"],
"phase-twist":["\\subsection{Complex convolution by a coefficient twist}"],
"crt-prime-axes":["CRT and axis layouts"],
"linear-network-frames":["Each such invocation has its own auxiliary wires, distinct from all\nother invocations"],
"finite-network-subspaces":["Let $\\mathcal T$ be the set of three-element subsets of $[h]$."],
"recursive-power-saving":["Because the sum of these ranks is less than the number of wires times\n$m$, the resulting recurrence saves a power of the chunk width."],
"address-interchange":["The chunks can be interchanged in $O(Ve^\\tau)$ time"],
"fast-butterfly-layer":["We will obtain cost $O(Vd^{\\lambda'})$"],
"precision-exact-recovery":["\\subsection{Precision and exact recovery}"],
"nlogn-conjecture":["\\subsection{The complete time bound}"],
"tape-address-rearrangement":["\\begin{lemma}[Lower triangular factorization]"],
"convolution":["\\item Multiply corresponding complex coefficients exactly and truncate"],
"main-theorem":["\\subsection{The multiplication algorithm}","Chunk exchanges for transform layout"],
}
for c in d["concepts"]:
    for q in X.get(c["id"],[]): c["evidence"].append({"source":"paper","quote":q})
json.dump(d,open(f,"w"),indent=1)
