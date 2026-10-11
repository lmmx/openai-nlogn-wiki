The floor function rounds a real number down to an integer. The exact multiplication argument relies on it to split integers into radix digits and to propagate carries between those digits.

## Definition

The floor $\lfloor\xi\rfloor$ of a real number $\xi$ is the greatest integer not greater than $\xi$. Equivalently, $\lfloor\xi\rfloor$ is the unique integer with
$$\lfloor\xi\rfloor\le\xi<\lfloor\xi\rfloor+1.$$

Every value of the floor function is an [integer](integer.md), so the floor function takes values in the integers.

Examples. $\lfloor 7/2\rfloor=3$, because $3\le 3.5<4$. An integer is its own floor: $\lfloor 4\rfloor=4$. Negative inputs round down, not toward zero: $\lfloor -7/2\rfloor=-4$, because $-4\le -3.5<-3$. Rounding toward zero would give $-3$.

## Division with remainder

Dividing $17$ by $5$ gives quotient $\lfloor 17/5\rfloor=3$ and remainder $17-5\cdot 3=2$, so $17=5\cdot 3+2$ with $0\le 2<5$. The remainder always lies in $[0,5)$ when the quotient is the floor of the exact ratio.

The paper's division machine computes exactly this. <cite data-source="paper">where q = ⌊a/b⌋</cite> The letters $q$, $a$ and $b$ in that quotation are the paper's own, for the quotient, dividend and divisor; they do not keep the meanings they have on other pages of this wiki. The paper's square-root machine likewise returns the floor of a square root: <cite data-source="paper">returns binn (⌊ a⌋)</cite>

## Using an approximate quotient

An approximate quotient is corrected to the exact floor with one exact integer computation. The paper uses this step: <cite data-source="paper">Its floor q0 differs from q = ⌊a/b⌋ by at most one.</cite> The remainder $r_0=a-bq_0$ is then computed exactly, and $q_0$ is decremented or incremented by one when $r_0$ falls outside $[0,b)$.

Worked example with $a=17$ and $b=5$. Suppose an approximation gives $q_0=4$. Then $r_0=17-5\cdot 4=-3$ is negative, so decrement to $q_0=3$ and add $b$ back to the remainder, giving $r_0=-3+5=2$. The floor is $3$, as before.

## Digits and carries

Splitting an integer into digits is repeated floor division. In base 10, $\lfloor 1234/10\rfloor=123$ and the last digit is $1234-10\cdot 123=4$. Repeating on $123$ gives the next digit, and so on.

A carry is the same operation applied to a coefficient. A coefficient $37$ in one place contributes $\lfloor 37/10\rfloor=3$ to the next place and leaves $37-10\cdot 3=7$ in its own place. Carry propagation applies this rule to every place in turn.
