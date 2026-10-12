The fixed-tape machine model is a Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, so neither the alphabet nor the number of tapes grows with the input. Its cost is a count of steps of a concrete machine of this kind, which is what the page's later bounds are stated in.

The restriction that matters is on movement. In each step a head moves at most one cell, so moving a value from one end of a tape to the other takes one step per cell crossed. <cite data-source="paper">A step reads and writes at most one cell on each tape and moves each head by at most one cell.</cite>

Fixed tracks and finitely many work tapes are harmless for this count. They change the running time only by a constant factor, so the number of steps is fixed up to a constant. <cite data-source="paper">Fixed tracks and finitely many work tapes change time by a fixed factor.</cite>

Later pages count the cost of rearranging data in this model. Moving one digit in a fixed radix takes a bounded number of scans, whereas interchanging fields whose numbers of digits grow needs more work, so the model's scans are the unit of cost.
