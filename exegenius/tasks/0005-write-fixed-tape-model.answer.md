A fixed-tape machine is a multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length. It is the model in which the integer multiplication result of this argument is proved, so the later bounds on multiplication cost are claims about such machines.

The restriction matters because a standard multitape machine may use more tapes, or a larger alphabet, as its input grows. A fixed-tape machine may not. Its alphabet and tape count are set before any input is read, and one machine must handle inputs of every size. Running time is measured as usual: the worst case, over all inputs of a given size, of the number of steps the machine takes.

The paper's main theorem states the model directly: there is one deterministic machine with <cite data-source="paper">a fixed finite alphabet and a fixed finite number of one-dimensional tapes</cite>, and it computes the exact product of two integers for every input size.

The integer product is computed exactly on one fixed-tape machine, the model in which [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md) is proved.
