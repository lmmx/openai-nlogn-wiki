# exegenius task 0672-support-bit-network

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

Claim: It is the building block of the tape step that interchanges two equal address chunks:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We use the bit network to interchange two equal address chunks on tape."

Paragraph:

> The bit network is a fixed linear network whose wires carry bits. It exchanges two banks of bits and leaves its scratch wires as they started. It is the building block of the tape step that interchanges two equal address chunks:

### 2

Claim: The paper's first tape procedure interchanges two blocks of $u$ bits, the fields of the address:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The first procedure interchanges two disjoint contiguous address fields of u bits"

Paragraph:

> An address is a bit string, and an address chunk is a block of adjacent address bits. The paper's first tape procedure interchanges two blocks of $u$ bits, the fields of the address:, so each entry moves to the address with its two fields swapped.

### 3

Claim: It

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "uses only pointwise XOR gates"

Paragraph:

> The bit network is a binary instance of [linear networks and frames](linear-network-frames.md), since its wires carry scalars of $\mathbb{F}_2$, the field with two elements in which addition is exclusive or and multiplication is AND. It, so each gate replaces the bits on some wires by sums of bits on other wires. Over $\mathbb{F}_2$ subtraction is the same as addition, so the signs in the paper's general construction disappear.

### 4

Claim: The paper's count reads:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2."

Paragraph:

> The initial scratch values enter $Y$ in rows 0 and 1 and again in rows 4 and 5. The two copies cancel because $1+1=0$ in $\mathbb{F}_2$, whatever the scratch wires held. What remains is the contribution of $W$. The bit $W_{\sigma'}$ reaches $Y_\sigma$ through the side wire $\zeta_{\sigma\sigma'}$ when $\sigma'$ is a neighbour of $\sigma$, and through $J_\upsilon$ for each $\upsilon\in\sigma\cap\sigma'$. The paper's count reads: Here $S$ is $\sigma$ and $T$ is $\sigma'$. Adding the side route, the coefficient of $W_{\sigma'}$ in the change to $Y_\sigma$ is $|\sigma\cap\sigma'|$ plus one if $\sigma'$ is a neighbour, taken mod 2. This is $0$ when $\sigma'\neq\sigma$: for neighbours $|\sigma\cap\sigma'|=1$ and the two routes give $1+1=0$, and otherwise $|\sigma\cap\sigma'|\in\{0,2\}$. When $\sigma'=\sigma$ the three central routes give $3\equiv 1$. So a forward invocation sets $Y_\sigma\leftarrow Y_\sigma+W_\sigma$ for every triple. The paper states this as

### 5

Claim: The paper states this as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a forward invocation changes yS to yS + xS and leaves every other value unchanged."

Paragraph:

> The initial scratch values enter $Y$ in rows 0 and 1 and again in rows 4 and 5. The two copies cancel because $1+1=0$ in $\mathbb{F}_2$, whatever the scratch wires held. What remains is the contribution of $W$. The bit $W_{\sigma'}$ reaches $Y_\sigma$ through the side wire $\zeta_{\sigma\sigma'}$ when $\sigma'$ is a neighbour of $\sigma$, and through $J_\upsilon$ for each $\upsilon\in\sigma\cap\sigma'$. The paper's count reads: Here $S$ is $\sigma$ and $T$ is $\sigma'$. Adding the side route, the coefficient of $W_{\sigma'}$ in the change to $Y_\sigma$ is $|\sigma\cap\sigma'|$ plus one if $\sigma'$ is a neighbour, taken mod 2. This is $0$ when $\sigma'\neq\sigma$: for neighbours $|\sigma\cap\sigma'|=1$ and the two routes give $1+1=0$, and otherwise $|\sigma\cap\sigma'|\in\{0,2\}$. When $\sigma'=\sigma$ the three central routes give $3\equiv 1$. So a forward invocation sets $Y_\sigma\leftarrow Y_\sigma+W_\sigma$ for every triple. The paper states this as

### 6

Claim: Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The inverse schedule with logical source Y and target X effects X ← X − Y"

Paragraph:

> The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $W$. Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes. Starting from $(W,Y)$, the three invocations give $(W,Y+W)$, then $(Y,Y+W)$, then $(Y,W)$. In the second step $W\leftarrow W+(Y+W)=Y$. In the third $Y\leftarrow(Y+W)+Y=W$. So the banks are exchanged and the scratch wires are unchanged. Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result: and $Y$, and the same invocations Because the scratch values may start arbitrary, the exchange must hold for any of them:

### 7

Claim: Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In the bit construction this is the permutation exchanging Xa"

Paragraph:

> The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $W$. Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes. Starting from $(W,Y)$, the three invocations give $(W,Y+W)$, then $(Y,Y+W)$, then $(Y,W)$. In the second step $W\leftarrow W+(Y+W)=Y$. In the third $Y\leftarrow(Y+W)+Y=W$. So the banks are exchanged and the scratch wires are unchanged. Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result: and $Y$, and the same invocations Because the scratch values may start arbitrary, the exchange must hold for any of them:

### 8

Claim: and $Y$, and the same invocations

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "restores every auxiliary value."

Paragraph:

> The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $W$. Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes. Starting from $(W,Y)$, the three invocations give $(W,Y+W)$, then $(Y,Y+W)$, then $(Y,W)$. In the second step $W\leftarrow W+(Y+W)=Y$. In the third $Y\leftarrow(Y+W)+Y=W$. So the banks are exchanged and the scratch wires are unchanged. Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result: and $Y$, and the same invocations Because the scratch values may start arbitrary, the exchange must hold for any of them:

### 9

Claim: Because the scratch values may start arbitrary, the exchange must hold for any of them:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The final permutation is exact for arbitrary initial auxiliary values."

Paragraph:

> The exchange uses three invocations: forward, inverse, forward. The inverse is the same eight-row schedule with the roles of the banks swapped, so its gates read $Y$ and update $W$. Over $\mathbb{F}_2$ it sets $W\leftarrow W+Y$; the paper writes. Starting from $(W,Y)$, the three invocations give $(W,Y+W)$, then $(Y,Y+W)$, then $(Y,W)$. In the second step $W\leftarrow W+(Y+W)=Y$. In the third $Y\leftarrow(Y+W)+Y=W$. So the banks are exchanged and the scratch wires are unchanged. Lemma 5 of the paper, in *Integer multiplication below n log n* (OpenAI, 2026), states this result: and $Y$, and the same invocations Because the scratch values may start arbitrary, the exchange must hold for any of them:

### 10

Claim: On tape, binary changes of basis are carried out by moving whole address chunks:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We implement those changes by moving whole address chunks."

Paragraph:

> On tape, binary changes of basis are carried out by moving whole address chunks: The bit network performs the chunk interchanges that implement a [binary change of basis](binary-change-of-basis.md) on tape.

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

Write the answer to `exegenius/tasks/0672-support-bit-network.answer.json`, then run `exegenius submit 0672-support-bit-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
