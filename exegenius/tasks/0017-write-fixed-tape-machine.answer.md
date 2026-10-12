The fixed-tape machine model is a Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, so neither grows with the input. Its cost is a count of steps of such a machine.

The restriction that matters is on movement. <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite> So a value moved from one end of a tape to the other takes one step per cell crossed.

Fixed tracks, meaning several parallel rows of symbols stored in each cell, and finitely many work tapes are harmless for this count. <cite data-source="paper">Fixed tracks and finitely many work tapes change time by a fixed factor.</cite>

A scan is one pass of a head across a stretch of tape. A field is a block of consecutive digits holding one number. Moving one digit in a fixed radix takes a bounded number of scans, because a digit is one symbol from a fixed alphabet, so the finite control can hold it while the head makes a fixed number of passes. Interchanging fields whose digit counts grow needs more. The control cannot hold a whole field, so each digit must be carried past the other field, and the number of passes grows with the field lengths.

Scans are the unit of cost because a scan takes about as many steps as the cells it crosses, since each step moves a head one cell. Counting scans therefore counts steps up to a constant factor.
