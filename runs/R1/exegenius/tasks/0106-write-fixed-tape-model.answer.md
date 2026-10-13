A fixed-tape machine is the cost model in which the paper states its integer multiplication bound. Its cost is set by how data moves along the tapes, so the operations to minimize are scans, shifts and permutations of data.

The machine has <cite data-source="paper">one fixed finite alphabet and one fixed finite number of one-dimensional tapes</cite>, each with its own head. <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite> Moving a value across many cells therefore takes at least as many steps as cells it crosses.

A track is a parallel row of cells on one tape. <cite data-source="paper">Fixed tracks and finitely many work tapes change time by a fixed factor.</cite> A fixed number of tracks is a larger fixed alphabet, and a finite number of extra tapes can be interleaved into one tape, so each step of the original machine becomes a bounded number of steps on the enlarged one. Adding them therefore keeps asymptotic bounds.

A stream is a sequence of cells that one head reads or writes in order during a scan. <cite data-source="paper">Every scan includes its counters and the return of its tape heads.</cite> An address is the position of an entry in an ordered stream. A field is a contiguous block of digit positions within each address, so interchanging two equal-width fields swaps their contents in every address.

<cite data-source="paper">We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow.</cite> A radix digit is a fixed-size block of cells, which the finite control can hold, so moving one digit takes a bounded number of scans.

Interchanging whole fields moves blocks across long distances, which is expensive because each step moves a head by one cell. The paper instead realizes the interchange by <cite data-source="paper">computing XOR combinations of intermediate data streams</cite>.

A simple XOR combination is the standard identity that two values can be exchanged by three XORs. The first value becomes its XOR with the second, then the second becomes its XOR with the new first, then the first becomes its XOR with the new second. No temporary copy of either value is needed.
