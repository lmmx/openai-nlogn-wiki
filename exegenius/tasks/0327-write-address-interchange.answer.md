Address-field interchange is a tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width. [Integer multiplication below n log n](main-theorem.md) uses it to organize the layouts of its transforms.

A tape procedure moves tape contents in a bounded number of passes. The procedure runs on the [Fixed-tape machine model](fixed-tape-model.md) with a fixed number of one-dimensional tapes.

Let $u$ be the bits per field and $V$ the stored bit volume, the number of bits held in the array. Let $\tau<1$ be a fixed number, the exponent in the bound $O(V u^{\tau})$. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite>

The method is not a direct copy. <cite data-source="paper">Our address procedure forms XOR combinations of intermediate data</cite>, although its final effect is a permutation. Write $x$ and $y$ for the two fields, read as blocks of bits at matching positions; these letters change meaning here. Let $\oplus$ denote bitwise exclusive or (XOR), which adds bits modulo 2. Three XOR steps swap the fields:
$$(x,y)\to(x,\;x\oplus y)\to(y,\;x\oplus y)\to(y,\;x).$$
The second step replaces $x$ by $x\oplus(x\oplus y)=y$, since a block XORed with itself is zero. For example, $x=10$, $y=01$ give $(10,01)\to(10,11)\to(01,11)\to(01,10)$.

The source uses signs: <cite data-source="paper">(x, y), the three stages give (x, y + x), then (−y, y + x), then (−y, x).</cite> Over bits, $-y=y$ and $y+x=x\oplus y$, so the signs vanish and leave the chain above.

Each XOR step acts on all matching addresses at once. The interchange is carried out by a [Linear networks and frames](linear-network-frames.md) network, which restores its [scratch storage](scratch-storage.md) to its starting contents, whatever they were. Per the source, <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to</cite> <cite data-source="paper">yS + xS and leaves every other value unchanged.</cite> The network is fixed and <cite data-source="paper">restores every auxiliary value.</cite> So the data changes do not depend on the scratch starting values: <cite data-source="paper">The final permutation is exact for arbitrary initial auxiliary values.</cite>

The cost bound comes from a recursion on the width. Let $m\ge 2$ be a fixed integer base; the letter $m$ changes meaning here. A width $u=m^k$ has $k=\log_m u$ levels; the letter $k$ changes meaning here too. Let $W\ge 2$ be the number of equal pieces the volume is cut into at each call, and let $s$ be the number of smaller calls one call makes. <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly s.</cite> Each child works on $V/W$ bits, since <cite data-source="paper">each contains V /W bits.</cite>

Let $j$ count levels below the top call; the letter $j$ changes meaning here. Level $j$ has $s^j$ calls, each on volume $V/W^j$, so its work is proportional to $V(s/W)^j$. The source's counting gives <cite data-source="paper">that the total number s of smaller calls satisfies s < W m.</cite> Hence $s/W<m$. The source then chooses <cite data-source="paper">Choose a rational number τ ∈ (0, 1) with s/W < mτ .</cite> Such $\tau$ exists since $m^{\tau}\to m$ as $\tau\to 1$.

The recursion stops after $k$ levels, since <cite data-source="paper">Here j ≤ k0 = logm e0 .</cite> The levels sum to $V\sum_{j=0}^{k}(s/W)^j$. If $s/W\le 1$ this is at most $(k+1)V$, and $k+1=O((m^{\tau})^k)$ because $m^{\tau}>1$. If $s/W>1$ it is $O(V(s/W)^k)$, and $(s/W)^k<(m^{\tau})^k$. Either way the work is $O(V(m^{\tau})^k)=O(Vu^{\tau})$, since $(m^{\tau})^k=(m^k)^{\tau}=u^{\tau}$.
