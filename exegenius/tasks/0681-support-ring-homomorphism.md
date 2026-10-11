# exegenius task 0681-support-ring-homomorphism

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

Claim: The paper checks that this is well defined with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "respects xS = 1, so it defines an algebra map."

Paragraph:

> Let $S=s_1\cdots s_d$, where the $s_i$ are pairwise coprime, and let $x$ be the generator of the first ring. The paper's map $\Phi$ sends $\mathbb{C}[x]/(x^S-1)$ to $\mathbb{C}[x_1,\dots,x_d]/(x_1^{s_1}-1,\dots,x_d^{s_d}-1)$. $\Phi$ sends $x$ to the monomial $g=\prod_i x_i^{\mu_i}$, where $\mu_i$ is the paper's integer with $P_i\mu_i\equiv 1 \pmod{s_i}$ and $P_i=s_1\cdots s_{i-1}$, with $P_1=1$. The paper checks that this is well defined with Substituting $g$ for $x$ gives a homomorphism as in the lemma, and $g^S=1$ because each $s_i$ divides $S$.

### 2

Claim: Hence the powers of $g$ run

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "through all target basis monomials exactly once."

Paragraph:

> Bijectivity is verified using a [basis](linear-algebra-basics.md) of the target. The monomials $x_1^{e_1}\cdots x_d^{e_d}$, where $e_i$ is the exponent of $x_i$ and $0\le e_i<s_i$, form a basis of the target, and there are $S$ of them. The power $g^k$ is the basis monomial with exponents $k\mu_i \bmod s_i$. If $g^k=g^{k'}$ with $0\le k,k'<S$, then $s_i\mid(k-k')\mu_i$ for each $i$, so $s_i\mid k-k'$ because $\mu_i$ is invertible modulo $s_i$, and so $S\mid k-k'$ by pairwise coprimality. Hence the powers of $g$ run So $\Phi$ maps the basis $1,x,\dots,x^{S-1}$ of the source onto the target basis, and it is bijective as well as a homomorphism.

### 3

Claim: The paper's statement is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Hence Φ is an isomorphism and preserves cyclic"

Paragraph:

> The paper's statement is. An isomorphism of this kind [preserves cyclic convolution](cyclic-convolution.md). Identify a sequence $(a_k)$ of length $S$ with $a=\sum_k a_kx^k$, and likewise $b$. The product $ab$ is the cyclic convolution of $a$ and $b$, so $\Phi(ab)=\Phi(a)\Phi(b)$ and $ab=\Phi^{-1}(\Phi(a)\Phi(b))$.

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

Write the answer to `exegenius/tasks/0681-support-ring-homomorphism.answer.json`, then run `exegenius submit 0681-support-ring-homomorphism` in the project directory. If submit rejects the answer, fix the answer and submit again.
