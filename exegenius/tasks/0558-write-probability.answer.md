Probability is a number between $0$ and $1$ assigned to each event of an experiment, the measure of how likely the event is. The argument relies on it where it states the bounds for the rank-saving recursion and for exact coefficient recovery, and the notion of independence of events is built on it.

## Outcomes and events

Fix a finite set $\Xi$, the sample space, whose elements are all the possible outcomes of an experiment. An event is a subset $\mathcal{A} \subseteq \Xi$, the set of outcomes in which the event occurs. Events are written $\mathcal{A}$, $\mathcal{B}$, and so on, and each one is a subset of $\Xi$.

A probability assigns to each event a real number $\Pr(\mathcal{A})$ satisfying three rules:

1. Nonnegativity: $\Pr(\mathcal{A}) \ge 0$ for every event $\mathcal{A}$.
2. Certainty: $\Pr(\Xi) = 1$, so the certain event, which contains every outcome, has probability $1$.
3. Additivity: if two events $\mathcal{A}$ and $\mathcal{B}$ are disjoint, meaning $\mathcal{A}\cap\mathcal{B}=\varnothing$ (they share no outcome), then
$$\Pr(\mathcal{A}\cup\mathcal{B}) = \Pr(\mathcal{A}) + \Pr(\mathcal{B}).$$

The complement of $\mathcal{A}$ is $\Xi\setminus\mathcal{A}$, the outcomes not in $\mathcal{A}$. Since $\mathcal{A}$ and $\Xi\setminus\mathcal{A}$ are disjoint with union $\Xi$, additivity and certainty give $\Pr(\mathcal{A}) + \Pr(\Xi\setminus\mathcal{A}) = 1$, so $\Pr(\Xi\setminus\mathcal{A}) = 1-\Pr(\mathcal{A})$.

## Worked example

Flip a coin twice, and take $\Xi=\{HH,HT,TH,TT\}$, where $H$ is heads and $T$ is tails. Give each outcome probability $1/4$. Let $\mathcal{A}$ be the event "at least one head", so $\mathcal{A}=\{HH,HT,TH\}$. Splitting $\mathcal{A}$ into three disjoint single outcomes and applying additivity three times gives $\Pr(\mathcal{A}) = \tfrac14+\tfrac14+\tfrac14 = \tfrac34$. The complement $\Xi\setminus\mathcal{A}=\{TT\}$ has probability $\tfrac14 = 1-\tfrac34$, as the complement rule says.

Two events $\mathcal{A}$ and $\mathcal{B}$ are independent when $\Pr(\mathcal{A}\cap\mathcal{B}) = \Pr(\mathcal{A})\,\Pr(\mathcal{B})$, which is the definition that the independence page builds on this measure.
