# exegenius task 0719-support-destination-rank

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

Claim: The paper computes ranks this way:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "scan the stream with a record-rank counter"

Paragraph:

> Each record is a block of $R$ payload bits, where $R$ is the number of payload bits in a record. It is stored at an address $\Psi=(\Psi_1,\Psi_2,\Psi_3)$ of three chunks, named $1$, $2$ and $3$, where $\Psi_1$, $\Psi_2$, $\Psi_3$ are its chunk values. The rectangular routine runs packed additions on a stream whose addresses form a complete rectangle in these chunks. Every other address field is fixed across the rectangle; such a field is a spectator. The rank $\operatorname{rank}(\Psi)$ of the record at $\Psi$ is its position among the records in stream order, counted from $0$. The destination rank is computed by a scan of the [Stream](stream.md) in order, with a counter. The paper computes ranks this way:.

### 2

Claim: The algorithm extracts the records at the addresses of $\mathcal{E}$, gives each one the key $\operatorname{rank}(\Psi')$, and marks its hole, the address $\Psi'$ it returns to:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "mark its hole on a fixed track of the full stream"

Paragraph:

> The algorithm extracts the records at the addresses of $\mathcal{E}$, gives each one the key $\operatorname{rank}(\Psi')$, and marks its hole, the address $\Psi'$ it returns to:. Distinct addresses have distinct ranks, so holes.

### 3

Claim: Distinct addresses have distinct ranks, so

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "these keys are distinct and are exactly the ranks of the marked"

Paragraph:

> The algorithm extracts the records at the addresses of $\mathcal{E}$, gives each one the key $\operatorname{rank}(\Psi')$, and marks its hole, the address $\Psi'$ it returns to:. Distinct addresses have distinct ranks, so holes.

### 4

Claim: The paper defines

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Arect = ⌈log2 (2V )⌉"

Paragraph:

> Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md). That sort makes one pass per key bit, least significant bit first, and keeps equal keys in their earlier order., and ranks are among them. Ranks lie in $\{0,\dots,M-1\}$, so a key has $\lceil\log_2 M\rceil$ bits. Let $V=MR$ be the number of bits in the stream, so $M\le V$. The paper defines, hence $\lceil\log_2 M\rceil\le A_{\mathrm{rect}}$. The sort therefore makes at most $A_{\mathrm{rect}}$ passes:.

### 5

Claim: The sort therefore makes at most $A_{\mathrm{rect}}$ passes:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the at most Arect radix passes"

Paragraph:

> Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md). That sort makes one pass per key bit, least significant bit first, and keeps equal keys in their earlier order., and ranks are among them. Ranks lie in $\{0,\dots,M-1\}$, so a key has $\lceil\log_2 M\rceil$ bits. Let $V=MR$ be the number of bits in the stream, so $M\le V$. The paper defines, hence $\lceil\log_2 M\rceil\le A_{\mathrm{rect}}$. The sort therefore makes at most $A_{\mathrm{rect}}$ passes:.

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

Write the answer to `exegenius/tasks/0719-support-destination-rank.answer.json`, then run `exegenius submit 0719-support-destination-rank` in the project directory. If submit rejects the answer, fix the answer and submit again.
