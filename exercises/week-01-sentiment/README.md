# Week 1 Sentiment Service

## What it does

This project is a FastAPI REST service that scores Danish and English course-evaluation text. It accepts text at the `/v1/sentiment` endpoint and returns a sentiment score between `-5` and `5`.

The current implementation uses keyword matching. It recognizes a small set of positive and negative words and returns `3`, `-3`, or `0` for positive, negative, or unrecognized text.

## Requirements

- Python 3.11 or later
- [uv](https://docs.astral.sh/uv/)
- Docker or Podman

## Run the tests

Install the project and development dependencies, then run the test suite:

```sh
uv sync
uv run pytest
```

The tests cover the required positive, negative and dry course-evaluation examples, as well as validation for a missing `text` field.

## Run locally

Start the FastAPI development server:

```sh
uv run uvicorn main:app --reload
```

The interactive Swagger documentation is available at <http://127.0.0.1:8000/docs>.

Test the service from another terminal:

```sh
curl -X POST http://127.0.0.1:8000/v1/sentiment \
	-H 'Content-Type: application/json' \
	-d '{"text":"It was a good course"}'
```

Expected response:

```json
{"score": 3}
```

## Run with Docker

Build the image and start a container:

```sh
docker build -t sentiment-api .
docker run --rm -p 8000:8000 sentiment-api
```

The container serves the same Swagger documentation and API endpoint on port 8000. Stop it with `Ctrl+C`.

## API example

The service accepts a JSON object with a required `text` field at `POST /v1/sentiment`:

```json
{"text":"Det var en god lærer."}
```

It returns a JSON object containing the score:

```json
{"score": 3}
```

## Limitations

This is a small educational baseline, not a trained sentiment-analysis model. Its result depends on a limited keyword list, so it cannot reliably understand context, negation, irony or language outside the words it recognizes.
