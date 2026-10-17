# exegenius task 0345-baseline-g9-reader

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Answer a question as a reader with exactly the background stated below, with no access to any other material. This answer is the baseline that answers written with the help of a wiki are compared against.

- Use only what that background covers. Everything else you know, the reader does not.
- Some names in the question may be invented: do not guess what they stand for.
- Use no tools except to write your answer file and run `exegenius submit`: do not open files, search the web, or start sessions or agents. If the background does not let the reader answer, say so plainly instead of guessing.

## The reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## The question

Summarise in a few sentences how the algorithm turns two n-bit integers into their exact product, naming the main stages in order and saying why the final answer is exact rather than approximate.

## Answer

The answer is one JSON object following this schema:

```json
{
  "additionalProperties": false,
  "properties": {
    "answer": {
      "description": "The answer, or a plain statement that the background does not cover it.",
      "type": "string"
    }
  },
  "required": [
    "answer"
  ],
  "title": "BaselineAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0345-baseline-g9-reader.answer.json`, then run `exegenius submit 0345-baseline-g9-reader` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0345-baseline-g9-reader`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
