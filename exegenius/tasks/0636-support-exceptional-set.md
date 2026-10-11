# exegenius task 0636-support-exceptional-set

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

Claim: The failures of that formula are confined to the exceptional set, and the source repairs them afterwards:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "by a deterministic correction of the explicitly identified exceptional addresses."

Paragraph:

> The exceptional set is a set of [Address](address.md) values, namely those at which the generic formula must be replaced by a special rule. Outside it the generic formula is correct, so a procedure that applies the generic formula everywhere is wrong only at these addresses, and only they need extra work. The main argument needs this because a [simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies a two-point map (a rule that takes a pair of values and returns a new pair) to every pair of entries whose addresses differ in one of several selected bits. It does this in one tape pass, using one generic formula for all pairs. The failures of that formula are confined to the exceptional set, and the source repairs them afterwards:

### 2

Claim: The source defines the exceptional addresses for this layer as those at which such a test fails:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Let B consist of the addresses for which at least one used guard value, in either y or z, fails"

Paragraph:

> In the layer, the generic formula is a packed addition: several small fields inside one binary number are updated by one addition, and a field that overflows carries into its neighbour. A guard value is a field value that the source tests against a fixed range before the addition. The source defines the exceptional addresses for this layer as those at which such a test fails: the range test. Outside this set no field carries into the next, so the generic formula is correct there:.

### 3

Claim: Outside this set no field carries into the next, so the generic formula is correct there:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "no segment carries into or borrows from the next segment"

Paragraph:

> In the layer, the generic formula is a packed addition: several small fields inside one binary number are updated by one addition, and a field that overflows carries into its neighbour. A guard value is a field value that the source tests against a fixed range before the addition. The source defines the exceptional addresses for this layer as those at which such a test fails: the range test. Outside this set no field carries into the next, so the generic formula is correct there:.

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

Write the answer to `exegenius/tasks/0636-support-exceptional-set.answer.json`, then run `exegenius submit 0636-support-exceptional-set` in the project directory. If submit rejects the answer, fix the answer and submit again.
