# exegenius task 0419-grade-g4

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

The chain turns the integer product into a short-coefficient convolution, moves it onto axes of prime length, replaces each prime-length transform by a power-of-two one (resampling plus chirp), runs the power-of-two convolution as a ring convolution whose transforms need only signed shifts, and finally rounds the result back to exact integers. Stage by stage. (1) Radix digits: each n-bit integer is cut into q = ceil(n/b) digits of b = ceil(log2 n) bits. The product then becomes a convolution of length S whose coefficients c_j are short integers below 2^(3b), and S is chosen so that nothing wraps around. This is needed because it makes the final rounding step able to recover exact integers. (2) Address map: S is a product of distinct odd primes. The map Phi rewrites the length-S convolution as one on d axes of pairwise coprime prime lengths s_i, because a transform of length S has no power-of-two structure while coprime axes split into short one-axis transforms. (3) Resampling and chirps: each prime-length transform F_s is re-expressed through a nearby larger power-of-two transform F_t, using an input map A and an output map B_0, so that only power-of-two transforms need a fast algorithm. The permutations are never executed as sorts. The target permutation Q of F_t is absorbed by the chirp identity Q F_t u = conj(a) times (a convolved with (conj(a) times u)) divided by T, which turns it into one convolution of length T between two phase multiplications. (4) Twist: the convolution over complex arrays is moved onto the ring C[y]/(y^r+1) by the map x_d to zeta*y with zeta = e^(pi i/r). The wrap of the last cyclic axis then becomes a sign, which is repaired by a phase. This is needed because in that ring multiplication by a root of unity (a power of y) is a signed shift of the coefficient list, so transforms over the ring need no complex multiplications. (5) Synthetic-transform convolution: forward synthetic transforms over the ring on the remaining axes, a pointwise record product, and the opposite transform give f*g/T. The forward output is left in bit-reversed order and the opposite transform takes that order as input, so no reordering is run. (6) Assembly: apply Phi to the two digit arrays, apply the resampling-and-chirp transform to each, multiply the results pointwise and truncate, apply the opposite transform, scale by S and by 2^(2b+4)S, round to the nearest integers, apply Phi inverse, and propagate radix-2^b carries to get the exact 2n-bit product. The rounding step is licensed by an error bound below 1/2, which I took from the page without opening the page that proves it. Confidence is moderate: the chain of reductions is consistent across the pages I opened, but the resampling identity was imported without proof and I did not check the scale factors beyond the arithmetic shown.

### Answer B

The chain has five stages. Each stage turns the problem into one that the next stage can use.

1. Radix digits (Multiplication as radix-digit convolution). Write each n-bit input in radix 2^b, with b = ceil(log2 n) and q = ceil(n/b) digits. The product of the two digit polynomials is a Cyclic convolution of length S with integer coefficients below 2^(3b), and its degree is below S, so nothing wraps. The integer product is thereby reduced to one Cyclic convolution of length S on small integers. Later stages only have to compute that Cyclic convolution, and an approximation with error below 1/2 rounds to the exact coefficients.

2. Address map (Chinese-remainder address map). S is a product of pairwise coprime lengths s_1, ..., s_d (distinct odd primes). The map x to the product of x_i^(mu_i), where mu_i is the inverse of P_i modulo s_i, is an isomorphism that preserves Cyclic convolution. It sends the length-S Cyclic convolution to a Cyclic convolution on d separate cyclic axes of lengths s_i. This is needed because a transform of length S has no power-of-two structure, whereas over coprime axes each one-axis transform can be treated on its own, one axis at a time.

3. Resampling with chirps (Gaussian resampling, Bluestein chirp identity, Retained permutation cancellation). Each prime-length transform F_s is rewritten through a power-of-two transform F_t, with t somewhat larger than s: P_s F_s = 2^(2 alpha^2) B_0 P_t F_t A, where A and B_0 are contractions (A resamples the input, B_0 the output). The permutations P_s and P_t are never executed, because a sort would cost a log factor that cancels the power saving. The remaining target permutation Q inside P_t F_t is absorbed by the chirp identity Q F_t u = conj(a) . (a * (conj(a) . u)) / T, with a_j = exp(-pi i sum_i s_i j_i^2 / t_i). So Q becomes one Cyclic convolution of length T between two pointwise phase multiplications. The retained source permutation R cancels across the two forward transforms, their pointwise product and the opposite transform: (R F_s^+)[(R F_s u) . (R F_s v)] = u*v/S^2, with no sort. This is needed because the next stage computes Cyclic convolutions over axes whose lengths are powers of two.

4. Twist to the polynomial ring (Phase twist). The last cyclic axis, of length r, is mapped to the coordinate y of the ring C[y]/(y^r+1) by x_d -> zeta*y, with zeta = e^(pi i/r). This is a diagonal phase that multiplies coefficient k by zeta^k, and it is undone at the end. The phase cancels the sign that the wrap would otherwise introduce, so the Cyclic convolution on that axis is reproduced. This is needed because the transforms over that ring (Synthetic polynomial transform) have roots of unity that are powers of y, so every twiddle multiplication is a signed shift of coefficients.

5. Synthetic-transform convolution (Convolution from the retained transform layout). On the remaining d-1 axes, the normalized Cyclic convolution over the ring is computed from two forward synthetic transforms, record-by-record products and an opposite transform, with the transform layout kept so that no reordering is executed. Undoing the twist gives the normalized complex Cyclic convolution f*g/T. The algorithm then multiplies by S, multiplies by 2^(2b+4)S, rounds to integers, and propagates radix-2^b carries to output the exact 2n-bit product.

I checked the wiki's own worked examples by hand: the q = 2 transform example on the Discrete Fourier transform page, the d = 1 chirp example on the Bluestein chirp identity page, the r = 2 twist example on the Phase twist page, and the s = (3,5) address-map example on the Chinese-remainder address map page.

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

Write the answer to `exegenius/tasks/0419-grade-g4.answer.json`, then run `exegenius submit 0419-grade-g4` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0419-grade-g4`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
