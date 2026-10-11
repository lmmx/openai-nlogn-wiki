An axis line is the set of entries of a multidimensional array that vary along one chosen axis while all other coordinates stay fixed. The argument uses axis lines to state how a [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) acts on several axes at once.

Each axis line is taken along one [Transform axis](transform-axis.md) $i$. Let $X$ be the array, indexed by $D$ coordinates, one for each axis, and write $X(x_1,\dots,x_D)$ for its entry at the address $(x_1,\dots,x_D)$, where $x_j$ runs from $0$ to $t_j-1$. To form the axis-$i$ line, fix a value of every other coordinate $x_j$ with $j \neq i$, and let $x_i$ run from $0$ to $t_i-1$. The line is the set of the $t_i$ entries $X(x_1,\dots,x_D)$ obtained this way.

For example, let $D=2$, $t_1=2$ and $t_2=3$, so $X$ is a $2\times 3$ array with entries $X(x_1,x_2)$ for $x_1\in\{0,1\}$ and $x_2\in\{0,1,2\}$. The axis-1 line with $x_2=2$ holds the two entries $X(0,2)$ and $X(1,2)$. The axis-2 line with $x_1=1$ holds the three entries $X(1,0)$, $X(1,1)$ and $X(1,2)$.

For a fixed axis $i$, every entry of $X$ lies on exactly one axis-$i$ line, since the line is determined by the values of the coordinates other than $x_i$. So the axis-$i$ lines partition the entries of $X$, and there are $\prod_{j\neq i} t_j$ of them. A map that acts within each line of one axis changes entries only along that axis.

The paper's tensor-product construction uses this decomposition: <cite data-source="paper">apply the one-dimensional maps to one coordinate line at a time</cite>.
