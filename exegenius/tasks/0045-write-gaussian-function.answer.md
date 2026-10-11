The Gaussian function is a bell-shaped weight that decays rapidly away from its centre. The argument uses it as a smooth weight that moves values between two grids of frequencies.

Here $z$ is a real number, the distance from the centre at which the weight is evaluated. Here $\alpha$ is an integer width parameter with $\alpha\ge 2$, and a larger $\alpha$ gives a wider bell. Write $G_\alpha$ for the Gaussian function, $G_\alpha(z)=e^{-\pi z^2/\alpha^2}$. The weight is largest at the centre, $G_\alpha(0)=1$, and the shifted copy $G_\alpha(z-c)$ is centred at $c$. For example, with $\alpha=2$, $G_2(4)=e^{-4\pi}\approx 3.5\times 10^{-6}$, so the weight four units from the centre is already negligible.

Let $s$ and $t$ be integers, and let $u$ be a vector of $s$ values. The Gaussian function is used to build the [linear map](linear-map.md) $S$ below. Here $\kappa$ is the position of an output value, and $\ell$ is a summation index over the integers. For $0\le\kappa<t$,
$$(Su)_\kappa=\frac1\alpha\sum_{\ell\in\mathbb Z}G_\alpha\!\left(\ell-\frac{s\kappa}{t}\right)u_\ell.$$
Each output is a weighted sum of inputs near the point $s\kappa/t$, since the weight decays away from that point.

Gaussian weights are used to resample the [discrete Fourier transform](discrete-fourier-transform.md) on grids of lengths $s$ and $t$. The second map $T$ is built the same way with the roles of the two grids exchanged. Here $N$ is a correction map built from $S$, $T$, a diagonal rescaling and a selection of coordinates. The terms of $N$ other than the selected one are negligible when $\alpha^2\theta>1$, where $\theta=t/s-1$. <cite data-source="paper">Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series.</cite>
