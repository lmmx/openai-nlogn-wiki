Synthetic polynomial transforms are transforms of a list of ring elements in which every twiddle factor is a power of $y$, so the transform needs no general multiplications: only signed shifts, address rearrangements and butterflies. They serve the argument by making the convolution over the remaining axes cheap enough for a fixed-tape machine.

Synthetic polynomial transforms work over the [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md), where $y^r=-1$. Take $r=4$ and the element $1+2y+3y^2+4y^3$. Multiplying it by $y^2$ gives $y^2+2y^3+3y^4+4y^5=-3-4y+y^2+2y^3$. In coefficient-list form, $(1,2,3,4)$ becomes $(-3,-4,1,2)$: each coefficient moves up two places, and the two that wrap past the end return with a minus sign. Multiplying by any power of $y$ below $y^r$ works the same way, so it is a signed shift of the coefficient list.

The transform's roots of unity are therefore powers of $y$ <cite data-source="paper">Powers of $y$ then serve as roots of unity in the remaining axes</cite>.

Like the [Discrete Fourier transform and butterflies](dft-fft.md), a synthetic transform computes its transforms by butterfly levels: each level combines pairs of entries into their sum and their difference, after multiplying one of them by a power of $y$.

The method shows the claim directly. Every multiplication inside a butterfly is by a power of $y$, hence a signed shift; the rest of each level is addition and subtraction, and moving entries between levels is an address rearrangement. The motivation is that multiplying by a general complex root costs real multiplications, which a signed shift avoids.
