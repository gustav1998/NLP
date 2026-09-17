# Week 2 PDF-to-sentences service

This project is a FastAPI service that accepts a PDF upload and returns the extracted text split into sentences.

## Requirements

- Python 3.11 or later
- uv
- Docker or Podman

## Run the tests

Install the project and development dependencies, then run the test suite:

```sh
uv sync
uv run pytest
```

The test uploads `2303.15133.pdf` and checks that the response contains the required sentence:
`How language should best be handled is not clear.`

## Run locally

Start the API on port 8000:

```sh
uv run uvicorn main:app --reload
```

If port 8000 is already in use, choose another host port:

```sh
uv run uvicorn main:app --reload --port 8001
```

Upload a PDF from a second terminal:

```sh
curl -X POST http://127.0.0.1:8000/v1/extract-sentences \
	-F "pdf_file=@../../course-material/official/week-02/2303.15133.pdf"
```

The service returns JSON in this form:

```json
{"sentences": ["First sentence.", "Second sentence."]}
```

The interactive API documentation is available at `/docs`.

## Run with Docker

Build and start the service:

```sh
docker build -t week-02-pdf-to-sentences .
docker run --rm -p 8000:8000 week-02-pdf-to-sentences
```

Then use the same `curl` request shown above. The container listens on port 8000.

## Implementation

The service reads uploaded PDF bytes with PyMuPDF and uses NLTK sentence tokenization. No external Web service is used.

## Limitations

The current implementation extracts all text in reading order. It does not yet identify and remove headers, footers, references or other non-body content from every possible PDF layout. PDFs without a text layer may require OCR, which is outside this implementation.
