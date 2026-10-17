# exegenius task 0084-write-array-frames

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## This page

Concept: Frames on wire arrays
Gloss: Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter.

## This page in the argument

The step: If every scalar wire value is replaced by an array over a finite address set $\Omega$ and every gate acts pointwise, then assigning an invertible operator $D_v$ (a frame) to each source, gate and sink, with the same $D_v$ on all incidences of a gate, makes the network apply $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$: a route from input role $w$ to output role $\rho(w)$ applies only the endpoint frames $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ and its scalar sign.
How: Maintain the invariant 'stored array = $D_v$ applied to the logical array' at every vertex, checking it at sources by definition, along edges by applying $D_vD_u^{-1}$, and across gates by linearity.
Why: A linear pointwise gate commutes with any operator applied identically to all its input arrays, so the frames telescope along each route and only the two endpoint frames matter, leaving the intermediate frames free to be chosen so that each edge change is cheap. (the sources say so: "intermediate frames can then be chosen to make each edge change inexpensive." (paper))

Its sub-steps, in order:

- At each source, gate and sink $v$ an invertible operator $D_v$ (the frame) on $R^\Omega$ is assigned; an edge from $u$ to $v$ applies $D_vD_u^{-1}$.
- The invariant 'the stored array equals $D_v$ applied to the logical array' holds at the sources by definition and along each edge.
- At a gate all incident arrays have the common frame $D_v$, and $R$-linearity makes $G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$, so the invariant continues to the sinks.
- The implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$.
- For a signed role permutation sending $w$ to $\rho(w)$ with sign $\varepsilon_w$, the route applies $\varepsilon_w D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its input array, for every role including scratch roles.

It serves these steps, from the main result down:

- A single deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model.; how: Build two power-saving tape procedures (chunk interchange and simultaneous butterfly layer) from fixed finite linear networks; use them to accelerate the synthetic polynomial transforms and ring convolution; use Gaussian resampling with retained permutations and chirps to reduce the prime-length cyclic convolution of the radix-digit coefficients to those power-of-two transforms; assemble the exact product with a proof that the error is below $1/2$; and total the cost to show a power of $\log n$ is saved. (on [Power-saving integer multiplication](main-result.md))
- Both tape primitives (the interchange of two address chunks of $u$ digits and the simultaneous butterfly layer on up to $d$ axes) cost the volume times a power below one of their width, because a call at parameter $mf$ makes $s$ calls at parameter $f$ on streams of volume $V/W$ with $s<Wm$, so the cost per unit volume grows by $s/W<m$ per factor $m$ of the parameter.; how: Build a fixed finite linear network of $W$ wires that exchanges two banks and restores all scratch values, make the representation of each wire's array vary along the network through frames so that an edge costs one smaller call per unit of rank, show the total rank $s$ is below $Wm$, fix an exponent, and solve the recurrence in the bit variant (interchange) and the complex variant (butterfly layer). (on [Recursive power saving](rank-recurrence.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1.2.1, S1.2.2, S1.2.3, S1.2.4, S1.2.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1.2.1**: At each source, gate and sink $v$ an invertible operator $D_v$ (the frame) on $R^\Omega$ is assigned; an edge from $u$ to $v$ applies $D_vD_u^{-1}$.
Source: "At each source, gate and sink $v$, assign an invertible $R$-linear operator" (paper)
> At each source, gate and sink $v$, assign an invertible $R$-linear operator $D_v$ on $R^\Omega$, called its \emph{frame}. A frame acts on the values indexed by addresses within one wire's array and may mix them; a gate instead combines wire values at each fixed address. All incoming and outgoing incidences of one gate use the same $D_v$. On an edge from $u$ to $v$, apply $D_vD_u^{-1}$ to that wire's array. Define the operators on all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals

**S1.2.2**: The invariant 'the stored array equals $D_v$ applied to the logical array' holds at the sources by definition and along each edge.
Source: "At a vertex $v$, the invariant is that the stored array equals $D_v$ applied" (paper)
> ce, gate and sink $v$, assign an invertible $R$-linear operator $D_v$ on $R^\Omega$, called its \emph{frame}. A frame acts on the values indexed by addresses within one wire's array and may mix them; a gate instead combines wire values at each fixed address. All incoming and outgoing incidences of one gate use the same $D_v$. On an edge from $u$ to $v$, apply $D_vD_u^{-1}$ to that wire's array. Define the operators on all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with

**S1.2.3**: At a gate all incident arrays have the common frame $D_v$, and $R$-linearity makes $G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$, so the invariant continues to the sinks.
Source: "Thus the common frame commutes with the pointwise gate, and" (paper)
> ne the operators on all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.

**S1.2.4**: The implemented operator is $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$.
Source: "D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}." (paper)
> w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.

**S1.2.5**: For a signed role permutation sending $w$ to $\rho(w)$ with sign $\varepsilon_w$, the route applies $\varepsilon_w D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its input array, for every role including scratch roles.
Source: "\varepsilon_wD_{\mathrm{sink}(\rho(w))}" (paper)
> t holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.

## Symbols already bound on earlier pages

The symbols in the names of the concepts the reader knows are listed with those concepts above.

- $y$ (ring variable), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $r$ (record length), bound on [Polynomial ring modulo y^r + 1](ring-y.md): The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent), bound on [Schönhage–Strassen optimality conjecture](conjecture.md): A fixed positive constant by which the exponent of the logarithm in the running time is lowered.
- $p$ (fractional bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of operations applied since the layer began.
- $\Delta$ (extra reserved bits), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The number of extra bits reserved, at least the number of operations charged to the layer.
- $Q_p$ (truncation), bound on [Fixed-point Gaussian dyadic records](fixed-point.md): The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $h$ (ground-set size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of wires in each data bank.
- $m$ (label-space dimension), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The dimension of the label space used later.
- $I$ (invocation count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of invocations.
- $z_{\rm b}$ (bit neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the bit construction.
- $z_{\rm c}$ (complex neighbour count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of neighbours of a fixed triple in the complex construction.
- $c_{\rm b}$ (bit central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on [Linear exchange network with restored scratch wires](exchange-network.md): The total number of wires in the complex network.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Linear exchange network with restored scratch wires](exchange-network.md): A fixed network of linear gates on wires holding values that swaps two banks with a prescribed sign while undoing the effect of arbitrary initial scratch values, built from three-element subsets.
  Shown as: Frames on wire arrays *<predicate>* Linear exchange network with restored scratch wires

## Pages that build on this one

- Nested subspace labels and rank deficit: Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.

## Other pages you may link to

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Evidence from the sources, with the paragraph around each quote

- "We call $D_v$ its frame: the stored" (paper)

  > The representation of a role's array may change along the network. At a source, gate, or sink $v$, choose an invertible linear operator $D_v$ on the space of arrays indexed by the common address set. We call $D_v$ its frame: the stored array is $D_vg$ when the logical array is $g$. All incidences of one gate have the same frame. Along an edge from $u$ to $v$, the operator $D_vD_u^{-1}$ changes the stored array from $D_ug$ to $D_vg$. At a pointwise linear gate $G$, the common frame commutes with the gate: \[ G(D_vg_1,\ldots,D_vg_t)=D_vG(g_1,\ldots,g_t). \] The supplied input needs no preliminary change of frame: its logical interpretation is defined by applying the inverse input frame. Thus the intermediate frames cancel, and a route from input role $w$ to output role $\rho(w)$ applies $D_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$, together with its prescribed scalar sign. Undoing the role exchange and those signs leaves the endpoint operator on every role array, including the roles that carried auxiliary scalar values.

- "Thus the common frame commutes with the pointwise gate" (paper)

  > efine the operators on all input and output roles by \[ D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)},\qquad D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}. \] For a supplied physical input $f$, define its logical interpretation to be $g=D_{\rm in}^{-1}f$; this definition requires no physical preprocessing. At a vertex $v$, the invariant is that the stored array equals $D_v$ applied to the logical array there. It holds at the sources by definition. On an edge whose logical array is $\varphi$, the edge operator changes $D_u\varphi$ to $D_v\varphi$. At a gate with logical input arrays $\varphi_j$, $R$-linearity gives $\sum_j c_jD_v\varphi_j=D_v(\sum_j c_j\varphi_j)$ for each output combination, with $c_j\in R$. Thus the common frame commutes with the pointwise gate, and the invariant continues to the sinks. The implemented operator is therefore \begin{equation} D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}. \label{eq:common-frame-identity} \end{equation} In particular, if the scalar network is a signed role permutation that sends input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))} D_{\mathrm{source}(w)}^{-1}$ to its input array. All roles, including the auxiliary roles, enter this identity. Once the scalar routing is fixed, the endpoint frames determine the array operator on each route; the intermediate frames can then be chosen to make each edge change inexpensive.


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Say what $t$ denotes where it is first used (for a size or count, what it counts): "$G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$" (The gate formula uses t as the number of inputs of the gate without saying so; later the page uses t for a sink (D_t), a different meaning that also comes after this first use.)
- Say what $s$ denotes where it is first used: the page uses it before saying so in "On a route from a source $s$ through gates $a$ and $b$"

## Previous version (revise it)

It has 350 words, not counting mathematics and citations. Fix the problems by restructuring rather than appending: submit rejects a rewrite over 437 words. Pages that grow with every repair stop being self-contained explanations of one concept. Submit also rejects letters in the mathematics that the previous version did not use, unless the symbols they make are bound: a new formula brings new symbols for the reader to learn.

Frames let a network of scalar gates act on whole arrays stored differently on different wires, so that only the representations at the two ends of a route matter. They extend the [linear exchange network with restored scratch wires](exchange-network.md) from scalars to arrays while keeping each edge cheap.

Let $R$ be the ring of scalars carried by the wires, and let $\Omega$ be a finite set of addresses indexing every array. Replace each scalar wire value by an array in $R^\Omega$ and apply every gate pointwise, at each address separately. Write $\mathsf S_\Omega$ for the resulting network acting on all the wire arrays together.

At each source, gate and sink $v$, assign an invertible $R$-linear operator $D_v$ on $R^\Omega$, called its frame. A frame may mix entries of one array across addresses, whereas a gate combines different wires at one fixed address. All incidences of a gate use the same $D_v$, and an edge from $u$ to $v$ applies $D_vD_u^{-1}$ to the array it carries.

The invariant is that the stored array at $v$ equals $D_v$ applied to the logical array. It holds at the sources by definition: with $D_{\rm in}=\bigoplus_w D_{\mathrm{source}(w)}$ stacking the source frames over the input roles $w$, a physical input $f$ is interpreted as the logical input $g=D_{\rm in}^{-1}f$, which needs no preprocessing. It continues along an edge: if the logical array is $\varphi$, the stored array $D_u\varphi$ becomes $D_vD_u^{-1}D_u\varphi=D_v\varphi$.

At a gate, every incoming array has the common frame $D_v$, and a gate output combines its logical inputs $\varphi_j$ with coefficients $c_j\in R$. Because $D_v$ is $R$-linear, $\sum_j c_jD_v\varphi_j=D_v\bigl(\sum_j c_j\varphi_j\bigr)$. So $G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$ for a gate $G$: the gate applied to stored arrays gives the stored form of the logical output, and the invariant continues to the sinks <cite data-source="paper">the common frame commutes with the pointwise gate</cite>.

With $D_{\rm out}=\bigoplus_w D_{\mathrm{sink}(w)}$, the implemented operator is therefore
$$D_{\rm out}\,\mathsf S_\Omega\,D_{\rm in}^{-1}.$$

On a route from a source $s$ through gates $a$ and $b$ to a sink $t$, the edges apply $D_aD_s^{-1}$, $D_bD_a^{-1}$ and $D_tD_b^{-1}$, whose product is $D_tD_s^{-1}$: the intermediate frames telescope away. So if the scalar network is a signed role permutation sending input role $w$ to output role $\rho(w)$ with scalar sign $\varepsilon_w$, that route applies $\varepsilon_wD_{\mathrm{sink}(\rho(w))}D_{\mathrm{source}(w)}^{-1}$ to its input array. This holds for every role, scratch roles included.

The endpoint frames fix the operator on each route, so the <cite data-source="paper">intermediate frames can then be chosen to make each edge change inexpensive.</cite>

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0084-write-array-frames.answer.md` and the JSON to `exegenius/tasks/0084-write-array-frames.answer.json`, then run `exegenius submit 0084-write-array-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0084-write-array-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
