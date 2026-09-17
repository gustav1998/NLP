# Week 3 Text-to-person

## Status

Starter folder prepared from the official specification in `course-material/official/week-03/text-to-persons.md`.

## Confirmed course topics

- Prompt engineering
- LLM APIs
- CampusAI
- Entity recognition

The exercise asks for a REST service that extracts person names from text, using CampusAI or another justified approach.

## Exercise contract

- Run a Python Web service in a Docker or Podman container.
- Listen on container port `8000`.
- Provide `POST /v1/extract-persons`.
- Accept JSON with a required `text` field.
- Return JSON with a `persons` field containing a list of names from the text.
- Do not include an API key in the hand-in.
- Include a `Dockerfile` at the Week 3 exercise-folder root for the hand-in archive.

Example request:

```sh
curl -s -X POST http://localhost:8000/v1/extract-persons \
	-H 'Content-Type: application/json' \
	-d '{"text":"Einstein and von Neumann meet each other."}'
```

Expected response:

```json
{"persons": ["Einstein", "von Neumann"]}
```

The supplied examples also expect:

```text
Ms Mette Frederiksen is in New York today.
-> ["Mette Frederiksen"]

Einstein and von Neumann meet each other.
-> ["Einstein", "von Neumann"]
```

## Runtime configuration

The official specification gives these runtime settings:

```text
CAMPUSAI_API_KEY=<local secret>
CAMPUSAI_MODEL=google/gemma-4-26b-a4b
CAMPUSAI_EMBED_MODEL=cai-embedding
CAMPUSAI_API_URL=https://api.campusai.compute.dtu.dk/v1
```

Keep the real key in a local environment file and pass it at runtime with `--env-file`. Never commit it.

## Reading

- NLP notes, Chapter 7: Prompt engineering, printed pages 59-63
- NLP notes, section 8.3: LLM APIs, printed pages 86-88
- NLP notes: CampusAI examples, especially printed pages 15 and 63
- Knowledge Graphs notes, section 8.2: Entity recognition, printed pages 79-80

## Before implementation

Decide and document:

- Whether to call CampusAI through an OpenAI-compatible client or directly over HTTP
- The prompt and output format used to request person names
- How malformed model output and API errors are handled
- Focused tests for the supplied examples
- How asynchronous requests and timeouts are handled

Keep API keys in a local `.env` file. Never commit real keys.

## Next small step

Create the smallest FastAPI endpoint with the confirmed request and response shape. Add the CampusAI call only after the local contract test is clear.
