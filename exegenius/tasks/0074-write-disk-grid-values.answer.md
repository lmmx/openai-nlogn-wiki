A disk-grid value is a complex number stored exactly as a pair of fixed-point numbers: its real and imaginary parts are integers divided by $2^p$, for a fixed number $p$ of fractional bits. The set of such numbers is a grid in the complex plane with spacing $2^{-p}$ in each direction.

For example, with $p = 2$ the grid contains $\tfrac14 + \tfrac12 i$ and $-\tfrac34$, but not $\tfrac13$. Each stored value is therefore determined by two integers, which is the form the tape procedures handle.

The paper's coefficient arrays consist of such values with norm less than $\tfrac14$. Keeping the norm bounded in this way is what allows the rounding error of a single truncation to stay below the level needed for exact recovery.

The grid also makes the arithmetic exact up to a known rounding. A sum of two grid values is again on the grid, and a product is on the grid of twice the precision, which is then truncated back to $p$ fractional bits. The truncation back to $p$ bits is a rounding step, and the [precision and exact recovery](precision-and-rounding.md) page bounds the total effect of such steps.
