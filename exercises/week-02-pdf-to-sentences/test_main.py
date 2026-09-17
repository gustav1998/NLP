from pathlib import Path

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)
PDF_PATH = (
    Path(__file__).resolve().parents[2]
    / "course-material/official/week-02/2303.15133.pdf"
)


def test_extract_sentences():
    with PDF_PATH.open("rb") as pdf_file:
        response = client.post(
            "/v1/extract-sentences",
            files={"pdf_file": (PDF_PATH.name, pdf_file, "application/pdf")},
        )

    assert response.status_code == 200, response.text
    data = response.json()
    assert isinstance(data["sentences"], list)
    assert "How language should best be handled is not clear." in data["sentences"]