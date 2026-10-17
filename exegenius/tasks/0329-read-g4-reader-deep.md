# exegenius task 0329-read-g4-reader-deep

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Simulate a reader using a wiki to answer a question. The point is to find out whether the wiki gets this reader there, so behave like this reader, not like an expert.

- The reader knows exactly the background stated below. Everything else you know, the reader does not. When a page relies on something outside that background, the reader has to find it in the wiki: follow a link, search, or go back to an earlier page.
- The wiki may give the concepts it teaches invented names. Treat them as new words: do not guess which real terms they stand for, and do not use real names for them in your answer.
- See the wiki only through the two commands below. Use no other tools except to write your answer file and run `exegenius submit`: do not open files, search the web, or start sessions or agents.
- Record every place you got stuck: the page, a short quote copied from it, what you could not follow, and its level: a symbol or term you could not decode, a statement whose status you could not tell, a single step you could not follow, a chain whose steps you followed without seeing why they lead where they do, or something you could not connect to anything you know. Include places you got past only by guessing.
- Answer from the pages alone. Support each step of the answer with a quote copied exactly from a page you opened. If the pages do not get you to an answer within the page budget, give up and say where it broke down.
- If you answer, also name the key idea of the page you relied on most: say it in a sentence, and quote the passage of the page that carries it.
- An honest `gave_up` is worth more than a fluent answer the pages do not support.

## The reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## The question

Explain how the algorithm turns a product of two integers into transforms of power-of-two length, in order: what each stage in the chain (radix digits, address map, resampling with chirps, twist to the polynomial ring, synthetic-transform convolution) accomplishes and why it is needed for the next stage.

## Reading the wiki

You arrive on a page deep inside the wiki, as if from a search engine. Run these in the project directory:

- `exegenius read 0329-read-g4-reader-deep siz` opens the first page. `exegenius read 0329-read-g4-reader-deep <page>` opens any page by its handle: links look like `[text](handle)`, and `home` is the front page.
- `exegenius search 0329-read-g4-reader-deep <words>` lists pages containing all the words.

You may open at most 15 pages (opening a page again counts). Everything you open is logged.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Citation": {
      "additionalProperties": false,
      "properties": {
        "page": {
          "description": "Handle of a page you opened.",
          "type": "string"
        },
        "quote": {
          "description": "Text copied exactly from that page.",
          "type": "string"
        }
      },
      "required": [
        "page",
        "quote"
      ],
      "type": "object"
    },
    "KeyIdeaAnswer": {
      "additionalProperties": false,
      "properties": {
        "page": {
          "description": "Handle of the page you relied on most.",
          "type": "string"
        },
        "quote": {
          "description": "The passage of the page that carries it, copied exactly.",
          "type": "string"
        },
        "statement": {
          "description": "The key idea of that page, in one sentence of your own.",
          "type": "string"
        }
      },
      "required": [
        "page",
        "statement",
        "quote"
      ],
      "type": "object"
    },
    "Level": {
      "description": "Where understanding broke down, from Spratte's levels of proof comprehension.",
      "oneOf": [
        {
          "const": "symbol",
          "description": "A symbol or term I could not decode.",
          "type": "string"
        },
        {
          "const": "statement",
          "description": "I could not tell what a statement's status was: definition, assumption or claim.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "I could not follow one inference.",
          "type": "string"
        },
        {
          "const": "chain",
          "description": "I followed the steps but not why they lead where they do.",
          "type": "string"
        },
        {
          "const": "beyond",
          "description": "I could not connect it to anything I already know.",
          "type": "string"
        }
      ]
    },
    "Outcome": {
      "enum": [
        "answered",
        "gave_up"
      ],
      "type": "string"
    },
    "Stuck": {
      "additionalProperties": false,
      "properties": {
        "level": {
          "$ref": "#/$defs/Level"
        },
        "note": {
          "description": "What you could not follow.",
          "type": "string"
        },
        "page": {
          "description": "Handle of the page where you got stuck.",
          "type": "string"
        },
        "quote": {
          "description": "Text copied exactly from that page, where the trouble starts.",
          "type": "string"
        }
      },
      "required": [
        "page",
        "quote",
        "note",
        "level"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "answer": {
      "description": "The answer to the question; empty if you gave up.",
      "type": "string"
    },
    "citations": {
      "description": "Quotes supporting the answer.",
      "items": {
        "$ref": "#/$defs/Citation"
      },
      "type": "array"
    },
    "key_idea": {
      "anyOf": [
        {
          "$ref": "#/$defs/KeyIdeaAnswer"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "If you answered: the key idea of the page you relied on most."
    },
    "outcome": {
      "$ref": "#/$defs/Outcome"
    },
    "reason": {
      "description": "Why you gave up, or how sure you are of the answer.",
      "type": "string"
    },
    "stuck": {
      "description": "Every place you got stuck.",
      "items": {
        "$ref": "#/$defs/Stuck"
      },
      "type": "array"
    }
  },
  "required": [
    "outcome",
    "answer",
    "citations",
    "stuck",
    "reason"
  ],
  "title": "ReadAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0329-read-g4-reader-deep.answer.json`, then run `exegenius submit 0329-read-g4-reader-deep` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0329-read-g4-reader-deep`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
