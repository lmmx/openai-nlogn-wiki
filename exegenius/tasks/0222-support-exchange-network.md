# exegenius task 0222-support-exchange-network

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

Claim: But $x_{S'}$ reaches $y_S$ with a coefficient depending on $|S\cap S'|$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "on intersection size, and auxiliary wires cancel the unwanted"

Paragraph:

> Through central wires $C_i$, $i\in[h]$, gather adds $\sum_{S'\ni i}x_{S'}$ to $C_i$, for $S'$ another triple, and scatter adds $\sum_{i\in S}C_i$ to $y_S$. But $x_{S'}$ reaches $y_S$ with a coefficient depending on $|S\cap S'|$. Side wires $A_{SS'}$, one per ordered neighbour pair, cancel it: copy adds $x_{S'}$ to $A_{SS'}$, and side injection adds a multiple of $A_{SS'}$ to $y_S$.

### 2

Claim: So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "invocation changes $y_S$ to $y_S+x_S$ and leaves every other value"

Paragraph:

> Let $\sigma,\gamma$ be the initial side and central values, and $\mathcal V,\mathcal G,\mathcal J,\mathcal R$ the copy, gather, injection and scatter maps. The schedule subtracts $\mathcal J\sigma+\mathcal R\gamma$ from $y$; copies and gathers, making the scratch values $\sigma+\mathcal Vx$, $\gamma+\mathcal Gx$; scatters and injects, adding $\mathcal R(\gamma+\mathcal Gx)+\mathcal J(\sigma+\mathcal Vx)$ to $y$; then undoes gather and copy, restoring $\gamma,\sigma$. The net change of $y$ is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$, free of $\sigma,\gamma$; by the coefficients above it is $y\gets y+x$. So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged.

### 3

Claim: At every $a$,
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Performing a forward invocation from $X$ to $Y$ at stage 1,"

Paragraph:

> The inverse schedule, the forward one with target updates negated, performs $X\gets X-Y$ when $Y$ is the source bank and $X$ the target. Run forward $X\to Y$ at stage 1, inverse $Y\to X$ at stage 2 and forward $X\to Y$ at stage 3. At every $a$,
> $$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
> that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires.

### 4

Claim: A triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "z_{\rm b}=3\binom{97}{2}=13968"

Paragraph:

> A triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction. It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus two). There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.

### 5

Claim: It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus two)

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "z_{\rm c}=\binom{97}{3}+3\cdot97=147731"

Paragraph:

> A triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction. It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus two). There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.

### 6

Claim: The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"

Paragraph:

> Ordered pairs are counted: $vz_{\rm b}$ side wires per invocation. The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires. The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires. All these numbers are fixed, independent of input length.

### 7

Claim: The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "W_{\rm c}&=2N+I(vz_{\rm c}+c_{\rm c})"

Paragraph:

> Ordered pairs are counted: $vz_{\rm b}$ side wires per invocation. The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires. The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires. All these numbers are fixed, independent of input length.

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

Write the answer to `exegenius/tasks/0222-support-exchange-network.answer.json`, then run `exegenius submit 0222-support-exchange-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0222-support-exchange-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
