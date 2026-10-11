An incidence relates a wire to a [Gate and terminal of a network](network-gate-terminal.md): it holds when the wire touches that gate or terminal. The [subset-intersection network](subset-intersection-network.md) uses incidences to change every wire at one gate by the same frame, so the gate can run on the stored arrays directly.

Every incidence lies in a linear network, and the [frame of a gate](linear-network-frames.md) is shared by all its incidences. <cite data-source="paper">All incidences of one gate have the same frame.</cite>

A frame is an invertible linear operator on arrays, attached to a vertex $v$. <cite data-source="paper">We call Dv its frame: the stored array is Dv g when the logical array is g.</cite> So the stored array at $v$ is $D_v g$ when the logical array there is $g$.

Let a pointwise linear gate $G$ take $t$ input wires. Let $g_1, g_2, \dots, g_t$ be the logical arrays on the $t$ input wires of the gate, so $g_s$ is the logical array on input wire $s$. The weights $\alpha_s$ are the same at every address, so $G(g_1,\dots,g_t)=\sum_{s=1}^t \alpha_s g_s$. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

This follows from linearity. Each $D_v$ is linear, so $D_v \sum_s \alpha_s g_s = \sum_s \alpha_s D_v g_s$. The left side is $\sum_s \alpha_s D_v g_s$, so the two sides agree for every choice of arrays.

All incidences must use the same frame. Suppose the second incidence used a different invertible operator $D'$ in place of $D_v$, with nonzero weights $\alpha_1,\alpha_2$. The gate then produces $\alpha_1 D_v g_1 + \alpha_2 D' g_2$, while one operator $\Gamma$ would have to move the result back to logical form, giving $\Gamma(\alpha_1 g_1+\alpha_2 g_2)$. Setting $g_2=0$ gives $\Gamma g_1 = D_v g_1$ for every $g_1$, so $\Gamma=D_v$. Setting $g_1=0$ gives $\Gamma=D'$. Hence $D'=D_v$.

A wire's logical array does not change along its length; the edge from $u$ to $v$ applies an operator to the stored array as it passes. <cite data-source="paper">Along an edge from u to v, the operator Dv Du−1 changes the stored array from Du g to Dv g.</cite> So the stored array reaching the gate at $v$ is $D_v g$, in that gate's frame, and that is the frame of the incidence on that side.

For example, let arrays have two entries, at addresses $0$ and $1$, let $\alpha_1=\alpha_2=1$, and let $D_v$ swap the two entries. Take $g_1=(1,0)$ and $g_2=(1,1)$. Then $G(D_v g_1, D_v g_2)=(0,1)+(1,1)=(1,2)$, while $D_v G(g_1,g_2)=D_v(2,1)=(1,2)$.
