A payload is the record data stored at one address of an array, as distinct from the address that locates that record. It matters because the packed selected-bit addition step moves records between addresses, and its time bound must hold whatever payloads the records carry.

An array is a finite collection of records, each stored at an address. An address is a binary string, such as $01$, saying where its record sits. The payload is what the record carries.

Take an array with four records at the two-bit addresses $00$, $01$, $10$ and $11$, carrying the payloads $5$, $0$, $3$ and $1$. Each payload is the integer value of that record's binary data. Swapping the two address bits sends the record at $01$ to $10$ and the record at $10$ to $01$. Afterwards address $01$ holds payload $3$ and address $10$ holds payload $0$: the payloads moved with their records, and only the addresses changed.

The step's time bound is $O(V(L^{\tau}+1))$, where $V$ is the number of stored bits in the stream, $L$ is the width of an address chunk (a block of consecutive address bits), and $\tau$ is a fixed exponent with $0<\tau<1$. Under the lemma's asymptotic hypotheses, the paper states the bound as <cite data-source="paper">O(V (Lτ + 1)), uniformly over the permitted lengths and payloads in the fixed family.</cite>

The paper states this bound with the payload left arbitrary. <cite data-source="paper">The correction depends only on addresses</cite>, so the time bound is worst-case <cite data-source="paper">over all payloads.</cite>

A payload can be very small: <cite data-source="paper">The general address-swap subroutine also covers one-bit payloads</cite>, so the swap cost must stay bounded even when each record carries a single bit. The correction work therefore cannot depend on how much data a record carries; it is determined by the addresses the step touches.
