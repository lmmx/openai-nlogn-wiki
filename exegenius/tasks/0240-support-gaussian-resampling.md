# exegenius task 0240-support-gaussian-resampling

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

Claim: Harvey and van der Hoeven's maps $\mathsf S,\mathsf T$ from length-$s$ to length-$t$ complex vectors are, for $0\le k<t$, with $u$ extended periodically and $j$ over all integers,
$$(\mathsf Su)_k=\frac1\alpha\sum_j e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (\mathsf Tu)_k=\sum_j e^{-\pi\alpha^2(tj/s-k)^2}u_j.$$
They satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\mathsf T P_sF_s=P_tF_t\mathsf S,"

Paragraph:

> Harvey and van der Hoeven's maps $\mathsf S,\mathsf T$ from length-$s$ to length-$t$ complex vectors are, for $0\le k<t$, with $u$ extended periodically and $j$ over all integers,
> $$(\mathsf Su)_k=\frac1\alpha\sum_j e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (\mathsf Tu)_k=\sum_j e^{-\pi\alpha^2(tj/s-k)^2}u_j.$$
> They satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$.

### 2

Claim: The other summands form $((N-I)u)_j$, and the cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}."

Paragraph:

> To undo $\mathsf T$, let $q_j$ be the integer nearest $tj/s$ and $\beta_j=tj/s-q_j$. Let $C$ select coordinates from length-$t$ to length-$s$ vectors, $(Cv)_j=v_{q_j}$, and $(\mathsf Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$. Put $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$, because $tj/s-q_j=\beta_j$. The other summands form $((N-I)u)_j$, and the cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$.

### 3

Claim: These are contractions, since $\|C\|=1$ and the three factors have norms below $3/4$, $7/8$, $1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\|\mathsf S'\|<\frac34,\qquad \|\mathsf J'\|<\frac78,\qquad \|\mathsf D'\|<1."

Paragraph:

> Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, and put $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. These are contractions, since $\|C\|=1$ and the three factors have norms below $3/4$, $7/8$, $1$.

### 4

Claim: The cited algorithms give approximations $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ with errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\widetilde{\mathsf S}'&16p&O(tp^{3/2+\delta}\alpha)\\"

Paragraph:

> Let $\mathbb D_p$ be the grid of [Fixed-point Gaussian dyadic records](fixed-point.md). An approximation $\widetilde L$ of a contraction $L$ has error below a bound if $2^p\|\widetilde Lu-Lu\|$ is less than it for all inputs $u\in\mathbb D_p$; composing approximations adds errors. Fix $0<\delta<1/8$, the time-exponent slack. The cited algorithms give approximations $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ with errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$.

### 5

Claim: The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "also cost $O(tp)$, so $C$ takes $O(tp)$ time with zero numerical error."

Paragraph:

> The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error.

### 6

Claim: Let $\widetilde E$ be the approximation of $E$ on $\mathbb D_p$ from the cited Lemma 4.11: for every $z\in\mathbb D_p^s$ $\widetilde Ez\in\mathbb D_p^s$ and $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\|\widetilde E z\|<0.42\|z\|+(p/3)2^{-p}<1"

Paragraph:

> Let $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$, the number of series terms kept (a new meaning of $k$). As $\|E\|<2^{-\alpha^2\theta}$ and $\alpha^2\theta>1$, the omitted terms sum to less than $2\cdot2^{-p}$. Let $\widetilde E$ be the approximation of $E$ on $\mathbb D_p$ from the cited Lemma 4.11: for every $z\in\mathbb D_p^s$ $\widetilde Ez\in\mathbb D_p^s$ and $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$. Start from $\widetilde v^{(0)}$, the rounding of $u/2$, and set $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$. The Neumann series with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$ with every iterate kept in $\mathbb D_p$.

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

Write the answer to `exegenius/tasks/0240-support-gaussian-resampling.answer.json`, then run `exegenius submit 0240-support-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0240-support-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
