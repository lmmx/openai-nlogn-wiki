Gaussian resampling is a technique that replaces a [Discrete Fourier transform](discrete-fourier-transform.md) of arbitrary length by transforms whose axis lengths are powers of two, which the integer multiplier needs. Gaussian weights are exponential factors that decay quadratically with distance, and they move values between the two sets of frequencies.

Gaussian resampling computes the transforms of a [radix-digit convolution](radix-digit-convolution.md) from power-of-two transforms.

The integer product needs transform lengths that are pairwise coprime, while the synthetic transforms use powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes</cite>, so the transform of one length must be moved onto the frequencies of the other.

Here $s$ is the number of coordinates of a source vector. Here $t$ is the number of coordinates of a target vector, with $s<t$ and $\gcd(s,t)=1$. The integer $\alpha$ is the width parameter of the Gaussian weights. $F_s$ and $F_t$ are the normalized Fourier transforms of length $s$ and $t$, and $P_s$ and $P_t$ are the coordinate permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, with subscripts taken modulo the length.

The operator norm of a linear map is the largest factor by which it stretches a vector in the maximum-modulus norm. A linear map is a contraction when its operator norm is at most 1. $A$ is a linear contraction from vectors of length $s$ to vectors of length $t$, and $B_0$ is a linear contraction from vectors of length $t$ to vectors of length $s$.

The identity rests on two Gaussian-weighted maps $S$ and $T$ from vectors of length $s$ to vectors of length $t$. $D$ is the diagonal map on vectors of length $s$ that multiplies coordinate $j$ by a Gaussian factor, and $C$ selects from a length-$t$ vector the coordinates at the indices nearest $tj/s$, for $0\le j<s$. Put $N=CTD$, a map close to the identity.

1. $TP_sF_s=P_tF_tS$, the Gaussian resampling identity before normalization.
2. $\|N-I\|<1/2$, so $N$ is invertible. If $\|N-I\|<1$, then $N^{-1}=\sum_{k\ge 0}(I-N)^k$, a Neumann series whose terms shrink geometrically in operator norm.
3. Since $CT=ND^{-1}$, the map $DN^{-1}C$ is a left inverse of $T$, because $(DN^{-1}C)T=DN^{-1}ND^{-1}=I$. Applying it to step 1 gives $DN^{-1}CP_tF_tS=P_sF_s$.
4. The factors of 2 are absorbed by taking $A=S/2$ and $B_0=2^{-(2\alpha^2-2)}DN^{-1}C/2$. Their scale factors multiply to $2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.

Multiplying by $2^{2\alpha^2}$ gives $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, with contractions $A$ and $B_0$.
