from fastapi import FastAPI
from pydantic import BaseModel
import httpx
import os
import requests 
from openai import OpenAI


app = FastAPI()
# OpenAI client
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    timeout=20.0    
)


@app.get("/")
async def root():
    return {"status": "ok"}

class WeatherRequest(BaseModel):
    city: str


@app.post("/weather")
async def weather(req: WeatherRequest):
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:

            r = await client.get(
                f"https://wttr.in/{req.city}?format=j1"
            )
        r.raise_for_status()
        data = r.json()
        return {
           "city": req.city,
           "temp": data["current_condition"][0]["temp_C"]
        }
    except Exception as e:
        return {
            "error": str(e)
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
    try:
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
    except Exception as e:
        return {
            "error": str(e)
        }
