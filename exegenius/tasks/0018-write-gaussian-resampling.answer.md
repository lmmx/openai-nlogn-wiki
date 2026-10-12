Gaussian resampling is a technique that replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, which the integer multiplier needs. It moves values between the two sets of frequencies with Gaussian weights, which are exponential factors that decay quadratically with distance.

It replaces the Fourier transforms needed for a [radix-digit convolution](radix-digit-convolution.md) by transforms whose axis lengths are powers of two. The integer product needs pairwise coprime transform lengths, but the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes</cite>.

Here $s$ is the number of coordinates of a source vector, and $t$ is the number of coordinates of a target vector, with $s<t$ and $\gcd(s,t)=1$. The integer $\alpha$ is the width parameter of the Gaussian weights. $F_s$ and $F_t$ are the normalized Fourier transforms of length $s$ and $t$. $P_s$ and $P_t$ are the coordinate permutations $(P_s g)_j=g_{tj}$ and $(P_t h)_m=h_{-sm}$ on vectors $g$ of length $s$ and $h$ of length $t$, with $j$ and $m$ the coordinate indices and subscripts taken modulo the length. $I$ is the identity map.

The operator norm $\|\cdot\|$ of a linear map is the largest factor by which the map stretches a vector, where vectors are measured in the maximum-modulus norm, the largest absolute value of a coordinate. A map is a contraction when its operator norm is at most $1$.

The identity rests on two Gaussian-weighted maps $S$ and $T$ from vectors of length $s$ to vectors of length $t$. $D$ is the diagonal map on vectors of length $s$ that multiplies coordinate $j$ by a Gaussian factor, and $C$ selects from a length-$t$ vector the coordinates at the indices nearest $tj/s$, for $0\le j<s$. Put $N=CTD$, a map close to $I$.

The argument has four steps.

First, $TP_sF_s=P_tF_tS$ holds before normalization, as an exact Gaussian identity <cite data-source="paper">[15, Theorem 4.2 and Lemma 4.6]</cite>.

Second, the source gives $\|N-I\|<1/2$ <cite data-source="paper">∥N − I∥ < 1/2, so N is invertible by the Neumann series</cite>, so $N$ is invertible. Its inverse is the Neumann series $N^{-1}=\sum_{r\ge 0}(I-N)^r$, where $r$ is the summation index. Each term has norm at most $2^{-r}$, so the series converges, and multiplying its partial sums by $N$ leaves $I$ minus a power of $I-N$, which tends to $0$.

Third, since $N=CTD$, we have $CT=ND^{-1}$. Hence $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$, so $DN^{-1}C$ is a left inverse of $T$. Applying it to the first identity gives $DN^{-1}CP_tF_tS=P_sF_s$.

Fourth, set $A=S/2$ and $B_0=2^{-(2\alpha^2-2)}DN^{-1}C/2$. The scale factors multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$. Multiplying by $2^{2\alpha^2}$ gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$.

Both factors are contractions. $N-I$ is small because $D$ cancels the Gaussian factor at each selected coordinate, leaving only the small Gaussian weights of the other coordinates. The source bounds $\|S/2\|<3/4$ and $\|N^{-1}/2\|<7/8$, and $\|2^{-(2\alpha^2-2)}D\|<1$ <cite data-source="paper">∥D′ ∥ < 1</cite>. Since $\|C\|=1$, the product $B_0$ has norm below $1$.
