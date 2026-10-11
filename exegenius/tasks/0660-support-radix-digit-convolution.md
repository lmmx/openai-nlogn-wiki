# exegenius task 0660-support-radix-digit-convolution

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

Claim: The paper states the reduction in one sentence:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients."

Paragraph:

> The paper states the reduction in one sentence:

### 2

Claim: The paper sets

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "b = ⌈log2 n⌉"

Paragraph:

> **Digits.** Let $x$ and $y$ be the two binary inputs, each of $n$ bits, with $n \ge 2$. Let $b$ be the digit width, the number of bits in each digit (the letter $b$ changes meaning here). The paper sets. Since $b \ge \log_2 n$, we have $2^b \ge n$. Cut each input into blocks of $b$ bits, counting from the least significant end, and pad the last block with leading zeros. Each block is a digit with a value from $0$ to $2^b-1$, and $2^b$ is the radix. Let $J = \lceil n/b\rceil$ be the number of digits in each input. Let $x_i$ be the digit of $x$ at position $i$, for $0 \le i \le J-1$, so that $x = \sum_{i=0}^{J-1} x_i (2^b)^i$. The digits $y_j$ of $y$ are defined the same way.

### 3

Claim: The paper's count is that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Θ(log n) transform levels already costs Θ(n log n)."

Paragraph:

> **Where the cost goes.** The convolution is computed with the [Discrete Fourier transform](discrete-fourier-transform.md) at a power-of-two length of at least $2J-1$. That length avoids wraparound, since the product has $2J-1$ coefficients. A transform of length $2^k$ has $k$ levels, one for each bit of the position index, so the number of levels is $\Theta(\log n)$ because $J = \Theta(n/b)$ and $b = \Theta(\log n)$. Its transforms are built from [Butterfly](butterfly.md) operations, and each transform level applies them to the whole array. A level reads the array in order and writes each entry back at its new position, so the head visits every stored bit once per level, and the time is proportional to the stored bits, $\Theta(n)$ after the split. The arithmetic is proportional too. A level performs about $J$ butterflies, each on one coefficient of $O(\log n)$ bits, so it costs $O(n)$ bit steps. Each level therefore costs $\Theta(n)$, and the $\Theta(\log n)$ levels multiply this to $\Theta(n\log n)$. The split removes the cost of the digits, and the cost that remains lies in the transforms. The paper's count is that

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

Write the answer to `exegenius/tasks/0660-support-radix-digit-convolution.answer.json`, then run `exegenius submit 0660-support-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
