from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_extract_persons_contract(monkeypatch):
    async def mock_extract_persons_with_campusai(text: str) -> list[str]:
        assert text == "Einstein and von Neumann meet each other."
        return ["Einstein", "von Neumann"]
    monkeypatch.setattr("app.extract_persons_with_campusai", mock_extract_persons_with_campusai)
    payload = {"text": "Einstein and von Neumann meet each other."}
    response = client.post("/v1/extract-persons", json=payload)
    assert response.json() == {"persons": ["Einstein", "von Neumann"]}
    assert response.status_code == 200

def test_extract_persons_contract_minus_titles(monkeypatch):
    async def mock_extract_persons_with_campusai(text: str) -> list[str]:
        assert text == "Ms Mette Frederiksen is in New York today."
        return ["Mette Frederiksen"]
    monkeypatch.setattr("app.extract_persons_with_campusai", mock_extract_persons_with_campusai)
    payload = {"text": "Ms Mette Frederiksen is in New York today."}
    response = client.post("/v1/extract-persons", json=payload)
    assert response.json() == {"persons": ["Mette Frederiksen"]}
    assert response.status_code == 200

def test_missing_text_is_rejected():
    payload = {}
    response = client.post("/v1/extract-persons", json=payload)
    assert response.status_code == 422

def test_missing_api_key(monkeypatch):
    monkeypatch.delenv("CAMPUSAI_API_KEY", raising=False)
    payload = {"text": "Einstein"}
    response = client.post("/v1/extract-persons", json=payload)

    assert response.status_code == 503
    assert response.json() == {
        "detail": "CampusAI API key is not configured"
    }