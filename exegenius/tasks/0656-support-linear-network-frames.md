# exegenius task 0656-support-linear-network-frames

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

Claim: , and it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "restores every auxiliary value"

Paragraph:

> A *wire* carries one scalar, and a *gate* is a fixed linear map on the wires it touches., the gates that touch it in time order, and its sink. A *bank* is a set of wires with a common index set, so exchanging two banks swaps values at matching indices., and it..

### 2

Claim: A vertex $v$ carries an invertible linear operator $D_v$, its *frame*, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the stored array is Dv g when the logical array is g"

Paragraph:

> Each scalar becomes an array over common addresses, and a *pointwise* gate acts separately at each address. The *logical array* $g$ is the array a wire represents. A vertex $v$ carries an invertible linear operator $D_v$, its *frame*, and. Frames are built from invertible linear operators, as defined in [Linear algebra basics](linear-algebra-basics.md).

### 3

Claim: It replaces the field $H$ by $H+D$ and keeps $D$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H, D over a common residue ring, are updated by (H, D) 7→ (H + D, D)."

Paragraph:

> The bit procedure interchanges two equal address fields. The bit network acts on the two [Address field](address-field.md) blocks of each array, H and K.. It replaces the field $H$ by $H+D$ and keeps $D$, and Over bits, $H+K$ is a pointwise XOR, adding two bits modulo 2 at each address. The bit network, so it realises the shear.

### 4

Claim: The bit network

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "uses only pointwise XOR gates"

Paragraph:

> The bit procedure interchanges two equal address fields. The bit network acts on the two [Address field](address-field.md) blocks of each array, H and K.. It replaces the field $H$ by $H+D$ and keeps $D$, and Over bits, $H+K$ is a pointwise XOR, adding two bits modulo 2 at each address. The bit network, so it realises the shear.

### 5

Claim: Each tape procedure is such a network because

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We construct two fixed linear networks that exchange two banks of values"

Paragraph:

> Each tape procedure is such a network because, and Applying the scalar wiring at every address is legitimate, since a scalar gate. Once the scalar routing is fixed, make each edge change inexpensive.

### 6

Claim: , and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The scalar network already has the required signed exchange."

Paragraph:

> Each tape procedure is such a network because, and Applying the scalar wiring at every address is legitimate, since a scalar gate. Once the scalar routing is fixed, make each edge change inexpensive.

### 7

Claim: Applying the scalar wiring at every address is legitimate, since a scalar gate

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "is then applied pointwise to matching addresses on the roles that it touches"

Paragraph:

> Each tape procedure is such a network because, and Applying the scalar wiring at every address is legitimate, since a scalar gate. Once the scalar routing is fixed, make each edge change inexpensive.

### 8

Claim: Once the scalar routing is fixed,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the intermediate frames can then be chosen to"

Paragraph:

> Each tape procedure is such a network because, and Applying the scalar wiring at every address is legitimate, since a scalar gate. Once the scalar routing is fixed, make each edge change inexpensive.

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

Write the answer to `exegenius/tasks/0656-support-linear-network-frames.answer.json`, then run `exegenius submit 0656-support-linear-network-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.
