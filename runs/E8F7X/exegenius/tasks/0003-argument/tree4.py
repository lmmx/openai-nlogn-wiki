from lib import *


def synth_transform():
    return show(
        r"On $\mathcal R_r=\mathbb C[y]/(y^r+1)$ the transforms $F_t^\pm$ with roots $\omega_t=y^{2r/t}$ are contractions with $F_t^+F_t^-=t^{-1}I$, and $F_t^-$ is computed by decimation-in-frequency rounds of $H_0$ butterflies and monomial twiddles.",
        "Treat powers of $y$ as roots of unity acting by signed shifts, prove character cancellation directly, and split each transform into pairs $z_k,z_{k+t/2}$ so that the length-$t/2$ procedure recurses on each branch.",
        mot("The ring has zero divisors, so character cancellation is verified directly instead of dividing by $\\omega_t^j-1$.", "explicit",
            (2807, r"The ring has zero divisors, so we verify character cancellation", r"directly instead of dividing by $\omega_t^j-1$.")),
        [
            infer(r"Every power of $\omega_t$ is an isometry and each transform entry averages $t$ such images, so both transforms are contractions.",
                  2805, r"Every power of $\omega_t$ is an isometry, and each transform entry is", r"Thus both transforms are contractions."),
            show(
                r"$\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise, hence $F_t^+F_t^-=t^{-1}I$.",
                "Pair the summands by a shift $k\\mapsto k+t/2^{v+1}$ that multiplies the sum by $y^{rj_0}=-1$, then expand the composite transforms.",
                mot("Because $\\mathcal R_r$ has zero divisors the usual geometric-series argument is unavailable, but a sign-changing shift of the index works.", "recoverable"),
                [
                    infer(r"Writing $j=2^vj_0$ with $j_0$ odd, replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies their sum by $y^{rj_0}=-1$, so the sum vanishes because the additive group has no two-torsion.",
                          2820, r"Write $j=2^v j_0$ with $j_0$ odd", r"has no two-torsion."),
                    infer(r"Expanding the composite transforms and using this identity proves $F_t^+F_t^-=t^{-1}I$.",
                          2824, r"Expanding the composite transforms", r"proves the final formula."),
                ],
                frm=["roots-of-unity", "summation-geometric-series-and-products"],
                salient="Character cancellation holds in a ring with zero divisors, because $y^{rj_0}=-1$ makes the shifted sum equal to its own negative."),
            infer(r"The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$, applies $H_0$, multiplies the $b=1$ output by $\omega_t^{-k}$ and recurses on each branch, computing $F_t^-$ by $(F_t^-z)_{2h+b}=\frac{1}{t/2}\sum_k(\omega_t^2)^{-hk}\omega_t^{-bk}\frac{z_k+(-1)^bz_{k+t/2}}2$.",
                  2832, r"For $t\geq2$, the decimation-in-frequency step pairs", r"\frac{z_k+(-1)^b z_{k+t/2}}2."),
        ],
        page="synthetic-transform",
        frm=["negacyclic-ring", "dft", "butterfly", "roots-of-unity", "multidimensional-dft", "error-accounting"],
        adds=[bind(r"t", "transform length", "the length of the transform, a power of two dividing $2r$", "count"),
              bind(r"\omega_t", "synthetic root", "the power $y^{2r/t}$ of the ring variable, acting as a primitive $t$-th root of unity by a signed shift", "direct")])


def retained_order():
    return show(
        r"The recursion writes frequency $j$ in slot $\operatorname{rev}_a(j)$, and the opposite procedure consuming that order implements $F_t^+B_t^{-1}$, so no sort is executed.",
        "Track which address-bit slots hold frequency bits after each level, then traverse the recursion in reverse for the opposite transform and count its scale factors.",
        mot("The recursion writes its outputs directly in this order and does not move whole frequency indices.", "explicit",
            (2869, r"directly in this order; it does not move whole frequency indices.")),
        [
            infer(r"After $s$ levels the values of the first $s$ named slots are branch bits, identified as frequency bits $0,\dots,s-1$ from the least significant end.",
                  2848, r"For $0\leq s\leq a$, after $s$ levels the values of", r"numbered from the least significant bit."),
            infer(r"After all $a$ rounds the slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ occupies slot $\operatorname{rev}_a(j)$; call this record permutation $B_t$.",
                  2864, r"After all $a$ rounds, the named slots from high to low therefore", r"occupies slot $\operatorname{rev}_a(j)$."),
            infer(r"Since $H_0^2=I/2$ each reversed level is half the inverse of its forward level, and with $a=\log_2t$ levels the reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$.",
                  2876, r"As $H_0^2=I/2$, the reversed level is half the inverse of the", r"$2^{-a}I=I/t$."),
            infer(r"Character cancellation gives the same composite for $F_t^+B_t^{-1}$, so the two reverse operators agree and the exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.",
                  2879, r"Lemma~\ref{lem:synthetic-characters} gives the same composite for", r"respectively."),
        ],
        page="retained-frequency-order",
        frm=["synthetic-transform", "butterfly", "permutations", "binary-representation-and-bitwise-operations"],
        salient="The bit-reversal permutation $B_t$ is never executed: it stays inside the stored order, and the opposite transform undoes it by running the recursion backwards.")


def transform_layout():
    return show(
        r"A layout permutation $L$ places the selected bits of all axes at a common offset in consecutive $K$-bit chunks, so every round is one simultaneous layer, and the forward and opposite procedures cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.",
        "Move one slot of each long axis and the lowest slots to a prefix, exchange width-$K$ chunks so the remaining slots sit chunk by chunk, run each round on the layout with one truncation, and add per-round errors.",
        mot("To apply the simultaneous layer in a round, the selected bits of the participating axes must sit at a common offset in consecutive $K$-bit chunks.", "explicit",
            (2918, r"To apply Proposition~\ref{prop:simultaneous-layer} in a transform round,", r"in consecutive $K$-bit chunks.")),
        [
            infer(r"A round applies one $H_0$ per participating axis, and the twiddle of one axis commutes with the other axes' butterflies, so a round is a parallel butterfly followed by one recordwise monomial $J_E$.",
                  2895, r"A round applies one current $H_0$ on each participating axis.", r"operation $J_E$."),
            infer(r"The at most $D(b+1)=O(dK)$ listed slots moved to a prefix cost $O(TpdK)$.",
                  2999, r"Form a list of the slots to move to a prefix.", r"so the moves cost $O(TpdK)$."),
            infer(r"At most $Dq-1$ exchanges of width-$K$ chunks reach the chunk-major order, each costing $O(TpK^\tau)$, so in total $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$.",
                  3019, r"To obtain this order, scan its target positions from left to right.", r"=O\bigl(Tp\,pK^{\tau-1}\bigr)."),
            infer(r"Rounds run at position $h=\ell-1$ on the long axes first, then $h=\ell-2,\dots,b$ on the remaining chunks, then the bottom positions, so all axes in a round have current length $2^{h+1}$.",
                  3058, r"First process the round at named position $h=\ell-1$ on the long", r"current length $u_i=2^{h+1}$."),
            infer(r"In each chunk round the layer sees the complete address set $[P]\times[2^K]^D\times[S]$ with $n_P+DK+n_S\le D\ell=O(p)$.",
                  3075, r"Every combination of those bits occurs, so the layer sees the complete address set", r"\leq D\ell=O(p)."),
            infer(r"The simultaneous layer therefore costs $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.",
                  3103, r"The simultaneous-layer procedure therefore applies at cost", r"in total."),
            infer(r"On prefix slots the bits are processed individually without truncation, since after $s\le D$ factors the coefficients are exact dyadics on the $2^{-(p+s)}$ grid and stay in the disk.",
                  3115, r"That width suffices without truncating between axes:", r"still lie in the disk."),
            infer(r"There are at most $b+1\le K$ rounds on prefix slots, giving cost $O(TpdK)$.",
                  3127, r"most $b+1\leq K$ rounds on prefix slots, giving cost $O(TpdK)$."),
            infer(r"Multiplying by $y^E$ with $E=er+s$ splits the coefficient list before position $r-s$, puts the tail before the head, negates the moved tail and applies the sign $(-1)^e$.",
                  3148, r"To implement the monomial, write $E=er+s$ with $0\leq s<r$.", r"modulo $y^r+1$."),
            infer(r"Truncation toward zero is odd and acts on each real and imaginary part, and $J_E$ is a signed coefficient permutation, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: truncating once after the exact round is what happens.",
                  3162, r"Truncation toward zero is odd", r"Q_p(J_E\mathcal H z)."),
            infer(r"A contraction does not increase the difference between computed and exact arrays and one truncation adds less than $\sqrt2\,2^{-p}$, so after at most $\ell$ rounds the error is below $\sqrt2\,\ell\,2^{-p}$ and the disk is preserved.",
                  3171, r"A contraction does not increase the norm of the difference", r"give the claimed error and disk bounds."),
            infer(r"The forward entry with frequency address $j$ is stored at $L(Bj)$, and the full exact operators are $LBF^-_{\boldsymbol t}$ and $F^+_{\boldsymbol t}B^{-1}L^{-1}$.",
                  3194, r"In particular, the forward entry with frequency address $j$ is", r"stored at $L(Bj)$."),
        ],
        page="transform-layout",
        frm=["synthetic-transform", "retained-frequency-order", "simultaneous-butterfly-layer", "arbitrary-width-interchange",
             "stream-operations", "fixed-point-disk", "error-accounting", "multidimensional-dft", "negacyclic-ring"],
        salient="The cost has three terms of different character: the prefix moves $dK$ and the chunk exchanges $pK^{\\tau-1}$ both depend on the chunk width $K$ in opposite ways, which forces $K$ to grow, but only slowly.")


def signed_packing():
    return show(
        r"Evaluating polynomial records at $2^{4p}$ turns the ring product $fg$ into four signed integer products of $O(rp)$ bits, from which the exact negacyclic product is recovered, and $Q_p(fg/r)$ is returned in $O(rp\log(rp))$.",
        "Use a signed Kronecker substitution: choose a base so large that product coefficients cannot overlap, multiply the four signed evaluation integers with the established multiplier, and read the coefficients back by carry-tracking extraction.",
        mot("The reduction is a signed form of Kronecker substitution; the packing and recovery must also handle negative coefficients and the tape format.", "explicit",
            (3217, r"reduction is a signed form of Kronecker substitution")),
        [
            infer(r"Writing $f=2^{-p}(a+ib)$, $g=2^{-p}(c+ie)$ with integer polynomials of coefficients at most $2^p$, the evaluation integers $A_u=u(2^{4p})$ for $u\in\{a,b,c,e\}$ each fit in $4pr$ bits.",
                  3239, r"where $a,b,c,e\in\mathbb Z[y]$ have degree less than $r$ and", r"A_u=u(B_0)=\sum_{j=0}^{r-1}u_jB_0^j."),
            infer(r"Every coefficient of an ordinary product satisfies $|h_j|\le r2^{2p}<2^{3p}<B_0/2$, so after removing lower coefficients the next is identified by its centred residue modulo $B_0$.",
                  3260, r"|h_j|\leq r2^{2p}<2^{3p}<B_0/2.", r"residue modulo $B_0$."),
            infer(r"When forming $A_u$ the carry stays in $\{-1,0\}$ because $-B_0<u_j+\gamma_j<B_0$, giving a two's-complement block encoding with $\gamma_r=-1$ exactly when $A_u<0$.",
                  3270, r"Since $-B_0<u_j+\gamma_j<B_0$ whenever", r"the carry stays in $\{-1,0\}$."),
            infer(r"Extraction reads one block at a time with a centred representative $\widehat h_j$ of $q_j+\rho_j$ modulo $B_0$ and a carry $\rho_{j+1}\in\{0,1\}$ updated by a constant-size step.",
                  3298, r"Put $\rho_0=0$.", r"or subtracts $B_0$."),
            infer(r"By the separation bound the centred representative of $q_j+\rho_j$ is $h_j$ itself, so $\widehat h_j=h_j$ and the residual identity propagates to the next block.",
                  3318, r"For $j<J$, reduction modulo $B_0$ gives", r"Thus $\widehat h_j=h_j$."),
            infer(r"The real and imaginary numerator streams are $ac-be$ and $ae+bc$; reduction modulo $y^r+1$ subtracts the coefficient at $j+r$ from the one at $j$.",
                  3331, r"The real and imaginary numerator streams are respectively", r"treating a missing coefficient as zero."),
            infer(r"Each wrapped coefficient is a sum of exactly $r$ signed products of Gaussian integers of modulus at most $2^p$, so $|H_j|\le r2^{2p}$.",
                  3338, r"resulting Gaussian integer coefficient $H_j$ is a sum of exactly", r"|H_j|\leq r2^{2p}."),
            infer(r"The returned $p$-bit grid numerator is the truncation toward zero of $\Re H_j/2^{p+\ell}$ plus $i$ times that of $\Im H_j/2^{p+\ell}$, a shift of the magnitude by $p+\ell$ bits.",
                  3352, r"Finally the $p$-bit grid numerator of the normalized product is",
                  r"+i\operatorname{trunc}_0\left(\frac{\Im H_j}{2^{p+\ell}}\right)."),
            infer(r"Four exact integer products dominate the linear packing, extraction, combination, wrapping and truncation costs, giving $O(rp\log(rp))$ with the $O(N\log N)$ multiplier.",
                  3366, r"Four exact integer products dominate the linear", r"truncation costs."),
        ],
        page="signed-packing-product",
        frm=["established-multiplier", "negacyclic-ring", "fixed-point-disk", "polynomials", "schoolbook-integer-arithmetic"])


def synth_convolution():
    norm = show(
        r"Two forward transforms, a pointwise ring product divided by $r$, the opposite transform and an exact scaling by $M$ compute $\mathcal M_r(f,g)=(f*g)/T$.",
        "Check the normalization identity with the convolution theorem, then show that permuting records by $LB$ commutes with the pointwise product, so the retained order feeds the opposite transform.",
        mot("Pointwise products commute with a common record permutation, so no reordering is needed between the transforms.", "recoverable"),
        [
            infer(r"Expanding the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$, and with $F^+F^-=I/M$ this gives $MF^+\bigl((F^-f)(F^-g)/r\bigr)=(f*g)/(rM)$.",
                  3422, r"To check normalization, expansion of the finite sums gives", r"=\frac{f*g}{rM}."),
            infer(r"Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so $\mathcal T_+$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$.",
                  3437, r"Since $LB$ permutes records and leaves their polynomial suffixes",
                  r"$F_{\boldsymbol t}^+P(F_{\boldsymbol t}^-f,F_{\boldsymbol t}^-g)$."),
        ])
    err = show(
        r"The computed convolution has error below $\sqrt2\,M(3\ell+1)2^{-p}$.",
        "Chain the errors through the exact bilinear contraction $P$: two forward errors below $\\delta$ give $2\\delta$ at the product, one truncation adds $\\eta$, the opposite contraction does not enlarge it and adds its own $\\delta$, and the final scale multiplies by $M$.",
        mot("All maps are contractions on disk arrays, so errors only add and never amplify.", "recoverable"),
        [
            infer(r"With $\delta=\sqrt2\ell2^{-p}$ and $\eta=\sqrt2\,2^{-p}$ the exact stored forward outputs $u,v$ and returned ones $\widetilde u,\widetilde v$ are disk arrays within $\delta$, and the exact product $P$ is bilinear with $\|P(x,y)\|\le\|x\|\|y\|$.",
                  3443, r"For the error estimate, put", r"bound in Lemma~\ref{lem:signed-ring-product}."),
            infer(r"Splitting $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$ and using the disk bounds gives error below $2\delta$.",
                  3455, r"\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty", r"second uses it on $u$."),
            infer(r"The truncated product $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ is a disk grid array within $2\delta+\eta$ of $z_*=P(u,v)$.",
                  3461, r"Write $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$", r"$\|\widetilde z-z_*\|_\infty<2\delta+\eta$."),
            infer(r"Since $\mathcal T_+$ is a contraction, the returned opposite output is within $3\delta+\eta$ of $\mathcal T_+z_*$.",
                  3464, r"If $\widetilde h$ is the returned opposite output,", r"<3\delta+\eta."),
            infer(r"The exact scaling by $M$ gives error below $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$.",
                  3472, r"The final exact multiplication by $M$ therefore gives error less than", r"as claimed."),
        ],
        frm=["triangle-inequality-and-norms", "error-accounting"],
        salient="The bound $\\sqrt2\\,M(3\\ell+1)2^{-p}$ counts exactly three transforms' worth of error plus one truncation, because every map is a contraction and so errors only add.")
    return show(
        r"Two forward synthetic transforms in layout order, a pointwise ring product divided by $r$, the opposite transform and an exact scaling by $M$ compute the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ with error below $\sqrt2\,M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.",
        "Build it from the transform with retained frequency order, the layout that makes every round a simultaneous layer, and the signed-packing ring product; then verify normalization and add errors.",
        mot("Pointwise multiplication commutes with applying the same record permutation to both operands, so the forward outputs can be multiplied in their retained order and passed directly to the opposite procedure.",
            "explicit", (3202, r"Pointwise multiplication commutes with applying the same record permutation", r"pass that order directly to the opposite procedure.")),
        [
            synth_transform(),
            retained_order(),
            transform_layout(),
            infer(r"Pointwise multiplication commutes with applying the same record permutation $LB$ to both operands, so the forward outputs can be multiplied in their retained order and passed to the opposite procedure.",
                  3202, r"Pointwise multiplication commutes with applying the same record permutation", r"directly to the opposite procedure."),
            signed_packing(),
            infer(r"A coefficient of $\mathcal M_r(f,g)$ averages $rM$ signed scalar products, so $\mathcal M_r$ is a bilinear contraction with $\|\mathcal M_r(f,g)\|\le\|f\|\|g\|$.",
                  3382, r"Thus that coefficient averages", r"bilinear contraction:"),
            norm,
            err,
            infer(r"There are $M=T/r$ pointwise polynomial products costing $O(Tp\log(rp))$ in total; the three transforms cost as stated and the last scaling is linear.",
                  3491, r"There are $M=T/r$ pointwise polynomial products.", r"linear in $Tp$."),
        ],
        page="synthetic-convolution",
        frm=["synthetic-transform", "retained-frequency-order", "transform-layout", "signed-packing-product", "cyclic-convolution",
             "multidimensional-dft", "error-accounting", "negacyclic-ring", "dft"],
        adds=[bind(r"\ell", "axis bits", "the base-2 logarithm of the polynomial length, $\\ell=\\log_2r$, which is the number of address bits of a long axis", "direct"),
              bind(r"M", "record count", "the number of polynomial records, $M=T/r$, one for each point of the first $d-1$ axes", "count")])
