from fastapi import FastAPI, File, UploadFile
from pathlib import Path

from nltk.tokenize import sent_tokenize
import pymupdf

app = FastAPI()


def sentences_from_pdf(contents: bytes) -> list[str]:
    document = pymupdf.open(stream=contents, filetype="pdf")
    text = "\n".join(page.get_text() for page in document)
    normalized_text = " ".join(text.split())
    return sent_tokenize(normalized_text, language="english")


@app.post("/v1/extract-sentences")
async def extract_sentences(pdf_file: UploadFile = File(...)):
    contents = await pdf_file.read()
    return {"sentences": sentences_from_pdf(contents)}


if __name__ == "__main__":
    pdf_path = (
        Path(__file__).resolve().parents[2]
        / "course-material/official/week-02/studyboard.pdf"
    )

    with open(pdf_path, "rb") as pdf_file:
        for sentence in sentences_from_pdf(pdf_file.read()):
            print(repr(sentence))