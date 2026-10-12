# exegenius task 0139-support-address-interchange

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

Claim: Address-field interchange is a tape procedure, a procedure carried out on the tapes of a Turing machine, that swaps two disjoint, contiguous address fields of an array

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The first procedure interchanges two disjoint contiguous address fields of u bits in an array"

Paragraph:

> Address-field interchange is a tape procedure, a procedure carried out on the tapes of a Turing machine, that swaps two disjoint, contiguous address fields of an array. The main result uses it to make the transform layers cheap, where a transform layer is one of the levels of the transform, each of which rearranges and combines the whole array. The cost of the procedure therefore matters.

### 2

Claim: The procedure runs in $O(V u^{\tau})$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its cost is O(V uτ ) for a fixed τ < 1"

Paragraph:

> The exponent $\tau$ is a fixed constant with $\tau<1$, so $u^{\tau}$ grows more slowly than $u$ itself. The procedure runs in $O(V u^{\tau})$ time.

### 3

Claim: The network has scratch wires for temporary values and restores them, and the final permutation is exact for any initial scratch values

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The final permutation is exact for arbitrary initial auxiliary values"

Paragraph:

> The procedure is built from a fixed [Linear networks and frames](linear-network-frames.md) network that exchanges two banks of values. The network has scratch wires for temporary values and restores them, and the final permutation is exact for any initial scratch values.

### 4

Claim: Each recursive level costs a strictly smaller power of $u$, because the network's edge ranks sum to less than its number of wires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Because the sum of these ranks is less than the number of wires"

Paragraph:

> The network is applied recursively to streams. A stream is a block of stored values handled as one unit, here a fraction of the volume $V$. Each recursive level costs a strictly smaller power of $u$, because the network's edge ranks sum to less than its number of wires.

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

Write the answer to `exegenius/tasks/0139-support-address-interchange.answer.json`, then run `exegenius submit 0139-support-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
