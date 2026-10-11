Two events are independent when the probability that both occur equals the product of their probabilities. The wiki's exact-recovery step relies on this page: [Exact coefficient recovery](recovery-and-error.md) concludes that the recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients.

An experiment has a finite set $\Omega$ of possible outcomes, the sample space. An event is a subset of $\Omega$, and the outcomes in an event are the ones for which it occurs. Let $\mathcal{C}$ and $\mathcal{D}$ be events, that is, subsets of $\Omega$. When every outcome is equally likely, the probability of an event $\mathcal{C}$ is $\Pr(\mathcal{C}) = |\mathcal{C}|/|\Omega|$, where $\Pr$ is the probability function and $|\mathcal{C}|$ is the number of outcomes in $\mathcal{C}$.

The event $\mathcal{C}\cap\mathcal{D}$, where $\mathcal{C}\cap\mathcal{D}$ is the event that both occur, consists of the outcomes lying in both events. The events $\mathcal{C}$ and $\mathcal{D}$ are independent when

$$\Pr(\mathcal{C}\cap\mathcal{D}) = \Pr(\mathcal{C})\,\Pr(\mathcal{D}).$$

So independence is a numerical test on the two probabilities and the probability of their overlap.

**Example.** Roll one fair six-sided die, so $\Omega=\{1,2,3,4,5,6\}$ and each face has probability $1/6$. Let $\mathcal{C}$ be the event that the roll is even, $\mathcal{C}=\{2,4,6\}$, and let $\mathcal{D}$ be the event that the roll is at most 4, $\mathcal{D}=\{1,2,3,4\}$. Then

$$\Pr(\mathcal{C})=\tfrac{3}{6}=\tfrac12,\qquad \Pr(\mathcal{D})=\tfrac{4}{6}=\tfrac23,\qquad \Pr(\mathcal{C}\cap\mathcal{D})=\Pr(\{2,4\})=\tfrac{2}{6}=\tfrac13.$$

Since $\tfrac13=\tfrac12\cdot\tfrac23$, the events $\mathcal{C}$ and $\mathcal{D}$ are independent. The event $\{1,2,3\}$ fails the test with $\mathcal{C}$: it has probability $\tfrac12$, the overlap $\{2\}$ has probability $\tfrac16$, and $\tfrac16\neq\tfrac12\cdot\tfrac12$.
