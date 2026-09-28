from pathlib import Path
import pytest

from fastapi.testclient import TestClient

from main import app, clean_text

client = TestClient(app)
PDF_PATH = (
    Path(__file__).resolve().parents[2]
    / "course-material/official/week-02/2303.15133.pdf"
)

def test_clean_text_joins_broken_word():
    text = "dis-\nplay"
    assert clean_text(text) == "display"

def test_clean_text_preserves_word_spacing():
    text = "the\ncourse"
    assert clean_text(text) == "the course"

@pytest.mark.xfail(reason= "the current rule cannot distinguish genuine hyphens from layout hyphenation.")
def test_clean_text_preserves_genuine_hyphen():
    text = "work-in-\nprogress"
    assert clean_text(text) == "work-in-progress"

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