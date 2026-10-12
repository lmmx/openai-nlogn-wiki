A linear network that restores auxiliary values is a fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state. The [Subset-intersection network](subset-network.md) uses it to swap two banks.

Let $[h]=\{1,\dots,h\}$, where $h$ is the number of elements of the ground set. Here $T$ denotes a three-element subset of $[h]$, not the earlier linear map. Let $\mathcal T$ be the set of all such subsets. Two data banks $X_a$ and $Y_a$ are indexed by $a=(a_1,a_2,a_3)\in\mathcal T^3$. The network is a linear operator in [Linear algebra over a field](linear-algebra.md). It has the fixed structure of a [Fixed-tape machine model](fixed-tape-machine.md): its wires and schedule do not depend on the values.

A forward invocation takes controls $x_T$ and targets $y_S$, where $S,T\in\mathcal T$. Subsets $S$ and $T$ are neighbors when $|S\cap T|=1$. For each ordered neighbor pair $(S,T)$ there is a scratch wire $A_{ST}$, and for each $i\in[h]$ a central wire $C_i$. Its four gates are:

- copy: add $x_T$ to $A_{ST}$;
- gather: add $\sum_{T\ni i}x_T$ to $C_i$;
- scatter: add $\sum_{i\in S}C_i$ to $y_S$;
- side injection: add $\sum_{T:\,|S\cap T|=1}A_{ST}$ to $y_S$.

Each gate adds a sum of other wires to one wire, so the reversed, negated gate list undoes an invocation.

Let $p$ and $q$ be the initial values of the $A_{ST}$ and $C_i$. Rows 0 and 1 subtract the side injection and scatter of $p$ and $q$ from $y_S$. Rows 2 and 3 copy and gather, so $A_{ST}=p_{ST}+x_T$ and $C_i=q_i+\sum_{T\ni i}x_T$. Rows 4 and 5 add scatter and side injection of the updated wires. Rows 6 and 7 undo gather and copy, returning the wires to $p$ and $q$.

Rows 0 and 1 subtract exactly the $p$ and $q$ terms that rows 4 and 5 add, so the old scratch contents cancel:
$$y_S\gets y_S+\sum_{i\in S}\sum_{T\ni i}x_T+\sum_{T:\,|S\cap T|=1}x_T.$$
The first sum gives $x_T$ the coefficient $|S\cap T|$, and the side injection adds $1$ more when $|S\cap T|=1$. Modulo 2 the total is $1$ only when $|S\cap T|=3$, that is $T=S$, since $1+1=0$. So $y_S$ becomes $y_S+x_S$ and no other value changes. This matches the paper's lemma. <cite data-source="paper">For arbitrary initial values of its auxiliary wires, a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.</cite>

Stage 1 is a forward invocation from $X$ to $Y$, so $Y_a$ becomes $Y_a+X_a$ for each $a$. Stage 2 is the reversed, negated gate list of a forward invocation from $Y$ to $X$, which adds $Y_a$ to $X_a$; undoing it changes $X_a$ to $X_a-Y_a$. Stage 3 repeats stage 1. For single values $X=x$ and $Y=y$ the stages give $(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$. Every invocation restores its scratch wires, so the composition sends $(X_a,Y_a)\mapsto(-Y_a,X_a)$. Over $\mathbb F_2$ the sign is immaterial. <cite data-source="paper">In the bit construction this is the permutation exchanging $X_a$ and $Y_a$.</cite>
