# exegenius task 0001-extract

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Decompose the source documents into the concepts a specific reader must understand to reach a target result. Your answer is a prerequisite graph that becomes a wiki with one explanatory page per concept the reader does not already know.

- Make one concept per idea that deserves its own explanatory page. Fold minor terms into the gloss of the concept that uses them instead of giving them their own concept.
- Cover everything the target depends on in the sources, including named techniques, constructions, lemmas and notation-heavy objects. Leave out material the target does not depend on.
- `requires` lists the concepts a reader must understand before this one. Use only ids that appear in your answer. The graph must have no cycles.
- Mark `known: true` for concepts the reader profile already covers. Include known concepts that other concepts require, so prerequisites bottom out in what the reader knows, and give known concepts `requires: []`.
- `evidence` quotes must be copied from the sources character for character (a phrase or one sentence), with the id of the source they come from. Submit rejects any quote it cannot find in that source (it ignores differences in whitespace and in typographic quotes and dashes). Every concept the reader does not know needs at least one quote; known concepts may have none.
- `target` is the id of the concept for the target result.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Concept": {
      "additionalProperties": false,
      "description": "One concept. This is also the shape of a concept in an extract answer, so the field\ndocs double as instructions in the task file.",
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations the sources use for this concept.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "evidence": {
          "description": "Short quotes copied exactly from the sources that state or use this concept.",
          "items": {
            "$ref": "#/$defs/Evidence"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what the concept is.",
          "type": "string"
        },
        "id": {
          "description": "Lowercase slug, unique across the graph, e.g. \"chirp-identity\".",
          "type": "string"
        },
        "known": {
          "description": "True if the reader profile already covers this concept.",
          "type": "boolean"
        },
        "name": {
          "description": "Display name, e.g. \"Chirp identity\".",
          "type": "string"
        },
        "requires": {
          "description": "Ids of the concepts a reader must understand before this one.",
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "required": [
        "id",
        "name",
        "aliases",
        "gloss",
        "requires",
        "known",
        "evidence"
      ],
      "type": "object"
    },
    "Evidence": {
      "additionalProperties": false,
      "properties": {
        "quote": {
          "description": "Text copied character for character from that source.",
          "type": "string"
        },
        "source": {
          "description": "Id of the source the quote comes from.",
          "type": "string"
        }
      },
      "required": [
        "source",
        "quote"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "concepts": {
      "items": {
        "$ref": "#/$defs/Concept"
      },
      "type": "array"
    },
    "target": {
      "description": "Id of the concept that is the target result.",
      "type": "string"
    }
  },
  "required": [
    "target",
    "concepts"
  ],
  "title": "ExtractAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0001-extract.answer.json`, then run `exegenius submit 0001-extract` in the project directory. If submit rejects the answer, fix the answer file and submit again.
