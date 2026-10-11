# exegenius task 0704-support-address-interchange

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check whether each quotation on a page of an explanatory wiki supports the claim it is attached to. Writers back claims taken from the sources with a quotation copied from them; a quotation can exist in the source and still not support what it is attached to.

- Judge each claim against its quotation alone, not against what you know or what the source may say elsewhere.
- `supported`: the quotation states the claim or directly implies it.
- `partial`: the quotation supports part of the claim, or a weaker version of it.
- `unsupported`: the quotation does not address what the claim asserts.
- `contradicted`: the quotation says something incompatible with the claim.
- For every label but `supported`, say in one line what is missing or wrong.
- Label every quotation listed, each once.

## Quotations

### 1

Claim: The paper states:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The first procedure interchanges two disjoint contiguous address fields of u bits in an array"

Paragraph:

> The paper states:. Here $u$ is the field width and $V$ the stored bit volume. The letter $\tau$ changes meaning here: it is this fixed exponent, below 1.

### 2

Claim: The method uses XOR combinations:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Our address procedure forms XOR combinations of intermediate data"

Paragraph:

> The method uses XOR combinations:, although its final effect is a permutation. Let $x$ and $y$ be the two fields, each read as a block of bits at matching positions; these letters change meaning here. Let $\oplus$ be exclusive or (XOR), addition modulo 2. Three XOR updates swap the fields:
> $$(x,y)\to(x,\;x\oplus y)\to(y,\;x\oplus y)\to(y,\;x).$$
> The second update works because $x\oplus(x\oplus y)=y$, a block XORed with itself being zero. Each update is its own inverse, so their composition is a permutation. For $x=10$, $y=01$ the chain is $(10,01)\to(10,11)\to(01,11)\to(01,10)$. With signs, the paper writes: Over bits the signs vanish.

### 3

Claim: With signs, the paper writes:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(x, y), the three stages give (x, y + x), then (−y, y + x), then (−y, x)."

Paragraph:

> The method uses XOR combinations:, although its final effect is a permutation. Let $x$ and $y$ be the two fields, each read as a block of bits at matching positions; these letters change meaning here. Let $\oplus$ be exclusive or (XOR), addition modulo 2. Three XOR updates swap the fields:
> $$(x,y)\to(x,\;x\oplus y)\to(y,\;x\oplus y)\to(y,\;x).$$
> The second update works because $x\oplus(x\oplus y)=y$, a block XORed with itself being zero. Each update is its own inverse, so their composition is a permutation. For $x=10$, $y=01$ the chain is $(10,01)\to(10,11)\to(01,11)\to(01,10)$. With signs, the paper writes: Over bits the signs vanish.

### 4

Claim: Its gates act pointwise:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Execute each circuit gate pointwise at matching addresses of its role streams."

Paragraph:

> The interchange is carried out by a [Linear networks and frames](linear-network-frames.md) network. Its gates act pointwise: The network has scratch wires with arbitrary starting values. Its schedule subtracts their effect, then adds the same terms back, so they cancel from the net change, which depends only on $x$. The network thus [restores its scratch storage](scratch-storage.md) to its starting contents, whatever they were.

### 5

Claim: The base case is one digit:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For k = 0 apply the single-digit operation of Lemma 3."

Paragraph:

> The cost comes from a recursion on width. Let $m\ge 2$ be a fixed integer, the number of pieces each field is cut into; this letter changes meaning here. Take $u=m^k$, so the recursion has $k$ levels, where $k=\log_m u$ counts them; this letter changes meaning here too. The base case is one digit:

### 6

Claim: Each call works on one stream, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "each contains V /W bits."

Paragraph:

> Let $s$ be the number of smaller calls one call makes; this letter changes meaning here. An edge whose matrix has [matrix rank](matrix-rank.md) $r$ needs $r$ smaller interchanges. Each call works on one stream, and The counting gives So $s/W<m$.

### 7

Claim: The counting gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that the total number s of smaller calls satisfies s < W m."

Paragraph:

> Let $s$ be the number of smaller calls one call makes; this letter changes meaning here. An edge whose matrix has [matrix rank](matrix-rank.md) $r$ needs $r$ smaller interchanges. Each call works on one stream, and The counting gives So $s/W<m$.

### 8

Claim: A call of volume $V$ spends $CV$ on its own work, with $C$ a constant, since

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "triangular operations have total cost O(V ) because their number is fixed."

Paragraph:

> Let $\vartheta_j$ be the time per unit volume of a call on width $m^j$, the level $j$; the letter $j$ changes meaning here. A call of volume $V$ spends $CV$ on its own work, with $C$ a constant, since Its $s$ children each have volume $V/W$. So $\vartheta_0=O(1)$ and
> $$\vartheta_j\le C+\frac{s}{W}\,\vartheta_{j-1}.$$
> The exponent is chosen as in the paper: Such $\tau$ exists because $s/W<m$ and $m^{\tau}\to m$ as $\tau\to 1$.

### 9

Claim: So $\vartheta_0=O(1)$ and
$$\vartheta_j\le C+\frac{s}{W}\,\vartheta_{j-1}.$$
The exponent is chosen as in the paper:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Choose a rational number τ ∈ (0, 1) with s/W < mτ ."

Paragraph:

> Let $\vartheta_j$ be the time per unit volume of a call on width $m^j$, the level $j$; the letter $j$ changes meaning here. A call of volume $V$ spends $CV$ on its own work, with $C$ a constant, since Its $s$ children each have volume $V/W$. So $\vartheta_0=O(1)$ and
> $$\vartheta_j\le C+\frac{s}{W}\,\vartheta_{j-1}.$$
> The exponent is chosen as in the paper: Such $\tau$ exists because $s/W<m$ and $m^{\tau}\to m$ as $\tau\to 1$.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Label": {
      "additionalProperties": false,
      "properties": {
        "label": {
          "$ref": "#/$defs/Verdict"
        },
        "mark": {
          "description": "Number of the quotation, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "reason": {
          "description": "What is missing or wrong; may be empty for `supported`.",
          "type": "string"
        }
      },
      "required": [
        "mark",
        "label",
        "reason"
      ],
      "type": "object"
    },
    "Verdict": {
      "oneOf": [
        {
          "const": "supported",
          "description": "The quotation states the claim or directly implies it.",
          "type": "string"
        },
        {
          "const": "partial",
          "description": "The quotation supports part of the claim, or a weaker version.",
          "type": "string"
        },
        {
          "const": "unsupported",
          "description": "The quotation does not address what the claim asserts.",
          "type": "string"
        },
        {
          "const": "contradicted",
          "description": "The quotation says something incompatible with the claim.",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "properties": {
    "labels": {
      "items": {
        "$ref": "#/$defs/Label"
      },
      "type": "array"
    }
  },
  "required": [
    "labels"
  ],
  "title": "SupportAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0704-support-address-interchange.answer.json`, then run `exegenius submit 0704-support-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
