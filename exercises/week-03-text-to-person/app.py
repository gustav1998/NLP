from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import httpx

CAMPUSAI_API_URL = "https://api.campusai.compute.dtu.dk/v1"
CAMPUSAI_MODEL = "cai-mini"

app = FastAPI()

class TextInput(BaseModel):
    text: str

class PersonsOutput(BaseModel):
    persons: list[str]


async def extract_persons_with_campusai(text: str) -> list[str]:
    api_key = os.environ.get("CAMPUSAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=503, detail="CampusAI API key is not configured")
    endpoint = f"{CAMPUSAI_API_URL}/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    request_body = {
                        "model": CAMPUSAI_MODEL,
                        "messages": [
                            {
                                "role": "system",
                                "content": "Extract person names from the user's text. Exclude titles such as Ms. Return only valid JSON with a persons list.",
                            },
                            {
                                "role": "user",
                                "content": text,
                            },
                        ],
                        "response_format": {"type": "json_object"},
                    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint,
                headers=headers,
                json=request_body,
                timeout=60,
            )
            response.raise_for_status()
    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=502,
            detail="CampusAI request failed",
        ) from error
    response_data = response.json()
    content = response_data["choices"][0]["message"]["content"]
    parsed_output = PersonsOutput.model_validate_json(content)
    return parsed_output.persons

@app.post("/v1/extract-persons")
async def extract_persons(payload: TextInput) -> dict[str, list[str]]:
    return {"persons": await extract_persons_with_campusai(payload.text)}
