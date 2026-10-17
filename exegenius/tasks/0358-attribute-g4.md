# exegenius task 0358-attribute-g4

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage.

## Key points

1. Cutting each integer into radix-2^b digits makes the product a convolution of short integer coefficients, and the padded length S exceeds the product's degree so cyclic wraparound does nothing.
2. The Chinese-remainder address map re-lays a cyclic convolution of length S as a convolution over several axes of pairwise coprime prime lengths, via cheap triangular controlled shifts.
3. Prime-length transforms are not directly available from the fast power-of-two machinery, so Gaussian resampling approximates them through nearby power-of-two lengths and the chirp identity converts the remaining permuted transform into a cyclic convolution.
4. A phase twist converts the last cyclic axis into the ring modulo y^r + 1, where roots of unity are powers of y, so the synthetic transform needs only signed shifts and can use the fast primitives.
5. After the pointwise product and the opposite transform, rescaling and rounding recover the integer coefficients and carry propagation yields the binary product.

## Answers

### Answer 1

The chain turns two n-bit integers into their exact 2n-bit product in five stages, each feeding the next. (1) Radix digits (page vub): each input is written in radix 2^b with b = ceil(log2 n) and q digits, so the product becomes a convolution of short coefficient sequences, and the page shows that the convolution length S is large enough that nothing wraps around, and every coefficient is below 2^{3b}. (2) Address map (page guf): the map Phi sends a convolution of length S = s_1...s_d, with pairwise coprime axis lengths s_i, to a convolution on d axes by moving the data only with controlled shifts and axis reorderings. The page says this 'prepares' the next stage but does not say why the axes must be split, so I take it that the next stage works on each prime axis separately. (3) Resampling with chirps (pages roz, pap, dib): each prime-length transform is re-expressed through a power-of-two length t, with the source and target permutations left in place, so that only power-of-two transforms need a fast algorithm. For even t_i the chirp identity on page pap removes the target permutation: the transform becomes a chirp phase, a convolution of length T, and another chirp phase, so the permutation is absorbed into the convolution and never executed as a sort. (4) Twist to the polynomial ring (page taf): multiplying coefficient k of the last cyclic axis of length r by zeta^k, with zeta = e^{pi i/r}, turns that axis into the coordinate of the ring with y^r = -1; a wrap-around then carries a sign that exactly cancels the twist, so convolution along that axis becomes ring convolution, and the twist is undone afterwards. (5) Synthetic-transform convolution (pages tab and kur): the ring convolution over the remaining axes is computed from two forward transforms, M pointwise ring products, and the opposite transform, then scaled by M. Back on page siz, the scalings by S undo the 1/S normalizations, the result is multiplied by 2^{2b+4} S, rounded to the nearest integers, mapped back by Phi inverse, and carries are propagated to give the 2n-bit product, with total error below 1/2 so rounding is exact. The step from stage 3 to 4 and the claim that the twist is what makes the synthetic transform applicable are the weakest links; I followed the algebra but could not verify the cited error bounds.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "Splitting each input into digits in a large power-of-two radix turns the integer product into a convolution of short integer sequences"
2. "Every exponent $j$ is at most $2q-2<S$, so nothing folds."
3. "Any approximation of $c_j$ with error below $1/2$ rounds to $c_j$,"
4. "moving the data on tape by controlled shifts and axis reorderings only"
5. "so the powers run through all of them exactly once"
6. "Gaussian resampling expresses a Discrete Fourier transform of length $s$, the source length, through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm."
7. "the identity below supplies power-of-two transforms instead."
8. "so the target permutation of resampling is absorbed into the convolution and never executed as a sort."
9. "The permutation needs no separate step: it only changes which frequency is read, and the sign of the cross term $2j_ik_i$ already matches it."
10. "so that Cyclic convolution can be computed by ring convolution, and that is undone afterwards."
11. "The coefficient of $y^j$ is thus $\zeta^j$ times the cyclic coefficient; untwisting by $\zeta^{-j}$ restores it with the correct sign."
12. "Multiply the $M$ record pairs pointwise there, apply the opposite procedure to that order, and multiply by $M$."
13. "A convolution is thus computed by two forward transforms, a pointwise product, one opposite transform, and a known rescaling."
14. "The two scalings by $S$ undo different normalizations."
15. "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits."
16. "the error on these coefficients is below $1/2$, so rounding is exact."

### Answer 2

The chain runs in six stages, each one reducing the product to something the next stage can handle. (1) Radix digits (page vub): each n-bit integer is written as q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n). The digit product is a wrap-around product (the wiki's Cyclic convolution) of length S, and S is long enough that nothing wraps and every coefficient fits in 3b bits, so the integer product becomes a Cyclic convolution of short coefficients. (2) Address map (page guf): S is a product of pairwise coprime lengths s_1..s_d. The map sending x to the product of x_i raised to mu_i is an isomorphism that preserves Cyclic convolution, so the single length-S Cyclic convolution becomes a d-axis one, with one axis per s_i. This is needed because the later stages act on one axis at a time. (3) Resampling and chirps (pages roz and pap): a transform of prime length s is re-expressed through a transform of a nearby power-of-two length t, so only power-of-two transforms need a fast algorithm. For even t_i the chirp identity gives Q F_t u = conj(a) times (a Cyclic convolution (conj(a) times u)) divided by T, so the target reordering is absorbed into an ordinary Cyclic convolution of power-of-two length T, between two pointwise phase multiplications. (4) Twist (page taf, with page reb): the last cyclic axis is turned into the ring R_r = C[y]/(y^r+1) by multiplying entry k by zeta^k with zeta = e^(pi i/r). The wrap sign of ring multiplication then reproduces the Cyclic convolution on that axis. This is needed because in R_r multiplying by a power of y is only a signed shift, so the transforms over the ring need no complex multiplications. (5) Synthetic-transform convolution (pages tab and gip): both operands are transformed over R_r with roots of unity omega_t = y^(2r/t), multiplied record by record in the ring, and transformed back, with a scaling by the number of records. (6) Assembly and rounding (page siz): after the two forward transforms, the pointwise product, the opposite transform, a rescaling by S, and multiplication by 2^(2b+4) S, the values are rounded to integers, mapped back by the inverse address map, and carries are propagated to give the exact 2n-bit product. Rounding is exact because the error is below 1/2, a claim the page cites to another page that I did not open. Confidence is moderate: I could follow the stage-by-stage reductions and their size bookkeeping, but I took the error bounds and the cited lemmas on trust.

Covers key points: 1, 2, 3, 4, 5

Quotations:

1. "The multiplication algorithm chains the reductions of the earlier pages to turn two $n$-bit integers into their exact $2n$-bit product."
2. "Multiplication therefore reduces to a [Cyclic convolution](fam) of length $S$ on short integer coefficients."
3. "Every exponent $j$ is at most $2q-2<S$, so nothing folds."
4. "So every coefficient is a nonnegative integer of at most $3b$ bits."
5. "moving the data on tape by controlled shifts and axis reorderings only."
6. "is an isomorphism and preserves [Cyclic convolution](fam)."
7. "Gaussian resampling expresses a Discrete Fourier transform of length $s$, the source length, through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm."
8. "Applied along each axis of a [Multidimensional transforms](dib), it replaces $s$ by $t$."
9. "The Bluestein chirp identity rewrites a permuted [Discrete Fourier transform](kur) as a pointwise chirp phase, a Cyclic convolution, and another chirp phase, so the target permutation of resampling is absorbed into the convolution and never executed as a sort."
10. "The permuted transform is thus reduced to one [Cyclic convolution](fam) of length $T$ between two pointwise phase multiplications."
11. "The twist converts the last cyclic axis into the coordinate of the [Polynomial ring modulo y^r + 1](reb)"
12. "The twist reproduces [Cyclic convolution](fam) on that axis."
13. "this is what lets the later transforms avoid complex multiplications."
14. "so every twiddle multiplication (multiplication by a root of unity) is a signed shift of a coefficient list."
15. "computed by transforming both operands, multiplying records pointwise and transforming back."
16. "The transform diagonalizes [Cyclic convolution](fam): the transform of a convolution is a pointwise product of transforms."
17. "A convolution is thus computed by two forward transforms, a pointwise product, one opposite transform, and a known rescaling."
18. "Multiply by $2^{2b+4}S$, round to the nearest integers"
19. "Exactness is shown by [Error tracking and exact recovery](mes): the error on these coefficients is below $1/2$, so rounding is exact."

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Attribution": {
      "additionalProperties": false,
      "properties": {
        "answer": {
          "description": "Number of the answer, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "support": {
          "items": {
            "$ref": "#/$defs/Support"
          },
          "type": "array"
        }
      },
      "required": [
        "answer",
        "support"
      ],
      "type": "object"
    },
    "Support": {
      "additionalProperties": false,
      "description": "The quotation that supports one covered key point.",
      "properties": {
        "point": {
          "description": "Number of the key point.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "quotation": {
          "description": "Number of the quotation under the answer.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        }
      },
      "required": [
        "point",
        "quotation"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "answers": {
      "description": "One entry for every answer listed.",
      "items": {
        "$ref": "#/$defs/Attribution"
      },
      "type": "array"
    }
  },
  "required": [
    "answers"
  ],
  "title": "AttributeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0358-attribute-g4.answer.json`, then run `exegenius submit 0358-attribute-g4` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0358-attribute-g4`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
