from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import requests 
from openai import OpenAI


app = FastAPI()
# OpenAI client
client = OpenAI(
    api_key="YOUR_OPENAI_KEY"
)


@app.get("/")
async def root():
    return {"status": "ok"}

class WeatherRequest(BaseModel):
    city: str


@app.post("/weather")
async def weather(req: WeatherRequest):

    async with httpx.AsyncClient() as client:

        r = await client.get(
            f"https://wttr.in/{req.city}?format=j1"
        )

        data = r.json()

    return {
        "city": req.city,
        "temp": data["current_condition"][0]["temp_C"]
    }
class PoemRequest(BaseModel):
    poet: str
    topic: str

@app.post("/poem")
async def make_poem(req: PoemRequest):

    prompt = (
        f"Write a short poem about "
        f"{req.topic} "
        f"in style of {req.poet}"
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    poem = response.choices[0].message.content

    return {
        "poem": poem
    }

