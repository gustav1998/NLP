# Week 2 PDF-to-sentences service

This project is a FastAPI service that accepts a PDF upload and returns sentences extracted from the document body by GROBID.

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

Start GROBID first:

```sh
docker compose up -d grobid
```

Then start the API on port 8000:

```sh
uv run uvicorn main:app --reload
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

## Run with Docker Compose

Build and start both the API and GROBID:

```sh
docker compose up --build
```

The API is available at `http://127.0.0.1:8000`, and GROBID is exposed locally at `http://127.0.0.1:8070`. The two containers communicate over the private Compose network. Then use the same `curl` request shown above.

Stop and remove the containers and Compose network with:

```sh
docker compose down
```

On Apple Silicon with Colima, GROBID needed an 8 GiB virtual-machine memory allocation in this setup:

```sh
colima stop
colima start --memory 8 --cpu 4
```

## Implementation

The FastAPI service sends uploaded PDF bytes asynchronously to the GROBID container. GROBID returns TEI XML with sentence elements from the document body. The API parses those elements, normalizes whitespace and returns the sentences as JSON. All processing uses services in the local Compose setup; no external Web service is used.

## Limitations

PDF extraction depends on document structure and GROBID's models. Complex layouts, lists, URLs, genuine hyphens and layout hyphenation may produce imperfect sentence text. PDFs without a usable text layer may require OCR, which is outside this exercise.
