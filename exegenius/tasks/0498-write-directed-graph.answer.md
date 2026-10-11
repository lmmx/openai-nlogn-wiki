A directed graph is the basic network structure the later pages use to describe wiring: a set of points, and a set of one-way connections between them. Later pages build their circuit descriptions on it.

A directed graph is a pair $G = (V, E)$ of a set $V$ of vertices and a set $E$ of ordered pairs of vertices. Each element $(u, v)$ of $E$ is a directed edge from $u$ to $v$, where $u$ and $v$ are vertices and $(u, v)$ is an ordered pair, a two-entry tuple whose first entry is $u$ and whose second entry is $v$. Because the pair is ordered, $(u, v)$ and $(v, u)$ are different edges, and the edge $(u, v)$ points only from $u$ to $v$.

For example, take $V = \{1, 2, 3\}$ and $E = \{(1, 2), (2, 3), (1, 3)\}$. The edge $(1, 2)$ leaves vertex $1$ and enters vertex $2$. Vertex $1$ has two outgoing edges, to $2$ and to $3$, and no incoming edges. Vertex $3$ has two incoming edges and no outgoing edges. If $(3, 1)$ were added to $E$, it would be a new edge, distinct from $(1, 3)$.

An edge of the form $(u, u)$, which starts and ends at the same vertex, is called a loop. The definition allows loops, and it allows several edges between the same two vertices only if they are distinct ordered pairs, so $E$ is a set with no repeated edges.
