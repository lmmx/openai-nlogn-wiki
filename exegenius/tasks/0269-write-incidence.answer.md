An incidence relates a wire to a [Gate and terminal of a network](network-gate-terminal.md): it holds when the wire touches that gate or terminal. The [subset-intersection network](subset-intersection-network.md) relies on incidences to say that every wire touching one gate is changed by the same frame, so the gate can be applied to the stored arrays directly.

A frame is an invertible linear operator on arrays, attached to a vertex $v$ of the network. <cite data-source="paper">We call Dv its frame: the stored array is Dv g when the logical array is g.</cite> So a vertex with frame $D_v$ stores $D_v g$ where the logical array is $g$.

Each gate has several incidences, one for each wire it touches, and the frame of the gate is shared by all of them. <cite data-source="paper">All incidences of one gate
have the same frame.</cite> A wire carries its frame change along its length, so the frame of an incidence is the frame of the gate on that side of the wire.

The reason for the shared frame is the identity that a pointwise linear gate satisfies. <cite data-source="paper">At a pointwise linear gate G, the common frame commutes with the gate:</cite>

$$G(D_v g_1, \dots, D_v g_t) = D_v\, G(g_1, \dots, g_t).$$

The left side applies the gate to the stored arrays on its incidences, and the right side applies the gate to the logical arrays and then the frame. Equality means the gate can run on stored arrays without first converting them back to logical form. The identity needs all $t$ incidences of the gate to use the same $D_v$: if one incidence used a different frame, the gate would combine arrays in two different representations, and no single operator would move the result back.

Worked example. Let arrays have two entries, indexed by addresses $0$ and $1$, and let the gate be pointwise addition, $G(g_1,g_2)=g_1+g_2$. Let the common frame $D_v$ swap the two entries. Take $g_1=(1,0)$ and $g_2=(1,1)$. Then $D_v g_1=(0,1)$ and $D_v g_2=(1,1)$, so $G(D_v g_1, D_v g_2)=(1,2)$. On the other side, $G(g_1,g_2)=(2,1)$ and $D_v(2,1)=(1,2)$. The two sides agree.
