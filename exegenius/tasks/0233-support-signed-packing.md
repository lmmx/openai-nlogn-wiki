# exegenius task 0233-support-signed-packing

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

Claim: So after removing lower coefficients, the next is identified by its centered residue modulo $B_0$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "this strict bound identifies the next coefficient by its centered residue modulo $B_0$"

Paragraph:

> The multiplier takes nonnegative integers, so signed packing multiplies the four pairs of absolute values with the [Established O(n log n) multiplier](hvdh-multiplier.md), restoring each sign, to obtain $A_aA_c,A_bA_e,A_aA_e,A_bA_c$. A product is negative when exactly one operand is. For the ordinary product $h=ac$ of integer polynomials, let $h_j$ be its coefficient of $y^j$ and pad $h_{2r-1}=0$. Then $A_aA_c=(ac)(B_0)=\sum_{j<2r}h_jB_0^j$. Each $h_j$ sums at most $r$ products of coefficients of size at most $2^p$, so $|h_j|\le r2^{2p}<2^{3p}<B_0/2$. So after removing lower coefficients, the next is identified by its centered residue modulo $B_0$.

### 2

Claim: Put $\rho_0=0$, and let $\rho_j$ be the carry into block $j$ and $\widehat h_j$ be the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$,"

Paragraph:

> Take a product integer $Z=\sum_{j<2r}h_jB_0^j$. Because $|Z|<B_0^{2r}/4$, zero-filling high blocks and, for a negative sign, complementing and incrementing converts it to $Z=\sum_{j<2r}q_jB_0^j+\varepsilon B_0^{2r}$ with blocks $0\le q_j<B_0$ and $\varepsilon\in\{-1,0\}$. Put $\rho_0=0$, and let $\rho_j$ be the carry into block $j$ and $\widehat h_j$ be the unique integer in $[-B_0/2,B_0/2)$ congruent to $q_j+\rho_j$ modulo $B_0$ and $\rho_{j+1}=(q_j+\rho_j-\widehat h_j)/B_0$. The carry is in $\{0,1\}$, since $q_j+\rho_j\in[0,B_0]$. If $\widehat h_i=h_i$ for $i<j$, then $\sum_{i<j}q_iB_0^i=\sum_{i<j}h_iB_0^i+\rho_jB_0^j$, so $q_j+\rho_j\equiv h_j$ modulo $B_0$. Since $h_j\in[-B_0/2,B_0/2)$, $\widehat h_j=h_j$.

### 3

Claim: Each part loses less than $2^{-p}$, so the error is less than $\sqrt2\,2^{-p}$ from $fg/r$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "with error less than $\sqrt2\,2^{-p}$ from $fg/r$"

Paragraph:

> Each coefficient of $fg/r$ is $2^{-2p}H_j/r$, of modulus at most $1$, so the normalized product of disk polynomials lies in the disk. Signed packing returns $Q_p(2^{-2p}H_j/r)$, shifting the magnitudes of the real and imaginary parts of $H_j$ right by $p+\log_2 r$ bits, an $O(p)$ step. Each part loses less than $2^{-p}$, so the error is less than $\sqrt2\,2^{-p}$ from $fg/r$.

### 4

Claim: Four exact integer products therefore dominate the linear packing, extraction, combination, wrapping and truncation costs, so the total is $O(rp\log(rp))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "in time $O(rp\log(rp))$ on a fixed number of tapes"

Paragraph:

> Every other stage is a constant number of scans of tapes holding $O(rp)$ bits, with a constant-size carry between blocks: forming the $A_u$, complementing, converting each $Z$, extracting the $\widehat h_j$, and the subtraction, after splitting the halves onto separate tapes to align coefficients $j$ and $j+r$. Each multiplier input has at most $4pr$ bits, so each product costs $O(rp\log(rp))$. Four exact integer products therefore dominate the linear packing, extraction, combination, wrapping and truncation costs, so the total is $O(rp\log(rp))$.

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

Write the answer to `exegenius/tasks/0233-support-signed-packing.answer.json`, then run `exegenius submit 0233-support-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0233-support-signed-packing`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
