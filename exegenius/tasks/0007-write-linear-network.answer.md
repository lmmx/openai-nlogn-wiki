A linear network that restores auxiliary values is a fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state. The [Subset-intersection network](subset-network.md) uses it.

Let $[h]=\{1,\dots,h\}$, where $h$ is the number of elements of the ground set. Let $\mathcal T$ be the set of three-element subsets of $[h]$, and write $v=\binom{h}{3}$ for the number of its elements. Two data banks $X_a$ and $Y_a$ are indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. The network is a linear operator in [Linear algebra over a field](linear-algebra.md). It has the fixed structure of a [Fixed-tape machine model](fixed-tape-machine.md): a fixed set of wires and a schedule that does not depend on the values it carries.

At stage $j$, fix the other two coordinates of $a$ and operate on the $v$ values obtained by varying coordinate $j$. Let $S,T\in\mathcal T$ be the varying coordinates of a forward invocation, which takes controls $x_T$ and targets $y_S$. In the bit construction, scalars lie in $\mathbb F_2$ and $S,T$ are neighbors when $|S\cap T|=1$. For each neighboring ordered pair $(S,T)$ there is a scratch wire $A_{ST}$, and for each $i\in[h]$ a central wire $C_i$. The gates are:

- copy, adding $x_T$ to $A_{ST}$;
- gather, adding $\sum_{T\ni i}x_T$ to $C_i$;
- scatter, adding $\sum_{i\in S}C_i$ to $y_S$;
- side injection, adding $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$.

Let $p$ and $q$ be the initial values of the $A_{ST}$ and $C_i$. Rows 0 and 1 subtract the side injection and scatter of $p$ and $q$, so old scratch contents do not survive in the targets. Rows 2 and 3 copy and gather the controls. Rows 4 and 5 add scatter and side injection of the updated scratch values, and rows 6 and 7 undo gather and copy. The net change is independent of $p$ and $q$. In the bit construction the coefficient of $x_T$ in $y_S$ is $|S\cap T|\bmod 2$, and side injection cancels the cases $|S\cap T|=1$, leaving only $T=S$. <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.</cite>

Stage 1 is a forward invocation from $X$ to $Y$. Stage 2 is the inverse schedule, with source $Y$ and target $X$, whose net effect is $X\gets X-Y$. Stage 3 repeats stage 1. Starting from $X=x$ and $Y=y$, the stages give $(x,y+x)$, $(-y,y+x)$, then $(-y,x)$. The composition therefore sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$, and every scratch wire is restored. <cite data-source="paper">In the bit construction this is the permutation exchanging $X_a$ and $Y_a$.</cite>
