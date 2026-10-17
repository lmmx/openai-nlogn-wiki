# exegenius task 0349-grade-g4

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage.

## Key points

1. Cutting each integer into radix-2^b digits makes the product a convolution of short integer coefficients, and the padded length S exceeds the product's degree so cyclic wraparound does nothing.
2. The Chinese-remainder address map re-lays a cyclic convolution of length S as a convolution over several axes of pairwise coprime prime lengths, via cheap triangular controlled shifts.
3. Prime-length transforms are not directly available from the fast power-of-two machinery, so Gaussian resampling approximates them through nearby power-of-two lengths and the chirp identity converts the remaining permuted transform into a cyclic convolution.
4. A phase twist converts the last cyclic axis into the ring modulo y^r + 1, where roots of unity are powers of y, so the synthetic transform needs only signed shifts and can use the fast primitives.
5. After the pointwise product and the opposite transform, rescaling and rounding recover the integer coefficients and carry propagation yields the binary product.

## Answers

### Answer A

The background does not cover this question in full, so I can only explain the parts that rest on material the reader has seen. The background covers polynomials, complex numbers, big-O notation, Karatsuba multiplication, modular arithmetic, binary representation, and Turing machines with tapes. It does not cover the discrete Fourier transform or FFT, chirps or chirp-type resampling, quotient rings beyond basic definitions, tensor products, or the literature on fast integer multiplication. I cannot say what the stages named in the question (the address map, the chirp resampling, the twist to the polynomial ring, and the synthetic-transform convolution) do, or why each is needed for the next, because the background gives no definition or method for any of them.

What the reader can follow: writing an integer in a radix (for example base 2 or base 10) splits it into digits, and an integer product can be seen as a polynomial product in which the radix plays the role of the variable's value, with the digits as coefficients. Multiplying two polynomials is a convolution of their coefficient lists. Karatsuba shows that splitting such products into smaller pieces can lower the asymptotic cost below schoolbook multiplication, which is the sense in which fast methods are compared by big-O. Complex numbers and the polynomial background give the reader the vocabulary to describe evaluating a polynomial at several points, but the background does not say how a transform of power-of-two length is defined, why it turns convolution into pointwise products, or how the stages connect. A full explanation of the chain in the question therefore needs material outside this background.

### Answer B

The chain turns two n-bit integers into their exact 2n-bit product in five stages, each feeding the next. (1) Radix digits (page vub): each input is written in radix 2^b with b = ceil(log2 n) and q digits, so the product becomes a convolution of short coefficient sequences, and the page shows that the convolution length S is large enough that nothing wraps around, and every coefficient is below 2^{3b}. (2) Address map (page guf): the map Phi sends a convolution of length S = s_1...s_d, with pairwise coprime axis lengths s_i, to a convolution on d axes by moving the data only with controlled shifts and axis reorderings. The page says this 'prepares' the next stage but does not say why the axes must be split, so I take it that the next stage works on each prime axis separately. (3) Resampling with chirps (pages roz, pap, dib): each prime-length transform is re-expressed through a power-of-two length t, with the source and target permutations left in place, so that only power-of-two transforms need a fast algorithm. For even t_i the chirp identity on page pap removes the target permutation: the transform becomes a chirp phase, a convolution of length T, and another chirp phase, so the permutation is absorbed into the convolution and never executed as a sort. (4) Twist to the polynomial ring (page taf): multiplying coefficient k of the last cyclic axis of length r by zeta^k, with zeta = e^{pi i/r}, turns that axis into the coordinate of the ring with y^r = -1; a wrap-around then carries a sign that exactly cancels the twist, so convolution along that axis becomes ring convolution, and the twist is undone afterwards. (5) Synthetic-transform convolution (pages tab and kur): the ring convolution over the remaining axes is computed from two forward transforms, M pointwise ring products, and the opposite transform, then scaled by M. Back on page siz, the scalings by S undo the 1/S normalizations, the result is multiplied by 2^{2b+4} S, rounded to the nearest integers, mapped back by Phi inverse, and carries are propagated to give the 2n-bit product, with total error below 1/2 so rounding is exact. The step from stage 3 to 4 and the claim that the twist is what makes the synthetic transform applicable are the weakest links; I followed the algebra but could not verify the cited error bounds.

### Answer C

The chain runs in six stages, each one reducing the product to something the next stage can handle. (1) Radix digits (page vub): each n-bit integer is written as q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n). The digit product is a wrap-around product (the wiki's Cyclic convolution) of length S, and S is long enough that nothing wraps and every coefficient fits in 3b bits, so the integer product becomes a Cyclic convolution of short coefficients. (2) Address map (page guf): S is a product of pairwise coprime lengths s_1..s_d. The map sending x to the product of x_i raised to mu_i is an isomorphism that preserves Cyclic convolution, so the single length-S Cyclic convolution becomes a d-axis one, with one axis per s_i. This is needed because the later stages act on one axis at a time. (3) Resampling and chirps (pages roz and pap): a transform of prime length s is re-expressed through a transform of a nearby power-of-two length t, so only power-of-two transforms need a fast algorithm. For even t_i the chirp identity gives Q F_t u = conj(a) times (a Cyclic convolution (conj(a) times u)) divided by T, so the target reordering is absorbed into an ordinary Cyclic convolution of power-of-two length T, between two pointwise phase multiplications. (4) Twist (page taf, with page reb): the last cyclic axis is turned into the ring R_r = C[y]/(y^r+1) by multiplying entry k by zeta^k with zeta = e^(pi i/r). The wrap sign of ring multiplication then reproduces the Cyclic convolution on that axis. This is needed because in R_r multiplying by a power of y is only a signed shift, so the transforms over the ring need no complex multiplications. (5) Synthetic-transform convolution (pages tab and gip): both operands are transformed over R_r with roots of unity omega_t = y^(2r/t), multiplied record by record in the ring, and transformed back, with a scaling by the number of records. (6) Assembly and rounding (page siz): after the two forward transforms, the pointwise product, the opposite transform, a rescaling by S, and multiplication by 2^(2b+4) S, the values are rounded to integers, mapped back by the inverse address map, and carries are propagated to give the exact 2n-bit product. Rounding is exact because the error is below 1/2, a claim the page cites to another page that I did not open. Confidence is moderate: I could follow the stage-by-stage reductions and their size bookkeeping, but I took the error bounds and the cited lemmas on trust.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Grade": {
      "additionalProperties": false,
      "properties": {
        "contradicted": {
          "description": "Numbers of the key points the answer contradicts.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "covered": {
          "description": "Numbers of the key points the answer makes.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "label": {
          "description": "The answer's letter.",
          "type": "string"
        },
        "wrong": {
          "description": "Wrong claims in the answer that contradict no key point.",
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "required": [
        "label",
        "covered",
        "contradicted",
        "wrong"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "grades": {
      "items": {
        "$ref": "#/$defs/Grade"
      },
      "type": "array"
    }
  },
  "required": [
    "grades"
  ],
  "title": "GradeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0349-grade-g4.answer.json`, then run `exegenius submit 0349-grade-g4` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0349-grade-g4`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
