from fastapi import FastAPI, File, UploadFile
from pathlib import Path
import os
import httpx
from xml.etree import ElementTree

from nltk.tokenize import sent_tokenize
import pymupdf

GROBID_URL = os.getenv("GROBID_URL", "http://127.0.0.1:8070")
app = FastAPI()

def clean_text(text: str) -> str:
    text = text.replace("-\n", "")
    normalized_text = " ".join(text.split())
    return normalized_text

async def body_sentences_from_grobid(contents: bytes) -> list[str]:
    endpoint = f"{GROBID_URL}/api/processFulltextDocument"
    files = {"input": ("document.pdf", contents, "application/pdf")}
    data = {"segmentSentences": "1"}
    async with httpx.AsyncClient() as client:
        response = await client.post(endpoint, files=files, data=data, timeout=120)
    response.raise_for_status()
    root = ElementTree.fromstring(response.content)
    namespace = {"tei": "http://www.tei-c.org/ns/1.0"}
    body = root.find(".//tei:text/tei:body", namespace)
    if body is None:
        return []
    sentence_elements = body.findall(".//tei:s", namespace)
    sentences = []
    for element in sentence_elements:
        sentence_text = "".join(element.itertext())
        sentences.append(sentence_text)
    sentences = [clean_text(sentence) for sentence in sentences]
    return sentences

def sentences_from_pdf(contents: bytes) -> list[str]:
    document = pymupdf.open(stream=contents, filetype="pdf")
    text = "\n".join(page.get_text() for page in document)
    normalized_text = clean_text(text)
    return sent_tokenize(normalized_text, language="english")


@app.post("/v1/extract-sentences")
async def extract_sentences(pdf_file: UploadFile = File(...)):
    contents = await pdf_file.read()
    return {"sentences": await body_sentences_from_grobid(contents)}


if __name__ == "__main__":
    pdf_path = (
        Path(__file__).resolve().parents[2]
        / "course-material/official/week-02/studyboard.pdf"
    )

    with open(pdf_path, "rb") as pdf_file:
        for sentence in sentences_from_pdf(pdf_file.read()):
            print(repr(sentence))