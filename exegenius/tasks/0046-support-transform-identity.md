# exegenius task 0046-support-transform-identity

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

Claim: The paper makes this choice explicitly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We retain both permutations in the transform formula"

Paragraph:

> The transform identity with retained permutations is an exact identity between the normalized Fourier transforms $F_s$ and $F_t$ of two lengths, in which both coordinate permutations $P_s$ and $P_t$ stay as explicit factors. It is obtained by inverting the [Gaussian resampling](gaussian-resampling.md) identity, which keeps both permutations. The usual implementation sorts twice on each coordinate. Keeping both permutations in the formula avoids those sorts and lets them cancel across a convolution. The paper makes this choice explicitly

### 2

Claim: The claim is stated in

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Lemma 19 (Resampling without executing the two permutations)"

Paragraph:

> Here $2\le s<t$, $s$ and $t$ are coprime, $\alpha\ge 2$, and $\theta=t/s-1$ satisfies $\alpha^2\theta>1$. Here $v$ is a generic length-$t$ vector, not the second integer of radix-digit convolution. The permutations are $(P_su)_j=u_{tj}$ for a length-$s$ vector $u$, and $(P_tv)_k=v_{-sk}$ for a length-$t$ vector $v$, with subscripts taken modulo $s$ and $t$. The identity is
> $$P_sF_s=2^{2\alpha^2}B_0P_tF_tA,$$
> where $A$ is a linear map from length-$s$ to length-$t$ vectors and $B_0$ is a linear map from length-$t$ to length-$s$ vectors. The letters $A$ and $B_0$ mean these new maps here, not the $A=S$ and $B=DN^{-1}C$ of the Gaussian resampling page. The two maps are linear contractions, bounded in the [operator norm](operator-norm.md) by one, meaning each sends a vector to one of norm at most its input norm. The claim is stated in.

### 3

Claim: Prior work establishes it, with the proof in

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "[15, Theorem 4.2 and Lemma 4.6]"

Paragraph:

> The proof uses the Gaussian maps $S$ and $T$, which send length-$s$ vectors to length-$t$ vectors, and the Gaussian identity
> $$TP_sF_s=P_tF_tS.$$
> It says that transforming at length $s$ and then resampling with $T$ agrees with resampling with $S$ and then transforming. Prior work establishes it, with the proof in, and it applies because $S$ and $T$ share the same $s$, $t$ and $\alpha$.

### 4

Claim: The operator $N=CTD$ is close to $I$: the inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "[15, Theorem 4.2 and Lemma 4.6]"

Paragraph:

> Let $I$ denote the identity map. The operator $N=CTD$ is close to $I$: the inverse estimate of prior work gives $\|N-I\|<2^{-\alpha^2\theta}$, which is below $1/2$ because $\alpha^2\theta>1$. The Neumann series is the matrix analogue of the geometric series, and it converges when $\|I-N\|<1$.

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

Write the answer to `exegenius/tasks/0046-support-transform-identity.answer.json`, then run `exegenius submit 0046-support-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
