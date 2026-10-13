The operator norm of a linear map is the largest factor by which the map can stretch a vector, measured in a chosen vector norm. The argument uses it to bound how far a transform can grow its input. Because such bounds multiply along a chain of maps, the size of a composite can be controlled one stage at a time.

Let $\Phi$ be a linear map from one finite-dimensional complex vector space to another, each with a chosen vector norm $\|\cdot\|$. Write $\xi$ for a vector in the domain of $\Phi$. The operator norm of $\Phi$ is

$$\|\Phi\| = \sup\{\, \|\Phi\xi\| : \|\xi\| \le 1 \,\}.$$

So $\|\Phi\|$ is the largest value that $\|\Phi\xi\|$ takes on the unit ball $\{\xi : \|\xi\| \le 1\}$. In finite dimensions the unit ball is compact, so the supremum is attained and is a maximum.

Two facts follow from the definition. First, $\|\Phi\xi\| \le \|\Phi\|\,\|\xi\|$ for every vector $\xi$: for $\xi \ne 0$, apply the definition to $\xi/\|\xi\|$. Second, $\|\Phi\|$ is the smallest constant $c$ with $\|\Phi\xi\| \le c\|\xi\|$ for all $\xi$, so it is the sharpest bound of this form. Consequently, if $\Psi$ is a second linear map whose output can be fed into $\Phi$, then

$$\|\Phi\Psi\| \le \|\Phi\|\,\|\Psi\|,$$

since $\|\Phi\Psi\xi\| \le \|\Phi\|\,\|\Psi\xi\| \le \|\Phi\|\,\|\Psi\|\,\|\xi\|$. This is why a chain of stages can be bounded one stage at a time.

Example. Let $\Phi(\xi_1,\xi_2) = (\xi_1+\xi_2,\,0)$ on $\mathbb{C}^2$, with the maximum norm $\|\xi\| = \max_j |\xi_j|$. If $\|\xi\| \le 1$ then $|\xi_1+\xi_2| \le 2$, and $\xi=(1,1)$ attains the value 2. So $\|\Phi\| = 2$.
