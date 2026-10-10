A multitape Turing machine in this paper has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. Each tape has its own head. In one step, the machine reads and writes at most one cell on each tape, and moves each head by at most one cell.

The model is the standard one for measuring bit complexity: the running time counts elementary bit-level steps on the tapes, rather than arithmetic operations on machine words. The paper's main result is stated as a bound on this quantity, and the algorithm is intended to establish a bit-complexity bound.

The machine may have tracks, which are fixed rows of extra data stored on each tape alongside the main data. Using a fixed number of tracks, or a fixed number of work tapes, changes the time only by a constant factor, so these choices do not affect the bounds that matter here.

The paper distinguishes two kinds of rearrangement of data on tape. Moving one digit of a fixed radix to another position takes a bounded number of scans of the data. Interchanging two fields whose numbers of digits grow is much more expensive, and it is the subject of the [address-field interchange](address-interchange.md) procedure.

For example, consider an array of volume $V$, the number of stored data bits. Moving one specified radix-$q$ digit to another position, while preserving the order of the other positions, takes $O(V)$ steps. This is a linear-time operation on the whole array, which is the kind of cost the paper's later bounds are built from.

Counting also has a cost in this model. A binary counter over $L$ consecutive counts costs $O(L + w)$ time, where $w$ is its width, because the low-order positions change more often than the high-order ones.
