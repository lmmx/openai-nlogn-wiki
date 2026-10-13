The fixed-tape machine is the cost model in which the paper measures its multiplication algorithm. Its running time is set by how data moves along the tapes, so the operations to minimize are scans, shifts and permutations of data.

A fixed-tape machine has one fixed finite alphabet and a fixed number of one-dimensional tapes, each with its own head. <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite> A step therefore touches only a bounded amount of data, and moving a value across many cells costs at least as many steps as the distance covered.

<cite data-source="paper">Fixed tracks and finitely many work tapes change time by a fixed factor.</cite> So adding them does not change asymptotic bounds, and the model's costs are not sensitive to such choices.

A stream is a sequence of cells that one head reads or writes in order during a scan. A scan is one sweep of a head along a tape. <cite data-source="paper">Every scan includes its counters and the return of its tape heads.</cite> Its cost is therefore proportional to the length of the stream it handles, plus the trip back.

The paper separates two kinds of operation. <cite data-source="paper">We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow.</cite> Moving one digit is cheap because a fixed number of scans suffices. Interchanging two fields with growing digit counts is expensive, because whole streams must be shifted and reordered over long distances. The paper realizes that interchange by computing XOR combinations of intermediate data streams.

For example, shifting a stream one cell to the right on a single tape takes one pass. The machine's finite state remembers the one symbol it has just read, writes that symbol one cell further on, and continues. Only a constant amount of information is carried from cell to cell, which is why a finite state suffices.
