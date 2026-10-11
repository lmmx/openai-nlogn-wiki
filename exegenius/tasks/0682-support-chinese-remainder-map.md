# exegenius task 0682-support-chinese-remainder-map

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

Claim: In the exact multiplication algorithm,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the radix-digit coefficient list is placed on a product of distinct"

Paragraph:

> The Chinese-remainder map is a relabeling of coefficient positions. It is applied to a [cyclic convolution](cyclic-convolution.md) and turns it into a multidimensional cyclic convolution whose axes have pairwise [coprime](coprime.md) lengths. It places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes. In the exact multiplication algorithm, prime cyclic axes. It is also called the Agarwal–Cooley map, after the authors who used the [Chinese remainder theorem](chinese-remainder-theorem.md) to split a cyclic convolution: cyclic convolution. This map uses.

### 2

Claim: It is also called the Agarwal–Cooley map, after the authors who used the [Chinese remainder theorem](chinese-remainder-theorem.md) to split a cyclic convolution:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional"

Paragraph:

> The Chinese-remainder map is a relabeling of coefficient positions. It is applied to a [cyclic convolution](cyclic-convolution.md) and turns it into a multidimensional cyclic convolution whose axes have pairwise [coprime](coprime.md) lengths. It places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes. In the exact multiplication algorithm, prime cyclic axes. It is also called the Agarwal–Cooley map, after the authors who used the [Chinese remainder theorem](chinese-remainder-theorem.md) to split a cyclic convolution: cyclic convolution. This map uses.

### 3

Claim: This map uses

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that algebraic split"

Paragraph:

> The Chinese-remainder map is a relabeling of coefficient positions. It is applied to a [cyclic convolution](cyclic-convolution.md) and turns it into a multidimensional cyclic convolution whose axes have pairwise [coprime](coprime.md) lengths. It places the coefficients of a [radix-digit convolution](radix-digit-convolution.md) on distinct prime cyclic axes. In the exact multiplication algorithm, prime cyclic axes. It is also called the Agarwal–Cooley map, after the authors who used the [Chinese remainder theorem](chinese-remainder-theorem.md) to split a cyclic convolution: cyclic convolution. This map uses.

### 4

Claim: These $\Lambda$ distinct monomials exhaust the basis, so the powers $\Phi(x)^0,\dots,\Phi(x)^{\Lambda-1}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "through all target basis monomials exactly once."

Paragraph:

> Let $e$ be an ordinary coefficient index, $0\le e<\Lambda$ (the letter $e$ changes meaning from earlier pages). The powers $\Phi(x)^e$ are distinct: suppose $\Phi(x)^a=\Phi(x)^b$ for exponents $a$ and $b$ with $0\le a<b<\Lambda$. Multiplying by the inverse of $\Phi(x)^a$ gives $\Phi(x)^{b-a}=1$, so $\Lambda\mid b-a$, impossible since $0<b-a<\Lambda$. Each $\Phi(x)^e=\prod_i x_i^{\mu_i e}$ is a basis monomial once its exponents are reduced modulo the $\lambda_i$. These $\Lambda$ distinct monomials exhaust the basis, so the powers $\Phi(x)^0,\dots,\Phi(x)^{\Lambda-1}$

### 5

Claim: The source confirms this:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Hence Φ is an isomorphism and preserves cyclic"

Paragraph:

> So $\Phi$ maps the basis $1,x,\dots,x^{\Lambda-1}$ bijectively onto the standard basis of the target. The source confirms this: convolution. A ring isomorphism carries products to products, so the cyclic convolution becomes a multidimensional one on axes $\lambda_1,\dots,\lambda_D$.

### 6

Claim: Substituting the digits gives
$$\mu_i e=\mu_i e_i\pi_i+\mu_i\sum_{j<i}e_j\pi_j+\sum_{j>i}\mu_i e_j\pi_j.$$
For $j>i$, $\pi_j$ contains the factor $\lambda_i$, so the last sum vanishes modulo $\lambda_i$ (

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Indeed terms with j > i are divisible by si"

Paragraph:

> Each index $e$ has [mixed-radix digits](mixed-radix-digits.md) $e_1,\dots,e_D$, where $e_j$ is the digit on axis $j$ and $0\le e_j<\lambda_j$., namely $e=\sum_{j=1}^D e_j\pi_j$. The Chinese-remainder map computes its coordinates from the mixed-radix digits of $e$. Let $\gamma_i\in[0,\lambda_i)$ be the coordinate of $e$ on axis $i$, meaning the exponent of $x_i$ in $\Phi(x^e)$ reduced modulo $\lambda_i$. Since $\Phi(x^e)=\prod_i x_i^{\mu_i e}$, $\gamma_i$ is $\mu_i e$ reduced modulo $\lambda_i$. Substituting the digits gives
> $$\mu_i e=\mu_i e_i\pi_i+\mu_i\sum_{j<i}e_j\pi_j+\sum_{j>i}\mu_i e_j\pi_j.$$
> For $j>i$, $\pi_j$ contains the factor $\lambda_i$, so the last sum vanishes modulo $\lambda_i$ (, where the paper writes $s_i$ for $\lambda_i$). The first term is $e_i(\mu_i\pi_i)\equiv e_i$, so
> $$\gamma_i\equiv e_i+\mu_i\sum_{j<i}e_j\pi_j \pmod{\lambda_i}.$$

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

Write the answer to `exegenius/tasks/0682-support-chinese-remainder-map.answer.json`, then run `exegenius submit 0682-support-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
