A schedule is built from [tape procedures](tape-procedure.md), applied one after another. The paper states its linear constructions this way, as a fixed list of procedures run in a fixed order, and the cancellation of scratch values in its bit construction is one such list.

Write $\Xi_1$, $\Xi_2$ and $\Xi_3$ for three tape procedures. The schedule $(\Xi_1, \Xi_2, \Xi_3)$ applies $\Xi_1$ first, then $\Xi_2$, then $\Xi_3$, so each procedure acts on the contents left by the one before it. The inverse schedule applies the inverse of each procedure in the reverse order, $(\Xi_3^{-1}, \Xi_2^{-1}, \Xi_1^{-1})$. Running a schedule and then its inverse returns the tape to its starting contents, because each inverse undoes the step just before it.

The paper uses an inverse schedule to subtract rather than add: <cite data-source="paper">The inverse schedule with logical source Y and target X effects X ← X − Y</cite>.

Take a toy case in which each procedure swaps the contents of two cells. Let the tape start as $(1, 2, 3)$, and let $\Xi_1$ swap cells 1 and 2, $\Xi_2$ swap cells 2 and 3, and $\Xi_3$ swap cells 1 and 3. Applying the schedule in order gives $(1,2,3) \to (2,1,3) \to (2,3,1) \to (1,3,2)$. A swap is its own inverse, so the inverse schedule applies $\Xi_3$, then $\Xi_2$, then $\Xi_1$ to $(1,3,2)$, giving $(2,3,1) \to (2,1,3) \to (1,2,3)$, the starting contents.
