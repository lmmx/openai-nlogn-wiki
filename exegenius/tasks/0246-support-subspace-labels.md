# exegenius task 0246-support-subspace-labels

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

Claim: Bit labels live in $F=\mathbb Q^h$, where $h=100$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "h=100,\qquad v=\binom h3=161700"

Paragraph:

> A subspace $U$ is *nondegenerate* when the form restricted to it is, so the space is $U\perp U^\perp$. Bit labels live in $F=\mathbb Q^h$, where $h=100$, with the form $\langle x,y\rangle=x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for vectors $x,y\in F$. Its matrix fixes zero-sum vectors and scales the all-ones vector by $1-h/9=-91/9\neq0$, so it is nondegenerate. Complex labels live in $F=\mathbb F_2^h$ with the dot product. For *triples* (three-element subsets of $[h]$) $S,T$, indicator vectors $t_S,t_T$ have integer dot product $|S\cap T|$ and entry sum $3$, so $\langle t_S,t_T\rangle=|S\cap T|-1$; over $\mathbb F_2$, $t_S\cdot t_T=|S\cap T|\bmod 2$. Each line $\langle t_T\rangle$ is thus nondegenerate ($\langle t_T,t_T\rangle\in\{2,1\}$), and *neighbours* (bit: sharing one element; complex: distinct with even intersection) are orthogonal.

### 2

Claim: Each of the $I=3v^2$ invocations ($v^2$ per stage) has one such edge per centre wire, so the losses are $L_{\rm b}=Ic_{\rm b}h$ and $L_{\rm c}=Ic_{\rm c}h$, with $c_{\rm b}=100$ (bit) and $c_{\rm c}=101$ (complex) centre wires per invocation

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "With $c_{\rm b}=100$ and $c_{\rm c}=101$ central wires per invocation"

Paragraph:

> The same splitting shows every arrow is an inclusion except centre $3\to4$, dropping $P\otimes F$ of dimension $h$; side $2\to5$ needs $\langle t_X\rangle\subset t_Y^\perp$, true as $t_X\perp t_Y$. Each of the $I=3v^2$ invocations ($v^2$ per stage) has one such edge per centre wire, so the losses are $L_{\rm b}=Ic_{\rm b}h$ and $L_{\rm c}=Ic_{\rm c}h$, with $c_{\rm b}=100$ (bit) and $c_{\rm c}=101$ (complex) centre wires per invocation. As $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$; likewise $L_{\rm c}/N=30300/161700=101/539$. Both are below $1/2$.

### 3

Claim: Bit-network edges cost one smaller call per unit of rank of their endpoints' rational matrix difference

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "implements an edge change with one smaller interchange per unit of its rational rank"

Paragraph:

> Bit-network edges cost one smaller call per unit of rank of their endpoints' rational matrix difference. A vertex labelled $U$ gets the projection $\Pi_U$ onto $U$ along $U^\perp$, except sources: $-\Pi_{U_a}$ at $X_a$, else $0$. For $U\subset V$, $\Pi_V-\Pi_U$ (identity on $V\cap U^\perp$, zero on $U\perp V^\perp$) has rank $\dim V-\dim U$, as does its negative. Only $X_a$'s first edge differs: at stage $1$ its first gate has label $U_a$, so $2\Pi_{U_a}$ has rank one where the dimension change is zero. Endpoint differences ($\Pi_{U_a^\perp}+\Pi_{U_a}$ from source $X_a$ to sink $Y_a$, else $\mathrm{Id}-0$) all equal $\mathrm{Id}$, giving every role the same shear. So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$. [Binary phase frames](phase-frames.md) give the complex network $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.

### 4

Claim: So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "=W_{\rm b}m-N+2L_{\rm b} =177176569088785861287000000<W_{\rm b}m"

Paragraph:

> Bit-network edges cost one smaller call per unit of rank of their endpoints' rational matrix difference. A vertex labelled $U$ gets the projection $\Pi_U$ onto $U$ along $U^\perp$, except sources: $-\Pi_{U_a}$ at $X_a$, else $0$. For $U\subset V$, $\Pi_V-\Pi_U$ (identity on $V\cap U^\perp$, zero on $U\perp V^\perp$) has rank $\dim V-\dim U$, as does its negative. Only $X_a$'s first edge differs: at stage $1$ its first gate has label $U_a$, so $2\Pi_{U_a}$ has rank one where the dimension change is zero. Endpoint differences ($\Pi_{U_a^\perp}+\Pi_{U_a}$ from source $X_a$ to sink $Y_a$, else $\mathrm{Id}-0$) all equal $\mathrm{Id}$, giving every role the same shear. So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$. [Binary phase frames](phase-frames.md) give the complex network $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.

### 5

Claim: Since $Iv=3N$ and $Ic_{\rm b}=N/539$, $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"

Paragraph:

> The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$, but tiny beside $W_{\rm b}m$. Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$). Since $Iv=3N$ and $Ic_{\rm b}=N/539$, $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$.

### 6

Claim: , so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "=\frac{339}{22587335000000}"

Paragraph:

> The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$, but tiny beside $W_{\rm b}m$. Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$). Since $Iv=3N$ and $Ic_{\rm b}=N/539$, $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$.

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

Write the answer to `exegenius/tasks/0246-support-subspace-labels.answer.json`, then run `exegenius submit 0246-support-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0246-support-subspace-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
