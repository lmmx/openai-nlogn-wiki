A fixed-tape machine is the cost model in which the paper states its integer multiplication bound. Its cost is set by how data moves along the tapes, so the operations to minimize are scans, shifts and permutations of data.

The machine has one fixed finite alphabet and a fixed number of one-dimensional tapes, each with its own head. <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite> Moving a value across many cells therefore takes at least as many steps as the distance covered.

<cite data-source="paper">Fixed tracks and finitely many work tapes change time by a fixed factor.</cite> So adding them does not change asymptotic bounds: each step of the original machine becomes a bounded number of steps on the enlarged one.

A stream is a sequence of cells that one head reads or writes in order during a scan. <cite data-source="paper">Every scan includes its counters and the return of its tape heads.</cite>

A field is a contiguous block of digit positions within each address, where an address is the position of an entry in the ordered stream. Interchanging two equal-width fields swaps the contents of the two blocks in every address.

<cite data-source="paper">We distinguish moving one digit in a fixed radix, which needs a bounded number of scans, from interchanging fields whose numbers of digits grow.</cite> Moving one digit is cheap because a radix digit is a fixed-size block of cells, which the finite state can hold. Shifting a stretch of cells by one digit-width is one pass: at each cell the head writes the digit it holds and reads the next block into its state. One more scan returns the heads.

Interchanging whole fields needs blocks to cross long distances, and the paper instead <cite data-source="paper">forms XOR combinations of intermediate data</cite>. The basic identity is that two values can be exchanged by three XORs: replace the first by its XOR with the second, then the second by its XOR with the new first, then the first by its XOR with the new second. Applied cell by cell to two equal-width streams, three passes exchange two fields with no temporary copy.
