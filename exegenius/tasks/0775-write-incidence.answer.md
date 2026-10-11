An incidence relates a wire to a [Gate and terminal of a network](network-gate-terminal.md): it holds when the wire touches that gate or terminal. Every incidence lies in a [linear network](linear-network-frames.md), whose vertices carry frames. The [subset-intersection network](subset-intersection-network.md) relies on this: every wire at one gate is changed by the same frame, so the gate can run on the stored arrays directly.

A frame is an invertible linear operator on arrays, attached to a vertex $v$. <cite data-source="paper">We call Dv its frame: the stored array is Dv g when the logical array is g.</cite> So a wire at $v$ stores $D_v g$ when its logical array is $g$. All incidences of one gate <cite data-source="paper">have the same frame.</cite> The reason is that <cite data-source="paper">a gate instead combines wire values at each fixed address.</cite> Values at the same address must therefore be in one representation before the gate combines them.

Let a pointwise linear gate $G$ take $t$ input wires, with fixed scalar weights $\Upsilon_\ell$, one for each input wire $\ell = 1,\dots,t$. Let $g_\ell$ be the logical array on input wire $\ell$. The weights are the same at every address, so $G(g_1,\dots,g_t)=\sum_{\ell=1}^t \Upsilon_\ell g_\ell$. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

This follows from linearity: $D_v \sum_\ell \Upsilon_\ell g_\ell = \sum_\ell \Upsilon_\ell D_v g_\ell$, since $D_v$ is linear.

The frame must be the same for both incidences of a two-input gate. Suppose instead that the second incidence uses a different invertible operator $D'$ in place of $D_v$, with nonzero weights $\Upsilon_1, \Upsilon_2$. Let $\Psi$ be the moving-back operator, which returns the gate's stored output to logical form. Then $\Psi(\Upsilon_1 D_v g_1+\Upsilon_2 D' g_2)=\Upsilon_1 g_1+\Upsilon_2 g_2$ for all arrays. Setting $g_2=0$ and dividing by $\Upsilon_1$ gives $\Psi D_v=I$. Setting $g_1=0$ and dividing by $\Upsilon_2$ gives $\Psi D'=I$. So $\Psi=D_v^{-1}$, and $\Psi D'=I$ then forces $D'=D_v$.

A wire's logical array does not change along its length. <cite data-source="paper">Along an edge from u to v, the operator Dv Du−1 changes the stored array</cite>, so the stored array reaching the gate at $v$ is $D_v g$, in that gate's frame.

For example, let arrays have two entries, at addresses $0$ and $1$, let $\Upsilon_1=\Upsilon_2=1$, and let $D_v$ swap the two entries. Take $g_1=(1,0)$ and $g_2=(1,1)$. Then $G(D_v g_1, D_v g_2)=(0,1)+(1,1)=(1,2)$, while $D_v G(g_1,g_2)=D_v(2,1)=(1,2)$.
